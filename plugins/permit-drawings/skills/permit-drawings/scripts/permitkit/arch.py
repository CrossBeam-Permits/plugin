"""Architectural symbols in plan and elevation.

Plan geometry is real inches, x east and y north. A wall is defined by its
finished face, the compass direction it runs, and the compass direction from
that face into the wall body. Every opening names its wall axis explicitly.
Deriving the axis from the swing direction is how a past set got every door
leaf flipped.

Line style follows status: a face or thickness that is ASSUMED, or derives
from an ASSUMED value, draws grey and dashed. Action sets the poché:
existing = light grey, new = dark grey, demo = dashed outline with no fill.
"""
from __future__ import annotations

import math

from .display import (INK, INK2, POCHE_E, POCHE_N, STATUS_STYLE, WHITE, View, arc_segments,
                      poly_segments, rect_segments)
from .model import UNVERIFIED, Value
from .pens import width as _pw

DIRS = {"N": (0.0, 1.0), "S": (0.0, -1.0), "E": (1.0, 0.0), "W": (-1.0, 0.0)}
# existing = (E) existing to remain. relocate = (E) moved. new = (N). demo = removed.
FILL = {"existing": POCHE_E, "relocate": POCHE_E, "new": POCHE_N, "demo": None}
WALL_LW = _pw("cut")          # the pen standard (pens.py): walls are the cut pen
JAMB_LW = _pw("cut_med")
LEAF_LW = 1.0
FINE_LW = _pw("fine")


def _fill(action: str):
    if action not in FILL:
        raise ValueError(f"action {action!r} is not one of {', '.join(FILL)}")
    return FILL[action]


def _status_of(x, default="MEASURED") -> str:
    if isinstance(x, Value):
        return "ASSUMED" if x.unverified else x.status
    return default


def _line_kw(status: str, action: str = "existing", width: float = WALL_LW) -> dict:
    st = STATUS_STYLE.get(status, STATUS_STYLE["MEASURED"])
    kw = {"stroke": st["stroke"], "width": width}
    if st["dash"]:
        kw["dash"] = st["dash"]
    if action == "demo":
        kw["dash"] = (5.0, 3.0)
    return kw


def _add(p, d, k):
    return (p[0] + d[0] * k, p[1] + d[1] * k)


