"""QA gate for a built set. No person needed. Output is JSON.

It reads build.json (the sidecar the kit wrote) and the PDFs. Most checks use
the text records the kit wrote with their bounding boxes. The scale-bar check
reads the text runs in the PDF itself.

Checks:
  true_scale        view ratio within 0.5 percent of its label; MediaBox equals
                    the declared sheet size; no scaling transform in any page;
                    each scale bar, measured from its printed numbers in the
                    PDF, agrees with the view's printed scale label
  title_block       every required title-block field prints its project.json
                    value, and the value is not empty
  decimal_inches    no decimal inches or feet in kit-emitted text, except an
                    off-grid length the kit prints as decimal inches (0.019")
  field_verify      every printed FV tag exists; every unverified value carries its tag
  collisions        text on text, text outside its region, and view text
                    that sits on building linework (walls, doors, swings)
                    or on a placed image without a filled backing.
                    A build.json from an older kit has no linework record;
                    the check then warns "rebuild with this kit version"
  kit_version       the kit that wrote build.json is this kit; warns when not
  layout            views that draw outside their cell
  chain_closure     dimension chains close
  sheet_index       a printed sheet index equals the bound order; page labels
                    match; no hand-typed table stands in for the index
  claims            no compliance note rests on an unverified value
  rules             each drawn value that a rule in project.json names meets
                    the rule's limit (units converted); warns when the value is
                    missing or unverified
  images            each placed image's file is unchanged since the build; its
                    source label prints; a concept rendering carries its label
                    on the image and sits in no drawing view; warns under 100 dpi
  revisions         every cloud's delta is a listed revision
  determinism       two rebuilds gave identical files
  stale             project.json, the sheet scripts and attachments have not
                    changed since the build (a failed build leaves the old one)
  stale_outputs     the build folder holds no PDF that this build did not
                    write (a removed sheet, an old merged set), and no PNG or
                    SVG preview older than this build

It also extracts every code citation string, grouped by note, so an LLM can
judge consistency. The kit only extracts; it does not judge.

Advisory (never fails): `advisory.unverified_text` lists every note or label
that prints an unverified value or an FV tag. Whether such a text claims
compliance is a judgment for the reviewing agent, not a pattern match.
`advisory.conditional_code_notes` lists every printed note whose recorded
code-decision id (the `cd=` argument of kit.text or kit.claim; it never
prints) is one that `code_notes` in project.json marks as having conditions. Whether the note prints the condition, or its branch and the fact
that selects it, is a judgment for the reviewing agent.
"""
from __future__ import annotations

import glob
import json
import math
import os
import re

from . import __version__, drafting
from . import textmetrics as tm
from .build import outputs_listed
from .display import box_inside, boxes_overlap
from .model import ExprError, Project, RangeError, fv_parse, fv_sorted, fv_text, rule_refs
from .pdf import read_pdf, text_runs
from .sheet import GUTTER, OPTIONAL_TB, TB_SOURCES, title_block_scale
from .units import PT_PER_IN, ScaleError, UnitError, convert, fmt_ftin, parse_scale_label, unit_info

RATIO_TOL = 0.005
MATCH_PT = 1.0           # how far a PDF text run may sit from its sidecar record, points

# A decimal number followed by a length unit: 5.5" .5" 5.5 IN 5.5-INCH 2.5 FT.
# Mechanical format check on text the kit emitted; not a semantic judgment.
_DECIMAL = re.compile(
    r"(?<![\w.])(?P<num>\d+\.\d+|\.\d+)\s*-?\s*(?P<unit>\"|''|IN\b|INCH(?:ES)?\b|'(?!')|FT\b|FEET\b)",
    re.I)
_INCH_DECIMAL = {'"', "''", "in", "inch", "inches"}


def _off_grid_decimal_inches(m: re.Match, denom: int) -> bool:
    """True when this match is the kit's exact form for a length that is not a
    whole number of 1/denom inches (0.019\"). A length on the grid (3.25\" is
    3 1/4\") and any decimal in feet still count as a decimal-length fail."""
    if m.group("unit").lower() not in _INCH_DECIMAL:
        return False
    inches = float(m.group("num"))
    return abs(inches * denom - round(inches * denom)) >= 1e-6


def decimal_inch_fails(text: str, denom: int = 16) -> list[str]:
    """Decimal lengths in `text` that QA should fail.

    An off-grid inch length the kit prints so a code limit keeps its value
    (0.019\") is allowed. On-grid decimals and decimal feet are not.
    """
    return [m.group(0) for m in _DECIMAL.finditer(text) if not _off_grid_decimal_inches(m, denom)]


_SHEET_ID = re.compile(r"[A-Z]{1,3}-[0-9]+(?:\.[0-9]+)?[A-Z]?")
_CITE = re.compile(
    r"(?:(?P<code>[A-Z][A-Za-z&]{1,9}(?:\s?\d{1,3})?)\s+)?"
    r"(?P<ref>(?:§\s*\d+(?:\.\d+)*(?:\([A-Za-z0-9]+\))*[A-Z0-9]*)"
    r"|(?:(?:SECTION|SEC\.|TABLE|FIGURE)\s+[A-Z]?\d+(?:\.\d+)*(?:\([A-Za-z0-9]+\))*)"
    r"|(?:\b[A-Z]\d{3,4}(?:\.\d+)*(?:\([A-Za-z0-9]+\))*[A-Z0-9]*)"
    r"|(?:\b\d{2,4}(?:\.\d+)+(?:\([A-Za-z0-9]+\))*[A-Z0-9]*))"
    # the whole number, then no unit word: "50.59 SQ FT" is an area, not "50.5"; "12.9 DEG" an angle
    r"(?!\.?\d)(?!\s*(?:SQ|SF|S\.F\.|FT|IN\b|VA\b|A\b|%|\"|'|LB|PSF|KVA|AMP|DEG|°|:12))")
# The only form in which the kit writes a 'cm': clip, image matrix, paint (pdf.image_block).
_N = rb"-?\d+(?:\.\d+)?"
_IMAGE_BLOCK = re.compile(rb"(?m)^q\n" + rb" ".join([_N] * 4) + rb" re W n\n" + rb" ".join([_N] * 6)
                          + rb" cm\n/Im\d+ Do\nQ\n")
_NOT_CODE = {"AND", "OR", "PER", "SEE", "TO", "OF", "THE", "WITH", "IN", "AT", "ON", "BY", "FOR", "NOT"}


def _result(status, detail=None, **extra):
    out = {"status": status, "detail": detail or []}
    out.update(extra)
    return out


def _status(fails, warns=()):
    return "fail" if fails else ("warn" if warns else "pass")


