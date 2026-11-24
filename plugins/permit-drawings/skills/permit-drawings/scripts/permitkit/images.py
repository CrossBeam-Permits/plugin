"""Raster images on sheets: photos, concept renderings, aerials, product images.

Every image is an `images` entry in project.json (id, path, kind, source,
date) and a sheet places it by id. The kit prints the entry's source under
every image and a fixed note for its kind. A concept rendering always prints
"CONCEPT RENDERING - NOT A CONSTRUCTION DOCUMENT" on a band across the image
itself and under it, and it can never go into a drawing view. Only an aerial
goes into a view, the N.T.S. vicinity map, with a north arrow and a site
marker drawn over it in kit vector.

An image occupies its area: QA fails a text that sits on an image without a
filled backing shape (see display.text_over_images).

    fr = sh.place_image((0, 10, 8, 6), "PH-1", title="EXISTING BATH")
    images.vicinity_map(sh, (18, 10, 8, 7), "AER-1")

See references/images-and-finishes.md.
"""
from __future__ import annotations

from . import textmetrics as tm
from .display import DIM, INK, INK2, LIGHT, WHITE, LayoutError, circle_segments, first_line_marks, rect_segments
from .raster import ImageError, load

CONCEPT_LABEL = "CONCEPT RENDERING — NOT A CONSTRUCTION DOCUMENT"
#: The fixed note each kind prints under its image. The kit supplies it; a script cannot change it.
KIND_NOTE = {
    "photo": "PHOTO FOR REFERENCE ONLY. NOT TO SCALE. DIMENSIONS ON THE DRAWINGS GOVERN.",
    "concept": CONCEPT_LABEL + ". NOT TO SCALE.",
    "aerial": "AERIAL FOR LOCATION ONLY. NOT TO SCALE.",
    "product": "PRODUCT IMAGE FOR IDENTIFICATION ONLY.",
}


def entry(project, image_id: str) -> dict:
    """The images entry with this id. Raises ImageError when there is none."""
    for im in project.data.get("images", []):
        if im["id"] == image_id:
            return im
    raise ImageError(f"image {image_id!r} is not in project.json images")


def raster(project, image_id: str):
    """The decoded image for an id, read once per project load."""
    cache = project.__dict__.setdefault("_rasters", {})
    if image_id not in cache:
        e = entry(project, image_id)
        try:
            path = project.resolve_path(e["path"])
        except ValueError as exc:
            raise ImageError(str(exc)) from None
        try:
            cache[image_id] = load(path)
        except OSError as exc:
            raise ImageError(f"image {image_id!r}: cannot read {e['path']!r} ({exc.strerror})") from None
    return cache[image_id]


def source_line(e: dict) -> str:
    """The printed source label: the entry's source, and its date when the source does not hold it."""
    s = "SOURCE: " + e["source"].strip()
    if e.get("date") and e["date"] not in s:
        s += f", {e['date']}"
    return s


def draw(page, project, image_id: str, box, region: str, fit: str = "fit", layer: str = "geom") -> dict:
    """Place image `image_id` in box (points) and record it for the sidecar.

    Low level: the caller prints the labels (label_texts). Returns the image op.
    """
    e = entry(project, image_id)
    r = raster(project, image_id)
    return page.image(r, box, fit=fit, region=region, layer=layer,
                      record={"id": e["id"], "kind": e["kind"], "path": e["path"], "source": e["source"]})


def label_meta(op, image_id: str, which: str) -> dict:
    """The meta that ties a label text to one placed image (QA matches them by the image's seq)."""
    return {"image": image_id, "image_label": which, "image_seq": op["seq"]}


def _label(page, x, y, s, op, image_id, which, region, **kw):
    meta = label_meta(op, image_id, which)
    return page.text(x, y, s, region=region, role="image.label", meta=meta, **kw)


def concept_band(page, op, image_id: str, region: str, size: float = 9.0) -> None:
    """The white band across the foot of a concept image, with the concept label on it."""
    x0, y0, x1, _ = op["clip"]
    h = size * 1.9
    if tm.text_width(CONCEPT_LABEL, size, True) > x1 - x0 - 8:
        raise LayoutError(f"concept image {image_id!r} is too narrow for its label; make its cell wider")
    page.path(rect_segments(x0, y0, x1, y0 + h), stroke=DIM, width=0.8, fill=WHITE, layer="annot", region=region)
    _label(page, (x0 + x1) / 2, y0 + h / 2 - size * 0.36, CONCEPT_LABEL, op, image_id, "concept", region,
           size=size, bold=True, anchor="middle", color=DIM)


