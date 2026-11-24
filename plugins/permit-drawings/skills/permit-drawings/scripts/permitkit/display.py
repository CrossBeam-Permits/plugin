"""Backend-neutral display list.

A Page holds drawing operations in paper points. Paper axes: origin at the
lower-left corner of the sheet, x right, y up (the same as PDF, and the same
as a north-up plan).

A View maps real inches to paper points at one true scale. Geometry is given
in real inches. Annotation sizes (text, ticks, symbols) are given in points so
they read the same at every scale.

Draw order is fixed by layer, then by call order inside a layer:
  geometry -> annotation -> text -> frame -> frame text.
So a fill can never cover a label, whatever order a script calls things in.
Every text the kit emits is recorded with its bounding box. QA reads those
records; it never has to parse the PDF text.
"""
from __future__ import annotations

import math

from . import textmetrics as tm
from .units import Scale

LAYERS = {"back": 0, "geom": 1, "annot": 2, "text": 3, "frame": 4, "frame_text": 5}

INK = "#111111"
INK2 = "#444444"
GREY = "#8a8a8a"
LIGHT = "#b5b5b5"
DIM = "#8c2f2f"          # dimension and field-verify colour (dark red, prints well in grey)
POCHE_E = "#d6d6d6"      # existing construction
POCHE_N = "#7a7a7a"      # new construction
WHITE = "#ffffff"

#: How each status draws. ASSUMED and PLACEHOLDER read as unverified at a glance.
STATUS_STYLE = {
    "MEASURED": {"stroke": INK, "dash": None},
    "DERIVED": {"stroke": INK, "dash": None},
    "PROPOSED": {"stroke": INK, "dash": None},
    "MANUFACTURER": {"stroke": INK, "dash": None},
    "ASSUMED": {"stroke": GREY, "dash": (6.0, 3.0)},
    "PLACEHOLDER": {"stroke": GREY, "dash": (9.0, 3.0, 2.0, 3.0)},
}


#: Share of a text run's width that sits left of its anchor point.
ANCHOR_FRACTION = {"start": 0.0, "middle": 0.5, "end": 1.0}


class LayoutError(ValueError):
    """Something does not fit where it was placed."""


