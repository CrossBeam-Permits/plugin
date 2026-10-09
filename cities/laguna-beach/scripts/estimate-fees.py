#!/usr/bin/env python3
"""Estimate Laguna Beach permit fees from requirements/fees/fee-data.json.

Every result is an ESTIMATE. The City has not confirmed the Building permit fee
formula, and it sets the final fee when it invoices the permit. The caller (the
agent) decides which fee lines apply from the project evidence; this script only
does the arithmetic for the lines it is given.

Examples:

    python3 scripts/estimate-fees.py --valuation 250000
    python3 scripts/estimate-fees.py --valuation 250000 --permits 2 --smip-residential \
        --line electrical_outlets=12 --line plumbing_water_heaters=1
    python3 scripts/estimate-fees.py --line reroof_permit --line reroof_plan_review
    python3 scripts/estimate-fees.py --planning design_review_admin --planning zoning_plan_check_small
    python3 scripts/estimate-fees.py --list
"""

from __future__ import annotations

import argparse
import json
import sys
from decimal import ROUND_HALF_EVEN, Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA = ROOT / "requirements" / "fees" / "fee-data.json"
CENT = Decimal("0.01")


def cents(value: Decimal) -> Decimal:
    return value.quantize(CENT, rounding=ROUND_HALF_EVEN)


def percent(value) -> str:
    return f"{float(value) * 100:g}%"


def dec(value) -> Decimal:
    return Decimal(str(value))


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        data = json.load(stream)
    if "ESTIMATE" not in data.get("estimate_notice", ""):
        raise SystemExit(f"{path} has no estimate notice; refusing to estimate from it")
    return data


def building_permit_fee(valuation: Decimal, table: dict) -> tuple[Decimal, dict]:
    """Row base plus the per-$1,000 rate on the valuation above the row floor, prorated."""
    if valuation <= 0:
        raise SystemExit("valuation must be more than $0")
    rows = table["rows"]
    row = next(
        (item for item in rows if item["up_to"] is None or valuation <= dec(item["up_to"])),
        rows[-1],
    )
    base = dec(row["base"])
    if row["per_additional_1000"] is None:
        return cents(base), row
    floor = dec(row["from"]) - 1
    over = max(Decimal(0), valuation - floor)
    return cents(base + dec(row["per_additional_1000"]) * over / 1000), row


def stepped(quantity: Decimal, rule: dict) -> Decimal:
    brackets = rule["brackets"]
    chosen = brackets[-1]
    for bracket in brackets:
        upper = bracket.get("up_to")
        if upper is None or quantity <= dec(upper):
            chosen = bracket
            break
    amount = dec(chosen["base"])
    if dec(chosen.get("per", 0)) and dec(chosen.get("unit", 0)):
        over = max(Decimal(0), quantity - dec(chosen["floor"]))
        units = (over / dec(chosen["unit"])).to_integral_value(rounding="ROUND_CEILING")
        amount += units * dec(chosen["per"])
    return cents(amount * dec(rule.get("multiplier", 1)))


def per_unit(quantity: Decimal, rule: dict) -> Decimal | None:
    if "min_input" in rule and quantity < dec(rule["min_input"]):
        return None
    counted = max(Decimal(0), quantity - dec(rule.get("offset", 0)))
    amount = counted * dec(rule["rate"])
    if "minimum" in rule:
        amount = max(amount, dec(rule["minimum"]))
    return cents(amount)


def line_amount(line: dict, quantity: Decimal | None, valuation: Decimal | None) -> tuple[Decimal | None, str | None]:
    """Return (amount, note). A None amount means the script cannot estimate the line."""
    rule = line.get("rule")
    if rule is None:
        if "amount" in line:
            count = quantity if quantity is not None else Decimal(1)
            return cents(dec(line["amount"]) * count), None
        return None, "No amount is published for this line; confirm with the City."
    kind = rule.get("type")
    if kind == "per_unit":
        if quantity is None:
            return None, f"Needs a quantity ({rule.get('input', 'count')}): pass --line {line['id']}=N"
        amount = per_unit(quantity, rule)
        return amount, None if amount is not None else "Below the City's minimum quantity for this line."
    if kind == "stepped":
        source = valuation if rule.get("input") == "valuation" else quantity
        if source is None:
            return None, f"Needs {rule.get('input', 'a quantity')}: pass --line {line['id']}=N or --valuation"
        return stepped(source, rule), None
    if kind == "percent_of_valuation":
        if valuation is None:
            return None, "Needs --valuation."
        return cents(valuation * dec(rule["pct"])), None
    return None, "This line depends on other City-computed amounts; confirm with the City."


