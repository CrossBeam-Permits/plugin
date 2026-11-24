# project.json: the one source of truth

Every number on every sheet comes from one file, `project.json`. The sheet scripts read it. They never type a shared number. When a value changes, edit this file and rebuild the whole set.

This card is what every project needs. Load a topic card only when its topic comes up:

- `project-geometry.md`: `walls`, `openings` and other geometry items, `action`, names and inline keys, `expr`, `chains`, true north, recording a measurement.
- `project-rules.md`: `rules` (code limits QA checks) and `code_notes`.
- `project-blocks.md`: `revisions`, and the optional `energy`, `green`, `structure`, `model3d`, `images` and `finishes` blocks.

The schema is `schemas/project.schema.json`. Check a file with:

```
PYTHONPATH=<skill>/scripts python3 -m permitkit validate project.json
```

The command prints JSON. `errors` stop the build. `warnings` do not, but read them. Each warning has a `code`. For example, `assumed-without-tag` is an ASSUMED value with no FV tag, which the kit will not print. `placeholder-without-tag` is a PLACEHOLDER, which never prints; it is expected until a value replaces it. `opening-wall-unknown` is an opening whose `wall` names no item in `walls`.

## Axes and units

The file states the axes once. Every value uses them.

- x = east, y = north, z = up. Lengths are real inches.
- Plans draw north up. Set `axes.true_north_deg` when true north differs from plan north (`project-geometry.md`, "True north").
- `axes.origin` names the physical point at x = 0, y = 0, z = 0. Pick a point you can find on site, such as an interior wall corner at finished floor.

A sketch or photo can face any direction. Record which direction is up in each source image (see Sources). A rotated sketch once put a stair 90 degrees wrong for weeks.

## A short complete example

```json
{
  "schema": "permitkit/1",
  "units": "in",
  "axes": {"x": "east", "y": "north", "z": "up",
           "origin": "SW interior corner of the bedroom, at finished floor"},
  "project": {
    "title": "BEDROOM WINDOW REPLACEMENT",
    "address": "100 EXAMPLE ST, ANYTOWN",
    "owner": "A. OWNER",
    "preparer": {"name": "A. OWNER", "role": "OWNER",
                 "statement": "<the preparer statement the jurisdiction requires>"},
    "date": "2026-10-01",
    "status_label": "REVIEW — NOT FOR CONSTRUCTION"
  },
  "drawing": {"sheet_size": "ARCH_D", "dim_style": "in", "set_name": "window-set"},
  "sources": [
    {"id": "S1", "kind": "sketch", "path": "sources/sketch-1.jpg", "by": "owner", "date": "2026-09-28",
     "orientation_note": "Window wall at the top of the page. The window faces north, so top = north."},
    {"id": "S2", "kind": "tape", "by": "owner", "date": "2026-09-29"},
    {"id": "S3", "kind": "mfr_doc", "path": "sources/window-data-sheet.pdf"}
  ],
  "values": {
    "room_w": {"v": 132, "status": "MEASURED", "source": "S2",
               "between": ["W wall finished face", "E wall finished face"], "along": "level",
               "ref_level": "about 36 in. above floor"},
    "pier_w":   {"v": 40, "status": "MEASURED", "source": "S1",
                 "between": ["W wall finished face", "window W jamb"]},
    "win_w":    {"v": 48, "status": "PROPOSED"},
    "pier_e":   {"expr": "room_w - pier_w - win_w", "status": "DERIVED"},
    "wall_t":   {"v": 5.5, "status": "ASSUMED", "fv": "FV-1", "note": "nominal; not taped"},
    "win_nco":  {"v": 5.9, "unit": "sf", "status": "MANUFACTURER", "source": "S3"}
  },
  "field_verify": [
    {"tag": "FV-1", "rank": 1, "what": "EXTERIOR WALL THICKNESS AT THE WINDOW",
     "why": "Sets the jamb depth and the outer wall line.", "values": ["wall_t"]}
  ],
  "chains": [
    {"id": "N-wall", "total": "$room_w",
     "segments": [{"len": "$pier_w", "what": "wall"}, {"len": "$win_w", "what": "opening"},
                  {"len": "$pier_e", "what": "wall"}]}
  ],
  "openings": [
    {"id": "W-1", "mark": "W-1", "type": "window", "action": "new", "wall": "N",
     "offset": "$pier_w", "width": "$win_w", "height": {"v": 48, "status": "PROPOSED"}}
  ],
  "sheets": [
    {"id": "A-1", "title": "EXISTING AND PROPOSED PLAN", "script": "sheets/a1_plan.py"}
  ],
  "revisions": []
}
```

