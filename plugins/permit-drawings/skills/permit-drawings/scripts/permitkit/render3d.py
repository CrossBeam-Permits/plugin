"""3D views drawn by the kit, in colour, from the same project numbers as the plans.

A small scene model (walls with openings, slabs, roofs, boxes for cabinets,
fixtures and furniture, members for posts, beams and rafters), two cameras
(parallel axonometric and true perspective), flat shading from a sun
direction, and painter's ordering through a BSP tree that splits faces where
they cross. The result goes into the kit's display list as filled, stroked
polygons inside an N.T.S. View cell, so it prints as crisp vector in the PDF
and the SVG preview.

Every element carries the status of the Values it was built from. An element
that rests on an ASSUMED or PLACEHOLDER value draws lighter, with grey dashed
edges and its FV tag. Callouts on a 3D view print text built from project.json
Values and `rules`, never typed numbers, and a dimension callout checks that the
drawn geometry measures the Value it prints.

Axes as everywhere in the kit: x = east, y = north, z = up, real inches.

Typical sheet script:

    from permitkit import render3d as r3

    def build(kit):
        sh = kit.sheet("A-0.2")
        scene = r3.Scene.from_project(kit.project)
        v = r3.View3D(sh, scene, "kitchen", "KITCHEN — INTERIOR PERSPECTIVE", cell=(0, 0, 20, 14))
        v.callout(scene["ISLAND"].at(0.5, 0, 1), v.rule_text("R-6", "{rule.limit} {rule.op} RECEPTACLE AT THE ISLAND"))
        v.dim(a, b, kit.value("hood_h"), rule="R-10")
        return sh
"""
from __future__ import annotations

import functools
import math

from . import textmetrics as tm
from .display import GREY, INK, INK2, WHITE, LayoutError, poly_segments, rect_segments, rgb, text_box
from .model import PrintRefused, Value
from .model import fv_text
from .notes import Txt, fill, tags_for, value_text
from .tables import rule as rule_entry
from .units import UnitError, convert

# ------------------------------------------------------------------ vectors


def _add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def _sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def _mul(a, k):
    return (a[0] * k, a[1] * k, a[2] * k)


def _dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def _norm(a):
    n = math.sqrt(_dot(a, a))
    if n < 1e-12:
        raise ValueError("zero-length vector")
    return (a[0] / n, a[1] / n, a[2] / n)


def _lerp(a, b, t):
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(len(a)))


def _newell(pts):
    nx = ny = nz = 0.0
    n = len(pts)
    for i in range(n):
        x1, y1, z1 = pts[i]
        x2, y2, z2 = pts[(i + 1) % n]
        nx += (y1 - y2) * (z1 + z2)
        ny += (z1 - z2) * (x1 + x2)
        nz += (x1 - x2) * (y1 + y2)
    return _norm((nx, ny, nz))


def _dir(az_deg, alt_deg):
    """Unit vector toward compass bearing az (clockwise from plan north) at altitude alt."""
    az, alt = math.radians(az_deg), math.radians(alt_deg)
    return (math.sin(az) * math.cos(alt), math.cos(az) * math.cos(alt), math.sin(alt))


COMPASS = {"N": (0.0, 1.0, 0.0), "S": (0.0, -1.0, 0.0), "E": (1.0, 0.0, 0.0), "W": (-1.0, 0.0, 0.0)}

EPS = 1e-4                 # plane tolerance, inches
NEAR = 3.0                 # perspective near plane, inches in front of the eye

# ------------------------------------------------------------------ materials

#: Default materials: name -> (hex colour, swatch label). project.json
#: model3d.materials adds to or overrides these.
MATERIALS = {
    "stucco": ("#e6dcc6", "STUCCO"),
    "siding": ("#d8d1bf", "SIDING"),
    "trim": ("#f6f4ee", "TRIM, WHITE"),
    "roof": ("#5d646d", "ROOFING"),
    "glass": ("#9dc1d6", "GLASS"),
    "door": ("#7a5236", "DOOR"),
    "concrete": ("#cdc8bd", "CONCRETE"),
    "grass": ("#b7c99c", "LAWN"),
    "ground": ("#ddd6c5", "GRADE"),
    "wood_floor": ("#c9a06c", "WOOD FLOOR"),
    "tile": ("#dcd8cf", "TILE"),
    "drywall": ("#f1ede4", "PAINTED GYPSUM BOARD"),
    "ceiling": ("#f7f5ef", "CEILING, PAINTED"),
    "cabinet": ("#efe5cb", "CABINETS"),
    "counter": ("#e4e2dd", "COUNTERTOP"),
    "steel": ("#c4c8cc", "STAINLESS STEEL"),
    "appliance": ("#d3d6d9", "APPLIANCE"),
    "dark": ("#3b3e42", "DARK METAL"),
    "wood": ("#b27e4f", "WOOD"),
    "fixture": ("#f6f6f2", "FIXTURE, WHITE"),
    "plate": ("#f8f8f4", "DEVICE PLATE"),
    "cut": ("#6f6f6f", "CUT WALL"),
}

FIT_PAD = 0.06   # share of a fitted axon frame left around the fit elements
FRAME_W = 1.75  # schematic window/door frame width, in.; a drawing size only

VERIFIED, ASSUMED, PLACEHOLDER = "VERIFIED", "ASSUMED", "PLACEHOLDER"

#: Edge weights in points: silhouette (outline against something farther),
#: crease (a fold between two faces you see), fine (panel and frame detail).
EDGE_W = {"sil": 1.05, "crease": 0.5, "fine": 0.28}
EDGE_INK = (0.16, 0.16, 0.17)
DASH = {ASSUMED: (5.0, 2.5), PLACEHOLDER: (7.0, 2.0, 1.5, 2.0)}

KINDS = ("box", "wall", "slab", "roof", "member", "device")
STYLES = ("plain", "base", "upper", "tall", "range", "fridge", "hood", "basin", "panel")
ROOF_FORMS = ("gable", "hip", "shed", "flat")


# ------------------------------------------------------------------ scene


class Face:
    """One planar polygon of an element. edges[i] is the class of edge pts[i] -> pts[i+1]:
    'auto' (classified against its neighbours), 'sil', 'crease', 'fine' or None (never drawn)."""

    __slots__ = ("pts", "n", "d", "base", "elem", "edges", "two", "kind", "mat")

    def __init__(self, pts, elem, base, edges=None, two=False, kind="", hint=None):
        pts = [tuple(float(c) for c in p) for p in pts]
        edges = list(edges) if edges is not None else ["auto"] * len(pts)
        n = _newell(pts)
        if hint is not None and _dot(n, hint) < 0:
            m = len(pts)
            pts = pts[::-1]
            edges = [edges[(m - 2 - j) % m] for j in range(m)]
            n = _mul(n, -1.0)
        self.pts, self.n, self.d = pts, n, _dot(n, pts[0])
        self.base, self.elem, self.edges, self.two, self.kind = base, elem, edges, two, kind
        self.mat = elem.material


class Element:
    """A thing in the scene: a wall, a box, a roof. Holds its faces and status."""

    def __init__(self, ident, kind, status=VERIFIED, fv=(), material="", label="", keys=()):
        self.id = ident
        self.kind = kind
        self.status = status
        self.fv = tuple(fv)
        self.material = material
        self.label = label
        self.keys = tuple(keys)
        self.faces: list[Face] = []
        self.prisms: list[tuple] = []        # (plan points, z low, z high): solids a section can cap
        self.lo = None
        self.hi = None

    @property
    def unverified(self) -> bool:
        return self.status != VERIFIED

    def _grow(self, pts):
        for p in pts:
            self.lo = p if self.lo is None else tuple(min(a, b) for a, b in zip(self.lo, p))
            self.hi = p if self.hi is None else tuple(max(a, b) for a, b in zip(self.hi, p))

    def at(self, fx=0.5, fy=0.5, fz=0.5) -> tuple:
        """A point inside the element's bounding box, by fractions: at(0.5, 0, 1) is the
        middle of the south top edge."""
        return tuple(self.lo[i] + (self.hi[i] - self.lo[i]) * f for i, f in enumerate((fx, fy, fz)))

    def top(self, fx=0.5, fy=0.5) -> tuple:
        """The highest point of the element's surface over a plan point given by bounding-box
        fractions: top(0.25, 0.5) lands on a roof slope or a counter top, where a callout
        leader should point."""
        x, y = (self.lo[i] + (self.hi[i] - self.lo[i]) * f for i, f in enumerate((fx, fy)))
        best = None
        for f in self.faces:
            if abs(f.n[2]) < 1e-6:
                continue
            z = (f.d - f.n[0] * x - f.n[1] * y) / f.n[2]
            if _in_face(f, (x, y, z)) and (best is None or z > best):
                best = z
        if best is None:
            raise LayoutError(f"3D element {self.id}: no surface over plan fraction ({fx:g}, {fy:g})")
        return (x, y, best)


def _f(x) -> float:
    return float(x)


def _vals(*xs):
    out = []
    for x in xs:
        if isinstance(x, Value):
            out.append(x)
        elif isinstance(x, (list, tuple)):
            out.extend(_vals(*x))
    return out


