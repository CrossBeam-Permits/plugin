# California Baseline — Restaurant Tenant Improvement

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Restaurant TI — State Regulatory Decision Engine

This skill contains California state-level restaurant tenant improvement rules synthesized from the California Retail Food Code (CRFC), AB 671 fast-track legislation, AB 592 outdoor dining permanence, and Title 24 building codes. It covers everything a plan reviewer checks when a restaurant remodels, opens in a new space, or changes ownership.

**What this covers**: State law — the floor that all California jurisdictions must enforce. Cities/counties may add requirements but cannot waive these.

**What this does NOT cover**: City/county-specific ordinances, local fee schedules, local submission portals, or project-specific engineering. Use the city-level restaurant-ti skill for those.

### How to Use This Skill

When reviewing a restaurant TI submission, follow the 3-step decision tree below. Each step tells you which reference files to load. Load only what you need — most reviews require 4-6 reference files, not all 12.

---

### Decision Tree Router

#### STEP 1: Classify the Submission Type

What kind of restaurant TI is this?

| Submission Type | Always Load | Description |
|-----------------|-------------|-------------|
| **New food facility** (new restaurant in existing shell) | `ab671-pathways.md`, `health-construction.md` | Full review — all disciplines |
| **Major remodel** (new kitchen, layout change, hood work) | `ab671-pathways.md`, `health-construction.md` | Full review — all disciplines |
| **Minor remodel** (finishes, equipment swap, no layout change) | `ab671-pathways.md`, `health-construction.md` | Reduced scope — skip mechanical/fire if no hood changes |
| **Change of ownership** (no construction) | `ab671-pathways.md`, `health-food-safety.md` | Operational review only — skip building/mechanical/fire |
| **Outdoor dining addition** | `ab671-pathways.md`, `outdoor-dining.md` | Plus egress/fire if occupancy load changes |

#### STEP 2: Load Discipline-Specific References

Based on the submission type, load the references for each applicable review discipline.

##### Health Department Review (CRFC) — applies to ALL submission types

| Condition | Load These References |
|-----------|----------------------|
| **Always** (any food facility TI) | `health-construction.md` — floors, walls, ceilings, lighting, vermin exclusion |
| New facility or major remodel with equipment changes | `health-equipment.md` — equipment installation, sinks, spacing |
| New facility or major remodel with plumbing work | `health-plumbing-sanitation.md` — handwashing, water supply, waste, floor drains |
| Change of ownership or operational questions | `health-food-safety.md` — food handling, storage, temps (layout relevance only) |

##### Building Department Review (CBC) — applies to new facility, major remodel, occupancy change

| Condition | Load These References |
|-----------|----------------------|
| Occupancy load >=50 OR room >=750 sq ft | `building-occupancy-egress.md` — A-2 classification, egress, exits, ADA |
| ANY change of occupancy (e.g., retail to restaurant) | `building-occupancy-egress.md` + `existing-building.md` |
| TI in existing building (always true for restaurant TI) | `existing-building.md` — alteration levels, change of occupancy triggers |

##### Mechanical Review (CMC) — applies when commercial cooking equipment is present

| Condition | Load These References |
|-----------|----------------------|
| Commercial cooking (fryers, grills, ranges, ovens, broilers) | `mechanical-ventilation.md` — Type I/II hoods, exhaust rates, makeup air, duct specs |
| Dishwasher only (no cooking) | `mechanical-ventilation.md` — Type II hood requirements only |
| No cooking equipment, no dishwasher | Skip mechanical review |

##### Plumbing Review (CPC) — applies to new facility, major remodel

| Condition | Load These References |
|-----------|----------------------|
| Commercial cooking producing grease | `plumbing-grease.md` — grease interceptors/traps, sizing, fixture counts |
| Any food facility (fixture count check) | `plumbing-grease.md` — minimum fixture counts by occupant load |

##### Fire Review (CFC/CMC) — applies when cooking or assembly thresholds are triggered

| Condition | Load These References |
|-----------|----------------------|
| Commercial cooking under Type I hood | `fire-suppression-assembly.md` — UL 300 hood suppression, equipment shutoff |
| Assembly occupant load >49 | `fire-suppression-assembly.md` — sprinkler triggers, fire alarm, exits |
| Assembly occupant load >=300 | `fire-suppression-assembly.md` — manual fire alarm, main exit requirements |

