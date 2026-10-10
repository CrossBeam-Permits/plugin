# California Baseline — Retaining Wall

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Retaining Wall — State Regulatory Decision Engine

This skill contains California state-level retaining wall requirements extracted from the 2025 California Building Code (CBC), California Residential Code (CRC), and referenced standards. It covers residential and light commercial retaining walls — the most common permit type.

**What this covers**: State building code — the requirements that apply everywhere in California. Every city must enforce at least these standards.

**What this does NOT cover**: City-specific ordinances, setback requirements, grading permit thresholds, or local fee schedules. Use the city-level retaining wall skill for those. Does NOT cover garden walls (freestanding, no retained soil), basement foundation walls (see foundation skill), or shoring/temporary excavation support.

### How to Use This Skill

When reviewing a retaining wall permit or answering a retaining wall code question, follow the decision tree below. Each step tells you which reference files to load. Load only what you need — most reviews require 2-3 reference files, not all of them.

After loading references, check the **Quick-Reference Tables** below for the key numbers that come up in almost every retaining wall review.

---

### Decision Tree Router

#### STEP 1: Does This Project Need a Permit?

| Condition | Permit Required? | Code Section | Reference File |
|-----------|-----------------|--------------|----------------|
| Retaining wall <=4 ft (footing to top), level backfill, no surcharge | NO (exempt) | CRC R105.2 | `permit-engineering-triggers.md` |
| Retaining wall >4 ft (footing to top) | YES | CRC R105.2 | `permit-engineering-triggers.md` |
| Retaining wall any height with surcharge loads | YES | CRC R105.2 | `permit-engineering-triggers.md` |
| Retaining wall any height impounding flammable liquids | YES | CRC R105.2 | `permit-engineering-triggers.md` |
| Retaining wall in front setback (local requirement) | Often YES | City municipal code | `permit-engineering-triggers.md` |

**Height measurement**: Measured from the **bottom of the footing** to the **top of the wall**. This is NOT the exposed face height — it includes the below-grade footing depth.

#### STEP 2: What Type of Review Is This?

| Review Type | Load These References |
|-------------|----------------------|
| **Full permit review** (plans in, pass/fail out) | `permit-engineering-triggers.md`, `structural-design-cbc1807.md`, `drainage-waterproofing.md` |
| **Permit threshold question only** (do I need a permit?) | `permit-engineering-triggers.md` |
| **Engineering requirement question** (do I need an engineer?) | `permit-engineering-triggers.md` |
| **Structural design question** (lateral loads, footing, reinforcement) | `structural-design-cbc1807.md` |
| **Drainage or waterproofing question** | `drainage-waterproofing.md` |
| **Material or construction method question** | `materials-construction.md` |
| **Guard/railing question** (fence on retaining wall) | `permit-engineering-triggers.md` |
| **Tiered wall question** | `permit-engineering-triggers.md`, `structural-design-cbc1807.md` |
| **Soils report question** | `permit-engineering-triggers.md`, `structural-design-cbc1807.md` |

#### STEP 3: Walk the Review Checklist

