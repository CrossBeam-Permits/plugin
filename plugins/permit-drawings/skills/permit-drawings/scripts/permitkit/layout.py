"""Sheet composition: pick scales and cells so drawings fill the sheet.

A drawing that sits small in a big empty cell is the first thing that makes a
set look amateur. `arrange` takes the views a sheet needs, in reading order,
and finds the row layout and the largest standard scale for each view that
fits the area, then gives every view a cell sized to it. The kit's rule holds:
a view is placed at a true scale or not at all. `arrange` only chooses the
scale; it never shrinks a drawing.

    from permitkit import layout
    plan, elec = layout.arrange(sh, [
        {"title": "PROPOSED FLOOR PLAN", "extents": (-36, -36, 252, 200)},
        {"title": "ELECTRICAL PLAN", "extents": (-36, -36, 252, 200), "max_scale": '1/4" = 1\'-0"'},
    ], area=(0, 4.5, 26.5, 17.9))             # inches from the drawing-area lower-left

    cells = layout.cover_cells(sh)            # a title-sheet composition
    sh.panel(cells["data"], "PROJECT DATA") ...
"""
from __future__ import annotations

from functools import lru_cache

from . import textmetrics as tm
from .display import LayoutError
from .sheet import TITLE_LEFT, TITLE_STRIP, title_lines, title_width
from .units import PT_PER_IN, SCALES, SIZE_SCALES, ScaleError, scale as get_scale, scale_kind

#: Architectural scales a view may take, smallest first: 1/16" (a large plan) to 3" (a detail).
#: 1/32" = 1'-0" is in SCALES for a site plan; pass it in a view's `scales`.
ARCH_SCALES = [lab for lab, sc in SCALES.items() if lab.endswith("= 1'-0\"") and 1 / 192 - 1e-12 <= sc.ratio <= 0.25]
#: Engineering (site) scales, smallest first.
SITE_SCALES = sorted((lab for lab in SCALES if lab.startswith('1" = ') and lab.endswith("'-0\"")
                      and not lab.endswith("= 1'-0\"")), key=lambda lab: SCALES[lab].ratio)
PAD = 6.0 / PT_PER_IN            # the view's inner padding, inches (Sheet.view uses 6 pt)
MARGIN = 0.1                    # default slack around a view's extents, paper inches


def need(extents, label: str, title: str | None = None, margin: float = 0.0,
         subtitle: str = "") -> tuple[float, float]:
    """Paper inches (w, h) a view needs at a scale, title strip and padding included.

    With a title, the width also holds the view title, its bubble and scale
    line, wrapped the way Sheet.view wraps them (two title lines, a long
    subtitle on its own line), so a long title does not push views into more
    rows or a smaller scale. `margin` adds paper inches on every side, for a
    revision cloud or a label that sits just outside the extents.
    """
    x0, y0, x1, y1 = (float(v) for v in extents)
    r = get_scale(label).ratio
    w = (x1 - x0) * r + 2 * PAD + 0.02 + 2 * margin
    if title:
        w = max(w, _title_need(title, subtitle or "", get_scale(label).printed))
    return w, (y1 - y0) * r + TITLE_STRIP / PT_PER_IN + 2 * PAD + 0.02 + 2 * margin


@lru_cache(maxsize=4096)
def _title_need(title: str, subtitle: str, printed: str) -> float:
    """The narrowest cell (inches) whose view title strip fits, to 0.01 in."""
    def fits(w_in):
        return title_lines(title, subtitle, printed, w_in * PT_PER_IN - 2 * PAD * PT_PER_IN - TITLE_LEFT)

    one = ([tm.clean(title)], [f"SCALE: {printed}" + (f"   {subtitle}" if subtitle else "")])
    hi = (title_width(one) + 2 * PAD * PT_PER_IN + 2) / PT_PER_IN
    lo = 0.0
    if not fits(hi):
        return hi
    while hi - lo > 0.01:
        mid = (lo + hi) / 2
        if fits(mid):
            hi = mid
        else:
            lo = mid
    return hi