##### Energy Review (Part 6) — applies to new facility, major remodel

| Condition | Load These References |
|-----------|----------------------|
| Lighting changes affecting >=10% of luminaires | `energy-efficiency.md` — lighting power density limits |
| New/replacement HVAC | `energy-efficiency.md` — HVAC efficiency requirements |
| Minor remodel (no lighting/HVAC changes) | Skip energy review |

##### AB 671 Pathway Determination — applies to ALL restaurant TI submissions

| Condition | Load These References |
|-----------|----------------------|
| **Always** | `ab671-pathways.md` — QPC vs standard pathway, timelines, deemed-approval |

##### Outdoor Dining — applies only when outdoor dining is part of scope

| Condition | Load These References |
|-----------|----------------------|
| Adding or modifying outdoor dining | `outdoor-dining.md` — AB 592, IPM plan, satellite food service |
| Open-front design (folding doors, NanaWall) | `outdoor-dining.md` — HSC 114266(d) requirements |

#### STEP 3: Output the Review Result

For each checklist item in the loaded reference files, output one of:
- **PASS** — requirement met, cite code section
- **FAIL** — requirement not met, cite code section and explain what's wrong
- **FLAG** — cannot determine from submitted data, explain what info is needed
- **N/A** — does not apply to this project

---

### Quick-Reference Thresholds

These numbers come up in almost every restaurant TI review. Check here first before loading a reference file.

#### Assembly Occupancy Triggers

| Threshold | Value | Code Section |
|-----------|-------|-------------|
| A-2 occupancy classification | Restaurants, bars, cafeterias with associated commercial kitchens | CBC 303.3 |
| A-2 reclassified as B | Occupant load <50 persons | CBC 303.1.1 |
| Accessory assembly as B | Room <750 sq ft, accessory to another occupancy | CBC 303.1.2 |
| Occupant load — tables & chairs | 15 net sq ft per occupant | CBC Table 1004.5 |
| Occupant load — standing space | 5 net sq ft per occupant | CBC Table 1004.5 |
| Occupant load — commercial kitchen | 200 gross sq ft per occupant | CBC Table 1004.5 |
| Occupant load — fixed booths | 1 person per 24 inches of seat | CBC Table 1004.5 |
| Post occupant load sign | When 50+ occupants in assembly room | CBC 1004.9 |

#### Sprinkler and Fire Alarm Triggers

| Trigger | Threshold | Code Section |
|---------|-----------|-------------|
| Sprinkler required (A-2) | Fire area >5,000 sq ft OR occupant load >=100 OR not on exit discharge level | CBC 903.2.1.2 |
| Manual fire alarm (A) | Occupant load >=300, or >100 above/below exit discharge | CBC 907.2.1 |
| Emergency voice/alarm | Occupant load >=1,000 | CBC 907.2.1 |
| Number of exits (A) | 1 exit: <=49 occupants; 3 exits: 501-1,000; 4 exits: >1,000 | CBC Table 1006.2.1 |

#### Health Department Key Dimensions

| Dimension | Value | Code Section |
|-----------|-------|-------------|
| Floor coving radius | 3/8" minimum | HSC 114268(b) |
| Floor coving wall height | 4" minimum | HSC 114268(b) |
| Floor drain slope | 1:50 to drains | HSC 114269(a) |
| Floor-mounted equipment clearance | 6" minimum (or sealed to floor) | HSC 114169(b) |
| Table-mounted equipment clearance | 4" minimum (or sealed to table) | HSC 114169(d) |
| Equipment-to-wall gap | <=1/32" (or sealed) | HSC 114169(a)(2-3) |
| Storage above floor | 6" minimum | HSC 114047(b), 114178(a) |
| Hot water at faucet | 120 deg F minimum | HSC 114192(a) |
| Handwash water temp | 100-108 deg F | HSC 113953(c) |
| Lighting — food work surfaces | 50 foot-candles | HSC 114252(c) |
| Lighting — handwash/warewash/toilet | 20 foot-candles | HSC 114252(b) |
| Lighting — walk-in/dry storage | 10 foot-candles at 30" AFF | HSC 114252(a) |
| 3-compartment sink | Required + 2 integral metal drainboards | HSC 114099(a) |
| Food prep sink minimum | 18"W x 18"L x 12"D + 18"x18" drainboard | HSC 114163(a)(1) |
| Consumer separation from food prep | 3 ft minimum, 3 ft high barrier | HSC 113984.1 |

