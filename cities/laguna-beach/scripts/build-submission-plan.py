#!/usr/bin/env python3
"""Compile confirmed records and packets into exact EnerGov transactions.

Each online record becomes one transaction that names the portal record type
(catalog menu id) AND the work class. The agent chooses the work class by
reasoning from the project facts and writes that choice, with its reasons, to
``work-class-selection.json``. This script never picks a work class. It checks
the choice against the pinned v2 portal map and blocks the record when the
class, its layout, or its attachment rules are not in the map.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _lib import confirmed_fact_value, fact_index, load_json, plugin_root, sha256_file, utc_now, write_json  # noqa: E402
from _portal import MAP_SCHEMA_VERSION, attachments_for, contacts_for, layout_questions, record_type, work_class  # noqa: E402
from _schema import validate_instance  # noqa: E402

PLUGIN_ROOT = plugin_root()

ROLE_FACTS = {
    "Applicant": "applicant.name",
    "Owner": "owner.name",
    "Contractor": "contractor.name",
    "Architect": "designer.architect.name",
    "Designer": "designer.name",
    "Engineer": "designer.engineer.name",
}

NEXT_ACTION = {
    "review_first": (
        "City completeness screen; staff generally contacts the applicant in 2-3 business days for payment. "
        "Building permit issuance is later in person where applicable. See references/after-filing.md."
    ),
    "pay_first": (
        "Pay First work class: the portal asks for fees as part of filing. Stop at the fee step; payment needs its own "
        "explicit approval and the user enters payment details. See references/after-filing.md."
    ),
    "simple": (
        "Simple work class: the portal may issue or invoice immediately. Capture exactly what it shows; payment still "
        "needs its own explicit approval. See references/after-filing.md."
    ),
}


def usable_fact(facts: dict[str, dict[str, Any]], fact_id: str, blocked: list[str]) -> Any:
    fact = facts.get(fact_id)
    if fact is None:
        blocked.append(f"missing fact: {fact_id}")
        return None
    usable, value, reason = confirmed_fact_value(fact)
    if not usable:
        blocked.append(f"unusable fact {fact_id}: {reason}")
        return None
    return value


def custom_field_facts(
    facts: dict[str, dict[str, Any]], menu_id: int, questions: dict[str, dict[str, Any]], blocked: list[str]
) -> list[dict[str, Any]]:
    mapped: dict[str, dict[str, Any]] = {}
    prefix = f"portal:{menu_id}:"
    for fact_id, fact in facts.items():
        for consumer in fact.get("consumers") or []:
            target = consumer.get("target")
            if consumer.get("kind") != "portal_field" or not isinstance(target, str) or not target.startswith(prefix):
                continue
            field_name = target[len(prefix):]
            if field_name not in questions:
                blocked.append(f"portal field drift: {field_name} is not in the selected work class layout for type {menu_id}")
                continue
            usable, value, reason = confirmed_fact_value(fact)
            if not usable:
                blocked.append(f"unusable portal fact {fact_id}: {reason}")
                continue
            if field_name in mapped:
                blocked.append(f"multiple facts target portal field: {field_name}")
                continue
            mapped[field_name] = {"field_name": field_name, "fact_id": fact_id, "value": value}
    for name, question in questions.items():
        if question.get("required") and name not in mapped:
            blocked.append(f"required portal field has no sourced fact: {name}")
    return [mapped[name] for name in sorted(mapped)]


def load_selections(path: str | None, run_id: str) -> dict[str, dict[str, Any]]:
    if not path:
        return {}
    document = load_json(path)
    schema = load_json(PLUGIN_ROOT / "schemas/work-class-selection.schema.json")
    errors = validate_instance(document, schema)
    if errors:
        raise SystemExit(f"work-class selection is invalid: {errors}")
    if document["run_id"] != run_id:
        raise SystemExit("run_id mismatch between work-class selection and application set")
    selections: dict[str, dict[str, Any]] = {}
    for item in document["selections"]:
        if item["record_id"] in selections:
            raise SystemExit(f"more than one work class selected for record {item['record_id']}")
        selections[item["record_id"]] = item
    return selections


def allowed_extension(path: Path, allowed: str | None) -> bool:
    if not allowed:
        return True
    extensions = {item.strip().lower() for item in allowed.split(",") if item.strip()}
    return path.suffix.lower() in extensions


def check_work_class(route: dict[str, Any], selection: dict[str, Any] | None, blocked: list[str]) -> dict[str, Any] | None:
    if selection is None:
        blocked.append(
            "no work class selected; reason from the project facts, write work-class-selection.json, and confirm it with the filing theory"
        )
        return None
    if selection["portal_type_id"] != route["menuId"]:
        blocked.append(f"work class selection names type {selection['portal_type_id']}, record uses type {route['menuId']}")
        return None
    if selection["status"] != "confirmed" or not selection.get("confirmed_at"):
        blocked.append("work class selection is not confirmed by the user")
    klass = work_class(route, selection["work_class_id"])
    if klass is None:
        blocked.append(
            f"HARD STOP: work class {selection['work_class_label']} ({selection['work_class_id']}) is not in the pinned portal map "
            f"for type {route['menuId']}; check portal freshness and rebuild the map before filing"
        )
        return None
    if klass["label"].strip() != selection["work_class_label"].strip():
        blocked.append(f"work class label differs from pinned map: selected {selection['work_class_label']!r}, map {klass['label']!r}")
    linked = klass.get("deepLinkedByMenuIds") or []
    if linked and route["menuId"] not in linked:
        blocked.append(f"work class {klass['label']} has its own catalog entry {linked}; file it there, not under type {route['menuId']}")
    if not klass.get("online"):
        blocked.append(f"work class {klass['label']} is not offered online")
    return klass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--facts", required=True)
    parser.add_argument("--application-set", required=True)
    parser.add_argument("--portal-map", required=True)
    parser.add_argument(
        "--work-class-selection",
        help="The agent's reasoned, user-confirmed work class per online record (schemas/work-class-selection.schema.json)",
    )
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    facts_document = load_json(args.facts)
    facts = fact_index(facts_document)
    application_set = load_json(args.application_set)
    portal_map = load_json(args.portal_map)
    if portal_map.get("schema_version") != MAP_SCHEMA_VERSION:
        raise SystemExit(
            f"{args.portal_map} is not a v{MAP_SCHEMA_VERSION} portal map. The v1 map has no work classes; "
            "use assets/portal-maps/v2-portal-map.json"
        )
    if application_set.get("status") != "confirmed" or not application_set.get("confirmed_at"):
        raise SystemExit("application set is not user-confirmed")
    if application_set["run_id"] != facts_document["run_id"]:
        raise SystemExit("run_id mismatch between project facts and application set")
    selections = load_selections(args.work_class_selection, application_set["run_id"])

    transactions = []
    for record in application_set["records"]:
        if record["channel"] != "online":
            continue
        blocked = list(record.get("blocked_reasons") or [])
        if record.get("status") != "confirmed":
            blocked.append(f"record is not confirmed: {record.get('status')}")
        for prerequisite_id in record["prerequisites"]:
            if usable_fact(facts, prerequisite_id, blocked) is not True:
                blocked.append(f"prerequisite is not satisfied: {prerequisite_id}")
        portal = record.get("portal")
        if not portal:
            raise SystemExit(f"online record {record['id']} has no portal configuration")
        route = record_type(portal_map, portal["type_id"])
        if route is None:
            raise SystemExit(f"record {record['id']}: portal type {portal['type_id']} is not supported")
        if route["module"] != portal["module"] or route["label"].strip() != portal["label"].strip():
            blocked.append("application-set portal label/module differs from pinned map")

        klass = check_work_class(route, selections.get(record["id"]), blocked)
        questions: dict[str, dict[str, Any]] = {}
        attachment_rules: list[dict[str, Any]] = []
        contact_rules: list[dict[str, Any]] = []
        if klass is not None:
            layout = layout_questions(portal_map, klass.get("layoutId"))
            if layout is None:
                blocked.append(f"HARD STOP: layout {klass.get('layoutId')} for work class {klass['label']} is not in the pinned portal map")
            else:
                questions = layout
            attachment_rules = attachments_for(portal_map, klass) or []
            contact_rules = contacts_for(portal_map, klass) or []
            if not attachment_rules:
                blocked.append(f"HARD STOP: attachment rules for work class {klass['label']} are not in the pinned portal map")

        address = usable_fact(facts, application_set["address_fact_id"], blocked)
        description = usable_fact(facts, record["scope_description_fact_id"], blocked)
        basic_info = []
        if description is not None:
            basic_info.append({"fact_id": record["scope_description_fact_id"], "value": description})
        if record["lane"] == "building":
            valuation_id = record.get("valuation_fact_id")
            if not valuation_id:
                blocked.append("Building record has no separate valuation fact")
            else:
                valuation = usable_fact(facts, valuation_id, blocked)
                if valuation is not None:
                    basic_info.append({"fact_id": valuation_id, "value": valuation})

        contacts = []
        for contact in contact_rules:
            role = contact["name"]
            fact_id = ROLE_FACTS.get(role)
            if contact.get("required"):
                if fact_id is None:
                    blocked.append(f"no canonical identity mapping for required contact role: {role}")
                    continue
                if usable_fact(facts, fact_id, blocked) is not None:
                    contacts.append({"role": role, "identity_fact_id": fact_id})
            elif fact_id is not None and fact_id in facts and confirmed_fact_value(facts[fact_id])[0]:
                # The City's instructions ask for Applicant/Owner and any licensed professional
                # even where the portal marks the role optional. Add roles we have sourced facts for.
                contacts.append({"role": role, "identity_fact_id": fact_id})

        rules = {item["name"]: item for item in attachment_rules}
        uploads = []
        files_per_category: dict[str, int] = {}
        for attachment in record.get("attachments") or []:
            category = attachment["category"]
            path = Path(attachment["path"])
            files_per_category[category] = files_per_category.get(category, 0) + 1
            rule = rules.get(category)
            if klass is not None and rule is None:
                blocked.append(f"attachment category is not available on type {route['menuId']} / {klass['label']}: {category}")
                continue
            if not path.is_file():
                blocked.append(f"attachment file is missing: {path}")
                continue
            if path.stat().st_size == 0:
                blocked.append(f"attachment file is empty: {path}")
                continue
            if rule is not None and not allowed_extension(path, rule.get("allowedFileTypes")):
                blocked.append(f"{category} accepts {rule.get('allowedFileTypes')} only: {path.name}")
                continue
            uploads.append({"category": category, "files": [{"path": str(path.resolve()), "sha256": sha256_file(path)}]})
        for category, count in sorted(files_per_category.items()):
            limit = (rules.get(category) or {}).get("maxFiles")
            if limit is not None and count > limit:
                blocked.append(
                    f"{category} takes {limit} file(s) on this work class; merge them into one PDF (for Plans, one merged plan set)"
                )
        for name, rule in sorted(rules.items()):
            if rule.get("required") and name not in files_per_category:
                blocked.append(f"required attachment category is missing: {name}")

        normalized = "|".join([str(address or ""), str(route["menuId"]), str(klass["id"] if klass else ""), str(description or ""), application_set["run_id"]])
        behavior = (klass or {}).get("filingBehavior") or "review_first"
        transactions.append(
            {
                "record_id": record["id"],
                "portal_type_id": route["menuId"],
                "module": route["module"],
                "label": route["label"].strip(),
                "work_class": {
                    "id": klass["id"] if klass else None,
                    "label": klass["label"] if klass else None,
                    "filing_behavior": (klass or {}).get("filingBehavior"),
                    "layout_id": (klass or {}).get("layoutId"),
                    "template_name": (klass or {}).get("templateName"),
                },
                "portal_map_pulled_at": portal_map["source"]["pulled_at"],
                "deep_link": route["applyUrl"],
                "idempotency_key": hashlib.sha256(normalized.encode("utf-8")).hexdigest(),
                "address": {"fact_id": application_set["address_fact_id"], "value": address},
                "basic_info": basic_info,
                "contacts": contacts,
                "custom_fields": custom_field_facts(facts, route["menuId"], questions, blocked),
                "uploads": uploads,
                "checkpoints": {
                    "signature": "user_personal_entry_required",
                    "final_submit": "fresh_explicit_approval_required",
                    "payment": "separate_explicit_approval_required",
                },
                "expected_confirmation": route["submitSuccessMessage"],
                "post_submit_next_action": NEXT_ACTION.get(behavior, NEXT_ACTION["review_first"]),
                "status": "blocked" if blocked else "portal_ready",
                "blocked_reasons": sorted(set(blocked)),
            }
        )

    if not transactions:
        raise SystemExit("application set contains no online records")
    output = {
        "schema_version": "1.2.0",
        "run_id": application_set["run_id"],
        "generated_at": utc_now(),
        "records": transactions,
    }
    write_json(args.output, output)
    blocked_count = sum(item["status"] == "blocked" for item in transactions)
    print(f"Built {len(transactions)} transactions ({blocked_count} blocked) -> {args.output}")
    return 2 if blocked_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
