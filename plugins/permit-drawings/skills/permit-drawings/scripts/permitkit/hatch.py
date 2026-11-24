"""Material hatching for sections, details and site plans.

A plan checker reads a section by its hatching: concrete stipple, earth below
grade, batt insulation loops in the stud cavity, an X through cut lumber. The
patterns here are the common US architectural ones. Their size is in paper
points, so a pattern reads the same at 1/2" = 1'-0" and at 3" = 1'-0".

    from permitkit import hatch
    hatch.fill(v, [(0, 0), (15, 0), (15, -8), (0, -8)], "concrete", outline="cut")
    hatch.rect(v, 0, 0, 3.5, 96, "batt")                 # stud cavity
    hatch.grade(v, -60, 200, 0, depth_pt=16)             # grade line with earth below

Every pattern is clipped to its outline. Hatching never counts as linework in
the text-over-geometry check, so labels still need leaders, not hatching, to
stay readable. Random-looking patterns (concrete, gravel, sand) come from a
fixed seed taken from the shape, so every build draws the same bytes.

Materials: see MATERIALS (name -> description). `hatch.MATERIALS` also feeds
the legend kind "hatch:<name>" in Panel.legend.

This is the kit's one set of material patterns: section.grade, earth,
concrete, insulation and wood_cut are short aliases of the calls here.
"""
from __future__ import annotations

import math

from . import pens
from .display import INK, INK2, WHITE, circle_segments, points_box, poly_segments, rect_segments

MATERIALS = {
    "concrete": "CONCRETE",
    "earth": "EARTH / UNDISTURBED SOIL",
    "fill": "COMPACTED FILL",
    "gravel": "GRAVEL / CRUSHED ROCK",
    "sand": "SAND",
    "mortar": "MORTAR / GROUT",
    "plaster": "STUCCO / PLASTER",
    "batt": "BATT INSULATION",
    "rigid": "RIGID INSULATION",
    "masonry": "BRICK / MASONRY",
    "cmu": "CONCRETE MASONRY UNIT",
    "wood": "WOOD, CONTINUOUS (CUT)",
    "blocking": "WOOD BLOCKING / SHIM",
    "plywood": "PLYWOOD / OSB SHEATHING",
    "gypsum": "GYPSUM BOARD",
    "steel": "STEEL",
    "tile": "TILE",
    "planting": "PLANTING / LAWN",
    "pavers": "PAVERS",
    "solid": "SOLID (NEW WALL / STEEL PLATE)",
}


class _Rand:
    """A small linear congruential generator: same seed, same numbers, any Python."""

    def __init__(self, seed: int):
        self.s = (seed * 2654435761 + 12345) & 0xFFFFFFFF or 1

    def __call__(self) -> float:
        self.s = (1103515245 * self.s + 12345) & 0x7FFFFFFF
        return self.s / 0x7FFFFFFF


def _seed(poly) -> int:
    return int(sum(abs(x) * 7 + abs(y) * 13 for x, y in poly) * 10) & 0xFFFFFF


def _axes(poly):
    """Long axis unit vector, cross axis unit vector, length and thickness of a polygon's box."""
    x0, y0, x1, y1 = points_box(poly)
    w, h = x1 - x0, y1 - y0
    if w >= h:
        return (1.0, 0.0), (0.0, 1.0), w, h, (x0, (y0 + y1) / 2)
    return (0.0, 1.0), (-1.0, 0.0), h, w, ((x0 + x1) / 2, y0)


def _parallel(poly, angle, spacing, offsets=(0.0,)):
    x0, y0, x1, y1 = points_box(poly)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    half = math.hypot(x1 - x0, y1 - y0) / 2 + 1
    a = math.radians(angle)
    dx, dy = math.cos(a), math.sin(a)
    nx, ny = -dy, dx
    segs = []
    k = -half
    while k <= half:
        for off in offsets:
            px, py = cx + nx * (k + off), cy + ny * (k + off)
            segs += [("M", px - dx * half, py - dy * half), ("L", px + dx * half, py + dy * half)]
        k += spacing
    return segs


