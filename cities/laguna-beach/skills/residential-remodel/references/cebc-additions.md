# CEBC Chapter 11 — Additions

> **Source:** 2025 CEBC §§ 202, 301.3.2, 606.1, 1101.2, and 1103.1 (Title 24 Part 10, effective January 1, 2026).
> **Authority:** 2025 California Existing Building Code (CEBC), Title 24 Part 10
> **Effective:** January 1, 2026

Additions are not a "trip wire" but are nearly always relevant when residential remodel scope adds floor area. The §1103.1 5% gravity-load rule and §1101.2 nonconformity rule are the load-bearing thresholds.

---

## What is an "addition" under CEBC

An addition is any work that increases the building's gross floor area, height, or footprint. CEBC §606.1 references the Chapter 2 definition; in practice any new conditioned or unconditioned space (including roofed-over outdoor space tied into the building envelope) counts.

When scope includes added square footage → dispatch to `../../residential-addition/references/california-baseline.md` for the full addition-side review, **and** apply the rules below for impacts on the existing building.

---

## §1101.1 Scope (verbatim)

> *"An addition to a building or structure shall comply with the California Building Standards Codes as adopted for new construction without requiring the existing building or structure to comply with any requirements of those codes or of these provisions, except as required by this chapter. Where an addition or alteration impacts the existing building or structure, the result of the addition or alteration shall not put the existing building or structure out of compliance with the California Building or Residential Code as applicable. The provisions of height and area of the California Building or Residential Code shall apply to the entire existing building with the additions."*

**Plain reading:** the **addition itself** must meet new-construction code. The **existing building** is left alone unless the addition impacts it (§1101.2, §1103.1, §1103.2 below). Height and area limits apply to the **whole building including the addition**.

---

## §1101.2 Creation or extension of nonconformity (verbatim)

> *"An addition shall not create or extend any nonconformity in the existing building to which the addition is being made with regard to accessibility, structural strength, supports and attachments for nonstructural components, fire safety, means of egress or the capacity of mechanical, plumbing or electrical systems."*

**Operational reading:** if the existing building is already nonconforming (e.g., undersized water service, under-strength shear walls, no fire separation between dwelling units), the addition cannot make that nonconformity worse — and may force upgrades of those systems if the addition's load pushes them over capacity.

**Exception:** *"Nonconforming supports and attachments for nonstructural components that serve the addition from within the existing building need not be altered to comply with California Building Code Section 1613 unless the components are part of the addition's life safety system or are required to serve an addition assigned to Risk Category IV."*

---

## §1103.1 Additional gravity loads — the 5% trigger (verbatim)

> *"Any existing gravity load-carrying structural element for which an addition and its related alterations cause an increase in design dead, live or snow load, including snow drift effects, of more than 5 percent shall be replaced or altered as needed to carry the gravity loads required by the California Building Code for new structures. Any existing gravity load-carrying structural element whose gravity load-carrying capacity is decreased as part of the addition and its related alterations shall be considered to be an altered element subject to the requirements of Section 805.2. Any existing element that will form part of the lateral load path for any part of the addition shall be considered to be an existing lateral load-carrying structural element subject to the requirements of Section 1103.2."*

**Operational reading — element-by-element test:**
- For each existing gravity element (footing, wall, post, beam, joist, rafter), compute the change in design dead + live + snow load (with snow drift) caused by the addition.
- If that increase exceeds **5%** for **any single element**, that element must be **replaced or altered** to meet new-construction CBC capacity.
- Decreased-capacity elements are treated as "altered" per §805.2.
- Any element in the lateral load path of the addition becomes a §1103.2 lateral element (see below).

**Exception:** *"Buildings of Group R occupancy with not more than five dwelling units or sleeping units used solely for residential purposes where the existing building and the addition together comply with the conventional light-frame construction methods of the California Building Code or the provisions of the California Residential Code."*

Same conventional-light-frame exception as §906.2 — engineered designs do not qualify.

---

## §1103.2 Lateral force-resisting system (verbatim)

