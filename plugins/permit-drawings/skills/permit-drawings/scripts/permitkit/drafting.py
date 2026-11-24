"""Drafting-standard checks: what a plan checker reads a sheet by before reading a number.

A set gets sent back, or read with suspicion, when every line is one weight,
when a section shows no materials, when a plan is filled in colours that turn
to mud on a black-and-white print, or when a load-carrying connection is drawn
with nothing behind it. These checks read the build sidecar (build.json); the
kit records what they need when it builds a sheet:

  line_weights  fail: a true-scale drawing has no line at a cut weight;
                warn: every line in it is about one weight. Walls and members the
                cut passes through take the "cut" pen, edges seen beyond take
                "beyond", dimensions and hatching are finest (pens.py).
  hatching      fail: a drawing has solid cut-weight lines but no material at
                all (no hatch, no poche fill); warn: a hatched material is in no
                legend in the set.
  grayscale     fail: a true-scale drawing fills an area in colour. Cities
                print and scan in black and white; use a grey or a hatch.
  view_scale    warn: a view placed by hand at a fixed scale fits its own cell
                at a larger standard scale.
  connections   warn: a connection in project.json `connections` still has no
                basis (maker's tested detail or engineer's calculation), or is
                on no sheet.

Every check is mechanical: it reads widths, fills, hatches and slot records,
never the words of a title or note. Which lines are cut is the drafter's call;
the kit only checks the weights say something.
"""
from __future__ import annotations

from . import pens
from .display import LAYERS, WHITE, rgb
from .units import scale_kind

#: The lightest pen that reads as cut. "cut" is 1.6 pt and "cut_med" 1.1 pt;
#: "profile" (1.4 pt, an elevation outline) also counts as a heavy line.
CUT_MIN = pens.width("cut_med")
#: Pen widths that mean the cut passes through the part (pens.py).
CUT_WIDTHS = (pens.width("cut"), pens.width("cut_med"))
#: A drawing needs at least this many stroked paths before line weight is judged.
MIN_LINES = 3
#: The heaviest line must be at least this many times the lightest.
WEIGHT_RATIO = 2.0
#: A fill whose largest minus smallest colour channel exceeds this is a colour.
CHROMA_MAX = 0.06

_GEOM = (LAYERS["back"], LAYERS["geom"])


def _hex(c) -> str:
    return "#" + "".join(f"{int(round(v * 255)):02x}" for v in c)


def view_linework(page, view_ids) -> dict:
    """What each view draws, for the sidecar: {view id: {widths, cut, fills, hatch}}.

    widths  {"<pt>": count} of stroked building lines (layers back and geom)
    cut     solid lines at a cut pen width (a dashed line, such as a property
            line, is never cut)
    fills   colours that fill an area in the view (white left out), sorted
    hatch   materials hatched in the view (hatch.py; "hatch" for View.hatch), sorted
    """
    out = {vid: {"widths": {}, "cut": 0, "fills": set(), "hatch": set()} for vid in view_ids}
    for op in page.ops:
        rec = out.get(op.get("region"))
        if rec is None or op["k"] != "path" or op["layer"] not in _GEOM:
            continue
        if op["stroke"] is not None and op["lw"] > 0:
            key = f"{op['lw']:.2f}"
            rec["widths"][key] = rec["widths"].get(key, 0) + 1
            if not op["dash"] and any(abs(op["lw"] - w) < 0.005 for w in CUT_WIDTHS):
                rec["cut"] += 1
        if op["fill"] is not None and tuple(op["fill"]) != rgb(WHITE):
            rec["fills"].add(_hex(op["fill"]))
    for h in page.hatches:
        if h["region"] in out:
            out[h["region"]]["hatch"].add(h["material"])
    return {vid: {"widths": dict(sorted(r["widths"].items())), "cut": r["cut"], "fills": sorted(r["fills"]),
                  "hatch": sorted(r["hatch"])} for vid, r in out.items()}


def _chroma(hexcolor: str) -> float:
    c = rgb(hexcolor)
    return max(c) - min(c)


def _grey_for(hexcolor: str) -> str:
    """The grey with the same luminance, so a colour fill can be swapped one for one."""
    r, g, b = rgb(hexcolor)
    y = 0.299 * r + 0.587 * g + 0.114 * b
    return _hex((y, y, y))


def _name(sh, v) -> str:
    return f"{sh['id']} view {v['number']} '{v['title']}'"


def _drawings(sheets):
    """(sheet, view, linework) for every true-scale view with a linework record."""
    for sh in sheets:
        for v in sh["views"]:
            if v["true_scale"] and v.get("linework"):
                yield sh, v, v["linework"]


