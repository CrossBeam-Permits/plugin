# Title 24 energy and CALGreen sheets

This needs the kit's optional `energy` module. Run `python3 -m permitkit modules`; if it is not installed, fetch it as `00-connect.md` section 3 says (`crossbeam_get_skill` with `"module": "energy"`).

Read this when the scope touches the building envelope, space conditioning, water heating or lighting of a single-family house, or adds conditioned area. It says what the kit checks, what it cannot do, and how to record the energy and green facts in `project.json`.

The code is the 2025 California Energy Code (Title 24, Part 6, "CEnC") and the 2025 California Green Building Standards Code (Title 24, Part 11, "CALGreen"), effective 2026-01-01. The kit reads every limit, threshold and quote from two data files. Each entry was cut word for word from the CrossBeam code corpus (`data/state-code`) and names the file it came from:

- `scripts/permitkit/data/t24-2025-sfr.json`: CEnC 150.0, 150.1 (Table 150.1-A) and 150.2 limits, the 150.2 thresholds, the requirements a scope can trigger, the state form names and three 100.1 definitions.
- `scripts/permitkit/data/calgreen-2025-residential.json`: the CALGreen 301.1.1 trigger and 32 Chapter 4 measures that reach additions and alterations, each with a short quote and a suggested responsible party and verifier.
- `scripts/permitkit/data/cec-building-climate-zones-by-zip.csv`: the Energy Commission's building climate zone by ZIP code list.

`make_t24_2025_sfr.py` and `make_calgreen_2025_residential.py` in the same folder rebuild the two JSON files from the corpus. A test fails when a shipped file differs from what they build. When the corpus changes, run them; never hand-edit a quote or a limit.

## 1. What the kit does, and what it cannot do

The kit does:

- read the climate zone from the ZIP code, as a Value with its source;
- check the values you record (U-factor, SHGC, areas, R-values) against the prescriptive and mandatory limits of the zone, as rules in the kit's rules shape;
- list the requirements the scope triggers, with the quoted section, and flag each one that needs field verification by an ECC-Rater (earlier cycles called this a HERS Rater);
- say when the CF1R must be registered with an ECC-Provider data registry (Title 24 Part 1, 10-103(a)1B) and when a performance run decides compliance;
- print a T-24 summary panel, a CF1R worksheet panel (the values to type into the state form or CBECC-Res) and a CALGreen mandatory measures sheet.

The kit cannot:

- produce or sign a CF1R. The certificate comes from the state form or from CBECC-Res (Commission-certified software), and its documentation author and the responsible person sign it (10-103(a)). The worksheet says so in print;
- run CBECC-Res. On the performance path it checks the mandatory measures only;
- register a CF1R or do field verification;
- decide which CALGreen measures apply. You decide, with a reason for each;
- check multifamily or nonresidential work. `energy.building` accepts `single-family` only.

When a limit cannot be read for the zone, the kit asks you instead of printing a number. Example: the corpus cell of Table 150.1-A for SHGC in Climate Zone 15 reads `0.203`, which may be a footnote mark or a scrape error. The kit lists it under OPEN ITEMS and tells you to read the printed table. Record what you read as a code decision (`05-code-questions.md`), then enter the value; never guess.

## 2. Climate zone

```
python3 -m permitkit energy --zip 92651
```

prints a `climate_zone` Value, the `CEC-CZ` source entry and the start of the `energy` block. Copy them into `project.json`. The value is DERIVED with `source: "CEC-CZ"` (a value read from a table names the table in `source`; it needs no `expr`).

A ZIP code can cross a zone line. When the site is near one, confirm the zone with the city. When the address has no ZIP yet, record the zone as ASSUMED with an FV tag. Every check rests on the zone, so with an ASSUMED zone each one reads WOULD MEET; CONFIRM FV-n until the zone is confirmed. `validate` reports an error when `energy.zip` and a CEC-CZ zone disagree.

## 3. The path: prescriptive or performance

Record your choice in `energy.path` and the reason in `energy.path_reason`. These are the branches the kit follows (thresholds from the data file):

| Scope | Prescriptive branch | Notes |
|---|---|---|
| Addition, 400 sq ft or less of CFA | 150.2(a)1B; total fenestration the greater of 75 sq ft or 30 percent of the addition CFA (150.2(a)1Biv(b)) | West-facing limit, radiant barrier and ceiling insulation by zone; QII does not apply (150.2(a)1Bv) |
| Addition, over 400 and up to 700 sq ft | 150.2(a)1B; total fenestration the greater of 120 sq ft or 25 percent (150.2(a)1Biv(a)) | Same as above |
| Addition over 700 sq ft | 150.2(a)1A: the full 150.1(c) package with modifications | QII applies and is ECC verified. The kit checks fenestration, doors and insulation only and asks you to use the state form or CBECC-Res for the rest. Performance is usually simpler |
| Alteration | 150.2(b)1, item by item | Replacement fenestration up to 75 sq ft takes the 150.2(b)1B exception limits; added fenestration up to 16 sq ft skips the area limits (150.2(b)1A Exception 2) |
| Any | Performance, 150.2(a)2 or 150.2(b)2 | A CBECC-Res run by the documentation author decides compliance. The kit checks mandatory measures and says the run is needed |

CFA is measured at the exterior surfaces of the exterior walls (CEnC 100.1, CONDITIONED FLOOR AREA). Fenestration area is the rough opening area (100.1, FENESTRATION AREA). Store each as its own Value with `unit: "sf"`.

## 4. The `energy` block

