# CEBC Substantial Structural Alteration — TRIP WIRE 3

> **Sources:**
> - 2025 CEBC § 202 (definition)
> - 2025 CEBC § 906.2 (consequence)
> - Cross-reference: CBC §1609 (wind) and CEBC §304.3.2 (seismic evaluation)
>
> Fetched 2026-05-09. Authority: 2025 CEBC, Title 24 Part 10. Effective Jan 1, 2026.

This is **State Trip Wire 3.** It is **independent** of the CEBC §604 Level 3 work-area trigger — a project can fire SSA without being a Level 3 alteration, and vice versa.

---

## Definition (CEBC §202, verbatim)

> *"[BS] SUBSTANTIAL STRUCTURAL ALTERATION. An alteration in which the gravity load-carrying structural elements altered within a 5-year period support more than 30 percent of the total floor and roof area of the building or structure. The areas to be counted toward the 30 percent shall include mezzanines, penthouses, and in-filled courts and shafts tributary to the altered structural elements."*

**Source:** chapter-2-definitions.md line 194.

---

## Consequence (CEBC §906.2, verbatim)

> *"Where work involves a substantial structural alteration, the lateral load-resisting system of the altered building shall be shown to satisfy the requirements of Section 1609 of the California Building Code and Section 304.3.2 of this code. Where the building is assigned to Seismic Design Category D or F, supports and attachments for nonstructural components required to serve any portion of the building with a use included in Risk Category IV shall comply with Section 1613 of the California Building Code or shall comply with ASCE 41 using an objective of Position Retention nonstructural performance with the BSE-1E earthquake hazard level."*

**Source:** chapter-9-alterations-level-3.md line 137.

**Plain-English consequence:** the entire lateral force-resisting system of the building must be evaluated and upgraded to meet **current new-construction wind (CBC §1609) and seismic (CEBC §304.3.2) standards**. This is the most expensive structural trigger in the existing building code and is often the difference between a $200K and a $700K project.

---

## §906.2 Exceptions (verbatim)

> *"Exceptions:*
> *1. Buildings of Group R occupancy with not more than five dwelling or sleeping units used solely for residential purposes that are altered based on the conventional light-frame construction methods of the California Building Code or in compliance with the provisions of the California Residential Code.*
> *2. Where the intended alteration involves only the lowest story of a building, structural components of the lateral load resisting system above that story need not comply with this section."*

**Operational reading of Exception 1:**
- An SFR or duplex (Group R, ≤5 units) that follows **conventional light-frame construction** per CBC or CRC is exempt from the §906.2 lateral upgrade.
- "Conventional light-frame construction" is a specific methodology in CBC §2308 / CRC §R602. Engineered designs (e.g., post-and-beam, structural steel moment frame, mass timber) do **not** qualify.
- **Trap:** if the structural drawings show engineered lateral elements (e.g., steel moment frames, hold-downs designed by a licensed engineer per CBC §1604), the project is **not** "conventional light-frame" and Exception 1 does not apply. Most coastal/oceanfront SFRs are engineered, not conventional, and Exception 1 routinely fails.

---

## How to apply the test

### Step 1 — Identify gravity-load-carrying structural elements being altered

Gravity-load-carrying elements include:
- Bearing walls (interior and exterior)
- Posts, columns, piers
- Beams, girders, headers (when modified)
- Floor joists, rafters, trusses (when modified, removed, or replaced)
- Continuous footings supporting any of the above

**"Altered"** means removed, replaced, modified in cross-section, or having materially changed connections. Pure cosmetic work (drywall, finishes) on a wall does not "alter" the gravity element behind it.

### Step 2 — Compute tributary floor + roof area for each altered element

For each altered element, compute the floor area and roof area whose gravity load it supports. Sum across all altered elements.

**§202 inclusion rule:** add mezzanines, penthouses, and in-filled courts and shafts tributary to altered elements.

### Step 3 — Compare to total floor + roof area of the building

Total floor and roof area = sum of all floor levels (gross floor area, all stories) + total roof projected area.

### Step 4 — Apply the 5-year rolling lookback

**Critical:** the 5-year window is **rolling**, not fixed. Look back at all building permits at the same APN within the prior 5 years. Sum the tributary areas of structural elements altered under all of those permits **plus** the current proposed alteration. If the cumulative total exceeds 30% of total floor + roof area, SSA fires.

This makes phased remodels detectable. A pattern of 4 small permits over 4 years that each touch ~10% of structure stacks into a 40% SSA trigger on the 5th permit (or even on the 4th, depending on cumulative math).

**Lookback comparison to other state trip wires:**
- SSA: **rolling 5-year** lookback.
- Coastal §13252(b): no time window specified in regulation; CCC enforcement looks at "overall scope of work" which can include phased permits at a single APN.
- CEBC §604 Level 3: no time window — single-permit work-area test.
- (Laguna Title 15 §1103.5.4 sprinkler: scope-based, no time window.)

The skill must track the SSA lookback **independently** of any other lookback window.

---

## Output checklist for the SSA test

For every residential remodel where any structural element is altered, produce:

| # | Check | What to Verify | Reference |
|---|-------|----------------|-----------|
| SSA-1 | Identify altered gravity elements | List every bearing wall, post, beam, header, joist, rafter, footing being modified per S-sheets | S-sheet review |
| SSA-2 | Compute tributary area for each | For each element, sum the floor + roof area whose gravity load it carries | Engineering calc; flag if not on submittal |
| SSA-3 | Pull 5-year permit history | At same APN, list all building permits issued in prior 60 months that touched structure | City permit records |
| SSA-4 | Sum cumulative tributary area | Add SSA-2 (current) + tributary areas from all SSA-3 permits | Spreadsheet |
| SSA-5 | Compare to total floor + roof | Total = gross floor area (all stories) + roof projected area, including mezzanines/penthouses/in-filled courts/shafts | Building dimensions |
| SSA-6 | If cumulative >30%, apply §906.2 | Lateral system must be upgraded per CBC §1609 (wind) + CEBC §304.3.2 (seismic) | Engineering deliverable |
| SSA-7 | Apply Exception 1 only if applicable | Group R, ≤5 units, AND **conventional light-frame** (not engineered) — verify on S-sheets | Engineering review |

---

## Common phantom-remodel signals tied to SSA

- New continuous footings shown under "existing-to-remain" walls on the S-sheets → those walls are gravity elements being altered (replaced or jacked) — count toward SSA.
- New shear panels and hold-downs at every "existing" stud bay → engineering retrofit; not "conventional light-frame"; Exception 1 does not apply.
- Plate-height changes shown at "existing" walls on the framing plan → wall is being rebuilt; SSA count applies.
- Roof-pitch changes at "existing" walls → roof framing being altered; SSA count applies.

See `phantom-remodel-detection.md` for the full signal catalog.

---

## Cross-references
- Definition: 2025 CEBC § 202.
- Consequence: 2025 CEBC § 906.2.
- Cumulative compliance context: `cebc-alteration-levels.md`.
- Phantom detection signals: `phantom-remodel-detection.md`.
