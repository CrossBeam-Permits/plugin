# Card: sheets, cover and tables

Sheet composition, the cover sheet, notes, schedules, tables and the title block. Signatures: `python3 -m permitkit api sheet layout tables pens`. Pattern: `examples/garage-adu/sheets/a0_cover.py`.

## What plan reviewers send back

- A cover sheet missing project data the city asks for: address, APN, owner, scope of work, occupancy and construction type, areas, code basis, sheet index, preparer. The stage 2 answers (category b) list them; this card does not.
- A sheet index that disagrees with the bound sheets (QA checks it).
- General notes that cite a code edition the city has not adopted, or contradict a drawing.
- Sheets that look amateur and so get read with suspicion: tiny drawings in big empty cells, one line weight everywhere, plain-text lists where a table belongs.
- A title block missing a field, or a preparer statement the jurisdiction requires (QA checks the fields; you check the statement).

## Composition rules

1. Fill the sheet with drawing. Pick the largest standard scale that fits; let `layout.arrange` choose. Give a view `max_scale` or `min_scale` only for a reason.
2. One row of views shares a baseline (`align="bottom"`, the default).
3. Panels are as tall as their text: stack them in one column with `rest = a.fit(); b = sh.panel(rest)`, so each next panel gets the space the last one left in that column; never leave an empty frame. A panel that overflows after stacking needs a bigger column, not a smaller font. Give the space the panels leave to the views (`layout.arrange(..., area=rest)`), not to an empty band. QA lists a sheet with less than half its drawing area in use in `advisory.sheet_fill` (`qa-reference.md`, "Advisory list").
4. Three or four text sizes per sheet (`pens.TEXT`). Notes and table cells 7 to 7.8 pt on ARCH D.
5. Line weight says what a line is. Use a pen name, never a typed width. QA fails a drawing with no cut-weight line or with every line about one weight (`line_weights`).
6. Every cut material is hatched, and the sheet carries a legend. QA fails cut lines with no material and warns on a hatched material in no legend (`hatching`).
7. Black and white. Fill areas with greys or hatches, never colours: cities print and scan in black and white (`grayscale`). Colour belongs only in a photo, a 3D view or a finish schedule.
8. Every opening has a tag and a schedule row; every room a room tag; every section and elevation a marker.
9. The cover carries ruled project-data and zoning tables, the sheet index as a table, and slots for a 3D view and a vicinity map.

## Paper and layout