```json
"energy": {
  "building": "single-family", "work": ["addition"], "zip": "92651",
  "climate_zone": "$climate_zone", "path": "prescriptive",
  "path_reason": "Bedroom addition under 400 sq ft; 150.2(a)1B covers it.",
  "addition": {"cfa": "$add_gross_area_sf", "existing_cfa": "$house_area_e_sf",
               "fenestration_area": "$fen_area_sf", "west_fenestration_area": "$d2_area_sf"},
  "fenestration": [{"id": "W-1", "kind": "window", "change": "addition", "area": "$w1_area_sf",
                    "u_factor": "$fen_u", "shgc": "$fen_shgc", "orientation": "S", "product": "..."}],
  "insulation": [{"id": "CEILING", "assembly": "vented_attic_ceiling", "change": "addition", "r_value": "$ceil_r_n"}],
  "hvac": [{"id": "MS-1", "change": "new", "system": "heat_pump", "ducted": false}],
  "lighting": {"change": "new"}
}
```

`references/project-blocks.md` lists every field. The rules:

- Every number is a Value reference. U-factor uses `unit: "u-factor"`, SHGC `ratio`, R-values `R-value`, areas `sf`.
- A product value from an NFRC label or a data sheet is MANUFACTURER with its source. Until the product is chosen, record PLACEHOLDER: the sheet prints SELECT PRODUCT and the limit, never a number.
- Leave a field out when you do not know it. The kit then asks for it and prints the limit it must meet.
- `change` says what the work does to each item (`addition`, `added`, `replacement` for fenestration; `new`, `extended`, `complete_replacement`, `equipment_replaced`, `refrigerant_altered` for HVAC). It selects the code branch. It is your reading of the scope, recorded in `logs/scope.md`; the kit never infers it from words.
- An exception you claim goes in `exception` or `ecc_exception` with its reason, and is a code decision (`05-code-questions.md` section 7).

Run:

```
python3 -m permitkit energy project.json                 # checks, asks, ECC list, forms
python3 -m permitkit energy project.json --write-rules   # put the checks into `rules` as T24-* entries
```

`--write-rules` replaces only the `T24-*` rules, so the QA `rules` check also covers them. Run it again after each change to the energy block; `energy` reports `rules_in_project.in_sync`.

## 5. Field verification and registration

The kit marks a requirement ECC when the quoted section calls for field verification and diagnostic testing: for example refrigerant charge verification for a new heat pump (150.1(c)7A with Table 150.1-A), duct sealing for altered ducts (150.2(b)1D and E), and QII for an addition over 700 sq ft. When any ECC item applies, the CF1R must be registered with an ECC-Provider data registry (10-103(a)1B), and an ECC-Rater tests on site and files the Certificate of Field Verification and Diagnostic Testing (CF3R; Title 24 Part 1, 10-103). Tell the owner early: it is a separate hire and an inspection-day dependency.

When no ECC item applies, a window or water-heater replacement may not need a CF1R at the city's discretion (10-103(a)1C). The sheet says so; ask the city.

## 6. Mandatory measures (150.0)

They apply on both paths. The kit checks those it models: 150.0(q) fenestration U-factor, 150.0(a) ceiling insulation, 150.0(c) wall insulation, 150.0(d) raised-floor insulation. For new or altered lighting, it prints the quoted 150.0(k) measures as plan notes (efficacy, recessed downlights, blank boxes, on/off and vacancy controls, dimming, independent controls, outdoor lighting).

## 7. CALGreen

CALGreen 301.1.1 applies Chapter 4 to an addition or alteration that increases the building's conditioned area, volume or size, and then only within the area of the work. Record your answer and its reason:

```json
"green": {
  "trigger": {"increases_area_volume_or_size": true, "reason": "Adds a new conditioned bedroom (A-3)."},
  "measures": [{"section": "4.406.1", "applies": true, "reason": "New exterior walls with sole-plate penetrations."},
               {"section": "4.506.1", "applies": false, "reason": "No bathroom in the scope."}],
  "local": [{"section": "...", "text": "...", "source": "...", "reason": "..."}]
}
```

- With the trigger `true`, decide every catalog measure, `applies` true or false, each with a reason. The sheet refuses to print while any is undecided. `python3 -m permitkit green project.json` lists them.
- With the trigger `false`, an undecided measure prints as not required by 301.1.1. A note can still apply: for example the 4.303.1 Note points to Civil Code 1101.1 et seq. for older houses, whatever 301.1.1 says.
- `responsibility` and `verification` override the catalog's suggestions, which are the preparer's assignment, not code text.
- A city amendment goes in `local` with its source. List only amendments you have sourced (`crossbeam_get_review_requirements` or the city code).

## 8. Sheets

In a sheet script:

```python
from permitkit import energy, greensheets

def build(kit):
    return energy.sheet(kit, "T-1", green=True)    # small scope: T-24 and CALGreen on one sheet
```

- `energy.sheet(kit, sid, green=False)`: summary and checks, then triggered requirements (left); CF1R worksheet, then the CALGreen measures when `green` (right); 150.0(k) lighting notes in the notes column.
- `greensheets.sheet(kit, sid)`: a whole CALGreen sheet in two columns.
- Panels to compose your own: `energy.summary_panel`, `energy.requirements_panel`, `energy.cf1r_panel`, `energy.mandatory_notes`, `greensheets.measures_panel`, `greensheets.green_notes`; `energy.stack(sheet, x, w, builders)` stacks panels down one column.

Every printed number comes through `kit.text` or `kit.claim`: MEETS prints only for verified values, and an unverified value or limit prints its FV tag. Attach the signed CF1R itself (`08-package.md`) in the position the city asks for.
