# Card: elevations and sections

Exterior elevations, building sections, details and roofs. Signatures: `python3 -m permitkit api section hatch symbols pens`. Pattern: `examples/garage-adu/sheets/a4_elev.py` and `a5_section.py`.

## What plan reviewers send back

- Missing elevations. Show every side the work changes; for new buildings and additions, all four.
- Heights with no datum: the building height measured from grade the way the city measures it, plate and ridge heights, finished floor above grade. Level markers from Values, never typed numbers.
- Roof pitch, roofing, siding and other materials not called out.
- Openings on the elevation that disagree with the plan or the schedule (count, size, sill or head).
- A section that stops short: it should run from footing and grade to the roof, showing the floor, wall and roof assemblies, insulation, ceiling height and headroom where a rule controls them.
- One line weight everywhere, so nothing reads as cut (QA `line_weights` fails it).
- Cut materials not hatched, and no materials legend (QA `hatching`).
- Colour fills: cities print and scan in black and white (QA `grayscale`).
- A connection that carries a load drawn "schematic" with nothing behind it: Building asks for the maker's tested detail or an engineer's calculation (below).
- No section marker on the plan, or a marker that names the wrong sheet.

## Axes

x runs along the view as seen, y up, in real inches. y = 0 is usually finished floor; say what it is in the view title or a note. Draw elevations and sections from the same values as the plans: wall lengths, opening offsets, sill and head heights, plate height and roof pitch. Never retype a number.

## Calls

- `section.roof_profile(v, x0, x1, plate, pitch, overhang, kind="gable" | "shed")` returns `{"ridge": y, "eave": y}` (real inches, bare numbers) for placing a marker; `roof_eave` draws the eave side of a gable roof; `pitch_symbol(v, at, pitch)` the slope triangle.
- `section.siding(kind=...)`: `"lap"` (courses every `exposure`, default 7"), `"board"` (board and batten, battens every `exposure`, default 12"), `"stucco"` (stipple), or `"plain"` (no texture, for a material that is unknown or that the kit does not draw; name it in a note or keynote).
- A printed ridge height is a DERIVED value, never the number roof_profile returns. Convert the slope in a value of its own, so no `expr` adds inches to in/ft (`validate` warns `expr-unit-mix` on that): `"roof_rise": {"expr": "ext_w / 2 / 12 * roof_pitch", "status": "DERIVED"}`, then `"ridge_h": {"expr": "plate + roof_rise + roof_t", "status": "DERIVED"}` (`roof_t` is the roof thickness you pass, or the fascia; when nobody gave it, make it ASSUMED with an FV tag, so the ridge prints with the tag). Print it with `level_marker(v, x, p.v("ridge_h"), "T.O. RIDGE", p["ridge_h"])`.
- A roof pitch is a Value with `unit: "in/ft"` (a 4:12 roof is `4`). It is also the slope unit the `rules` check compares, so a roof-slope rule checks the value the elevation draws. Any other unit is refused.
- `arch.elev_window(kind=...)`: `"XO"` / `"OX"` (slider, X on the moving panel as seen), `"casement"` (swing lines meet at `hinge`), `"fixed"` (no operation mark), `"single-hung"` (meeting rail, up arrow in the lower sash), `"double-hung"` (arrows in both sashes). Any other kind raises. `arch.elev_door(kind="panel" | "dutch")`, `arch.elev_slider`.
- Elevations of one building share a scale: pass `same_scale=True` to `layout.arrange`.
- Details and build-ups (a floor or wall assembly, a threshold, a flashing) read at `3" = 1'-0"`, `HALF SIZE` or `FULL SIZE` (`kit-sheets.md`, "Detail scales"). At a size scale a 1/8 in. layer is 1/8 in. on paper, so set `extents` to the detail's real inches plus room for leaders and notes.
- `hatch.rect(v, x0, y0, x1, y1, "concrete", outline="cut")`, `hatch.fill(v, pts, material)`. Materials: `concrete`, `earth`, `fill`, `gravel`, `sand`, `mortar`, `plaster`, `batt`, `rigid`, `masonry`, `cmu`, `wood`, `blocking`, `plywood`, `gypsum`, `steel`, `tile`, `planting`, `pavers`, `solid`. Hatches are clipped to the shape and ignored for text collisions.
- `hatch.layers(v, face, (bottom, top), [(stucco_t, "plaster"), (wsp_t, "plywood"), (stud_d, "batt"), (gyp_t, "gypsum")])` draws a built-up wall (axis `"x"`) or floor/roof (axis `"y"`) from Values and returns the far face.
- `hatch.grade(v, x0, x1, y, gaps=[(a, b)], label="FINISH GRADE")`: grade with earth below, open where a footing passes.
- `symbols.level_marker(v, x, y, "T.O. PLATE", "plate_h", reach_pt=40, line=False)`: target, name and height from a value key.
- Pens: `cut` heaviest, then `cut_med`, `profile`, `object`, `beyond`, `fine`, `hatch`; `grade` for the ground line. `pens.kw("beyond", status="ASSUMED")` gives grey dashed at the same width. Every geometry call takes a pen, never a typed width: in a section or detail, the members, slabs, sheathing and posts the cut passes through are `cut` (thin ones `cut_med`) and each is hatched; what is seen beyond the cut is `beyond`; trim, joints and glass are `fine`. In an elevation nothing is cut: the outline is `profile`, the rest `beyond` and `fine`.
- `section.grade`, `earth`, `concrete`, `insulation`, `wood_cut` and `level_marker` are short aliases of the hatch and symbol calls.

