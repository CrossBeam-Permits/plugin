"""The sheet template: border, title block, notes column, view placement.

Paper layout is in inches from the lower-left corner of the drawing area,
x right and y up, like every other axis in the kit.

Hard rule: a view is placed at its stated scale or not at all. If its extents
do not fit the cell at that scale, Sheet.view() raises ScaleError. The kit never
shrinks a drawing to fit.
"""
from __future__ import annotations

from . import textmetrics as tm
from .annot import auto_bar_feet, cloud_segments, delta, scale_bar as draw_scale_bar
from .site import PL_DASH, SETBACK_DASH
from .display import (DIM, GREY, INK, INK2, LIGHT, POCHE_E, POCHE_N, WHITE, LayoutError, Page, View,
                      box_inside, boxes_overlap, circle_segments, first_line_marks, rect_segments,
                      text_over_geometry)
from .units import NTS, PT_PER_IN, SCALES, SHEET_SIZES, ScaleError, scale as get_scale, scale_kind, fmt_in

BORDER = 0.5            # border inset, inches
GUTTER = 0.3            # space between border/column and the drawing area, inches
TITLE_STRIP = 50.0      # height of a view title under the drawing, points
TITLE_LEFT = 35.0       # bubble and gap left of the title text, plus the rule's overhang, points
VIEW_PAD = 6.0          # padding inside a view cell, points


def title_lines(title: str, subtitle: str, scale_label: str, width: float):
    """The view title strip wrapped to `width` points of text: (title lines, scale lines),
    or None when it does not fit the strip at that width.

    A long title wraps to two lines; a subtitle that does not fit on the scale
    line takes a line of its own under it (one title line only). So a title
    follows the view's width instead of widening the cell.
    """
    tl = tm.wrap(tm.clean(title), width, 10.5, True)
    if len(tl) > 2 or any(tm.text_width(ln, 10.5, True) > width + 1e-6 for ln in tl):
        return None
    scale = f"SCALE: {scale_label}"
    one = scale + (f"   {subtitle}" if subtitle else "")
    if tm.text_width(tm.clean(one), 7.5) <= width + 1e-6:
        return tl, [one]
    if len(tl) == 1 and tm.text_width(scale, 7.5) <= width + 1e-6 \
            and tm.text_width(tm.clean(subtitle), 7.5) <= width + 1e-6:
        return tl, [scale, subtitle]
    return None


def title_width(lines) -> float:
    """Points a wrapped title strip spans, bubble included."""
    tl, sl = lines
    return TITLE_LEFT + max([tm.text_width(ln, 10.5, True) for ln in tl] +
                            [tm.text_width(tm.clean(ln), 7.5) for ln in sl])


#: Title-block fields and where each value comes from. QA checks that the
#: printed text of each field holds that value. The preparer statement is
#: optional: a jurisdiction may need none, or a professional prepares part.
TB_SOURCES = {"project": ("title",), "address": ("address",), "owner": ("owner",),
              "preparer": ("preparer", "name"), "date": ("date",), "status": ("status_label",),
              "statement": ("preparer", "statement")}
OPTIONAL_TB = ("statement",)


def title_block_scale(view_scales) -> str:
    """The scale the title block prints, from each view's printed scale.

    One scale shared by every view prints that scale. Views at different
    scales, or a mix of true-scale and N.T.S. views, print AS NOTED. A sheet
    with no views, or only N.T.S. views, prints N.T.S.
    """
    labels = set(view_scales)
    if not labels:
        return NTS.label
    return labels.pop() if len(labels) == 1 else "AS NOTED"