def parse_line(text: str) -> tuple[str, Decimal | None]:
    if "=" in text:
        key, value = text.split("=", 1)
        return key.strip(), dec(value.strip())
    return text.strip(), None


def estimate(data: dict, args: argparse.Namespace) -> dict:
    result: dict = {
        "estimate_notice": data["estimate_notice"],
        "source": data["source"],
        "effective_from": data["effective_from"],
        "lines": [],
        "not_estimated": [],
    }
    table = data["building_valuation_fee"]
    surcharges = {item["id"]: item for item in table["surcharges"]}

    def add(label: str, amount: Decimal, cite: str | None, paid_to: str | None = None, note: str | None = None) -> None:
        result["lines"].append(
            {"label": label, "amount": str(cents(amount)), "cite": cite, "paid_to": paid_to, "note": note}
        )

    valuation = dec(args.valuation) if args.valuation is not None else None
    if valuation is not None:
        permit, row = building_permit_fee(valuation, table)
        plan_review = cents(permit * dec(table["plan_review_pct"]))
        add(f"Building permit fee (valuation ${valuation:,.0f}, row {row['row']}: {row['city_text']})", permit, table["cite"],
            note="Formula not confirmed by the City.")
        add("Plan review (65% of the permit fee)", plan_review, table["plan_review_cite"])
        if args.combination_trades:
            trades = cents(permit * dec(table["combination_trades_pct"]))
            add("Combination mechanical, electrical, plumbing (new construction)", trades, table["combination_trades_cite"])
        for surcharge in table["surcharges"]:
            add(f"{surcharge['label']} ({percent(surcharge['pct'])} of permit and plan review)",
                cents((permit + plan_review) * dec(surcharge["pct"])), surcharge.get("cite"))
        if args.smip_residential:
            rate = dec(data["statewide"]["smip_residential_rate"])
            add("Strong motion instrumentation (state fee, residential under 3 stories)", cents(valuation * rate),
                data["statewide"].get("smip_cite"), paid_to="State of California")

    if valuation is not None or args.line:
        issuance = table["issuance"]
        count = max(1, args.permits)
        add(f"Permit issuance ({count} permit{'s' if count > 1 else ''})",
            dec(issuance["first"]) + dec(issuance["each_additional"]) * (count - 1), issuance["cite"])

    lines_by_id = {line["id"]: line for line in data["scope_addons"] + data["deposits"]}
    for text in args.line:
        line_id, quantity = parse_line(text)
        line = lines_by_id.get(line_id)
        if line is None:
            raise SystemExit(f"unknown fee line: {line_id} (use --list)")
        amount, note = line_amount(line, quantity, valuation)
        if amount is None:
            result["not_estimated"].append({"id": line_id, "label": line["label"], "reason": note, "cite": line.get("cite")})
            continue
        label = line["label"] + (f" ({quantity:,f})" if quantity is not None else "")
        if line.get("kind") == "actual_cost_deposit" or "deposit" in line_id:
            label += " (deposit)"
        add(label, amount, line.get("cite"), line.get("paid_to"), line.get("applies_when"))
        for surcharge_id in line.get("surcharges", []):
            surcharge = surcharges.get(surcharge_id)
            if surcharge:
                add(f"{surcharge['label']} on {line['label']}", cents(amount * dec(surcharge["pct"])), surcharge.get("cite"))

    planning = data["planning"]
    planning_lines = {line["id"]: line for line in planning["flat"] + planning["deposits"] + planning["variable"]}
    gaps = {line["id"]: line for line in planning["not_in_schedule"]}
    for line_id in args.planning:
        if line_id in gaps:
            result["not_estimated"].append({"id": line_id, "label": gaps[line_id]["label"], "reason": gaps[line_id].get("note"), "cite": gaps[line_id].get("cite")})
            continue
        line = planning_lines.get(line_id)
        if line is None:
            raise SystemExit(f"unknown Planning fee line: {line_id} (use --list)")
        if "amount" in line:
            add(line["label"], dec(line["amount"]), line.get("cite"), "City of Laguna Beach Planning")
        elif "min" in line:
            add(f"{line['label']} (minimum deposit; actual cost billed)", dec(line["min"]), line.get("cite"), "City of Laguna Beach Planning", line.get("note"))
        elif "base" in line:
            add(f"{line['label']} (base; more may be billed)", dec(line["base"]), line.get("cite"), "City of Laguna Beach Planning", line.get("note"))
        else:
            result["not_estimated"].append({"id": line_id, "label": line["label"], "reason": line.get("note"), "cite": line.get("cite")})

    if args.school_fee_sqft is not None:
        statewide = data["statewide"]
        rate_key = "school_fee_commercial_per_sqft" if args.school_fee_use == "commercial" else "school_fee_residential_per_sqft"
        add(f"School district developer fee ({args.school_fee_sqft} sq ft, {args.school_fee_use})",
            dec(statewide[rate_key]) * dec(args.school_fee_sqft), statewide.get("school_fee_cite"),
            statewide.get("school_fee_paid_to"), statewide.get("school_fee_applies_when"))

    total = sum((dec(line["amount"]) for line in result["lines"]), Decimal(0))
    result["total_estimate"] = str(cents(total))
    return result


