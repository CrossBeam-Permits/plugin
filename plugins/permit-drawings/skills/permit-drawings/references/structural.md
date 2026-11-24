# Structural framing checks and the preliminary calc

This needs the kit's optional `structural` module. Run `python3 -m permitkit modules`; if it is not installed, fetch it as `00-connect.md` section 3 says (`crossbeam_get_skill` with `"module": "structural"`).

`scripts/permitkit/struct.py` helps the drafter with light-frame wood structure. It does two things:

1. **Prescriptive checks.** It looks up each joist, rafter, ceiling joist, header and footing in the 2025 CRC tables and checks the drawn span or size. The checks go into the kit QA as rules, with PASS, FAIL or WARN.
2. **A preliminary calc.** When the tables do not cover a member, it runs a simply supported beam check from design values that the drafter records with a citation. The result is a calc package for a California-licensed engineer to review and stamp. **It is not a structural design.**

The kit never decides that a member is adequate. A table check says what the cited table allows for the inputs in `project.json`. The engineer decides everything the tables do not cover.

## When to use it

- In stage 5 (code questions) and stage 6 (draw), when the set shows new framing: floor joists, rafters, ceiling joists, headers in bearing walls, beams, posts or footings.
- When a city comment asks for header sizes, joist spans or a framing plan.
- Before you print any member size. A size prints through `struct.size_label`, so a failing or engineer-only member can never print as designed.

## The `structure` block in `project.json`

Every number is a Value with a status (`references/project-file.md`). A field can be a `$key` reference to a value in `values`, or an inline value. Inline values register as `structure.<path>`, for example `structure.members.J-1.span`, with the member `id` in the path.

```json
"structure": {
  "criteria": {
    "ground_snow_load": {"v": 0, "unit": "psf", "status": "ASSUMED", "fv": "FV-20", "note": "city Table R301.2 not yet read"},
    "roof_live_load":   {"v": 20, "unit": "psf", "status": "PROPOSED"},
    "wind_speed":       {"v": 95, "unit": "mph", "status": "ASSUMED", "fv": "FV-20", "source": "C9"},
    "wind_exposure":    {"text": "C", "status": "ASSUMED", "fv": "FV-20", "source": "C9"},
    "seismic_design_category": {"text": "D", "status": "ASSUMED", "fv": "FV-20", "source": "C9"},
    "stories":          {"v": 1, "unit": "count", "status": "MEASURED", "source": "C9"}
  },
  "members": [
    {"id": "J-1", "type": "floor_joist", "size": "2x8", "species": "Douglas fir-larch", "grade": "#2",
     "spacing": "$joist_oc_in", "span": "$floor_joist_span_in",
     "live_load": {"v": 30, "unit": "psf", "status": "PROPOSED"}, "dead_load": {"v": 10, "unit": "psf", "status": "PROPOSED"}},
    {"id": "H-1", "type": "header", "size": "2-2x8", "species": "Douglas fir-larch", "grade": "#2",
     "wall": "exterior", "supporting": "Roof and ceiling", "span": "$w1_ro_w_in",
     "building_width": "$house_w_in", "top_braced": true,
     "jack_studs": {"v": 1, "unit": "count", "status": "PROPOSED"},
     "full_height_studs": {"v": 2, "unit": "count", "status": "PROPOSED"}}
  ],
  "triggers": [
    {"id": "irregular", "citation": "2025 CRC R301.2.2.6", "question": "is the building irregular per R301.2.2.6 items 1-8",
     "applies": {"v": 0, "unit": "count", "status": "PROPOSED", "note": "rectangular one-story addition"}}
  ],
  "bracing": [{"id": "A-B", "building": "detached", "spacing": "$bwl_spacing_in"}]
}
```

Fields by member `type`:

| type | table | fields |
|---|---|---|
| `floor_joist` | R502.3.1(1) (30 psf LL), R502.3.1(2) (40 psf LL) | size, species, grade, spacing, span, live_load, dead_load |
| `rafter` | R802.4.1(1)-(8), factor R802.4.1(9) | size, species, grade, spacing, span (horizontal projection), slope (in/ft), dead_load, ceiling_attached, tie_height_ratio |
| `ceiling_joist` | R802.5.1(1), R802.5.1(2) | size, species, grade, spacing, span, attic (`no_storage` or `limited_storage`), live_load, dead_load |
| `header` | R602.7(1) exterior, R602.7(2) interior; R602.7.5 | size (`2-2x10`), species, grade, wall, supporting (the table's row text, such as `Roof and ceiling`), span, building_width, top_braced, jack_studs, full_height_studs |
| `footing` | R403.1(1), R401.4.1(1) | story (the table's row text, such as `1 story—with crawl space`), width, thickness, building_width, soil_bearing |
| `beam`, `post` | none | `design: "prelim"` with a `calc` block, or `design: "engineer"` with an `engineer` block |

`design` is `table` (the default for the table types), `prelim` (sized by this kit's calc, prints `PRELIM — BY ENGINEER`) or `engineer` (by the engineer of record; with `engineer.stamped: true` and `calc_ref`, the size prints with the calc reference). Until it is stamped, an `engineer` member prints `BY ENGINEER (PENDING)` and adds an open ENGINEER REQUIRED row (`STRUCT-<id>-ENG`, R301.1.3) that QA fails until the stamped design is recorded; it is never shown as a preliminary calc.

A text criterion (`wind_exposure`, `seismic_design_category`) is `{"text", "status"}`. The kit carries its status and FV tag on a carrier value, so a check that uses it WARNs while it is unverified. `seismic_design_category` `D` with no sub-category applies every D0-D2 limit, the conservative reading.

## What the checks do

Each check is a rule with an id such as `STRUCT-J-1-SPAN`. `model.py` adds the rules to the project at load, so `permitkit rules`, `permitkit qa` and the framing check panel all report them. The QA rules check then:

- **PASS** when every input is verified and the drawn value meets the table.
- **FAIL** when every input is verified and the drawn value breaks the table, or a verified input puts the member outside the tables.
- **WARN** when any input of the check is ASSUMED or PLACEHOLDER: the drawn value, the span, the spacing, a load, the snow load, the building width, the seismic category. The message still says `would pass` or `WOULD FAIL`.

When a member is past the tables, or a code trigger applies, the check reads **`OUTSIDE PRESCRIPTIVE LIMITS — ENGINEER REQUIRED`** and names the provision. Examples: ground snow load over 70 psf (R301.2.3), roof slope under 3:12 so the ridge must be a designed beam (R802.4.4), a size or span past the last table cell, soil bearing below 1,500 psf, an irregular building in SDC D0-D2 (R301.2.2.6), more than two stories in SDC D2 (R301.2.2.7), a dead load over the SDC D limits (R301.2.2.2), wind design required (R301.2.1.1), a beam or post with no table.

### How the lookups read the tables

- **Only what a table allows is interpolated.** R602.7(1) and R602.7(2): building width (footnote c). R403.1(1): footing width between soil bearing pressures, with no extrapolation. Every other table: no interpolation.
- **Between columns that cannot be interpolated, the kit uses the next more severe one.** That means the wider spacing, the heavier dead load, the heavier snow column, and the larger header span row for R602.7.5. The 30 psf snow column applies when the ground snow load is under 30 psf and the roof live load is 20 psf or less (R602.7(1) note e).
- **Jack studs** (NJ) take the larger of the two bracketing columns. NJ is never interpolated.
- **A span cell with a footnote mark** (`16-10a` in R502.3.1(2)) checks against its span, and the footnote's text joins the lookup notes. A cell that is neither a span nor the table's span-exceeds note is an error (`struct-bad-cell`), never a guess.
- **The rafter governing load** is the larger of the roof live load and the ground snow load (R301.6). Ceiling-joist attachment and the tie-height factor come from R802.4.1(9).
- Every check records the table, the edition and the verbatim table row in its `lookup`. The calc package prints them.

## The preliminary calc

A `calc` block on a `beam` (or a `header` the tables do not cover):

```json
"calc": {
  "material": "sawn", "plies": 2,
  "b": {"v": 1.5, "status": "PROPOSED"}, "d": {"v": 11.25, "status": "PROPOSED"},
  "Fb": {"v": 900, "unit": "psi", "status": "ASSUMED", "fv": "FV-21", "citation": "AWC NDS Supplement (2024) Table 4A, DF-L No. 2"},
  "Fv": {...}, "E": {...},
  "factors": {"Fb": {"CM": {...}, "Ct": {...}, "CL": {...}, "CF": {...}, "Cr": {...}}, "Fv": {...}, "E": {...}},
  "loads": [
    {"id": "d", "kind": "uniform", "case": "D", "psf": {"v": 10, "unit": "psf", "status": "PROPOSED"}, "trib": "$trib_in"},
    {"id": "p", "kind": "point", "case": "L", "P": {"v": 800, "unit": "lb", "status": "PROPOSED", "note": "girder reaction"}, "a": "$p_at_in"}
  ],
  "combos": [{"name": "D + L", "factors": {"D": 1, "L": 1},
              "CD": {"v": 1.0, "unit": "factor", "status": "ASSUMED", "fv": "FV-21", "citation": "NDS 2.3.2"},
              "citation": "ASCE 7-22 2.4.1 via CBC 1605.1"}],
  "deflection": {"live": "Floors", "total": "Floor members", "dry_service": true}
}
```

- **The kit holds no design values.** Each of Fb, Fv, E, every adjustment factor (CD, CM, Ct, CL, CF, Cfu, Ci, Cr, CV and the rest) and each load combination is an input with a `citation`. The schema refuses a design value with no citation, and the calc refuses a blank one. A missing value stops the calc (`input-required`); there are no defaults. `factor_checklist` lists the usual factors for the material that you did not list, so the engineer can confirm each does not apply.
- **The loads** are uniform (`psf` x `trib` as Values, or `plf` as a design value with a citation) or point (`P` in lb at `a` from the left support, as Values), each with a case: D, L, Lr or S. The combos name their factors and their CD. CBC 1605 equation text is not in the corpus, so the combinations are inputs with a citation too.
- **The checks are**:
  - bending: fb = M / S against F'b = Fb x CD x the factors;
  - shear: fv = 1.5 V / A against F'v;
  - live-load deflection: L, Lr and S cases, against the CRC Table R301.7 row you name in `deflection.live` (Floors L/360, flexible-finish ceilings L/240, and so on);
  - total deflection: creep x dead + live, against the CBC Table 1604.3 row you name in `deflection.total`; the creep factor comes from note d (0.5 dry service, 1.0 otherwise).
  Moment and deflection are evaluated on 401 points plus every point-load position.
- **The status** is `computed` (all inputs verified), `unverified` (an ASSUMED input; the ratios print with a warning and its FV tags), `placeholder` or `input-required` (not calculated).

## Printing on the sheets

```python
from permitkit import struct

struct.framing_check_panel(kit, sh, (13.0, 9.4, 13.48, 6.0))   # MARK / MEMBER / SIZE / SPACING / SPAN / TABLE MAX. / BASIS / CHECK
struct.calc_panel(kit, sh, (0, 0, 16, 10), "B-1")              # inputs, formulas, ratios, under the PRELIMINARY banner
kit.text(...) + struct.size_label(kit.project, "H-1")           # a member size for a schedule or a leader
```

`size_label` prints:

- the size with the FV tags of its unverified inputs, when the table checks pass;
- `SEE STRUCTURAL CHECK` when a check fails;
- `BY ENGINEER` when the member is outside the tables;
- `PRELIM — BY ENGINEER` when only this kit's calc sized it;
- `BY ENGINEER (PENDING)` for `design: "engineer"` before the stamped design is in hand;
- the size and the engineer's calc reference when the engineer of record stamped it.

## Commands

```
PYTHONPATH=<skill>/scripts python3 -m permitkit struct project.json                     # checks + calc summary
PYTHONPATH=<skill>/scripts python3 -m permitkit struct project.json --calc-md struct-calcs.md   # the calc package
PYTHONPATH=<skill>/scripts python3 -m permitkit struct project.json --full              # every lookup trace
```

The markdown package is headed **PRELIMINARY — FOR REVIEW AND STAMP BY A CALIFORNIA-LICENSED ENGINEER. NOT A STRUCTURAL DESIGN.** It lists the design criteria, every check with its verbatim table row or provision, and for each calc every input with its status and citation, the section properties, M, V, fb, fv, the deflections and the ratios. Send it to the engineer with the set. Do not submit it to the city as a design.

## The table data

`scripts/permitkit/data/crc2025_structural.json` holds every table row and provision the checks use. Each row carries its citation, the edition (2025 CRC, effective 2026-01-01) and the verbatim source line from the CrossBeam code corpus (`data/state-code/part-02.5-residential`, and `part-02-building` for CBC Table 1604.3). Nothing in it was typed from memory. To rebuild it after a corpus update, run `python3 skills/shared/permit-drawings/scripts/tools/build_struct_tables.py` from the repo root. The tests check that every quoted line is still in the corpus.

What is not in it, and so not checked:

- **NDS reference design values** are not in the corpus. You record them per member, with a citation.
- **Table R602.10.3(3)** lost its Story Location column in the corpus scrape, so its required bracing lengths are not usable. Bracing length is an input with its own `required_citation`.
- **The CBC 1605 load combinations**: the equation text is empty in the corpus.
- Wall studs (R602.3(5)), girders (R602.7 girder rows beyond the header tables), connections, hold-downs, uplift (R802.11) and diaphragm nailing are not checked. Mark them `by engineer` on the sheets. Give each load-carrying connection a `connections` entry and a spot on the sheet (`kit-elevations-sections.md`, "Connections that carry a load"), so the maker's tested detail or the engineer's calculation has a place.
