"""CALGreen residential mandatory measures sheet (2025 CALGreen, Title 24 Part 11).

The catalog in data/calgreen-2025-residential.json holds the Chapter 4
measures that commonly reach additions and alterations, each with a short quote
cut verbatim from the CrossBeam code corpus, plus suggested responsibility and
verification columns (suggestions, not code text).

Which measures apply is the drafter's judgment, recorded in project.json
`green` with a reason for each (references/energy-and-green.md):

    "green": {
      "trigger": {"increases_area_volume_or_size": true,
                  "reason": "Adds a 187 sq ft bedroom (logs/scope.md)."},
      "measures": [{"section": "4.303.1.1", "applies": true,
                    "reason": "New water closet in the new bath."}, ...],
      "local": [{"section": "LBMC 14.86.011", "text": "...", "source": "...", "reason": "..."}]
    }

CALGreen 301.1.1 applies Chapter 4 to an addition or alteration that increases
the building's conditioned area, volume or size, within the area of the work.
When the drafter records `false` there, every catalog measure the drafter has
not decided is listed as not required by 301.1.1. When it is `true`, every
catalog measure must be decided: the sheet refuses to print until each one is.
The kit never picks a measure from words in the scope.
"""
from __future__ import annotations

import functools
import json
import os

from .energy import _clean, caps
from .energy import _txt as _t
from .model import PrintRefused

GREEN_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "calgreen-2025-residential.json")


@functools.lru_cache(maxsize=1)
def catalog() -> dict:
    with open(GREEN_FILE, encoding="utf-8") as fh:
        return json.load(fh)


def _sections():
    return [m["section"] for m in catalog()["measures"]]


def validate(project) -> None:
    """Issues for the green block: unknown or duplicate sections, undecided measures."""
    g = project.data.get("green")
    if not g:
        return
    known = set(_sections())
    seen = set()
    for m in g.get("measures", []):
        where = f"green.measures.{m['section']}"
        if m["section"] not in known:
            project.issue("error", "green-unknown-section", where,
                          f"{m['section']} is not in the kit's CALGreen catalog; put a sourced measure in green.local")
        if m["section"] in seen:
            project.issue("error", "green-duplicate", where, "section decided twice")
        seen.add(m["section"])
    undecided = [s for s in _sections() if s not in seen]
    if g["trigger"]["increases_area_volume_or_size"] and undecided:
        project.issue("warning", "green-undecided", "green.measures",
                      f"{len(undecided)} CALGreen measures are not decided yet: {', '.join(undecided)}. "
                      "Record applies true or false with a reason for each; the sheet refuses until then")


def decisions(project) -> dict:
    """Every catalog measure with the drafter's decision, or the 301.1.1 default."""
    g = project.data.get("green")
    if not g:
        raise PrintRefused("project.json has no green block")
    trig = g["trigger"]
    by = {m["section"]: m for m in g.get("measures", [])}
    rows, undecided = [], []
    for m in catalog()["measures"]:
        d = by.get(m["section"])
        if d is None:
            if trig["increases_area_volume_or_size"]:
                undecided.append(m["section"])
                continue
            d = {"applies": False, "reason": "Not required by CALGreen 301.1.1: the drafter records that the "
                                              "work does not increase conditioned area, volume or size.",
                 "default": True}
        rows.append({**m, "applies": d["applies"], "reason": d["reason"],
                     "responsibility": d.get("responsibility") or m["responsibility"],
                     "verification": d.get("verification") or m["verification"],
                     "cd": d.get("cd"), "default": d.get("default", False)})
    return {"trigger": trig, "rows": rows, "undecided": undecided, "local": list(g.get("local", []))}


def report(project) -> dict:
    """A short JSON report for `permitkit green`."""
    d = decisions(project)
    return {"chapter_4_by_301_1_1": d["trigger"]["increases_area_volume_or_size"],
            "trigger_reason": d["trigger"]["reason"],
            "applies": [r["section"] for r in d["rows"] if r["applies"]],
            "not_applied": [r["section"] for r in d["rows"] if not r["applies"] and not r["default"]],
            "not_required_by_301_1_1": [r["section"] for r in d["rows"] if r["default"]],
            "undecided": d["undecided"], "local": [x["section"] for x in d["local"]]}


def _decided(kit):
    d = decisions(kit.project)
    if d["undecided"]:
        raise PrintRefused("CALGreen measures not decided: " + ", ".join(d["undecided"])
                           + ". Record applies true or false with a reason for each in project.json green.measures")
    return d


SIZE = 8.0          # table text on a CALGreen panel (pt)