def render(result: dict) -> str:
    out = [f"**{result['estimate_notice']}**", "", "| Fee | Estimate | Source |", "|---|---:|---|"]
    for line in result["lines"]:
        out.append(f"| {line['label']} | ${dec(line['amount']):,.2f} | {line['cite'] or ''} |")
    out.append(f"| **Total estimate** | **${dec(result['total_estimate']):,.2f}** | |")
    if result["not_estimated"]:
        out += ["", "Not estimated:"]
        out += [f"- {item['label']}: {item['reason']}" for item in result["not_estimated"]]
    out += ["", f"Source: {result['source']['title']}, effective {result['effective_from']}. {result['source'].get('url') or ''}",
            "", f"**{result['estimate_notice']}**"]
    return "\n".join(out)


def list_lines(data: dict) -> str:
    out = [data["estimate_notice"], "", "Building and other fee lines (--line ID or ID=QUANTITY):"]
    for line in data["scope_addons"] + data["deposits"]:
        out.append(f"  {line['id']}: {line['label']}")
    out.append("")
    out.append("Planning fee lines (--planning ID):")
    planning = data["planning"]
    for line in planning["flat"] + planning["deposits"] + planning["variable"] + planning["not_in_schedule"]:
        out.append(f"  {line['id']}: {line['label']}")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Laguna Beach fee ESTIMATE (not confirmed by the City)")
    parser.add_argument("--data", default=str(DEFAULT_DATA))
    parser.add_argument("--valuation", type=float, help="Building valuation in dollars for one permit")
    parser.add_argument("--permits", type=int, default=1, help="number of permits issued (issuance fee)")
    parser.add_argument("--combination-trades", action="store_true", help="new construction combination MEP permit (10%%)")
    parser.add_argument("--smip-residential", action="store_true", help="add the state SMIP fee for residential under 3 stories")
    parser.add_argument("--line", action="append", default=[], help="Building fee line id, or id=quantity")
    parser.add_argument("--planning", action="append", default=[], help="Planning fee line id")
    parser.add_argument("--school-fee-sqft", type=float, help="assessable new floor area for the school district fee")
    parser.add_argument("--school-fee-use", choices=["residential", "commercial"], default="residential")
    parser.add_argument("--json", help="also write the estimate as JSON to this path")
    parser.add_argument("--list", action="store_true", help="list the fee line ids and exit")
    args = parser.parse_args(argv)

    data = load(Path(args.data))
    if args.list:
        print(list_lines(data))
        return 0
    if args.valuation is None and not args.line and not args.planning and args.school_fee_sqft is None:
        parser.error("give --valuation, --line, --planning or --school-fee-sqft")
    result = estimate(data, args)
    if args.json:
        Path(args.json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.json).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(render(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
