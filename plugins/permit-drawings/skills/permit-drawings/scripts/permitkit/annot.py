"""Annotations: dimension chains, leaders, keynotes, bubbles, clouds.
Tags (opening_tag, room_tag) are aliases of the symbols library.

Positions are real inches on a View. Sizes are paper points, so a tick or a
tag looks the same at 1/4" = 1'-0" and at 3" = 1'-0".

Dimension text always comes from a model Value. The kit formats it in
fractions and adds the field-verify tag when the value is unverified. A raw
number is refused: the kit cannot know its status.
"""
from __future__ import annotations

import math

from . import pens
from . import textmetrics as tm
from .display import (DIM, GREY, INK, INK2, WHITE, View, arc_segments, circle_segments,
                      first_line_marks, points_box, poly_segments, rect_segments, text_box)
from .model import PrintRefused, Value
from .model import fv_text
from .notes import tags_for, value_text
# One tag drawing for plans, elevations and schedules: these two live in symbols.
from .symbols import opening_tag, room_tag as _symbols_room_tag

#: names imported from another module that `permitkit api` lists here, as aliases
ALIASES = {"opening_tag": "symbols.opening_tag"}

DIM_SIZE = 8.0           # dimension text, points
TICK = 3.2               # half-length of a tick mark, points
GAP = 2.5                # gap between geometry and an extension line, points
OVER = 3.0               # extension line overshoot past the dimension line, points


def dim_label(view: View, val, style: str | None = None, suffix: str = "") -> tuple[str, list, list]:
    """Printed text for one dimension: (text, value keys, FV tags)."""
    if not isinstance(val, Value):
        raise TypeError("dimension text must come from a model Value (project.value(key)); "
                        f"got {val!r}. Add the number to project.json with a status")
    proj = view.project
    tags = tags_for(proj, val)
    text = value_text(proj, val, style)
    if suffix:
        text += " " + suffix          # the suffix reads with the number: 33'-7" SEP. FV-1,8
    if tags:
        text += " " + fv_text(tags)
    return text, [val.key], list(tags)


def _seg(item):
    if isinstance(item, dict):
        return item["value"], item.get("suffix", ""), item.get("hide", False), item.get("style")
    return item, "", False, None


def dim_chain(view: View, values, start: float, at: float, axis: str = "x", ext_from=None,
              side: int = 1, style: str | None = None, size: float = DIM_SIZE, color=INK2):
    """A chained dimension string with architectural tick marks.

    values  list of Values (or {"value": V, "suffix": "SILL", "hide": False, "style": "in"}).
            Stations are the running sum from `start`.
    axis    'x': stations along x, dimension line at y = at.
            'y': stations along y, dimension line at x = at.
    ext_from  coordinate of the measured geometry on the other axis. Extension
            lines run from there to the dimension line. None draws short nubs.
    side    +1 puts text above (axis x) or left (axis y); -1 below or right.
    Returns the text records.
    """
    segs = [_seg(v) for v in values]
    stations = [float(start)]
    for val, _, _, _ in segs:
        if not isinstance(val, Value):
            dim_label(view, val)          # raises the explanatory TypeError
        stations.append(stations[-1] + float(val))
    unverified = any(v.unverified for v, _, _, _ in segs)
    u = view.u
    lo, hi = min(stations), max(stations)
    line_kw = {"stroke": color, "width": pens.width("dim"), "layer": "annot"}

    def pt(s, o):
        return (s, o) if axis == "x" else (o, s)

    # dimension line, with a short run past the outer ticks
    a, b = pt(lo - 2 * u, at), pt(hi + 2 * u, at)
    view.line(*a, *b, **line_kw)
    for s in stations:
        # tick: 45 degree slash
        x, y = pt(s, at)
        view.line(x - TICK * u, y - TICK * u, x + TICK * u, y + TICK * u,
                  stroke=INK, width=pens.width("tick"), layer="annot")
        if ext_from is None:
            view.line(*pt(s, at - 5 * u), *pt(s, at + 5 * u), **line_kw)
        else:
            d = 1 if at > ext_from else -1
            view.line(*pt(s, ext_from + d * GAP * u), *pt(s, at + d * OVER * u),
                      stroke=color, width=pens.width("ext"), layer="annot")
    records = []
    cap = tm.ASCENT * size
    for i, (val, suffix, hide, sty) in enumerate(segs):
        if hide:
            continue
        text, keys, tags = dim_label(view, val, sty or style, suffix)
        mid = (stations[i] + stations[i + 1]) / 2
        seg_pt = abs(stations[i + 1] - stations[i]) / u
        w = tm.text_width(tm.clean(text), size)
        fits = w + 6 <= seg_pt
        tcolor = DIM if tags else INK
        if axis == "x":
            near = 3.0 if side > 0 else -(cap + 3.0)
            far = -(cap + 3.0) if side > 0 else 3.0
            out = seg_pt / 2 + w / 2 + 5
            cands = [(0, near), (0, far), (out, near), (-out, near), (0, near + side * (cap + 4))]
            if not fits:
                cands = cands[2:] + cands[:2]
            x, y = mid, at
            rot = 0.0
        else:
            near = -3.0 if side > 0 else cap + 3.0
            far = cap + 3.0 if side > 0 else -3.0
            out = seg_pt / 2 + w / 2 + 5
            cands = [(near, 0), (far, 0), (near, out), (near, -out), (near - side * (cap + 4), 0)]
            if not fits:
                cands = cands[2:] + cands[:2]
            x, y = at, mid
            rot = 90.0
        rec = view.text(x, y, text, size=size, dx=cands[0][0], dy=cands[0][1], place=cands[1:],
                        anchor="middle", rot=rot, color=tcolor, role="dim", keys=keys, fv=tags)
        records.append(rec)
    if unverified:
        # unverified chains get a dashed grey dimension line on top, so they read as such
        view.line(*a, *b, stroke=GREY, width=0.6, dash=(4, 2), layer="annot")
    return records