- Sheet sizes: `ARCH_E`, `ARCH_D` (default, drawing area about 26 1/2 x 22 3/8 in.), `ARCH_C`, `ANSI_B`, `LETTER`. The right column holds the general notes over the title block.
- `sh.view(...)` and `sh.panel(...)` take `cell=(x, y, w, h)` in inches from the drawing-area lower-left. Cells may not overlap. A view needs about 3/4 in. under it for its title.
- `layout.arrange(sh, [{"title", "extents", "max_scale", "min_scale", "scale", "margin"}, ...], area=(x, y, w, h), same_scale=False, fill="even")` picks rows, scales and cells and returns the Views. Scales come down together, so views of one size get one scale; `same_scale=True` forces it (elevations, plans of one building). Rows take the height they need; `fill` places the spare height: `"even"` (equal space above each row and under the last), `"top"` (rows packed at the top) or `"stretch"` (rows grow, the drawing sits at the foot of its cell); when the chosen scales leave less than half the area holding drawings, a detail at 3" = 1'-0" with no scale limit of its own may grow to HALF SIZE or FULL SIZE (`grow=False` keeps the 3" ceiling); `layout.plan` returns the choice without drawing; `layout.split(area, fractions, "x" | "y", gap)`; `layout.cover_cells(sh)` returns a title-sheet composition.
- **Detail scales**: `FULL SIZE` (1:1) and `HALF SIZE` (1:2) print as those words. Use them for a small detail, such as a threshold, a flashing or a tile edge, that 3" = 1'-0" draws too small. Pass one to `sh.view` as the scale, or give the view `"max_scale": "FULL SIZE"` (or `"HALF SIZE"`) in `layout.arrange` to let it pick up to that size; without a size scale in `max_scale` or `min_scale`, `arrange` stops at 3" = 1'-0" unless the sheet would be under half used (`grow`, above). A view with a size scale in `max_scale` is a detail: when big views on the same sheet would leave it under 3" = 1'-0" (then 1-1/2"), `arrange` brings them down one step so the detail reaches it; a view's own `min_scale` (a plan the city wants at 1/4") is never broken. A FULL SIZE view that does not fit its cell is offered HALF SIZE or an architectural scale.
- `sh.largest_scale(extents, cell)` gives the largest standard scale that fits. Paper inches per foot = 12 x points-per-inch / 72.
- `sh.side_panel(title)`: a panel in the right column for a legend or keynotes; call `sh.notes()` first on a sheet with general notes. `sh.key_plan(draw, extents)`: a small key plan in the title block. `sh.slot(name, cell, title)`: a frame for a picture that prints "<TITLE> TO BE PLACED" until filled. `sh.connection(id, cell)`: the labeled spot for a load-carrying connection (`kit-elevations-sections.md`).

## Panels and tables

- Free text in a view: `v.text(x, y, s, size=..., rot=90)` (real point, `rot` in degrees; there is no `rotate`). Text in a panel goes through the panel's calls below.

- `Panel`: `heading`, `banner` (cover title lines), `para`, `numbered`, `table` (mark a column `"wrap"`), `legend`, `grid_table(columns, rows)` (ruled, with `("group", "SETBACKS")` bands), `opening_schedule`, `fv_schedule(grid=True)`, `columns([(heading, [notes]), ...], ncols=2)`. A panel that overflows raises `LayoutError`; the kit never clips text. A `kit.text` or `kit.claim` in a cell keeps its keys, FV tags and claim, so QA checks it like a note.
- Legend kinds: `poche_e`, `poche_n`, `demo`, `measured`, `assumed`, `light`, `recept`, `switch`, `smoke`, `smoke_co`, `fv`, `cloud`, `property_line`, `setback`, plus `"hatch:<material>"`, `"pen:<name>"`, `"tag:<shape>:<mark>"`.
- `sh.notes([...])` fills the notes column and numbers the notes 1, 2, 3 in order. A blank item (`""` or `None`) adds space and takes no number. Never type the number into a note (it would print `1. 1.`); to renumber, reorder the list. `Panel.numbered(items, start=1)` does the same in a panel; pass `start` to carry one list across two panels. `sh.sheet_index(panel, grid=True)` prints the sheet list from `project.json`; never type a sheet list (QA fails it).
- `tables.zoning_table` is on the site card (`kit-site.md`).

## Title block

Drawn for you from `project.json`: preparer box (name, role, any `firm`, `address`, `phone`, `email`, `license`), project box (title, address, owner, contractor, APN, permit number when present), revisions, sheet title, sheet number with "n OF m", scale ("AS NOTED" when views differ), date, status label (the gate, `10-release.md`), the preparer statement when there is one, a signature line and a stamp box. Leave `preparer.statement` out when the jurisdiction needs none or a professional's stamp carries it.

## Sheet numbering (guidance)

| Sheet | Usual content |
|---|---|
| A-0 | Cover: project data, scope, code data, sheet index, vicinity map, preparer statement |
| A-0.1 | Plot plan and general notes |
| A-1.x / A-2.x | Existing floor plans; demolition plans |
| A-3.x | Proposed floor plans, with electrical when small |
| A-4.x / A-5.x | Elevations; sections, details and schedules |
| T-x | Title 24 energy and CALGreen (`energy-and-green.md`) |

Leave out what the scope does not need. External documents (energy forms, product data, city forms) go in `sheets` with `attach`, in the order the city asks for. Each `attach` path is relative to the project folder with no `..`; the kit refuses a path that leads outside it, also through a symbolic link. Photos, renderings, vicinity maps and finish schedules: `images-and-finishes.md`.