## A section sheet

```python
from permitkit import hatch, layout, symbols
from permitkit.sheet import columns_height

def build(kit):
    p = kit.project
    sh = kit.sheet("A-5")
    dw, dh = sh.drawing_area_in
    band = columns_height(FOUNDATION_NOTES, dw, ncols=3) + 0.3
    sec, = layout.arrange(sh, [{"title": "SECTION A", "extents": (-60, -40, 260, 200),
                                "max_scale": '3/4" = 1\'-0"'}], area=(0, band + 0.4, dw, dh - band - 0.4))
    hatch.rect(sec, 0, -24, 15, -12, "concrete", outline="cut")            # footing
    hatch.grade(sec, -60, 260, 0, gaps=[(0, 15)])
    hatch.layers(sec, 0, (p.v("floor_h"), p.v("plate_h")),
                 [(p["stucco_t"], "plaster"), (p["wsp_t"], "plywood"), (p["stud_d"], "batt"), (p["gyp_t"], "gypsum")])
    symbols.level_marker(sec, 240, p.v("plate_h"), "T.O. PLATE", value_key="plate_h")
    sh.panel((0, 0, dw, band)).columns(FOUNDATION_NOTES, ncols=3)
    sh.side_panel("MATERIALS").legend([("hatch:concrete", "CONCRETE"), ("hatch:earth", "UNDISTURBED SOIL"),
                                       ("hatch:batt", "BATT INSULATION")])
    return sh
```

## Connections that carry a load

A post, ledger, hanger, post base or bracket that a code rule loads (a newel post that takes the guard or handrail load, a grab-bar backing, a deck ledger) needs a basis Building can check: the maker's tested detail (with its evaluation report and rated load) or an engineer's calculation. The kit sizes none of them, and a drawing marked "schematic, no capacity shown" alone draws a correction.

1. When a drawing shows one, add it to `connections` in `project.json`: `{"id": "C-1", "what": "NEWEL POST D TO THE STAIR STRINGER", "basis": "open"}`. A `load` prints only with the `cd` of its code decision.
2. Ask the owner once which basis they want (`asking-the-owner.md`): a connector or post kit whose maker publishes a tested detail and rated load, or an engineer. Record the answer in `logs/decisions.md`.
3. Give it a spot next to the drawing: `sh.connection("C-1", cell)` draws a framed CONNECTION C-1 block with what it joins, its load and its basis. While `basis` is `open` it prints that the maker's tested detail or an engineer's calculation goes there. Point to it from the drawing with a diamond tag, `symbols.tag(v, at, "C-1", shape="diamond")`, and a leader, or a note that names C-1.
4. When the detail or calculation arrives, set `basis` to `manufacturer` or `engineer`, write `evidence` (product, report number and table, or the engineer and the calculation), place the maker's drawing in `slot.image_cell` if there is one, attach the report or calculation in `sheets`, and rebuild.

QA warns on every `open` connection and on one no sheet shows. An open connection is an open item at the city package (`08-package.md` section 3, step 6).

Framing sizes on a section come from `struct.size_label` when the structural module is installed (`structural.md`); otherwise print BY ENGINEER, never a size from memory.