def fit_scale(extents, w: float, h: float, scales=None) -> str:
    """The largest scale in `scales` (default ARCH_SCALES) at which a view fits a w x h inch cell."""
    for lab in reversed(list(scales or ARCH_SCALES)):
        nw, nh = need(extents, lab)
        if nw <= w and nh <= h:
            return lab
    raise ScaleError(f"extents {extents} fit no scale in {list(scales or ARCH_SCALES)} in a "
                     f"{w:.2f} x {h:.2f} in cell")


def _ladder(spec) -> list[str]:
    lad = list(spec.get("scales") or ARCH_SCALES)
    # FULL SIZE and HALF SIZE join only when the view's max_scale or min_scale names one
    if not spec.get("scales") and any(spec.get(k) and scale_kind(spec[k]) == "size"
                                      for k in ("max_scale", "min_scale")):
        lad += SIZE_SCALES
    lad.sort(key=lambda lab: get_scale(lab).ratio)
    if spec.get("max_scale"):
        mx = get_scale(spec["max_scale"]).ratio
        lad = [s for s in lad if get_scale(s).ratio <= mx + 1e-9]
    if spec.get("min_scale"):
        mn = get_scale(spec["min_scale"]).ratio
        lad = [s for s in lad if get_scale(s).ratio >= mn - 1e-9]
    if not lad:
        raise ScaleError(f"view {spec.get('title')!r}: no scale between its min_scale and max_scale")
    return lad


def _partitions(n):
    """Every way to split n ordered views into consecutive rows."""
    for mask in range(1 << (n - 1)):
        rows, cur = [], [0]
        for i in range(1, n):
            if mask >> (i - 1) & 1:
                rows.append(cur)
                cur = [i]
            else:
                cur.append(i)
        rows.append(cur)
        yield rows


def _sizes(specs, ladders, idx):
    return [need(s["extents"], ladders[i][idx[i]], s.get("title"), s.get("margin", MARGIN), s.get("subtitle", ""))
            for i, s in enumerate(specs)]


def _fits(sizes, rows, W, H, gap):
    """(row widths, row heights) when the rows fit W x H, else None."""
    widths = [sum(sizes[i][0] for i in r) + gap * (len(r) - 1) for r in rows]
    heights = [max(sizes[i][1] for i in r) for r in rows]
    if all(w <= W + 1e-9 for w in widths) and sum(heights) + gap * (len(rows) - 1) <= H + 1e-9:
        return widths, heights
    return None


def _ratios(ladders, idx):
    return [get_scale(ladders[i][k]).ratio for i, k in enumerate(idx)]


def _paper_area(specs, ladders, idx):
    total = 0.0
    for spec, r in zip(specs, _ratios(ladders, idx)):
        x0, y0, x1, y1 = spec["extents"]
        total += (x1 - x0) * (y1 - y0) * r * r
    return total


def _capped(ladders, cap):
    """Each view's largest scale at or under `cap` (its smallest scale when all are bigger)."""
    out = []
    for lad in ladders:
        k = 0
        for j, lab in enumerate(lad):
            if get_scale(lab).ratio <= cap + 1e-12:
                k = j
        out.append(k)
    return out


def _raise(specs, ladders, idx, rows, W, H, gap):
    """Step views up their ladders while the rows still fit, smallest scale first."""
    idx = list(idx)
    while True:
        best = None
        for i in range(len(idx)):
            if idx[i] + 1 >= len(ladders[i]):
                continue
            trial = idx[:i] + [idx[i] + 1] + idx[i + 1:]
            if _fits(_sizes(specs, ladders, trial), rows, W, H, gap) is None:
                continue
            key = (get_scale(ladders[i][idx[i]]).ratio, -_paper_area(specs, ladders, trial), i)
            if best is None or key < best[0]:
                best = (key, trial)
        if best is None:
            return idx
        idx = best[1]