For a full permit review, check each item in order. The checklist tells you which reference file has the answer and what code section applies.

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 1 | **Permit required?** | Height >4 ft (footing to top), or any height with surcharge, or impounding flammable liquids. Measure from bottom of footing to top of wall, not exposed face only. | CRC R105.2 | `permit-engineering-triggers.md` |
| 2 | **Engineering required?** | Walls >4 ft, surcharge loads, adverse soils, slopes above or below, tiered walls within influence zone, walls supporting structures/driveways, walls near ROW or property lines. Must be designed by CA licensed civil/structural engineer or architect. | CBC 1807.2 | `permit-engineering-triggers.md` |
| 3 | **Soils report provided?** | Required when: adverse soil conditions (expansive, liquefiable, fill), slopes, or per AHJ. Report must include allowable bearing pressure, lateral soil parameters, groundwater level, and recommendations. | CBC 1803.2, 1803.5.3 | `permit-engineering-triggers.md` |
| 4 | **Lateral soil loads calculated?** | Design for lateral earth pressure using equivalent fluid method or Rankine/Coulomb. Must account for at-rest vs active conditions, soil type, groundwater, and surcharge. Seismic lateral earth pressure for walls >6 ft in SDC D/E/F. | CBC 1807.2.2, 1610; ASCE 7-22 | `structural-design-cbc1807.md` |
| 5 | **Surcharge loads accounted for?** | Identify all surcharges: vehicles/driveways, buildings, slopes, stored materials, adjacent walls. Surcharge adds equivalent height to lateral pressure calculation. Typical: 2 ft equivalent for residential driveways, 4 ft for heavy vehicles. | CBC 1807.2.2 | `structural-design-cbc1807.md` |
| 6 | **Stability analysis adequate?** | Check safety factors: overturning >=1.5 (1.1 with seismic), sliding >=1.5 (1.1 with seismic). Bearing pressure within allowable. Uses 0.7x nominal earthquake loads + 1.0x other nominal loads. Standard load combinations of CBC 1605 do NOT apply to retaining wall stability. | CBC 1807.2.3 | `structural-design-cbc1807.md` |
| 7 | **Footing design adequate?** | Footing width, depth, reinforcement, and key (if provided). Footing below frost line (minimal in most CA) and minimum 12" below lower grade. Bearing area sufficient for soil capacity. | CBC 1807.2, 1809 | `structural-design-cbc1807.md` |
| 8 | **Wall stem design adequate?** | Stem thickness, vertical and horizontal reinforcement, concrete or masonry strength, dowel connections to footing. CMU walls: cells grouted, bond beams provided. | CBC 1807.2; ACI 318 / TMS 402 | `structural-design-cbc1807.md`, `materials-construction.md` |
| 9 | **Drainage system shown?** | Drainage behind wall is critical. Verify: drain rock (12" min width), perforated drain pipe at base (4" min, sloped to daylight), filter fabric between drain rock and native soil. Weep holes as supplemental (4" dia, 6-8 ft OC). Surface drainage graded away from wall top. | Engineering practice; CBC 1805 | `drainage-waterproofing.md` |
| 10 | **Waterproofing addressed?** | Below-grade portions: dampproofing or waterproofing per CBC 1805 where wall retains habitable space or where required by design. Waterproofing membrane on soil side of wall below grade. | CBC 1805 | `drainage-waterproofing.md` |
| 11 | **Guards/railings required?** | Guards required where retaining wall is within 36" of a walking surface AND the drop exceeds 30" from the walking surface to grade below. Guard height: 42" min above walking surface. Openings: 4" sphere test. Loads: 200 lb concentrated at top. | CBC 1807.2.5; CRC R321.1.1-R321.1.3 (2025 CRC; formerly R312.1); loads Table R301.5 | `permit-engineering-triggers.md` |
| 12 | **Material specifications shown?** | Structural concrete strength/durability follows CBC 1904.1/ACI 318 and the exposure/design; the 3,000-psi minimum is limited to CBC 1904.1's stated Group R-2/R-3 weather-exposed vertical surfaces. Verify CMU/mortar/grout/rebar/SRW specifications under the applicable design. Timber uses an R304.1 naturally durable or treated path; R304.1.2 ground-contact treatment applies only in its stated scope. | CBC 1904.1, 2103; CRC R304.1, R304.1.2; applicable ASTM/ACI/TMS design | `materials-construction.md` |
| 13 | **Tiered walls analyzed correctly?** | If multiple walls, check spacing. Influence zone = 2x height of lower wall measured from base of lower wall. Walls within influence zone must be analyzed as a single composite wall. Walls outside influence zone may be designed independently. | CBC 1807.2 | `permit-engineering-triggers.md` |
| 14 | **Grading plan consistent?** | If retaining wall is part of a grading project, verify consistency with grading plan. Grading permits per CBC Appendix J when cut/fill exceeds thresholds (typically 50 cu yd or 5 ft depth of cut). | CBC Appendix J | `permit-engineering-triggers.md` |
| 15 | **Contractor licensing adequate?** | B (General Building) or C-8 (Concrete) for concrete walls. C-29 (Masonry) for CMU walls. C-12 (Earthwork/Paving) for grading. A (General Engineering) for walls with engineered grading. | B&P Code 7028 | N/A |

#### STEP 4: Output the Review Result

For each checklist item, output one of:
- **PASS** — requirement met, cite code section
- **FAIL** — requirement not met, cite code section and explain what's wrong
- **FLAG** — cannot determine from submitted data, explain what additional info is needed
- **N/A** — does not apply to this project

---

### Quick-Reference Tables

#### Permit and Engineering Thresholds

| Condition | Permit? | Engineering? | Code Section |
|-----------|---------|-------------|--------------|
| <=4 ft, level backfill, no surcharge | No | No | CRC R105.2 |
| >4 ft, level backfill, no surcharge | Yes | Yes | CRC R105.2; CBC 1807.2 |
| Any height with surcharge (driveway, building, slope) | Yes | Yes | CRC R105.2; CBC 1807.2 |
| Any height on adverse soils (expansive, fill, liquefiable) | Yes | Yes | CBC 1803.2 |
| Tiered walls within influence zone (2x H) | Yes | Yes | CBC 1807.2 |
| Wall supporting structure or utility | Yes | Yes | CBC 1807.2 |

#### Typical Equivalent Fluid Pressures (Lateral Soil Loads)

| Soil Type | At-Rest (psf/ft) | Active (psf/ft) | Use When |
|-----------|-------------------|-----------------|----------|
| Clean sand/gravel (well-drained) | 55 | 30 | Free-draining backfill, wall can deflect |
| Sand-silt mix | 65 | 45 | Mixed backfill |
| Clay/silt (poorly drained) | 85 | 60 | Cohesive soils, poor drainage |

*At-rest pressure used when wall cannot deflect (e.g., basement walls, walls restrained at top). Active pressure used when wall can rotate/deflect slightly at top (typical cantilever retaining walls).*

#### Safety Factors for Stability

| Condition | Sliding | Overturning |
|-----------|---------|-------------|
| Static (no seismic) | >= 1.5 | >= 1.5 |
| With seismic (0.7x earthquake loads) | >= 1.1 | >= 1.1 |

#### Prescriptive Footing Dimensions (<=4 ft walls, no surcharge)

| Wall Height | Min Footing Width | Min Footing Depth | Footing Rebar | Notes |
|-------------|-------------------|-------------------|---------------|-------|
| 2 ft | 18" | 10" | #4 @ 12" OC E.W. | Gravity wall OK |
| 3 ft | 24" | 12" | #4 @ 12" OC E.W. | Gravity or cantilever |
| 4 ft | 24"-30" | 12" | #4 @ 12" OC E.W. | Cantilever preferred |

*Prescriptive values for standard conditions only. Actual requirements depend on soil conditions, seismic zone, and local jurisdiction standards. When in doubt, require engineering.*

#### Prescriptive CMU Wall Reinforcement (<=4 ft, no surcharge)

| Component | Requirement |
|-----------|-------------|
| Wall thickness | 8" CMU minimum |
| Vertical rebar | #4 @ 24" OC |
| Horizontal rebar | #4 in bond beam at top and every 24" OC |
| Footing width | 24" minimum |
| Footing depth | 12" minimum |
| Footing rebar | 2-#4 continuous, top and bottom |
| Dowels | #4 @ 24" OC matching vertical rebar |

#### Prescriptive Poured Concrete Wall (<=4 ft, no surcharge)

| Component | Requirement |
|-----------|-------------|
| Stem thickness | 6" minimum |
| Stem vertical rebar | #4 @ 12" OC (soil side) |
| Stem horizontal rebar | #4 @ 18" OC |
| Footing width | 24"-30" |
| Footing depth | 10"-12" |
| Footing rebar | #4 @ 12" OC E.W., top and bottom |
| Key (optional) | 4" wide x 4" deep in bottom of footing |

#### Guard Requirements at Retaining Walls

| Condition | Guard Required? | Min Height | Code Section |
|-----------|----------------|------------|--------------|
| Drop <=30" | No | N/A | CBC 1807.2.5 |
| Drop >30", walking surface within 36" | Yes | 42" above walking surface | CBC 1807.2.5; CRC R321.1 |
| Not accessible to public | No (exception) | N/A | CBC 1807.2.5.1 |

---

### Key Principles

1. **The 4-ft rule is the critical threshold.** Retaining walls <=4 ft from bottom of footing to top of wall, with level backfill and no surcharge, are exempt from permits under state code. Everything above that line requires a permit and typically engineering.

2. **Height is measured from bottom of footing, not exposed face.** A wall that appears 3 ft tall above grade but has a 2 ft deep footing is actually a 5 ft wall — and requires a permit and engineering.

3. **Surcharge changes everything.** A 2 ft retaining wall with a driveway on top requires a permit and engineering because the vehicle surcharge creates lateral loads the wall must resist.

4. **Drainage is the most common cause of failure.** Lack of drainage behind a retaining wall allows hydrostatic pressure to build up, which can double or triple the lateral load. Every retaining wall review should verify drainage is shown on the plans.

5. **Tiered walls are analyzed together.** Two 3 ft walls stacked with a small terrace between them may need to be designed as a single 6 ft wall if they fall within each other's influence zone (2x wall height).

6. **Safety factors are specific to retaining walls.** Standard load combinations per CBC 1605 do NOT apply. Retaining wall stability uses safety factors of 1.5 (static) and 1.1 (seismic) against sliding and overturning.

7. **Guards are life-safety.** Any retaining wall with >30" drop adjacent to a walking surface needs a 42" guard with 4" sphere opening limits. A fence on top of the wall can serve as the guard if it meets these requirements.

8. **Most of California is SDC D or higher.** Seismic design governs for retaining walls >6 ft of backfill. Geotechnical investigation must provide seismic lateral earth pressure parameters.
