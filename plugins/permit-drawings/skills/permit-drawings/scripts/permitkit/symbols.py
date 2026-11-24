"""The standard symbol library: opening tags, room tags, elevation markers,
grid bubbles and level markers.

Sizes are paper points, positions real inches on a View, like annot.py.
Every number a symbol prints comes from project.json through the kit, with its
FV tags (see notes.fill). The common set:

    symbols.opening_tag(v, (x, y), "W-1")        # hexagon for a window, circle for a door
    symbols.room_tag(v, (x, y), "BEDROOM", number="101", area="bed_area_sf",
                     lines=[kit.text("CLG {ceil_h:ftin}")])
    symbols.elevation_marker(v, (x, y), {"N": 1, "E": 2}, "A-4")
    symbols.grid_line(v, (0, -40), (0, 300), "A")
    symbols.level_marker(v, 0, 97, "T.O. PLATE", "plate_h")

Use the same symbol for the same thing on every sheet; the door and window
schedule (Panel.opening_schedule) draws the same tags as the plan.

This is the kit's one symbol library. annot.opening_tag, annot.room_tag and
section.level_marker are aliases of the calls here (kept for older sheet
scripts), not separate drawings.
"""
from __future__ import annotations

import math

from . import pens
from . import textmetrics as tm
from .display import DIM, INK, INK2, WHITE, circle_segments, poly_segments, rect_segments
from .model import PrintRefused, Value
from .notes import fill as fill_note

#: opening type -> tag shape. A window or skylight is a hexagon; every door type a circle.
TAG_SHAPE = {"window": "hex", "skylight": "hex"}
#: the `kind` words opening_tag takes, as tag shapes
_KIND_SHAPE = {"door": "circle", "window": "hex"}