def _jitter_grid(poly, step, rnd):
    x0, y0, x1, y1 = points_box(poly)
    y = y0 + step / 2
    while y < y1:
        x = x0 + step / 2
        while x < x1:
            yield x + (rnd() - 0.5) * step * 0.9, y + (rnd() - 0.5) * step * 0.9
            x += step
        y += step


def _dots(points, r):
    segs = []
    for x, y in points:
        segs += circle_segments(x, y, r)
    return segs


def _pattern(poly, material, k, rnd):
    """(stroke segments, filled segments) for a material in paper points; k scales the pattern."""
    st, fl = [], []
    if material == "masonry":
        st = _parallel(poly, 45, 3.6 * k)
    elif material == "cmu":
        st = _parallel(poly, 45, 5.0 * k) + _parallel(poly, 135, 20.0 * k)
    elif material == "steel":
        st = _parallel(poly, 45, 4.5 * k, offsets=(0.0, 1.3 * k))
    elif material == "earth" or material == "fill":
        c = 6.5 * k
        a = math.radians(45)
        u, v = (math.cos(a), math.sin(a)), (-math.sin(a), math.cos(a))
        x0, y0, x1, y1 = points_box(poly)
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        n = int(math.hypot(x1 - x0, y1 - y0) / c / 2) + 2
        for i in range(-n, n + 1):
            for j in range(-n, n + 1):
                ox = cx + (i * u[0] + j * v[0]) * c
                oy = cy + (i * u[1] + j * v[1]) * c
                # a cell spans c along u and v from its origin; skip cells clear of the
                # outline's box (a long grade band would otherwise draw a square of hatch)
                if ox + c * 1.5 < x0 or ox - c * 1.5 > x1 or oy + c * 1.5 < y0 or oy - c * 1.5 > y1:
                    continue
                along, across = (u, v) if (i + j) % 2 == 0 else (v, u)
                for f in (0.2, 0.5, 0.8) if material == "earth" else (0.5,):
                    sx = ox + across[0] * f * c
                    sy = oy + across[1] * f * c
                    st += [("M", sx, sy), ("L", sx + along[0] * c, sy + along[1] * c)]
        if material == "fill":
            fl = _dots([p for p in _jitter_grid(poly, 3.4 * k, rnd) if rnd() < 0.5], 0.32 * k)
    elif material == "concrete":
        for x, y in _jitter_grid(poly, 5.0 * k, rnd):
            r = rnd()
            if r < 0.42:
                fl += circle_segments(x, y, 0.33 * k)
            elif r < 0.72:
                s = (1.6 + rnd() * 1.4) * k
                a0 = rnd() * math.tau
                pts = [(x + s * math.cos(a0 + i * math.tau / 3), y + s * math.sin(a0 + i * math.tau / 3))
                       for i in range(3)]
                st += poly_segments(pts, closed=True)
        fl += _dots([p for p in _jitter_grid(poly, 3.0 * k, rnd) if rnd() < 0.35], 0.22 * k)
    elif material == "gravel":
        for x, y in _jitter_grid(poly, 5.2 * k, rnd):
            r0 = (1.0 + rnd() * 1.3) * k
            n = 6
            a0 = rnd() * math.tau
            pts = [(x + r0 * (0.75 + 0.35 * rnd()) * math.cos(a0 + i * math.tau / n),
                    y + r0 * (0.75 + 0.35 * rnd()) * math.sin(a0 + i * math.tau / n)) for i in range(n)]
            st += poly_segments(pts, closed=True)
    elif material in ("sand", "mortar", "plaster"):
        step = {"sand": 2.6, "mortar": 2.0, "plaster": 2.2}[material] * k
        fl = _dots([p for p in _jitter_grid(poly, step, rnd) if rnd() < 0.75], 0.3 * k)
    elif material == "gypsum":
        fl = _dots([p for p in _jitter_grid(poly, 3.2 * k, rnd) if rnd() < 0.55], 0.3 * k)
    elif material == "batt":
        d, n, length, t, o = _axes(poly)
        # a prolate cycloid: loops that touch both faces of the cavity
        amp = t / 2 * 0.92
        rr = max(t * 0.16, 0.6)
        pts = []
        th = -math.pi
        while True:
            s = rr * th - amp * 0.62 * math.sin(th)
            if s > length + t:
                break
            c = -amp * math.cos(th)
            pts.append((o[0] + d[0] * s + n[0] * c, o[1] + d[1] * s + n[1] * c))
            th += math.pi / 14
        st = poly_segments(pts)
    elif material == "rigid":
        d, n, length, t, o = _axes(poly)
        pts = []
        s, i = 0.0, 0
        while s <= length + t:
            c = (t / 2) * (1 if i % 2 == 0 else -1)
            pts.append((o[0] + d[0] * s + n[0] * c, o[1] + d[1] * s + n[1] * c))
            s += t * 0.7
            i += 1
        st = poly_segments(pts)
    elif material in ("wood", "blocking"):
        x0, y0, x1, y1 = points_box(poly)
        st = [("M", x0, y0), ("L", x1, y1)]
        if material == "wood":
            st += [("M", x0, y1), ("L", x1, y0)]
    elif material == "plywood":
        d, n, length, t, o = _axes(poly)
        layers = max(2, min(5, int(t / (1.2 * k))))
        for i in range(1, layers):
            c = -t / 2 + t * i / layers
            a = (o[0] + n[0] * c, o[1] + n[1] * c)
            st += [("M", a[0], a[1]), ("L", a[0] + d[0] * length, a[1] + d[1] * length)]
    elif material == "tile":
        st = _parallel(poly, 0, 4.0 * k) + _parallel(poly, 90, 4.0 * k)
    elif material == "pavers":
        st = _parallel(poly, 0, 9.0 * k) + _parallel(poly, 90, 9.0 * k)
    elif material == "planting":
        for x, y in _jitter_grid(poly, 7.0 * k, rnd):
            if rnd() < 0.7:
                s = 1.8 * k
                st += [("M", x - s, y + s), ("L", x, y), ("L", x + s, y + s), ("M", x, y), ("L", x, y + s * 1.3)]
    elif material == "solid":
        fl = poly_segments(poly, closed=True)
    else:
        raise ValueError(f"unknown material {material!r}; materials: {', '.join(MATERIALS)}")
    return st, fl