class Frame:
    """A placed image: its op, its entry, and the box it occupies (points)."""

    def __init__(self, op, e, region):
        self.op = op
        self.entry = e
        self.region = region
        self.box = tuple(op["clip"])

    def px(self, col: float, row: float) -> tuple:
        """Paper point of a pixel position [column, row] from the image's top-left corner."""
        x0, y0, x1, y1 = self.op["placed"]
        w, h = self.op["raster"].display_size
        return (x0 + (x1 - x0) * col / w, y1 - (y1 - y0) * row / h)


def place(sheet, cell, image_id: str, title: str | None = None, caption=None, fit: str = "fit",
          size: float = 7.0, slot: str | None = None) -> Frame:
    """Place an image in its own cell, (x, y, w, h) inches from the drawing-area lower-left.

    The cell holds an optional heading, the image at its aspect ratio, and
    right under it the caption (default: the entry's caption), the kind note
    and the source label. fit="fit" shows the whole image at the top of the
    cell; fit="fill" fills the space between heading and labels and crops.
    A concept rendering also gets its label on a band across the image.

    slot: the name of a cell already reserved with sheet.slot(...), in place
    of `cell` (pass cell=None). The image fills that slot and marks it filled.
    """
    from .sheet import Panel
    e = entry(sheet.project, image_id)
    if slot is not None:
        sl = sheet.slots[slot]
        rid, box = next((r, b) for r, b in sheet.cells if r == f"slot:{slot}")
        sl.filled = True
    else:
        n = sum(1 for rid, _ in sheet.cells if rid.startswith("image:")) + 1
        rid = f"image:{n}"
        box = sheet._cell(cell, rid)
        sheet.cells.append((rid, box))
    pn = Panel(sheet, rid, box)
    if title:
        pn.heading(title)
    caption = caption if caption is not None else e.get("caption")
    note_color = DIM if e["kind"] == "concept" else INK2

    def label_lines(width):
        """(text, size, bold, color, which, source item) for labels wrapped to width."""
        out = []
        if caption:
            for i, ln in enumerate(tm.wrap(tm.clean(str(caption)), width, size + 1, True)):
                out.append((ln, size + 1, True, INK, "caption", caption if i == 0 else None))
        for ln in tm.wrap(KIND_NOTE[e["kind"]], width, size, e["kind"] == "concept"):
            out.append((ln, size, e["kind"] == "concept", note_color, "kind", None))
        for ln in tm.wrap(tm.clean(source_line(e)), width, size):
            out.append((ln, size, False, INK2, "source", None))
        return out

    dw, dh = raster(sheet.project, image_id).display_size
    width = pn.width
    for _ in range(3):        # the labels wrap to the image's width, which depends on their height
        lines = label_lines(width)
        text_h = sum(z * 1.3 for _, z, *_ in lines) + 6
        img_box = (pn.x0, box[1] + pn.pad + text_h, pn.x1, pn.y)
        if img_box[3] - img_box[1] < 36:
            raise LayoutError(f"{sheet.id} {rid}: no room for image {image_id!r} under its heading and "
                              "above its labels; make the cell taller")
        if fit != "fit":
            break
        # the whole image, at the top, labels right under it, aligned to its left edge
        h = min(img_box[3] - img_box[1], pn.width * dh / dw)
        new_w = h * dw / dh
        img_box = (pn.x0 + (pn.width - new_w) / 2, img_box[3] - h, pn.x0 + (pn.width + new_w) / 2, img_box[3])
        if abs(new_w - width) < 0.5 or new_w > width:
            break
        width = new_w
    lines = label_lines(img_box[2] - img_box[0]) if fit == "fit" else lines
    op = draw(sheet.page, sheet.project, image_id, img_box, rid, fit=fit)
    x0, y0, x1, y1 = op["clip"]
    sheet.page.path(rect_segments(x0, y0, x1, y1), stroke=LIGHT, width=0.6, layer="annot", region=rid)
    if e["kind"] == "concept":
        concept_band(sheet.page, op, image_id, rid)
    y = y0 - 4
    for text, s, bold, color, which, src in lines:
        y -= s * 1.3
        marks = first_line_marks(src, True) if src is not None else {}
        rec = _label(sheet.page, x0, y + s * 0.25, text, op, image_id, which, rid, size=s, bold=bold,
                     color=color, **{k: v for k, v in marks.items() if k != "claim"})
        rec["meta"]["group"] = f"{rid}:{which}"
    return Frame(op, e, rid)


# ------------------------------------------------------------------ vicinity map