def _shape_segs(shape: str, cx: float, cy: float, r: float):
    if shape == "circle":
        return circle_segments(cx, cy, r)
    if shape == "hex":
        return poly_segments([(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
                              for a in range(0, 360, 60)], closed=True)
    if shape == "diamond":
        return poly_segments([(cx + r, cy), (cx, cy + r), (cx - r, cy), (cx, cy - r)], closed=True)
    if shape == "square":
        return rect_segments(cx - r * 0.85, cy - r * 0.85, cx + r * 0.85, cy + r * 0.85)
    if shape == "rect":
        return rect_segments(cx - r * 1.5, cy - r * 0.7, cx + r * 1.5, cy + r * 0.7)
    raise ValueError(f"unknown tag shape {shape!r}: circle, hex, diamond, square or rect")


def tag_radius(mark: str, size: float = 7.0, shape: str = "circle") -> float:
    """The radius a tag needs for its mark."""
    w = tm.text_width(tm.clean(mark), size, True)
    r = max(size * 1.15, w / 2 + (3.2 if shape == "hex" else 2.6))
    return r * (1.08 if shape == "hex" else 1.0)


def tag_paper(page, px, py, mark: str, shape: str = "circle", size: float = 7.0, region=None, view=None,
              layer="annot", role="tag", r=None):
    """A tag symbol centred at paper point (px, py). Returns the text record."""
    r = r or tag_radius(mark, size, shape)
    page.path(_shape_segs(shape, px, py, r), stroke=INK, fill=WHITE, layer=layer, region=region,
              width=pens.width("annot") * 1.4)
    tl = "frame_text" if layer == "frame" else "text"
    return page.text(px, py - tm.ASCENT * size / 2, mark, size=size, bold=True, anchor="middle",
                     region=region, view=view, role=role, collide=False, layer=tl, meta={"mark": mark})


def tag(view, at, mark: str, shape: str = "circle", size: float = 7.0):
    """A tag symbol with its mark at a real point."""
    px, py = view.P(*at)
    return tag_paper(view.page, px, py, mark, shape, size, region=view.id, view=view.id)


def door_tag(view, at, mark: str, size: float = 7.0):
    return tag(view, at, mark, "circle", size)


def window_tag(view, at, mark: str, size: float = 7.0):
    return tag(view, at, mark, "hex", size)


def opening_shape(item: dict) -> str:
    """The tag shape for a project.json opening, from its `type` (or its `tag_shape`)."""
    return item.get("tag_shape") or TAG_SHAPE.get(item.get("type", ""), "circle")


def find_opening(project, mark: str):
    """The project.json opening whose `mark` or `id` is `mark`, or None."""
    ops = project.items("openings") if project is not None else []
    return next((o for o in ops if o.get("mark", o["id"]) == mark or o["id"] == mark), None)


def opening_tag(view, at, mark: str, kind: str | None = None, size: float = 7.0):
    """The tag of a project.json opening: its full mark ("GD-1", never "GD1")
    in the shape its type takes (a hexagon for a window or skylight, a circle
    for every door; an opening's `tag_shape` overrides).

    mark  the opening's `mark` or `id`. When project.json lists openings, a
          mark that none carries is refused, so a tag cannot point at nothing.
    kind  'door' or 'window' (or a tag shape: circle, hex, diamond, square,
          rect) to override the shape, or for a project with no openings list.
    """
    text = tm.clean(str(mark))
    item = find_opening(view.project, text)
    if item is None and view.project is not None and view.project.items("openings"):
        raise PrintRefused(f"opening tag {text!r}: no opening in project.json has that mark or id")
    if kind is not None:
        shape = _KIND_SHAPE.get(kind, kind)
        _shape_segs(shape, 0.0, 0.0, 1.0)          # refuses an unknown kind
    else:
        shape = opening_shape(item) if item is not None else "circle"
    return tag(view, at, (item.get("mark") or item["id"]) if item is not None else text, shape, size)


def room_tag(view, at, name: str, number: str | None = None, area: str | None = None, lines=(),
             size: float = 9.0, frame: bool = False, mask: bool = False):
    """A room tag: name, then the room number in a box, then the area and other lines.

    area   a value key whose unit is sf; prints through the kit with its FV tags.
    lines  more lines (kit.text results), e.g. ceiling height or finishes.
    frame  draw a thin box around the whole tag.
    mask   paint white behind the tag, so a hatch or tint under it stays clear.
    """
    proj = view.project
    rows = [(name, size, True, INK)]
    if area:
        rows.append((fill_note(proj, "{" + area + ":sf}"), size * 0.78, False, INK2))
    for ln in lines:
        rows.append((ln, size * 0.74, False, INK2))
    px, py = view.P(*at)
    lead = 1.18
    num_h = (size * 1.35) if number else 0.0
    heights = [s * lead for _, s, _, _ in rows]
    total = sum(heights) + (num_h + 3 if number else 0)
    widths = [tm.text_width(tm.clean(str(t)), s, b) for t, s, b, _ in rows]
    if number:
        widths.append(tm.text_width(number, size * 0.8, True) + 8)
    half = max(widths) / 2 + 4
    top = py + total / 2
    if mask or frame:
        box = rect_segments(px - half, top - total - 3, px + half, top + 2)
        view.paper_path(box, stroke=INK if frame else None, width=pens.width("fine"),
                        fill=WHITE if mask else None, layer="annot")
    recs = []
    y = top - size
    t, s, b, c = rows[0]
    recs.append(view.paper_text(px, y, t, size=s, bold=b, anchor="middle", color=c, role="room"))
    # the name's underline
    nw = widths[0] / 2
    view.paper_path([("M", px - nw, y - 2.6), ("L", px + nw, y - 2.6)], stroke=INK, width=0.5, layer="annot")
    y -= size * 0.4
    if number:
        nw2 = (tm.text_width(number, size * 0.8, True) + 8) / 2
        view.paper_path(rect_segments(px - nw2, y - num_h, px + nw2, y), stroke=INK, fill=WHITE,
                        width=pens.width("annot"), layer="annot")
        recs.append(view.paper_text(px, y - num_h / 2 - tm.ASCENT * size * 0.8 / 2, number, size=size * 0.8,
                                    bold=True, anchor="middle", role="room", collide=False,
                                    meta={"room_number": number}))
        y -= num_h + 3
    for (t, s, b, c), h in zip(rows[1:], heights[1:]):
        y -= s * 1.05
        recs.append(view.paper_text(px, y, t, size=s, bold=b, anchor="middle", color=c, role="room",
                                    keys=getattr(t, "keys", ()), fv=getattr(t, "fv", ())))
        y -= s * (lead - 1.05)
    return recs


def elevation_marker(view, at, numbers: dict, sheet_ref: str = "", r: float = 11.0):
    """Interior or exterior elevation marker.

    numbers  compass direction -> elevation number, e.g. {"N": 1, "E": 2}. Each
             direction gets a black pointer; plan north is up the sheet.
    """
    px, py = view.P(*at)
    ang = {"N": 90.0, "E": 0.0, "S": 270.0, "W": 180.0}
    for d in numbers:
        if d not in ang:
            raise ValueError(f"elevation marker direction {d!r} must be N, E, S or W")
    for d in numbers:
        a = math.radians(ang[d])
        tip = (px + (r + 8) * math.cos(a), py + (r + 8) * math.sin(a))
        b1 = (px + r * 1.02 * math.cos(a + 0.75), py + r * 1.02 * math.sin(a + 0.75))
        b2 = (px + r * 1.02 * math.cos(a - 0.75), py + r * 1.02 * math.sin(a - 0.75))
        view.paper_path(poly_segments([tip, b1, b2], closed=True), stroke=None, fill=INK, layer="annot")
    view.paper_path(circle_segments(px, py, r), stroke=INK, fill=WHITE, width=1.0, layer="annot")
    recs = []
    if len(numbers) == 1:
        (d, n), = numbers.items()
        view.paper_path([("M", px - r, py), ("L", px + r, py)], stroke=INK, width=0.6, layer="annot")
        recs.append(view.paper_text(px, py + 2.5, str(n), size=7.5, bold=True, anchor="middle", role="bubble",
                                    collide=False))
        recs.append(view.paper_text(px, py - 7.5, sheet_ref or "-", size=5.5, anchor="middle", role="bubble",
                                    collide=False))
        return recs
    if sheet_ref:
        recs.append(view.paper_text(px, py - 2.0, sheet_ref, size=5.0, anchor="middle", role="bubble",
                                    collide=False))
    for d, n in numbers.items():
        a = math.radians(ang[d])
        cx, cy = px + r * 0.62 * math.cos(a), py + r * 0.62 * math.sin(a)
        recs.append(view.paper_text(cx, cy - 2.2, str(n), size=6.0, bold=True, anchor="middle", role="bubble",
                                    collide=False))
    return recs


def grid_bubble(view, at, label: str, r: float = 11.0):
    """A structural grid bubble at a real point."""
    px, py = view.P(*at)
    view.paper_path(circle_segments(px, py, r), stroke=INK, fill=WHITE, width=0.9, layer="annot")
    return view.paper_text(px, py - tm.ASCENT * 9 / 2, label, size=9, bold=True, anchor="middle", role="grid",
                           collide=False)


def grid_line(view, a, b, label: str, ends: str = "start", r: float = 11.0):
    """A grid line from a to b (real points) in the centre pen, with a bubble at one or both ends."""
    pa, pb = view.P(*a), view.P(*b)
    L = math.hypot(pb[0] - pa[0], pb[1] - pa[1]) or 1.0
    ux, uy = (pb[0] - pa[0]) / L, (pb[1] - pa[1]) / L
    s = (pa[0] + ux * r, pa[1] + uy * r) if ends in ("start", "both") else pa
    e = (pb[0] - ux * r, pb[1] - uy * r) if ends in ("end", "both") else pb
    view.paper_path([("M",) + s, ("L",) + e], layer="annot", **pens.kw("center"))
    recs = []
    if ends in ("start", "both"):
        recs.append(_bubble_paper(view, pa, label, r))
    if ends in ("end", "both"):
        recs.append(_bubble_paper(view, pb, label, r))
    return recs


def _bubble_paper(view, p, label, r):
    view.paper_path(circle_segments(p[0], p[1], r), stroke=INK, fill=WHITE, width=0.9, layer="annot")
    return view.paper_text(p[0], p[1] - tm.ASCENT * 9 / 2, label, size=9, bold=True, anchor="middle",
                           role="grid", collide=False)


def level_marker(view, x, y, label: str, value=None, side: str = "right", length_pt: float = 64.0,
                 size: float = 7.0, line: bool = True, reach_pt: float = 0.0, style: str | None = None,
                 value_key: str | None = None):
    """A level datum: a quartered target symbol, the level name and its height.

    value      the height printed under the name: a model Value or a value key
               (e.g. plate height above floor), printed like kit.text with its
               FV tags, in the dimension colour when unverified. None prints
               the name only.
               `value_key=` is the same argument by its older name.
    side       'right' or 'left': which way the marker runs from (x, y).
    reach_pt   a dashed leader this long runs from (x, y) to the symbol, for a
               datum set off the building's face (section.level_marker uses 40).
    line       a solid line under the name, length_pt long from (x, y).
    style      the length format (ftin, in ...); default the project's.
    """
    value = value if value is not None else value_key
    px, py = view.P(x, y)
    r = 4.2
    sgn = 1 if side == "right" else -1
    if reach_pt:
        view.paper_path([("M", px, py), ("L", px + sgn * reach_pt, py)], stroke=INK2, width=0.5, dash=(4, 2),
                        layer="annot")
    cx = px + sgn * (reach_pt + r) if reach_pt else px
    if line:
        view.paper_path([("M", cx + sgn * r, py), ("L", px + sgn * max(length_pt, reach_pt + 2 * r), py)],
                        layer="annot", **pens.kw("annot"))
    view.paper_path(circle_segments(cx, py, r), stroke=INK, fill=WHITE, width=0.7, layer="annot")
    view.paper_path([("M", cx, py)] + _quad(cx, py, r, 0) + [("Z",)], stroke=None, fill=INK, layer="annot")
    view.paper_path([("M", cx, py)] + _quad(cx, py, r, 2) + [("Z",)], stroke=None, fill=INK, layer="annot")
    anchor = "start" if sgn > 0 else "end"
    tx = cx + sgn * (r + 4)
    recs = [view.paper_text(tx, py + 2.5, label, size=size, bold=True, anchor=anchor, role="level")]
    if value is not None:
        val = view.project.value(value) if isinstance(value, str) else value
        if not isinstance(val, Value):
            raise TypeError("level_marker value must be a model Value or a value key, so its status prints")
        txt = fill_note(view.project, "{" + val.key + (":" + style if style else "") + "}")
        recs.append(view.paper_text(tx, py - size - 1.5, txt, size=size * 0.92, anchor=anchor,
                                    color=DIM if txt.fv else INK2, role="level", keys=txt.keys, fv=txt.fv))
    return recs


def _quad(px, py, r, q):
    """Path segments for quarter q (0 = upper right ... counter-clockwise) of a circle, from its centre."""
    from .display import arc_segments
    a0 = q * math.pi / 2
    return [("L", px + r * math.cos(a0), py + r * math.sin(a0))] + arc_segments(px, py, r, a0, a0 + math.pi / 2)


__all__ = ["tag", "door_tag", "window_tag", "opening_tag", "opening_shape", "find_opening", "room_tag",
           "elevation_marker", "grid_bubble", "grid_line", "level_marker", "tag_paper", "tag_radius"]