class Wall:
    """A straight wall. Openings are placed by offset from the wall's start point.

    view    the View to draw on
    start   (x, y) start of the finished face, real inches
    along   compass direction the face runs: 'N', 'S', 'E' or 'W'
    length  length of the face (Value or number)
    t       wall thickness (Value). An unverified thickness dashes the back line.
    body    compass direction from the face into the wall body
    """

    def __init__(self, view: View, start, along: str, length, t, body: str,
                 action: str = "existing", face_status: str = "MEASURED", draw: bool = True,
                 caps: bool = True):
        if DIRS[along][0] * DIRS[body][0] + DIRS[along][1] * DIRS[body][1] != 0:
            raise ValueError(f"wall body {body} must be at right angles to its run {along}")
        self.view = view
        self.start = (float(start[0]), float(start[1]))
        self.along = along
        self.a = DIRS[along]
        self.n = DIRS[body]
        self.body = body
        self.length = float(length)
        self.t = t
        self.th = float(t)
        self.action = action
        self.face_status = face_status
        self.back_status = _status_of(t, face_status)
        if draw:
            self.draw(caps)

    def pt(self, offset: float, depth: float = 0.0):
        """A point `offset` along the face and `depth` into the wall body."""
        return _add(_add(self.start, self.a, offset), self.n, depth)

    def draw(self, caps: bool = True):
        v = self.view
        p0, p1 = self.pt(0), self.pt(self.length)
        q0, q1 = self.pt(0, self.th), self.pt(self.length, self.th)
        fill = _fill(self.action)
        if fill:
            v.polygon([p0, p1, q1, q0], stroke=None, fill=fill)
        v.line(*p0, *p1, **_line_kw(self.face_status, self.action))
        v.line(*q0, *q1, **_line_kw(self.back_status, self.action))
        if caps:
            v.line(*p0, *q0, **_line_kw(self.face_status, self.action, JAMB_LW))
            v.line(*p1, *q1, **_line_kw(self.face_status, self.action, JAMB_LW))

    # ---- openings

    def _frame(self, offset, width):
        o, w = float(offset), float(width)
        return o, w, self.pt(o), self.pt(o + w), self.pt(o, self.th), self.pt(o + w, self.th)

    def cut(self, offset, width, jambs: bool = True):
        """Knock the wall out between offset and offset + width and draw the jambs."""
        o, w, p0, p1, q0, q1 = self._frame(offset, width)
        pad = 1.0 * self.view.u
        a0 = _add(p0, self.n, -pad)
        a1 = _add(p1, self.n, -pad)
        b1 = _add(q1, self.n, pad)
        b0 = _add(q0, self.n, pad)
        self.view.polygon([a0, a1, b1, b0], stroke=None, fill=WHITE)
        if jambs:
            self.view.line(*p0, *q0, stroke=INK, width=JAMB_LW)
            self.view.line(*p1, *q1, stroke=INK, width=JAMB_LW)
        return p0, p1, q0, q1

    def door(self, offset, width, swing: str, hinge: str = "start", leaf_width=None):
        """Hinged door shown open 90 degrees, with a dashed swing arc.

        swing  compass direction the leaf swings toward ('N', 'S', 'E', 'W'),
               at right angles to the wall run.
        hinge  'start' or 'end': which jamb carries the hinges, in the run direction.
        """
        if DIRS[swing][0] * self.a[0] + DIRS[swing][1] * self.a[1] != 0:
            raise ValueError(f"door swing {swing} must be at right angles to wall run {self.along}")
        p0, p1, q0, q1 = self.cut(offset, width)
        outward = DIRS[swing] == self.n
        base0, base1 = (q0, q1) if outward else (p0, p1)
        hinge_pt, latch = (base0, base1) if hinge == "start" else (base1, base0)
        w = float(leaf_width if leaf_width is not None else width)
        d = DIRS[swing]
        tip = _add(hinge_pt, d, w)
        self.view.line(*hinge_pt, *tip, stroke=INK, width=LEAF_LW)
        a0 = math.atan2(latch[1] - hinge_pt[1], latch[0] - hinge_pt[0])
        a1 = math.atan2(tip[1] - hinge_pt[1], tip[0] - hinge_pt[0])
        da = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi
        segs = [("M",) + _add(hinge_pt, (math.cos(a0), math.sin(a0)), w)]
        segs += arc_segments(hinge_pt[0], hinge_pt[1], w, a0, a0 + da)
        self.view.path(segs, stroke=INK, width=FINE_LW, dash=(3.0, 2.0))
        return {"hinge": hinge_pt, "tip": tip}

    def window(self, offset, width):
        """Window in plan: frame lines at the faces of a sash band and a glass line."""
        o, w, p0, p1, q0, q1 = self._frame(offset, width)
        self.cut(offset, width)
        v = self.view
        for k in (0.3, 0.7):
            v.line(*self.pt(o, self.th * k), *self.pt(o + w, self.th * k), stroke=INK, width=FINE_LW)
        v.line(*self.pt(o, self.th * 0.5), *self.pt(o + w, self.th * 0.5), stroke=INK, width=0.6)

    def _leaf(self, s, e, k0, k1):
        """A sliding leaf from offset s to e, between depths k0 and k1 (shares of the thickness)."""
        self.view.polygon([self.pt(s, self.th * k0), self.pt(e, self.th * k0), self.pt(e, self.th * k1),
                           self.pt(s, self.th * k1)], stroke=INK, width=0.5, fill=WHITE)

    def slider(self, offset, width, overlap: float = 2.0):
        """Sliding glass door or window: two offset panels inside the wall."""
        o, w, *_ = self._frame(offset, width)
        self.cut(offset, width)
        half = w / 2
        for k0, k1, s, e in ((0.22, 0.42, o, o + half + overlap), (0.58, 0.78, o + half - overlap, o + w)):
            self._leaf(s, e, k0, k1)
            mid = (k0 + k1) / 2
            self.view.line(*self.pt(s, self.th * mid), *self.pt(e, self.th * mid), stroke=INK, width=FINE_LW)

    def bypass(self, offset, width, overlap: float = 2.0):
        """Bypass closet doors: two thin leaves on separate tracks."""
        o, w, *_ = self._frame(offset, width)
        self.cut(offset, width)
        half = w / 2
        for k0, k1, s, e in ((0.15, 0.35, o, o + half + overlap), (0.65, 0.85, o + half - overlap, o + w)):
            self._leaf(s, e, k0, k1)

    def cased(self, offset, width):
        """Cased opening, no door: dashed header lines on both faces."""
        p0, p1, q0, q1 = self.cut(offset, width)
        self.view.line(*p0, *p1, stroke=INK2, width=0.6, dash=(5.0, 3.0))
        self.view.line(*q0, *q1, stroke=INK2, width=0.6, dash=(5.0, 3.0))

    def bifold(self, offset, width, swing: str):
        """Bi-fold doors folding toward `swing`."""
        o, w, p0, p1, q0, q1 = self._frame(offset, width)
        self.cut(offset, width)
        outward = DIRS[swing] == self.n
        b0, b1 = (q0, q1) if outward else (p0, p1)
        d = DIRS[swing]
        h = w / 2
        v = self.view
        for base, sgn in ((b0, 1.0), (b1, -1.0)):
            mid = _add(_add(base, self.a, h * 0.45 * sgn), d, h * 0.55)
            end = _add(base, self.a, h * 0.9 * sgn)
            v.line(*base, *mid, stroke=INK, width=LEAF_LW)
            v.line(*mid, *end, stroke=INK, width=LEAF_LW)
        v.line(*b0, *b1, stroke=INK2, width=0.5, dash=(4.0, 3.0))

    def overhead(self, offset, width, action: str = "existing", track: float | None = None):
        """Overhead (garage) door: the door line at the inside face, and the
        door's open position overhead drawn dashed into the room (`track`
        real inches deep; default about its height, 84 in.; 0 for none).
        action 'demo' draws everything dashed: the door is removed and the
        opening stays until another call fills it."""
        o, w, *_ = self._frame(offset, width)
        self.cut(offset, width)
        v = self.view
        dash = (5.0, 3.0) if action == "demo" else None
        kw = {"stroke": INK, "width": 1.0}
        if dash:
            kw["dash"] = dash
        # panel: a thin band just inside the face
        v.polygon([self.pt(o, -1.0), self.pt(o + w, -1.0), self.pt(o + w, -3.0), self.pt(o, -3.0)],
                  fill=WHITE, **kw)
        depth = 84.0 if track is None else float(track)
        if depth > 0:
            v.polygon([self.pt(o, -3.0), self.pt(o + w, -3.0), self.pt(o + w, -3.0 - depth),
                       self.pt(o, -3.0 - depth)], stroke=INK2, width=0.5, dash=(6.0, 3.0), layer="annot")

    def infill(self, offset, width, action: str = "new"):
        """Fill an opening with new wall. Dark poché for new work."""
        o, w, p0, p1, q0, q1 = self._frame(offset, width)
        self.cut(offset, width, jambs=False)
        self.view.polygon([p0, p1, q1, q0], stroke=INK, width=JAMB_LW, fill=_fill(action) or WHITE)