def _choose(specs, ladders, W, H, gap, same):
    """Rows and a scale for every view: (score, rows, idx, widths, heights) or None.

    Scales come down together: every view takes the largest scale under one
    cap, and the cap drops until some row layout fits. Then each view that
    still has room steps up on its own (a detail capped by max_scale, a small
    view beside a big one). Among layouts, the one whose smallest scale is
    largest wins (then the next smallest, and so on), then more drawing on
    paper, then fewer rows. So four elevations of one building share a scale
    instead of one taking 1/2" while another drops to 1/16". The last tie-break
    is the least empty width in the emptiest row, so two sections sit side by
    side rather than one alone in a wide row.
    """
    caps = sorted({get_scale(lab).ratio for lad in ladders for lab in lad}, reverse=True)
    parts = list(_partitions(len(specs)))
    for cap in caps:
        base = _capped(ladders, cap)
        sizes = _sizes(specs, ladders, base)
        best = None
        for rows in parts:
            if _fits(sizes, rows, W, H, gap) is None:
                continue
            idx = base if same else _raise(specs, ladders, base, rows, W, H, gap)
            widths, heights = _fits(_sizes(specs, ladders, idx), rows, W, H, gap)
            score = (tuple(round(r, 9) for r in sorted(_ratios(ladders, idx))),
                     round(_paper_area(specs, ladders, idx), 3), -len(rows),
                     -round(max(W - w for w in widths), 3))
            if best is None or score > best[0]:
                best = (score, rows, idx, widths, heights)
        if best is not None:
            return best
    return None


FILLS = ("even", "top", "stretch")

#: arrange() grows small details past 3" = 1'-0" only when its first choice
#: leaves less than this share of the area holding drawings.
GROW_BELOW = 0.5


def _used(specs, ladders, idx, W, H) -> float:
    """Share of the W x H area the chosen views need (their cells before spare space)."""
    return sum(w * h for w, h in _sizes(specs, ladders, idx)) / (W * H)


def _grow(specs, ladders, best, W, H, gap):
    """(ladders, best) with HALF SIZE and FULL SIZE added for small details, when that fills more.

    Only a view with no `scales`, `scale`, `max_scale` or `min_scale` of its
    own, already at the top of its ladder (3" = 1'-0"), grows. The views keep
    a true, standard scale; the cap that brings scales down together still
    applies, so a big plan beside a detail is never shrunk for it.
    """
    before = _used(specs, ladders, best[2], W, H)
    if before >= GROW_BELOW:
        return ladders, best
    grown = []
    for spec, lad, k in zip(specs, ladders, best[2]):
        own = any(spec.get(key) for key in ("scales", "scale", "max_scale", "min_scale"))
        if own or k != len(lad) - 1:
            grown.append(lad)
        else:
            grown.append(sorted(set(lad) | set(SIZE_SCALES), key=lambda lab: get_scale(lab).ratio))
    if grown == ladders:
        return ladders, best
    alt = _choose(specs, grown, W, H, gap, False)
    if alt is None or _used(specs, grown, alt[2], W, H) <= before + 1e-9:
        return ladders, best
    return grown, alt


#: A detail (a view whose max_scale names HALF SIZE or FULL SIZE) asks for the
#: first of these scales it can reach before arrange() settles on less.
DETAIL_FLOORS = ('3" = 1\'-0"', '1-1/2" = 1\'-0"')
#: How many steps down its ladder another view may take so the details reach a floor.
DETAIL_GIVE = 1


def _ratio(label: str) -> float:
    return get_scale(label).ratio


def _is_detail(spec) -> bool:
    """A view the drafter marked as a detail: max_scale names a size scale, and no
    min_scale, scale or scales of its own fixes it."""
    return (bool(spec.get("max_scale")) and scale_kind(spec["max_scale"]) == "size"
            and not any(spec.get(k) for k in ("min_scale", "scale", "scales")))