class Sheet:
    """One drawing sheet. Create it with kit.sheet('A-1') inside a sheet script."""

    def __init__(self, kit, sid: str, title: str | None = None, subtitle: str | None = None,
                 size: str | None = None, orientation: str | None = None):
        self.kit = kit
        self.project = kit.project
        entry = next((s for s in self.project.sheets if s["id"] == sid), None)
        if entry is None:
            raise LayoutError(f"sheet {sid} is not listed in project.json sheets")
        self.id = sid
        self.title = title or entry["title"]
        self.subtitle = subtitle if subtitle is not None else entry.get("subtitle", "")
        self.size_name = size or self.project.sheet_size
        w, h = SHEET_SIZES[self.size_name]
        orient = orientation or self.project.orientation
        if orient == "portrait":
            w, h = h, w
        self.w_in, self.h_in = w, h
        self.page = Page(sid, w * PT_PER_IN, h * PT_PER_IN)
        self.page.title = self.title
        self.views: list[View] = []
        self.cells: list[tuple] = []          # (region id, box in points)
        self.notes_items: list = []
        self.notes_title = "GENERAL NOTES"
        self.layout_issues: list[str] = []
        self.text_over_geometry: list[dict] = []
        self.tb: dict = {}
        self.stamp_box = None
        self._panels = 0
        self._finished = False
        self._key_plan = None
        self._side = None
        self.slots: dict = {}
        # column and drawing area, in points
        P = PT_PER_IN
        self.col_w = min(8.0, max(3.5, w * 0.22)) * P
        self.border = (BORDER * P, BORDER * P, (w - BORDER) * P, (h - BORDER) * P)
        self.col = (self.border[2] - self.col_w, self.border[1], self.border[2], self.border[3])
        self.da = (self.border[0] + GUTTER * P, self.border[1] + GUTTER * P,
                   self.col[0] - GUTTER * P, self.border[3] - GUTTER * P)

    # ---- placement

    @property
    def drawing_area_in(self):
        """Width and height of the drawing area, inches."""
        return ((self.da[2] - self.da[0]) / PT_PER_IN, (self.da[3] - self.da[1]) / PT_PER_IN)

    def _cell(self, cell, rid: str):
        if cell is None:
            box = self.da
        else:
            x, y, cw, ch = cell
            box = (self.da[0] + x * PT_PER_IN, self.da[1] + y * PT_PER_IN,
                   self.da[0] + (x + cw) * PT_PER_IN, self.da[1] + (y + ch) * PT_PER_IN)
        if not box_inside(box, self.da, tol=0.01):
            dw, dh = self.drawing_area_in
            raise LayoutError(f"{self.id}: cell {cell} (inches) leaves the drawing area, "
                              f"which is {dw:.2f} x {dh:.2f} in")
        for other, obox in self.cells:
            if boxes_overlap(box, obox, tol=0.01):
                raise LayoutError(f"{self.id}: cell {cell} for {rid} overlaps {other}")
        return box

    def view(self, title: str, scale: str, extents, cell=None, number=None, align: str = "center",
             scale_bar: bool = True, subtitle: str = "") -> View:
        """Place a drawing at a true scale and return its View.

        title    view title printed under the drawing
        scale    printed scale label, e.g. '1/2" = 1\\'-0"' or '1/2'
        extents  (x0, y0, x1, y1) real inches the view shows. Include room for
                 dimensions and labels; everything drawn must stay in the cell.
        cell     (x, y, w, h) inches from the drawing-area lower-left. Default: all of it.
        number   view number in the title bubble. Default: next number.
        align    'center' (default), 'tl' (top left), 'top' (centred, at the top
                 of the cell) or 'bottom' (centred, title at the foot of the
                 cell, so the titles of a row line up).
        A title wider than the cell wraps to two lines, and a long subtitle
        takes its own line; a strip that still does not fit raises LayoutError.
        """
        number = number if number is not None else len(self.views) + 1
        rid = f"view:{number}"
        if scale == "fit":
            scale = self.largest_scale(extents, cell)
        sc = get_scale(scale)
        box = self._cell(cell, rid)
        x0, y0, x1, y1 = (float(v) for v in extents)
        if x1 <= x0 or y1 <= y0:
            raise LayoutError(f"{self.id}: view {title!r} extents must run low to high: {extents}")
        avail_w, avail_h = self._room(box)
        if sc.is_true:
            s = sc.pt_per_in
            need_w, need_h = (x1 - x0) * s, (y1 - y0) * s
            if need_w > avail_w + 1e-6 or need_h > avail_h + 1e-6:
                best = self._best_scale((x0, y0, x1, y1), box, family=sc)
                hint = (f" The largest standard scale that fits this cell is {best}."
                        if best else " No standard scale of this family fits this cell.")
                # scale="fit" searches architectural scales only (labels ending 1'-0").
                fit = ' (or pass scale="fit")' if sc.label.endswith("1'-0\"") else ""
                raise ScaleError(
                    f"{self.id}: view {title!r} at {sc.label} needs {need_w / 72:.2f} x {need_h / 72:.2f} in "
                    f"of paper for extents {fmt_in(x1 - x0)} x {fmt_in(y1 - y0)}, but the cell holds "
                    f"{avail_w / 72:.2f} x {avail_h / 72:.2f} in after its title.{hint} Use a smaller scale, a "
                    f"bigger cell, or tighter extents{fit}. The kit never shrinks a view.")
            nts = None
        else:
            nts = min(avail_w / (x1 - x0), avail_h / (y1 - y0))
            s = nts
            need_w, need_h = (x1 - x0) * s, (y1 - y0) * s
        group_h = need_h + TITLE_STRIP
        if align not in ("center", "tl", "top", "bottom"):
            raise ValueError("align must be 'center', 'tl', 'top' or 'bottom'")
        pad = VIEW_PAD
        lines = title_lines(title, subtitle, sc.printed, box[2] - box[0] - 2 * pad - TITLE_LEFT)
        if lines is None:
            raise LayoutError(f"{self.id}: the title of view {title!r} (with its scale line and subtitle) does "
                              f"not fit a {(box[2] - box[0]) / 72:.2f} in. wide cell in two lines; shorten the "
                              "title or subtitle, or widen the cell")
        tw = title_width(lines)
        if align == "center":
            ox = box[0] + (box[2] - box[0] - need_w) / 2
            top = box[3] - (box[3] - box[1] - group_h) / 2
        elif align == "tl":
            ox = box[0] + pad
            top = box[3] - pad
        elif align == "top":
            ox = box[0] + (box[2] - box[0] - need_w) / 2
            top = box[3] - pad
        else:
            # centre the drawing and its title together, so a long title stays in the cell
            ox = box[0] + max(pad, (box[2] - box[0] - max(need_w, tw)) / 2)
            top = box[1] + pad + group_h
        # the title starts under the drawing, moved left only as far as it must to stay in the cell
        tx = max(box[0] + pad, min(ox, box[2] - pad - tw))
        oy = top - need_h
        self.cells.append((rid, box))     # only a view that fits takes its cell
        v = View(self.page, rid, title, sc, (x0, y0, x1, y1), (ox, oy), box, self.project,
                 nts_factor=nts, number=number)
        v.subtitle = subtitle
        # A larger standard scale of the same kind that fits this cell, for QA's
        # view_scale advisory (layout.arrange clears it: it chose from its ladder).
        v.fits_larger = None
        if sc.is_true:
            best = self._best_scale((x0, y0, x1, y1), box, family=sc)
            if best and get_scale(best).pt_per_in > sc.pt_per_in * (1 + 1e-6):
                v.fits_larger = best
        self._view_title(v, tx, oy - 12, scale_bar, lines)
        self.views.append(v)
        return v

    @staticmethod
    def _room(box):
        """Paper points a view may fill in a cell: the cell less padding and the title strip."""
        return box[2] - box[0] - 2 * VIEW_PAD, box[3] - box[1] - TITLE_STRIP - 2 * VIEW_PAD

    def _best_scale(self, extents, box, family):
        """The largest standard scale of `family`'s kind at which extents fit the box, or None.

        Kinds: architectural (labels ending 1'-0"), engineering site scales
        (1" = 10'-0" and up) and the size scales FULL SIZE and HALF SIZE. A
        size scale is a detail scale: a FULL SIZE view that does not fit is
        offered HALF SIZE or an architectural scale, never a site scale. An
        architectural family stays architectural, so scale="fit" never picks a
        size scale.
        """
        x0, y0, x1, y1 = (float(v) for v in extents)
        avail_w, avail_h = self._room(box)
        kinds = {"arch": ("arch",), "eng": ("eng",), "size": ("size", "arch")}[scale_kind(family)]
        best = None
        for sc in SCALES.values():
            if not sc.is_true or scale_kind(sc) not in kinds:
                continue
            s = sc.pt_per_in
            if (x1 - x0) * s <= avail_w + 1e-6 and (y1 - y0) * s <= avail_h + 1e-6:
                # on a tie (HALF SIZE and 6" = 1'-0") a detail keeps the size name
                if best is None or s > best.pt_per_in + 1e-9 or (
                        abs(s - best.pt_per_in) <= 1e-9 and scale_kind(sc) == "size"):
                    best = sc
        return best.label if best else None

    def largest_scale(self, extents, cell=None, engineering: bool = False) -> str:
        """The largest standard scale at which `extents` fit `cell`, as its label.

        Architectural scales (1/8" = 1'-0" up to 6" = 1'-0") by default;
        engineering scales (1" = 10'-0" and up) with engineering=True. Use it
        to plan a sheet, or pass scale="fit" to sh.view(). The result is still a
        true, printed scale; the kit only picks which one.
        """
        box = self._cell(cell, "largest_scale")
        fam = get_scale('1" = 10\'-0"') if engineering else get_scale('1/4" = 1\'-0"')
        best = self._best_scale(extents, box, family=fam)
        if best is None:
            raise ScaleError(f"{self.id}: extents {extents} fit no standard scale in cell {cell}")
        return best

    def _view_title(self, v: View, x, y_top, scale_bar: bool, lines=None):
        r = 11.0
        cx, cy = x + r, y_top - r
        v.paper_path(circle_segments(cx, cy, r), stroke=INK, width=1.2, fill=WHITE, layer="annot")
        v.paper_text(cx, cy - 4.0, str(v.number), size=11, bold=True, anchor="middle",
                     role="view.number", collide=False)
        tx = cx + r + 7
        label = v.scale.printed
        if lines is None:
            lines = ([v.title], [f"SCALE: {label}" + (f"   {v.subtitle}" if v.subtitle else "")])
        tl, sl = lines
        right = tx
        for i, ln in enumerate(tl):
            t = v.paper_text(tx, cy + 1 - 11.0 * i, ln, size=10.5, bold=True, role="view.title")
            right = max(right, t["bbox"][2])
        y_rule = cy - 3.5 - 11.0 * (len(tl) - 1)
        recs = []
        for i, ln in enumerate(sl):
            if i == 0:
                recs.append(v.paper_text(tx, y_rule - 7.0, ln, size=7.5, color=INK2, role="view.scale",
                                         meta={"scale": label}))
            else:
                recs.append(v.paper_text(tx, y_rule - 7.0 - 9.0 * i, ln, size=7.5, color=INK2,
                                         role="view.subtitle"))
        right = max([right] + [rc["bbox"][2] for rc in recs])
        v.paper_path([("M", tx, y_rule), ("L", right + 6, y_rule)], stroke=INK, width=0.8,
                     layer="annot")
        if scale_bar and v.scale.is_true:
            bar_x = right + 26
            ft_pt = 12 * v.s
            if bar_x + auto_bar_feet(v) * ft_pt + 40 < v.cell[2]:
                px, py = bar_x, cy - 9
                rx, ry = v.x0 + (px - v.ox) / v.s, v.y0 + (py - v.oy) / v.s
                draw_scale_bar(v, (rx, ry))

    def panel(self, cell, title: str | None = None) -> "Panel":
        """A text panel (tables, schedules, note blocks) in a cell, in inches."""
        self._panels += 1
        rid = f"panel:{self._panels}"
        box = self._cell(cell, rid)
        self.cells.append((rid, box))
        p = Panel(self, rid, box)
        if title:
            p.heading(title)
        return p

    def slot(self, name: str, cell, title: str | None = None, placeholder: str | None = None) -> "Slot":
        """Reserve a named region of the drawing area for a picture or a block drawn later.

        A title sheet uses slots for its rendering and vicinity map. The slot
        takes its cell like a panel, draws a light frame and its title, and
        prints `placeholder` (default "<TITLE> TO BE PLACED") until something
        marks it filled (`slot.filled = True`, which an image placement does).
        `slot.image_cell` is the cell inside the frame and title, in inches.
        """
        if name in self.slots:
            raise LayoutError(f"{self.id}: slot {name!r} is already placed")
        rid = f"slot:{name}"
        box = self._cell(cell, rid)
        self.cells.append((rid, box))
        sl = Slot(self, name, rid, tuple(cell), box, title, placeholder)
        self.slots[name] = sl
        return sl

    def connection(self, cid: str, cell) -> "Slot":
        """The labeled spot for a load-carrying connection in project.json `connections`.

        A framed block titled CONNECTION <id> that prints what the connection
        joins, its design load (only with the load's `cd`), and its basis: the
        maker's tested detail or an engineer's calculation, with the evidence.
        While the basis is `open` it prints that one of the two is to be placed
        there, so the sheet never shows a load-carrying connection as settled.
        Place the maker's detail drawing or the engineer's sketch in
        `slot.image_cell` (sh.place_image) once it arrives. Tag the connection
        on the drawing with symbols.tag(v, at, "<id>", shape="diamond") and a
        leader, or a note naming it.
        kit-elevations-sections.md, "Connections that carry a load".
        """
        try:
            entry = self.project.item("connections", cid)
        except KeyError:
            raise LayoutError(f"{self.id}: connection {cid!r} is not in project.json connections") from None
        sl = self.slot(f"connection-{cid}", cell, title=f"CONNECTION {cid}")
        x0, y0, x1, y1 = sl.image_box
        width = x1 - x0 - 4
        y = y1 - 2
        basis = {"manufacturer": "BASIS: MANUFACTURER'S TESTED DETAIL. ",
                 "engineer": "BASIS: ENGINEER'S CALCULATION. "}.get(entry["basis"], "")
        rows = [(entry["what"], 8.0, True, ())]
        if entry.get("load"):
            rows.append(("DESIGN LOAD: " + entry["load"], 7.5, False, (entry["cd"],) if entry.get("cd") else ()))
        if basis:
            rows.append((basis + entry.get("evidence", ""), 7.5, False, ()))
        for text, size, bold, cd in rows:
            for ln in tm.wrap(tm.clean(text), width, size, bold):
                y -= size * 1.3
                if y < y0:
                    raise LayoutError(f"{self.id}: connection {cid} text does not fit its cell; give it a bigger "
                                      "cell or shorten `what`, `load` or `evidence`")
                self.page.text(x0 + 2, y, ln, size=size, bold=bold, region=sl.id, role="connection",
                               meta={"connection": cid}, cd=cd)
        y -= 4
        need = 0.0
        if entry["basis"] == "open":
            sl.placeholder = ("MANUFACTURER'S TESTED DETAIL (WITH ITS EVALUATION REPORT AND RATED LOAD) "
                              "OR AN ENGINEER'S CALCULATION TO BE PLACED HERE")
            need = len(Slot.placeholder_lines(sl.placeholder, x1 - x0)) * 9.0 + 8.0
        else:
            sl.filled = True
        if y - y0 < need:
            raise LayoutError(f"{self.id}: connection {cid} needs a taller cell: its text and the space for the "
                              "detail or calculation do not fit")
        sl.image_box = (x0, y0, x1, y)
        sl.image_cell = (sl.image_cell[0], sl.image_cell[1], sl.image_cell[2], (y - y0) / PT_PER_IN)
        return sl

    def key_plan(self, draw, extents, height_in: float = 1.7) -> None:
        """A key plan in the title block: `draw(view)` draws it, not to scale, into a
        View that fits `extents` (real inches) in a box `height_in` tall.

        The key plan prints no scale and does not change the sheet scale. Draw
        the building outline light and the area of work in solid poche.
        """
        self._key_plan = {"draw": draw, "extents": tuple(float(e) for e in extents),
                          "height": height_in * PT_PER_IN}

    def _draw_key_plan(self, box):
        x0, y0, x1, y1 = self._key_plan["extents"]
        bw, bh = box[2] - box[0], box[3] - box[1]
        f = min(bw / (x1 - x0), bh / (y1 - y0))
        ox = box[0] + (bw - (x1 - x0) * f) / 2
        oy = box[1] + (bh - (y1 - y0) * f) / 2
        kv = View(self.page, "tb", "KEY PLAN", NTS, (x0, y0, x1, y1), (ox, oy), box, self.project,
                  nts_factor=f, number=0)
        self._key_plan["draw"](kv)

    def side_panel(self, title: str | None = None) -> "Panel":
        """A panel in the right column above the title block.

        Use it for a legend, a materials key, keynotes or a short schedule, so
        the column is not left empty. On a sheet with general notes, call
        sh.notes() first: the panel then takes the column below the notes.
        Call key_plan() first if the sheet has one.
        """
        if self._side is not None:
            return self._side
        saved = (dict(self.tb), self.stamp_box, getattr(self, "scale_text", None))
        tb_top = self._title_block(measure=True)
        self.tb, self.stamp_box, self.scale_text = saved
        top = self.col[3] - 6
        if self.notes_items:
            top = self._notes(tb_top, draw=False) - 6
            if top - (tb_top + 6) < 72:
                raise LayoutError(f"{self.id}: the general notes leave less than 1 in. for the side panel; "
                                  "shorten the notes or move the panel's content into a drawing-area panel")
        box = (self.col[0] + 6, tb_top + 6, self.col[2] - 6, top)
        rid = "panel:side"
        self.cells.append((rid, box))
        self._side = Panel(self, rid, box)
        self._side_top = tb_top
        self._side_notes = list(self.notes_items)
        if title:
            self._side.heading(title)
        return self._side

    def place_image(self, cell, image_id: str, **kw):
        """Place a project.json image by id in its own cell, with its caption and
        source label. See images.place and references/images-and-finishes.md."""
        from .images import place
        return place(self, cell, image_id, **kw)

    def notes(self, items, title: str = "GENERAL NOTES") -> None:
        """Numbered notes for the column above the title block. Blank items add space.
        With a side panel, call this before sh.side_panel()."""
        if self._side is not None:
            raise LayoutError(f"{self.id}: call sh.notes() before sh.side_panel(); the side panel goes "
                              "below the notes")
        self.notes_items = list(items)
        self.notes_title = title

    def claim(self, template: str, depends_on=(), cd=()):
        """A compliance note. Refused if it rests on an unverified value."""
        return self.kit.claim(template, depends_on, cd)

    def sheet_index(self, panel: "Panel", grid: bool = False, size: float = 7.5) -> None:
        """Write the sheet index from project.json into a panel, in bound order.

        grid=True draws it as a ruled grid_table, as on a professional cover.
        The SHEET column widens with `size`, so a cover sheet at size 10 still fits.
        """
        rows = [[s["id"], s["title"]] for s in self.project.sheets]
        meta = [{"sheet_id": s["id"], "order": i} for i, s in enumerate(self.project.sheets)]
        sheet_w = (0.8 if grid else 0.9) * size / 7.5
        if grid:
            panel.grid_table([("SHEET", sheet_w), ("TITLE", None, "wrap")], rows, size=size, role="index",
                             row_meta=meta)
        else:
            panel.table([("SHEET", sheet_w), ("TITLE", None)], rows, size=size, role="index", row_meta=meta)

    # ---- finish

    def finish(self) -> Page:
        if self._finished:
            return self.page
        self._finished = True
        pg = self.page
        P = PT_PER_IN
        b = self.border
        pg.path(rect_segments(*b), stroke=INK, width=2.0, layer="frame", region="frame")
        pg.path([("M", self.col[0], b[1]), ("L", self.col[0], b[3])], stroke=INK, width=1.2,
                layer="frame", region="frame")
        for sl in self.slots.values():
            sl._finish()
        tb_top = self._title_block()
        self._notes(tb_top)
        for v in self.views:
            ink = pg.ink_box(region=v.id)
            if ink and not box_inside(ink, v.cell, tol=0.5):
                over = (max(0, v.cell[0] - ink[0]), max(0, v.cell[1] - ink[1]),
                        max(0, ink[2] - v.cell[2]), max(0, ink[3] - v.cell[3]))
                self.layout_issues.append(
                    f"view {v.number} '{v.title}' draws outside its cell by "
                    f"left {over[0] / P:.2f}, bottom {over[1] / P:.2f}, right {over[2] / P:.2f}, "
                    f"top {over[3] / P:.2f} in. Widen the extents or the cell")
        self.text_over_geometry = text_over_geometry(pg)
        return pg

    def _tb_text(self, field, x, y, s, **kw):
        kw.setdefault("region", "tb")
        kw.setdefault("layer", "frame_text")
        rec = self.page.text(x, y, s, role=f"tb.{field}", **kw)
        self.tb[field] = (self.tb.get(field, "") + " " + rec["s"]).strip()
        return rec

    def _title_block(self, measure: bool = False) -> float:
        """Draw the title block at the foot of the right column. Returns its top, in points.

        A grid of boxed cells, top to bottom: preparer (firm) and project;
        revisions and the key plan; sheet title and the large sheet number;
        scale, date and status; preparer statement, signature and the stamp
        box. A narrow column stacks the paired cells.
        """
        pg = self.page
        meta = self.project.meta
        x0, x1 = self.col[0], self.col[2]
        pad = 9.0
        W = x1 - x0
        paired = W >= 400
        LABEL = dict(size=6.0, color=GREY, tracking=0.7)

        def wrap(text, size, bold=False, width=None):
            return tm.wrap(tm.clean(text), width, size, bold)

        def label(x, y, s, field):
            self._tb_text(field, x, y, s, **LABEL)

        # ---- cell builders: each returns (height, draw(cx0, cx1, top))
        prep = meta["preparer"]

        def c_preparer(cw):
            tw = cw - 2 * pad
            name = wrap(prep["name"], 9.5, True, tw)
            role = wrap(prep["role"], 7, False, tw) if prep.get("role") else []
            info = []
            for k in ("firm", "address", "phone", "email", "license"):
                if prep.get(k):
                    info += wrap(str(prep[k]), 6.8, False, tw)
            h = 14 + 11.5 * len(name) + 9 * len(role) + 8.4 * len(info) + 6

            def draw(cx0, cx1, top):
                label(cx0 + pad, top - 10, "PREPARED BY", "preparer_label")
                y = top - 22
                for ln in name:
                    self._tb_text("preparer", cx0 + pad, y, ln, size=9.5, bold=True)
                    y -= 11.5
                for ln in role:
                    self._tb_text("preparer", cx0 + pad, y + 1, ln, size=7, color=INK2)
                    y -= 9
                for ln in info:
                    self._tb_text("preparer_info", cx0 + pad, y + 1, ln, size=6.8, color=INK2)
                    y -= 8.4
            return h, draw

        def c_project(cw):
            tw = cw - 2 * pad
            title = wrap(meta["title"], 10.5, True, tw)
            addr = wrap(meta["address"], 7.5, False, tw)
            people = [("owner", f"OWNER: {meta['owner']}")]
            if meta.get("contractor"):
                people.append(("contractor", f"CONTRACTOR: {meta['contractor']}"))
            for k, lab in (("apn", "APN"), ("permit_no", "PERMIT NO.")):
                if meta.get(k):
                    people.append((k, f"{lab}: {meta[k]}"))
            plines = [(f, ln) for f, t in people for ln in wrap(t, 6.8, False, tw)]
            if not paired:
                plines.append(("preparer", f"PREPARED BY: {prep['name']}" + (f" ({prep['role']})" if prep.get("role") else "")))
            h = 14 + 12.5 * len(title) + 9.5 * len(addr) + 8.6 * len(plines) + 6

            def draw(cx0, cx1, top):
                label(cx0 + pad, top - 10, "PROJECT", "project_label")
                y = top - 22.5
                for ln in title:
                    self._tb_text("project", cx0 + pad, y, ln, size=10.5, bold=True)
                    y -= 12.5
                for ln in addr:
                    self._tb_text("address", cx0 + pad, y + 1, ln, size=7.5)
                    y -= 9.5
                for f, ln in plines:
                    self._tb_text(f, cx0 + pad, y, ln, size=6.8, color=INK2)
                    y -= 8.6
            return h, draw

        revs = self.project.revisions

        def c_revisions(cw):
            tw = cw - 2 * pad
            dx, desc_x = 26.0, 80.0
            rows = []
            for r in revs:
                lines = wrap(str(r["desc"]), 6.8, False, tw - desc_x)
                rows.append((r, lines))
            n = sum(max(1, len(ls)) for _, ls in rows) or 1
            h = 31 + 9.2 * n + 4

            def draw(cx0, cx1, top):
                label(cx0 + pad, top - 10, "REVISIONS", "revisions")
                hy = top - 21
                for x, t in ((cx0 + pad, "REV"), (cx0 + pad + dx, "DATE"), (cx0 + pad + desc_x, "DESCRIPTION")):
                    self._tb_text("revisions_head", x, hy, t, size=5.6, color=INK2, bold=True, tracking=0.4)
                pg.path([("M", cx0 + pad, hy - 3), ("L", cx1 - pad, hy - 3)], stroke=LIGHT, width=0.5,
                        layer="frame", region="tb")
                y = hy - 12.5
                if not rows:
                    self._tb_text("revisions", cx0 + pad + desc_x, y, "NONE", size=6.8, color=INK2)
                for r, lines in rows:
                    delta(pg, cx0 + pad + 7, y + 2.4, r["delta"], size=9, region="tb", layer="frame")
                    self._tb_text("revision", cx0 + pad + dx, y, str(r["date"]), size=6.8, color=INK2)
                    for i, ln in enumerate(lines or [""]):
                        if ln:
                            self._tb_text("revision", cx0 + pad + desc_x, y - 9.2 * i, ln, size=6.8, color=INK2)
                    y -= 9.2 * max(1, len(lines))
            return h, draw

        def c_keyplan(cw):
            h = self._key_plan["height"]

            def draw(cx0, cx1, top):
                label(cx0 + pad, top - 10, "KEY PLAN", "key_plan_label")
                self._draw_key_plan((cx0 + pad, top - h + pad, cx1 - pad, top - 16))
            return h, draw

        title_lines = None
        id_w = 150.0 if paired else min(130.0, W * 0.42)

        def c_title(cw):
            nonlocal title_lines
            tw = cw - 2 * pad
            title_lines = wrap(self.title, 14, True, tw)
            sub = wrap(self.subtitle, 7.5, False, tw) if self.subtitle else []
            h = max(78.0, 22 + 16 * len(title_lines) + 9.5 * len(sub) + 8)

            def draw(cx0, cx1, top):
                label(cx0 + pad, top - 10, "SHEET TITLE", "sheet_title_label")
                y = top - 26
                for ln in title_lines:
                    self._tb_text("sheet_title", cx0 + pad, y, ln, size=14, bold=True)
                    y -= 16
                for ln in sub:
                    self._tb_text("subtitle", cx0 + pad, y + 4, ln, size=7.5, color=INK2)
                    y -= 9.5
            return h, draw

        idx = [s["id"] for s in self.project.sheets].index(self.id)
        id_size = 34.0
        while id_size > 14 and tm.text_width(self.id, id_size, True) > id_w - 14:
            id_size -= 1

        def c_sheet_id(cw):
            def draw(cx0, cx1, top):
                cx = (cx0 + cx1) / 2
                self._tb_text("sheet_label", cx, top - 10, "SHEET", anchor="middle", **LABEL)
                self._tb_text("sheet_id", cx, top - 20 - id_size * 0.78, self.id, size=id_size, bold=True,
                              anchor="middle")
                self._tb_text("sheet_count", cx, top - 22 - id_size * 0.78 - 11,
                              f"{idx + 1} OF {len(self.project.sheets)}", size=6.5, color=INK2, anchor="middle")
            return 30 + id_size * 0.78 + 14, draw

        scale_text = title_block_scale(v.scale.printed for v in self.views)
        self.scale_text = scale_text

        def c_field(field, lab, value, size=8.5, bold=True):
            def mk(cw):
                lines = wrap(value, size, bold, cw - 2 * pad)

                def draw(cx0, cx1, top):
                    label(cx0 + pad, top - 10, lab, field + "_label")
                    y = top - 22
                    for ln in lines:
                        self._tb_text(field, cx0 + pad, y, ln, size=size, bold=bold)
                        y -= size * 1.2
                return 16 + size * 1.2 * len(lines) + 4, draw
            return mk

        status_lines = None

        def c_status(cw):
            nonlocal status_lines
            status_lines = wrap(meta["status_label"], 8, True, cw - 2 * pad)

            def draw(cx0, cx1, top):
                y = top - 12.5
                for ln in status_lines:
                    self._tb_text("status", cx0 + pad, y, ln, size=8, bold=True, color=DIM)
                    y -= 10
            return 8 + 10 * len(status_lines) + 2, draw

        def c_statement(cw):
            tw = cw - 2 * pad
            stmt = wrap(prep["statement"], 6.5, False, tw) if prep.get("statement") else []
            sig = "SIGNATURE ________________________   DATE _________"
            sig_lines = wrap(sig, 7, False, tw)
            h = 12 + 8.2 * len(stmt) + (6 if stmt else 0) + 11 * len(sig_lines) + 8

            def draw(cx0, cx1, top):
                y = top - 11
                for ln in stmt:
                    self._tb_text("statement", cx0 + pad, y, ln, size=6.5, color=INK2)
                    y -= 8.2
                y -= 12 if stmt else 14
                for ln in sig_lines:
                    self._tb_text("signature", cx0 + pad, y, ln, size=7, color=INK2)
                    y -= 11
            return h, draw

        stamp_h = 1.5 * PT_PER_IN

        def c_stamp(cw):
            def draw(cx0, cx1, top):
                sx0, sy0, sx1, sy1 = cx0 + pad, top - stamp_h + pad, cx1 - pad, top - pad
                pg.path(rect_segments(sx0, sy0, sx1, sy1), stroke=LIGHT, width=0.8, layer="frame", region="tb")
                self.stamp_box = (sx0, sy0, sx1, sy1)
                self._tb_text("stamp", (sx0 + sx1) / 2, sy1 - 10,
                              meta.get("stamp_label", "RESERVED FOR AGENCY STAMPS"), size=6.0, color=GREY,
                              anchor="middle", tracking=0.6)
            return stamp_h, draw

        # ---- the grid: rows of (width share or fixed points, builder)
        half = W / 2
        grid = []
        if paired:
            grid.append([(half, c_preparer), (None, c_project)])
        else:
            grid.append([(None, c_project)])
        if self._key_plan and paired:
            grid.append([(W * 0.58, c_revisions), (None, c_keyplan)])
        else:
            grid.append([(None, c_revisions)])
            if self._key_plan:
                grid.append([(None, c_keyplan)])
        grid.append([(W - id_w, c_title), (None, c_sheet_id)])
        grid.append([(half * 0.62 if paired else W * 0.5, c_field("scale", "SCALE", scale_text, 9.5)),
                     (half * 0.38 if paired else None, c_field("date", "DATE", meta["date"], 8.5, False))] +
                    ([(None, c_status)] if paired else []))
        if not paired:
            grid.append([(None, c_status)])
        if paired:
            grid.append([(half, c_statement), (None, c_stamp)])
        else:
            grid.append([(None, c_statement)])
            grid.append([(None, c_stamp)])

        built = []
        for row in grid:
            fixed = sum(w for w, _ in row if w)
            free = [i for i, (w, _) in enumerate(row) if not w]
            rest = (W - fixed) / max(1, len(free))
            xs, cells = x0, []
            for w, fn in row:
                cw = w or rest
                h, draw = fn(cw)
                cells.append((xs, xs + cw, h, draw))
                xs += cw
            built.append((max(c[2] for c in cells), cells))

        total = sum(h for h, _ in built)
        bottom = self.col[1]
        top = bottom + total
        if measure:
            return top
        if top > self.col[3] - 60:
            raise LayoutError(f"{self.id}: title block is {total / 72:.2f} in tall and leaves no room for notes")
        pg.path(rect_segments(x0, bottom, x1, top), stroke=INK, width=2.0, layer="frame", region="tb")
        y = top
        for ri, (h, cells) in enumerate(built):
            for ci, (cx0, cx1, _h, draw) in enumerate(cells):
                draw(cx0, cx1, y)
                if ci:
                    pg.path([("M", cx0, y), ("L", cx0, y - h)], stroke=INK, width=0.8, layer="frame", region="tb")
            y -= h
            if ri < len(built) - 1:
                pg.path([("M", x0, y), ("L", x1, y)], stroke=INK, width=0.8, layer="frame", region="tb")
        self.tb_box = (x0, bottom, x1, top)
        return top

    def _notes(self, tb_top: float, draw: bool = True) -> float:
        """Draw the general notes (or, with draw=False, only measure them). Returns their bottom, points."""
        pg = self.page
        if draw and self._side is not None:
            if tb_top > self._side_top + 0.5:
                raise LayoutError(f"{self.id}: the title block grew after side_panel() was placed; call "
                                  "key_plan() before side_panel()")
            if self.notes_items != self._side_notes:
                raise LayoutError(f"{self.id}: the general notes changed after side_panel() was placed; call "
                                  "sh.notes() before sh.side_panel()")
        x0, x1 = self.col[0] + 12, self.col[2] - 12
        top = self.col[3] - 14
        bottom = tb_top if self._side is None else self._side.box[3] + 6
        if draw:
            self.notes_box = (self.col[0], bottom, self.col[2], self.col[3])
        if not self.notes_items:
            return top
        if draw:
            pg.text(x0, top - 12, self.notes_title, size=11, bold=True, tracking=0.8, region="notes",
                    layer="frame_text", role="notes.title")
            pg.path([("M", x0, top - 18), ("L", x1, top - 18)], stroke=INK, width=1.0, layer="frame",
                    region="notes")
        y = top - 34
        n = 0
        size, lead = 7.5, 9.6
        indent = 18.0
        for gi, item in enumerate(self.notes_items):
            if item is None or not str(item).strip():
                y -= lead * 0.6
                continue
            n += 1
            lines = tm.wrap(tm.clean(str(item)), x1 - x0 - indent, size)
            if y - lead * (len(lines) - 1) < bottom + 10:
                raise LayoutError(f"{self.id}: general notes overflow the column at note {n}. "
                                  "Move notes to a panel or a notes sheet; the kit never clips text")
            if draw:
                pg.text(x0, y, f"{n}.", size=size, bold=True, region="notes", layer="frame_text", role="notes")
            for li, ln in enumerate(lines):
                if draw:
                    pg.text(x0 + indent, y, ln, size=size, region="notes", layer="frame_text", role="notes",
                            meta={"group": f"note:{gi}"}, **first_line_marks(item, li == 0))
                y -= lead
            y -= lead * 0.45
        return y + lead * 0.45 + lead - 12.0      # last baseline, less its descent and a gap