class Shell:
    """A rectangular room shell measured to its interior faces.

    (x0, y0) is the south-west interior corner and (x1, y1) the north-east one.
    t maps 'N', 'S', 'E', 'W' to wall thickness Values. The shell draws one
    continuous poché. Use .N, .S, .E, .W to place openings; offsets run from
    the west face (N and S walls) or the south face (E and W walls).
    """

    def __init__(self, view: View, x0, y0, x1, y1, t: dict, action: str = "existing",
                 face_status: str = "MEASURED"):
        self.view = view
        self.x0, self.y0, self.x1, self.y1 = (float(x0), float(y0), float(x1), float(y1))
        self.t = t
        ox0, oy0, ox1, oy1 = self.outer
        fill = _fill(action)
        outer = rect_segments(ox0, oy0, ox1, oy1)
        inner = [("M", self.x0, self.y0), ("L", self.x0, self.y1), ("L", self.x1, self.y1),
                 ("L", self.x1, self.y0), ("Z",)]
        if fill:
            view.path(outer + inner, stroke=None, fill=fill, evenodd=True)
        face = _line_kw(face_status, action)
        view.polygon([(self.x0, self.y0), (self.x1, self.y0), (self.x1, self.y1), (self.x0, self.y1)],
                     **face)
        for side, a, b in (("S", (ox0, oy0), (ox1, oy0)), ("E", (ox1, oy0), (ox1, oy1)),
                           ("N", (ox1, oy1), (ox0, oy1)), ("W", (ox0, oy1), (ox0, oy0))):
            view.line(*a, *b, **_line_kw(_status_of(t[side], face_status), action))
        w, h = self.x1 - self.x0, self.y1 - self.y0
        mk = dict(action=action, face_status=face_status, draw=False)
        self.N = Wall(view, (self.x0, self.y1), "E", w, t["N"], "N", **mk)
        self.S = Wall(view, (self.x0, self.y0), "E", w, t["S"], "S", **mk)
        self.W = Wall(view, (self.x0, self.y0), "N", h, t["W"], "W", **mk)
        self.E = Wall(view, (self.x1, self.y0), "N", h, t["E"], "E", **mk)

    @property
    def outer(self):
        return (self.x0 - float(self.t["W"]), self.y0 - float(self.t["S"]),
                self.x1 + float(self.t["E"]), self.y1 + float(self.t["N"]))