def vicinity_map(sheet, cell, image_id: str, title: str = "VICINITY MAP", site_label: str = "PROJECT SITE",
                 address: bool = True):
    """An aerial image as an N.T.S. view, with a north arrow and a site marker in kit vector.

    The image must be kind "aerial" with north_deg (degrees clockwise from
    image-up to true north). site_px [column, row] places the site marker; the
    label prints site_label and the project address. Returns the View.
    """
    from . import annot
    project = sheet.project
    e = entry(project, image_id)
    if e["kind"] != "aerial":
        raise ImageError(f"vicinity_map takes an aerial image; {image_id!r} is a {e['kind']}. "
                         "A photo or a concept rendering never goes into a drawing view")
    if "north_deg" not in e:
        raise ImageError(f"aerial {image_id!r} has no north_deg. Record the degrees clockwise from the "
                         "image's up direction to true north (0 when north is up) before drawing the map")
    r = raster(project, image_id)
    W, H = r.display_size
    v = sheet.view(title, "N.T.S.", extents=(0, 0, W, H), cell=cell, scale_bar=False)
    pg = sheet.page
    op = draw(pg, project, image_id, v.bbox_pt, v.id, fit="fill")
    x0, y0, x1, y1 = op["clip"]
    pg.path(rect_segments(x0, y0, x1, y1), stroke=INK, width=0.8, layer="annot", region=v.id)
    fr = Frame(op, e, v.id)

    # north arrow on a white disc in the top-right corner
    rr = 30.0
    cx, cy = x1 - rr - 8, y1 - rr - 8
    pg.path(circle_segments(cx, cy, rr), stroke=INK, width=0.6, fill=WHITE, layer="annot", region=v.id)
    annot.north_arrow(v, (v.x0 + (cx - v.ox) / v.s, v.y0 + (cy - v.oy) / v.s), r=11.0,
                      rotation_deg=float(e["north_deg"]), label="N")

    # source and kind note on a white box in the bottom-left corner
    lines = [(KIND_NOTE["aerial"], "kind", True), (tm.clean(source_line(e)), "source", False)]
    size = 6.5
    bw = max(tm.text_width(s, size, b) for s, _, b in lines) + 10
    bh = size * 1.35 * len(lines) + 6
    if bw > x1 - x0 - 8:
        raise LayoutError(f"{sheet.id}: vicinity map is too narrow for its source label; widen its cell")
    pg.path(rect_segments(x0 + 4, y0 + 4, x0 + 4 + bw, y0 + 4 + bh), stroke=INK, width=0.5, fill=WHITE,
            layer="annot", region=v.id)
    ty = y0 + 4 + bh - 3
    for s, which, bold in lines:
        ty -= size * 1.35
        _label(pg, x0 + 9, ty + size * 0.3, s, op, image_id, which, v.id, size=size, bold=bold, color=INK)

    # site marker and its label
    if e.get("site_px"):
        sx, sy = fr.px(*e["site_px"])
        if not (x0 < sx < x1 and y0 < sy < y1):
            raise ImageError(f"aerial {image_id!r}: site_px {e['site_px']} is outside the image")
        ring = 13.0
        pg.path(circle_segments(sx, sy, ring), stroke=WHITE, width=4.0, layer="annot", region=v.id)
        pg.path(circle_segments(sx, sy, ring), stroke=DIM, width=1.8, layer="annot", region=v.id)
        pg.path(circle_segments(sx, sy, 2.0), stroke=None, fill=DIM, layer="annot", region=v.id)
        texts = [(site_label, 8.0, True)]
        if address and project.meta.get("address"):
            texts.append((tm.clean(project.meta["address"]), 6.5, False))
        lw = max(tm.text_width(s, z, b) for s, z, b in texts) + 12
        lh = sum(z * 1.35 for _, z, _ in texts) + 6
        right = sx + 30 + lw < x1 - 4
        up = sy + 26 + lh < y1 - 4 and not (right and sy + 26 + lh > cy - rr - 4 and sx + 30 + lw > cx - rr)
        bx = sx + 30 if right else sx - 30 - lw
        by = sy + 26 if up else sy - 26 - lh
        if bx < x0 + 4 or by < y0 + 4:
            raise LayoutError(f"{sheet.id}: no room for the site label beside site_px {e['site_px']}")
        ex = bx if right else bx + lw
        ey = by if up else by + lh
        tip = ((ex - sx), (ey - sy))
        d = (tip[0] ** 2 + tip[1] ** 2) ** 0.5
        start = (sx + tip[0] / d * ring, sy + tip[1] / d * ring)
        for col, wd in ((WHITE, 3.2), (DIM, 1.0)):
            pg.path([("M", *start), ("L", ex, ey)], stroke=col, width=wd, layer="annot", region=v.id)
        pg.path(rect_segments(bx, by, bx + lw, by + lh), stroke=DIM, width=0.8, fill=WHITE, layer="annot",
                region=v.id)
        ty = by + lh - 3
        for s, z, b in texts:
            ty -= z * 1.35
            pg.text(bx + 6, ty + z * 0.3, s, size=z, bold=b, color=DIM if b else INK, region=v.id,
                    view=v.id, role="image.site")
    return v