class Slot:
    """A named region of a sheet, reserved with Sheet.slot()."""

    TITLE_H = 20.0

    def __init__(self, sheet, name, rid, cell, box, title, placeholder):
        self.sheet = sheet
        self.name = name
        self.id = rid
        self.cell = cell
        self.box = box
        self.title = title
        self.placeholder = placeholder
        self.filled = False
        th = self.TITLE_H if title else 0.0
        P = PT_PER_IN
        self.image_box = (box[0] + 4, box[1] + 4, box[2] - 4, box[3] - 4 - th)
        self.image_cell = (cell[0] + 4 / P, cell[1] + 4 / P, cell[2] - 8 / P, cell[3] - (8 + th) / P)

    @staticmethod
    def placeholder_lines(label: str, width: float) -> list[str]:
        """The placeholder wrapped to a frame `width` points wide (7 pt, tracked 0.6 pt)."""
        if tm.text_width(label, 7, tracking=0.6) <= width - 8:
            return [label]
        return tm.wrap(tm.clean(label), (width - 8) * 0.8, 7)

    def _finish(self):
        pg = self.sheet.page
        x0, y0, x1, y1 = self.box
        if self.title:
            pg.text(x0 + 4, y1 - 13, self.title, size=9.5, bold=True, tracking=0.5, region=self.id,
                    role="slot.title", meta={"slot": self.name})
            pg.path([("M", x0 + 4, y1 - 17), ("L", x1 - 4, y1 - 17)], stroke=INK, width=0.9, layer="annot",
                    region=self.id)
        if not self.filled:
            b = self.image_box
            pg.path(rect_segments(*b), stroke=LIGHT, width=0.6, dash=(4, 3), layer="annot", region=self.id)
            label = self.placeholder or f"{(self.title or self.name).upper()} TO BE PLACED"
            lines = self.placeholder_lines(label, b[2] - b[0])
            y = (b[1] + b[3]) / 2 - 3 + (len(lines) - 1) * 4.5
            for ln in lines:
                pg.text((b[0] + b[2]) / 2, y, ln, size=7, color=GREY, anchor="middle",
                        tracking=0.6, region=self.id, role="slot.placeholder", meta={"slot": self.name})
                y -= 9


