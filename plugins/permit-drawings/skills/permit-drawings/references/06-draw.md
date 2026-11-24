# Stage 6: Draw

Read this when the reading is confirmed and the code decisions for the scope are recorded.
Then read `drawing-kit.md` for the kit (it names the task card for each sheet: plans, site, elevations and sections, sheets, QA), and `project-file.md` for the schema.

## Drawing only

Use this path when stages 1 to 5 happened elsewhere (an earlier session, another tool, a designer) or the owner asks only for sheets drawn from what exists. It skips stage logistics that have nothing to act on. It never skips a safety or honesty rule.

Always, on this path too:

- Every non-negotiable in `SKILL.md`. No code value from memory: a printed limit or citation needs a `quoted` or `primary-read` entry in `logs/code-decisions.md`, passed with `cd=`. With no such entry, print the requirement as open or leave it off, and offer stage 5 (`05-code-questions.md`).
- Every ASSUMED value that prints carries its FV tag. A PLACEHOLDER never prints. No compliance claim rests on an ASSUMED value (`kit.claim`).
- Every missing value and every open decision prints as an open item ("NOT YET PROVIDED", "OWNER TO SELECT: ..."), never as a guess, and goes in `logs/questions.md`. No "or" choice prints unresolved.
- Sections 1 to 5, 7 and 8 below in full.

Read only: `drawing-kit.md`, the one task card per sheet type you draw, `project-file.md` (and a topic card it names only when you write that field), and `examples/garage-adu/README.md`. Open an example script only for a pattern the card and `python3 -m permitkit api <modules>` do not give you; the example's `project.json` repeats what `project-file.md` shows, so skip it.

Set `project.status_label` to the gate label: a set drawn for review prints `REVIEW — NOT FOR CONSTRUCTION` (`10-release.md`, "The gates").

Skip only what does not apply:

- Site-visit list (section 0): skip the ranking when `logs/decisions.md` already holds the owner's measure-or-tag choice for each ASSUMED and PLACEHOLDER value. Otherwise tell the owner once which values are unmeasured and that each prints as an FV open item (`06-draw-checks.md` section 1, steps 5 and 6), and record the answer.
- Sheet index (`02-path.md` section 7): when the owner asks for a whole set and `logs/sheet-index.md` does not exist, write it before the first sheet, with its owner question on structural and energy sheets (a set drawn from scratch includes both). Skip it for a single sheet or detail.
- Checklist rows (section 3): when `logs/required-documents.md` exists, follow `06-draw-checks.md` section 2. With none, draw the sheets the owner asked for and tell the owner that no stage 2 checklist backs the sheet list.
- Cross-sheet text audit (section 6): it runs before each CrossBeam check and each city package. A draft that goes to neither may skip it; say so when you hand it over.
- Stage logs: write `Stage 6 done` in `logs/release.md` only when the project folder keeps the stage logs.

Done when the kit QA shows `pass: true` with no `rules` FAIL (a rule the owner chose to break carries `accepted` and shows as a WARN with its conflict labeled on the sheet), you did one vision pass (section 5), every open item prints as open, and you told the owner which items are open.

## 0. Site-visit list

Run it once, before the first permit build, and again for new values only when a CrossBeam round sends you back to stage 3. It ranks the ASSUMED and PLACEHOLDER values, turns them into one list for the owner, and records the owner's choice to measure or to draw with FV tags. Steps: `06-draw-checks.md` section 1.

## 1. One source, regenerate every time

- Every value comes from `project.json`. A sheet script reads only `project.json`.
- Write one script per sheet in `sheets/`. Use the kit's helpers for plans, schedules and title blocks.
- Every design and measured dimension comes only from `project.json`. Never type one into a sheet script or a note. Print it with `kit.text` or `kit.claim`, including inside notes.
- Layout numbers may be typed in a sheet script: view scale, cell, extents and label offsets. They place the drawing. They are not values of the building.
- A symbol position that prints no dimension (an electrical device, a fixture outline, a leader target) is a layout position. The script may compute it from the room geometry in `project.json`. Say in the script that these positions are schematic. When a reviewer checks a position (a clearance, a distance from a sink, a spacing), store it in `project.json` and dimension it.
- A code limit quoted in a note must match an entry in `logs/code-decisions.md` whose level is `quoted` or `primary-read`, and carry that entry's citation. Pass the entry ID with `cd=` so QA can find the note. The ID never prints (`05-code-questions.md` sections 3 and 6).
- To change the set, change `project.json` or a sheet script. Rebuild the whole set.
- Never edit a rendered PDF or image. Never move text on a signed PDF.

Example: an owner saw text bleeding across a box again and wrote: "Can you figure out how these docs were made, like with code or something, and see if you can work from there? Feels like you're working with further downstream docs that are difficult for you to manage." Moving back to the source generator was the most important correction in that project.