class Scene:
    """The model a 3D view draws. Build it from project.json with Scene.from_project(),
    or add elements from a sheet script with the add_* methods (numbers or Values)."""

    def __init__(self, project=None, materials=None, sun=(210.0, 45.0)):
        self.project = project
        self.materials = {k: (rgb(c), lab) for k, (c, lab) in MATERIALS.items()}
        for name, spec in (materials or {}).items():
            if isinstance(spec, str):
                self.materials[name] = (rgb(spec), self.materials.get(name, (None, name.upper()))[1])
            else:
                self.materials[name] = (rgb(spec["rgb"]), spec.get("label", name.upper()))
        self.sun = tuple(float(s) for s in sun)
        self.elements: list[Element] = []
        self._by_id: dict[str, Element] = {}
        self.cameras: dict[str, dict] = {}

    # ---- lookup

    def __getitem__(self, ident) -> Element:
        return self._by_id[ident]

    def __contains__(self, ident) -> bool:
        return ident in self._by_id

    def color(self, name) -> tuple:
        if name not in self.materials:
            raise LayoutError(f"unknown 3D material {name!r}; add it to model3d.materials "
                              f"(known: {', '.join(sorted(self.materials))})")
        return self.materials[name][0]

    def _status(self, values, assumed=None):
        """Status and FV tags of an element from the Values it was built from."""
        tags, placeholder, unverified = [], False, False
        for v in values:
            for t in v.fv_tags:
                if t not in tags:
                    tags.append(t)
            if v.unverified:
                unverified = True
                if self.project is not None:
                    placeholder |= any(self.project.values[u].status == "PLACEHOLDER"
                                       for u in v.unverified_inputs if u in self.project.values)
                else:
                    placeholder |= v.status == "PLACEHOLDER"
        if assumed:
            unverified = True
            if assumed.get("fv") and assumed["fv"] not in tags:
                tags.append(assumed["fv"])
        status = PLACEHOLDER if placeholder else ASSUMED if unverified else VERIFIED
        return status, tags

    def _new(self, ident, kind, values, material, label="", assumed=None) -> Element:
        if ident in self._by_id:
            raise LayoutError(f"3D element id {ident!r} is used twice")
        self.color(material)
        status, tags = self._status(values, assumed)
        el = Element(ident, kind, status, tags, material, label, [v.key for v in values])
        self.elements.append(el)
        self._by_id[ident] = el
        return el

    def _face(self, el, pts, material, hint, edges=None, two=False, kind="", shade=1.0):
        base = self.color(material)
        if shade != 1.0:
            base = tuple(min(1.0, c * shade) for c in base)
        f = Face(pts, el, base, edges, two, kind, hint)
        f.mat = material
        el.faces.append(f)
        el._grow(f.pts)
        return f

    def _box(self, el, x0, y0, z0, x1, y1, z1, material, kind="", prism=True, edges="auto", shade=1.0):
        if x1 - x0 <= 1e-6 or y1 - y0 <= 1e-6 or z1 - z0 <= 1e-6:
            raise LayoutError(f"3D element {el.id}: a box needs a positive size, got "
                              f"{x1 - x0:g} x {y1 - y0:g} x {z1 - z0:g} in")
        e = [edges] * 4
        quads = [
            ([(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)], (0, 0, -1)),
            ([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], (0, 0, 1)),
            ([(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)], (0, -1, 0)),
            ([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], (0, 1, 0)),
            ([(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)], (-1, 0, 0)),
            ([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], (1, 0, 0)),
        ]
        for pts, hint in quads:
            self._face(el, pts, material, hint, e, kind=kind, shade=shade)
        if prism:
            el.prisms.append(([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], z0, z1, material))

    # ---- elements

    def add_box(self, ident, x, y, z, w, d, h, material="cabinet", style="plain", front="S",
                label="", values=(), assumed=None) -> Element:
        """A box from its south-west-bottom corner (x, y, z) and its size w (east), d (north),
        h (up). style draws schematic detail on the `front` face (N, S, E or W):
        base, upper, tall (cabinet doors and drawers), range, fridge, hood, basin, panel.
        Detail positions are schematic and print no number."""
        el = self._new(ident, "box", _vals(x, y, z, w, d, h, values), material, label, assumed)
        x0, y0, z0 = _f(x), _f(y), _f(z)
        x1, y1, z1 = x0 + _f(w), y0 + _f(d), z0 + _f(h)
        if style not in STYLES:
            raise LayoutError(f"3D element {ident}: style {style!r} is not one of {', '.join(STYLES)}")
        if front not in COMPASS:
            raise LayoutError(f"3D element {ident}: front must be N, S, E or W, not {front!r}")
        if style == "hood":
            self._hood(el, x0, y0, z0, x1, y1, z1, material, front)
            return el
        self._box(el, x0, y0, z0, x1, y1, z1, material)
        if style != "plain":
            _Detail(self, el, (x0, y0, z0, x1, y1, z1), front, material).draw(style)
        return el

    def _hood(self, el, x0, y0, z0, x1, y1, z1, material, front):
        """A canopy range hood: a flared canopy over the cooktop and a chimney above it."""
        h = z1 - z0
        zc = z0 + min(h, max(6.0, h * 0.28))            # top of the canopy (schematic)
        fx, fy = COMPASS[front][0], COMPASS[front][1]
        cw = 0.36                                        # chimney share of the width (schematic)
        cx0, cx1 = x0 + (x1 - x0) * (0.5 - cw / 2), x0 + (x1 - x0) * (0.5 + cw / 2)
        cy0, cy1 = y0 + (y1 - y0) * (0.5 - cw / 2), y0 + (y1 - y0) * (0.5 + cw / 2)
        # the chimney sits against the back (the side away from `front`)
        if fx == 0:
            cx0, cx1 = x0 + (x1 - x0) * 0.32, x1 - (x1 - x0) * 0.32
            cy0, cy1 = (y0, y0 + (y1 - y0) * 0.45) if fy > 0 else (y1 - (y1 - y0) * 0.45, y1)
        else:
            cy0, cy1 = y0 + (y1 - y0) * 0.32, y1 - (y1 - y0) * 0.32
            cx0, cx1 = (x0, x0 + (x1 - x0) * 0.45) if fx > 0 else (x1 - (x1 - x0) * 0.45, x1)
        lip = min(2.0, (zc - z0) / 3)
        self._box(el, x0, y0, z0, x1, y1, z0 + lip, material, prism=False)
        bot = [(x0, y0, z0 + lip), (x1, y0, z0 + lip), (x1, y1, z0 + lip), (x0, y1, z0 + lip)]
        top = [(cx0, cy0, zc), (cx1, cy0, zc), (cx1, cy1, zc), (cx0, cy1, zc)]
        for i in range(4):
            j = (i + 1) % 4
            pts = [bot[i], bot[j], top[j], top[i]]
            mid = _mul(_add(_add(bot[i], bot[j]), _add(top[i], top[j])), 0.25)
            c = ((x0 + x1) / 2, (y0 + y1) / 2, (z0 + zc) / 2)
            hint = _sub(mid, c)
            if _dot(hint, hint) < 1e-9:
                continue
            try:
                self._face(el, pts, material, (hint[0], hint[1], 0.0))
            except ValueError:
                continue
        if z1 - zc > 1e-6:
            self._box(el, cx0, cy0, zc, cx1, cy1, z1, material, prism=False)
        el.prisms.append(([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], z0, z1, material))

    def add_slab(self, ident, x0, y0, x1, y1, z, t, material="concrete", label="", values=(),
                 assumed=None) -> Element:
        """A slab, floor or ground pad from x0..x1, y0..y1 whose top is at z, t thick."""
        el = self._new(ident, "slab", _vals(x0, y0, x1, y1, z, t, values), material, label, assumed)
        zt = _f(z)
        self._box(el, min(_f(x0), _f(x1)), min(_f(y0), _f(y1)), zt - _f(t),
                  max(_f(x0), _f(x1)), max(_f(y0), _f(y1)), zt, material)
        return el

    def add_member(self, ident, a, b, w, d, material="wood", count=1, step=(0, 0, 0), label="",
                   values=(), assumed=None) -> Element:
        """A post, beam or rafter from 3D point a to b with a w (side) x d (depth) section.
        count and step repeat it, e.g. rafters at 24 in. on center."""
        el = self._new(ident, "member", _vals(a, b, w, d, count, step, values), material, label, assumed)
        a = tuple(_f(c) for c in a)
        b = tuple(_f(c) for c in b)
        st = tuple(_f(c) for c in step)
        n = int(round(_f(count)))
        if n < 1:
            raise LayoutError(f"3D element {ident}: count must be at least 1")
        for k in range(n):
            off = _mul(st, k)
            self._member(el, _add(a, off), _add(b, off), _f(w), _f(d), material)
        return el

    def _member(self, el, a, b, w, d, material):
        axis = _sub(b, a)
        u = _norm(axis)
        if abs(u[2]) > 0.999:                       # vertical post
            s, up = (1.0, 0.0, 0.0), (0.0, 1.0, 0.0)
        else:
            s = _norm(_cross(u, (0.0, 0.0, 1.0)))
            up = _cross(s, u)
        hw, hd = w / 2, d / 2
        if abs(u[2]) <= 0.999 and abs(u[2]) < 1e-9:
            # a level beam: hang the section so its top is at the given points (d down)
            a2, b2 = _sub(a, (0, 0, hd)), _sub(b, (0, 0, hd))
        else:
            a2, b2 = a, b
        corners = []
        for p in (a2, b2):
            corners.append([_add(_add(p, _mul(s, sx * hw)), _mul(up, sy * hd))
                            for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1))])
        ca, cb = corners
        cen = _mul(_add(a2, b2), 0.5)
        for i in range(4):
            j = (i + 1) % 4
            pts = [ca[i], ca[j], cb[j], cb[i]]
            mid = _mul(_add(_add(ca[i], ca[j]), _add(cb[i], cb[j])), 0.25)
            self._face(el, pts, material, _sub(mid, cen))
        self._face(el, ca, material, _mul(u, -1))
        self._face(el, cb, material, u)
        if abs(u[2]) > 0.999:
            lo, hi = min(a[2], b[2]), max(a[2], b[2])
            el.prisms.append(([(c[0], c[1]) for c in ca], lo, hi, material))

    def add_device(self, ident, x, y, z, face, material="plate", label="", values=(), assumed=None,
                   size=(2.75, 4.5)) -> Element:
        """A wall device plate (receptacle, switch) centred at (x, y, z) on a wall face,
        facing `face` (N, S, E, W, or U for a worktop device). The plate size is a schematic
        symbol size."""
        el = self._new(ident, "device", _vals(x, y, z, values), material, label, assumed)
        c = (_f(x), _f(y), _f(z))
        if face == "U":
            n, s, up = (0.0, 0.0, 1.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0)
        elif face in COMPASS:
            n = COMPASS[face]
            s, up = (-n[1], n[0], 0.0), (0.0, 0.0, 1.0)
        else:
            raise LayoutError(f"3D element {ident}: face must be N, S, E, W or U (up), not {face!r}")
        pw, ph = size
        t = 0.3
        self._plate(el, c, n, s, pw, ph, t, material, up=up)
        self._plate(el, _add(c, _mul(n, t)), n, s, pw * 0.55, ph * 0.62, 0.05, "appliance", detail=True, up=up)
        return el

    def _plate(self, el, c, n, s, pw, ph, t, material, detail=False, up=(0.0, 0.0, 1.0)):
        z = up
        back = [_add(_add(c, _mul(s, sx * pw / 2)), _mul(z, sz * ph / 2))
                for sx, sz in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
        front = [_add(p, _mul(n, t)) for p in back]
        ek = ["fine"] * 4 if detail else None
        self._face(el, front, material, n, ek, kind="detail" if detail else "")
        if not detail:
            for i in range(4):
                j = (i + 1) % 4
                mid = _mul(_add(_add(back[i], back[j]), _add(front[i], front[j])), 0.25)
                self._face(el, [back[i], back[j], front[j], front[i]], material, _sub(mid, c))

    def add_wall(self, ident, a, b, t, z, h, body="left", openings=(), material="stucco", inner=None,
                 label="", values=(), assumed=None) -> Element:
        """A straight wall whose finished face runs from plan point a to b, t thick toward
        `body` (N, S, E, W, 'left' or 'right' of a->b), from z up h.

        openings: dicts {offset, width, sill, height, kind, style, material}; offset runs
        from a along the face; sill is above z. kind: window, door, glass_door or opening.
        style for windows and glass doors: fixed, XO (two panes) or pair."""
        el = self._new(ident, "wall", _vals(a, b, t, z, h, values), material, label, assumed)
        ax, ay, bx, by = _f(a[0]), _f(a[1]), _f(b[0]), _f(b[1])
        L = math.hypot(bx - ax, by - ay)
        if L < 1e-6:
            raise LayoutError(f"3D wall {ident}: a and b are the same point")
        u = ((bx - ax) / L, (by - ay) / L, 0.0)
        if body in COMPASS:
            nb = COMPASS[body]
        elif body == "left":
            nb = (-u[1], u[0], 0.0)
        elif body == "right":
            nb = (u[1], -u[0], 0.0)
        else:
            raise LayoutError(f"3D wall {ident}: body must be N, S, E, W, left or right")
        if abs(_dot(u, nb)) > 1e-6:
            raise LayoutError(f"3D wall {ident}: body {body} is not at right angles to the wall run")
        T, z0 = _f(t), _f(z)
        z1 = z0 + _f(h)
        inner = inner or material
        ops = []
        for o in openings:
            s0 = _f(o["offset"])
            s1 = s0 + _f(o["width"])
            zl = z0 + _f(o.get("sill", 0.0))
            zh = zl + _f(o["height"])
            oid = o.get("id", "?")
            if s0 < -EPS or s1 > L + EPS or zl < z0 - EPS or zh > z1 + EPS or s1 - s0 <= EPS or zh - zl <= EPS:
                raise LayoutError(f"3D wall {ident}: opening {oid} ({s0:g}..{s1:g} along, {zl:g}..{zh:g} up) "
                                  f"does not fit the wall (0..{L:g} along, {z0:g}..{z1:g} up)")
            ops.append((max(0.0, s0), min(L, s1), max(z0, zl), min(z1, zh), o))

        def P(s, depth, zz):
            return (ax + u[0] * s + nb[0] * depth, ay + u[1] * s + nb[1] * depth, zz)

        S = sorted({0.0, L, *[o[0] for o in ops], *[o[1] for o in ops]})
        Z = sorted({z0, z1, *[o[2] for o in ops], *[o[3] for o in ops]})
        S = _dedupe(S)
        Z = _dedupe(Z)
        ns, nz = len(S) - 1, len(Z) - 1

        def is_open(i, j):
            sm, zm = (S[i] + S[i + 1]) / 2, (Z[j] + Z[j + 1]) / 2
            return any(o[0] < sm < o[1] and o[2] < zm < o[3] for o in ops)

        solid = [[not is_open(i, j) for j in range(nz)] for i in range(ns)]
        out, inw = _mul(nb, -1.0), nb
        up, down = (0.0, 0.0, 1.0), (0.0, 0.0, -1.0)
        mu = _mul(u, -1.0)
        for i in range(ns):
            for j in range(nz):
                if not solid[i][j]:
                    continue
                s0, s1, za, zb = S[i], S[i + 1], Z[j], Z[j + 1]
                self._face(el, [P(s0, 0, za), P(s1, 0, za), P(s1, 0, zb), P(s0, 0, zb)], material, out)
                self._face(el, [P(s0, T, za), P(s1, T, za), P(s1, T, zb), P(s0, T, zb)], inner, inw)
                el.prisms.append(([P(s0, 0, 0)[:2], P(s1, 0, 0)[:2], P(s1, T, 0)[:2], P(s0, T, 0)[:2]],
                                  za, zb, material))
                # left / right: an end cap at the wall end, or a jamb at an opening
                if i == 0 or not solid[i - 1][j]:
                    self._face(el, [P(s0, 0, za), P(s0, T, za), P(s0, T, zb), P(s0, 0, zb)], material, mu)
                if i == ns - 1 or not solid[i + 1][j]:
                    self._face(el, [P(s1, 0, za), P(s1, T, za), P(s1, T, zb), P(s1, 0, zb)], material, u)
                if j == 0 or not solid[i][j - 1]:
                    self._face(el, [P(s0, 0, za), P(s1, 0, za), P(s1, T, za), P(s0, T, za)], material, down)
                if j == nz - 1 or not solid[i][j + 1]:
                    mat = material if j == nz - 1 else "trim"
                    self._face(el, [P(s0, 0, zb), P(s1, 0, zb), P(s1, T, zb), P(s0, T, zb)], mat, up)
        for s0, s1, zl, zh, o in ops:
            kind = o.get("kind", "window")
            style = o.get("style", "fixed")
            if kind == "opening":
                continue
            # the glass or leaf is an element of its own: it carries the status of the
            # opening's values, while the wall keeps the status of its own
            ov = _vals(*[o.get(k) for k in ("offset", "width", "sill", "height")])
            sub = self._new(f"{ident}.{o.get('id', 'opening')}", "opening", ov,
                            o.get("material") or ("door" if kind == "door" else "glass"), o.get("id", ""),
                            assumed)
            if kind == "door":
                dm = o.get("material", "door")
                depth = T * 0.75
                self._face(sub, [P(s0, depth, zl), P(s1, depth, zl), P(s1, depth, zh), P(s0, depth, zh)],
                           dm, out, ["crease"] * 4, two=True, kind="door")
                continue
            depth = T / 2
            fm = o.get("material", "trim")
            panes = 2 if style in ("XO", "pair") else 1
            # schematic frame: a drawing size only, never printed
            fw = min(FRAME_W, (s1 - s0) / panes / 6, (zh - zl) / 6)
            rail = fw * (3 if kind == "glass_door" else 1)
            for k in range(panes):
                a0 = s0 + (s1 - s0) * k / panes
                a1 = s0 + (s1 - s0) * (k + 1) / panes
                g0, g1, h0, h1 = a0 + fw, a1 - fw, zl + rail, zh - fw
                quad = (lambda u0, u1, w0, w1: [P(u0, depth, w0), P(u1, depth, w0), P(u1, depth, w1),
                                                P(u0, depth, w1)])
                self._face(sub, quad(g0, g1, h0, h1), "glass", out, ["fine"] * 4, two=True, kind="glass")
                for u0, u1, w0, w1 in ((a0, a1, zl, h0), (a0, a1, h1, zh), (a0, g0, h0, h1), (g1, a1, h0, h1)):
                    on = (w0 == zl, u1 == a1, w1 == zh, u0 == a0)  # edges on the pane outline
                    self._face(sub, quad(u0, u1, w0, w1), fm, out, ["crease" if b else None for b in on],
                               two=True, kind="frame")
        return el

    def wall_from_plan(self, ident, wall, z, h, openings=(), material="stucco", inner=None, label="",
                       values=(), assumed=None) -> Element:
        """A 3D wall from an arch.Wall a plan sheet already drew: same face line, run and
        thickness. Give the base z and height h; openings as for add_wall."""
        a = wall.start
        b = (a[0] + wall.a[0] * wall.length, a[1] + wall.a[1] * wall.length)
        return self.add_wall(ident, a, b, wall.t, z, h, body=wall.body, openings=openings,
                             material=material, inner=inner, label=label, values=values, assumed=assumed)

    def add_roof(self, ident, x0, y0, x1, y1, z, pitch, overhang, rake=None, form="gable", ridge="x",
                 low="S", thick=None, material="roof", wall_material="stucco", fascia_material="trim",
                 label="", values=(), assumed=None) -> Element:
        """A roof over the wall footprint x0..x1, y0..y1 (outside faces) with its underside
        at z on the wall faces. pitch is the rise per 12 of run. form: gable (ridge along
        `ridge`, 'x' or 'y'), hip, shed (low eave on side `low`) or flat. overhang is the
        eave overhang, rake the gable-end overhang (default overhang). thick is the roof
        edge depth (default 6 in., a drawing size only)."""
        el = self._new(ident, "roof", _vals(x0, y0, x1, y1, z, pitch, overhang, rake, thick, values),
                       material, label, assumed)
        if form not in ROOF_FORMS:
            raise LayoutError(f"3D roof {ident}: form {form!r} is not one of {', '.join(ROOF_FORMS)}")
        X0, X1 = sorted((_f(x0), _f(x1)))
        Y0, Y1 = sorted((_f(y0), _f(y1)))
        zp, p, o = _f(z), _f(pitch) / 12.0, _f(overhang)
        r = o if rake is None else _f(rake)
        th = 6.0 if thick is None else _f(thick)
        _Roof(self, el, (X0, Y0, X1, Y1), zp, p, o, r, th, material, wall_material, fascia_material,
              form, ridge, low).build()
        return el

    # ---- from project.json

    @classmethod
    def from_project(cls, project) -> "Scene":
        """The scene described by project.json `model3d`."""
        m = project.data.get("model3d") or {}
        sun = m.get("sun", {})
        sc = cls(project, m.get("materials"), (sun.get("azimuth", 210.0), sun.get("altitude", 45.0)))
        for cam in m.get("cameras", []):
            sc.cameras[cam["id"]] = cam
        for e in m.get("elements", []):
            if e.get("action") == "demo":
                continue
            sc._from_item(e)
        return sc

    def _dim(self, e, field, default=None, required=True):
        raw = e.get(field)
        if raw is None:
            if default is not None or not required:
                return default
            raise LayoutError(f"model3d element {e['id']} ({e['kind']}) needs {field!r}")
        return _resolve(self.project, raw)

    def _from_item(self, e):
        k, g = e["kind"], (lambda f, d=None, r=True: self._dim(e, f, d, r))
        common = {"label": e.get("label", ""), "assumed": e.get("assumed")}
        mat = e.get("material")
        if k == "box":
            self.add_box(e["id"], g("x"), g("y"), g("z"), g("w"), g("d"), g("h"), mat or "cabinet",
                         e.get("style", "plain"), e.get("front", "S"), **common)
        elif k == "slab":
            self.add_slab(e["id"], g("x0"), g("y0"), g("x1"), g("y1"), g("z"), g("t"), mat or "concrete",
                          **common)
        elif k == "wall":
            ops = [self._opening(e, o) for o in e.get("openings", [])]
            self.add_wall(e["id"], (g("x0"), g("y0")), (g("x1"), g("y1")), g("t"), g("z"), g("h"),
                          e.get("body", "left"), ops, mat or "stucco", e.get("inner"), **common)
        elif k == "roof":
            self.add_roof(e["id"], g("x0"), g("y0"), g("x1"), g("y1"), g("z"), g("pitch"), g("overhang"),
                          g("rake", None, False), e.get("form", "gable"), e.get("ridge", "x"), e.get("low", "S"),
                          g("thick", None, False), mat or "roof", e.get("wall_material", "stucco"),
                          e.get("fascia_material", "trim"), **common)
        elif k == "member":
            step = (g("step_x", None, False) or 0.0, g("step_y", None, False) or 0.0,
                    g("step_z", None, False) or 0.0)
            self.add_member(e["id"], (g("x0"), g("y0"), g("z0")), (g("x1"), g("y1"), g("z1")), g("w"), g("d"),
                            mat or "wood", g("count", None, False) or 1, step, **common)
        elif k == "device":
            self.add_device(e["id"], g("x"), g("y"), g("z"), e.get("face", "S"), mat or "plate", **common)
        else:
            raise LayoutError(f"model3d element {e['id']}: kind {k!r} is not one of {', '.join(KINDS)}")

    def _opening(self, e, o):
        out = {"id": o.get("ref") or o.get("id"), "kind": o.get("kind"), "style": o.get("style", "fixed"),
               "material": o.get("material")}
        item = {}
        if o.get("ref"):
            item = self.project.item("openings", o["ref"])
            if out["kind"] is None:
                out["kind"] = {"window": "window", "slider": "window", "door": "door", "dutch_door": "door",
                               "pocket": "door", "bifold": "door", "bypass": "door"}.get(item["type"], "opening")
        out["kind"] = out["kind"] or "window"
        for f in ("offset", "width", "sill", "height"):
            raw = o.get(f, item.get(f))
            if raw is None:
                if f == "sill":
                    out[f] = 0.0
                    continue
                raise LayoutError(f"model3d element {e['id']}: opening {out['id']} needs {f!r}")
            out[f] = _resolve(self.project, raw)
        if out["material"] is None:
            out.pop("material")
        return out

    def camera(self, ident, aspect=1.5) -> "Camera":
        if ident not in self.cameras:
            raise LayoutError(f"no camera {ident!r} in model3d.cameras ({', '.join(self.cameras) or 'none'})")
        return Camera.from_spec(self.cameras[ident], self.project, aspect)


def _resolve(project, raw):
    """A Dim from project.json: '$key' (also an item field), an inline Value, or a number
    (cameras only)."""
    if isinstance(raw, (int, float)) and not isinstance(raw, bool):
        return float(raw)
    if isinstance(raw, Value):
        return raw
    if project is None:
        raise LayoutError(f"cannot resolve {raw!r} without a project")
    if isinstance(raw, str):
        return project.lookup(raw)
    return project.dim(raw)


def _dedupe(xs):
    out = []
    for x in xs:
        if not out or x - out[-1] > EPS:
            out.append(x)
    return out


class _Detail:
    """Schematic detail on a box's front face: cabinet doors, drawers, appliance fronts.
    Sizes here are drawing sizes, not design values; they print no number."""

    def __init__(self, scene, el, box, front, material):
        self.sc, self.el, self.box, self.front, self.mat = scene, el, box, front, material
        x0, y0, z0, x1, y1, z1 = box
        n = COMPASS[front]
        self.n = n
        if front == "S":
            self.o, self.u, self.width = (x0, y0, z0), (1.0, 0.0, 0.0), x1 - x0
        elif front == "N":
            self.o, self.u, self.width = (x1, y1, z0), (-1.0, 0.0, 0.0), x1 - x0
        elif front == "W":
            self.o, self.u, self.width = (x0, y1, z0), (0.0, -1.0, 0.0), y1 - y0
        else:
            self.o, self.u, self.width = (x1, y0, z0), (0.0, 1.0, 0.0), y1 - y0
        self.height = z1 - z0

    def P(self, s, zz, out=0.0):
        return _add(_add(self.o, _mul(self.u, s)), _add((0.0, 0.0, zz), _mul(self.n, out)))

    def panel(self, s0, s1, za, zb, material=None, shade=0.955, out=0.3, kind="detail"):
        if s1 - s0 < 0.5 or zb - za < 0.5:
            return
        pts = [self.P(s0, za, out), self.P(s1, za, out), self.P(s1, zb, out), self.P(s0, zb, out)]
        self.sc._face(self.el, pts, material or self.mat, self.n, ["fine"] * 4, kind=kind, shade=shade)

    def handle(self, s, za, zb, horizontal=False, length=5.0):
        """A small dark bar handle centred at s along the face, between za and zb."""
        zm = (za + zb) / 2
        if horizontal:
            pts = [self.P(s - length / 2, zm - 0.3, 1.0), self.P(s + length / 2, zm - 0.3, 1.0),
                   self.P(s + length / 2, zm + 0.3, 1.0), self.P(s - length / 2, zm + 0.3, 1.0)]
        else:
            pts = [self.P(s - 0.3, zm - length / 2, 1.0), self.P(s + 0.3, zm - length / 2, 1.0),
                   self.P(s + 0.3, zm + length / 2, 1.0), self.P(s - 0.3, zm + length / 2, 1.0)]
        self.sc._face(self.el, pts, "dark", self.n, ["fine"] * 4, kind="detail")

    def doors(self, za, zb, max_w=21.0, drawers=False):
        n = max(1, int(round(self.width / max_w)))
        g = 0.375
        for k in range(n):
            s0 = self.width * k / n + g
            s1 = self.width * (k + 1) / n - g
            self.panel(s0, s1, za + g, zb - g)
            if drawers:
                self.handle((s0 + s1) / 2, za, zb, horizontal=True)
            else:
                hs = s1 - 2.0 if k % 2 == 0 else s0 + 2.0
                if n == 1:
                    hs = s1 - 2.0
                self.handle(hs, zb - 6.0 if zb - za > 14 else za, zb, horizontal=False,
                            length=min(5.0, (zb - za) * 0.4))

    def draw(self, style):
        W, H = self.width, self.height
        if style == "base":
            kick = min(4.0, H * 0.12)
            self.panel(0.0, W, 0.0, kick, material="dark", shade=1.0, out=0.05)
            band = min(6.0, (H - kick) * 0.25)
            self.doors(H - band, H, drawers=True)
            self.doors(kick, H - band)
        elif style == "upper":
            self.doors(0.0, H, max_w=18.0)
        elif style == "tall":
            self.doors(0.0, H, max_w=24.0)
        elif style == "range":
            x0, y0, z0, x1, y1, z1 = self.box
            self.panel(W * 0.08, W * 0.92, H * 0.18, H * 0.72, material="dark", shade=1.0)
            self.panel(W * 0.05, W * 0.95, H * 0.80, H * 0.94, material="steel", shade=0.9)
            self.handle(W / 2, H * 0.74, H * 0.78, horizontal=True, length=W * 0.7)
            for fx in (0.28, 0.72):
                for fy in (0.3, 0.7):
                    cx, cy = x0 + (x1 - x0) * fx, y0 + (y1 - y0) * fy
                    r = min(x1 - x0, y1 - y0) * 0.14
                    pts = [(cx - r, cy - r, z1 + 0.2), (cx + r, cy - r, z1 + 0.2), (cx + r, cy + r, z1 + 0.2),
                           (cx - r, cy + r, z1 + 0.2)]
                    self.sc._face(self.el, pts, "dark", (0, 0, 1), ["fine"] * 4, kind="detail")
        elif style == "fridge":
            split = H * 0.68
            self.panel(0.3, W / 2 - 0.2, split + 0.3, H - 0.3, shade=0.97)
            self.panel(W / 2 + 0.2, W - 0.3, split + 0.3, H - 0.3, shade=0.97)
            self.panel(0.3, W - 0.3, 3.0, split - 0.3, shade=0.97)
            self.handle(W / 2 - 1.2, split + 2, split + 20, length=16)
            self.handle(W / 2 + 1.2, split + 2, split + 20, length=16)
            self.handle(W / 2, split - 6, split - 2, horizontal=True, length=W * 0.5)
        elif style == "basin":
            x0, y0, z0, x1, y1, z1 = self.box
            m = min(x1 - x0, y1 - y0) * 0.12
            pts = [(x0 + m, y0 + m, z1 + 0.05), (x1 - m, y0 + m, z1 + 0.05), (x1 - m, y1 - m, z1 + 0.05),
                   (x0 + m, y1 - m, z1 + 0.05)]
            self.sc._face(self.el, pts, "steel", (0, 0, 1), ["fine"] * 4, kind="detail", shade=0.8)
        elif style == "panel":
            self.panel(0.5, W - 0.5, 0.5, H - 0.5)


class _Roof:
    """Roof surfaces in a local frame (a along the ridge, b across), mapped to the world.
    Face orientation comes from outward hints, so the mapping may mirror."""

    def __init__(self, sc, el, fp, z, p, o, r, th, mat, wall_mat, fascia_mat, form, ridge, low):
        self.sc, self.el = sc, el
        X0, Y0, X1, Y1 = fp
        self.z, self.p, self.o, self.r, self.th = z, p, o, r, th
        self.mat, self.wall_mat, self.fascia_mat, self.form = mat, wall_mat, fascia_mat, form
        if form == "shed":
            # b runs from the low eave to the high side
            if low in ("S", "N"):
                self.A, self.B = (X0, X1), (Y0, Y1)
                flip = low == "N"
                self.map = (lambda a, b, zz: (a, Y0 + Y1 - b, zz)) if flip else (lambda a, b, zz: (a, b, zz))
            elif low in ("W", "E"):
                self.A, self.B = (Y0, Y1), (X0, X1)
                flip = low == "E"
                self.map = (lambda a, b, zz: (X0 + X1 - b, a, zz)) if flip else (lambda a, b, zz: (b, a, zz))
            else:
                raise LayoutError(f"3D roof {el.id}: low must be N, S, E or W")
        else:
            if form == "hip":
                ridge = "x" if X1 - X0 >= Y1 - Y0 else "y"
            if ridge == "x":
                self.A, self.B = (X0, X1), (Y0, Y1)
                self.map = lambda a, b, zz: (a, b, zz)
            elif ridge == "y":
                self.A, self.B = (Y0, Y1), (X0, X1)
                self.map = lambda a, b, zz: (b, a, zz)
            else:
                raise LayoutError(f"3D roof {el.id}: ridge must be 'x' or 'y'")

    def face(self, local_pts, material, hint_local, edges=None):
        pts = [self.map(*q) for q in local_pts]
        h = self.map(*hint_local)
        # a hint is a direction: map it without the translation of a flipped axis
        o = self.map(0.0, 0.0, 0.0)
        hint = (h[0] - o[0], h[1] - o[1], h[2] - o[2])
        clean = []
        for q in pts:
            if not clean or max(abs(q[i] - clean[-1][i]) for i in range(3)) > 1e-6:
                clean.append(q)
        if len(clean) > 2 and max(abs(clean[0][i] - clean[-1][i]) for i in range(3)) <= 1e-6:
            clean.pop()
        if len(clean) < 3:
            return
        self.sc._face(self.el, clean, material, hint, edges)

    def build(self):
        getattr(self, "_" + self.form)()

    def _gable(self):
        (a0, a1), (b0, b1) = self.A, self.B
        z, p, o, r, th = self.z, self.p, self.o, self.r, self.th
        bm = (b0 + b1) / 2
        ze, zr = z - o * p, z + (bm - b0) * p
        A0, A1, B0, B1 = a0 - r, a1 + r, b0 - o, b1 + o
        for lift, hint in ((th, (0, 0, 1)), (0.0, (0, 0, -1))):
            self.face([(A0, B0, ze + lift), (A1, B0, ze + lift), (A1, bm, zr + lift), (A0, bm, zr + lift)],
                      self.mat, hint)
            self.face([(A0, B1, ze + lift), (A1, B1, ze + lift), (A1, bm, zr + lift), (A0, bm, zr + lift)],
                      self.mat, hint)
        for bb, hb in ((B0, -1), (B1, 1)):
            self.face([(A0, bb, ze), (A1, bb, ze), (A1, bb, ze + th), (A0, bb, ze + th)], self.fascia_mat, (0, hb, 0))
        for aa, ha in ((A0, -1), (A1, 1)):
            for bb in (B0, B1):
                self.face([(aa, bb, ze), (aa, bm, zr), (aa, bm, zr + th), (aa, bb, ze + th)], self.fascia_mat,
                          (ha, 0, 0))
        for aa, ha in ((a0, -1), (a1, 1)):
            self.face([(aa, b0, z), (aa, b1, z), (aa, bm, zr)], self.wall_mat, (ha, 0, 0))

    def _hip(self):
        (a0, a1), (b0, b1) = self.A, self.B
        z, p, o, th = self.z, self.p, self.o, self.th
        A0, A1, B0, B1 = a0 - o, a1 + o, b0 - o, b1 + o
        ze = z - o * p
        half = (B1 - B0) / 2
        bm = (B0 + B1) / 2
        ra0, ra1 = A0 + half, A1 - half
        for lift, hint in ((th, (0, 0, 1)), (0.0, (0, 0, -1))):
            zb, zt = ze + lift, ze + half * p + lift
            self.face([(A0, B0, zb), (A1, B0, zb), (ra1, bm, zt), (ra0, bm, zt)], self.mat, hint)
            self.face([(A1, B1, zb), (A0, B1, zb), (ra0, bm, zt), (ra1, bm, zt)], self.mat, hint)
            self.face([(A0, B1, zb), (A0, B0, zb), (ra0, bm, zt)], self.mat, hint)
            self.face([(A1, B0, zb), (A1, B1, zb), (ra1, bm, zt)], self.mat, hint)
        for q0, q1, hint in (((A0, B0), (A1, B0), (0, -1, 0)), ((A1, B1), (A0, B1), (0, 1, 0)),
                             ((A0, B1), (A0, B0), (-1, 0, 0)), ((A1, B0), (A1, B1), (1, 0, 0))):
            self.face([(q0[0], q0[1], ze), (q1[0], q1[1], ze), (q1[0], q1[1], ze + th), (q0[0], q0[1], ze + th)],
                      self.fascia_mat, hint)

    def _shed(self):
        (a0, a1), (b0, b1) = self.A, self.B
        z, p, o, r, th = self.z, self.p, self.o, self.r, self.th
        A0, A1, B0, B1 = a0 - r, a1 + r, b0 - o, b1 + o
        zl, zh = z - o * p, z + (b1 - b0 + o) * p
        for lift, hint in ((th, (0, 0, 1)), (0.0, (0, 0, -1))):
            self.face([(A0, B0, zl + lift), (A1, B0, zl + lift), (A1, B1, zh + lift), (A0, B1, zh + lift)],
                      self.mat, hint)
        self.face([(A0, B0, zl), (A1, B0, zl), (A1, B0, zl + th), (A0, B0, zl + th)], self.fascia_mat, (0, -1, 0))
        self.face([(A0, B1, zh), (A1, B1, zh), (A1, B1, zh + th), (A0, B1, zh + th)], self.fascia_mat, (0, 1, 0))
        for aa, ha in ((A0, -1), (A1, 1)):
            self.face([(aa, B0, zl), (aa, B1, zh), (aa, B1, zh + th), (aa, B0, zl + th)], self.fascia_mat, (ha, 0, 0))
        zw = z + (b1 - b0) * p
        self.face([(a0, b1, z), (a1, b1, z), (a1, b1, zw), (a0, b1, zw)], self.wall_mat, (0, 1, 0))
        for aa, ha in ((a0, -1), (a1, 1)):
            self.face([(aa, b0, z), (aa, b1, z), (aa, b1, zw)], self.wall_mat, (ha, 0, 0))

    def _flat(self):
        (a0, a1), (b0, b1) = self.A, self.B
        o, z, th = self.o, self.z, self.th
        pts = lambda zz: [(a0 - o, b0 - o, zz), (a1 + o, b0 - o, zz), (a1 + o, b1 + o, zz), (a0 - o, b1 + o, zz)]
        self.face(pts(z + th), self.mat, (0, 0, 1))
        self.face(pts(z), self.mat, (0, 0, -1))
        c = pts(z)
        for i, hint in enumerate(((0, -1, 0), (1, 0, 0), (0, 1, 0), (-1, 0, 0))):
            q0, q1 = c[i], c[(i + 1) % 4]
            self.face([q0, q1, (q1[0], q1[1], z + th), (q0[0], q0[1], z + th)], self.fascia_mat, hint)


# ------------------------------------------------------------------ cameras

ISO_ELEV = math.degrees(math.atan(1 / math.sqrt(2)))      # 35.264 degrees
DIMETRIC_ELEV = math.degrees(math.asin(math.tan(math.radians(20.705))))  # about 22.2 degrees


class Camera:
    """A parallel (axonometric or plan-oblique) or perspective camera.

    azimuth is the compass bearing from the target to the viewer (225 = viewer to the
    south-west), elevation the angle above the horizon. A perspective camera has an eye
    point, a target point and a lens in millimetres (35 mm frame, 24 = wide)."""

    def __init__(self, kind="axon", projection="iso", azimuth=225.0, elevation=None, rotate=30.0,
                 vscale=1.0, eye=None, target=None, lens=24.0, aspect=1.5, near=NEAR, cut_z=None,
                 hide=(), sun=None, shift=0.0, light=None, fit=()):
        self.kind = kind
        # axon only: frame the view on these elements and clip the rest at the frame
        self.fit = tuple(fit)
        # 'sun' shades from the sun direction; 'interior' from the room's ambient light and the
        # viewer, so a ceiling reads light. Default: interior for a perspective, sun otherwise.
        self.light = light or ("interior" if kind == "perspective" else "sun")
        self.hide = set(hide)
        self.cut_z = cut_z
        self.sun = sun
        self.aspect = aspect
        if kind == "axon":
            if projection == "plan_oblique":
                a = math.radians(rotate)
                k = float(vscale)
                self.mu = (math.cos(a), -math.sin(a), 0.0)
                self.mv = (math.sin(a), math.cos(a), k)
                self.V = _norm((-k * math.sin(a), -k * math.cos(a), 1.0))
            else:
                if elevation is None:
                    elevation = {"iso": ISO_ELEV, "dimetric": 20.705}.get(projection, 30.0)
                V = _dir(azimuth, elevation)
                right = _norm(_cross((0.0, 0.0, 1.0), V))
                self.mu, self.mv, self.V = right, _cross(V, right), V
        elif kind == "perspective":
            if eye is None or target is None:
                raise LayoutError("a perspective camera needs an eye and a target point")
            self.E = tuple(float(c) for c in eye)
            T = tuple(float(c) for c in target)
            f = _norm(_sub(T, self.E))
            if abs(f[2]) > 0.995:
                raise LayoutError("a perspective camera cannot look straight up or down")
            self.f = f
            self.r = _norm(_cross(f, (0.0, 0.0, 1.0)))
            self.up = _cross(self.r, f)
            self.lens = float(lens)
            self.near = float(near)
            self.hw = 18.0 / self.lens
            self.hh = self.hw / aspect
            self.shift = float(shift)
        else:
            raise LayoutError(f"camera type {kind!r} must be 'axon' or 'perspective'")

    def hides(self, ident: str) -> bool:
        """True when the camera hides this element, or the wall an opening part belongs to."""
        return ident in self.hide or ident.split(".")[0] in self.hide

    @classmethod
    def from_spec(cls, spec, project=None, aspect=1.5):
        def pt(key):
            raw = spec.get(key)
            if raw is None:
                return None
            if len(raw) != 3:
                raise LayoutError(f"camera {spec.get('id')}: {key} must be [x, y, z]")
            return tuple(float(_resolve(project, c)) for c in raw)
        cz = spec.get("cut_z")
        sun = spec.get("sun")
        return cls(kind=spec.get("type", "axon"), projection=spec.get("projection", "iso"),
                   azimuth=float(spec.get("azimuth", 225.0)),
                   elevation=float(spec["elevation"]) if "elevation" in spec else None,
                   rotate=float(spec.get("rotate", 30.0)), vscale=float(spec.get("vscale", 1.0)),
                   eye=pt("eye"), target=pt("target"), lens=float(spec.get("lens", 24.0)), aspect=aspect,
                   near=float(spec.get("near", NEAR)),
                   cut_z=float(_resolve(project, cz)) if cz is not None else None,
                   hide=spec.get("hide", ()),
                   sun=(float(sun["azimuth"]), float(sun["altitude"])) if sun else None,
                   shift=float(spec.get("shift", 0.0)), light=spec.get("light"), fit=spec.get("fit", ()))

    @property
    def parallel(self) -> bool:
        return self.kind == "axon"

    def side(self, n, d) -> float:
        """How far the viewer is on the front side of plane n.p = d (positive = in front)."""
        if self.parallel:
            return _dot(n, self.V)
        return _dot(n, self.E) - d

    def toward_viewer(self, p):
        if self.parallel:
            return self.V
        return _norm(_sub(self.E, p))

    def project(self, p):
        """Screen point (u, v) of a world point."""
        if self.parallel:
            return (_dot(self.mu, p), _dot(self.mv, p))
        q = _sub(p, self.E)
        zc = _dot(q, self.f)
        if zc <= 1e-9:
            raise LayoutError(f"the 3D point ({p[0]:g}, {p[1]:g}, {p[2]:g}) is behind the camera; "
                              "point the callout or dimension at something in front of it")
        return (_dot(q, self.r) / zc, _dot(q, self.up) / zc - self.shift * self.hh)

    def depth(self, p) -> float:
        """Distance in front of the eye along the view axis (perspective only)."""
        return _dot(_sub(p, self.E), self.f)


# ------------------------------------------------------------------ polygon clipping and BSP


def _clip(pts, edges, n, d, keep_front=True, new_edge=None):
    """Clip a polygon (with per-edge classes) to the side n.p >= d (or <= d)."""
    sgn = 1.0 if keep_front else -1.0
    s = [sgn * (_dot(n, p) - d) for p in pts]
    if all(x >= -EPS for x in s):
        return pts, edges
    if all(x <= EPS for x in s):
        return None, None
    op, oe = [], []
    m = len(pts)
    for i in range(m):
        a, b, e = pts[i], pts[(i + 1) % m], edges[i]
        sa, sb = s[i], s[(i + 1) % m]
        a_in, b_in = sa >= -EPS, sb >= -EPS
        if a_in:
            op.append(a)
            if b_in:
                oe.append(e)
            elif sa <= EPS:
                oe.append(new_edge)
            else:
                op.append(_lerp(a, b, sa / (sa - sb)))
                oe.extend([e, new_edge])
        elif b_in and sb > EPS:
            op.append(_lerp(a, b, sa / (sa - sb)))
            oe.append(e)
    return _tidy(op, oe)


def _tidy(pts, edges):
    if len(pts) < 3:
        return None, None
    op, oe = [], []
    m = len(pts)
    for i in range(m):
        p = pts[i]
        if op and max(abs(p[k] - op[-1][k]) for k in range(len(p))) <= 1e-7:
            oe[-1] = edges[i]
            continue
        op.append(p)
        oe.append(edges[i])
    if len(op) > 2 and max(abs(op[0][k] - op[-1][k]) for k in range(len(op[0]))) <= 1e-7:
        op.pop()
        oe.pop()
    if len(op) < 3:
        return None, None
    return op, oe


class _Poly:
    __slots__ = ("pts", "edges", "face")

    def __init__(self, pts, edges, face):
        self.pts, self.edges, self.face = pts, edges, face


class _Node:
    __slots__ = ("n", "d", "on", "front", "back")

    def __init__(self):
        self.n = self.d = None
        self.on, self.front, self.back = [], None, None


def _classify(poly, n, d):
    front = back = False
    for p in poly.pts:
        s = _dot(n, p) - d
        if s > EPS:
            front = True
        elif s < -EPS:
            back = True
    return (2 if front and back else 1 if front else -1 if back else 0)


def _split(poly, n, d):
    fp, fe = _clip(poly.pts, poly.edges, n, d, True)
    bp, be = _clip(poly.pts, poly.edges, n, d, False)
    return (_Poly(fp, fe, poly.face) if fp else None), (_Poly(bp, be, poly.face) if bp else None)


def bsp_order(polys, cam, candidates=6):
    """Polygons in back-to-front order for the camera, split where they cross."""
    if not polys:
        return []
    root = _Node()
    work = [(root, polys)]
    while work:
        node, items = work.pop()
        best, best_cost = 0, None
        for ci in range(min(candidates, len(items))):
            f = items[ci].face
            splits = fr = bk = 0
            for q in items:
                c = _classify(q, f.n, f.d)
                if c == 2:
                    splits += 1
                elif c == 1:
                    fr += 1
                elif c == -1:
                    bk += 1
            cost = splits * 8 + abs(fr - bk)
            if best_cost is None or cost < best_cost:
                best, best_cost = ci, cost
        f = items[best].face
        node.n, node.d = f.n, f.d
        fl, bl = [], []
        for q in items:
            c = _classify(q, f.n, f.d)
            if c == 0:
                node.on.append(q)
            elif c == 1:
                fl.append(q)
            elif c == -1:
                bl.append(q)
            else:
                a, b = _split(q, f.n, f.d)
                if a:
                    fl.append(a)
                if b:
                    bl.append(b)
        if fl:
            node.front = _Node()
            work.append((node.front, fl))
        if bl:
            node.back = _Node()
            work.append((node.back, bl))
    out = []
    stack = [(root, False)]
    while stack:
        node, expanded = stack.pop()
        if node is None:
            continue
        if expanded:
            out.extend(node.on)
            continue
        if cam.side(node.n, node.d) > 0:
            near, far = node.front, node.back
        else:
            near, far = node.back, node.front
        stack.append((near, False))
        stack.append((node, True))
        stack.append((far, False))
    return out


def _drop_contact(faces):
    """Faces where two solids touch: a face lying wholly on a face of the opposite
    normal in the same plane (a wall end butted into another wall, a cabinet back on a
    wall, a box bottom on a counter). Buried faces can't be seen, and their outlines
    would bleed through the joint, so they are dropped."""
    by = {}
    for f in faces:
        by.setdefault(_pkey(f), []).append(f)
    out = []
    for f in faces:
        opp = by.get((tuple(round(-c, 3) + 0.0 for c in f.n), round(-f.d, 2) + 0.0))
        if opp and not f.two and all(any(_in_face(g, q) for g in opp) for q in _probes(f)):
            continue
        out.append(f)
    return out


def _probes(f, n=9):
    """Points spread over the inside of face f: its centroid, points toward each corner and
    an n x n grid, so a face is called covered only when the union of faces covers it."""
    m = len(f.pts)
    c = _mul(functools.reduce(_add, f.pts), 1 / m)
    out = [c] + [_add(c, _mul(_sub(q, c), 0.95)) for q in f.pts]
    ax = max(range(3), key=lambda i: abs(f.n[i]))
    i, j = [k for k in range(3) if k != ax]
    lo = [min(q[k] for q in f.pts) for k in (i, j)]
    hi = [max(q[k] for q in f.pts) for k in (i, j)]
    for a in range(n):
        for b in range(n):
            u = lo[0] + (hi[0] - lo[0]) * (a + 0.5) / n
            w = lo[1] + (hi[1] - lo[1]) * (b + 0.5) / n
            q = [0.0, 0.0, 0.0]
            q[i], q[j] = u, w
            q[ax] = (f.d - f.n[i] * u - f.n[j] * w) / f.n[ax]
            q = tuple(q)
            if _in_face(f, q):
                out.append(q)
    return out


def _base_id(ident: str) -> str:
    return ident.split(".")[0]


def _pkey(f):
    return (tuple(round(c, 3) + 0.0 for c in f.n), round(f.d, 2) + 0.0)


def _butt(work, same_plane, wi, a, b, tol=0.02) -> bool:
    """True when edge a-b of face work[wi] lies along an edge of another face in the same
    plane and material: a butt joint (a wall end flush with the face of the wall it meets),
    which reads as one surface and draws no line."""
    f = work[wi][0]
    ab = _sub(b, a)
    lab = math.sqrt(_dot(ab, ab))
    if lab < tol:
        return False
    u = _mul(ab, 1 / lab)
    spans = []
    for wj in same_plane:
        g, gp = work[wj][0], work[wj][1]
        if wj == wi or g.mat != f.mat:
            continue
        for k in range(len(gp)):
            c, d = gp[k], gp[(k + 1) % len(gp)]
            off = [_sub(q, a) for q in (c, d)]
            if any(math.sqrt(max(0.0, _dot(o, o) - _dot(o, u) ** 2)) > tol for o in off):
                continue
            t0, t1 = sorted(_dot(o, u) for o in off)
            if t1 > tol and t0 < lab - tol:
                spans.append((max(t0, 0.0), min(t1, lab)))
    reach = 0.0
    for t0, t1 in sorted(spans):
        if t0 > reach + tol:
            return False
        reach = max(reach, t1)
    return reach >= lab - tol


def _ekey(a, b):
    ka = tuple(round(c, 3) for c in a)
    kb = tuple(round(c, 3) for c in b)
    return (ka, kb) if ka <= kb else (kb, ka)


def _inside2(pts, p) -> bool:
    inside = False
    n = len(pts)
    for i in range(n):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
        if (y1 > p[1]) != (y2 > p[1]):
            if p[0] < x1 + (p[1] - y1) * (x2 - x1) / (y2 - y1):
                inside = not inside
    return inside


def _area2(pts) -> float:
    return abs(sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1]
                   for i in range(len(pts)))) / 2