class Panel:
    """A text panel that flows top to bottom inside a cell. Overflow raises."""

    def __init__(self, sheet: Sheet, rid: str, box):
        self.sheet = sheet
        self.page = sheet.page
        self.id = rid
        self.box = box
        self.pad = 6.0
        self.y = box[3] - self.pad
        self.x0 = box[0] + self.pad
        self.x1 = box[2] - self.pad
        self._groups = 0

    @property
    def width(self):
        return self.x1 - self.x0

    def _need(self, h):
        if self.y - h < self.box[1] + self.pad - 0.01:
            raise LayoutError(f"{self.sheet.id} {self.id}: content overflows the panel by "
                              f"{(self.box[1] + self.pad - (self.y - h)) / 72:.2f} in. Make the cell taller")

    def _t(self, x, y, s, **kw):
        kw.setdefault("region", self.id)
        kw.setdefault("role", "panel")
        return self.page.text(x, y, s, **kw)

    def _p(self, segs, **kw):
        return self.page.path(segs, layer="annot", region=self.id, **kw)

    def _rule(self, y, **kw):
        self._p([("M", self.x0, y), ("L", self.x1, y)], stroke=INK, **kw)

    def space(self, pt: float = 6.0):
        self.y -= pt

    def fit(self, gap: float = 0.3):
        """Shrink the panel to its content and return the cell left below it, in inches.

        Stack panels in a column so each is as tall as its text, with no empty
        boxes: `rest = d.fit(); z = sh.panel(rest, "ZONING")`. Returns None when
        less than `gap` is left. Call it after the panel's last line.
        """
        sh = self.sheet
        bottom = min(self.box[3], max(self.box[1], self.y - self.pad + 4))
        old = self.box
        self.box = (old[0], bottom, old[2], old[3])
        sh.cells = [(rid, self.box if rid == self.id else b) for rid, b in sh.cells]
        P = PT_PER_IN
        top = (bottom - sh.da[1]) / P - gap
        y0 = (old[1] - sh.da[1]) / P
        if top - y0 <= 0.05:
            return None
        return ((old[0] - sh.da[0]) / P, y0, (old[2] - old[0]) / P, top - y0)

    def heading(self, text: str, size: float = 10.5, rule: bool = True):
        self._need(size + 8)
        self._t(self.x0, self.y - size, text, size=size, bold=True, tracking=0.4, meta={"heading": True})
        self.y -= size + 5
        if rule:
            self._rule(self.y, width=0.8)
        self.y -= 8

    def banner(self, title: str, lines=(), size: float = 26.0):
        """Large title text for a cover sheet: the project name in bold, then
        smaller lines (address, scope in a few words). Pass kit.text lines to
        print model values. A banner line wider than the panel wraps."""
        for i, (text, sz, bold) in enumerate([(title, size, True)] + [(ln, size * 0.5, False) for ln in lines]):
            wrapped = tm.wrap(tm.clean(str(text)), self.width, sz, bold)
            self._need(sz * 1.2 * len(wrapped))
            self._groups += 1
            for li, ln in enumerate(wrapped):
                self._t(self.x0, self.y - sz, ln, size=sz, bold=bold, color=INK if bold else INK2,
                        meta={"group": f"{self.id}:{self._groups}"}, **first_line_marks(text, li == 0))
                self.y -= sz * 1.2
            self.y -= sz * (0.35 if i == 0 else 0.1)

    def para(self, text, size: float = 7.5, bold: bool = False, color=INK, lead: float = 1.28,
             indent: float = 0.0):
        lines = tm.wrap(tm.clean(str(text)), self.width - indent, size, bold)
        self._need(size * lead * len(lines))
        self._groups += 1
        g = f"{self.id}:{self._groups}"
        for i, ln in enumerate(lines):
            self._t(self.x0 + indent, self.y - size, ln, size=size, bold=bold, color=color,
                    meta={"group": g}, **first_line_marks(text, i == 0))
            self.y -= size * lead
        self.y -= size * 0.3

    def numbered(self, items, size: float = 7.5, start: int = 1):
        n = start
        for item in items:
            if item is None or not str(item).strip():
                self.y -= size * 0.6
                continue
            self._need(size * 1.3)
            self._t(self.x0, self.y - size, f"{n}.", size=size, bold=True)
            self.para(item, size=size, indent=16)
            n += 1

    def table(self, columns, rows, size: float = 7.5, role: str = "panel", row_meta=None,
              header: bool = True, lead: float = 1.55, bold_first: bool = True):
        """columns: [(title, width in inches or None for the rest[, "wrap"])].

        A plain cell never wraps or clips: one wider than its column raises
        LayoutError. A column marked "wrap" wraps its text onto more lines.
        """
        fixed = sum(c[1] * 72 for c in columns if c[1])
        free = [i for i, c in enumerate(columns) if not c[1]]
        rest = (self.width - fixed) / max(1, len(free))
        widths = [c[1] * 72 if c[1] else rest for c in columns]
        wraps = [len(c) > 2 and c[2] == "wrap" for c in columns]
        tags = [len(c) > 2 and c[2] == "tag" for c in columns]
        if any(tags):
            from .symbols import tag_radius
            rmax = max((tag_radius(_tag_parts(r[ci])[1], size) for r in rows for ci in range(len(r))
                        if tags[ci] and r[ci]), default=0.0)
            lead = max(lead, (2 * rmax + 3) / size)
        if rest < 0:
            raise LayoutError(f"{self.sheet.id} {self.id}: table columns are wider than the panel")
        xs = [self.x0]
        for w in widths[:-1]:
            xs.append(xs[-1] + w)
        rh = size * lead
        line_h = size * 1.2
        if header:
            self._need(rh * 1.4)
            for x, c in zip(xs, columns):
                if str(c[0]).strip():
                    self._t(x, self.y - size, c[0], size=size * 0.9, bold=True, color=INK2, tracking=0.3)
            self.y -= rh * 0.8
            self._rule(self.y, width=0.7)
            self.y -= rh * 0.55
        for ri, row in enumerate(rows):
            cells = []
            for ci, cell in enumerate(row):
                if cell is None or str(cell) == "":
                    cells.append([])
                    continue
                if tags[ci]:
                    cells.append(["__tag__"])
                    continue
                s = tm.clean(str(cell))
                if wraps[ci]:
                    cells.append(tm.wrap(s, widths[ci] - 6, size, bold_first and ci == 0))
                else:
                    if tm.text_width(s, size, bold_first and ci == 0) > widths[ci] - 4:
                        raise LayoutError(f"{self.sheet.id} {self.id}: table cell {s!r} is wider than its "
                                          f"{widths[ci] / 72:.2f} in column. Widen the column, mark it "
                                          "'wrap', or shorten the text")
                    cells.append([cell])
            n = max(1, max(len(c) for c in cells))
            self._need(rh + line_h * (n - 1))
            self._groups += 1
            meta = dict(row_meta[ri]) if row_meta else {}
            for ci, (x, lines) in enumerate(zip(xs, cells)):
                if lines == ["__tag__"]:
                    from .symbols import tag_paper
                    shape, mark = _tag_parts(row[ci])
                    tag_paper(self.page, x + widths[ci] / 2 - 2, self.y - size * 0.62, mark, shape, size,
                              region=self.id, role=role)
                    continue
                for li, ln in enumerate(lines):
                    m = dict(meta)
                    m["group"] = f"{self.id}:r{self._groups}:c{ci}"
                    src = row[ci]
                    # the first line of a cell carries its keys, FV tags and claim, also when it wraps
                    self._t(x, self.y - size - li * line_h, ln, size=size, bold=(bold_first and ci == 0), role=role,
                            meta=m, **first_line_marks(src, li == 0))
            self.y -= rh + line_h * (n - 1)
            # a hairline under each row, below the last baseline
            rule = self.y + rh - size - 3.0
            last = ri == len(rows) - 1
            self._p([("M", self.x0, rule), ("L", self.x1, rule)], stroke=INK if last else LIGHT,
                    width=0.7 if last else 0.35)
        self.y -= 4

    def legend(self, rows, size: float = 7.5, swatch: float = 0.45):
        """Graphic legend. rows: [(kind, label)]. Kinds: poche_e, poche_n, demo,
        measured, assumed, hatch, light, recept, switch, smoke, smoke_co, leg, fv, cloud,
        property_line, setback, "hatch:<material>" (a hatch.MATERIALS pattern),
        "pen:<name>" (a pens.PENS line) and "tag:<shape>:<mark>" (a symbols tag,
        e.g. "tag:hex:W-1")."""
        sw = swatch * 72
        rh = max(size * 1.9, 15.0)
        for kind, label in rows:
            self._need(rh)
            self.page.legend_kinds.append(kind)
            x, ymid = self.x0, self.y - rh / 2
            y0, y1 = ymid - 5, ymid + 5
            box = rect_segments(x, y0, x + sw, y1)
            if kind == "poche_e":
                self._p(box, stroke=INK, width=0.9, fill=POCHE_E)
            elif kind == "poche_n":
                self._p(box, stroke=INK, width=0.9, fill=POCHE_N)
            elif kind == "demo":
                self._p(box, stroke=INK, width=0.9, dash=(5, 3))
            elif kind == "measured":
                self._p([("M", x, ymid), ("L", x + sw, ymid)], stroke=INK, width=1.3)
            elif kind == "assumed":
                self._p([("M", x, ymid), ("L", x + sw, ymid)], stroke=GREY, width=1.3, dash=(6, 3))
            elif kind == "hatch":
                self._p(box, stroke=INK, width=0.8)
                segs = []
                k = -10.0
                while k < sw:
                    segs += [("M", x + k, y0), ("L", x + k + 10, y1)]
                    k += 4
                self._p(segs, stroke=INK, width=0.4, clip=box)
            elif kind in ("light", "smoke", "smoke_co", "recept"):
                cx = x + sw / 2
                r = {"light": 6.0, "smoke": 7.0, "smoke_co": 7.0, "recept": 3.6}[kind]
                self._p(circle_segments(cx, ymid, r), stroke=INK, width=0.9, fill=WHITE)
                if kind == "light":
                    self._p([("M", cx - 8, ymid), ("L", cx + 8, ymid), ("M", cx, ymid - 8), ("L", cx, ymid + 8)],
                            stroke=INK, width=0.9)
                elif kind == "recept":
                    self._p([("M", cx - 1.3, ymid - 5.5), ("L", cx - 1.3, ymid + 5.5), ("M", cx + 1.3, ymid - 5.5),
                             ("L", cx + 1.3, ymid + 5.5)], stroke=INK, width=0.8)
                else:
                    lab = "SD" if kind == "smoke" else "SD/CO"
                    self._t(cx, ymid - 2, lab, size=4.6 if kind == "smoke_co" else 5.5, bold=True,
                            anchor="middle", role="legend", collide=False)
            elif kind == "switch":
                self._t(x + sw / 2, ymid - 3.2, "S", size=9, bold=True, anchor="middle", role="legend")
            elif kind == "leg":
                self._p([("M", x, ymid - 3), ("C", x + sw / 3, ymid + 5, x + 2 * sw / 3, ymid + 5, x + sw, ymid - 3)],
                        stroke=INK2, width=0.6, dash=(3, 2.5))
            elif kind == "fv":
                self._p(box, stroke=DIM, width=0.8, fill=WHITE)
                self._t(x + sw / 2, ymid - 2.4, "FV-#", size=6.5, bold=True, anchor="middle", color=DIM,
                        role="legend")
            elif kind == "property_line":
                self._p([("M", x, ymid), ("L", x + sw, ymid)], stroke=INK, width=1.6, dash=PL_DASH)
            elif kind == "setback":
                self._p([("M", x, ymid), ("L", x + sw, ymid)], stroke=INK2, width=0.6, dash=SETBACK_DASH)
            elif kind == "cloud":
                self._p(cloud_segments((x + 3, y0, x + sw - 3, y1), 3.0), stroke=INK, width=0.9)
            elif kind.startswith("hatch:"):
                from . import hatch as _hatch
                _hatch.swatch(self.page, (x, y0 - 1, x + sw, y1 + 1), kind[6:], region=self.id)
            elif kind.startswith("pen:"):
                from . import pens as _pens
                self._p([("M", x, ymid), ("L", x + sw, ymid)], **_pens.kw(kind[4:]))
            elif kind.startswith("tag:"):
                from .symbols import tag_paper
                shape, _, mark = kind[4:].partition(":")
                tag_paper(self.page, x + sw / 2, ymid, mark or "X", shape, 6.5, region=self.id, role="legend")
            else:
                raise ValueError(f"unknown legend kind {kind!r}")
            self._t(x + sw + 10, ymid - size * 0.35, label, size=size, role="legend")
            self.y -= rh

    def fv_schedule(self, size: float = 7.0, sign_off: bool = True, grid: bool = False):
        """The field-verify list from project.json, ranked, with a sign-off column.

        grid=True draws it as a ruled grid_table.
        """
        from .model import fv_key
        # rank first, then natural tag order (FV-2 before FV-10, FV-9 before FV-H1)
        fv = sorted(self.sheet.project.fv.values(), key=lambda e: (e.get("rank", 99), fv_key(e["tag"])))
        cols = [("TAG", 0.55), ("RANK", 0.45), ("VERIFY", 2.6, "wrap"), ("WHY IT MATTERS", None, "wrap")]
        if sign_off:
            cols.append(("BY / DATE", 1.0, "wrap"))
        rows = []
        for e in fv:
            row = [e["tag"], str(e.get("rank", "")), e["what"], e["why"]]
            if sign_off:
                so = e.get("signed_off")
                row.append(f"{so['by']} {so['date']}" if so else "")
            rows.append(row)
        if grid:
            cols = [(c[0], c[1], "wrap") if len(c) > 2 else (c[0], c[1], "center") for c in cols]
            self.grid_table(cols, rows, size=size, role="fv_schedule")
        else:
            self.table(cols, rows, size=size, role="fv_schedule")

    # ---- data tables, schedules and note columns

    def grid_table(self, columns, rows, size: float = 6.8, header: bool = True, lead: float = 1.5,
                   role: str = "panel", row_meta=None):
        """A ruled data table: a tinted header row, cell rules and optional group bands.

        columns  [(title, width in inches or None for the rest[, align])], align is
                 "wrap" (wraps, left), "right", "center" or "left" (default).
        rows     lists of cells (str or kit.text). A row ("group", "SETBACKS")
                 prints a full-width band. A cell never clips: a plain cell wider
                 than its column raises LayoutError; mark the column "wrap".
        Use it for zoning / area summaries, code data and schedules. Every number
        in a cell comes from kit.text, so QA reads its keys and FV tags.
        """
        fixed = sum(c[1] * 72 for c in columns if c[1])
        free = [i for i, c in enumerate(columns) if not c[1]]
        rest = (self.width - fixed) / max(1, len(free))
        if rest < 0 or (not free and fixed > self.width + 0.5):
            raise LayoutError(f"{self.sheet.id} {self.id}: table columns are wider than the panel")
        widths = [c[1] * 72 if c[1] else rest for c in columns]
        aligns = [c[2] if len(c) > 2 else "left" for c in columns]
        xs = [self.x0]
        for w in widths[:-1]:
            xs.append(xs[-1] + w)
        x_end = xs[-1] + widths[-1]
        line_h = size * 1.22
        padx = 3.0
        top = self.y
        hlines, vstarts = [top], []

        def band(text, tint, bold, h, tsize):
            self._p(rect_segments(self.x0, self.y - h, x_end, self.y), stroke=None, fill=tint)
            self._t(self.x0 + padx, self.y - h / 2 - tsize * 0.36, text, size=tsize, bold=bold, color=INK,
                    tracking=0.3, meta={"heading": True})

        if header:
            hh = size * lead + 2
            self._need(hh)
            self._p(rect_segments(self.x0, self.y - hh, x_end, self.y), stroke=None, fill=TABLE_HEAD)
            for x, w, c, al in zip(xs, widths, columns, aligns):
                self._t(_ax(x, w, al, padx), self.y - hh / 2 - size * 0.32, c[0], size=size * 0.88, bold=True,
                        color=INK, tracking=0.3, anchor=_anchor(al))
            self.y -= hh
            hlines.append(self.y)
            vstarts.append(self.y + hh)
        for ri, row in enumerate(rows):
            if isinstance(row, tuple) and len(row) == 2 and row[0] == "group":
                gh = size * lead + 1
                self._need(gh)
                band(row[1], TABLE_GROUP, True, gh, size * 0.92)
                self.y -= gh
                hlines.append(self.y)
                continue
            cells = []
            for ci, cell in enumerate(row):
                if cell is None or str(cell) == "":
                    cells.append([])
                    continue
                txt = tm.clean(str(cell))
                if aligns[ci] == "wrap":
                    cells.append(tm.wrap(txt, widths[ci] - 2 * padx, size, ci == 0))
                elif tm.text_width(txt, size, ci == 0) > widths[ci] - 2 * padx + 0.5:
                    raise LayoutError(f"{self.sheet.id} {self.id}: table cell {txt!r} is wider than its "
                                      f"{widths[ci] / 72:.2f} in column. Widen the column, mark it 'wrap', "
                                      "or shorten the text")
                else:
                    cells.append([cell])
            n = max(1, max((len(c) for c in cells), default=1))
            rh = size * lead + line_h * (n - 1)
            self._need(rh)
            self._groups += 1
            meta = dict(row_meta[ri]) if row_meta else {}
            for ci, (x, w, lines) in enumerate(zip(xs, widths, cells)):
                for li, ln in enumerate(lines):
                    m = dict(meta)
                    m["group"] = f"{self.id}:r{self._groups}:c{ci}"
                    self._t(_ax(x, w, aligns[ci], padx), self.y - (size * lead) / 2 - size * 0.34 - li * line_h,
                            ln, size=size, bold=(ci == 0), role=role, anchor=_anchor(aligns[ci]), meta=m,
                            **first_line_marks(row[ci], li == 0))
            self.y -= rh
            hlines.append(self.y)
        bottom = self.y
        for y in hlines[1:-1]:
            self._p([("M", self.x0, y), ("L", x_end, y)], stroke=LIGHT, width=0.35)
        for x in xs[1:]:
            self._p([("M", x, top), ("L", x, bottom)], stroke=LIGHT, width=0.35)
        self._p(rect_segments(self.x0, bottom, x_end, top), stroke=INK, width=0.7)
        self.y -= 6

    def opening_schedule(self, types=None, size: float = 6.8, notes: bool = True, title: str | None = None,
                         fields=("width", "height", "sill", "head"), style: str = "ftin"):
        """Door and window schedule from project.json `openings`, with the plan's tag symbols.

        types   opening types to list (e.g. ("window",)); None lists every opening.
        fields  the size columns, in order. Each prints from the opening's field
                with its FV tags, in `style`; a column no listed opening fills is
                left out. A PLACEHOLDER size prints PENDING.
        The TYPE column prints the opening's `desc` when it has one, else its
        type and action: (N) WINDOW, (E) DOOR, (E) OVERHEAD DOOR - REMOVE,
        (E) WINDOW - RELOCATED. NOTES prints its `note`.
        """
        from .symbols import opening_shape
        proj = self.sheet.project
        items = [o for o in proj.items("openings") if types is None or o.get("type") in types]
        if not items:
            raise LayoutError(f"{self.sheet.id} {self.id}: no openings of type {types} in project.json")
        if title:
            self.heading(title, size=9.5)
        fields = [f for f in fields if any(o.get(f) is not None for o in items)]
        cols = [("TAG", 0.5, "tag"), ("TYPE", 2.3, "wrap")]
        cols += [(f.upper(), 0.95) for f in fields]
        if notes:
            cols.append(("NOTES", None, "wrap"))
        rows = []
        for o in items:
            row = [(opening_shape(o), o.get("mark") or o["id"]), _opening_desc(o)]
            for f in fields:
                row.append(_value_cell(proj, o.get(f), style))
            if notes:
                row.append(str(o.get("note", "")).upper())
            rows.append(row)
        self.table(cols, rows, size=size, role="schedule",
                   row_meta=[{"opening": o["id"]} for o in items], lead=1.7)

    def columns(self, sections, ncols: int = 2, size: float = 7.0, gap: float = 16.0, lead: float = 1.25,
                heading_size: float = 8.5):
        """Numbered notes set in `ncols` balanced columns, each section under its heading.

        sections  [(heading or None, [note, ...])]. Notes number from 1 in each
                  section. A note never splits across columns; a heading never sits
                  alone at the foot of a column. Overflow raises LayoutError.
        """
        cw = (self.width - gap * (ncols - 1)) / ncols
        indent = 15.0
        blocks = _note_blocks(sections, cw - indent, size, lead, heading_size)
        avail = self.y - (self.box[1] + self.pad)
        cols = _balance(blocks, ncols)
        tallest = max(sum(b[1] for b in c) for c in cols)
        if tallest > avail + 0.01:
            raise LayoutError(f"{self.sheet.id} {self.id}: notes need {tallest / 72:.2f} in in {ncols} columns but "
                              f"the panel has {avail / 72:.2f} in left. Make the cell taller, add a column, or "
                              "move notes to another sheet")
        y_top = self.y
        for ci, col in enumerate(cols):
            x = self.x0 + ci * (cw + gap)
            y = y_top
            for kind, bh, pay in col:
                if kind == "head":
                    self._t(x, y - heading_size, pay, size=heading_size, bold=True, tracking=0.4,
                            meta={"heading": True})
                    self._p([("M", x, y - heading_size - 3.5), ("L", x + cw, y - heading_size - 3.5)],
                            stroke=INK, width=0.6)
                elif kind == "note":
                    n, item, lines = pay
                    self._groups += 1
                    g = f"{self.id}:{self._groups}"
                    self._t(x, y - size, f"{n}.", size=size, bold=True)
                    for li, ln in enumerate(lines):
                        self._t(x + indent, y - size - li * size * lead, ln, size=size, meta={"group": g},
                                **first_line_marks(item, li == 0))
                y -= bh
            if ci:
                self._p([("M", x - gap / 2, y_top), ("L", x - gap / 2, y_top - tallest)], stroke=LIGHT, width=0.4)
        self.y = y_top - tallest - 4


