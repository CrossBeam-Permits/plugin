"""Finish schedule and materials board, from the `finishes` block of project.json.

Each finish: id (the mark, such as T-1), location, item, material, color_name,
rgb ("#RRGGBB"), manufacturer, product, finish (sheen), status (SELECTED,
PROPOSED or TBD), and optionally the id of a product image.

Drawing:
    finishes.schedule(sh, (0, 0, 16, 9))     # table with a color swatch per row
    finishes.board(sh, (16.2, 0, 10, 9))     # swatch tiles, with product photos

Colors for other modules (3D views, elevations):
    finishes.rgb(project, "T-1")    -> (r, g, b) in 0..1, or None while TBD
    finishes.rgb255(project, "T-1") -> (r, g, b) in 0..255, or None
    finishes.get(project, "T-1")    -> the entry (a dict)

Text fields are note templates, so a size prints from a Value with its FV tag:
"PORCELAIN TILE {tile_w:in} x {tile_l:in}". A swatch is a screen color, never a
color match; the board says so. See references/images-and-finishes.md.
"""
from __future__ import annotations

from . import textmetrics as tm
from .display import DIM, GREY, INK, INK2, LIGHT, WHITE, LayoutError, first_line_marks, rect_segments, rgb as _rgb
from .notes import fill

STATUS_TEXT = {"SELECTED": "SELECTED", "PROPOSED": "PROPOSED, OWNER TO CONFIRM",
               "TBD": "TO BE SELECTED BY OWNER"}
BOARD_NOTE = ("SWATCH COLORS ARE APPROXIMATE SCREEN AND PRINT COLORS. MATCH TO THE MANUFACTURER'S PHYSICAL "
              "SAMPLE. DASHED CHIP: PROPOSED, OWNER TO CONFIRM. HATCHED CHIP: TO BE SELECTED.")
BAND = "#f1f1ee"          # light band behind a location heading in the schedule


def entries(project) -> list[dict]:
    """Every finish, in project.json order. Takes a Project or the raw project dict."""
    return list(getattr(project, "data", project).get("finishes", []))


def get(project, fid: str) -> dict:
    for f in entries(project):
        if f["id"] == fid:
            return f
    raise KeyError(f"finish {fid!r} is not in project.json finishes")


def rgb(project, fid: str):
    """The finish color as (r, g, b) floats 0..1, or None when it has no color yet (TBD)."""
    f = get(project, fid)
    return _rgb(f["rgb"]) if f.get("rgb") else None


def rgb255(project, fid: str):
    """The finish color as (r, g, b) integers 0..255, or None when it has no color yet."""
    c = rgb(project, fid)
    return tuple(int(round(v * 255)) for v in c) if c else None


def _t(project, s):
    """A finish text field filled as a note template (FV tags and value keys kept)."""
    return fill(project, s) if s else ""


def swatch(page, box, f: dict, region: str, size: float = 6.5) -> None:
    """One color chip in box (points). PROPOSED draws a dashed border; TBD draws hatched with 'TBD'."""
    x0, y0, x1, y1 = box
    segs = rect_segments(x0, y0, x1, y1)
    if f["status"] == "TBD" or not f.get("rgb"):
        page.path(segs, stroke=GREY, width=0.7, fill=WHITE, layer="annot", region=region)
        hatch, k, span = [], -(y1 - y0), x1 - x0
        while k < span:
            hatch += [("M", x0 + k, y0), ("L", x0 + k + (y1 - y0), y1)]
            k += 5.0
        page.path(hatch, stroke=LIGHT, width=0.4, clip=segs, layer="annot", region=region)
        page.path(rect_segments((x0 + x1) / 2 - 10, (y0 + y1) / 2 - 5, (x0 + x1) / 2 + 10, (y0 + y1) / 2 + 6),
                  stroke=None, fill=WHITE, layer="annot", region=region)
        page.text((x0 + x1) / 2, (y0 + y1) / 2 - size * 0.35, "TBD", size=size, bold=True, anchor="middle",
                  color=GREY, region=region, role="finish.swatch")
        return
    dash = (3.0, 2.0) if f["status"] == "PROPOSED" else None
    page.path(segs, stroke=INK2 if dash else INK, width=0.7, fill=f["rgb"], dash=dash, layer="annot",
              region=region)


def _lines(cell, width, size, bold=False):
    """A cell's lines: each item is (text, source item or None). Items are strings or note Txt."""
    out = []
    for item in cell:
        if not item:
            continue
        for i, ln in enumerate(tm.wrap(tm.clean(str(item)), width, size, bold)):
            out.append((ln, item if i == 0 else None))
    return out


def _put(pn, x, y, text, src, size, bold=False, color=INK, role="finish", meta=None):
    marks = first_line_marks(src, True) if src is not None else {}
    marks.pop("claim", None)
    return pn._t(x, y, text, size=size, bold=bold, color=color, role=role, meta=dict(meta or {}), **marks)