# ------------------------------------------------------------------ stairs and lines


def stair(view: View, x, y, width, treads: int, tread, up: str, status: str = "MEASURED",
          label: str = "UP", break_after: int | None = None):
    """Straight flight in plan. (x, y) is the corner at the bottom riser, on the
    left side looking up the flight. `up` is the compass direction of ascent.
    """
    d = DIRS[up]
    side = (d[1], -d[0])              # to the right when looking up the flight
    w, td = float(width), float(tread)
    kw = _line_kw(status, width=_pw("object"))
    shown = treads if break_after is None else min(treads, break_after)
    for i in range(shown + 1):
        a = _add((x, y), d, td * i)
        view.line(*a, *_add(a, side, w), **kw)
    run = td * shown
    end0, end1 = _add((x, y), d, run), _add(_add((x, y), d, run), side, w)
    view.line(x, y, *end0, **kw)
    view.line(*_add((x, y), side, w), *end1, **kw)
    if break_after is not None and break_after < treads:
        break_line(view, end0, end1)
    mid = _add((x, y), side, w / 2)
    a = _add(mid, d, td * 0.5)
    b = _add(mid, d, run - td * 0.5)
    view.line(*a, *b, stroke=INK, width=1.0, layer="annot")
    pb = view.P(*b)
    ang = math.atan2(d[1], d[0])
    p1 = (pb[0] - 6 * math.cos(ang - 0.4), pb[1] - 6 * math.sin(ang - 0.4))
    p2 = (pb[0] - 6 * math.cos(ang + 0.4), pb[1] - 6 * math.sin(ang + 0.4))
    view.paper_path(poly_segments([pb, p1, p2], closed=True), stroke=None, fill=INK, layer="annot")
    pa = view.P(*a)
    return view.paper_text(pa[0] - 6 * math.cos(ang), pa[1] - 6 * math.sin(ang) - 3, label, size=7.5,
                           bold=True, anchor="middle", role="label")


def break_line(view: View, a, b, amp_pt: float = 5.0):
    """Break line from a to b with a zig-zag at the middle."""
    pa, pb = view.P(*a), view.P(*b)
    dx, dy = pb[0] - pa[0], pb[1] - pa[1]
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    m = (pa[0] + dx / 2, pa[1] + dy / 2)
    pts = [pa, (m[0] - ux * 5, m[1] - uy * 5), (m[0] - ux * 2 + nx * amp_pt, m[1] - uy * 2 + ny * amp_pt),
           (m[0] + ux * 2 - nx * amp_pt, m[1] + uy * 2 - ny * amp_pt), (m[0] + ux * 5, m[1] + uy * 5), pb]
    view.paper_path(poly_segments(pts), stroke=INK, width=0.8, layer="geom")


# ------------------------------------------------------------------ elevation


WINDOW_KINDS = ("XO", "OX", "casement", "fixed", "single-hung", "double-hung")


