"""Plan symbols for plumbing fixtures, kitchen equipment and appliances.

Every symbol is placed by the midpoint of its back edge (the edge against
the wall) and the compass direction it faces, away from that wall:

    fixtures.toilet(v, (x, y), "N")       # back of the tank on the S wall, facing N

Sizes are schematic symbol sizes, in real inches, so the symbol reads at a
true scale. They are layout, not design values, and they print no number.
When a reviewer checks a size or a clearance (a toilet centreline, a tub
length, a counter depth), store it in project.json, pass it as `w` / `d`,
and dimension it with annot.dim_chain.

`action` sets the line weight: new is solid black, existing is thinner grey,
demo is dashed. An unverified `w` or `d` (ASSUMED or derived from ASSUMED)
draws grey dashed, like every other unverified line in the kit.
"""
from __future__ import annotations

import math

from . import textmetrics as tm
from .arch import DIRS
from .display import INK, INK2, STATUS_STYLE, WHITE, View
from .model import Value

ACTIONS = ("existing", "new", "demo", "relocate")


def _unverified(*vals) -> bool:
    return any(isinstance(x, Value) and x.unverified for x in vals)


def _style(action: str, *vals) -> dict:
    if action not in ACTIONS:
        raise ValueError(f"action {action!r} is not one of {', '.join(ACTIONS)}")
    if _unverified(*vals):
        st = STATUS_STYLE["ASSUMED"]
        return {"stroke": st["stroke"], "width": 0.7, "dash": st["dash"]}
    kw = {"stroke": INK if action == "new" else INK2, "width": 0.8 if action == "new" else 0.6}
    if action == "demo":
        kw["dash"] = (5.0, 3.0)
    return kw


class _Frame:
    """Local axes for one symbol: u along the wall (to the viewer's left when
    facing the symbol), w out from the wall. at = back-edge midpoint."""

    def __init__(self, at, facing: str):
        if facing not in DIRS:
            raise ValueError(f"facing must be N, S, E or W, not {facing!r}")
        self.o = (float(at[0]), float(at[1]))
        self.w = DIRS[facing]
        self.u = (self.w[1], -self.w[0])

    def __call__(self, u, w):
        return (self.o[0] + self.u[0] * u + self.w[0] * w, self.o[1] + self.u[1] * u + self.w[1] * w)

    def rect(self, u0, w0, u1, w1):
        return [self(u0, w0), self(u1, w0), self(u1, w1), self(u0, w1)]

    def ellipse(self, cu, cw, ru, rw, n: int = 48, a0: float = 0.0, a1: float = 360.0):
        pts = []
        for i in range(n + 1):
            a = math.radians(a0 + (a1 - a0) * i / n)
            pts.append(self(cu + ru * math.cos(a), cw + rw * math.sin(a)))
        return pts

    def rounded(self, u0, w0, u1, w1, r):
        """A rounded rectangle as a point ring."""
        r = min(r, abs(u1 - u0) / 2, abs(w1 - w0) / 2)
        pts = []
        corners = [(u1 - r, w0 + r, -90), (u1 - r, w1 - r, 0), (u0 + r, w1 - r, 90), (u0 + r, w0 + r, 180)]
        for cu, cw, start in corners:
            for i in range(7):
                a = math.radians(start + 90 * i / 6)
                pts.append(self(cu + r * math.cos(a), cw + r * math.sin(a)))
        return pts


def _label(v: View, at, text, size=5.5):
    """A short label centred on a real point. The symbol under it is filled white,
    so the label never sits on linework."""
    px, py = v.P(*at)
    return v.paper_text(px, py - tm.ASCENT * size / 2, text, size=size, bold=True, anchor="middle",
                        color=INK2, role="fixture")


def toilet(v: View, at, facing: str, action: str = "new", w=20, d=28):
    """Water closet: tank against the wall, elongated bowl in front."""
    f = _Frame(at, facing)
    kw = _style(action, w, d)
    W, D = float(w), float(d)
    tank_d = min(9.0, D * 0.32)
    v.polygon(f.rounded(-W / 2, 0, W / 2, tank_d, 1.5), fill=WHITE, **kw)
    bowl_rw = (D - tank_d) / 2
    v.polygon(f.ellipse(0, tank_d + bowl_rw, W * 0.36, bowl_rw), fill=WHITE, **kw)
    v.polygon(f.ellipse(0, tank_d + bowl_rw + 1, W * 0.24, bowl_rw * 0.7), **dict(kw, width=kw["width"] * 0.7))


