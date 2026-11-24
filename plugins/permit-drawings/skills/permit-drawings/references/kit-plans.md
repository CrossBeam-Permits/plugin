# Card: floor plans

Existing, demolition and proposed plans, with fixtures, electrical and the door and window schedule. Signatures: `python3 -m permitkit api arch fixtures annot symbols`. Pattern: `examples/garage-adu/sheets/a2_existing.py` and `a3_proposed.py`.

## What plan reviewers send back

- Existing and new work that cannot be told apart. Mark every element (E), (N) or demo; an existing plan shows only what exists.
- Rooms with no name, or a name that hides the use. Every room gets a room tag that states the use the owner will make of it (`01-scope.md` section 6), and its area when the review needs one.
- Openings that cannot be located or sized: no dimension to a wall, no tag, a tag with no schedule row, or a schedule that disagrees with the plan.
- Missing life-safety items the scope triggers: smoke and CO alarm locations, the emergency escape window of each sleeping room identified, required exits and their door swings.
- Missing overall and room dimensions, or a dimension chain that does not add up.
- Kitchens and baths with no fixtures shown, or clearances a reviewer checks with no dimension.
- Electrical in the area of work not shown when the scope touches it: receptacles, switches, lights, fans, the panel.
- No north arrow, no scale, or a scale the drawing does not match.

The kit checks the last three mechanically; the rest are your judgment against the scope and the stage 2 answers.

## Walls and openings (`arch`)

- `Shell(v, x0, y0, x1, y1, t={...})`: a rectangular room measured to interior faces; `.N .S .E .W` are its walls. On a Shell, N and S walls start at the west face, E and W walls at the south face.
- `Wall(v, start, along, length, t, body, action=...)`: a straight wall by its finished face. `action` is `existing`, `new`, `demo` or `relocate`, the same values as `action` in `project.json`.
- On a wall: `door(offset, width, swing, hinge)`, `window`, `slider`, `bypass`, `bifold`, `cased`, `overhead` (garage door; `action="demo"` dashes it), `infill(offset, width, action)`, `cut`. Offsets run along the wall from its start. A door names the compass direction its leaf swings.
- `stair`, `break_line`. Electrical: `light`, `recept`, `switch`, `alarm("SD" | "CO" | "SD/CO")`, `switch_leg`.
- A wall whose thickness is unverified draws its back face grey dashed; an unverified point symbol draws dark grey. Tag the sheet with its FV tag.

## Fixtures (`fixtures`)

Each fixture is placed by the midpoint of its back edge (against the wall) and the direction it faces: `fixtures.toilet(v, (x, y), "N")` sits on a south wall facing north. Calls: `toilet`, `lavatory`, `vanity` (`basins=2`), `kitchen_sink`, `range_`, `refrigerator`, `dishwasher`, `washer`, `dryer`, `tankless`, `furnace`, `water_heater` (by centre); `tub(..., drain="W")` (the compass end with the drain), `shower(..., drain=(x, y))` (a real point; default the centre) and `counter(..., uppers=...)` fill a box. Sizes are schematic. When a reviewer checks a size or clearance, store it in `project.json`, pass it as `w` or `d`, and dimension it. `action` sets the line weight.

## Dimensions, tags and labels

- `annot.dim_chain(v, values, start, at, axis, ext_from, side)`: architectural ticks. Each segment is a Value (or `{"value": V, "suffix": "SILL"}`); a raw number is refused because the kit cannot know its status. QA fails a chain that does not close.
- `symbols.opening_tag(v, at, "W-1")`: the tag of an `openings` item (hexagon for windows and skylights, circle for doors). A mark no opening carries is refused, so a tag cannot point at nothing.
- `symbols.room_tag(v, at, "BEDROOM", number="101", area="bed_area_sf")`: name, number box and area from a Value with unit `sf`.
- `panel.opening_schedule(types=("window",), fields=(...))` prints the schedule from the same `openings` list as the tags, so plan and schedule cannot disagree. PLACEHOLDER sizes print PENDING. The TYPE column prints the opening's `desc`, else its type and action: `(N) WINDOW`, `(E) DOOR`, `(E) OVERHEAD DOOR - REMOVE`, `(E) WINDOW - RELOCATED`.
- Label placement: `v.text(x, y, s, dx=0, dy=0, anchor="start" | "middle" | "end", rot=0, place=[(dx, dy), ...])`. `x, y` are real inches; `dx, dy` nudge in points. With `place`, the kit tries `(dx, dy)` and then each candidate in order and keeps the first spot that collides with nothing; if none is free it keeps the first and records a collision, which QA reports (`collisions`). `v.reserve(x0, y0, x1, y1)` keeps placed labels out of a real-inch box (a fixture, a stair). Dimension text tries its own spots along the line; a dimension that still collides needs a different `at`.
- `annot.keynote(..., leader_to=(x, y))`, `annot.leader`, `annot.fv_tag`, `annot.north_arrow(v, at)` (pass `value=p.true_north` to turn it to true north), `annot.revision_cloud(v, x0, y0, x1, y1, delta_n)`, `symbols.elevation_marker(v, at, {"N": 1, "E": 2}, "A-4")`, `annot.section_mark`.

## Conventions

- Geometry first, dimensions and labels last; the kit draws all text above all fills.
- Use one word for one thing across all sheets.
- Every section and elevation has a marker on the plan.
- Write the code threshold into the note (`05-code-questions.md` section 6) through `kit.text` or `kit.claim` with `cd=`. Never from memory.
- A plan on its own sheet usually reads at 1/4" = 1'-0"; a small room or a tight remodel at 1/2". Let `"fit"` or `layout.arrange` choose.