def elev_window(view: View, x, sill, w, h, kind: str = "XO", hinge: str = "left", inset: float = 1.5,
                label_size: float = 8.0, status: str = "PROPOSED"):
    """Window in elevation. x is the left edge, sill and h are heights above the floor.

    kind  'XO' / 'OX'   horizontal slider: a centre stile, X on the sliding
                        panel and O on the fixed one, as seen
          'casement'    dashed swing lines meeting at the hinge side (hinge
                        'left' or 'right', as seen)
          'fixed'       frame and glass only: no operation mark
          'single-hung' a meeting rail at mid height, the lower sash in front,
                        an up arrow in the lower sash
          'double-hung' the same, with a down arrow in the upper sash too
    Any other kind raises ValueError.
    """
    if kind not in WINDOW_KINDS:
        raise ValueError(f"elev_window kind must be one of {WINDOW_KINDS}, not {kind!r}")
    x, sill, w, h = float(x), float(sill), float(w), float(h)
    kw = _line_kw(status, width=_pw("object"))
    view.rect(x, sill, x + w, sill + h, fill=WHITE, **kw)
    view.rect(x + inset, sill + inset, x + w - inset, sill + h - inset, **_line_kw(status, width=FINE_LW))
    if kind in ("XO", "OX"):
        view.line(x + w / 2, sill + inset, x + w / 2, sill + h - inset, **_line_kw(status, width=0.6))
        for i, ch in enumerate(kind):
            view.text(x + w * (0.25 + 0.5 * i), sill + h / 2, ch, size=label_size, anchor="middle",
                      dy=-label_size * 0.35, role="symbol", collide=False)
    elif kind == "casement":
        hx = x + inset if hinge == "left" else x + w - inset
        ox = x + w - inset if hinge == "left" else x + inset
        view.polyline([(ox, sill + inset), (hx, sill + h / 2), (ox, sill + h - inset)],
                      stroke=INK2, width=0.5, dash=(4.0, 2.0))
    elif kind in ("single-hung", "double-hung"):
        mid = sill + h / 2
        rail = min(1.5, h / 12)
        # the lower sash's top rail sits in front of the upper sash's bottom rail
        view.line(x + inset, mid - rail, x + w - inset, mid - rail, **_line_kw(status, width=0.6))
        view.line(x + inset, mid + rail, x + w - inset, mid + rail, **_line_kw(status, width=FINE_LW))
        _sash_arrow(view, x + w / 2, sill + inset, mid - rail, up=True)
        if kind == "double-hung":
            _sash_arrow(view, x + w / 2, mid + rail, sill + h - inset, up=False)


def _sash_arrow(view: View, cx, y0, y1, up: bool):
    """An operation arrow in a hung sash: a thin shaft over the middle half of the sash and an open head."""
    span = y1 - y0
    if span <= 0:
        return
    a, b = y0 + span * 0.25, y1 - span * 0.25
    tip, tail = (b, a) if up else (a, b)
    head = min(3.0, span * 0.2) * (1 if up else -1)
    view.line(cx, tail, cx, tip, stroke=INK2, width=0.4)
    view.polyline([(cx - abs(head) * 0.7, tip - head), (cx, tip), (cx + abs(head) * 0.7, tip - head)],
                  stroke=INK2, width=0.4)


def elev_door(view: View, x, w, h, kind: str = "panel", hinge: str = "left", split=None, lite=None,
              status: str = "PROPOSED"):
    """Door in elevation. kind 'panel' or 'dutch' (pass split height). lite = (dx, dy, w, h)."""
    x, w, h = float(x), float(w), float(h)
    view.rect(x, 0, x + w, h, fill=WHITE, **_line_kw(status, width=_pw("object")))
    view.rect(x + 1.5, 0, x + w - 1.5, h - 1.5, **_line_kw(status, width=FINE_LW))
    knob_x = x + w - 4 if hinge == "left" else x + 4
    if kind == "dutch":
        s = float(split)
        view.line(x, s, x + w, s, **_line_kw(status, width=1.0))
        view.circle_pt(knob_x, s + 3, 1.8, stroke=None, fill=INK)
        view.circle_pt(knob_x, s - 4, 1.8, stroke=None, fill=INK)
    else:
        view.circle_pt(knob_x, 36.0, 1.8, stroke=None, fill=INK)
    if lite:
        lx, ly, lw, lh = (float(v) for v in lite)
        view.rect(x + lx, ly, x + lx + lw, ly + lh, stroke=INK, width=0.6)
        view.line(x + lx, ly, x + lx + lw, ly + lh, stroke=INK2, width=0.3)
        view.line(x + lx + lw, ly, x + lx, ly + lh, stroke=INK2, width=0.3)
    # swing mark: dashed lines meeting at the hinge side
    hx = x + 1.5 if hinge == "left" else x + w - 1.5
    ox = x + w - 1.5 if hinge == "left" else x + 1.5
    view.polyline([(ox, 0), (hx, h / 2), (ox, h - 1.5)], stroke=INK2, width=0.4, dash=(4.0, 3.0))