def _clip2(pts, edges, box):
    """Clip a screen polygon to an axis box (u0, v0, u1, v1). New edges are None."""
    u0, v0, u1, v1 = box
    for n, d in (((1.0, 0.0, 0.0), u0), ((-1.0, 0.0, 0.0), -u1), ((0.0, 1.0, 0.0), v0), ((0.0, -1.0, 0.0), -v1)):
        p3 = [(p[0], p[1], 0.0) for p in pts]
        p3, edges = _clip(p3, edges, n, d, True)
        if not p3:
            return None, None
        pts = [(p[0], p[1]) for p in p3]
    return pts, edges


# ------------------------------------------------------------------ rule and value text

_OP_WORD = {">=": "MIN.", "<=": "MAX.", "==": "EXACTLY"}
_OPS = {">=": lambda a, b, t: a >= b - t, "<=": lambda a, b, t: a <= b + t, "==": lambda a, b, t: abs(a - b) <= t}


def limit_text(project, rule) -> str:
    """The printed limit of a rule, without its MIN./MAX. word, in the house style
    of tables.limit_number: 24 in -> 2'-0", 6 in -> 6", 0.30 U-FACTOR."""
    from .tables import limit_number
    try:
        return limit_number(rule["check"], project.denom)
    except PrintRefused as exc:
        raise PrintRefused(f"rule {rule['id']}: {exc}") from None