def lavatory(v: View, at, facing: str, action: str = "new", w=20, d=17, wall_hung: bool = True):
    """Wall-hung lavatory (or, with wall_hung=False, a basin drawn alone)."""
    f = _Frame(at, facing)
    kw = _style(action, w, d)
    W, D = float(w), float(d)
    if wall_hung:
        v.polygon(f.rounded(-W / 2, 0, W / 2, D, 3), fill=WHITE, **kw)
    v.polygon(f.ellipse(0, D * 0.55, W * 0.36, D * 0.33), **kw)
    v.circle(*f(0, D * 0.55), 0.9, **dict(kw, width=0.5))


def vanity(v: View, at, facing: str, action: str = "new", w=36, d=21, basins: int = 1):
    """Vanity cabinet with one or two drop-in basins."""
    f = _Frame(at, facing)
    kw = _style(action, w, d)
    W, D = float(w), float(d)
    v.polygon(f.rect(-W / 2, 0, W / 2, D), fill=WHITE, **kw)
    n = max(1, int(basins))
    for i in range(n):
        cu = -W / 2 + W * (2 * i + 1) / (2 * n)
        v.polygon(f.ellipse(cu, D * 0.52, min(8.5, W / (2 * n) - 3), D * 0.3), **kw)
        v.circle(*f(cu, D * 0.52), 0.9, **dict(kw, width=0.5))


def tub(v: View, x0, y0, x1, y1, drain: str = "W", action: str = "new"):
    """Bathtub filling a box in real inches. drain = the compass end that holds the drain."""
    kw = _style(action, x1 - x0, y1 - y0)
    x0, y0, x1, y1 = (float(a) for a in (x0, y0, x1, y1))
    v.rect(x0, y0, x1, y1, fill=WHITE, **kw)
    ins = 3.0
    long_x = (x1 - x0) >= (y1 - y0)
    if (drain in ("W", "E")) != long_x:
        raise ValueError(f"tub drain {drain!r} must be at one end of the tub; this tub runs "
                         f"{'E-W' if long_x else 'N-S'}, so use {'W or E' if long_x else 'S or N'}")
    f = _Frame(((x0 + x1) / 2, (y0 + y1) / 2), "N")
    hx, hy = (x1 - x0) / 2 - ins, (y1 - y0) / 2 - ins
    v.polygon(f.rounded(-hx, -hy, hx, hy, 8), **kw)
    dx, dy = {"W": (x0 + ins + 6, (y0 + y1) / 2), "E": (x1 - ins - 6, (y0 + y1) / 2),
              "S": ((x0 + x1) / 2, y0 + ins + 6), "N": ((x0 + x1) / 2, y1 - ins - 6)}[drain]
    v.circle(dx, dy, 1.2, **dict(kw, width=0.5))


def shower(v: View, x0, y0, x1, y1, action: str = "new", drain=None, label: str = "SHOWER"):
    """Shower pan filling a box, with a centre drain and the usual diagonals.

    drain  (x, y) real point; default the centre. label prints in the pan
           ('' for none).
    """
    kw = _style(action, x1 - x0, y1 - y0)
    x0, y0, x1, y1 = (float(a) for a in (x0, y0, x1, y1))
    v.rect(x0, y0, x1, y1, fill=WHITE, **kw)
    cx, cy = drain if drain is not None else ((x0 + x1) / 2, (y0 + y1) / 2)
    r = 1.5
    thin = dict(kw, width=0.35)
    for px, py in ((x0, y0), (x1, y0), (x1, y1), (x0, y1)):
        a = math.atan2(py - cy, px - cx)
        v.line(cx + r * math.cos(a), cy + r * math.sin(a), px, py, **thin)
    v.circle(cx, cy, r, fill=WHITE, **dict(kw, width=0.5))
    if label:
        lx, ly = (x0 + x1) / 2, cy + (y1 - y0) * 0.22
        size = 5.5
        mask_w = (tm.text_width(label, size, True) + 4) * v.u
        mask_h = (size + 3) * v.u
        v.rect(lx - mask_w / 2, ly - mask_h / 2, lx + mask_w / 2, ly + mask_h / 2, stroke=None, fill=WHITE,
               layer="annot")
        _label(v, (lx, ly), label, size)


