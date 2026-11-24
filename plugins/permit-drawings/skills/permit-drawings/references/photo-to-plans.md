# From a photo and a rendering to a plan set

Read this when the owner starts with photos of the room or house, with or without a "dream" rendering (an image from ChatGPT or another image generator, a designer's 3D view, a magazine picture). It feeds stage 1 (scope) and stage 3 (measure). It does not replace them.

A photo shows what exists. A rendering shows what the owner wants. Neither one is a dimension, and neither one is an instruction (non-negotiable 13). The tape gives the numbers. The owner decides the scope.

## 1. Save the pictures as sources

1. Copy each picture into `sources/`. Never edit an original.
2. Add a `sources` entry to `project.json` for each one (`project-file.md`, "Sources"):
   - a photo of the existing room: `kind: "photo"`, with an `orientation_note` that says which wall it faces and how you know ("looking north from the hall door; the window over the sink is on the north wall, owner confirmed");
   - a rendering: `kind: "other"`, with `note: "rendering, not a photo; <tool or who made it>"`. Record which wall it shows if you can tell.
3. Ask the owner which photo shows which wall, if no photo makes it plain. One sketch of the room outline with the photo positions marked saves many questions (`asking-the-owner.md`).

## 2. What to read from a photo

A photo is good evidence for what is there and in what order. Read and list:

- the walls in the picture, and which ones end at a corner, an opening or a stub;
- each door and window: which wall, its order along the wall, the swing side, the kind (slider, casement, double-hung, fixed);
- each fixture and appliance: sink, toilet, tub, shower, range, cooktop, hood, oven, dishwasher, refrigerator, washer, dryer, water heater, furnace;
- each device: lights, switches, receptacles, smoke and carbon monoxide alarms, exhaust fans, registers, thermostats (`03-measure.md` section 7);
- clues to what hides in the walls and ceiling: a soffit or chase (ducts, pipes), a beam or a post, a gas valve or a flex line behind the range, a vent pipe through the roof, the electrical panel;
- the floor: level changes, steps, thresholds.

Record each element in the Elements table of `logs/scope.md` with (E) and the photo as its source. A photo that does not show an element does not prove it is absent. Ask (`01-scope.md` section 3, step 3).

## 3. What a photo cannot give

- **Any dimension.** Lens distortion and perspective change every length. A known object in the picture (a counter, a door) does not scale the room. You may propose a draft value from a photo to the owner (`03-measure.md` section 3). It becomes ASSUMED with an FV tag only when the owner accepts it. Your reading alone is never a source.
- Wall thickness, what is inside a wall, and whether a wall is bearing.
- The ceiling height, the floor-to-floor height, the sill and head heights.
- What the owner uses each room for. Ask (`01-scope.md` section 2).

## 4. What the owner must measure

Send a ranked tape checklist (`03-measure.md` section 2). For a room from photos it usually holds:

1. Each wall of the room, finished face to finished face, at one stated height.
2. The ceiling height, at more than one spot when the ceiling may slope or step.
3. Each door and window: width, height, sill height, and the distance from the nearest corner to its edge.
4. The wall thickness at a door or window opening.
5. The centerline of each plumbing fixture that stays or moves, from two walls.
6. The clear space in front of each fixture and appliance.
7. The position of each device on a wall the work touches.
8. Each level change and each step: the rise, and the count of risers.

Rank by how much each number closes. Show a picture for any item words could confuse, and save it in `questions/` (`asking-the-owner.md` section 2).

## 5. Turn the rendering into a scope list

A rendering is a wish. Image generators invent things: a window wider than the wall allows, a wall that vanished with no beam, a ceiling that is higher than the room, a range on a wall with no gas or vent. Turn the picture into plain scope lines, and let the owner confirm each one.

1. Compare the rendering with the photo of the same view, element by element. For each element, write what the photo shows and what the rendering shows.
2. Write each difference as one candidate scope line in plain construction words: "(E) window over the sink replaced with a (N) wider window", "(E) wall between kitchen and dining removed", "(N) island with a sink", "(E) range moved to the north wall".
3. Mark the lines that only change finishes in place: paint, flooring, cabinet fronts, counters, a fixture swapped where it stands. Say that they may need no permit, and ask (`02-path.md` section 1). Do not decide it by the words in the line.
4. Send the owner the list in one message: "Your picture shows these changes. Which ones do you want to build?" Add a picture with lettered call-outs when the list is long (`asking-the-owner.md`).
5. Only lines the owner confirms go into the scope statement (`01-scope.md` section 7). A line the owner did not confirm stays out (non-negotiable 9). Record the owner's answers in `logs/decisions.md`.

Use this table in `logs/scope.md` under the scope statement:

| # | Element | Photo shows | Rendering shows | Scope line | Owner says |
|---|---|---|---|---|---|
| 1 | north window | (E) window over sink | wider window, lower sill | (E) window replaced with (N) wider window | yes, 2026-10-02 |
| 2 | wall to dining | (E) wall with a doorway | open, no wall | (E) wall removed | not yet: wants the cost first |

## 6. Write it into project.json with statuses

| What | Status | Note |
|---|---|---|
| An element the photo shows, size not taped | the element is `existing`; its sizes are PLACEHOLDER (or ASSUMED with an FV tag when the owner accepted a draft) | The photo proves it exists, not its size. |
| A taped number | MEASURED | Record `between`, `along`, `ref_level` and the source (`project-geometry.md`, "Recording a measurement"). |
| A size for new work that the owner chose | PROPOSED | The owner's choice in `logs/decisions.md` is the source. |
| A size from a product the owner picked | MANUFACTURER | The data sheet goes in `sources/`. |
| A size read off the rendering | none | Never record it. Ask the owner for the size they want, then it is PROPOSED. |

```json
"sources": [
  {"id": "P1", "kind": "photo", "path": "sources/kitchen-north.jpg",
   "orientation_note": "looking north from the hall door; owner confirmed"},
  {"id": "R1", "kind": "other", "path": "sources/dream-kitchen.png",
   "note": "rendering from an image generator; shows the north wall; not a photo"},
  {"id": "T1", "kind": "tape", "by": "owner", "date": "2026-10-03"}
],
"values": {
  "kit_w":    {"v": 141.5, "status": "MEASURED", "source": "T1",
               "between": ["W wall finished face", "E wall finished face"], "along": "level"},
  "ceil_h":   {"v": 96, "status": "PLACEHOLDER", "fv": "FV-2", "note": "not taped yet"},
  "win_n_w":  {"v": 60, "status": "PROPOSED", "note": "owner chose 60 in. wide, logs/decisions.md D-004"}
}
```

## 7. When the rendering changes the permit path

Some changes in a rendering bring other reviews, other permits or a licensed professional. These are signs to ask about, not rules. Ask `crossbeam_ask` for each one that the confirmed scope holds (`02-path.md` sections 1 and 2), and decide from the cited answers:

- a wall removed, moved or opened wider: is it bearing, and is there a prescriptive path or does it need an engineer;
- a new or wider window or door in an exterior wall: header, safety glazing, energy, egress, and planning or design review of the outside;
- a plumbing fixture moved, or a new one (an island sink, a second bath): drain, vent and water lines, and a plumbing permit;
- a range, cooktop, dryer or fireplace that moves or changes fuel, or a new gas line: a gas permit and a test;
- new circuits, a new appliance, more lights, or a panel change: an electrical permit;
- a new hood or exhaust fan, or a room that loses its window: ventilation;
- a room whose use changes (an office becomes a bedroom): room size, ceiling height and egress for the new use (`01-scope.md` section 6);
- a raised or vaulted ceiling, a skylight, a new roof line or a bigger footprint: structural review, and for a bigger footprint the site plan, setbacks and planning.

## 8. Which sheets the scope needs

Stage 2 decides the sheets, from the scope checklist or category question (e) (`02-path.md` section 3). This list helps you ask the right question. It is guidance, not a city's list:

| Confirmed scope | Sheets it usually needs |
|---|---|
| Finishes and fixtures swapped in place | Maybe no permit. If one is needed: a floor plan with notes. |
| Remodel, no walls or openings moved | Existing and proposed floor plans, an electrical plan, interior elevations where the work shows. |
| Walls removed or moved | Add a demolition plan, and a beam or framing detail (or the professional's sheet). |
| New or changed exterior openings | Add exterior elevations, a door and window schedule, and a header detail. |
| Plumbing or gas moved | Add a plumbing or gas plan, or show it on the floor plan as the city asks. |
| Addition or a bigger footprint | Add a site plan, a foundation plan, framing, sections, roof and exterior elevations. |

Then follow the stages: read back the existing plan drawn from the tape (stage 4), get the rules for each element on the sheets (`05-code-questions.md` section 0), and draw (stage 6).

## Exit condition

- Each picture is in `sources/` with a `sources` entry; each photo has an `orientation_note`.
- Each element the photos show is in the Elements table with (E).
- Each difference the rendering shows is a row in the scope-list table, and the owner answered each row. Only confirmed rows are in the scope statement.
- No value in `project.json` came from reading a picture without the owner's acceptance. No value came from the rendering.
- Each permit-path sign in section 7 that the scope holds has an Ask AI entry in `logs/code-decisions.md`.