def run(build_dir: str, project_path: str | None = None) -> dict:
    with open(os.path.join(build_dir, "build.json"), encoding="utf-8") as fh:
        sc = json.load(fh)
    ppath = project_path or os.path.normpath(os.path.join(build_dir, sc["paths"]["project"]))
    project = Project.load(ppath)
    checks = {}
    sheets = sc["sheets"]

    # ---- stale (Project.load hashed the file bytes it read)
    stale, stale_warn = [], []
    if project.sha256 != sc["project_sha256"]:
        stale.append("project.json changed after this build; rebuild before QA")
    if "inputs_sha256" in sc:
        from .build import inputs_sha256
        now, then = inputs_sha256(project), sc["inputs_sha256"]
        for name in sorted(set(now) | set(then)):
            if now.get(name) != then.get(name):
                what = "is new" if name not in then else ("was removed" if name not in now else "changed")
                stale.append(f"{name} {what} after this build (or the last build failed); rebuild before QA")
    else:
        stale_warn.append("build.json records no sheet-script hashes; rebuild with this kit version")
    checks["stale"] = _result(_status(stale, stale_warn), stale + stale_warn)

    # ---- true scale
    fails = []
    set_info = read_pdf(os.path.join(build_dir, sc["set_pdf"]))
    if set_info["page_count"] != len(sheets):
        fails.append(f"set PDF has {set_info['page_count']} pages, sidecar lists {len(sheets)} sheets")
    for sh in sheets:
        want = [sh["size_in"][0] * 72, sh["size_in"][1] * 72]
        if [round(v, 2) for v in sh["mediabox_pt"]] != [round(v, 2) for v in want]:
            fails.append(f"{sh['id']}: sidecar MediaBox {sh['mediabox_pt']} is not {sh['size']} {want}")
        pdf_pages = []
        if sh["page_index"] < set_info["page_count"]:
            pdf_pages.append(("set", set_info["pages"][sh["page_index"]]))
        sheet_info = read_pdf(os.path.join(build_dir, sc["sheet_pdfs"][sh["id"]]))
        pdf_pages.append(("sheet", sheet_info["pages"][0]))
        for label, page in pdf_pages:
            mb = page["mediabox"]
            if abs(mb[2] - mb[0] - want[0]) > 0.01 or abs(mb[3] - mb[1] - want[1]) > 0.01:
                fails.append(f"{sh['id']}: {label} PDF MediaBox {mb} is not {want[0]:g} x {want[1]:g} pt")
            ops = re.sub(rb"\((?:\\.|[^\\)])*\)", b"()", page["content"])
            # A placed image needs a 'cm' to map its unit square onto its box. The kit
            # writes it only inside this one block (pdf.image_block); strip those
            # blocks, count them against the sidecar, then refuse any other 'cm'.
            ops, n_img = _IMAGE_BLOCK.subn(b"", ops)
            if n_img != len(sh.get("images", [])):
                fails.append(f"{sh['id']}: {label} PDF draws {n_img} images, the sidecar lists "
                             f"{len(sh.get('images', []))}")
            if re.search(rb"(?:^|\s)cm(?:\s|$)", ops):
                fails.append(f"{sh['id']}: {label} PDF content uses a 'cm' transform; scale is not guaranteed")
        scale_texts = {t["view"]: t for t in sh["texts"] if t["role"] == "view.scale"}
        for v in sh["views"]:
            if not v["true_scale"]:
                continue
            ratio = parse_scale_label(v["scale"])
            expect = ratio * 72
            r = v["pt_per_in"] / expect
            if abs(r - 1) > RATIO_TOL:
                fails.append(f"{sh['id']} view {v['number']}: {v['pt_per_in']:.4f} pt/in is "
                             f"{r:.4f} of {v['scale']} ({expect:.4f} pt/in)")
            ex = v["extents_in"]
            bb = v["bbox_pt"]
            for i, axis in ((0, "x"), (1, "y")):
                span = ex[i + 2] - ex[i]
                got = (bb[i + 2] - bb[i]) / span if span else expect
                if abs(got / expect - 1) > RATIO_TOL:
                    fails.append(f"{sh['id']} view {v['number']}: placed {axis} span gives "
                                 f"{got:.4f} pt/in, label says {expect:.4f}")
            st = scale_texts.get(v["id"])
            if not st or st["meta"].get("scale") != v["scale"]:
                fails.append(f"{sh['id']} view {v['number']}: printed scale does not match {v['scale']}")
        want_tb = title_block_scale(v["scale"] for v in sh["views"])
        if sh["scale_text"] != want_tb:
            fails.append(f"{sh['id']}: title block scale {sh['scale_text']!r}, views say {want_tb!r}")
        fails += _measure_scale_bars(sh, text_runs(sheet_info["pages"][0]["content"]))
    checks["true_scale"] = _result(_status(fails), fails,
                                   views_checked=sum(len(s["views"]) for s in sheets),
                                   scale_bars_measured=sum(len(s["scale_bars"]) for s in sheets))

    # ---- title block: each field prints its project.json value
    fails = []
    for sh in sheets:
        want = {f: _dig(project.meta, path) for f, path in TB_SOURCES.items()}
        want.update({"sheet_title": sh["title"], "sheet_id": sh["id"], "scale": sh["scale_text"]})
        for f, val in want.items():
            if val is None and f in OPTIONAL_TB:
                if str(sh["title_block"].get(f, "")).strip():
                    fails.append(f"{sh['id']}: title block prints a {f} that project.json does not have")
                continue
            if not isinstance(val, str) or not val.strip():
                fails.append(f"{sh['id']}: title block field {f!r} has no value in project.json")
                continue
            if _squash(_clean(val)) not in _squash(sh["title_block"].get(f, "")):
                fails.append(f"{sh['id']}: title block field {f!r} does not print {val!r}")
        sb = sh["stamp_box"]
        if not sb or (sb[2] - sb[0]) < 72 or (sb[3] - sb[1]) < 72:
            fails.append(f"{sh['id']}: stamp box missing or smaller than 1 x 1 in")
    checks["title_block"] = _result(_status(fails), fails)

    # ---- decimal inches
    fails = []
    for sh in sheets:
        for t in sh["texts"]:
            for hit in decimal_inch_fails(t["s"], project.denom):
                fails.append(f"{sh['id']}: decimal length {hit!r} in {t['s']!r}")
    checks["decimal_inches"] = _result(_status(fails), fails)

    # ---- field verify
    fails, warns = [], []
    printed = set()
    groups = _groups(sheets)
    for (sid, _), recs in groups.items():
        text = " ".join(r["s"] for r in recs)
        shown = set(fv_parse(text))
        for tag in shown:
            printed.add(tag)
            if tag not in project.fv:
                fails.append(f"{sid}: {tag} is printed but not in field_verify: {text!r}")
        for r in recs:
            for k in r["keys"]:
                try:
                    val = project.value(k)
                except KeyError:
                    fails.append(f"{sid}: printed value {k!r} no longer exists in project.json")
                    continue
                for tag in val.fv_tags:
                    if tag not in shown:
                        fails.append(f"{sid}: {k} is unverified and printed without {tag}: {text!r}")
                if val.unverified and not val.fv_tags:
                    fails.append(f"{sid}: {k} is unverified and has no tag: {text!r}")
    unused = sorted(set(project.fv) - printed)
    if unused:
        warns.append(f"field_verify tags never printed on a sheet: {', '.join(unused)}")
    checks["field_verify"] = _result(_status(fails, warns), fails + warns, printed=sorted(printed))

    # ---- collisions and regions
    fails, warns = [], []
    for sh in sheets:
        regions = sh["regions"]
        frame = regions["frame"]
        texts = sh["texts"]
        for t in texts:
            if not box_inside(t["bbox"], frame, tol=0.5):
                fails.append(f"{sh['id']}: text {t['s']!r} runs outside the border")
            reg = regions.get(t["region"]) if t["region"] else None
            if reg and not box_inside(t["bbox"], reg, tol=0.5):
                fails.append(f"{sh['id']}: text {t['s']!r} runs outside its region {t['region']}")
        live = [t for t in texts if t["collide"]]
        for i in range(len(live)):
            for j in range(i + 1, len(live)):
                a, b = live[i], live[j]
                if boxes_overlap(a["bbox"], b["bbox"]):
                    fails.append(f"{sh['id']}: text {a['s']!r} overlaps {b['s']!r}")
        if "text_over_geometry" not in sh:
            warns.append(f"{sh['id']}: build.json has no text-over-linework record (an older kit wrote it); "
                         "rebuild with this kit version")
        for hit in sh.get("text_over_geometry", []):
            if "image" in hit:
                fails.append(f"{sh['id']}: text {hit['text']!r} sits on image {hit['image']!r}; move it off "
                             "the image or give it a filled backing (a white box) drawn over the image")
                continue
            where = ""
            if hit.get("line_bbox"):
                x0, y0, x1, y1 = (c / 72 for c in hit["line_bbox"])
                where = (f" (the line spans {x0:.1f}-{x1:.1f} in. across and {y0:.1f}-{y1:.1f} in. up "
                         "from the sheet's lower-left corner)")
            fails.append(f"{sh['id']}: text {hit['text']!r} sits on building linework in {hit['region']}{where}; "
                         "move it clear of walls, doors, swings and windows, or use a leader. If that line is "
                         "not building linework (a setback, grid, leader or match line), draw it with "
                         "layer=\"annot\"")
    checks["collisions"] = _result(_status(fails, warns), fails + warns)

    # ---- internal references: the drafting software's own identifiers on a sheet
    fails = internal_refs(sheets)
    checks["internal_refs"] = _result(_status(fails), fails)

    # ---- images: the file is the one the build placed, labels printed, concept guard
    checks["images"] = image_check(sheets, project)

    # ---- kit version
    built_with = sc.get("kit_version")
    same = built_with == __version__
    checks["kit_version"] = _result("pass" if same else "warn",
                                    [] if same else [f"build.json was written by permitkit {built_with}, "
                                                     f"this QA is {__version__}; rebuild with this kit version"],
                                    built_with=built_with, qa_version=__version__)

    # ---- layout
    fails = [f"{sh['id']}: {m}" for sh in sheets for m in sh["layout_issues"]]
    checks["layout"] = _result(_status(fails), fails)

    # ---- chain closure (recomputed from the current project)
    fails = []
    report = project.chain_report()
    for r in report:
        if not r["ok"]:
            fails.append(f"chain {r['id']}: " + (r.get("error") or
                         f"sum {r['sum']:.4f} vs total {r['total']:.4f} (off {r['diff']:.4f} in.)"))
    checks["chain_closure"] = _result(_status(fails) if report else "n/a", fails, chains=len(report))

    # ---- sheet index and page labels
    fails = []
    drawn = [s["id"] for s in sheets]
    labels = [lab for _, lab in sorted(set_info["page_labels"])]
    if labels != drawn:
        fails.append(f"set PDF page labels {labels} do not equal the drawn order {drawn}")
    idx_rows = [t for s in sheets for t in s["texts"] if t["role"] == "index" and "sheet_id" in t["meta"]]
    if idx_rows:
        seen = {}
        for t in idx_rows:
            seen.setdefault(t["meta"]["order"], t["meta"]["sheet_id"])
        printed_order = [seen[k] for k in sorted(seen)]
        if printed_order != sc["bound_order"]:
            fails.append(f"printed sheet index {printed_order} does not equal bound order {sc['bound_order']}")
    fails += _hand_typed_index(sheets, sc["bound_order"])
    if idx_rows:
        status = _status(fails)
    else:
        status = "fail" if fails else "n/a"
    checks["sheet_index"] = _result(status, fails or ([] if idx_rows else ["no sheet index printed in this set"]))

    # ---- claims
    fails = []
    n_claims = 0
    for sh in sheets:
        for c in sh["claims"]:
            n_claims += 1
            try:
                bad = project.unverified_in(c["depends_on"])
            except KeyError as exc:
                fails.append(f"{sh['id']}: claim depends on a missing value: {exc}")
                continue
            if bad:
                fails.append(f"{sh['id']}: compliance note rests on unverified {bad}: {c['text']!r}")
    checks["claims"] = _result(_status(fails) if n_claims else "n/a", fails, claims=n_claims)

    # ---- code rules (rules in project.json, usually from crossbeam_rules kit_checks)
    rule_rows = rules_report(project)
    fails = [r["message"] for r in rule_rows if r["status"] == "fail"]
    warns = [r["message"] for r in rule_rows if r["status"] == "warn"]
    checks["rules"] = _result(_status(fails, warns) if rule_rows else "n/a", fails + warns,
                              rules=rule_rows,
                              counts=rule_counts(rule_rows))

    # ---- revisions
    fails = []
    deltas = {r["delta"] for r in project.revisions}
    for sh in sheets:
        for c in sh["clouds"]:
            if c["delta"] not in deltas:
                fails.append(f"{sh['id']}: cloud tagged delta {c['delta']} is not in revisions")
    checks["revisions"] = _result(_status(fails), fails)

    # ---- drafting standard: line weight, hatching, black-and-white fills, scale use, connections
    for name, (fails, warns) in drafting.checks(sheets, project).items():
        checks[name] = _result(_status(fails, warns), fails + warns)

    # ---- determinism
    det = sc.get("determinism")
    if det is None:
        checks["determinism"] = _result("warn", ["not run; build with determinism on"])
    else:
        checks["determinism"] = _result("pass" if det["ok"] and det["sidecar_core_equal"] else "fail",
                                        det.get("differing_files", []), builds=det["builds_compared"])

    # ---- stale outputs: files this build did not write
    listed = outputs_listed(sc)
    extra = []
    for pattern in ("*.pdf", os.path.join("sheets", "*.pdf")):
        for f in sorted(glob.glob(os.path.join(build_dir, pattern))):
            rel = os.path.relpath(f, build_dir).replace(os.sep, "/")
            if rel not in listed:
                extra.append(f"{rel} was not written by this build; delete it or rebuild into a clean folder")
    built_at = os.path.getmtime(os.path.join(build_dir, "build.json"))
    for pattern in (os.path.join("png", "*.png"), os.path.join("svg", "*.svg")):
        for f in sorted(glob.glob(os.path.join(build_dir, pattern))):
            if os.path.getmtime(f) < built_at - 1:
                rel = os.path.relpath(f, build_dir).replace(os.sep, "/")
                extra.append(f"{rel} is older than this build; run preview again or delete it")
    checks["stale_outputs"] = _result(_status(extra), extra)

    cites = citations(sheets, project)
    failed = [k for k, v in checks.items() if v["status"] == "fail"]
    return {
        "pass": not failed,
        "failed_checks": failed,
        "summary": {k: v["status"] for k, v in checks.items()},
        "counts": {"sheets": len(sheets), "views": sum(len(s["views"]) for s in sheets),
                   "rules": len(rule_rows),
                   "texts": sum(len(s["texts"]) for s in sheets),
                   "citations": sum(len(g["citations"]) for g in cites["groups"])},
        "checks": checks,
        "citations": cites,
        "advisory": {"unverified_text": unverified_text(sheets, project),
                     "conditional_code_notes": conditional_code_notes(sheets, project),
                     "sheet_fill": sheet_fill(sheets)},
    }