def draw(page, poly, material, region=None, scale: float = 1.0, outline: str | None = None,
         tint=None, layer: str = "geom", status: str | None = None, record: bool = True):
    """Hatch a polygon given in paper points. The low-level form of fill().

    record  list the material for QA (a cut material needs a legend row); the
            earth band under a grade line is not a cut material.
    """
    clip = poly_segments(poly, closed=True)
    if record:
        page.hatches.append({"region": region, "material": material})
    rnd = _Rand(_seed(poly) + sum(map(ord, material)))
    if tint:
        page.path(clip, stroke=None, fill=tint, layer=layer, clip=clip, region=region)
    st, fl = _pattern(poly, material, scale, rnd)
    hp = pens.kw("hatch", status=status)
    if material == "solid":
        page.path(fl, stroke=None, fill=INK2 if status is None else "#9a9a9a", layer=layer, clip=clip,
                  region=region)
    elif fl:
        page.path(fl, stroke=None, fill=hp["stroke"], layer=layer, clip=clip, region=region)
    if st:
        page.path(st, layer=layer, clip=clip, region=region, **hp)
    if outline:
        page.path(clip, layer=layer, region=region, **pens.kw(outline, status=status))


def fill(view, pts, material: str, outline: str | None = None, scale: float = 1.0, tint=None,
         status: str | None = None, record: bool = True):
    """Hatch a polygon given in real inches on a view.

    outline  a pen name (pens.PENS) to draw the outline with, e.g. "cut" for a
             part the section cuts through. None draws the hatch only.
    scale    pattern size factor (1 = standard).
    tint     optional light background fill under the pattern.
    status   a value status; ASSUMED or PLACEHOLDER draws the outline grey dashed.
    """
    poly = [view.P(x, y) for x, y in pts]
    draw(view.page, poly, material, region=view.id, scale=scale, outline=outline, tint=tint,
         status=status, record=record)