def leader(view: View, target, text, dx: float = 30.0, dy: float = 20.0, size: float = 7.5,
           bold: bool = False, color=INK, arrow: str = "dot", keys=(), fv=(), role="leader"):
    """A leader from a real point to a text label offset by (dx, dy) points.

    `text` may be a list of lines. Returns the text records.
    """
    lines = text if isinstance(text, (list, tuple)) else [text]
    tx, ty = view.P(*target)
    ex, ey = tx + dx, ty + dy
    shoulder = 8.0 if dx >= 0 else -8.0
    view.paper_path([("M", tx, ty), ("L", ex, ey), ("L", ex + shoulder, ey)],
                    stroke=color, width=pens.width("annot"), layer="annot")
    if arrow == "dot":
        view.paper_path(circle_segments(tx, ty, 1.6), stroke=None, fill=color, layer="annot")
    elif arrow == "arrow":
        ang = math.atan2(ey - ty, ex - tx)
        p1 = (tx + 7 * math.cos(ang + 0.35), ty + 7 * math.sin(ang + 0.35))
        p2 = (tx + 7 * math.cos(ang - 0.35), ty + 7 * math.sin(ang - 0.35))
        view.paper_path(poly_segments([(tx, ty), p1, p2], closed=True), stroke=None,
                        fill=color, layer="annot")
    anchor = "start" if dx >= 0 else "end"
    x0 = ex + shoulder + (2 if dx >= 0 else -2)
    lh = size * 1.25
    recs = []
    for i, line in enumerate(lines):
        k = getattr(line, "keys", keys)
        f = getattr(line, "fv", fv)
        recs.append(view.paper_text(x0, ey - size * 0.35 - i * lh, line, size=size, bold=bold,
                                    anchor=anchor, color=color, role=role, keys=k, fv=f))
    return recs


def text_block(view: View, x, y, lines, size: float = 7.5, lead: float = 1.3, anchor="start",
               bold_first=False, color=INK, role="note"):
    """Stacked lines starting at real point (x, y), first baseline at y, going down."""
    recs = []
    for i, line in enumerate(lines):
        if not str(line).strip():
            continue
        recs.append(view.text(x, y, line, size=size, dy=-i * size * lead, anchor=anchor,
                              bold=(bold_first and i == 0), color=color, role=role,
                              keys=getattr(line, "keys", ()), fv=getattr(line, "fv", ())))
    return recs