def _detail_floor(specs, ladders, best, W, H, gap):
    """(ladders, best) with every detail at a DETAIL_FLOORS scale, when the other views give at most DETAIL_GIVE steps.

    Scales come down together, so two big sections can take 3/4" = 1'-0" and
    leave a short row where the details only reach 1-1/2" = 1'-0" (or less),
    in wide empty cells. A drafter would put the sections at 1/2" and the
    details at 3". This tries each floor in turn: the details may not go under
    it, and the layout is kept only when no other view drops more than
    DETAIL_GIVE steps down its own ladder. A view's own min_scale still holds,
    so a plan the city wants at 1/4" never goes under it.
    """
    details = [i for i, s in enumerate(specs) if _is_detail(s)]
    if not details:
        return ladders, best
    for label in DETAIL_FLOORS:
        floor = get_scale(label).ratio
        if all(get_scale(ladders[i][best[2][i]]).ratio >= floor - 1e-9 for i in details):
            return ladders, best
        # a detail never ends under its first choice (up to 3"), nor under this floor;
        # _ladder keeps its HALF/FULL SIZE top, so a floored ladder is never empty
        floored = [_ladder(dict(s, min_scale=max(label, min(lad[best[2][i]], DETAIL_FLOORS[0], key=_ratio),
                                                 key=_ratio)))
                   if i in details else lad for i, (s, lad) in enumerate(zip(specs, ladders))]
        alt = _choose(specs, floored, W, H, gap, False)
        if alt is not None and all(alt[2][i] >= best[2][i] - DETAIL_GIVE
                                   for i in range(len(specs)) if i not in details):
            return floored, alt
    return ladders, best


def plan(specs, area, gap: float = 0.4, same_scale: bool = False, fill: str = "even", grow: bool = True):
    """Choose rows, scales and cells for views. Returns [(spec, scale label, cell)] in spec order.

    specs  dicts with `extents` and optionally `scales` (ladder), `max_scale`,
           `min_scale`. area = (x, y, w, h) inches.
    fill   where the height the rows do not need goes. 'even' (default):
           equal space above each row and under the last, so the rows spread
           down the area; 'top': rows packed at the top, spare at the bottom;
           'stretch': rows grow to fill the area (a bottom-aligned drawing then
           sits at the foot of a tall cell). A view's cell always reaches up to
           the row above, so a label just past the extents still lands in it.
    A detail (max_scale HALF SIZE or FULL SIZE) gets at least 3" = 1'-0",
    else 1-1/2" = 1'-0", when the other views give at most one scale step for it.
    grow   when the chosen scales leave under half the area holding drawings,
           details at 3" = 1'-0" with no scale limit of their own may take
           HALF SIZE or FULL SIZE, so a sheet of small details is not half
           blank. grow=False keeps the 3" ceiling. Not with same_scale.
    """
    if not specs:
        return []
    if fill not in FILLS:
        raise ValueError(f"fill must be one of {FILLS}")
    ax, ay, W, H = area
    ladders = [_ladder(s) for s in specs]
    if same_scale:
        common = sorted(set.intersection(*(set(l) for l in ladders)), key=lambda lab: get_scale(lab).ratio)
        if not common:
            raise ScaleError("same_scale: the views share no scale")
        ladders = [common for _ in specs]
    best = _choose(specs, ladders, W, H, gap, same_scale)
    if best is None:
        raise ScaleError(f"the views do not fit a {W:.2f} x {H:.2f} in area at any scale in their ladders. "
                         "Give them a bigger area, tighter extents, or smaller scales")
    if not same_scale:
        ladders, best = _detail_floor(specs, ladders, best, W, H, gap)
        if grow:
            ladders, best = _grow(specs, ladders, best, W, H, gap)
    _, rows, idx, widths, heights = best
    spare_h = max(0.0, H - sum(heights) - gap * (len(rows) - 1))
    n = len(rows)
    above = {"even": spare_h / (n + 1), "top": 0.0, "stretch": spare_h / n}[fill]
    sizes = _sizes(specs, ladders, idx)
    out = [None] * len(specs)
    y = ay + H
    for r, rw, rh in zip(rows, widths, heights):
        rh_cell = rh + above
        spare_w = W - rw
        sum_w = sum(sizes[i][0] for i in r)
        x = ax
        for i in r:
            nw = sizes[i][0]
            cw = nw + spare_w * nw / sum_w
            out[i] = (specs[i], ladders[i][idx[i]], (round(x, 4), round(y - rh_cell, 4), round(cw, 4),
                                                     round(rh_cell, 4)))
            x += cw + gap
        y -= rh_cell + gap
    return out