def line_weights(sheets) -> tuple[list, list]:
    fails, warns = [], []
    for sh, v, lw in _drawings(sheets):
        widths = {float(k): n for k, n in lw["widths"].items()}
        if sum(widths.values()) < MIN_LINES:
            continue
        heavy, light = max(widths), min(widths)
        if heavy < CUT_MIN - 1e-6:
            fails.append(f"{_name(sh, v)}: no line is heavier than {heavy:g} pt, so nothing reads as cut. "
                         "Draw walls, posts, slabs and members the cut passes through with pens.kw(\"cut\") "
                         "(thin cut parts \"cut_med\"; an elevation outline \"profile\"), edges seen beyond "
                         "with \"beyond\", and dimensions and hatching stay fine")
        elif heavy < WEIGHT_RATIO * light - 1e-6:
            # all heavy is a weaker sign (a key plan of walls only); it warns
            warns.append(f"{_name(sh, v)}: every line is {light:g} to {heavy:g} pt, about one weight. Keep "
                         "\"cut\" for what the cut passes through and draw what is seen beyond with "
                         "\"beyond\" or \"object\" and fine detail with \"fine\" (pens.py)")
    return fails, warns


def hatching(sheets) -> tuple[list, list]:
    fails, warns = [], []
    drawn = {}
    legend = {k[6:] for sh in sheets for k in sh.get("legend_kinds", []) if k.startswith("hatch:")}
    for sh, v, lw in _drawings(sheets):
        for m in lw["hatch"]:
            drawn.setdefault(m, sh["id"])
        if lw.get("cut") and not lw["hatch"] and not lw["fills"]:
            fails.append(f"{_name(sh, v)}: has cut lines but no material: no hatch and no poche. Hatch "
                         "each cut material (hatch.fill, hatch.layers for a build-up: wood, plywood, "
                         "concrete, tile, batt, gypsum ...) and poche cut walls in plan. If nothing in this "
                         "drawing is cut (an elevation, a site plan), draw it with \"profile\" and \"beyond\" "
                         "instead")
    # "hatch" is View.hatch's plain pattern: the legend's plain "hatch" row names it, so no check
    missing = sorted(m for m in drawn if m not in legend and m != "hatch")
    if missing:
        warns.append("hatched materials in no legend in the set: " +
                     ", ".join(f"{m} (first on {drawn[m]})" for m in missing) +
                     ". Add a legend row \"hatch:<material>\" for each (Panel.legend)")
    return fails, warns


def grayscale(sheets) -> tuple[list, list]:
    fails = []
    for sh, v, lw in _drawings(sheets):
        colours = [c for c in lw["fills"] if _chroma(c) > CHROMA_MAX]
        if colours:
            swap = ", ".join(f"{c} -> {_grey_for(c)}" for c in colours)
            fails.append(f"{_name(sh, v)}: fills areas in colour ({swap}). Cities print and scan in "
                         "black and white, where colours turn to the same grey; use a grey (the swap "
                         "shown keeps the same darkness) or a hatch, and name it in the legend. A colour "
                         "rendering belongs in a 3D view")
    return fails, []


def view_scale(sheets) -> tuple[list, list]:
    warns = []
    for sh in sheets:
        for v in sh["views"]:
            if v.get("fits_larger"):
                kind = scale_kind(v["scale"])
                if kind == "eng":
                    how = "place it at that scale (sh.largest_scale(extents, cell, engineering=True))"
                elif kind == "size":
                    # scale="fit" stays architectural, and largest_scale has no size family.
                    how = (f"pass scale=\"{v['fits_larger']}\" to sh.view; scale=\"fit\" and "
                           "largest_scale do not pick a size scale")
                else:
                    how = "pass scale=\"fit\" or let layout.arrange choose"
                warns.append(f"{_name(sh, v)}: placed at {v['scale']}, but its cell holds it at "
                             f"{v['fits_larger']}; {how}, so the drawing fills its space")
    return [], warns


def connections(sheets, project) -> tuple[list, list]:
    warns = []
    shown = {t["meta"].get("connection") for sh in sheets for t in sh["texts"]
             if t["role"] == "connection" and t.get("meta")}
    for c in project.data.get("connections", []):
        if c["basis"] == "open":
            warns.append(f"connection {c['id']} ({c['what']}): no basis yet. Building will ask for the maker's "
                         "tested detail (with its evaluation report and rated load) or an engineer's "
                         "calculation; ask the owner which, and record it in `basis` and `evidence`")
        if c["id"] not in shown:
            warns.append(f"connection {c['id']} is on no sheet; give it a spot with sh.connection(\"{c['id']}\", "
                         "cell) next to the drawing that shows it")
    return [], warns


def checks(sheets, project) -> dict:
    """{check name: (fails, warns)} for qa.run(). A sidecar from an older kit
    (no linework recorded) warns once instead of judging nothing."""
    if any("linework" not in v for sh in sheets for v in sh["views"]):
        rebuild = ([], ["build.json records no linework (an older kit wrote it); rebuild with this kit version"])
        return {"line_weights": rebuild, "hatching": rebuild, "grayscale": rebuild,
                "view_scale": ([], []), "connections": connections(sheets, project)}
    return {"line_weights": line_weights(sheets), "hatching": hatching(sheets),
            "grayscale": grayscale(sheets), "view_scale": view_scale(sheets),
            "connections": connections(sheets, project)}