def paragraph(view: View, x, y, text, width_pt: float, size: float = 7.5, lead: float = 1.3,
              bold: bool = False, color=INK, role="note"):
    """Wrap text to width_pt points, first baseline at real point (x, y), going down.

    The wrapped lines share one group, so QA reads them as one note. Returns
    the real y below the last line.
    """
    # count per page, not per process, so rebuilds in one process stay identical
    view.page.n_para += 1
    group = f"{view.id}:para{view.page.n_para}"
    lines = tm.wrap(tm.clean(str(text)), width_pt, size, bold)
    for i, ln in enumerate(lines):
        view.text(x, y, ln, size=size, dy=-i * size * lead, bold=bold, color=color, role=role,
                  meta={"group": group}, **first_line_marks(text, i == 0))
    return y - len(lines) * size * lead * view.u


def keynote(view: View, at, n, r: float = 7.0, color=INK, leader_to=None):
    """A numbered circle keyed to a numbered note.

    leader_to  a real point the keynote points at; a thin leader runs from
               the circle's edge to it, ending in a dot.
    """
    if leader_to is not None:
        a, b = view.P(*at), view.P(*leader_to)
        d = math.hypot(b[0] - a[0], b[1] - a[1])
        if d > r:
            sx, sy = a[0] + (b[0] - a[0]) * r / d, a[1] + (b[1] - a[1]) * r / d
            view.paper_path([("M", sx, sy), ("L", *b)], stroke=color, width=0.6, layer="annot")
            view.circle_pt(*leader_to, 1.6, stroke=None, fill=color)
    view.circle_pt(*at, r, stroke=color, fill=WHITE, width=1.0)
    px, py = view.P(*at)
    return view.paper_text(px, py - tm.ASCENT * 8 / 2, str(n), size=8, bold=True, anchor="middle",
                           color=color, role="keynote")


def fv_tag(view: View, at, tag: str, dx: float = 0.0, dy: float = 0.0, size: float = 7.0):
    """A boxed field-verify tag, e.g. FV-3. The tag must exist in field_verify."""
    if tag not in view.project.fv:
        raise PrintRefused(f"{tag} is not in project.json field_verify")
    px, py = view.P(*at)
    px += dx
    py += dy
    w = tm.text_width(tag, size, True) + 6
    h = size + 4
    view.paper_path(rect_segments(px - w / 2, py - h / 2, px + w / 2, py + h / 2), stroke=DIM,
                    fill=WHITE, width=0.8, layer="annot")
    return view.paper_text(px, py - tm.ASCENT * size / 2, tag, size=size, bold=True, anchor="middle",
                           color=DIM, role="fv", fv=[tag])


def room_tag(view: View, at, name: str, lines=(), size: float = 10.0, **kw):
    """Room name with smaller lines under it: alias of symbols.room_tag, with
    `lines` as the fourth argument. symbols.room_tag also takes number=,
    area=, frame= and mask=."""
    return _symbols_room_tag(view, at, name, lines=lines, size=size, **kw)


def north_arrow(view: View, at, r: float = 13.0, rotation_deg: float = 0.0, label="N", value=None):
    """North arrow at a real point. rotation_deg turns it clockwise from sheet-up.

    Plans draw north up, so a plan-north arrow uses 0 (label it "PN" if the
    sheet also shows true north). To show true north, pass the project's
    angle as `value` (`p.true_north`). The arrow then turns by that value, and an
    unverified angle prints its FV tag after the label, like any other value.
    A PLACEHOLDER angle, or an ASSUMED angle with no FV tag, is refused.
    """
    keys, tags = [], []
    if value is not None:
        val = view.project.value(value) if isinstance(value, str) else value
        if not isinstance(val, Value):
            raise TypeError("north_arrow value must be a model Value or a value key")
        rotation_deg = float(val)
        if val.status is not None:           # a plain-number true_north_deg has no status
            tags = list(tags_for(view.project, val))
            keys = [val.key]
    px, py = view.P(*at)
    a = -math.radians(rotation_deg)

    def rot(x, y):
        return (px + x * math.cos(a) - y * math.sin(a), py + x * math.sin(a) + y * math.cos(a))
    view.paper_path(circle_segments(px, py, r), stroke=INK, width=0.8, layer="annot")
    tip, left, right, tail = rot(0, r * 1.35), rot(-r * 0.42, -r * 0.6), rot(r * 0.42, -r * 0.6), rot(0, -r * 0.25)
    view.paper_path(poly_segments([tip, right, tail], closed=True), stroke=INK, fill=INK,
                    width=0.6, layer="annot")
    view.paper_path(poly_segments([tip, left, tail], closed=True), stroke=INK, fill=WHITE,
                    width=0.6, layer="annot")
    lx, ly = rot(0, r * 1.35 + 4)
    rec = view.paper_text(lx, ly, label, size=10, bold=True, anchor="middle", rot=0, role="north",
                          keys=keys, fv=tags)
    if tags:
        # The tag sits outside the circle on the side opposite the label, so
        # the label and the tag never meet at any rotation. It is in the same
        # text group as the label.
        group = f"north:{rec['seq']}"
        rec["meta"]["group"] = group
        tag = fv_text(tags)
        bx0, by0, bx1, by1 = text_box(0.0, 0.0, tag, 7, True, 0.0, "middle")
        ox, oy = math.sin(a), -math.cos(a)        # unit vector away from the label
        reach = r + 3 + abs(ox) * (bx1 - bx0) / 2 + abs(oy) * (by1 - by0) / 2
        cx, cy = px + ox * reach, py + oy * reach
        view.paper_text(cx - (bx0 + bx1) / 2, cy - (by0 + by1) / 2, tag, size=7, bold=True,
                        anchor="middle", color=DIM, role="north", meta={"group": group})
    return rec