def measures_panel(kit, sheet, cell, title="CALGREEN RESIDENTIAL MANDATORY MEASURES", show_not_applied=True,
                   divisions=None, intro=True, local=True):
    """The measures that apply, grouped by division, each with its section, the
    quoted requirement, who is responsible and how it is verified. `divisions`
    limits the panel to some divisions (to split a long list over columns)."""
    d = _decided(kit)
    cat = catalog()
    trig = d["trigger"]
    pan = sheet.panel(cell, title)
    if intro:
        pan.para(f"CODE: {cat['edition'].upper()}.", size=7.6, bold=True)
        pan.para(_t(kit, f"CALGREEN 301.1.1: \"{_clean(cat['trigger']['quote'])}\"", trig.get("cd")), size=7.4)
        yes = "YES" if trig["increases_area_volume_or_size"] else "NO"
        pan.para(_t(kit, f"DOES THIS WORK INCREASE CONDITIONED AREA, VOLUME OR SIZE? {yes}. "
                         + caps(trig["reason"]), trig.get("cd")), size=7.4, bold=True)
    applied = [r for r in d["rows"] if r["applies"]]
    if intro and not applied and not d["local"]:
        pan.para("NO CALGREEN CHAPTER 4 MEASURE APPLIES TO THIS SCOPE ON THE DRAFTER'S RECORD ABOVE.", size=7.6,
                 bold=True)
    cols = [("SECTION", 0.85), ("MEASURE AND QUOTED REQUIREMENT", None, "wrap"),
            ("WHY IT APPLIES", 2.6, "wrap"), ("RESPONSIBLE", 1.3, "wrap"), ("VERIFIED BY", 1.5, "wrap")]
    for div, name in cat["divisions"].items():
        rows = [r for r in applied if r["division"] == div]
        if not rows or (divisions is not None and div not in divisions):
            continue
        pan.heading(name, size=8.5)
        pan.table(cols, [[r["section"], _t(kit, f"{r['title'].upper()}: \"{_clean(r['quote'])}\"", r["cd"]),
                          _t(kit, caps(r["reason"]), r["cd"]), r["responsibility"].upper(),
                          caps(r["verification"])] for r in rows], size=SIZE)
    if local and d["local"]:
        pan.heading("LOCAL AMENDMENTS AND OTHER SOURCED MEASURES", size=8.5)
        pan.table(cols, [[x["section"], _t(kit, f"\"{x['text']}\" ({x['source']})".upper(), x.get("cd")),
                          _t(kit, caps(x["reason"]), x.get("cd")), (x.get("responsibility") or "").upper(),
                          caps(x.get("verification") or "")] for x in d["local"]], size=SIZE)
    if show_not_applied:
        skipped = [r for r in d["rows"] if not r["applies"]]
        if skipped:
            pan.heading("CATALOG MEASURES NOT APPLIED", size=8.5)
            if all(r["default"] for r in skipped):
                pan.para("ALL OTHER CATALOG MEASURES: NOT REQUIRED BY 301.1.1 (SEE THE ANSWER ABOVE).", size=SIZE)
            else:
                pan.table([("SECTION", 0.85), ("MEASURE", 3.0, "wrap"), ("REASON", None, "wrap")],
                          [[r["section"], r["title"].upper(), _t(kit, caps(r["reason"]), r["cd"])]
                           for r in skipped], size=SIZE)
    return pan


def green_notes(kit) -> list:
    """The applied measures as numbered plan notes (for a small set's notes column)."""
    d = decisions(kit.project)
    if d["undecided"]:
        raise PrintRefused("CALGreen measures not decided: " + ", ".join(d["undecided"]))
    out = [_t(kit, f"CALGREEN {r['section']}: \"{_clean(r['quote'])}\" RESPONSIBLE: {r['responsibility']}. "
                   f"VERIFIED BY: {r['verification']}.", r["cd"]) for r in d["rows"] if r["applies"]]
    out += [_t(kit, f"{x['section']}: \"{x['text']}\" ({x['source']})", x.get("cd")) for x in d["local"]]
    return out


def _split(kit):
    """Divisions for two columns: the first column takes divisions until it
    holds about half of the applied measures. Layout only."""
    d = _decided(kit)
    divs = [k for k in catalog()["divisions"] if any(r["applies"] and r["division"] == k for r in d["rows"])]
    n = sum(1 for r in d["rows"] if r["applies"])
    first, count = [], 0
    for k in divs:
        size = sum(1 for r in d["rows"] if r["applies"] and r["division"] == k)
        if first and count + size - n / 2 > n / 2 - count:
            break
        first.append(k)
        count += size
    return first, [k for k in divs if k not in first]


def sheet(kit, sid, title=None):
    """A whole CALGreen sheet: the measures in two columns (the 301.1.1 answer
    and the first divisions left; the rest, local measures and the measures not
    applied right), with the preparer's notes in the notes column."""
    from .energy import stack
    sh = kit.sheet(sid)
    w, _ = sh.drawing_area_in
    half = round(w / 2, 2)
    first, second = _split(kit)
    kw = {"title": title} if title else {}
    stack(sh, 0, half - 0.25, [lambda c: measures_panel(kit, sh, c, divisions=first, show_not_applied=False,
                                                         local=False, **kw)])
    stack(sh, half, w - half, [lambda c: measures_panel(kit, sh, c, title="CALGREEN MEASURES (CONTINUED)",
                                                         divisions=second, intro=False)])
    sh.notes([
        "OWNER AND CONTRACTOR: EACH MEASURE ON THIS SHEET IS A CODE REQUIREMENT FOR THIS SCOPE. KEEP PRODUCT DATA "
        "AND DOCUMENTATION ON SITE FOR THE INSPECTOR.",
        "RESPONSIBLE AND VERIFIED-BY ENTRIES ARE THE PREPARER'S ASSIGNMENT, NOT CODE TEXT.",
        "THE CITY MAY AMEND CALGREEN LOCALLY; LOCAL MEASURES ARE LISTED ONLY WHERE THE PREPARER HAS SOURCED THEM.",
    ], title="CALGREEN NOTES")
    return sh