## 2. True scale

- Every view prints at its stated scale on the stated sheet size.
- The kit fails the build if a view does not fit at its stated scale. Do not shrink a view to fit. Change the scale, the sheet size or the layout.
- Kit output is the only output certified for true scale. If you draw any sheet another way, label that sheet "SCALE NOT VERIFIED".

Example: a units error made every sheet in a set print at 75 percent of its stated scale. The city approved the set without noticing. The next city might not.

## 3. Choose the sheets

Draw the sheets `logs/sheet-index.md` lists, in its order, including its structural, energy and green sheets (`02-path.md` section 7). Pick the content of each sheet from the stage 2 checklist rows, and mark each row with the sheet that answers it before each CrossBeam check: `06-draw-checks.md` section 2. Then:

1. Add a view when one view cannot carry the information. Example: a nook faced one way and a closet faced another, so one elevation could not show both. A second elevation and a key plan solved it. A layer thickness needed a section detail, "or the thickness is just a claim."
2. Show existing, demolition and proposed work as the scope needs. A demolition note on the existing plan can replace a separate demolition sheet for a small scope.
3. Keep work that needs no permit on separate sheets, outside the permit set.
4. Draw every item in the Sheet content plan of `logs/required-documents.md`: the cover data, the general notes and the site-plan items. Each note prints only what its entry's level allows (`05-code-questions.md` section 3).
5. The site plan shows each item that category question (d) or the checklist named. When a value it needs is missing, still draw the site plan, and print each missing item as an open item on the sheet, for example "LOT DIMENSIONS: NOT YET PROVIDED". Do not print internal log ids (question or code-decision ids) on a sheet. Never draw a partial site plan that does not say what is missing. Record each open item in `logs/questions.md`.
6. Compose each sheet like an architect's set: `kit-sheets.md` "Composition rules". Let `layout.arrange` pick the scales and cells, draw with named pens, hatch every cut material, tag every opening and room, put schedules and data in ruled tables, and stack panels with `Panel.fit()` so no frame is empty. On the cover, print zoning limits only from quoted rules; otherwise say who sets them.

## 4. Status drives the line style

- The kit draws each element from its status. Do not override the style by hand.
- Every ASSUMED value that prints carries its FV tag.
- Dimensions print as feet, inches and fractions. Never print decimal inches.
- Datums are written on details ("top of finished surface") so nobody misreads them on site.

## 5. Look once per build

After each build, run the kit QA. Then do one vision pass:

1. Render each page.
2. Look at each page whole, then crop and zoom into the title block, every note block and every dimension cluster.
3. Look for overlap, cut-off text, labels on top of geometry, wrong swing directions and missing tags. Look for small drawings in big empty cells, empty panels, unhatched sections and lines all of one weight. Kit QA catches text on walls, doors and swings (`collisions`), but not every case. Look anyway.
4. Fix in the source. Rebuild. Look again only at what changed.

Do not report a sheet as clean before you look at it.

## 6. Audit the text of all sheets

Before each CrossBeam check and each city package, read the text of every sheet together and look for contradictions. Run it again on every sheet after any change that came back through stage 5 or changed the scope, and after every gate label change (`10-release.md`). The checklist: `06-draw-checks.md` section 3.

## 7. Keep history

- Before you rebuild over a set the owner has seen, copy the old build to `history/` with a date and a reason in the folder name.
- Label superseded drawings as history so nobody prints them by mistake.
- Never overwrite a set that went to CrossBeam or the city. Those copies stay in `package/` or `history/`.

## 8. Show the owner the right drawing

- A discussion drawing has lettered call-outs and few notes.
- A permit sheet has the full title block, notes and code data.
- A contractor sheet has the ask in one line, numbered items and no code discussion.

After each build, give the owner the path to the current file. If the viewer may show an older copy, close and reopen it.

## Exit condition

- The kit QA report shows `pass: true`. `qa-reference.md` lists its checks. The `rules` check has no FAIL, and each value it WARNs about is on the site-visit list or in `logs/questions.md`.
- The site-visit list ran, and the owner's choice is in `logs/decisions.md` (section 0, `06-draw-checks.md` section 1).
- You read the QA citation list. Each topic cites one section and one edition.
- You did one vision pass on the current build.
- The cross-sheet text audit (`06-draw-checks.md` section 3) found no open contradiction, no code limit below `quoted`, and no "or" choice that is not resolved or printed as an owner decision.
- Each plan sheet that CrossBeam named for the touched trades is drawn (`06-draw-checks.md` section 2).
- Each item in the Sheet content plan is drawn or printed as an open item (section 3).
- `logs/release.md` has the line `Stage 6 done`.
