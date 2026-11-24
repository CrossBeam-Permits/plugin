# Bring your own drawing: a self-check against the rules

Read this when the owner already has drawings (a hand sketch, plans from other CAD software, a PDF from a designer) and wants to know, before paying for a CrossBeam plan check, whether the drawn values meet the city's rules.

This is a quick check of the numbers on the drawing against the rules for what it shows. It is not a CrossBeam plan check and not a city review. It does not check completeness, notes, documents or packaging. Say so once when you give the result.

## 1. Read the drawing

1. Copy the files into `sources/`. Record each one in `project.json` `sources` with its kind (`sketch`, `plan`, `scan`), and an `orientation_note` for a sketch or scan.
2. Read every sheet. For a PDF, read the text and look at each page. For a hand sketch, rotate it upright first (`03-measure.md` section 1).
3. Write down the scope the drawing shows, the city, the address and each room's use as the drawing labels it. Ask the owner to confirm the room uses and the city (`01-scope.md` section 2). A room label is the owner's declaration, not yours to change.

## 2. List the elements and their numbers

For each thing the rules may govern, write the element and each number the drawing gives for it, with the sheet it came from:

| Element | Number on the drawing | Where | Status |
|---|---|---|---|
| bedroom 2 emergency escape window | 24 x 48 in. net opening, 40 in. sill | A-2, window schedule | PROPOSED (new window) |
| hall door to bedroom 2 | 2'-8" | A-2 | MEASURED (owner taped it) |
| office ceiling height | 7'-4" | A-3, section 1 | ASSUMED (owner: "from the old plans") |

- Take only numbers the drawing prints. A number you scale off the drawing is not a printed number. Write "not dimensioned" and ask the owner, or have it taped.
- Ask the owner where each existing number came from. A number the owner taped is MEASURED. Any other existing number is ASSUMED with an FV tag, with its source in `note`. A number for new work the owner chose is PROPOSED.

Write each number into a short `project.json` as a value with that status and the drawing as its source (`project-file.md`). You do not need sheet scripts for a self-check. `validate` and `rules` work on the values alone. The file still needs the `project` fields (`project-file.md`, "Project fields"); write `OWNER NAME PENDING` until the name is known.

## 3. Get the rules

Call `crossbeam_rules` once for the city, with every element from section 2 (`05-code-questions.md` section 0). Copy each `kit_checks` item into `rules`, one entry per drawn value. Ask `crossbeam_ask` about each element in `misses`.

## 4. Run the check

Set `PYTHONPATH` to the skill's `scripts` folder (`drawing-kit.md`, "Commands"). Then run:

```
python3 -m permitkit validate project.json
python3 -m permitkit rules project.json
```

`rules` needs no sheets and no build. It prints `counts`, one line per rule with FAIL first, and the full rows (`qa-reference.md`, "The QA gate"). It exits 1 when a rule fails.

When the owner also wants kit sheets, draw them (stage 6) and use `python3 -m permitkit qa build`. Its `rules` check is the same report.

## 5. Report to the owner

Give one line per rule, FAIL first, then WARN, then PASS:

- the element and the rule's citation;
- the number on the drawing and the limit, in the same unit;
- PASS, FAIL, or "not measured" for a WARN;
- for a FAIL, what would fix it, as options (`01-scope.md` section 6). Do not change the owner's drawing for them.

Then list the elements CrossBeam had no rule for, and the rules whose limit is `unquoted` (`05-code-questions.md` section 3). Say that a PASS on an ASSUMED number means the estimate is clear of the limit, not that it is measured: it holds only after the tape confirms it.

End with the next step: fix the FAILs and measure the WARNs, then run a CrossBeam plan check (stage 7), or redraw the set with the kit (stage 3 onward). Record the report in `logs/decisions.md` with the date.

## 6. Draw it and check it, no permit

When the owner asks you to draw something and say whether it meets code, but not for a permit ("draw this stair detail and tell me if it meets code"), combine this card with `06-draw.md`, "Drawing only":

1. Sections 1 to 4 of this card give the numbers and the rules: the values in `project.json` with their status and source, one `crossbeam_rules` call for the elements, and the `rules` entries.
2. `06-draw.md`, "Drawing only", and the task card for what you draw (a detail or build-up: `kit-elevations-sections.md`) give the sheet. Its rules apply in full: FV tags, open items, no limit without a `quoted` or `primary-read` entry.
3. Skip what only a permit needs: the permit path and the required documents (stage 2), the cover sheet and sheet index, the CrossBeam check, packaging and the city (stages 7 to 10). Do not ask the owner permit questions. Print the gate label `REVIEW — NOT FOR CONSTRUCTION`.
4. Build and run `qa build`. Its `rules` check is the report of section 5; give it the same way, with the drawing attached.
5. If an answer you got says the work needs a permit, tell the owner once, with the citation, and offer the permit path. Do not decide that from memory.
