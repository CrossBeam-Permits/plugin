# Images on sheets, finish boards and the vicinity map

Read this before you put a photo, a rendering, an aerial or a product image on a sheet, or before you draw a finish schedule or a materials board. Professional sets now often show a color rendering on the title sheet, an aerial vicinity map, and a finish board with color swatches. The kit draws all three. Each one stays honest: the kit prints where every image came from, and it never lets a picture pass for a drawing.

## 1. Images in project.json

Every image is an entry in `images`. A sheet places it by `id`. The file sits inside the project folder, usually in `images/`.

```json
"images": [
  {"id": "PH-1", "path": "images/bath-east.jpg", "kind": "photo",
   "source": "OWNER PHOTO", "date": "2026-10-08", "source_id": "P1",
   "caption": "(E) HALL BATH, LOOKING EAST"},
  {"id": "CR-1", "path": "images/chatgpt-bath.png", "kind": "concept",
   "source": "CHATGPT IMAGE FROM THE OWNER'S PROMPT", "date": "2026-10-09", "source_id": "R1"},
  {"id": "AER-1", "path": "images/aerial.png", "kind": "aerial",
   "source": "AERIAL (C) <PROVIDER> 2026", "north_deg": 0, "site_px": [412, 288]},
  {"id": "PR-T1", "path": "images/tile.jpg", "kind": "product", "source": "MANUFACTURER WEBSITE, 2026-10-09"}
]
```