The unit tests check that this example is valid. The status label is a gate label from `10-release.md`.

## Values

Every dimensional number is a Value. A bare number is an error.

When a value is unknown, do not leave it out and do not guess silently. Record it as ASSUMED with an FV tag (it prints with the tag) when a source gives a number, or as PLACEHOLDER (it holds a place and never prints) when no source does. A PLACEHOLDER still has a `v`: a working number that places the element on the drawing (draw it at a typical size; the kit draws it grey dash-dot and refuses to print the number). `03-measure.md` sections 3 and 8 say which sources count and when a PLACEHOLDER may place geometry. A form field outside `project.json`, such as a box on a city form, that has no value stays empty.

| Field | Meaning |
|---|---|
| `v` | The number. A point is `[x, y]`, two numbers. |
| `expr` | Arithmetic over other value keys (`project-geometry.md`, "Expressions"). Use `v` or `expr`, never both. |
| `status` | One of the six statuses below. Required. |
| `range` | ASSUMED only: `[low, high]`, the estimates the true number lies between, with `v` (the number drawn) inside. See "Ranges" below. |
| `unit` | `in` (default), `sf`, `count`, `deg`, `pct`, `ratio`, `hr` and `days` (time, such as a fire rating). For a value that is not a size: `cfm` (airflow), `gpm` (flow rate), `gpf` (flush volume), `A` (current), `psf` (load), `psi` (pressure), `lb` (weight), `mph` (wind speed), `degF` (temperature), `u-factor`, `R-value` (thermal resistance), `in/ft` (slope), `index` (flame spread or smoke-developed index). A value in one of these prints as a plain number. |
| `fv` | Field-verify tag: `FV-`, up to three capital letters that group it, a number and an optional letter, such as `FV-3`, `FV-2A` or `FV-H11` (H for the hall). Required for ASSUMED values before they print. A PLACEHOLDER never prints, with or without a tag. |
| `source` | A source id. |
| `between` | The two physical points the tape ran between. |
| `along` | `floor`, `slope`, `level`, `plumb`, `horizontal`, `vertical` or `diagonal`. |
| `ref_level` | The height at which a horizontal tape was held. |
| `by`, `date`, `note` | Who, when, and anything else worth keeping. |

Geometry items (`walls`, `openings`, `rooms`, `stairs`, `guards`, `fixtures`, `levels`) hold Values inline or refer to a key with `"$key"` (`project-geometry.md`). A key in `values` uses letters, digits and underscores only, such as `win_w`.

### Ranges

When an estimate has a low and a high end (a tile 9/16" to 5/8" thick, a floor that rises 3/4" to 13/16" under the old finish), give the ASSUMED value a `range` instead of writing one value per estimate:

```json
"tile_t": {"v": 0.5625, "range": [0.5625, 0.625], "status": "ASSUMED", "fv": "FV-H11",
           "note": "tile not chosen; 9/16 to 5/8 in."}
```

Geometry draws `v`. The value prints as its range, `9/16" TO 5/8" FV-H11`, and so does every DERIVED value computed from it (a riser that subtracts the tile prints its own low and high). Values that rest on the same estimate move together: two risers that both subtract the same tile keep the same difference at every estimate. The rules check tests every estimate (`project-rules.md`, "Ranges in the rules check"). `{key:explain}` refuses a ranged value, because its arithmetic has no one answer. `validate` refuses a `range` on any status but ASSUMED, on an `expr` or a point, one that does not run low to high, one that does not hold `v`, and a value whose formula breaks at an end (a square root of a negative, a division by zero) or that rests on more than 10 ranges.

