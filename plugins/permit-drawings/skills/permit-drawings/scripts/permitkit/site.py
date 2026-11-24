"""Site-plan symbols: property lines, setbacks, building footprints, paving,
street centrelines and the distances a plan checker measures on a site plan.

Positions are real inches, x east and y north, like a floor plan. A site plan
is usually drawn at 1" = 10'-0" (0.6 pt per real inch) or 1/8" = 1'-0".

Every printed length comes from a model Value, so an assumed lot line or an
assessor-map dimension prints with its FV tag.
"""
from __future__ import annotations

import math

from . import pens
from . import textmetrics as tm
from .annot import DIM_SIZE, dim_label
from .display import DIM, GREY, INK, INK2, POCHE_E, POCHE_N, WHITE, View, poly_segments, rect_segments
from .model import Value

#: Long-short-short: the drafting convention for a property line. The dashes
#: are the pens standard's (pens.PENS "property" and "center").
PL_DASH = pens.PENS["property"][2]
CENTER_DASH = pens.PENS["center"][2]
SETBACK_DASH = (6.0, 3.0)


def _unverified(*vals) -> bool:
    return any(isinstance(x, Value) and x.unverified for x in vals)


def _edge_text(v: View, a, b, text, keys=(), fv=(), offset_pt: float = 6.0, size: float = DIM_SIZE,
               color=INK, bold=False, outside: int = 1, role="site"):
    """Text centred along the edge a->b, rotated to read with it, offset to one side."""
    pa, pb = v.P(*a), v.P(*b)
    ang = math.degrees(math.atan2(pb[1] - pa[1], pb[0] - pa[0]))
    # keep text upright: read left to right or bottom to top
    if ang > 90.0 + 1e-6 or ang <= -90.0 + 1e-6:
        pa, pb = pb, pa
        ang = math.degrees(math.atan2(pb[1] - pa[1], pb[0] - pa[0]))
        outside = -outside
    mx, my = (pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2
    r = math.radians(ang)
    nx, ny = -math.sin(r), math.cos(r)          # left normal of the (upright) run
    if outside < 0:
        off = -(offset_pt + size * tm.ASCENT)
    else:
        off = offset_pt
    x, y = mx + nx * off, my + ny * off
    return v.paper_text(x, y, text, size=size, bold=bold, anchor="middle", rot=ang, color=color,
                        role=role, keys=keys, fv=fv)


def _ring_orientation(pts) -> float:
    """Signed area: positive for a counter-clockwise ring."""
    return sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1]
               for i in range(len(pts))) / 2


def property_line(v: View, pts, lengths=None, bearings=None, closed: bool = True, label_size: float = 8.0,
                  width: float = 1.6):
    """The lot boundary as a heavy long-short-short line.

    pts       corners in real inches, in order around the lot.
    lengths   one Value per edge (or None to skip an edge). Each prints outside
              the lot along its edge, with its FV tag when unverified. Take them
              from the survey, the deed or the assessor map, with that source.
    bearings  optional text per edge, e.g. "N 89°59'00\\" E", printed under the length.
    A lot line whose length is unverified draws grey.
    """
    pts = [(float(x), float(y)) for x, y in pts]
    n = len(pts)
    edges = n if closed else n - 1
    lengths = list(lengths) if lengths is not None else [None] * edges
    bearings = list(bearings) if bearings is not None else [None] * edges
    if len(lengths) != edges or len(bearings) != edges:
        raise ValueError(f"property_line has {edges} edges; give one length and one bearing (or None) per edge")
    ccw = _ring_orientation(pts) > 0 if closed else True
    recs = []
    for i in range(edges):
        a, b = pts[i], pts[(i + 1) % n]
        L = lengths[i]
        grey = _unverified(L)
        v.line(*a, *b, stroke=GREY if grey else INK, width=width, dash=PL_DASH)
        # outside of a CCW ring is to the right of each edge
        side = -1 if ccw else 1
        if L is not None:
            text, keys, tags = dim_label(v, L, "ftin")
            recs.append(_edge_text(v, a, b, text, keys, tags, offset_pt=7.0, size=label_size,
                                   color=DIM if tags else INK, bold=True, outside=side))
        if bearings[i]:
            recs.append(_edge_text(v, a, b, bearings[i], offset_pt=7.0 + label_size + 3, size=label_size * 0.85,
                                   color=INK2, outside=side))
    return recs


def setback_line(v: View, pts, label: str | None = None, at: int = 0):
    """A required-setback line, thin dashed. Label it with the setback name
    (e.g. "REAR SETBACK"); dimension the distance with annot.dim_chain or
    site.distance from the property line. `at` picks the edge for the label."""
    pts = [(float(x), float(y)) for x, y in pts]
    v.polyline(pts, stroke=INK2, width=0.6, dash=SETBACK_DASH, layer="annot")
    if label:
        a, b = pts[at], pts[at + 1]
        return _edge_text(v, a, b, label, offset_pt=3.0, size=6.0, color=INK2, outside=1)
    return None