def _note_blocks(sections, width, size, lead, heading_size):
    """Layout blocks (kind, height, payload) for numbered notes under headings."""
    blocks = []
    for heading, items in sections:
        if heading:
            blocks.append(("head", heading_size + 9, heading))
        n = 0
        for item in items:
            if item is None or not str(item).strip():
                blocks.append(("gap", size * 0.6, None))
                continue
            n += 1
            lines = tm.wrap(tm.clean(str(item)), width, size)
            blocks.append(("note", size * lead * len(lines) + size * 0.45, (n, item, lines)))
    return blocks


def _fill_columns(blocks, limit):
    """Greedy fill: a new column when the next block (a heading with its first note) would pass limit."""
    cols, cur, h = [], [], 0.0
    for i, b in enumerate(blocks):
        nxt_h = b[1] + (blocks[i + 1][1] if b[0] == "head" and i + 1 < len(blocks) else 0)
        if cur and h + nxt_h > limit + 0.01:
            cols.append(cur)
            cur, h = [], 0.0
        if not cur and b[0] == "gap":
            continue
        cur.append(b)
        h += b[1]
    cols.append(cur)
    return cols


def _balance(blocks, ncols):
    """The shortest column height whose greedy fill uses at most ncols columns."""
    lo = max((b[1] for b in blocks), default=0.0)
    hi = max(lo, sum(b[1] for b in blocks)) + 1
    for _ in range(40):
        mid = (lo + hi) / 2
        if len(_fill_columns(blocks, mid)) <= ncols:
            hi = mid
        else:
            lo = mid
    return _fill_columns(blocks, hi)


