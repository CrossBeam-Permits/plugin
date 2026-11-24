# Drawing a permit set with permitkit

`permitkit` is a drafting kit in standard-library Python. It runs unchanged in Claude Code, Claude Desktop, Cowork and a bare Linux sandbox, and writes vector PDFs with the built-in Helvetica fonts. You write one short script per sheet; the script reads every number from `project.json` (`project-file.md`). The kit carries what is easy to get wrong: true scale, status line styles, the title block, fractions, collision checks and the QA gate. Only kit output is certified for true scale; label anything else "SCALE NOT VERIFIED".

This card is what every sheet needs. Then read the one task card for the sheet you are drawing:

| Drawing | Card |
|---|---|
| Floor plans: existing, demolition, proposed, electrical, fixtures, door and window schedules | `kit-plans.md` |
| Site or plot plan, zoning table | `kit-site.md` |
| Elevations, building sections, details, roof | `kit-elevations-sections.md` |
| Cover sheet, notes, schedules, tables, sheet composition, title block | `kit-sheets.md` |
| Build outputs, the QA gate, previews, which file to submit | `kit-qa.md` |

For exact, current signatures ask the code, in three depths: `python3 -m permitkit api` is a short index of every call; `api arch fixtures symbols` gives each call's signature and one line (name every module the sheet uses in one call); `api tables.zoning_table` or `api Panel.fit` gives one call's whole docstring with its module's notes (row formats, cell names, return values). It reads the code, so it is never out of date.

## Commands

Set `PYTHONPATH` to the skill's `scripts` folder, then run from the folder that holds `project.json`:

```
python3 -m permitkit validate project.json          # check the model
python3 -m permitkit new-sheet A-3.1 --title "PROPOSED FLOOR PLAN"   # write a script template
python3 -m permitkit build project.json             # build every sheet into ./build
python3 -m permitkit qa build --out build/qa.json   # the QA gate: prints the result and each failure
python3 -m permitkit rules project.json             # only the code-rules check, no build
python3 -m permitkit measure project.json --out questions/measure-list.md   # what to tape before filing
python3 -m permitkit preview build --dpi 50         # PNG previews to look at once
python3 -m permitkit api [module ...]               # every drawing call with its signature
python3 -m permitkit modules                        # which optional modules are installed
```

Optional modules have their own commands and references: `energy` and `green` (`energy-and-green.md`), `struct` (`structural.md`), 3D views (`3d-views.md`). When one is not installed, the kit says how to fetch it (`00-connect.md` section 3).

## Start from the worked example

`examples/garage-adu/` is a complete six-sheet set for a garage-to-ADU conversion: cover, site plan, existing/demolition plan, proposed plan with fixtures and schedules, four elevations, and a section. It passes QA and a unit test rebuilds it. Read its `README.md` first: it maps each sheet script to the pattern it shows, so you open only the script for the sheet you are drawing. Copy the patterns, never the values (they are invented). To see it, copy the folder to a scratch folder and build it there.

`new-sheet` writes the script into `sheets/` and prints an `add_to_project_sheets` entry. Add it to `sheets` in `project.json` in bound order; the build draws only the sheets listed there. A script may `import common` (or any module in `sheets/`); never change `sys.path`. Scripts never write files.

## A sheet script