def rect(view, x0, y0, x1, y1, material: str, **kw):
    """Hatch an axis-aligned rectangle in real inches. Keywords as fill()."""
    fill(view, [(x0, y0), (x1, y0), (x1, y1), (x0, y1)], material, **kw)


def layers(view, face, span, stack, axis: str = "x", direction: int = 1, outline: str = "cut",
           seams: str = "fine", status: str | None = None):
    """A built-up assembly cut in section (a wall, floor or roof), layer by layer.

    face       coordinate of the first face on the stacking axis, real inches
    span       (a, b): extent along the other axis (a wall's bottom and top)
    stack      [(thickness, material or None)], from the face inward. A thickness
               is a Value or a number from project.json; None leaves a layer blank.
    axis       'x': layers stack along x (a wall in section); 'y': along y (a floor or roof)
    direction  +1 or -1: which way the stack runs from the face
    outline    pen for the assembly's outer boundary (the cut line); seams: pen between layers
    Returns the coordinate of the far face.
    """
    a, b = float(span[0]), float(span[1])
    pos = float(face)
    for t, material in stack:
        nxt = pos + direction * float(t)
        lo, hi = sorted((pos, nxt))
        box = (lo, a, hi, b) if axis == "x" else (a, lo, b, hi)
        if material:
            rect(view, *box, material, status=status)
        pos = nxt
    lo, hi = sorted((float(face), pos))
    # seams between layers, then the cut boundary over them
    p = float(face)
    for t, _ in stack[:-1]:
        p += direction * float(t)
        if axis == "x":
            view.line(p, a, p, b, layer="geom", **pens.kw(seams, status=status))
        else:
            view.line(a, p, b, p, layer="geom", **pens.kw(seams, status=status))
    box = (lo, a, hi, b) if axis == "x" else (a, lo, b, hi)
    view.rect(*box, layer="geom", **pens.kw(outline, status=status))
    return pos


def grade(view, x0, x1, y=0.0, depth_pt: float = 16.0, gaps=(), pen: str = "grade", material: str = "earth",
          label: str | None = None):
    """A finish-grade line from x0 to x1 at height y, with a band of earth below it.

    depth_pt  band depth in paper points
    gaps      [(xa, xb)] real-inch spans with no band (where a footing or slab sits)
    label     text at the left end of the line, e.g. "FINISH GRADE" (level
              markers usually sit at the right end). Returns its text record.
    """
    view.line(x0, y, x1, y, layer="geom", **pens.kw(pen))
    spans = [(x0, x1)]
    for ga, gb in sorted(gaps):
        nxt = []
        for a, b in spans:
            if gb <= a or ga >= b:
                nxt.append((a, b))
                continue
            if ga > a:
                nxt.append((a, ga))
            if gb < b:
                nxt.append((gb, b))
        spans = nxt
    d = depth_pt * view.u
    for a, b in spans:
        if b - a > 1e-6:
            rect(view, a, y - d, b, y, material, record=False)
    if label:
        px, py = view.P(x0, y)
        return view.paper_text(px + 4, py + 3, label, size=6.0, anchor="start", color=INK2, role="section")
    return None


def swatch(page, box, material: str, region=None):
    """A legend swatch: the pattern inside a framed box (paper points)."""
    x0, y0, x1, y1 = box
    poly = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
    page.path(rect_segments(x0, y0, x1, y1), stroke=None, fill=WHITE, layer="annot", region=region)
    # A legend chip is not a cut material. grade's earth band stays out the same way.
    draw(page, poly, material, region=region, layer="annot", record=False)
    page.path(rect_segments(x0, y0, x1, y1), stroke=INK, width=0.6, layer="annot", region=region)