def rule_note(project, rule_id, template) -> Txt:
    """A note built from a project.json rule. Fields: {rule.limit}, {rule.op} (MIN., MAX.,
    EXACTLY), {rule.citation}, {rule.element} and {rule.value} (the drawn value, with its
    FV tags), plus any {value_key} or {value_key:code} as in kit.text(). The rule's cd is
    recorded for QA."""
    r = rule_entry(project, rule_id)
    chk = r["check"]
    parts = {"rule.limit": limit_text(project, r), "rule.op": _OP_WORD[chk["op"]],
             "rule.citation": r.get("citation") or "", "rule.element": r["element"].upper()}
    t = str(template)
    if "{rule.citation}" in t and not parts["rule.citation"]:
        raise PrintRefused(f"rule {rule_id} has no citation to print")
    for k, s in parts.items():
        t = t.replace("{" + k + "}", s.replace("{", "{{").replace("}", "}}"))
    if "{rule.value}" in t:
        if "value" not in chk:
            raise PrintRefused(f"rule {rule_id} limits a spread of values; it has no one {{rule.value}} to print")
        key = project.lookup(chk["value"]).key
        t = t.replace("{rule.value}", "{" + key + "}")
    return fill(project, t, cd=r.get("cd") or ())


# ------------------------------------------------------------------ the view