# ------------------------------------------------------------------ schedule

def schedule(sheet, cell, title: str = "FINISH SCHEDULE", ids=None, size: float = 7.0):
    """The finish schedule as a table in its own panel, grouped by location, a swatch per row."""
    p = sheet.project
    rows = [f for f in entries(p) if ids is None or f["id"] in ids]
    if not rows:
        raise LayoutError(f"{sheet.id}: no finishes to schedule; add a finishes block to project.json")
    pn = sheet.panel(cell, title)
    cols = [("", 0.62, 0), ("MARK", 0.6, 0), ("ITEM", None, 1.0), ("MATERIAL / PRODUCT", None, 1.7),
            ("COLOR", None, 1.0), ("FINISH", 1.0, 0), ("STATUS", 1.25, 0)]
    fixed = sum(c[1] * 72 for c in cols if c[1])
    weight = sum(c[2] for c in cols if not c[1])
    rest = pn.width - fixed
    if rest < 72:
        raise LayoutError(f"{sheet.id} {pn.id}: the finish schedule needs a wider cell")
    widths = [c[1] * 72 if c[1] else rest * c[2] / weight for c in cols]
    xs = [pn.x0]
    for w in widths[:-1]:
        xs.append(xs[-1] + w)
    pn._need(size * 2.2)
    for x, c in zip(xs, cols):
        if c[0]:
            pn._t(x, pn.y - size, c[0], size=size * 0.9, bold=True, color=INK2, tracking=0.3)
    pn.y -= size * 1.4
    pn._rule(pn.y, width=0.8)
    pn.y -= 2
    chip_h, lead = size * 3.0, size * 1.25
    groups = []
    for f in rows:
        if not groups or groups[-1][0] != f["location"]:
            groups.append((f["location"], []))
        groups[-1][1].append(f)
    for loc, items in groups:
        band_h = size * 2.0
        pn._need(band_h + chip_h + 6)
        pn._p(rect_segments(pn.x0 - 2, pn.y - band_h, pn.x1 + 2, pn.y), stroke=None, fill=BAND)
        _put(pn, pn.x0 + 2, pn.y - band_h + size * 0.62, tm.clean(_t(p, loc)), _t(p, loc), size,
             bold=True, role="finish.location")
        pn.y -= band_h
        for f in items:
            cells = [[], [f["id"]], [_t(p, f["item"])],
                     [_t(p, f.get("material")), _t(p, " ".join(x for x in (f.get("manufacturer"), f.get("product"))
                                                                if x))],
                     [_t(p, f.get("color_name"))], [_t(p, f.get("finish"))], [STATUS_TEXT[f["status"]]]]
            lines = [_lines(c, w - 6, size, bold=(i == 1)) for i, (c, w) in enumerate(zip(cells, widths))]
            n = max(len(ls) for ls in lines)
            row_h = max(chip_h + 6, n * lead + 8)
            pn._need(row_h)
            top = pn.y - 4
            swatch(pn.page, (xs[0] + 2, top - chip_h, xs[0] + widths[0] - 8, top), f, pn.id)
            for i, (x, ls) in enumerate(zip(xs, lines)):
                for k, (ln, src) in enumerate(ls):
                    color = DIM if (i == 6 and f["status"] != "SELECTED") else INK
                    _put(pn, x, top - size - k * lead, ln, src, size, bold=(i == 1), color=color,
                         meta={"finish": f["id"], "group": f"{pn.id}:{f['id']}:c{i}"})
            pn.y -= row_h
            pn._p([("M", pn.x0, pn.y + 1), ("L", pn.x1, pn.y + 1)], stroke=LIGHT, width=0.35)
    pn._rule(pn.y + 1, width=0.8)
    pn.y -= 4
    pn.para(BOARD_NOTE, size=size * 0.9, color=INK2)
    return pn


# ------------------------------------------------------------------ materials board