#: advisory.sheet_fill lists a sheet in `low` when less than this share of its
#: drawing area holds a view, a panel, a slot or text.
FILL_LOW = 0.5


def _span(a: float, b: float, origin: float, step: float, n: int) -> tuple[int, int]:
    """The grid squares [first, last + 1) that the span a..b touches, clipped to 0..n."""
    return (min(n, max(0, int((a - origin) // step))), min(n, max(0, int((b - origin) // step) + 1)))


def sheet_fill(sheets, step: float = 18.0) -> dict:
    """How much of each sheet's drawing area holds a view, a fitted panel, a slot or text.

    Advisory only, never a failure: a sheet with large empty areas reads as
    amateur work (kit-sheets.md, "Composition rules"), but it is not an error.
    The drawing area is cut into squares of `step` points (1/4 in.); a square
    counts as used when a view's extents, a panel, a slot or a text box covers
    part of it. `empty_band_in` is the tallest strip across the whole drawing
    area with nothing in it.
    """
    out, low = [], []
    g = GUTTER * PT_PER_IN
    for sh in sheets:
        reg = sh["regions"]
        x0, y0, x1, y1 = reg["frame"][0] + g, reg["frame"][1] + g, reg["tb"][0] - g, reg["frame"][3] - g
        nx, ny = max(1, int((x1 - x0) // step)), max(1, int((y1 - y0) // step))
        used = bytearray(nx * ny)
        boxes = [v["bbox_pt"] for v in sh["views"]] + [t["bbox"] for t in sh["texts"]]
        boxes += [b for rid, b in reg.items() if rid.startswith(("panel:", "slot:")) and rid != "panel:side"]
        for b in boxes:
            i0, i1 = _span(b[0], b[2], x0, step, nx)
            j0, j1 = _span(b[1], b[3], y0, step, ny)
            if i1 > i0:
                for j in range(j0, j1):
                    used[j * nx + i0:j * nx + i1] = b"\x01" * (i1 - i0)
        band = run = 0
        for j in range(ny):
            run = 0 if any(used[j * nx:(j + 1) * nx]) else run + 1
            band = max(band, run)
        share = sum(used) / len(used)
        out.append({"sheet": sh["id"], "used": round(share, 2), "empty_band_in": round(band * step / PT_PER_IN, 2)})
        if share < FILL_LOW:
            low.append(sh["id"])
    return {"sheets": out, "low": low,
            "note": f"Advisory, never a failure. `low` lists sheets with less than {FILL_LOW:.0%} of the drawing "
                    "area in use. Look at each in the preview: give the views a larger scale or a bigger cell, "
                    "let panels take the space the others leave (kit-sheets.md, \"Composition rules\"), move "
                    "content from another sheet, or keep it and say why in your report."}


def image_check(sheets, project) -> dict:
    """Each placed image: its file is unchanged since the build, its source label
    prints the project.json source, a concept rendering prints the concept label
    on the image and sits in no drawing view. Warns under 100 dpi at print size."""
    import hashlib

    from .images import CONCEPT_LABEL, source_line
    fails, warns, n = [], [], 0
    entries = {e["id"]: e for e in project.data.get("images", [])}
    for sh in sheets:
        for im in sh.get("images", []):
            n += 1
            where = f"{sh['id']}: image {im.get('id')!r}"
            e = entries.get(im.get("id"))
            if e is None:
                fails.append(f"{where} is no longer in project.json images; rebuild")
                continue
            try:
                with open(project.resolve_path(e["path"]), "rb") as fh:
                    sha = hashlib.sha256(fh.read()).hexdigest()
            except (OSError, ValueError):
                fails.append(f"{where}: file {e['path']!r} is missing")
                sha = None
            if sha is not None and sha != im["sha256"]:
                fails.append(f"{where}: file {e['path']!r} changed after the build; rebuild")
            labels = [t for t in sh["texts"] if t["meta"].get("image_seq") == im["seq"]]
            src = " ".join(t["s"] for t in labels if t["meta"].get("image_label") == "source")
            if _squash(_clean(source_line(e))) not in _squash(src):
                fails.append(f"{where} does not print its source label {source_line(e)!r}")
            if e["kind"] == "concept":
                band = [t for t in labels if t["meta"].get("image_label") == "concept"
                        and t["s"] == tm.clean(CONCEPT_LABEL) and box_inside(t["bbox"], im["box"], tol=0.5)]
                if not band:
                    fails.append(f"{where} is a concept rendering without {CONCEPT_LABEL!r} on the image")
                if str(im.get("region") or "").startswith("view:"):
                    fails.append(f"{where} is a concept rendering inside a drawing view")
            elif e["kind"] != "aerial" and str(im.get("region") or "").startswith("view:"):
                fails.append(f"{where} is a {e['kind']} inside a drawing view; only an aerial map goes in a view")
            if im.get("dpi", 0) < 100:
                warns.append(f"{where} prints at {im.get('dpi')} dpi; supply a larger image for a sharp print")
    return _result(_status(fails, warns) if n else "n/a", fails + warns, images=n)


_OPS = {">=": lambda a, b, tol: a >= b - tol,
        "<=": lambda a, b, tol: a <= b + tol,
        "==": lambda a, b, tol: abs(a - b) <= tol}
_OP_WORDS = {">=": "at least", "<=": "at most", "==": "exactly"}


def _num(x: float) -> str:
    return f"{x:.4f}".rstrip("0").rstrip(".")


def _qty(x: float, unit: str, ftin: bool, denom: int, bare: bool = False, toward: str | None = None) -> str:
    """A rule-unit number for a message. A length in feet reads in feet and inches
    (3'-5 1/2"), never as decimal feet (3.4583 ft); other units keep the number."""
    if ftin:
        return fmt_ftin(x * 12.0, denom, toward)
    return _num(x) if bare else f"{_num(x)} {unit}"


def rule_counts(rows: list[dict]) -> dict:
    """How many rules_report rows pass, fail and warn."""
    return {k: sum(1 for r in rows if r["status"] == k) for k in ("pass", "fail", "warn")}


def rules_report(project) -> list[dict]:
    """Compare each drawn value that a rule in project.json names with the rule's limit.

    One row per rule, in file order. A rule checks one value (`check.value`)
    or the spread of several (`check.spread`: the largest minus the smallest).
    status is
      fail  the value is MEASURED, DERIVED, PROPOSED or MANUFACTURER (and rests
            on no unverified value) and breaks the limit; or it rests on a
            range of estimates and breaks the limit at every one of them, so no
            measurement inside the estimates could pass; or the rule cannot be
            compared (unit of another kind, a point value);
      warn  the value is missing, or rests on a PLACEHOLDER, or rests on an
            ASSUMED value and some estimate fails or comes close to the limit
            (within CLOSE, 10 %, of it, or the rule's `check.close`). The
            message says whether it would pass (with a range: at which end it
            fails), so a likely failure is not hidden;
      pass  otherwise: verified and meets the limit, or an estimate clear of
            the limit at every estimate (the FV tag still prints).
    A rule with `accepted` (the decisions-log entry, DEC-007, in which the owner
    chose to keep a design that breaks it) reports its design FAIL as WARN, so
    the set can pass QA while the row says the city must grant relief. A rule
    that cannot be compared still fails.
    The comparison converts the drawn value to the rule's unit. A length or an
    area within one part in a million of the limit counts as equal; `==`
    allows half the drawing precision for a length.
    """
    return [_accepted(r, _rule_row(project, r)) for r in project.data.get("rules", [])]


def _accepted(r, row) -> dict:
    """The owner keeps a design that breaks this rule (`accepted` names the decision)."""
    dec = row["accepted"] = r.get("accepted")
    if not dec:
        return row
    if row["status"] == "fail" and row["drawn"] is not None:
        return dict(row, status="warn", message=f"ACCEPTED BY OWNER ({dec}): {row['message']}. The owner keeps "
                                                "this design, so the city must grant relief (a variance, or a "
                                                "modification or alternate under the building code) before it "
                                                "can be approved")
    if row["status"] == "pass":
        return dict(row, message=f"{row['message']}. It no longer breaks the rule: take {dec} off the rule")
    return row


def _rule_row(project, r) -> dict:
    chk = r["check"]
    op, limit, unit = chk["op"], float(chk["limit"]), chk["unit"]
    refs = rule_refs(chk)
    spread = "spread" in chk
    cite = r.get("citation") or "no citation recorded"
    head = f"{r['id']} {r['element']} ({cite})"
    need = f"{_OP_WORDS[op]} {_num(limit)} {unit}"
    row = {"id": r["id"], "element": r["element"], "citation": r.get("citation"),
           "source_from": r.get("source_from"), "cd": r.get("cd"), "kit_key": r.get("kit_key"),
           "value": chk.get("value"), "op": op, "limit": limit, "unit": unit,
           "drawn": None, "drawn_text": None, "value_status": None, "fv": [], "range": None,
           "ok": None, "status": None}
    if spread:
        row["spread"] = refs
    vals, missing = [], []
    for ref in refs:
        try:
            vals.append(project.lookup(ref))
        except KeyError:
            missing.append(ref)
    if missing:
        return dict(row, status="warn", message=f"{head}: {', '.join(missing)} "
                                                f"{'is' if len(missing) == 1 else 'are'} not in project.json; "
                                                f"nothing to check against {need}")
    if not spread:
        row["value_status"], row["resolved_key"] = vals[0].status, vals[0].key
    else:
        row["resolved_keys"] = [v.key for v in vals]
    row["fv"] = fv_sorted(t for v in vals for t in v.fv_tags)
    points = [ref for ref, v in zip(refs, vals) if isinstance(v.v, (list, tuple))]
    if points:
        return dict(row, status="fail", message=f"{head}: {', '.join(points)} is a point, not a number; "
                                                "point the rule at one dimension")
    try:
        drawn_each = [convert(float(v), v.unit, unit) for v in vals]
        dim, factor = unit_info(unit)
    except UnitError as exc:
        return dict(row, status="fail", message=f"{head}: cannot compare {', '.join(refs)}: {exc}")
    ftin = dim == "length" and factor == 12.0

    def q(x: float, bare: bool = False, toward: str | None = None) -> str:
        return _qty(x, unit, ftin, project.denom, bare, toward)

    tol = max(abs(limit), 1.0) * 1e-6
    if spread:
        drawn = max(drawn_each) - min(drawn_each)
        if _num(max(drawn_each)) == _num(min(drawn_each)):
            text = f"spread {_num(drawn)} {unit} ({', '.join(refs)} all {_num(drawn_each[0])})"
        else:
            hi_i, lo_i = drawn_each.index(max(drawn_each)), drawn_each.index(min(drawn_each))
            text = (f"spread {_num(drawn)} {unit} (largest {refs[hi_i]} {_num(drawn_each[hi_i])}, "
                    f"smallest {refs[lo_i]} {_num(drawn_each[lo_i])})")
        row.update(drawn=drawn, drawn_text=f"{_num(drawn)} {unit}")
    else:
        val, ref = vals[0], refs[0]
        drawn = drawn_each[0]
        text = f"{_num(drawn)} {unit}"
        if val.unit == "in" and factor != 1.0:
            text = f"{fmt_ftin(float(val), project.denom, project.round_toward(val.key))} = {text}"
        elif unit_info(val.unit)[1] != factor:
            text = f"{_num(float(val))} {val.unit} = {text}"
        row.update(drawn=drawn, drawn_text=text)
        where = ref if val.key == ref[1:] else f"{ref} -> ${val.key}"
        text = f"{text} ({where})"
    if op == "==" and dim == "length":
        tol = max(tol, convert(0.5 / project.denom, "in", unit))
    ok = _OPS[op](drawn, limit, tol)
    row["ok"] = ok              # the drawn number against the limit (measure.py ranks by it)
    unverified = list(dict.fromkeys(u for v in vals for u in v.unverified_inputs))
    placeholders = [u for u in unverified if project.values[u].status == "PLACEHOLDER"]
    tags = f" {fv_text(row['fv'])}" if row["fv"] else ""
    if placeholders:
        return dict(row, status="warn", message=f"{head}: {', '.join(refs)} rests on PLACEHOLDER "
                                                f"{placeholders}{tags}; measure it, then check against {need}")
    if not unverified:
        if ok:
            return dict(row, status="pass", message=f"{head}: drawn {text} meets {need}")
        return dict(row, status="fail", message=f"{head}: drawn {text} breaks the rule; it must be {need}")
    unv = f"unverified ({', '.join(unverified)}{tags})"
    structural = str(r.get("kit_key") or "").startswith("struct:")
    if structural:
        close = math.inf                # a guessed load or span can be far off; the structural table warns too
        near = "a structural estimate, and it stays a warning however far inside the limit"
    else:
        close = float(chk["close"]) if "close" in chk else CLOSE * abs(limit)
        near = f"within {q(close, toward='up')} of the limit"
    if not project.ranged_inputs([v.key for v in vals]):
        if ok and _room(op, drawn, limit) >= close:
            return dict(row, status="pass", message=f"{head}: drawn {text} is {unv}, but even as an estimate it "
                                                    f"is clear of {need} (not {near}). Field-verify it as listed")
        if ok:
            return dict(row, status="warn", message=f"{head}: drawn {text} is {unv}; would pass against "
                                                    f"{need}, but it is {near}. Measure before you rely on it")
        return dict(row, status="warn", message=f"{head}: drawn {text} is {unv}; WOULD FAIL against {need}. "
                                                "Measure before you rely on it, or give the estimate a range "
                                                "so QA can tell whether it fails at every estimate")
    try:
        lo, hi, lower = _estimate_span(project, vals, unit, spread, drawn_each)
    except (RangeError, ExprError) as exc:
        return dict(row, status="warn", message=f"{head}: drawn {text} is {unv}; its estimates cannot be "
                                                f"tested: {exc}. Measure before you rely on it")
    row["range"] = [lo, hi]
    # Ends round outward, so a failing end never prints at the limit.
    span = q(lo) if _num(lo) == _num(hi) else f"{q(lo, bare=True, toward='down')} to {q(hi, toward='up')}"
    mono = project.monotone([v.key for v in vals])
    # `lower` can sit under every sampled spread. The ends then do not bound it.
    bounds = mono and abs(lower - lo) <= tol
    ends = [("low", lo, _OPS[op](lo, limit, tol)), ("high", hi, _OPS[op](hi, limit, tol))]
    if all(e[2] for e in ends):
        clear = min(_room(op, lo, limit), _room(op, hi, limit)) >= close
        # A spread that only shrinks between the ends still meets a cap.
        shrinks_under_cap = mono and op == "<=" and abs(lower - lo) > tol
        if (bounds or shrinks_under_cap) and clear:
            return dict(row, status="pass", message=f"{head}: drawn {text} is {unv}, but every estimate "
                                                    f"({span}) is clear of {need} (not {near}). Field-verify it "
                                                    "as listed")
        if bounds or shrinks_under_cap:
            return dict(row, status="warn", message=f"{head}: drawn {text} is {unv}; passes at every estimate "
                                                    f"({span}) against {need}, but it is {near}. Measure before "
                                                    "you rely on it")
        why = ("the spread can be smaller between the ends" if mono
               else "its formula uses abs or hypot, or min or max, so a number between the ends could fail")
        return dict(row, status="warn", message=f"{head}: drawn {text} is {unv}; the ends ({span}) meet "
                                                f"{need}, but {why}. Measure before you rely on it")
    some = (lo - tol <= limit <= hi + tol) if op == "==" else any(e[2] for e in ends)
    # A failure is sure only when every unverified input has a range and nothing
    # between the ends can pass: the samples bound the number, or a spread's
    # floor already breaks the limit.
    unranged = [u for u in unverified if not project.own_range(u)]
    lower_fails = not _OPS[op](lower, limit, tol)
    sure = not unranged and not some and (bounds or (mono and op != "==" and lower_fails))
    if not some and not sure:
        if unranged:
            why = f"{', '.join(unranged)} {'has' if len(unranged) == 1 else 'have'} no range"
        elif not mono:
            why = "its formula uses abs or hypot, or min or max, so a number between the ends could pass"
        else:
            why = "the spread can be smaller between the ends"
        return dict(row, status="warn", message=f"{head}: drawn {text} is {unv}; WOULD FAIL at every estimate "
                                                f"({span}) against {need}, but {why}. Measure before you "
                                                "rely on it")
    if not some:
        return dict(row, status="fail", message=f"{head}: drawn {text} is {unv} and breaks the rule at every "
                                                f"estimate ({span}); it must be {need}. It fails even at the "
                                                "best estimate, so measuring cannot save it: change the design")
    bad = " and ".join(f"the {name} end ({q(x, toward='down' if name == 'low' else 'up')})" for name, x, good in ends if not good)
    if not ok:
        return dict(row, status="warn", message=f"{head}: drawn {text} is {unv} and breaks {need} as drawn; "
                                                f"estimates {span} fail at {bad}. Measure before you rely on "
                                                "it, or change the design")
    return dict(row, status="warn", message=f"{head}: drawn {text} is {unv}; estimates {span} fail at {bad} "
                                            f"against {need}. Measure before you rely on it")


#: An unverified value at least this share of its limit inside the limit (at every
#: estimate) is clear of it and passes; nearer, it warns. A rule's `check.close`
#: (in the rule's unit) sets the distance for that rule instead.
CLOSE = 0.10


def _room(op, x, limit) -> float:
    """How far x sits inside the limit (negative outside); an exact (==) limit has no room."""
    return limit - x if op == "<=" else x - limit if op == ">=" else -math.inf


def _estimate_span(project, vals, unit, spread, drawn_each) -> tuple[float, float, float]:
    """(low, high, lower) of the checked quantity, in the rule's unit.

    low and high occur at a corner mix or at the drawn value. lower is a bound
    nothing in the range can go under. It equals low when those samples include
    the minimum: one value, or a spread of straight-line values on one estimate
    (also where two of them cross). Otherwise lower is a pairwise floor, which
    is not itself a spread any mix produces.
    """
    est = [[convert(x, v.unit, unit) for x, v in zip(e, vals)] for e in project.estimates([v.key for v in vals])]
    if not spread:
        xs = [e[0] for e in est]
        xs.append(drawn_each[0])
        lo, hi = min(xs), max(xs)
        return lo, hi, lo
    samples = [max(e) - min(e) for e in est]
    samples.append(max(drawn_each) - min(drawn_each))
    roots = project.ranged_inputs([v.key for v in vals])
    straight = project.monotone([v.key for v in vals])
    if len(roots) == 1 and straight:
        samples.extend(_spread_crossings(project, vals, unit, roots[0]))
    lo, hi = min(samples), max(samples)
    if len(roots) <= 1 and straight:
        return lo, hi, lo
    n = len(vals)
    # i == j keeps the floor at 0 or above. A floor that breaks the limit
    # breaks every estimate; a floor inside the limit is not a passing end.
    floor = max(min(e[i] - e[j] for e in est) for i in range(n) for j in range(n))
    return lo, hi, min(lo, floor)


def _spread_crossings(project, vals, unit, root: str) -> list[float]:
    """Spreads where two straight-line values are equal, between the one estimate's ends.

    The spread of straight lines is smallest at an end or at one of those crossings.
    """
    a, b = project.own_range(root)
    if not b > a:
        return []

    def at(t):
        return [convert(project._value_at(v.key, {root: t}), v.unit, unit) for v in vals]

    lo_v, hi_v = at(a), at(b)
    out, seen = [], []
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            denom = (hi_v[i] - lo_v[i]) - (hi_v[j] - lo_v[j])
            if abs(denom) < 1e-12:
                continue
            s = (lo_v[j] - lo_v[i]) / denom
            if s <= 1e-9 or s >= 1 - 1e-9 or any(abs(s - p) < 1e-9 for p in seen):
                continue
            seen.append(s)
            mid = at(a + s * (b - a))
            out.append(max(mid) - min(mid))
    return out


def _dig(d, path):
    for k in path:
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d


def _clean(s: str) -> str:
    try:
        return tm.clean(s)
    except ValueError:
        return s


def _squash(s: str) -> str:
    return re.sub(r"\s+", "", str(s))


def _find_run(runs, rec):
    """The PDF text run that a sidecar text record says was emitted, or None."""
    for r in runs:
        if r["s"] != rec["s"] or abs(r["size"] - rec["size"]) > 0.01:
            continue
        w = tm.text_width(r["s"], r["size"], r["bold"], r["tracking"])
        cx = r["x"] + r["matrix"][0] * w / 2
        bx = (rec["bbox"][0] + rec["bbox"][2]) / 2
        base = rec["bbox"][1] + tm.DESCENT * rec["size"]
        if abs(cx - bx) <= MATCH_PT and abs(r["y"] - base) <= MATCH_PT:
            return r, cx
    return None


#: Identifiers of the drafting workflow that a reviewer must never see on a sheet: its
#: file names, its name, and question- or decisions-log ids (Q-012, DEC-004). Mechanical matching of known
#: tokens, not a judgment about the text. FV tags (FV-3) are meant to print.
_INTERNAL = [(re.compile(r"project\.json", re.I), "the file name project.json"),
             (re.compile(r"build\.json", re.I), "the file name build.json"),
             (re.compile(r"permitkit", re.I), "the software name permitkit"),
             (re.compile(r"crossbeam_rules", re.I), "the tool name crossbeam_rules"),
             (re.compile(r"\bthe kit\b", re.I), "the words 'the kit'"),
             (re.compile(r"\bQ-\d{1,4}\b"), "a question-log id"),
             (re.compile(r"\bDEC-\d{1,4}\b"), "a decisions-log id")]


def internal_refs(sheets) -> list[str]:
    """Printed text that names the drafting workflow: a file name, the kit, a Q-### id.

    The city reviewer reads the set, not the workflow behind it. Write what the
    item is (OWNER TO CONFIRM ..., FIELD VERIFY ...) instead of where it is tracked."""
    out = []
    for sh in sheets:
        for t in sh["texts"]:
            for pat, what in _INTERNAL:
                m = pat.search(t["s"])
                if m:
                    out.append(f"{sh['id']}: text {t['s']!r} prints {what} ({m.group(0)!r}); say what the item "
                               "is, not where the drafting workflow tracks it")
                    break
    return out


def _measure_scale_bars(sh, runs) -> list[str]:
    """Measure each scale bar from the PDF: the spacing of its printed foot
    numbers against the view's printed scale label. The sidecar only says
    where to look; the numbers compared come from the PDF content."""
    fails = []
    for b in sh["scale_bars"]:
        where = f"{sh['id']}: scale bar in {b['view']}"
        label_rec = next((t for t in sh["texts"] if t["role"] == "view.scale" and t["view"] == b["view"]), None)
        found = _find_run(runs, label_rec) if label_rec else None
        if not found:
            fails.append(f"{where}: the view's scale label is not in the PDF")
            continue
        label = found[0]["s"].split("SCALE:", 1)[-1].split("   ")[0].strip()
        try:
            ratio = parse_scale_label(label)
        except ScaleError:
            fails.append(f"{where}: cannot read the printed scale label {label!r}")
            continue
        ticks = []
        for t in sh["texts"]:
            if t["role"] == "scalebar" and t["view"] == b["view"] and t["s"].isdigit():
                hit = _find_run(runs, t)
                if not hit:
                    fails.append(f"{where}: label {t['s']!r} is not in the PDF where the sidecar says")
                    continue
                ticks.append((int(t["s"]), hit[1]))
        if len(ticks) < 2 or ratio is None:
            fails.append(f"{where}: fewer than two printed foot numbers to measure")
            continue
        ticks.sort()
        (f0, x0), (f1, x1) = ticks[0], ticks[-1]
        got = (x1 - x0) / ((f1 - f0) * 12)
        want = ratio * 72
        if f1 == f0 or abs(got / want - 1) > RATIO_TOL:
            fails.append(f"{where}: measured {got:.4f} pt per inch from the PDF, the label "
                         f"{label!r} needs {want:.4f}")
    return fails


def _hand_typed_index(sheets, bound_order) -> list[str]:
    """A table that lists sheets but was not written by sheet_index().

    Flags a panel table whose first column holds two or more bound sheet ids,
    or a panel whose heading names a sheet index or list and holds table rows,
    when the kit did not write index rows there.
    """
    fails = []
    ids = set(bound_order)
    for sh in sheets:
        panels: dict = {}
        for t in sh["texts"]:
            reg = t["region"] or ""
            if reg.startswith("panel:"):
                panels.setdefault(reg, []).append(t)
        for reg, recs in panels.items():
            if any(t["role"] == "index" for t in recs):
                continue
            first_col = [t["s"].strip() for t in recs if str(t["meta"].get("group", "")).endswith(":c0")]
            heads = [t["s"].upper() for t in recs if t["meta"].get("heading")]
            named = any(("INDEX" in h or "LIST" in h) and ("SHEET" in h or "DRAWING" in h) or h.strip() == "INDEX"
                        for h in heads)
            listed = [s for s in first_col if s in ids and _SHEET_ID.fullmatch(s)]
            if len(listed) >= 2 or (named and first_col):
                fails.append(f"{sh['id']} {reg}: a typed table lists sheets ({', '.join(first_col[:6])}). "
                             "Print the index with sh.sheet_index(panel) so QA can check its order")
    return fails


def unverified_text(sheets, project) -> dict:
    """Every text group that prints an unverified value or an FV tag.

    Advisory only. The kit refuses kit.claim() notes that rest on unverified
    values; a note written another way can still read as a claim. The
    reviewing agent reads this list and judges each text.
    """
    out = []
    for (sid, _), recs in _groups(sheets).items():
        text = " ".join(r["s"] for r in recs)
        keys = []
        for r in recs:
            for k in r["keys"]:
                try:
                    if project.value(k).unverified and k not in keys:
                        keys.append(k)
                except KeyError:
                    continue
        tags = fv_parse(text)
        if keys or tags:
            out.append({"sheet": sid, "text": text, "unverified_keys": keys, "fv": tags,
                        "role": recs[0]["role"]})
    return {"groups": out,
            "note": "Advisory, never a failure. Read each text. If it states or implies that the "
                    "work complies, it must not rest on these values: rewrite it to state the "
                    "requirement and the FV tag, or measure first."}


def conditional_code_notes(sheets, project) -> dict:
    """Every printed text group whose recorded code-decision ids (the `cd`
    field of its text records, from kit.text(..., cd=...)) include an id that
    project.json `code_notes` marks with conditions.

    Advisory only. The match is on the recorded id, not on the printed text.
    The kit does not judge whether the note prints the condition; the
    reviewing agent does.
    """
    marked = {e["cd"]: e for e in project.data.get("code_notes", []) if e.get("conditions")}
    out = []
    printed: set = set()
    for (sid, _), recs in _groups(sheets).items():
        text = " ".join(r["s"] for r in recs)
        recorded = [i for r in recs for i in r.get("cd") or ()]
        ids = [i for i in dict.fromkeys(recorded) if i in marked]
        if ids:
            printed.update(ids)
            out.append({"sheet": sid, "text": text, "cd": ids,
                        "conditions": [marked[i].get("note", "") for i in ids],
                        "role": recs[0]["role"]})
    return {"groups": out,
            "not_printed": sorted(set(marked) - printed),
            "note": "Advisory, never a failure. Each note above prints from a rule with conditions. "
                    "Read it against its entry in logs/code-decisions.md: it must print the "
                    "condition with the limit, or the branch and the fact that selects it "
                    "(05-code-questions.md section 6). not_printed lists marked entries that no "
                    "printed note records with cd=."}


def _groups(sheets):
    """Text records joined by group: wrapped note lines stay together."""
    groups: dict = {}
    for sh in sheets:
        for t in sh["texts"]:
            g = t["meta"].get("group") or f"t{t['seq']}"
            groups.setdefault((sh["id"], g), []).append(t)
    return groups


_BARE_NUMBER = re.compile(r"\d+\.\d+")


def _printed_numbers(project, keys) -> list[float]:
    """The numbers of the value keys a note printed (points and unknown keys skipped)."""
    out = []
    for k in keys if project is not None else ():
        try:
            v = project.lookup(k)
            out.append(float(v))
        except (KeyError, TypeError, ValueError):
            continue
    return out


def citations(sheets, project=None) -> dict:
    """Every code citation string, grouped by the note it sits in. Extraction only.

    With the project, a bare number such as "12.9" that is the printed value of a
    key the note records (a rake angle, an area) is not listed: it came from
    project.json, not from a code.
    """
    groups = []
    by_ref: dict = {}
    seen: dict = {}
    for (sid, _), recs in _groups(sheets).items():
        text = " ".join(r["s"] for r in recs)
        keys = [k for r in recs for k in r.get("keys") or ()]
        printed = _printed_numbers(project, keys)
        # "RAKE 12.9" names the value. "CEC 210.8" is a section even when a
        # value on the same note is within a tenth of 210.8.
        names = {k.lstrip("$").upper() for k in keys}
        found = []
        for m in _CITE.finditer(text):
            code = m.group("code") or ""
            if code.upper() in _NOT_CODE:
                code = ""
            ref = re.sub(r"\s+", " ", m.group("ref")).strip()
            own_value = not code or code.upper() in names
            if (own_value and _BARE_NUMBER.fullmatch(ref)
                    and any(abs(float(ref) - x) < 10 ** -len(ref.rpartition(".")[2]) for x in printed)):
                continue                # a bare number within one unit of its last digit: the value, not a code
            found.append((code + " " + ref).strip())
            key = re.sub(r"^(?:§|SECTION|SEC\.)\s*", "", ref)
            by_ref.setdefault(key, []).append({"sheet": sid, "as_printed": (code + " " + ref).strip(),
                                               "text": text})
        if not found:
            continue
        if text in seen:
            seen[text]["sheets"].append(sid)
            continue
        g = {"text": text, "sheets": [sid], "citations": found}
        seen[text] = g
        groups.append(g)
    return {"groups": groups, "by_reference": dict(sorted(by_ref.items())),
            "note": "Extracted strings only. Judge consistency (same topic, same section, "
                    "same code edition) against CrossBeam or the primary text."}