class View3D:
    """A 3D view on a sheet: renders a Scene through a camera into an N.T.S. view cell.

    sheet    the Sheet (kit.sheet(...))
    scene    a Scene
    camera   a camera id from model3d.cameras, or a Camera
    title    the view title
    cell     (x, y, w, h) inches from the drawing-area lower-left, as for sheet.view
    margins  (left, bottom, right, top) room around the picture for callouts, as a
             share of the picture size
    """

    def __init__(self, sheet, scene, camera, title, cell=None, number=None, margins=(0.25, 0.03, 0.25, 0.03),
                 subtitle="", frame=None):
        from .sheet import TITLE_STRIP
        self.sheet, self.scene, self.project = sheet, scene, scene.project
        self.margins = margins
        if cell is not None:
            avail_w = cell[2] * 72 - 12
            avail_h = cell[3] * 72 - TITLE_STRIP - 12
            ml, mb, mr, mt = margins
            aspect = (avail_w / (1 + ml + mr)) / (avail_h / (1 + mb + mt))
        else:
            aspect = 1.5
        if isinstance(camera, str):
            self.camera_id = camera
            cam = scene.camera(camera, aspect)
        else:
            self.camera_id = None
            cam = camera
        self.cam = cam
        sun = cam.sun or scene.sun
        self.L = _dir(*sun)
        self.frags = self._render()
        if cam.parallel:
            if not self.frags:
                raise LayoutError(f"{sheet.id}: 3D view {title!r} shows nothing")
            focus = [fr for fr in self.frags if cam.fit and _base_id(fr[1].elem.id) in cam.fit] \
                or self.frags
            if cam.fit and focus is self.frags:
                raise LayoutError(f"{sheet.id}: 3D view {title!r}: no element of fit {list(cam.fit)} is visible")
            us = [p[0] for fr in focus for p in fr[0]]
            vs = [p[1] for fr in focus for p in fr[0]]
            box = (min(us), min(vs), max(us), max(vs))
            if cam.fit:
                pad = FIT_PAD * max(box[2] - box[0], box[3] - box[1])
                box = (box[0] - pad, box[1] - pad, box[2] + pad, box[3] + pad)
            self.frame = frame or box
            self.framed = bool(cam.fit or frame)
            if self.framed:
                kept = []
                for p2, face, ed, pts3 in self.frags:
                    p2, ed = _clip2(p2, ed, self.frame)
                    if p2 and _area2(p2) > 1e-12:
                        kept.append((p2, face, ed, pts3))
                self.frags = kept
        else:
            self.frame = (-cam.hw, -cam.hh, cam.hw, cam.hh)
            self.framed = True
        fx0, fy0, fx1, fy1 = self.frame
        W, H = fx1 - fx0, fy1 - fy0
        ml, mb, mr, mt = margins
        extents = (fx0 - ml * W, fy0 - mb * H, fx1 + mr * W, fy1 + mt * H)
        self.view = sheet.view(title, "NTS", extents, cell=cell, number=number, scale_bar=False,
                               subtitle=subtitle)
        self.id = self.view.id
        self._n_callouts = 0
        self._draw()

    # ---- rendering

    def _render(self):
        cam, sc = self.cam, self.scene
        faces = _drop_contact([f for el in sc.elements if not cam.hides(el.id) for f in el.faces])
        work = [(f, list(f.pts), list(f.edges)) for f in faces]
        if cam.cut_z is not None:
            work = self._cut(work, cam.cut_z)
        facing = {}
        for f, _, _ in work:
            facing[id(f)] = f.two or cam.side(f.n, f.d) > EPS
        # classify each 'auto' edge against the faces that share it
        emap = {}
        for wi, (f, pts, edges) in enumerate(work):
            m = len(pts)
            for i in range(m):
                emap.setdefault(_ekey(pts[i], pts[(i + 1) % m]), []).append(wi)
        planes = {}
        for wi, (f, pts, edges) in enumerate(work):
            if facing[id(f)]:
                planes.setdefault(_pkey(f), []).append(wi)
        polys = []
        for wi, (f, pts, edges) in enumerate(work):
            if not facing[id(f)]:
                continue
            m = len(pts)
            cls = []
            for i in range(m):
                e = edges[i]
                if e == "auto":
                    sharers = emap[_ekey(pts[i], pts[(i + 1) % m])]
                    e = self._edge_class(work, facing, wi, sharers)
                    if e == "sil" and _butt(work, planes.get(_pkey(f), ()), wi, pts[i], pts[(i + 1) % m]):
                        e = None
                cls.append(e)
            p, ed = pts, cls
            if not cam.parallel:
                p, ed = _clip(p, ed, cam.f, _dot(cam.f, cam.E) + cam.near, True)
                if not p:
                    continue
            polys.append(_Poly(p, ed, f))
        ordered = bsp_order(polys, cam)
        frags = []
        box = None if cam.parallel else (-cam.hw, -cam.hh, cam.hw, cam.hh)
        for q in ordered:
            p2 = [cam.project(p) for p in q.pts]
            ed = q.edges
            if box is not None:
                p2, ed = _clip2(p2, ed, box)
                if not p2:
                    continue
            if _area2(p2) < 1e-12:
                continue
            frags.append((p2, q.face, ed, q.pts))
        return frags

    @staticmethod
    def _edge_class(work, facing, wi, sharers):
        f = work[wi][0]
        others = [work[j][0] for j in sharers if j != wi]
        if not others:
            return "sil"
        seen = [g for g in others if facing[id(g)]]
        for g in seen:
            if _dot(g.n, f.n) > 0.9995 and abs(g.d - f.d) < 0.01:
                return None
        return "crease" if seen else "sil"

    def _cut(self, work, cz):
        """A horizontal section at z = cz: drop what is above, cap the solids it cuts."""
        out = []
        n = (0.0, 0.0, -1.0)
        for f, pts, edges in work:
            p, e = _clip(pts, edges, n, -cz, True, new_edge="sil")
            if p:
                out.append((f, p, e))
        for el in self.scene.elements:
            if self.cam.hides(el.id):
                continue
            for plan, zlo, zhi, mat in el.prisms:
                if zlo < cz - EPS and zhi > cz + EPS:
                    cap = Face([(x, y, cz) for x, y in plan], el, self.scene.color("cut"),
                               ["sil"] * len(plan), kind="cut", hint=(0, 0, 1))
                    out.append((cap, list(cap.pts), list(cap.edges)))
        return out

    def _color(self, face, pts3):
        n = face.n
        # shade against the view axis, not the ray to each fragment, so every face in one
        # plane (a wall split around its openings, a face split by the painter's
        # ordering) prints as one even tone with no seams
        vd = self.cam.V if self.cam.parallel else _mul(self.cam.f, -1.0)
        if face.two and self.cam.side(face.n, face.d) < 0:
            n = _mul(n, -1.0)
        if face.kind == "cut":
            k = 1.0
        elif self.cam.light == "interior":
            # side walls seen edge-on keep most of their tone: abs, not max
            k = 0.80 + 0.13 * abs(_dot(n, vd)) + 0.06 * abs(n[2]) + 0.04 * max(0.0, _dot(n, self.L))
        else:
            k = 0.60 + 0.30 * max(0.0, _dot(n, self.L)) + 0.12 * max(0.0, _dot(n, vd))
        col = tuple(min(1.0, ch * k) for ch in face.base)
        if face.elem.unverified:
            col = tuple(ch * 0.45 + 0.55 for ch in col)
        return col

    def _draw(self):
        v = self.view
        if self.framed and not self.cam.parallel:
            fx0, fy0, fx1, fy1 = self.frame
            v.polygon([(fx0, fy0), (fx1, fy0), (fx1, fy1), (fx0, fy1)], stroke=None, fill="#f3f5f6",
                      layer="back")
        for p2, face, edges, pts3 in self.frags:
            col = self._color(face, pts3)
            v.polygon(p2, stroke=col, fill=col, width=0.3, layer="geom")
            el = face.elem
            ink = EDGE_INK if not el.unverified else GREY
            dash = DASH.get(el.status) if el.unverified and face.kind != "detail" else None
            by = {}
            m = len(p2)
            for i in range(m):
                e = edges[i]
                if e in EDGE_W:
                    by.setdefault(e, []).append((p2[i], p2[(i + 1) % m]))
            for cls in ("fine", "crease", "sil"):
                segs = []
                for a, b in by.get(cls, ()):
                    segs += [("M", a[0], a[1]), ("L", b[0], b[1])]
                if segs:
                    v.path(segs, stroke=ink, width=EDGE_W[cls] * (0.85 if el.unverified else 1.0),
                           dash=dash, layer="geom")
        if self.framed:
            fx0, fy0, fx1, fy1 = self.frame
            v.polygon([(fx0, fy0), (fx1, fy0), (fx1, fy1), (fx0, fy1)], stroke=INK, width=0.8, layer="geom")
        self._fv_tags()

    # ---- geometry queries

    def P3(self, p):
        """Paper point of a world point."""
        return self.view.P(*self.cam.project(p))

    def occluded(self, p, tol=0.75) -> bool:
        """True when a face of the scene hides world point p from the camera."""
        cam = self.cam
        if cam.parallel:
            d = cam.V
            tmax = float("inf")
        else:
            seg = _sub(cam.E, p)
            tmax = math.sqrt(_dot(seg, seg))
            d = _mul(seg, 1 / tmax)
            if cam.depth(p) < cam.near:
                return True
        for el in self.scene.elements:
            if cam.hides(el.id):
                continue
            for f in el.faces:
                if f.kind == "glass":
                    continue
                den = _dot(f.n, d)
                if abs(den) < 1e-9:
                    continue
                t = (f.d - _dot(f.n, p)) / den
                if t <= tol or t >= tmax - tol:
                    continue
                if cam.cut_z is not None and p[2] + d[2] * t > cam.cut_z:
                    continue
                q = _add(p, _mul(d, t))
                if not cam.parallel and cam.depth(q) < cam.near:
                    continue
                if _in_face(f, q):
                    return True
        return False

    def _visible_point(self, el):
        """A paper point on the visible part of an element, or None."""
        own = [(i, fr) for i, fr in enumerate(self.frags) if fr[1].elem is el]
        own.sort(key=lambda t: -_area2(t[1][0]))
        for i, fr in own[:12]:
            p2 = fr[0]
            c = (sum(p[0] for p in p2) / len(p2), sum(p[1] for p in p2) / len(p2))
            if not _inside2(p2, c):
                continue
            if any(_inside2(later[0], c) for later in self.frags[i + 1:] if later[1].elem is not el):
                continue
            return self.view.P(*c)
        return None

    def _fv_tags(self):
        """Each FV tag of the unverified parts that show, once per view, on the part with the
        largest visible area that carries it. The lighter, dashed style marks every part."""
        page = self.view.page
        cell = self.view.cell
        area = {}
        for p2, face, _, _ in self.frags:
            if face.elem.unverified:
                area[face.elem.id] = area.get(face.elem.id, 0.0) + _area2(p2)
        placed = set()
        order = sorted((el for el in self.scene.elements if el.id in area and el.fv),
                       key=lambda el: (-area[el.id], el.id))
        for el in order:
            todo = [t for t in el.fv if t not in placed]
            if not todo:
                continue
            at = self._visible_point(el)
            if at is None:
                continue
            for k, tag in enumerate(todo):
                placed.add(tag)
                if tag not in self.project.fv:
                    raise PrintRefused(f"3D element {el.id}: {tag} is not in project.json field_verify")
                size = 7.0
                w = tm.text_width(tag, size, True) + 6
                h = size + 4
                spot = None
                for dx, dy in ((0, 0), (0, 14), (0, -14), (22, 0), (-22, 0), (0, 28), (0, -28), (30, 14), (-30, -14)):
                    x, y = at[0] + dx + k * (w + 3), at[1] + dy
                    box = (x - w / 2, y - h / 2, x + w / 2, y + h / 2)
                    if page.free(box) and box[0] > cell[0] and box[2] < cell[2]:
                        spot = (x, y, box)
                        break
                if spot is None:
                    x, y = at[0] + k * (w + 3), at[1]
                    spot = (x, y, (x - w / 2, y - h / 2, x + w / 2, y + h / 2))
                x, y, box = spot
                self.view.paper_path(rect_segments(*box), stroke="#8c2f2f", fill=WHITE, width=0.8, layer="annot")
                self.view.paper_text(x, y - tm.ASCENT * size / 2, tag, size=size, bold=True, anchor="middle",
                                     color="#8c2f2f", role="fv", fv=[tag])

    # ---- callouts

    def rule_text(self, rule_id, template) -> Txt:
        """rule_note() for this view's project."""
        return rule_note(self.project, rule_id, template)

    def text(self, template, depends_on=(), cd=()) -> Txt:
        return fill(self.project, template, False, depends_on, cd)

    def _lines(self, text, width, size, bold):
        given = list(text) if isinstance(text, (list, tuple)) else [text]
        lines = []
        for ln in given:
            if not isinstance(ln, Txt) and any(ch.isdigit() for ch in str(ln)):
                raise PrintRefused(f"callout text {ln!r} has a number that is not from project.json; "
                                   "build it with kit.text(), rule_note() or view.rule_text()")
            parts = tm.wrap(tm.clean(str(ln)), width, size, bold) if width else [str(ln)]
            for i, part in enumerate(parts):
                if i == 0:
                    lines.append(Txt(part, keys=getattr(ln, "keys", ()), fv=getattr(ln, "fv", ()),
                                     cd=getattr(ln, "cd", ())))
                else:
                    lines.append(Txt(part))
        return lines

    def callout(self, at, text, side=None, dy=0.0, size=7.2, bold=True, allow_hidden=False, width=150.0):
        """A leader from world point `at` to a note in the margin beside the picture.

        text  a Txt or a list of Txt lines from kit.text(), rule_note() or view.rule_text();
              a plain string only for words with no number.
        side  'left' or 'right' (default: the nearer side).
        width wrap each note to this many points (None: no wrap).
        For several callouts use callouts(): it orders them so leaders do not cross.
        """
        return self.callouts([{"at": at, "text": text, "side": side, "dy": dy, "allow_hidden": allow_hidden}],
                             size=size, bold=bold, width=width)[0]

    def callouts(self, items, size=7.2, bold=True, width=150.0, gap=7.0):
        """Several callouts at once. items: dicts {at, text, side?, dy?, allow_hidden?} or
        (at, text[, side]) tuples. Notes on each side stack in the order of their targets,
        top to bottom, so their leaders do not cross. Returns the text records of each."""
        from .annot import leader
        v = self.view
        cell = v.cell
        fx0, fy0, fx1, fy1 = self.frame
        left_pt, right_pt = v.P(fx0, fy0)[0], v.P(fx1, fy1)[0]
        lh = size * 1.25
        prepared = []
        for k, it in enumerate(items):
            if not isinstance(it, dict):
                it = dict(zip(("at", "text", "side"), it))
            lines = self._lines(it["text"], width, size, bold)
            at = it["at"]
            if not it.get("allow_hidden") and self.occluded(at):
                self.sheet.layout_issues.append(f"{v.id}: callout {str(lines[0])!r} points at a part of the "
                                                "model the camera cannot see; move the point or the camera")
            tx, ty = self.P3(at)
            u, w = self.cam.project(at)
            eps = 1e-9 * max(fx1 - fx0, fy1 - fy0)
            if not (fx0 - eps <= u <= fx1 + eps and fy0 - eps <= w <= fy1 + eps):
                # never drop a callout: a code note that silently vanishes is worse than a stop
                raise LayoutError(f"{self.sheet.id} {v.id}: callout {str(lines[0])!r} points outside the "
                                  "picture; pick a point the camera shows, or move the camera")
            side = it.get("side") or ("left" if tx < (left_pt + right_pt) / 2 else "right")
            if side not in ("left", "right"):
                raise LayoutError(f"callout side must be 'left' or 'right', not {side!r}")
            prepared.append({"k": k, "lines": lines, "tx": tx, "ty": ty, "side": side,
                             "want": ty + float(it.get("dy", 0.0)), "h": lh * len(lines)})
        out = [None] * len(items)
        for side in ("left", "right"):
            group = sorted((q for q in prepared if q["side"] == side), key=lambda q: (-q["want"], q["k"]))
            if not group:
                continue
            x_text = left_pt - 10.0 if side == "left" else right_pt + 10.0
            anchor = "end" if side == "left" else "start"
            top_lim, bot_lim = cell[3] - 4 - size * 0.75, cell[1] + 4
            prev_bottom = None
            for q in group:                         # top-down: no block above the one before it
                ey = max(min(q["want"], top_lim), bot_lim + q["h"])
                if prev_bottom is not None:
                    ey = min(ey, prev_bottom - gap - size * 0.75)
                for _ in range(400):
                    if all(v.page.free(b) for b in self._boxes(q, x_text, ey, size, bold, anchor, lh)):
                        break
                    ey -= 2.0
                q["ey"] = ey
                prev_bottom = ey - q["h"] + lh - size * 0.35
            low = group[-1]
            over = bot_lim - (low["ey"] - low["h"] + lh - size * 0.35)
            if over > 0:                             # bottom-up: lift the stack back into the cell
                for q in group:
                    q["ey"] += over
            for q in group:
                for b in self._boxes(q, x_text, q["ey"], size, bold, anchor, lh):
                    if b[0] < cell[0] - 0.5 or b[2] > cell[2] + 0.5 or b[3] > cell[3] + 0.5:
                        raise LayoutError(f"{self.sheet.id} {v.id}: callout {str(q['lines'][0])!r} does not "
                                          "fit beside the picture; widen the view margins, shorten the note "
                                          "or use fewer callouts on that side")
                shoulder = 8.0
                tx, ty = q["tx"], q["ty"]
                dx = (x_text - 2 - shoulder - tx) if side == "right" else (x_text + 2 + shoulder - tx)
                target = (v.x0 + (tx - v.ox) / v.s, v.y0 + (ty - v.oy) / v.s)
                recs = leader(v, target, q["lines"], dx=dx, dy=q["ey"] - ty, size=size, bold=bold,
                              arrow="arrow", role="callout")
                self._n_callouts += 1
                for r in recs:
                    r["meta"]["group"] = f"{v.id}:callout{self._n_callouts}"
                out[q["k"]] = recs
        return out

    @staticmethod
    def _boxes(q, x_text, ey, size, bold, anchor, lh):
        return [text_box(x_text, ey - size * 0.35 - i * lh, tm.clean(str(ln)), size, bold, 0.0, anchor)
                for i, ln in enumerate(q["lines"])]

    def dim(self, a, b, value, rule=None, offset=(0.0, 0.0, 0.0), size=7.0, label="both", tol=None):
        """A dimension between two world points, printed from a Value.

        The distance between a and b must equal `value` (within the drawing precision),
        so the picture and the number cannot disagree. With `rule`, the label adds the
        rule's limit ('2'-6" (MAX. 2'-0")', or only 'MAX. 2'-0"' with label='rule'), and a
        verified value that breaks the rule is refused. offset moves the dimension line
        off the geometry (world inches); extension lines join it back."""
        if not isinstance(value, Value):
            raise TypeError("a 3D dimension prints a project Value (kit.value(key)); "
                            f"got {value!r}")
        a = tuple(float(c) for c in a)
        b = tuple(float(c) for c in b)
        dist = math.sqrt(_dot(_sub(b, a), _sub(b, a)))
        tol = tol if tol is not None else 1.0 / self.project.denom
        if value.unit != "in":
            raise PrintRefused(f"{value.key} is in {value.unit}; a dimension prints a length")
        if abs(dist - float(value)) > tol + 1e-9:
            raise LayoutError(f"{self.sheet.id} {self.id}: the drawn distance {dist:.3f} in. does not equal "
                              f"{value.key} = {float(value):g} in.; the 3D points and the value disagree")
        tags = tags_for(self.project, value)
        vtext = value_text(self.project, value)
        if tags:
            vtext += " " + fv_text(tags)
        keys, cd = [value.key], ()
        text = vtext
        if rule is not None:
            r = rule_entry(self.project, rule)
            chk = r["check"]
            if "value" not in chk:
                raise PrintRefused(f"rule {rule} limits a spread of values, not one dimension")
            lim = f"{_OP_WORD[chk['op']]} {limit_text(self.project, r)}"
            try:
                drawn = convert(float(value), "in", chk["unit"])
            except UnitError as exc:
                raise PrintRefused(f"rule {rule}: {exc}") from None
            ok = _OPS[chk["op"]](drawn, float(chk["limit"]), max(abs(float(chk["limit"])), 1.0) * 1e-6)
            if not ok and not value.unverified:
                raise PrintRefused(f"{value.key} = {float(value):g} in. breaks rule {rule} "
                                   f"({chk['op']} {chk['limit']} {chk['unit']}); fix the design, do not label it")
            cd = r.get("cd") or ()
            text = lim if label == "rule" and not tags else f"{vtext} ({lim})"
        txt = Txt(text, keys=keys, fv=tags, cd=cd)
        o = tuple(float(c) for c in offset)
        a2, b2 = _add(a, o), _add(b, o)
        v = self.view
        pa, pb = self.P3(a2), self.P3(b2)
        kw = {"stroke": INK2, "width": 0.6, "layer": "annot"}
        if any(abs(c) > 1e-9 for c in o):
            for p, q in ((a, a2), (b, b2)):
                p1, q1 = self.P3(p), self.P3(q)
                L = math.hypot(q1[0] - p1[0], q1[1] - p1[1]) or 1.0
                ux, uy = (q1[0] - p1[0]) / L, (q1[1] - p1[1]) / L
                v.paper_path([("M", p1[0] + ux * 2.5, p1[1] + uy * 2.5), ("L", q1[0] + ux * 3, q1[1] + uy * 3)],
                             stroke=INK2, width=0.4, layer="annot")
        v.paper_path([("M", pa[0], pa[1]), ("L", pb[0], pb[1])], **kw)
        ang = math.atan2(pb[1] - pa[1], pb[0] - pa[0])
        for p, s in ((pa, 1), (pb, -1)):
            c, sn = math.cos(ang) * s, math.sin(ang) * s
            tip = p
            l, w = 6.0, 2.0
            back = (tip[0] + c * l, tip[1] + sn * l)
            v.paper_path(poly_segments([tip, (back[0] - sn * w, back[1] + c * w), (back[0] + sn * w, back[1] - c * w)],
                                       closed=True), stroke=None, fill=INK2, layer="annot")
        rot = math.degrees(ang)
        if rot > 90:
            rot -= 180
        elif rot <= -90:
            rot += 180
        mx, my = (pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2
        s = tm.clean(str(txt))
        w = tm.text_width(s, size, True)
        r = math.radians(rot)
        spot = None
        for k in (0, 1, -1, 2, -2, 3, -3):
            cx, cy = mx + math.cos(r) * k * 10, my + math.sin(r) * k * 10
            bx = cx - math.cos(r) * w / 2 + math.sin(r) * size * 0.35
            by = cy - math.sin(r) * w / 2 - math.cos(r) * size * 0.35
            if self.view.page.free(text_box(bx, by, s, size, True, rot)):
                spot = (bx, by, cx, cy)
                break
        collided = spot is None
        if spot is None:
            cx, cy = mx, my
            spot = (cx - math.cos(r) * w / 2 + math.sin(r) * size * 0.35,
                    cy - math.sin(r) * w / 2 - math.cos(r) * size * 0.35, cx, cy)
        bx, by, cx, cy = spot
        hw, hh = w / 2 + 3, size * 0.75
        ca, sa = math.cos(r), math.sin(r)
        corners = [(cx + px * ca - py * sa, cy + px * sa + py * ca) for px, py in ((-hw, -hh), (hw, -hh), (hw, hh), (-hw, hh))]
        v.paper_path(poly_segments(corners, closed=True), stroke=None, fill=WHITE, layer="annot")
        color = "#8c2f2f" if tags else INK
        rec = v.paper_text(bx, by, txt, size=size, bold=True, rot=rot, color=color, role="dim3d")
        if collided:
            v.page.collisions.append({"text": rec["s"], "bbox": rec["bbox"], "role": rec["role"]})
        return rec

    # ---- legends

    def materials_used(self, min_share=0.004):
        """Materials of the faces this view shows, largest visible area first. A material
        covering less than min_share of the picture is left out."""
        area = {}
        for p2, face, _, _ in self.frags:
            if face.kind in ("detail", "cut"):
                continue
            nm = face.mat
            area[nm] = area.get(nm, 0.0) + _area2(p2)
        total = sum(area.values()) or 1.0
        return [nm for nm, a in sorted(area.items(), key=lambda t: (-t[1], t[0])) if a / total >= min_share]


def _in_face(f, q, tol=0.05) -> bool:
    """True when q (on f's plane) lies inside convex-or-simple face f."""
    n = f.n
    ax = max(range(3), key=lambda i: abs(n[i]))
    i, j = [k for k in range(3) if k != ax]
    pts = [(p[i], p[j]) for p in f.pts]
    return _inside2(pts, (q[i], q[j]))


def material_legend(panel, scene, names, size: float = 7.5, swatch: float = 0.45):
    """Colour swatches with each material's label, in a sheet Panel.

    names: material names, for example view.materials_used(). Labels come from
    model3d.materials[name].label (a finish specification you write), or the default."""
    sw = swatch * 72
    rh = max(size * 1.9, 15.0)
    for nm in names:
        col, label = scene.materials[nm][0], scene.materials[nm][1]
        panel._need(rh)
        x, ymid = panel.x0, panel.y - rh / 2
        panel._p(rect_segments(x, ymid - 5, x + sw, ymid + 5), stroke=INK, width=0.6, fill=col)
        panel._t(x + sw + 10, ymid - size * 0.35, label, size=size, role="legend")
        panel.y -= rh


def status_legend(panel, size: float = 7.5, swatch: float = 0.45):
    """Two legend rows: verified parts, and parts that rest on unverified values."""
    sw = swatch * 72
    rh = max(size * 1.9, 15.0)
    for kind, label in ((VERIFIED, "MEASURED, PROPOSED OR FROM A DATA SHEET"),
                        (ASSUMED, "NOT YET MEASURED: LIGHTER, GREY DASHED EDGES, FV TAG")):
        panel._need(rh)
        x, ymid = panel.x0, panel.y - rh / 2
        if kind == VERIFIED:
            panel._p(rect_segments(x, ymid - 5, x + sw, ymid + 5), stroke=EDGE_INK, width=1.0, fill="#d8cdb4")
        else:
            panel._p(rect_segments(x, ymid - 5, x + sw, ymid + 5), stroke=GREY, width=0.9, fill="#ece6d9",
                     dash=DASH[ASSUMED])
        panel._t(x + sw + 10, ymid - size * 0.35, label, size=size, role="legend")
        panel.y -= rh


# ------------------------------------------------------------------ validation (called by model.py)


_REQUIRED = {"box": ("x", "y", "z", "w", "d", "h"), "slab": ("x0", "y0", "x1", "y1", "z", "t"),
             "wall": ("x0", "y0", "x1", "y1", "t", "z", "h"),
             "roof": ("x0", "y0", "x1", "y1", "z", "pitch", "overhang"),
             "member": ("x0", "y0", "z0", "x1", "y1", "z1", "w", "d"), "device": ("x", "y", "z")}


def model3d_issues(project) -> list:
    """(severity, code, where, message) for the model3d block."""
    m = project.data.get("model3d")
    if not m:
        return []
    out = []
    names = set(MATERIALS) | set((m.get("materials") or {}).keys())
    seen = set()
    openings = {o["id"] for o in project.data.get("openings", [])}
    for e in m.get("elements", []):
        where = f"model3d.{e['id']}"
        if e["id"] in seen:
            out.append(("error", "model3d-duplicate", where, "element id appears more than once"))
        seen.add(e["id"])
        for f in _REQUIRED.get(e["kind"], ()):
            if f not in e:
                out.append(("error", "model3d-field", where, f"a {e['kind']} needs {f!r}"))
        for f in ("material", "inner", "wall_material", "fascia_material"):
            if e.get(f) and e[f] not in names:
                out.append(("error", "model3d-material", where,
                            f"material {e[f]!r} is not a default material or in model3d.materials"))
        for o in e.get("openings", []):
            if o.get("ref") and o["ref"] not in openings:
                out.append(("error", "model3d-opening", where, f"opening ref {o['ref']!r} is not in openings"))
            if not o.get("ref") and not o.get("id"):
                out.append(("error", "model3d-opening", where, "an opening needs a ref or an id"))
        a = e.get("assumed")
        if a and a.get("fv") and a["fv"] not in project.fv:
            out.append(("error", "unknown-fv", where, f"fv tag {a['fv']} is not in field_verify"))
    cams = set()
    for c in m.get("cameras", []):
        where = f"model3d.cameras.{c['id']}"
        if c["id"] in cams:
            out.append(("error", "model3d-duplicate", where, "camera id appears more than once"))
        cams.add(c["id"])
        if c.get("type") == "perspective" and (not c.get("eye") or not c.get("target")):
            out.append(("error", "model3d-camera", where, "a perspective camera needs eye and target"))
        for h in c.get("hide", []):
            if h not in seen:
                out.append(("warning", "model3d-camera", where, f"hide names no element {h!r}"))
        for h in c.get("fit", []):
            if h not in seen:
                out.append(("error", "model3d-camera", where, f"fit names no element {h!r}"))
        if c.get("fit") and c.get("type") == "perspective":
            out.append(("warning", "model3d-camera", where, "fit applies to axon cameras only"))
    return out
