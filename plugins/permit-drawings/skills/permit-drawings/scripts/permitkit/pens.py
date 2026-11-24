"""The line-weight and text-size standard every kit helper draws with.

A professional set reads at a glance because line weight says what a line is:
what the cut passes through is heaviest, what lies beyond is lighter, and
dimensions, hatching and notes are finest. Widths are paper points, so a pen
draws the same at every scale (1 pt = 0.35 mm).

Use a pen by name:

    v.line(x0, y0, x1, y1, **pens.kw("cut"))
    v.rect(x0, y0, x1, y1, **pens.kw("beyond", status="ASSUMED"))   # grey dashed

`status` follows STATUS_STYLE: an unverified line keeps its pen width but turns
grey and dashed, so it still reads as unverified.
"""
from __future__ import annotations

from .display import GREY, INK, INK2, LIGHT, STATUS_STYLE

#: name -> (width pt, colour, dash or None, what it is for)
PENS = {
    "cut":      (1.6, INK, None, "walls and anything the plan or section cut passes through"),
    "cut_med":  (1.1, INK, None, "cut lines of thin parts: jambs, slabs and sheathing in a section"),
    "grade":    (2.2, INK, None, "finish grade in a section or elevation"),
    "profile":  (1.4, INK, None, "outline of a building in elevation"),
    "object":   (0.8, INK, None, "door leaves, cabinets, fixtures, stairs, items seen in plan"),
    "beyond":   (0.55, INK, None, "edges seen beyond the cut; elevation surfaces and trim"),
    "fine":     (0.35, INK, None, "glass lines, sashes, door swings, light detail"),
    "hatch":    (0.25, INK2, None, "material hatching and stipple"),
    "dim":      (0.35, INK2, None, "dimension lines"),
    "ext":      (0.3, INK2, None, "extension lines"),
    "tick":     (0.9, INK, None, "dimension ticks"),
    "annot":    (0.5, INK, None, "leaders, tags, symbols"),
    "hidden":   (0.5, INK2, (4.0, 2.5), "hidden or overhead items"),
    "center":   (0.35, INK2, (14.0, 3.0, 3.0, 3.0), "centre lines and grid lines"),
    "property": (1.0, INK, (18.0, 3.0, 3.0, 3.0, 3.0, 3.0), "property lines"),
    "demo":     (0.8, INK, (5.0, 3.0), "construction to be removed"),
    "light":    (0.35, LIGHT, None, "background context: neighbouring buildings, existing to remain at a site scale"),
    "frame":    (0.8, INK, None, "title block rules and table frames"),
    "border":   (2.0, INK, None, "the sheet border"),
}

#: Text sizes in points, largest first. A sheet reads best with three or four of them.
TEXT = {
    "sheet_number": 34.0,   # the sheet id in the title block
    "sheet_title": 14.0,    # sheet title in the title block
    "view_title": 11.0,     # title under a drawing
    "heading": 9.5,         # panel and notes headings
    "room": 9.0,            # room names
    "label": 7.5,           # leaders and labels in a view
    "note": 7.0,            # notes, table cells
    "dim": 7.5,             # dimension text
    "small": 6.0,           # sub-labels, scale bar numbers
}


def width(name: str) -> float:
    return PENS[_check(name)][0]


def _check(name: str) -> str:
    if name not in PENS:
        raise ValueError(f"unknown pen {name!r}; pens: {', '.join(PENS)}")
    return name


def kw(name: str, status: str | None = None, **extra) -> dict:
    """Drawing keywords (stroke, width, dash) for a named pen.

    status: a value status. ASSUMED and PLACEHOLDER keep the width and take the
    grey dashed style, so an unverified line still reads as unverified.
    Extra keywords (fill, layer ...) pass through and win.
    """
    w, color, dash, _ = PENS[_check(name)]
    out = {"stroke": color, "width": w}
    if dash:
        out["dash"] = dash
    if status:
        st = STATUS_STYLE.get(status, STATUS_STYLE["MEASURED"])
        if st["dash"]:
            out["stroke"] = GREY
            out["dash"] = st["dash"]
    out.update(extra)
    return out


def table() -> list[tuple]:
    """The pen standard as rows (name, width pt, width mm, use), for a legend or the docs."""
    return [(n, w, round(w * 25.4 / 72, 2), use) for n, (w, _c, _d, use) in PENS.items()]