def board(sheet, cell, title: str = "MATERIALS BOARD", ids=None, columns: int | None = None,
          size: float = 7.5, max_chip_in: float = 2.4):
    """The materials board: one tile per finish in a grid, filling the cell.

    Each tile is a color chip (with a product photo beside it when the finish
    names an image) and its labels: mark and item, location (when the board
    holds more than one), color name, material, manufacturer and product,
    finish, and the status when it is not SELECTED. Chips grow to fill the
    cell, up to max_chip_in inches tall.
    """
    from . import images
    p = sheet.project
    items = [f for f in entries(p) if ids is None or f["id"] in ids]
    if not items:
        raise LayoutError(f"{sheet.id}: no finishes for the board; add a finishes block to project.json")
    pn = sheet.panel(cell, title)
    note_lines = tm.wrap(BOARD_NOTE, pn.width, size * 0.85)
    note_h = len(note_lines) * size * 0.85 * 1.3 + 8
    cols = columns or max(1, int(pn.width // (2.6 * 72)))
    gap = 16.0
    tw = (pn.width - gap * (cols - 1)) / cols
    many_locs = len({f["location"] for f in items}) > 1
    small = size * 0.85
    tiles = []
    for f in items:
        lab = [(tm.clean(_t(p, f["item"])), _t(p, f["item"]), size, True, INK)]
        if many_locs:
            lab.append((tm.clean(_t(p, f["location"])), _t(p, f["location"]), small, False, INK2))
        if f.get("color_name"):
            lab.append((tm.clean(_t(p, f["color_name"])), _t(p, f["color_name"]), size, True, INK2))
        for key in ("material", "finish"):
            if f.get(key):
                lab.append((tm.clean(_t(p, f[key])), _t(p, f[key]), small, False, INK2))
        mp = " ".join(x for x in (f.get("manufacturer"), f.get("product")) if x)
        if mp:
            lab.append((tm.clean(_t(p, mp)), _t(p, mp), small, False, INK2))
        if f["status"] != "SELECTED":
            lab.append((STATUS_TEXT[f["status"]], None, small, True, DIM))
        lines = []
        for text, src, z, b, col in lab:
            for k, ln in enumerate(tm.wrap(text, tw, z, b)):
                lines.append((ln, src if k == 0 else None, z, b, col))
        tiles.append((f, lines))
    rows = [tiles[i:i + cols] for i in range(0, len(tiles), cols)]
    label_h = [max(sum(z * 1.3 for _, _, z, _, _ in ls) for _, ls in row) for row in rows]
    top, bottom = pn.y - 4, pn.box[1] + pn.pad + note_h
    row_gap = 18.0
    chip = min(max_chip_in * 72, (top - bottom - sum(label_h) - len(rows) * (row_gap + 8)) / len(rows))
    if chip < 36:
        raise LayoutError(f"{sheet.id} {pn.id}: the materials board needs a larger cell or more columns "
                          f"(chips would be {chip / 72:.2f} in tall)")
    used = len(rows) * (chip + 8) + sum(label_h) + (len(rows) - 1) * row_gap
    if len(rows) > 1:                    # spread the rows over the board's height
        row_gap = min(row_gap * 3, row_gap + (top - bottom - used - row_gap) / (len(rows) - 1))
    src_size = size * 0.7
    y = top
    for row, lh in zip(rows, label_h):
        for ci, (f, ls) in enumerate(row):
            x = pn.x0 + ci * (tw + gap)
            cw = (tw - 8) / 2 if f.get("image") else tw
            # a soft shadow under each chip, like a sample mounted on a board
            pn.page.path(rect_segments(x + 2.5, y - chip - 2.5, x + cw + 2.5, y - 2.5), stroke=None,
                         fill="#dcdcd8", layer="annot", region=pn.id)
            swatch(pn.page, (x, y - chip, x + cw, y), f, pn.id)
            tag_w = tm.text_width(f["id"], size, True) + 8
            pn.page.path(rect_segments(x + 5, y - 5 - size * 1.6, x + 5 + tag_w, y - 5), stroke=INK, width=0.5,
                         fill=WHITE, layer="annot", region=pn.id)
            pn.page.text(x + 9, y - 5 - size * 1.15, f["id"], size=size, bold=True, region=pn.id,
                         role="finish.tag", meta={"finish": f["id"]})
            if f.get("image"):
                e = images.entry(p, f["image"])
                il = tm.wrap(tm.clean(images.source_line(e)), cw, src_size)
                px0 = x + cw + 8
                pbox = (px0, y - chip + len(il) * src_size * 1.25 + 3, x + tw, y)
                op = images.draw(pn.page, p, f["image"], pbox, pn.id, fit="fit")
                c = op["clip"]
                pn.page.path(rect_segments(*c), stroke=LIGHT, width=0.5, layer="annot", region=pn.id)
                ty = pbox[1] - 3
                for ln in il:
                    ty -= src_size * 1.25
                    pn.page.text(px0, ty + 1.5, ln, size=src_size, color=INK2, region=pn.id, role="image.label",
                                 meta=dict(images.label_meta(op, f["image"], "source"),
                                           group=f"{pn.id}:{f['image']}:src"))
            ty = y - chip - 8
            for ln, src, z, b, col in ls:
                ty -= z * 1.3
                _put(pn, x, ty + z * 0.3, ln, src, z, bold=b, color=col,
                     meta={"finish": f["id"], "group": f"{pn.id}:{f['id']}"})
        y -= chip + 8 + lh + row_gap
    pn.y = bottom
    pn._rule(pn.y, width=0.5)
    pn.y -= 3
    for ln in note_lines:
        pn.y -= size * 0.85 * 1.3
        pn._t(pn.x0, pn.y + 2, ln, size=size * 0.85, color=INK2, meta={"group": f"{pn.id}:note"})
    return pn