def elev_slider(view: View, x, w, h, status: str = "MEASURED"):
    """Two-panel sliding door in elevation."""
    x, w, h = float(x), float(w), float(h)
    view.rect(x, 0, x + w, h, fill=WHITE, **_line_kw(status, width=_pw("object")))
    half = w / 2
    for px in (x, x + half):
        view.rect(px + 2, 2, px + half - 2, h - 2, **_line_kw(status, width=FINE_LW))
        view.line(px + 6, 6, px + half - 6, h - 6, stroke=INK2, width=0.3)
        view.line(px + half - 6, 6, px + 6, h - 6, stroke=INK2, width=0.3)


# ------------------------------------------------------------------ electrical (sizes in points)
#
# Point symbols carry no dimension. A dashed outline on a small circle stops
# reading as a symbol, so an unverified position draws solid in dark grey
# instead. Tag the sheet with the position's FV tag.


def _symbol_kw(status: str, width: float) -> dict:
    stroke = "#5a5a5a" if status in UNVERIFIED else INK
    return {"stroke": stroke, "width": width, "layer": "annot"}


def light(view: View, at, r: float = 8.0, status: str = "MEASURED", tag: str = ""):
    """Ceiling light: circle with a cross."""
    kw = _symbol_kw(status, 1.0)
    view.circle_pt(*at, r, fill=WHITE, **kw)
    view.path_pt(at, [("M", -r - 2, 0), ("L", r + 2, 0), ("M", 0, -r - 2), ("L", 0, r + 2)], **kw)
    if tag:
        return view.text(*at, tag, size=6, dx=r + 3, dy=r, role="symbol")


def recept(view: View, at, along: str = "E", status: str = "MEASURED", tag: str = ""):
    """Duplex receptacle: circle with two parallel lines along the wall."""
    kw = _symbol_kw(status, 0.9)
    view.circle_pt(*at, 4.5, fill=WHITE, **kw)
    if along in ("E", "W"):
        segs = [("M", -1.6, -7.0), ("L", -1.6, 7.0), ("M", 1.6, -7.0), ("L", 1.6, 7.0)]
    else:
        segs = [("M", -7.0, -1.6), ("L", 7.0, -1.6), ("M", -7.0, 1.6), ("L", 7.0, 1.6)]
    view.path_pt(at, segs, **kw)
    if tag:
        return view.text(*at, tag, size=6, dx=6, dy=4, role="symbol")


def switch(view: View, at, label: str = "S", tag: str = ""):
    """Wall switch, drawn as its letter (S, S3, SD for dimmer)."""
    recs = [view.text(*at, label, size=9, bold=True, anchor="middle", dy=-3.2, role="symbol")]
    if tag:
        recs.append(view.text(*at, tag, size=6, dx=6, dy=4, role="symbol"))
    return recs


def alarm(view: View, at, label: str = "SD", status: str = "MEASURED", r: float = 9.5):
    """Smoke or CO alarm: circle with its letters. label 'SD', 'CO' or 'SD/CO'."""
    kw = _symbol_kw(status, 1.1)
    view.circle_pt(*at, r, fill=WHITE, **kw)
    parts = label.split("/")
    recs = []
    for i, p in enumerate(parts):
        dy = (len(parts) - 1) * 3.4 - i * 6.8 - 2.4
        recs.append(view.text(*at, p, size=6.0 if len(parts) > 1 else 7.0, bold=True, anchor="middle",
                              dy=dy, role="symbol", collide=False))
    return recs


def switch_leg(view: View, a, b, bend_pt: float = 10.0):
    """Dashed curved line from a switch to a light."""
    pa, pb = view.P(*a), view.P(*b)
    mx, my = (pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2
    dx, dy = pb[0] - pa[0], pb[1] - pa[1]
    L = math.hypot(dx, dy) or 1.0
    c = (mx - dy / L * bend_pt, my + dx / L * bend_pt)
    view.paper_path([("M",) + pa, ("C", (pa[0] + 2 * c[0]) / 3, (pa[1] + 2 * c[1]) / 3,
                                    (pb[0] + 2 * c[0]) / 3, (pb[1] + 2 * c[1]) / 3) + pb],
                    stroke=INK2, width=0.6, dash=(3.0, 2.5), layer="annot")
