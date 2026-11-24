"""The "measure these" list: what the owner should tape before a set is called ready to file.

A city approves measured numbers. Every ASSUMED or PLACEHOLDER value that a
sheet prints, or that a code rule rests on, is an open item a plan checker can
send back. This list puts them in the order that matters, so the owner spends
one site visit on the numbers that can change the design:

  1. tags a code rule rests on whose drawn number breaks the rule (a measured
     number could still pass, or could prove the design must change);
  2. tags any other code rule rests on;
  3. tags printed on the most sheets;
  4. then the field_verify rank.

A tag closes when its entry has `signed_off`, or when every value that
carries it is measured. A PLACEHOLDER with no tag prints nowhere, so it is
listed apart: it blocks the work that depends on it.

    python3 -m permitkit measure project.json [--build build] [--out questions/measure-list.md]
"""
from __future__ import annotations

import json
import os

from .model import UNVERIFIED, fv_key
from .qa import rules_report


def _printed(build_dir) -> dict | None:
    """{tag: sorted sheet ids} from a build's sidecar, or None without a build."""
    path = os.path.join(build_dir, "build.json") if build_dir else None
    if not path or not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as fh:
        sc = json.load(fh)
    out: dict = {}
    for sh in sc["sheets"]:
        for t in sh["texts"]:
            for tag in t.get("fv", []):
                out.setdefault(tag, set()).add(sh["id"])
    return {k: sorted(v) for k, v in out.items()}


def measure_list(project, build_dir: str | None = None) -> dict:
    """{items, untagged, printed_known}: the open field-verify tags, ranked, and
    the PLACEHOLDER values with no tag."""
    rows = rules_report(project)
    printed = _printed(build_dir)
    own = {}                # tag -> the unverified values that carry it themselves
    for key, v in project.values.items():
        if v.status in UNVERIFIED:
            for tag in v.fv_tags:
                own.setdefault(tag, []).append(key)
    items = []
    for tag, e in project.fv.items():
        if e.get("signed_off"):
            continue
        keys = sorted(own.get(tag, []))
        if not keys and e.get("values"):
            continue            # every value it covers is measured now
        rules = [r for r in rows if tag in r["fv"]]
        items.append({
            "tag": tag, "what": e.get("what", ""), "why": e.get("why", ""), "rank": e.get("rank"),
            "values": keys,
            "rules": [{"id": r["id"], "element": r["element"], "status": r["status"],
                       "breaks": r["ok"] is False} for r in rules],
            "sheets": None if printed is None else printed.get(tag, []),
        })
    items.sort(key=lambda it: (-sum(r["breaks"] for r in it["rules"]), -len(it["rules"]),
                               -len(it["sheets"] or []), it["rank"] if it["rank"] is not None else 99,
                               fv_key(it["tag"])))
    untagged = sorted(k for k, v in project.values.items() if v.status == "PLACEHOLDER" and not v.fv_tags)
    return {"items": items, "untagged": untagged, "printed_known": printed is not None}


def markdown(rep: dict) -> str:
    """The list as a short markdown page for the owner (`asking-the-owner.md` section 2)."""
    out = ["# Measure these before the set goes to the city", ""]
    if not rep["items"] and not rep["untagged"]:
        return "\n".join(out + ["Every printed number is measured. Nothing to tape.", ""])
    out += ["A city approves measured numbers. Each item below prints as a field-verify (FV) tag "
            "until someone tapes it. The first items can change the design.", "",
            "| # | Tag | Measure | Why it matters | Code rules on it | Sheets |",
            "|---|---|---|---|---|---|"]
    for n, it in enumerate(rep["items"], 1):
        rules = ", ".join(f"{r['id']}{' (drawn number breaks it)' if r['breaks'] else ''}" for r in it["rules"])
        sheets = "build first" if it["sheets"] is None else (", ".join(it["sheets"]) or "not printed")
        cells = [str(n), it["tag"], it["what"], it["why"], rules or "none", sheets]
        out.append("| " + " | ".join(c.replace("|", "/") for c in cells) + " |")
    if rep["untagged"]:
        out += ["", "Not drawn yet (PLACEHOLDER, no tag): " + ", ".join(rep["untagged"]) +
                ". Each blocks the drawing that needs it."]
    return "\n".join(out + [""])
