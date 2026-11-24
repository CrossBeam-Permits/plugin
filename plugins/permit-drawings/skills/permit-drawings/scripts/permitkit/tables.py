"""Data tables built from project.json: zoning and area summaries, code limits.

The professional cover sheet carries dense ruled tables: each zoning standard
with what is required or allowed, what exists and what is proposed. Here
every cell comes from project.json: a limit from a `rules` entry (with its
citation and code-decision id), a drawn number from Values through kit.text.

    from permitkit import tables
    tables.zoning_table(kit, panel, [
        ("group", "LOT"),
        {"item": "LOT AREA", "existing": "{lot_area_sf:sf}"},
        {"item": "LOT COVERAGE", "required": "R-12", "existing": "{cov_e_pct:n}%",
         "proposed": "{cov_n_pct:n}%"},
        ("group", "SETBACKS"),
        {"item": "SIDE (EAST)", "required": "R-14", "proposed": "{side_setback:ftin}"},
    ])

A `required` that names a rule id prints that rule's limit and citation. Any
other `required` text prints as written, so write it from the city's text
(for example "PER PLANNING"), never a number from memory. A cell template with
braces is filled with kit.text, so its numbers carry their FV tags.
"""
from __future__ import annotations

from .model import PrintRefused, source_places
from .notes import Txt, fill
from .units import UnitError, convert, fmt_len_exact, unit_info, unit_word

_OP = {">=": "MIN.", "<=": "MAX.", "==": ""}


def rule(project, rule_id: str) -> dict:
    for r in project.data.get("rules", []):
        if r.get("id") == rule_id:
            return r
    raise PrintRefused(f"no rule {rule_id!r} in project.json rules")


def limit_number(check: dict, denom: int = 16) -> str:
    """A rule check's limit without its MIN./MAX. word: 7'-0", 40%, 70.00 SQ FT, 0.30 U-FACTOR.

    The house style for every printed code limit (tables, notes and 3D views).
    A length prints in feet-inches from 12 in. up, inches below; a length off
    the 1/denom grid prints as decimal inches so it keeps its value (0.019").
    Other numbers keep the decimals project.json wrote them with; a U-factor
    or a ratio shows at least two (0.30), as the energy tables print them.
    """
    raw, unit = check["limit"], str(check.get("unit", ""))
    lim = float(raw)
    try:
        dim, factor = unit_info(unit)
    except UnitError as exc:
        raise PrintRefused(str(exc)) from None
    places = source_places(raw)
    if dim == "length":
        if factor == 1.0:
            return fmt_len_exact(lim, "ftin" if lim >= 12 else "in", denom, places)
        return fmt_len_exact(convert(lim, unit, "in"), "ftin", denom)
    if dim == "U-factor" or (dim == "percent" and factor != 1.0):
        places = max(places or 0, 2)
    elif dim == "area" and factor == 144.0:
        places = max(places or 0, 2)
    n = f"{lim:.{places}f}" if places is not None else f"{lim:.4f}".rstrip("0").rstrip(".")
    if dim == "percent" and factor == 1.0:
        return f"{n}%"
    if dim == "area":
        return f"{n} {'SQ FT' if factor == 144.0 else 'SQ IN'}"
    if dim == "thermal resistance, R-value":
        return f"R-{n}"
    if dim == "time":
        return f"{n} {'HR' if factor == 1.0 else 'DAYS'}"
    word = unit_word(unit)
    return f"{n} {word}" if word else n


def limit_text(check: dict, denom: int = 16) -> str:
    """The printed limit of a rule check: 'MIN. 7\'-0"', 'MAX. 40%', 'MIN. 70.00 SQ FT'.
    denom is the project's length precision (project.denom)."""
    word = _OP.get(check["op"], "")
    return f"{word} {limit_number(check, denom)}".strip()


def rule_limit(project, rule_id: str, citation: bool = True) -> Txt:
    """A rule's limit as printable text, with its citation; records the rule's cd for QA."""
    r = rule(project, rule_id)
    text = limit_text(r["check"], project.denom)
    if citation and r.get("citation"):
        text += f" ({r['citation']})"
    return Txt(text, cd=r.get("cd") or ())


def _cell(project, x):
    if x is None:
        return ""
    if isinstance(x, Txt):
        return x
    s = str(x)
    if "{" in s:
        return fill(project, s)
    return s


ZONING_COLUMNS = [("ITEM", 1.55, "wrap"), ("REQUIRED / ALLOWED", 1.75, "wrap"), ("EXISTING", 1.2, "wrap"),
                  ("PROPOSED", 1.2, "wrap"), ("NOTES", None, "wrap")]


def zoning_table(kit, panel, rows, columns=None, size: float = 6.6):
    """A ruled zoning / area table in a panel. See the module docstring for the row format.

    rows: ("group", "TITLE") bands, or dicts with item, required, existing,
    proposed and note. `required` may name a rule id. Columns default to
    ZONING_COLUMNS; pass your own (same five keys, in order) to change widths.
    """
    project = kit.project
    rule_ids = {r.get("id") for r in project.data.get("rules", [])}
    out = []
    for row in rows:
        if isinstance(row, tuple):
            out.append(row)
            continue
        req = row.get("required")
        if isinstance(req, str) and req in rule_ids:
            req = rule_limit(project, req)
        else:
            req = _cell(project, req)
        out.append([row.get("item", ""), req, _cell(project, row.get("existing")),
                    _cell(project, row.get("proposed")), _cell(project, row.get("note"))])
    panel.grid_table(columns or ZONING_COLUMNS, out, size=size)