def columns_height(sections, width_in: float, ncols: int = 2, size: float = 7.0, gap: float = 16.0,
                   lead: float = 1.25, heading_size: float = 8.5) -> float:
    """Inches a Panel.columns() block needs in a panel `width_in` wide (padding included).

    Use it to size a notes band so it holds its notes and no empty space.
    """
    width = width_in * PT_PER_IN - 12.0
    cw = (width - gap * (ncols - 1)) / ncols
    cols = _balance(_note_blocks(sections, cw - 15.0, size, lead, heading_size), ncols)
    return (max(sum(b[1] for b in c) for c in cols) + 16.0) / PT_PER_IN


TABLE_HEAD = "#e6e6e6"
TABLE_GROUP = "#f2f2f2"


def _anchor(align):
    return {"right": "end", "center": "middle"}.get(align, "start")


def _ax(x, w, align, padx):
    if align == "right":
        return x + w - padx
    if align == "center":
        return x + w / 2
    return x + padx


def _tag_parts(cell):
    """(shape, mark) of a tag cell: a mark string (circle) or a (shape, mark) pair."""
    if isinstance(cell, (tuple, list)):
        return cell[0], str(cell[1])
    return "circle", str(cell)


#: What the TYPE column calls each opening type. "slider" stays SLIDER: it
#: may be a sliding door or a sliding window.
_TYPE_WORD = {"door": "DOOR", "window": "WINDOW", "slider": "SLIDER", "bifold": "BIFOLD DOOR",
              "bypass": "BYPASS DOOR", "cased": "CASED OPENING", "dutch_door": "DUTCH DOOR",
              "pocket": "POCKET DOOR", "overhead": "OVERHEAD DOOR", "skylight": "SKYLIGHT"}