def footprint(v: View, pts, action: str = "existing", label: str | None = None, lines=(), hatch: bool | None = None,
              label_at=None, size: float = 8.0):
    """A building outline (roof or wall line) on the site plan.

    action  existing: light grey fill; new: hatched with a heavy outline;
            demo: dashed outline, no fill.
    label   e.g. "(E) RESIDENCE"; `lines` print under it (stories, area, use).
    """
    pts = [(float(x), float(y)) for x, y in pts]
    if action == "existing" or action == "relocate":
        v.polygon(pts, stroke=INK, width=1.2, fill=POCHE_E)
    elif action == "new":
        v.polygon(pts, stroke=INK, width=1.8, fill=WHITE)
        if hatch is None or hatch:
            v.hatch(pts, angle=45, spacing_pt=5.0, stroke=POCHE_N, width=0.4)
    elif action == "demo":
        v.polygon(pts, stroke=INK, width=1.0, dash=(5.0, 3.0))
    else:
        raise ValueError(f"action {action!r} is not existing, new, demo or relocate")
    recs = []
    if label:
        cx = label_at[0] if label_at else sum(p[0] for p in pts) / len(pts)
        cy = label_at[1] if label_at else sum(p[1] for p in pts) / len(pts)
        block = [(label, size, True)] + [(ln, size * 0.78, False) for ln in lines]
        total = sum(s * 1.25 for _, s, _ in block)
        px, py = v.P(cx, cy)
        y = py + total / 2 - block[0][1]
        widest = max(tm.text_width(tm.clean(str(t)), s, b) for t, s, b in block)
        # a white mask so the label reads over the hatch
        v.paper_path(rect_segments(px - widest / 2 - 4, py - total / 2 - 2,
                                   px + widest / 2 + 4, py + total / 2 + 2),
                     stroke=None, fill=WHITE, layer="annot")
        for t, s, b in block:
            recs.append(v.paper_text(px, y, t, size=s, bold=b, anchor="middle", color=INK if b else INK2,
                                     role="site", keys=getattr(t, "keys", ()), fv=getattr(t, "fv", ())))
            y -= s * 1.25
    return recs


def paving(v: View, pts, label: str | None = None, kind: str = "concrete"):
    """A paved area: driveway, walk or patio. kind 'concrete' stipples, 'deck' hatches."""
    pts = [(float(x), float(y)) for x, y in pts]
    v.polygon(pts, stroke=INK2, width=0.6)
    if kind == "deck":
        v.hatch(pts, angle=0, spacing_pt=3.0, stroke=GREY, width=0.3)
    else:
        v.hatch(pts, angle=45, spacing_pt=7.0, stroke=GREY, width=0.25, dash=(1.0, 4.0))
    if label:
        cx = sum(p[0] for p in pts) / len(pts)
        cy = sum(p[1] for p in pts) / len(pts)
        w = tm.text_width(label, 6.5, False)
        px, py = v.P(cx, cy)
        v.paper_path(rect_segments(px - w / 2 - 3, py - 4, px + w / 2 + 3, py + 8),
                     stroke=None, fill=WHITE, layer="annot")
        return v.paper_text(px, py, label, size=6.5, anchor="middle", color=INK2, role="site")
    return None


def centerline(v: View, a, b, label: str = "CENTERLINE OF STREET"):
    """A street or alley centreline, dash-dot, labelled along its length."""
    v.line(*a, *b, stroke=INK2, width=0.6, dash=CENTER_DASH, layer="annot")
    return _edge_text(v, a, b, label, offset_pt=3.0, size=6.5, color=INK2) if label else None


def street_label(v: View, at, name: str, rot: float = 0.0, size: float = 10.0):
    """A street name in large spaced capitals."""
    px, py = v.P(*at)
    return v.paper_text(px, py, name, size=size, bold=True, anchor="middle", rot=rot, color=INK2,
                        tracking=1.5, role="site")


def distance(v: View, a, b, value, side: int = 1, size: float = 7.0, label: str = ""):
    """An aligned dimension between two real points (any direction): arrows at
    both ends and the Value's text along the line. Use it for a setback or a
    separation that is not axis-aligned; annot.dim_chain covers the rest."""
    text, keys, tags = dim_label(v, value, "ftin", label)
    pa, pb = v.P(*a), v.P(*b)
    v.paper_path([("M", *pa), ("L", *pb)], stroke=INK2, width=0.5, layer="annot")
    ang = math.atan2(pb[1] - pa[1], pb[0] - pa[0])
    for (x, y), d in ((pa, 1), (pb, -1)):
        ca, sa = math.cos(ang) * d, math.sin(ang) * d
        tip = (x, y)
        p1 = (x + 6 * ca - 2 * sa, y + 6 * sa + 2 * ca)
        p2 = (x + 6 * ca + 2 * sa, y + 6 * sa - 2 * ca)
        v.paper_path(poly_segments([tip, p1, p2], closed=True), stroke=None, fill=INK2, layer="annot")
    return _edge_text(v, a, b, text, keys, tags, offset_pt=2.5, size=size, color=DIM if tags else INK2,
                      outside=side, role="dim")


def utility(v: View, at, label: str, r: float = 5.0, side: str = "E"):
    """A small labelled circle for a utility point: meter, cleanout, panel, hose bib.
    side: compass side of the circle the label sits on ('E', 'W', 'N' or 'S')."""
    px, py = v.P(*at)
    v.circle_pt(*at, r, stroke=INK, width=0.7, fill=WHITE)
    x, y, anchor = {"E": (px + r + 3, py - 2.5, "start"), "W": (px - r - 3, py - 2.5, "end"),
                    "N": (px, py + r + 3, "middle"), "S": (px, py - r - 7.5, "middle")}[side]
    return v.paper_text(x, y, label, size=6.0, color=INK2, anchor=anchor, role="site")