> *"Where the addition is structurally independent of the existing structure, existing lateral load-carrying structural elements shall be permitted to remain unaltered. Where the addition is not structurally independent of the existing structure, the lateral force-resisting system of the existing structure and its addition acting together as a single structure shall comply with Section 1609 of the California Building Code and Section 304.3.1 of this code."*

**Two-bucket test:**
- **Structurally independent** addition (its own footings, no shared shear walls/diaphragms) → existing lateral elements untouched.
- **Not independent** → entire combined structure must meet current CBC §1609 (wind) and CEBC §304.3.1 (seismic). This often becomes the dominant cost driver.

**§1103.2 Exception 1:** R-occupancy ≤5 units, conventional light-frame for both existing and addition.

**§1103.2 Exception 2:** *"Any existing lateral load-carrying structural element whose demand-capacity ratio with the addition considered is not more than 10 percent greater than its demand-capacity ratio with the addition ignored shall be permitted to remain unaltered."* (10% D/C ratio increase carve-out, with cumulative-effects accounting since original construction.)

---

## §1103.3 Flood hazard areas (summary)

For additions in flood hazard areas, the substantial-improvement test (50% of market value) applies. If the addition + cumulative work is substantial improvement, the entire existing building must comply with CBC §1612 / CRC §R306 flood-resistant construction. See full text in source file for the sub-rules on horizontal vs vertical, structurally interconnected vs independent.

---

## Output checklist for additions

| # | Check | What to Verify | Code Section | Notes |
|---|-------|----------------|--------------|-------|
| ADD-1 | Addition meets new-construction code | All new construction code requirements (CBC, CRC, CPC, CMC, CEC, Energy, CALGreen) apply to the new SF | §1101.1 | Dispatch to `../../residential-addition/references/california-baseline.md` |
| ADD-2 | Existing building nonconformity not worsened | List existing nonconformities; verify addition does not extend them | §1101.2 | Often forces system-capacity upgrades |
| ADD-3 | 5% gravity-load element check | For each existing gravity element, compute load increase; flag any with >5% | §1103.1 | Engineering calc required; conventional light-frame exception applies for SFR ≤5 units |
| ADD-4 | Structural-independence determination | Independent → existing lateral untouched. Not independent → combined system to current code or 10% D/C exception | §1103.2 | S-sheet review |
| ADD-5 | Flood hazard substantial-improvement | If in SFHA, compute cumulative work cost ÷ market value; if ≥50%, full §1612/§R306 compliance | §1103.3 | Flood map review |
| ADD-6 | Height + area combined check | Existing + addition total within CBC/CRC limits | §1101.1, §1102.1, §1102.2 | Zoning + fire-area review |
| ADD-7 | Risk category re-evaluation | Mixed occupancy → re-determine per CBC §1604.5.1; possible change-of-occupancy trigger | §1101.3 | Rare for SFR |
| ADD-8 | Energy code | Addition complies with Title 24 Pt 6 §150.2(a) | §1104.1 | See `energy-code-additions-alterations.md` |

---

## Interaction with the trip wires

Additions can be the trigger that fires a parent-level trip wire on the **existing** building:

- **Coastal §13252(b):** if cumulative work (addition + concurrent alteration) replaces ≥50% of the SFR, the project loses repair/maintenance status and a CDP is required for the entire scope. See `coastal-replacement-structure.md`.
- **§604 Level 3:** "work area" can include the addition footprint where reconfiguration occurs at the join. If addition + reconfigured existing area >50% of building area (denominator counts existing building only, not the addition), Level 3 fires.
- **§202 SSA:** any structural elements altered to receive the addition (e.g., new opening cut into existing bearing wall to connect spaces) count toward the rolling 5-year SSA tally.

Always run the trip-wire tests **after** computing the addition envelope — additions cause trip-wire firings more often than standalone interior remodels.

---

## Cross-references
- Source: 2025 CEBC Ch. 11, especially §§ 1101.2 and 1103.1 (Title 24 Part 10).
- Energy code for additions: `energy-code-additions-alterations.md` (Title 24 Pt 6 §150.2(a)).
- Coastal replacement-structure trigger: `coastal-replacement-structure.md`.
- Sub-skill dispatch: `../../residential-addition/references/california-baseline.md`.