#: (prefix, suffix) per action: (N) WINDOW, (E) DOOR, (E) OVERHEAD DOOR - REMOVE, (E) WINDOW - RELOCATED.
_ACTION_WORD = {"new": ("(N)", ""), "existing": ("(E)", ""), "relocate": ("(E)", " - RELOCATED"),
                "demo": ("(E)", " - REMOVE")}


def _opening_desc(o) -> str:
    if o.get("desc"):
        return str(o["desc"]).upper()
    t = str(o.get("type", ""))
    kind = _TYPE_WORD.get(t, t.replace("_", " ").upper()) or "OPENING"
    pre, post = _ACTION_WORD.get(o.get("action", ""), ("", ""))
    return f"{pre} {kind}{post}".strip()


def _value_cell(project, ref, style: str = "ftin"):
    """A schedule cell for a Dim: its length with FV tags, '-' when empty, PENDING for a placeholder."""
    from .notes import Txt, fv_text, tags_for, value_text
    if ref is None:
        return "-"
    val = project.dim(ref)
    if val.status == "PLACEHOLDER" or any(project.values[u].status == "PLACEHOLDER"
                                          for u in val.unverified_inputs):
        return "PENDING"
    tags = tags_for(project, val)
    text = value_text(project, val, style if val.unit == "in" else None)
    if tags:
        text += " " + fv_text(tags)
    return Txt(text, keys=[val.key], fv=tags)
