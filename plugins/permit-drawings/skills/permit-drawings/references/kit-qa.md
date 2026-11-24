# Card: build, QA and previews

Run QA after every build, read what it says, and fix the design or the script, never the check. The full contract (every check, every build output, every option) is in `qa-reference.md`; read a section there only when a message is unclear.

## What plan reviewers send back

QA catches the mechanical faults reviewers reject a set for: a drawing not at its printed scale, a decimal inch, an unverified value with no FV tag, overlapping text, a dimension chain that does not add up, a sheet index that disagrees with the set, a title block missing a field, a drawn value that breaks a code rule, and the drafting faults a checker sees before reading a number: every line one weight, a section with no material hatching, a plan filled in colours that turn to the same grey on a black-and-white print. It cannot catch a leader pointing at the wrong thing or a sheet that is hard to read; the preview look does.

## Run it

```
python3 -m permitkit build project.json             # full build: also two rebuilds that prove determinism
python3 -m permitkit qa build --out build/qa.json   # short report on screen, full report in the file
python3 -m permitkit preview build --dpi 50         # build/png/<id>.png; --sheet A-2 --dpi 150 to zoom
```

`--no-determinism` skips the rebuilds while you iterate. A set you submit or hand to CrossBeam is a full build that QA reports `determinism: pass` on. Run `qa` and `preview` again after every build: a build clears the old outputs and previews.

## Read the short report

It prints `pass`, each check's status, the counts, `failed` (the detail lines of each failed check) and `rules` (one line per rule). Every message names the sheet and what to change. The usual fixes:

| Check | Usual fix |
|---|---|
| `collisions` | Move the text, use a leader, or put a line that is not building linework (setback, grid, leader) on `layer="annot"`. |
| `layout` | Enlarge the cell, tighten the extents, or let `layout.arrange` choose. |
| `true_scale`, `title_block`, `sheet_index` | Do not hand-place what the kit draws: use the kit's view, title block and `sh.sheet_index`. |
| `decimal_inches` | Print lengths through `kit.text` or a Value, never a typed number. |
| `field_verify`, `claims` | Give every ASSUMED value an FV tag listed in `field_verify`; never state compliance on an unverified value. |
| `chain_closure` | The chain's segments must add up to its total: fix the Values. |
| `internal_refs` | Print the work, not the workflow: no file names, `permitkit`, tool names or log ids on a sheet. |
| `stale`, `stale_outputs` | Rebuild; QA ran on old outputs. |
| `line_weights` | Give every geometry call a pen: `cut` for what the cut passes through, `beyond` or `object` for what is seen, `fine` for detail. Never one width for everything. |
| `hatching` | Hatch each cut material (`hatch.layers` for a floor or wall build-up, `hatch.fill`, `hatch.rect`) or poche the cut walls, and add a `"hatch:<material>"` legend row for each material. If nothing in the view is cut, draw it with `profile` and `beyond`. |
| `grayscale` | Swap each colour fill for the grey the message gives, or a hatch. Cities print in black and white. |
| `view_scale` (warn) | Architectural: `scale="fit"` or `layout.arrange`. Engineering: `largest_scale(..., engineering=True)`. A `HALF SIZE` view that fits at `FULL SIZE`: pass `FULL SIZE` to `sh.view`. |
| `connections` (warn) | Ask the owner for the maker's tested detail or an engineer's calculation, record it in the entry, and show the entry with `sh.connection` (`kit-elevations-sections.md`). |
| `rules` | A FAIL is a design problem or a wrong reference: fix the design with the owner (`01-scope.md` section 6), or fix the rule entry. Never change a limit to make a rule pass. A WARN on an ASSUMED value says whether it "would pass" or "WOULD FAIL". A value with a `range` that breaks the limit at every estimate FAILs: change the design (`project-rules.md`, "Ranges in the rules check"). An estimate clear of its limit passes; one near it warns. When the owner keeps a design that breaks a rule, put the decision in the rule's `accepted` and QA warns instead (`project-rules.md`, "A design the owner keeps"). |

Read every FAIL and every WARN before a CrossBeam check.

## Read the advisory lists (they never fail QA, you still act on them)

- `advisory.unverified_text`: every note that prints an unverified value. Rewrite any entry that states or implies compliance: state the requirement and the FV tag, or measure first. This is your judgment; the kit does not pattern-match claims.
- `advisory.conditional_code_notes`: every note whose `cd=` entry has conditions. Each must print the condition with the limit, or the branch and the fact that selects it (`05-code-questions.md` sections 6 and 7).
- `advisory.sheet_fill`: each sheet's share of the drawing area in use; `low` (also `sheet_fill_low` in the short report) lists sheets under half used. Fill them (`kit-sheets.md`, "Composition rules") or say why not.
- `citations`: every code citation on the sheets. The same topic must cite the same section and edition everywhere.

## Before you call a set ready to file

Run `python3 -m permitkit measure project.json --out questions/measure-list.md` after the last build and show the owner the list (`08-package.md` section 3, step 6). A city approves measured numbers; each open tag is an item a checker can send back. The first rows are the numbers a code rule rests on, so they can change the design.

## Which file to submit

No attachments: `build/<set_name>.pdf`. With attachments: `build/<set_name>-with-attachments.pdf`, or, when the build could not merge them, `<set_name>.pdf` plus each attached PDF in the positions the build lists (`qa-reference.md`, "Build outputs").

A picture you send the owner goes in `questions/` with `--out questions --prefix Q-<id>-` (`asking-the-owner.md` section 2).