def rgb(color) -> tuple | None:
    if color is None:
        return None
    if isinstance(color, tuple):
        return color
    c = color.lstrip("#")
    if len(c) == 3:
        c = "".join(ch * 2 for ch in c)
    return tuple(int(c[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def text_box(x, y, s, size, bold=False, rot=0.0, anchor="start", tracking=0.0):
    """Axis-aligned bounding box (x0, y0, x1, y1) of a text run, in points."""
    w = tm.text_width(s, size, bold, tracking)
    fx = ANCHOR_FRACTION[anchor]
    return points_box(_rotated_corners(x, y, rot, -w * fx, w * (1 - fx),
                                       -tm.DESCENT * size, tm.ASCENT * size))


def _rotated_corners(x, y, rot, lx0, lx1, ly0, ly1) -> list:
    """Corners of the local box (lx0..lx1, ly0..ly1), turned by rot degrees about (x, y)."""
    a = math.radians(rot)
    ca, sa = math.cos(a), math.sin(a)
    return [(x + px * ca - py * sa, y + px * sa + py * ca)
            for px, py in ((lx0, ly0), (lx1, ly0), (lx1, ly1), (lx0, ly1))]


def points_box(pts, pad: float = 0.0) -> tuple:
    """Axis-aligned box (x0, y0, x1, y1) around points, grown by pad on every side."""
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return (min(xs) - pad, min(ys) - pad, max(xs) + pad, max(ys) + pad)


def run_start(op) -> tuple:
    """Paper point where a text record's run starts, after its anchor shift."""
    w = tm.text_width(op["s"], op["size"], op["bold"], op["tracking"])
    fx = ANCHOR_FRACTION[op["anchor"]]
    a = math.radians(op["rot"])
    return op["x"] - w * fx * math.cos(a), op["y"] - w * fx * math.sin(a)


def first_line_marks(item, first: bool) -> dict:
    """The keys, fv, cd and claim arguments of Page.text for one wrapped line of a note.

    Only the first line carries the note's value keys, FV tags, code-decision
    ids and claim.
    """
    if not first:
        return {"keys": (), "fv": (), "cd": (), "claim": None}
    return {"keys": getattr(item, "keys", ()), "fv": getattr(item, "fv", ()),
            "cd": getattr(item, "cd", ()),
            "claim": item if getattr(item, "claims", False) else None}


def boxes_overlap(a, b, tol=0.25) -> bool:
    return a[0] < b[2] - tol and b[0] < a[2] - tol and a[1] < b[3] - tol and b[1] < a[3] - tol


def box_inside(inner, outer, tol=0.5) -> bool:
    return (inner[0] >= outer[0] - tol and inner[1] >= outer[1] - tol and
            inner[2] <= outer[2] + tol and inner[3] <= outer[3] + tol)


def union(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return (min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3]))


def arc_segments(cx, cy, r, a0, a1):
    """Cubic Bezier segments for a circular arc from angle a0 to a1 (radians)."""
    segs = []
    n = max(1, int(math.ceil(abs(a1 - a0) / (math.pi / 2) - 1e-9)))
    da = (a1 - a0) / n
    k = 4.0 / 3.0 * math.tan(da / 4.0)
    for i in range(n):
        t0 = a0 + da * i
        t1 = t0 + da
        p0 = (cx + r * math.cos(t0), cy + r * math.sin(t0))
        p3 = (cx + r * math.cos(t1), cy + r * math.sin(t1))
        p1 = (p0[0] - k * r * math.sin(t0), p0[1] + k * r * math.cos(t0))
        p2 = (p3[0] + k * r * math.sin(t1), p3[1] - k * r * math.cos(t1))
        segs.append(("C", p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]))
    return segs


def circle_segments(cx, cy, r):
    return [("M", cx + r, cy)] + arc_segments(cx, cy, r, 0.0, 2 * math.pi) + [("Z",)]


def poly_segments(pts, closed=False):
    """Straight segments through a list of points."""
    segs = [("M",) + tuple(pts[0])] + [("L",) + tuple(p) for p in pts[1:]]
    if closed:
        segs.append(("Z",))
    return segs


def rect_segments(x0, y0, x1, y1):
    return poly_segments([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], closed=True)


def map_segments(segs, fn):
    """Apply fn(x, y) -> (x, y) to every point of a segment list."""
    out = []
    for s in segs:
        if s[0] in ("M", "L"):
            out.append((s[0],) + fn(s[1], s[2]))
        elif s[0] == "C":
            out.append(("C",) + fn(s[1], s[2]) + fn(s[3], s[4]) + fn(s[5], s[6]))
        else:
            out.append(s)
    return out


def seg_points(segs):
    for s in segs:
        if s[0] in ("M", "L"):
            yield s[1], s[2]
        elif s[0] == "C":
            yield s[1], s[2]
            yield s[3], s[4]
            yield s[5], s[6]


# ---------------------------------------------------------------- text over linework
#
# QA's text-on-text check cannot see a label that sits on a door leaf or across
# a door swing. These helpers test each text's ink area against the building
# geometry drawn in the same view. Only the "geom" layer counts as a hit:
# dimension lines, leaders, tags and symbols are annotation and sit near text
# on purpose. A filled annotation shape (an FV tag box, a keynote circle) can
# still hide the geometry under its own text.
# Hatches (paths drawn with a clip) are left out, and so is any text placed
# with collide=False.

_FLATTEN_STEPS = 8
END_INSET = 0.5          # points the text area is inset at each end of the run
TINT_MIN = 0.9           # a fill whose every channel is at least this is a background tint


def text_quad(rec, inset: float = END_INSET) -> list:
    """Corners of the ink area of a text record, in points, following its rotation.

    The area runs from just above the baseline to about cap height, and is
    inset at both ends, so a line that only touches the box edge is not a hit.
    """
    w = tm.text_width(rec["s"], rec["size"], rec["bold"], rec.get("tracking", 0.0))
    fx = ANCHOR_FRACTION[rec["anchor"]]
    lx0, lx1 = -w * fx + inset, w * (1 - fx) - inset
    ly0, ly1 = 0.1 * rec["size"], 0.7 * rec["size"]
    if lx1 <= lx0:
        lx0 = lx1 = (lx0 + lx1) / 2
    return _rotated_corners(rec["x"], rec["y"], rec["rot"], lx0, lx1, ly0, ly1)


def flatten(segs) -> list:
    """Subpaths of a segment list as point lists. Curves become short lines.

    Returns [(points, closed)].
    """
    out, pts, start, closed = [], [], None, False
    for s in segs:
        if s[0] == "M":
            if len(pts) > 1:
                out.append((pts, closed))
            pts, start, closed = [(s[1], s[2])], (s[1], s[2]), False
        elif s[0] == "L":
            pts.append((s[1], s[2]))
        elif s[0] == "C" and pts:
            x0, y0 = pts[-1]
            for i in range(1, _FLATTEN_STEPS + 1):
                t = i / _FLATTEN_STEPS
                u = 1 - t
                pts.append((u ** 3 * x0 + 3 * u * u * t * s[1] + 3 * u * t * t * s[3] + t ** 3 * s[5],
                            u ** 3 * y0 + 3 * u * u * t * s[2] + 3 * u * t * t * s[4] + t ** 3 * s[6]))
        elif s[0] == "Z" and start is not None:
            if pts and pts[-1] != start:
                pts.append(start)
            closed = True
    if len(pts) > 1:
        out.append((pts, closed))
    return out


def _cross(o, a, b) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def _segments_cross(p1, p2, q1, q2) -> bool:
    d1, d2 = _cross(q1, q2, p1), _cross(q1, q2, p2)
    d3, d4 = _cross(p1, p2, q1), _cross(p1, p2, q2)
    return ((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0)) and d1 != 0 and d2 != 0 and d3 != 0 and d4 != 0


def _inside_convex(quad, p) -> bool:
    signs = [_cross(quad[i], quad[(i + 1) % 4], p) for i in range(4)]
    return all(c > 0 for c in signs) or all(c < 0 for c in signs)


def _inside_polygon(pts, p) -> bool:
    inside = False
    n = len(pts)
    for i in range(n):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
        if (y1 > p[1]) != (y2 > p[1]):
            if p[0] < x1 + (p[1] - y1) * (x2 - x1) / (y2 - y1):
                inside = not inside
    return inside


def segment_hits_quad(a, b, quad) -> bool:
    """True when the segment a-b passes through the inside of a convex quad."""
    if _inside_convex(quad, a) or _inside_convex(quad, b):
        return True
    return any(_segments_cross(a, b, quad[i], quad[(i + 1) % 4]) for i in range(4))


def _rings(subpaths) -> list:
    """The rings of flattened subpaths that can enclose an area, without a repeated last point."""
    rings = [pts[:-1] if pts[0] == pts[-1] else pts for pts, _ in subpaths]
    return [r for r in rings if len(r) >= 3]


def _is_tint(fill) -> bool:
    """A light background fill (an elevation wall surface, a room tint). Text on it reads fine."""
    return min(fill) >= TINT_MIN


def grow_quad(quad, along: float, across: float) -> list:
    """The quad from text_quad, grown by `along` points at each end of the run and
    by `across` points above and below it, following its rotation."""
    if along <= 0 and across <= 0:
        return list(quad)
    q0, _, _, q3 = quad
    ex, ey = q3[0] - q0[0], q3[1] - q0[1]          # local up: always nonzero (cap height)
    n = math.hypot(ex, ey)
    uy = (ex / n, ey / n)
    ux = (uy[1], -uy[0])                           # local right, perpendicular to up
    return [(p[0] + sx * along * ux[0] + sy * across * uy[0],
             p[1] + sx * along * ux[1] + sy * across * uy[1])
            for p, (sx, sy) in zip(quad, ((-1, -1), (1, -1), (1, 1), (-1, 1)))]


def _path_hits(op, quad) -> bool:
    subpaths = flatten(op["segs"])
    if op["stroke"] is not None:
        # A stroke has width. Its ink reaches half the line width past the
        # centreline, so the text area grows by that much above and below the
        # run. At the ends, the END_INSET already leaves room for a line that
        # touches the end of a text, so the area grows there only by the rest.
        half = op["lw"] / 2
        squad = grow_quad(quad, max(0.0, half - END_INSET), half)
        for pts, _ in subpaths:
            for a, b in zip(pts, pts[1:]):
                if segment_hits_quad(a, b, squad):
                    return True
    fill = op["fill"]
    if fill is None or _is_tint(fill):
        return False
    # A filled area: even-odd over all closed rings, so a wall poche drawn as an
    # outer and an inner ring does not count the room inside it.
    rings = _rings(subpaths)
    for ring in rings:
        for a, b in zip(ring, ring[1:] + ring[:1]):
            if segment_hits_quad(a, b, quad):
                return True
    cx = sum(p[0] for p in quad) / 4
    cy = sum(p[1] for p in quad) / 4
    return sum(_inside_polygon(r, (cx, cy)) for r in rings) % 2 == 1


def _covers(op, quad) -> bool:
    """True when a filled shape contains the whole quad, so it hides what lies under it."""
    if op["fill"] is None:
        return False
    rings = _rings(flatten(op["segs"]))
    return bool(rings) and all(sum(_inside_polygon(r, c) for r in rings) % 2 == 1 for c in quad)


def text_over_geometry(page) -> list:
    """Every view text whose ink area crosses building geometry in its own view.

    Returns [{text, role, region, bbox}], one entry per text. See the note
    above text_quad for what counts. Only geometry-layer paths can be hits.
    A filled shape that contains the whole text hides the geometry drawn
    before it, so the text is not a hit. That shape can be geometry (a window
    drawn in white over a wall) or annotation (an FV tag box, a keynote
    circle, a white mask).
    """
    geom, covers = {}, {}
    for op in page.ops:
        if op["k"] != "path" or op["clip"] is not None or not op.get("region"):
            continue
        pts = list(seg_points(op["segs"]))
        if not pts:
            continue
        entry = (points_box(pts, op["lw"] / 2), op)
        if op["layer"] == LAYERS["geom"]:
            geom.setdefault(op["region"], []).append(entry)
            covers.setdefault(op["region"], []).append(entry)
        elif op["layer"] == LAYERS["annot"] and op["fill"] is not None:
            covers.setdefault(op["region"], []).append(entry)
    hits = []
    for t in page.texts:
        reg = t.get("region") or ""
        if not t["collide"] or not reg.startswith("view:") or reg not in geom:
            continue
        quad = text_quad(t)
        qbox = points_box(quad)
        near = [(box, op) for box, op in geom[reg] if boxes_overlap(box, qbox, tol=0.0)]
        if not near:
            continue
        own = (t["layer"], t["seq"])
        hidden_below = max(((op["layer"], op["seq"]) for box, op in covers[reg]
                            if (op["layer"], op["seq"]) < own and boxes_overlap(box, qbox, tol=0.0)
                            and _covers(op, quad)),
                           default=None)
        for _, op in near:
            if hidden_below is not None and (op["layer"], op["seq"]) < hidden_below:
                continue
            if _path_hits(op, quad):
                hits.append({"text": t["s"], "role": t["role"], "region": reg, "bbox": t["bbox"],
                             "line_bbox": [round(c, 1) for c in points_box(list(seg_points(op["segs"])))]})
                break
    return hits + text_over_images(page)


def text_over_images(page) -> list:
    """Every text whose ink area lies on a placed image without a backing.

    An image is an occupied area, like building linework. A label may sit on
    it only on a filled backing shape drawn above the image (a white box
    behind a site label, the disc behind a north arrow), so it stays legible
    on any photo. A text placed with collide=False is exempt.
    Returns [{text, role, region, bbox, image}].
    """
    imgs = [op for op in page.ops if op["k"] == "image"]
    if not imgs:
        return []
    backs = [op for op in page.ops if op["k"] == "path" and op["fill"] is not None and op["clip"] is None]
    hits = []
    for t in page.texts:
        if not t["collide"]:
            continue
        quad = text_quad(t)
        qbox = points_box(quad)
        for im in imgs:
            if not boxes_overlap(tuple(im["clip"]), qbox, tol=0.0):
                continue
            above = (im["layer"], im["seq"])
            if any((op["layer"], op["seq"]) > above and (op["layer"], op["seq"]) < (t["layer"], t["seq"])
                   and _covers(op, quad) for op in backs):
                continue
            hits.append({"text": t["s"], "role": t["role"], "region": t.get("region") or "",
                         "bbox": t["bbox"], "image": next((r.get("id") for r in page.images
                                                           if r["seq"] == im["seq"]), None)})
            break
    return hits


class Page:
    """One sheet's display list, in paper points."""

    def __init__(self, sheet_id: str, width_pt: float, height_pt: float):
        self.sheet_id = sheet_id
        self.width = float(width_pt)
        self.height = float(height_pt)
        self.ops: list[dict] = []
        self.texts: list[dict] = []
        self.reserved: list[tuple] = []
        self.collisions: list[dict] = []
        self.claims: list[dict] = []
        self.clouds: list[dict] = []
        self.scale_bars: list[dict] = []
        self.images: list[dict] = []     # every placed raster image, for the sidecar and QA
        self.hatches: list[dict] = []    # every material hatch {region, material}, for QA (drafting.py)
        self.legend_kinds: list[str] = []   # every Panel.legend row kind, for QA (drafting.py)
        self.title = ""
        self.n_para = 0          # paragraphs so far, for group ids that repeat across rebuilds
        self._seq = 0

    # ---- low level

    def _add(self, op: dict, layer: str) -> dict:
        op["layer"] = LAYERS[layer]
        op["seq"] = self._seq
        self._seq += 1
        self.ops.append(op)
        return op

    def path(self, segs, stroke=INK, width=1.0, fill=None, dash=None, layer="geom",
             evenodd=False, cap=1, join=1, clip=None, region=None):
        """Add a path. segs: [('M',x,y), ('L',x,y), ('C',x1,y1,x2,y2,x,y), ('Z',)] in points."""
        op = {"k": "path", "segs": list(segs), "stroke": rgb(stroke), "fill": rgb(fill),
              "lw": float(width), "dash": tuple(dash) if dash else None, "evenodd": evenodd,
              "cap": cap, "join": join, "clip": list(clip) if clip else None, "region": region}
        return self._add(op, layer)

    def text(self, x, y, s, size=8.0, bold=False, anchor="start", rot=0.0, color=INK,
             layer="text", role="text", region=None, keys=(), fv=(), collide=True,
             view=None, tracking=0.0, meta=None, claim=None, cd=()) -> dict:
        """Add a text run at baseline point (x, y) in points. Returns its record.

        A notes.Txt carries the value keys and FV tags it printed; they are
        recorded here. A Txt made by kit.claim() is also recorded as a claim.
        """
        keys = keys or getattr(s, "keys", ())
        fv = fv or getattr(s, "fv", ())
        cd = cd or getattr(s, "cd", ())
        if claim is None and getattr(s, "claims", False):
            claim = s
        s = tm.clean(s)
        if not s.strip():
            raise ValueError("empty text")
        box = text_box(x, y, s, size, bold, rot, anchor, tracking)
        rec = {"k": "text", "x": x, "y": y, "s": s, "size": float(size), "bold": bool(bold),
               "anchor": anchor, "rot": float(rot), "color": rgb(color), "tracking": tracking,
               "bbox": box, "role": role, "region": region, "keys": list(keys),
               "fv": list(fv), "cd": list(cd), "collide": collide, "view": view, "meta": meta or {}}
        self._add(rec, layer)
        self.texts.append(rec)
        if claim is not None:
            self.claims.append({"text": str(claim), "depends_on": list(getattr(claim, "depends_on", ())),
                                "seq": rec["seq"]})
        return rec

    def image(self, raster, box, fit: str = "fit", region=None, layer: str = "geom", record=None) -> dict:
        """Place a raster image (raster.Raster) in box (x0, y0, x1, y1), in points.

        The image keeps its aspect ratio. fit="fit" shows the whole image,
        centred in the box; fit="fill" covers the box and crops what spills
        over. Either way nothing draws outside the box. record: what the
        sidecar keeps about the image (id, kind, path, source); the kit adds
        the box, the pixel size and the print resolution.
        """
        from .raster import placement_matrix
        x0, y0, x1, y1 = (float(v) for v in box)
        bw, bh = x1 - x0, y1 - y0
        dw, dh = raster.display_size
        if bw <= 0 or bh <= 0:
            raise LayoutError(f"image box {box} has no area")
        if fit not in ("fit", "fill"):
            raise ValueError("fit must be 'fit' or 'fill'")
        k = (min if fit == "fit" else max)(bw / dw, bh / dh)
        w, h = dw * k, dh * k
        px, py = x0 + (bw - w) / 2, y0 + (bh - h) / 2
        placed = (px, py, px + w, py + h)
        clip = placed if fit == "fit" else (x0, y0, x1, y1)
        op = {"k": "image", "raster": raster, "clip": clip, "placed": placed,
              "matrix": placement_matrix(raster.orientation, placed), "region": region,
              "fit": fit, "lw": 0.0, "stroke": None, "fill": None}
        self._add(op, layer)
        rec = dict(record or {})
        rec.update({"sha256": raster.sha256, "box": list(clip), "region": region, "fit": fit,
                    "px": [dw, dh], "dpi": round(72.0 * min(dw / w, dh / h), 1), "seq": op["seq"]})
        self.images.append(rec)
        return op

    def reserve(self, box, why="reserved") -> None:
        """Mark an area that labels placed with place_text() must avoid."""
        self.reserved.append((tuple(box), why))

    def free(self, box) -> bool:
        for t in self.texts:
            if t["collide"] and boxes_overlap(box, t["bbox"]):
                return False
        for r, _ in self.reserved:
            if boxes_overlap(box, r):
                return False
        return True

    def place_text(self, x, y, s, candidates=((0.0, 0.0),), **kw) -> dict:
        """Place text at the first candidate offset (points) that collides with nothing.

        If no candidate is free, the text goes at the first candidate and the
        collision is recorded for QA. Nothing is dropped silently.
        """
        size = kw.get("size", 8.0)
        bold = kw.get("bold", False)
        rot = kw.get("rot", 0.0)
        anchor = kw.get("anchor", "start")
        clean = tm.clean(s)
        for dx, dy in candidates:
            if self.free(text_box(x + dx, y + dy, clean, size, bold, rot, anchor)):
                return self.text(x + dx, y + dy, s, **kw)
        dx, dy = candidates[0]
        rec = self.text(x + dx, y + dy, s, **kw)
        self.collisions.append({"text": rec["s"], "bbox": rec["bbox"], "role": rec["role"]})
        return rec

    def ink_box(self, region=None):
        """Bounding box of everything drawn, or only of one region."""
        box = None
        for op in self.ops:
            if region is not None and op.get("region") != region:
                continue
            if op["k"] == "text":
                box = union(box, op["bbox"])
            elif op["k"] == "image":
                box = union(box, tuple(op["clip"]))
            else:
                pts = list(seg_points(op["clip"] or op["segs"]))
                if pts:
                    box = union(box, points_box(pts, op["lw"] / 2 if op["stroke"] else 0.0))
        return box

    def sorted_ops(self):
        return sorted(self.ops, key=lambda o: (o["layer"], o["seq"]))


class View:
    """A drawing placed on a page at a true scale.

    Geometry methods take real inches in project axes (plan: x east, y north;
    elevation: x along the wall as seen, y up). Annotation sizes are in points.
    """

    def __init__(self, page: Page, ident: str, title: str, scale: Scale, extents, origin_pt,
                 cell_pt, project=None, nts_factor: float | None = None, number=None):
        self.page = page
        self.id = ident
        self.title = title
        self.scale = scale
        self.number = number
        self.x0, self.y0, self.x1, self.y1 = (float(v) for v in extents)
        self.s = scale.pt_per_in if scale.is_true else float(nts_factor)
        self.ox, self.oy = origin_pt
        self.cell = tuple(cell_pt)
        self.project = project

    # ---- mapping

    def P(self, x, y):
        """Real inches -> paper points."""
        return (self.ox + (x - self.x0) * self.s, self.oy + (y - self.y0) * self.s)

    @property
    def u(self) -> float:
        """Real inches per paper point. Multiply a point size by u to get inches."""
        return 1.0 / self.s

    @property
    def bbox_pt(self):
        a = self.P(self.x0, self.y0)
        b = self.P(self.x1, self.y1)
        return (a[0], a[1], b[0], b[1])

    def _segs(self, segs):
        return map_segments(segs, self.P)

    @staticmethod
    def _style(kw):
        status = kw.pop("status", None)
        if status:
            st = STATUS_STYLE[status]
            kw.setdefault("stroke", st["stroke"])
            if st["dash"]:
                kw["dash"] = st["dash"]
        return kw

    # ---- geometry in real inches

    def path(self, segs, **kw):
        kw = self._style(kw)
        clip = kw.pop("clip", None)
        return self.page.path(self._segs(segs), clip=self._segs(clip) if clip else None,
                              region=self.id, **kw)

    def line(self, x1, y1, x2, y2, **kw):
        return self.path([("M", x1, y1), ("L", x2, y2)], **kw)

    def polyline(self, pts, closed=False, **kw):
        return self.path(poly_segments(pts, closed), **kw)

    def polygon(self, pts, **kw):
        return self.polyline(pts, closed=True, **kw)

    def rect(self, x0, y0, x1, y1, **kw):
        return self.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], **kw)

    def circle(self, cx, cy, r, **kw):
        """Circle with radius r in real inches."""
        return self.path(circle_segments(cx, cy, r), **kw)

    def arc(self, cx, cy, r, a0_deg, a1_deg, **kw):
        a0, a1 = math.radians(a0_deg), math.radians(a1_deg)
        start = ("M", cx + r * math.cos(a0), cy + r * math.sin(a0))
        return self.path([start] + arc_segments(cx, cy, r, a0, a1), **kw)

    def hatch(self, pts, angle=45.0, spacing_pt=6.0, **kw):
        """Parallel hatch lines clipped to a polygon. Spacing is in points."""
        kw.setdefault("width", 0.4)
        kw.setdefault("layer", "geom")
        self.page.hatches.append({"region": self.id, "material": "hatch"})   # generic: no legend kind
        x0, y0, x1, y1 = points_box(pts)
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        half = math.hypot(x1 - x0, y1 - y0) / 2 + 1
        a = math.radians(angle)
        dx, dy = math.cos(a), math.sin(a)
        nx, ny = -dy, dx
        step = spacing_pt * self.u
        segs = []
        k = -half
        while k <= half:
            px, py = cx + nx * k, cy + ny * k
            segs += [("M", px - dx * half, py - dy * half), ("L", px + dx * half, py + dy * half)]
            k += step
        return self.path(segs, clip=poly_segments(pts, closed=True), **kw)

    # ---- annotation primitives in points, anchored at real points

    def circle_pt(self, cx, cy, r_pt, **kw):
        px, py = self.P(cx, cy)
        kw = self._style(kw)
        kw.setdefault("layer", "annot")
        return self.page.path(circle_segments(px, py, r_pt), region=self.id, **kw)

    def path_pt(self, at, segs_pt, **kw):
        """A path whose shape is in points, placed with its origin at real point `at`."""
        px, py = self.P(*at)
        out = map_segments(segs_pt, lambda x, y: (px + x, py + y))
        kw = self._style(kw)
        kw.setdefault("layer", "annot")
        return self.page.path(out, region=self.id, **kw)

    def paper_path(self, segs, **kw):
        """A path already in paper points, recorded in this view's region."""
        return self.page.path(segs, region=self.id, **kw)

    def paper_text(self, x, y, s, **kw):
        """Text at a paper point, recorded in this view's region and as this view's text."""
        kw.setdefault("region", self.id)
        kw.setdefault("view", self.id)
        return self.page.text(x, y, s, **kw)

    def text(self, x, y, s, size=8.0, dx=0.0, dy=0.0, place=None, **kw):
        """Text at real point (x, y), nudged by (dx, dy) points.

        place: a list of extra (dx, dy) candidates in points. When given, the
        first free spot wins and a collision is recorded if none is free.
        """
        px, py = self.P(x, y)
        kw.setdefault("region", self.id)
        kw.setdefault("view", self.id)
        if place:
            cands = [(dx, dy)] + [tuple(c) for c in place]
            return self.page.place_text(px, py, s, candidates=cands, size=size, **kw)
        return self.page.text(px + dx, py + dy, s, size=size, **kw)

    def reserve(self, x0, y0, x1, y1, why="geometry"):
        """Keep labels placed with `place=` out of a real-inch rectangle."""
        a = self.P(x0, y0)
        b = self.P(x1, y1)
        self.page.reserve(points_box((a, b)), why)