#### Equipment Classification — Type I vs. Type II Hood

Per NFPA 96 Section 5.2 and CMC Section 507.1.1, any cooking equipment that produces grease-laden vapors during normal use (griddles, fryers, broilers, ranges, woks, panini presses with grease-producing foods, etc.) requires a Type I hood. Equipment that produces only steam, heat, or moisture (steamers, ovens, dishwashers, coffee makers) requires a Type II hood. When equipment classification is uncertain, default to Type I.

#### Mechanical Ventilation Key Values

| Parameter | Value | Code Section |
|-----------|-------|-------------|
| Type I hood overhang | 6" minimum beyond cooking surface (open sides) | CMC 508.4.1 |
| Hood-to-cooking distance max | 4 feet vertical | CMC 508.3 |
| Exhaust rate — heavy duty wall canopy | 400 CFM/linear ft | CMC Table 508.5.1 |
| Exhaust rate — medium duty wall canopy | 200 CFM/linear ft | CMC Table 508.5.1 |
| Duct velocity range | 500-2,500 FPM | CMC 511 |
| Makeup air negative pressure max | 0.02" water column | CMC 511.3 |
| Duct slope (<=75 ft) | 1/4" per foot minimum | CMC 510.5.3 |
| Hood fire suppression | UL 300 wet chemical, auto + manual actuation | CMC 513 |

#### Plan Review Timelines (AB 671)

| Phase | Timeline | Consequence | Code Section |
|-------|----------|-------------|-------------|
| Initial review | 20 business days | Deemed approved if no decision | Gov. Code 66345.2(b)(2-3), HSC 114380(f)(1) |
| Resubmission review | 10 business days | Limited to identified deficiencies | Gov. Code 66345.2(b)(4), HSC 114380(f)(2) |
| QPC audit rate | 20% of weekly submissions minimum | Random audit | Gov. Code 66345.2(c)(1) |
| Audit initiation | Within 5 business days of permit issuance | — | Gov. Code 66345.2(c)(2) |

---

### Key Definitions

| Term | Definition | Source |
|------|-----------|--------|
| **Restaurant** (AB 671) | Retail food establishment that prepares, serves, and vends food directly to consumers. Excludes fast food per Labor Code 1474 (60+ national chain locations, limited-service). | Gov. Code 66345.1(b) |
| **Tenant Improvement** | A change to the interior of an existing building | Gov. Code 66345.1(c) |
| **QPC** | Qualified Professional Certifier — licensed architect or PE with 5+ years commercial experience and $2M insurance | Gov. Code 66345.1(a) |
| **PHF** | Potentially Hazardous Food — food requiring temperature control for safety | HSC 113871 |
| **Extensive remodel** | Remodel triggering full code compliance (floor drains, floor sinks, etc.) | HSC 114269 |

---

### Key Principles

1. **Dual-track review**: Restaurant TIs require BOTH building department (CBC/CEC/CMC/CPC) AND health department (CRFC) plan review. The 20-business-day clock runs independently on each track.

2. **AB 671 applies to non-fast-food only**: Fast food restaurants (60+ national chain locations, limited-service per Labor Code 1474) are excluded from the QPC pathway and fast-track timelines.

3. **CRFC governs construction requirements**: The California Retail Food Code (HSC Division 104 Part 7) sets detailed construction standards for food facilities — floors, walls, ceilings, sinks, equipment spacing, lighting, ventilation. These requirements are enforced by the local health department, not the building department.

4. **Assembly occupancy triggers cascading requirements**: When occupant load hits 50 (A-2 classification), 100 (sprinklers), 300 (fire alarm), or 1,000 (voice/alarm), additional building and fire code requirements are triggered.

5. **Change of occupancy is the biggest trigger**: Converting a non-restaurant space (B, M, F) to A-2 restaurant triggers Chapter 10 of the Existing Building Code, potentially requiring full code compliance for egress, sprinklers, fire alarm, and accessibility.

6. **Hood suppression is always UL 300**: All kitchen hood fire suppression systems must be UL 300 wet chemical. CO2 extinguishers are prohibited. Auto + manual actuation required. Equipment must auto-shutoff on suppression activation.

7. **Progressive disclosure is mandatory**: The agent reads this SKILL.md first, then the submission, then loads ONLY the 3-6 reference files relevant to that specific case. Never load all 12 references.