def arrange(sh, specs, area=None, gap: float = 0.4, same_scale: bool = False, fill: str = "even",
            grow: bool = True):
    """Place views on a sheet with the scales and cells plan() picks. Returns the Views in spec order.

    Each spec may also carry the Sheet.view keywords `number`, `subtitle`,
    `scale_bar` and `align` ('bottom' default, 'center', 'top' or 'tl'), `scale` to fix one view's scale outright, and
    `margin` (paper inches of slack around its extents, default MARGIN).
    area   (x, y, w, h) inches from the drawing-area lower-left; default the
           whole drawing area. Keep panels out of it.
    same_scale  give every view one scale (plans of one building).
    fill   'even' (default), 'top' or 'stretch': where spare height goes (see plan()).
    grow   let small details take HALF SIZE or FULL SIZE when the sheet would
           be under half used (see plan()).
    """
    if area is None:
        dw, dh = sh.drawing_area_in
        area = (0.0, 0.0, dw, dh)
    specs = [dict(s, scales=[s["scale"]]) if s.get("scale") else dict(s) for s in specs]
    placed = plan(specs, area, gap, same_scale, fill, grow)
    views = []
    for spec, label, cell in placed:
        kw = {k: spec[k] for k in ("number", "subtitle", "scale_bar", "align") if k in spec}
        kw.setdefault("align", "bottom")
        v = sh.view(spec["title"], label, spec["extents"], cell=cell, **kw)
        v.fits_larger = None        # the scale came from the view's ladder, not a hand pick
        views.append(v)
    return views


def grid(area, rows: int, cols: int, gap: float = 0.3):
    """Equal cells (x, y, w, h) on a rows x cols grid, left to right, top to bottom."""
    ax, ay, W, H = area
    cw = (W - gap * (cols - 1)) / cols
    ch = (H - gap * (rows - 1)) / rows
    return [(ax + c * (cw + gap), ay + H - (r + 1) * ch - r * gap, cw, ch) for r in range(rows) for c in range(cols)]


def split(area, fractions, axis: str = "x", gap: float = 0.3):
    """Split an area into strips by fractions, left to right (axis x) or top to bottom (axis y)."""
    ax, ay, W, H = area
    total = sum(fractions)
    span = (W if axis == "x" else H) - gap * (len(fractions) - 1)
    out, pos = [], (ax if axis == "x" else ay + H)
    for f in fractions:
        d = span * f / total
        if axis == "x":
            out.append((pos, ay, d, H))
            pos += d + gap
        else:
            out.append((ax, pos - d, W, d))
            pos -= d + gap
    return out


def cover_cells(sh, image: bool = True, gap: float = 0.3):
    """Cells for a title sheet modelled on a professional cover.

    Left column: `data` (project data, zoning and area tables). Centre column:
    `rendering` (a slot for a 3D view or photo) over `vicinity` (a slot for
    the vicinity or aerial map). Right column: `codes`, `directory`, `index`
    and `scope`. With image=False the centre column becomes `notes` (top) and
    `fv` (bottom). Returns {name: (x, y, w, h)} in inches.
    """
    dw, dh = sh.drawing_area_in
    left, mid, right = split((0.0, 0.0, dw, dh), [0.37, 0.36, 0.27], "x", gap)
    top, bottom = split(mid, [0.56, 0.44], "y", gap)
    codes, directory, index, scope = split(right, [0.30, 0.17, 0.27, 0.26], "y", gap)
    cells = {"data": left, "codes": codes, "directory": directory, "index": index, "scope": scope}
    if image:
        cells.update(rendering=top, vicinity=bottom)
    else:
        cells.update(notes=top, fv=bottom)
    for name, c in cells.items():
        if c[2] <= 0 or c[3] <= 0:
            raise LayoutError(f"cover cell {name} has no room on this sheet size")
    return cells