def _bar_step(ft_pt: float) -> int:
    for cand in (1, 2, 5, 10, 20, 50):
        if cand * ft_pt >= 18:
            return cand
    return 100


def auto_bar_feet(view: View) -> int:
    """Default scale-bar length in feet: four divisions when they fit in about
    3 in. of paper, fewer when not."""
    ft_pt = 12 * view.s
    step = _bar_step(ft_pt)
    return step * max(1, min(4, int(220 / (step * ft_pt))))


def scale_bar(view: View, at, feet: int | None = None):
    """Graphic scale in feet, left end at a real point. Length matches the view scale."""
    if not view.scale.is_true:
        raise PrintRefused("a scale bar on an N.T.S. view would be false")
    ft_pt = 12 * view.s
    step = _bar_step(ft_pt)
    if feet is None:
        feet = auto_bar_feet(view)
    px, py = view.P(*at)
    n = max(1, feet // step)
    for i in range(n):
        x0 = px + i * step * ft_pt
        view.paper_path(rect_segments(x0, py, x0 + step * ft_pt, py + 5), stroke=INK, width=0.6,
                        fill=INK if i % 2 == 0 else WHITE, layer="annot")
    recs = []
    for i in range(n + 1):
        recs.append(view.paper_text(px + i * step * ft_pt, py + 8, str(i * step), size=6, anchor="middle",
                                    color=INK2, role="scalebar"))
    recs.append(view.paper_text(px + n * step * ft_pt + 6, py, "FEET", size=6, color=INK2,
                                role="scalebar"))
    view.page.scale_bars.append({"view": view.id, "feet": n * step,
                                 "length_pt": n * step * ft_pt, "pt_per_in": view.s})
    return recs


def detail_bubble(view: View, at, number, sheet_ref: str = "", r: float = 11.0):
    """Circle split by a line: detail number on top, sheet reference below."""
    px, py = view.P(*at)
    view.paper_path(circle_segments(px, py, r), stroke=INK, fill=WHITE, width=1.0, layer="annot")
    recs = []
    if sheet_ref:
        view.paper_path([("M", px - r, py), ("L", px + r, py)], stroke=INK, width=0.7, layer="annot")
        recs.append(view.paper_text(px, py + 2.5, str(number), size=8, bold=True, anchor="middle",
                                    role="bubble", collide=False))
        recs.append(view.paper_text(px, py - 8, sheet_ref, size=6, anchor="middle", role="bubble",
                                    collide=False))
    else:
        recs.append(view.paper_text(px, py - 3, str(number), size=9, bold=True, anchor="middle",
                                    role="bubble", collide=False))
    return recs


def section_mark(view: View, a, b, number, sheet_ref: str = "", look: int = 1, r: float = 10.0):
    """A section cut from a to b (real points) with a bubble at each end.

    look: +1 looks to the left of a->b, -1 to the right. Arrows show the view direction.
    """
    pa, pb = view.P(*a), view.P(*b)
    view.paper_path([("M",) + pa, ("L",) + pb], stroke=INK, width=1.2, dash=(14, 3, 3, 3),
                    layer="annot")
    ang = math.atan2(pb[1] - pa[1], pb[0] - pa[0]) + look * math.pi / 2
    recs = []
    for p in (pa, pb):
        tip = (p[0] + (r + 7) * math.cos(ang), p[1] + (r + 7) * math.sin(ang))
        base = [(p[0] + r * math.cos(ang + 0.6), p[1] + r * math.sin(ang + 0.6)),
                (p[0] + r * math.cos(ang - 0.6), p[1] + r * math.sin(ang - 0.6))]
        view.paper_path(poly_segments([tip] + base, closed=True), stroke=None, fill=INK, layer="annot")
        recs += _bubble_at(view, p, number, sheet_ref, r)
    return recs


def _bubble_at(view, p, number, sheet_ref, r):
    view.paper_path(circle_segments(p[0], p[1], r), stroke=INK, fill=WHITE, width=1.0, layer="annot")
    view.paper_path([("M", p[0] - r, p[1]), ("L", p[0] + r, p[1])], stroke=INK, width=0.6,
                    layer="annot")
    return [view.paper_text(p[0], p[1] + 2.5, str(number), size=7.5, bold=True, anchor="middle",
                            role="bubble", collide=False),
            view.paper_text(p[0], p[1] - 7.5, sheet_ref or "-", size=5.5, anchor="middle",
                            role="bubble", collide=False)]


# ------------------------------------------------------------------ revisions


def cloud_segments(box, r: float = 6.0):
    """Scalloped outline around a box (x0, y0, x1, y1) in points. Scallops bulge outward."""
    x0, y0, x1, y1 = box
    corners = [(x0, y0), (x0, y1), (x1, y1), (x1, y0)]      # clockwise in y-up axes
    segs = [("M",) + corners[0]]
    for i in range(4):
        ax, ay = corners[i]
        bx, by = corners[(i + 1) % 4]
        length = math.hypot(bx - ax, by - ay)
        n = max(1, round(length / (2 * r)))
        for k in range(n):
            sx, sy = ax + (bx - ax) * k / n, ay + (by - ay) * k / n
            ex, ey = ax + (bx - ax) * (k + 1) / n, ay + (by - ay) * (k + 1) / n
            cx, cy = (sx + ex) / 2, (sy + ey) / 2
            rr = math.hypot(ex - sx, ey - sy) / 2
            a0 = math.atan2(sy - cy, sx - cx)
            # clockwise travel: the outward side is to the left, so sweep clockwise (negative)
            segs += arc_segments(cx, cy, rr, a0, a0 - math.pi)
    segs.append(("Z",))
    return segs


def delta(page, x, y, n: int, size: float = 11.0, region=None, view=None, layer="annot"):
    """A revision triangle with its number, centred at (x, y) points."""
    h = size
    segs = [("M", x, y + h * 0.62), ("L", x - h * 0.6, y - h * 0.42), ("L", x + h * 0.6, y - h * 0.42), ("Z",)]
    page.path(segs, stroke=INK, fill=WHITE, width=1.0, layer=layer, region=region)
    tl = "frame_text" if layer == "frame" else "text"
    return page.text(x, y - h * 0.3, str(n), size=h * 0.62, bold=True, anchor="middle",
                     region=region, view=view, role="delta", collide=False, layer=tl,
                     meta={"delta": n})


def revision_cloud(view: View, x0, y0, x1, y1, delta_n: int, pad_pt: float = 4.0, r: float = 6.0,
                   corner: str = "tr"):
    """Cloud a real-inch box on a view and tag it with a revision triangle.

    The cloud grows by pad_pt around the box, so it does not touch what it marks.
    """
    a, b = view.P(x0, y0), view.P(x1, y1)
    box = points_box((a, b), pad_pt)
    return cloud_box(view.page, box, delta_n, r=r, corner=corner, region=view.id, view=view.id)


def cloud_box(page, box, delta_n: int, r: float = 6.0, corner: str = "tr", region=None, view=None):
    """Cloud a box given in points. Records the cloud for QA."""
    page.path(cloud_segments(box, r), stroke=INK, width=1.1, layer="annot", region=region)
    x = box[2] + r + 8 if "r" in corner else box[0] - r - 8
    y = box[3] if "t" in corner else box[1]
    rec = delta(page, x, y, delta_n, region=region, view=view)
    page.clouds.append({"delta": delta_n, "bbox": box, "view": view})
    return rec
