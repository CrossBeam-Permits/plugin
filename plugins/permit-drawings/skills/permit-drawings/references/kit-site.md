# Card: site plan

The site or plot plan and its zoning table. Signatures: `python3 -m permitkit api site annot tables`. Pattern: `examples/garage-adu/sheets/a1_site.py`.

## What plan reviewers send back

- Property lines without lengths, or with lengths and no source. Take them from the survey, the deed or the assessor map, and record that source in `project.json`; an assumed line prints grey with its FV tag.
- Setbacks not dimensioned from the property line to the nearest part of each structure (wall, or eave and projection when the city measures to those). Every required setback the stage 5 rules name gets a dimension and a label.
- Existing structures missing or not marked: every building, accessory structure, deck and pool on the lot, (E) or (N), with the separation between buildings when a rule controls it.
- No street name, no north arrow, no scale, or a lot drawn without its street frontage.
- Easements, driveways, parking spaces, utility meters, the sewer cleanout or septic, and drainage left off when the scope or the stage 2 answers name them.
- A zoning table with numbers and no source, or numbers that disagree with the drawing (lot area, coverage, floor area, height).

## Calls (`site`)

Positions are real inches, x east and y north, like a plan.

- `property_line(v, corners, lengths=[Value per edge], bearings=[...])`: the long-short-short lot line; each length prints outside the lot with its FV tag.
- `setback_line(v, pts, label="REAR SETBACK")`: the required line, thin dashed; dimension the distance with `annot.dim_chain` or `site.distance`.
- `footprint(v, pts, action, label, lines)`: existing is grey, new is hatched with a heavy outline, demo is dashed.
- `paving(v, pts, label, kind="concrete" | "deck")`, `centerline`, `street_label`, `utility(v, at, label, side)`.
- `distance(v, a, b, value)`: an aligned dimension between any two points, for a setback that is not axis-aligned.
- `annot.north_arrow(v, at)` points up the sheet (plan north; label it "PN" when the sheet also shows true north). `value=p.true_north` turns it to true north from `axes.true_north_deg`; an ASSUMED angle prints its FV tag and a PLACEHOLDER angle is refused.

## Scale

Site plans read at 1" = 10'-0" (0.6 pt per real inch), 1/8" = 1'-0" or 1/16" = 1'-0". Engineering scales (1" = 20', 30', 40', 50', 60', 100') take `engineering=True` in `sh.largest_scale`. Let `"fit"` choose, then check the lot and the street both show.

## Zoning table

`tables.zoning_table(kit, panel, rows)` prints ITEM / REQUIRED / EXISTING / PROPOSED / NOTES. A `required` that names a rule id prints that rule's limit and citation and records its `cd`. Name a rule id only when its code decision is `quoted` or `primary-read` (`05-code-questions.md` section 6); otherwise write who sets it ("PER PLANNING"), never a number from memory. Areas are Values with unit `sf`.