- `kind`: `photo` (the site or the existing work), `concept` (a rendering or an AI image of the intended look), `aerial` (an aerial or map image), `product` (a manufacturer's image).
- `source` is required. It prints under the image as `SOURCE: <source>, <date>`. Write who made the image, and for an aerial the provider and its copyright line as the provider asks.
- `source_id` links the image to its `sources` entry (`photo-to-plans.md` section 1), when it has one.
- `north_deg` and `site_px` are for an aerial only (section 4).

Files: JPEG (baseline or progressive, 8-bit, gray, RGB or CMYK) and PNG (any color type and bit depth, with or without transparency). The kit refuses an interlaced PNG, an arithmetic or lossless JPEG, and any other format, and says how to re-save the file. A phone JPEG that is turned by its EXIF orientation prints upright. QA warns when an image prints below 100 dpi; supply a larger file.

`validate` refuses a missing file, a path outside the project folder, a duplicate id and an unknown `source_id`.

## 2. Placing an image

```python
fr = sh.place_image((0, 10.4, 8.9, 6.3), "PH-1", title="EXISTING CONDITIONS (OWNER PHOTO)")
```

The cell is `(x, y, w, h)` inches from the drawing-area lower-left, like a panel. The image keeps its aspect ratio. `fit="fit"` (default) shows the whole image at the top of the cell; `fit="fill"` fills the space and crops the overflow. Under the image the kit prints the caption (`caption=` or the entry's `caption`), a fixed note for the kind (for a photo: `PHOTO FOR REFERENCE ONLY. NOT TO SCALE. DIMENSIONS ON THE DRAWINGS GOVERN.`) and the source label. A caption may be a `kit.text` note, so a value prints with its FV tag. `fr.px(col, row)` gives the paper point of a pixel, for an overlay. With the named slots of the title-sheet layout, pass `cell=None, slot="rendering"`.

An image is an occupied area. QA fails a text that sits on an image unless a filled shape drawn over the image backs it (a white box). An overlay label gets a white box: `sh.page.path(rect_segments(...), fill=WHITE, layer="annot", region=fr.region)`, then the text.

## 3. The concept guard

A rendering shows a wish (`photo-to-plans.md` section 5). On a sheet it must never read as a drawing. So, for `kind: "concept"`:

- The kit prints `CONCEPT RENDERING — NOT A CONSTRUCTION DOCUMENT` on a band across the foot of the image itself, and again under it. A script cannot turn this off.
- It never goes into a drawing view. Only an aerial goes into a view (the N.T.S. vicinity map). `vicinity_map` refuses any other kind, and QA fails a concept or photo inside a view.
- It is never a finish's product image.

QA (`images`) fails a concept image without its label on the image, and any image without its source label. It also fails when an image file changed after the build.

Put the owner's rendering on the cover or the finish sheet next to the drawn plans, so the plan checker sees the intent. The dimensions still come from the tape and from `project.json`, never from the picture.

## 4. Vicinity map

```python
from permitkit import images
images.vicinity_map(sh, (17.95, 10.4, 8.5, 7.15), "AER-1")
```

It places the aerial as an N.T.S. view titled VICINITY MAP, with a kit-vector north arrow on a white disc, a site marker with a leader to `PROJECT SITE` and the project address, and the kind note and source on a white box. The image entry needs:

- `north_deg`: degrees clockwise from the image's up direction to true north (0 when north is up, as on most map tiles). The map refuses to draw without it.
- `site_px`: `[column, row]` of the site in the upright image, from its top-left corner. Read it off the image; it places the marker only.

Where the aerial comes from: the CrossBeam server can render a parcel aerial; when your connector offers one for the address, save it into `images/` and use it. Otherwise the owner supplies an image from a map service, and you record its provider and copyright line in `source`. Never draw a site plan over an aerial: an aerial is not a survey.

## 5. Finishes

The `finishes` block is the finish and color schedule.

```json
"finishes": [
  {"id": "T-1", "location": "HALL BATH", "item": "FLOOR TILE",
   "material": "PORCELAIN TILE {tile_fl_w:in} SQUARE, RECTIFIED", "color_name": "WARM SAND",
   "rgb": "#D8CFC0", "rgb_source": "MFR PUBLISHED RGB", "manufacturer": "<MAKER>", "product": "<LINE>",
   "finish": "MATTE", "status": "PROPOSED", "image": "PR-T1"},
  {"id": "MR-1", "location": "HALL BATH", "item": "MIRROR", "status": "TBD"}
]
```

- `status`: `SELECTED` (the owner chose it), `PROPOSED` (the owner still confirms; the chip draws with a dashed border), `TBD` (the owner selects later; the chip draws hatched with `TBD`). `rgb` is required unless the status is `TBD`.
- Text fields are note templates. A size prints from a Value through `{key:in}`, with its FV tag, never as a typed number.
- `image` names a `product` or `photo` image shown beside the chip.
- `rgb` is a display color. It is never a color match. The board prints that the colors are approximate and that the manufacturer's physical sample governs. Record where the RGB came from in `rgb_source`.

Drawing:

```python
from permitkit import finishes
finishes.board(sh, (0, 9.4, 18.6, 12.9), columns=4)      # chips with labels and product photos
finishes.schedule(sh, (0, 0, 18.6, 9.2))                 # table, grouped by location, a chip per row
```

Both take `ids=[...]` to show only some finishes. A finish sheet (for example `A-5 FINISH SCHEDULE AND MATERIALS BOARD`) usually holds the board, the schedule, the owner's concept rendering and a photo of the existing room. Finishes are not code compliance. Where a finish carries a code requirement (safety glazing, nonabsorbent shower walls), say so with a note that points at the sheet with the code note.

## 6. Finish colors for other modules

Any module that needs a material color (a 3D view, a color rendering) reads it from the same block. A true-scale drawing (a plan, section or elevation drawn to scale) stays black, white and grey: QA fails a colour fill there (`grayscale`, qa-reference.md) because cities print and scan in black and white. Put a color elevation in a 3D or N.T.S. view, and name finishes on the scaled drawing with tags and a schedule:

```python
finishes.rgb(project, "T-1")      # (0.847, 0.812, 0.753), floats 0..1; None while TBD
finishes.rgb255(project, "T-1")   # (216, 207, 192); None while TBD
finishes.get(project, "T-1")      # the whole entry
finishes.entries(project)         # every finish, in project.json order
```

`project` is a loaded `Project` or the raw project dict. A finish with no color yet returns `None`: draw it as unverified (grey, hatched), never in a guessed color.

## 7. Making a placeholder image

`permitkit.raster.encode_png(width, height, pixels, color_type)` writes a PNG with the standard library. Use it for a clearly labelled placeholder while the owner's photo is on its way, and label the entry's `source` as a placeholder.