def counter(v: View, x0, y0, x1, y1, action: str = "new", uppers=None):
    """A counter top in plan. uppers=(x0, y0, x1, y1) draws upper cabinets dashed."""
    kw = _style(action, x1 - x0, y1 - y0)
    v.rect(x0, y0, x1, y1, fill=WHITE, **kw)
    if uppers is not None:
        ux0, uy0, ux1, uy1 = uppers
        v.rect(ux0, uy0, ux1, uy1, **dict(kw, width=0.45, dash=(4.0, 2.5)))


def kitchen_sink(v: View, at, facing: str, action: str = "new", w=33, d=22, bowls: int = 2, setback=2.5):
    """Drop-in sink, back edge `setback` in. from the wall (inside a counter)."""
    f = _Frame(at, facing)
    kw = _style(action, w, d)
    W, D, sb = float(w), float(d), float(setback)
    v.polygon(f.rect(-W / 2, sb, W / 2, sb + D * 0.85), fill=WHITE, **kw)
    n = max(1, int(bowls))
    gap = 2.0
    bw = (W - 4 - gap * (n - 1)) / n
    for i in range(n):
        u0 = -W / 2 + 2 + i * (bw + gap)
        v.polygon(f.rounded(u0, sb + 2, u0 + bw, sb + D * 0.85 - 2, 2.5), **kw)
        v.circle(*f(u0 + bw / 2, sb + D * 0.42), 1.0, **dict(kw, width=0.5))


def range_(v: View, at, facing: str, action: str = "new", w=30, d=26):
    """Range or cooktop: a box with four burners."""
    f = _Frame(at, facing)
    kw = _style(action, w, d)
    W, D = float(w), float(d)
    v.polygon(f.rect(-W / 2, 0, W / 2, D), fill=WHITE, **kw)
    for cu, cw, r in ((-W / 4, D * 0.3, 3.6), (W / 4, D * 0.3, 4.4), (-W / 4, D * 0.7, 4.4),
                      (W / 4, D * 0.7, 3.6)):
        v.polygon(f.ellipse(cu, cw, r, r), **dict(kw, width=0.5))


def _box_label(v: View, at, facing, action, w, d, text, dashed=False):
    f = _Frame(at, facing)
    kw = _style(action, w, d)
    if dashed:
        kw = dict(kw, dash=(4.0, 2.5))
    W, D = float(w), float(d)
    v.polygon(f.rect(-W / 2, 0, W / 2, D), fill=WHITE, **kw)
    _label(v, f(0, D / 2), text)


def refrigerator(v: View, at, facing: str, action: str = "new", w=36, d=30, label: str = "REF"):
    _box_label(v, at, facing, action, w, d, label)


def dishwasher(v: View, at, facing: str, action: str = "new", w=24, d=24, label: str = "DW"):
    """Under-counter: dashed, inside the counter outline."""
    _box_label(v, at, facing, action, w, d, label, dashed=True)


def washer(v: View, at, facing: str, action: str = "new", w=27, d=30, label: str = "W"):
    _box_label(v, at, facing, action, w, d, label)


def dryer(v: View, at, facing: str, action: str = "new", w=27, d=30, label: str = "D"):
    _box_label(v, at, facing, action, w, d, label)


def water_heater(v: View, at, action: str = "new", dia=22, label: str = "WH"):
    """Tank water heater by its centre."""
    kw = _style(action, dia)
    v.circle(at[0], at[1], float(dia) / 2, fill=WHITE, **kw)
    _label(v, at, label)


def tankless(v: View, at, facing: str, action: str = "new", w=14, d=10, label: str = "TWH"):
    _box_label(v, at, facing, action, w, d, label)


def furnace(v: View, at, facing: str, action: str = "new", w=22, d=28, label: str = "FAU"):
    _box_label(v, at, facing, action, w, d, label)