```python
from permitkit import annot, arch, symbols


def build(kit):
    p = kit.project
    sh = kit.sheet("A-2")                       # title comes from project.json
    W, D = p.v("room_w"), p.v("room_d")

    # 1. Place the drawing at a true scale ("fit" picks the largest standard scale).
    v = sh.view("PROPOSED FLOOR PLAN", '1/2" = 1\'-0"',
                extents=(-36, -36, 252, 200),   # real inches, room for dimensions and labels
                cell=(0, 0, 18, 22))            # paper inches from the drawing-area lower-left

    # 2. Geometry first, in real inches. x east, y north.
    t = {"N": p["t_ext"], "S": p["t_int"], "E": p["t_int"], "W": p["t_int"]}
    shell = arch.Shell(v, 0, 0, W, D, t)
    shell.N.window(p.v("pier_w"), p["win_w"])
    shell.S.door(p.v("door_x"), p["door_w"], swing="N", hinge="start")

    # 3. Dimensions and labels last. Dimension text comes from Values only.
    annot.dim_chain(v, [p["pier_w"], p["win_w"], p["pier_e"]], start=0,
                    at=D + 24, axis="x", ext_from=D + p.v("t_ext"))
    symbols.room_tag(v, (W / 2, D / 2), "BEDROOM", lines=[kit.text("{room_w:ftin} x {room_d:ftin}")])

    # 4. Notes. Replace each <...> with the limit and citation from logs/code-decisions.md.
    sh.notes([
        kit.text("NEW WINDOW W-1 {win_w:in} WIDE."),
        kit.claim("EGRESS: NET CLEAR OPENING {win_nco:sf} PER THE ATTACHED DATA; "
                  "<LIMIT> SQ FT MIN. PER <CODE> <SECTION>.", cd="CD-014"),
    ])
    return sh
```

## Numbers and notes

- Layout numbers may be typed: cells, extents, label positions, offsets, text sizes.
- Design and measured dimensions come only from `project.json`, through `p["key"]`, `p.v("key")` or a `{key}` field. Never type one into a script or a note.
- `kit.text(template, cd=None)` fills `{key}` or `{key:code}`. Codes: `ftin`, `in`, `both`, `auto` (lengths, in fractions; never decimal inches), `sf` (a value whose `unit` is `sf`), `n` (a plain number), `u` (number with its unit word: `100 A`, `R-19`), `explain` (the arithmetic of a DERIVED value). Every unverified value prints its FV tag; a PLACEHOLDER, or a value resting on an unverified value with no FV tag, refuses the note. Write `{{` `}}` for literal braces. A value with no `unit` in `project.json` is a length; set `unit` (count, pct, A, cfm, psi, hr, days, sf ...) for anything else.
- `kit.claim(template, depends_on=[...], cd=None)` does the same and refuses the note if anything it rests on is unverified. Use it for every compliance statement. A note never says COMPLIES without the limit and the citation.
- A code limit in a note matches an entry in `logs/code-decisions.md` and passes its ID with `cd="CD-014"` (recorded in `build.json`, never printed). When the entry's quote has conditions, mark it in `code_notes` (`project-rules.md`, "Code notes").
- Read project fields as `kit.project.meta["title" | "address" | "owner" | "date"]`; never retype them on a sheet.

## True scale and layers

A view is placed at its stated scale or not at all. If the extents do not fit the cell, `sh.view()` raises `ScaleError` with the paper it needs and the largest scale that fits. `sh.view(title, "fit", extents, cell)` places it at the largest standard scale that fits; `layout.arrange` does that for several views (`kit-sheets.md`). The kit never shrinks a drawing. Everything a view draws must stay inside its cell.

Every geometry call takes `stroke`, `width`, `fill`, `dash`, `status` (`"ASSUMED"` draws grey dashed) and `layer`. Layer `"geom"` (default) is building linework, and text on it fails QA; `"annot"` is dimension lines, leaders, setback and grid lines; `"back"` is light textures. Colours are in `permitkit.display`; line widths come from named pens (`pens.kw("cut")`), never typed: QA fails a drawing whose lines are all one weight. Fills are grey or hatched, never coloured (QA `grayscale`).

## The loop

1. Edit `project.json` or a sheet script. Never edit an output PDF.
2. `build`, then `qa`. Fix every failure (`kit-qa.md`).
3. `preview` and look at each sheet once: a leader pointing at the wrong thing, a symbol on the wrong wall, a sheet that is hard to read. QA cannot see these.
4. Show the owner a draft early; door swings and openings are cheap to fix on paper.

A set you submit or hand to CrossBeam is a full build without `--no-determinism`.