Plain numbers print at the precision of their source and never round up, except a value that a rule caps, which rounds up (`project-rules.md`, "Printed lengths near a limit"); the same rule decides which way a length rounds. A typed `v` keeps its own decimals: `50` prints `50`, and `7.6` prints `7.6`. A computed value is cut to two decimals. An area (`unit: sf`) shows at least two decimals.

## Status

| Status | Use it when | How the kit draws and prints it |
|---|---|---|
| MEASURED | The owner taped it or wrote it on a sketch. | Solid line. Plain dimension. |
| DERIVED | It follows by arithmetic from other values. Give it an `expr`. | Plain dimension. Write a whole number as an integer (`50`, not `50.0`). A typed decimal prints with its decimals. `{key:explain}` prints the arithmetic. |
| ASSUMED | Nobody measured it. A phone scan is ASSUMED until a tape confirms it. | Grey dashed line. Every printed number carries its FV tag. |
| PROPOSED | It is a design decision for new work. | Solid line. Plain dimension. |
| MANUFACTURER | It comes from a product data sheet. | Solid line. Plain dimension. Cite the data sheet in `source`. |
| PLACEHOLDER | No source gives a number. It holds a place and is not a design value. | The kit refuses to print it. Geometry placed with it draws grey with a dash-dot line; print its FV tag beside it. |

Status flows through arithmetic. A DERIVED value that uses an ASSUMED value is unverified too. It prints with the FV tag of every ASSUMED input.

Two rules follow, and the kit enforces both:

1. The kit refuses to print an unverified value that has no FV tag.
2. A note that claims compliance must not rest on an unverified value. Write such notes with `kit.claim(...)`. The kit refuses the note if any value it names, or any value in `depends_on`, is unverified. Rewrite the note to state the requirement and the FV tag, or measure first.

When a tape replaces an assumption: `project-geometry.md`, "Recording a measurement".

## Sources

`kind` is one of `sketch`, `photo`, `scan`, `tape`, `answer`, `document`, `mfr_doc`, `survey`, `plan`, `other`. A `sketch`, `photo` or `scan` needs an `orientation_note`.

## Field-verify list

`field_verify` lists what someone must measure on site before construction. Each entry has a `tag`, `what` to measure, `why` it matters, a `rank` (1 first), and the `values` it covers. Add `signed_off: {by, date, result}` when it is done. `Panel.fv_schedule()` prints the list with a sign-off column. Keep a "not for construction" status label until every entry is signed off.

## Sheets and drawing settings

- `sheets` is the bound order. Each entry has an `id`, a `title`, an optional `subtitle`, and a `script` path of the form `sheets/<name>.py`. Use `attach` instead of `script` for an external PDF bound in that position. An `attach` path is relative to the project folder and has no `..`. The kit refuses a script or attach path that leads outside the project folder. `permitkit new-sheet` prints the entry to add here.
- `revisions`: `project-blocks.md`.
- `drawing` sets `sheet_size` (`ARCH_E`, `ARCH_D`, `ARCH_C`, `ANSI_B`, `LETTER`), `orientation`, `precision_denominator` (default 16), `dim_style` (`ftin`, `in`, `both`, `auto`) and `set_name`.

## Project fields

`project.title`, `address`, `owner`, `preparer.name`, `date` and `status_label` print in every title block. None of them may be empty; `validate` refuses an empty or blank field. `project.owner` is the property owner: the person or entity on the property record. The property owner can differ from the owner who uses this skill (`terms.md`). Take the name from a document (a tax bill, a deed) or from the stage 1 answer (`01-scope.md` section 2). Until it is known, write `OWNER NAME PENDING` and keep the question open in `logs/questions.md`. Replace it before the city submittal (`10-release.md`, PERMIT REVIEW). `preparer.statement` is optional. When it is present it prints in every title block. Leave it out when the jurisdiction needs no statement, or when a professional prepares part of the set and their stamp carries it; the title block then omits that line. The preparer statement and any code list come from the jurisdiction or from CrossBeam. The kit never writes them.

`status_label` is the gate label from `10-release.md`, for example `REVIEW — NOT FOR CONSTRUCTION`.
