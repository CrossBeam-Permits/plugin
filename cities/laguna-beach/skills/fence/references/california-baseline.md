# California Baseline — Fence/Wall

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Fence & Wall Permit Review

This skill covers **state-level** California requirements for residential and light commercial fences, walls, and barriers. It routes between the California Residential Code (CRC) for dwellings and the California Building Code (CBC) for commercial/light commercial buildings.

**What this covers:**
- Fence and freestanding wall construction (wood, vinyl, chain link, masonry/block, wrought iron)
- Height limits and permit exemption thresholds
- Post spacing, post depth, and footing requirements
- Masonry/block wall construction (CMU, foundation, reinforcement, mortar)
- Retaining walls and when engineering is required
- Wind load considerations for fences and walls
- Pool barrier and enclosure requirements (Swimming Pool Safety Act)
- Self-closing/self-latching gate hardware
- Guards at retaining walls
- Glazing in hazardous locations near pools

**What this does NOT cover:**
- City-specific height limits, setbacks, or design standards (see city overlay skills)
- City-specific permit triggers or zoning requirements
- Engineered retaining walls over 4 ft (requires registered design professional)
- Sound walls along freeways (Caltrans jurisdiction)
- Security fencing for industrial/utility facilities
- Accessibility requirements for commercial fencing (see CBC Chapter 11B)

---

### How to Use This Skill

1. Determine whether the project is **residential** (CRC) or **commercial** (CBC)
2. Walk through the Decision Tree Router below
3. For each checklist item, load the referenced file from `/` as needed
4. See `../SKILL.md` for the full reference file catalog

---

### Decision Tree Router

#### STEP 1 — Determine Code Path

| Building Use | Code | Key Sections |
|---|---|---|
| Single-family dwelling, duplex, townhouse <=3 stories | CRC | R105.2, R606, R321, Appendix CI |
| Commercial, light commercial, multifamily >3 stories | CBC | 105, 1807, 2101, 3109, 3119B |

Both codes share the same material standards (ASTM) and California amendments. The CRC includes the Swimming Pool Safety Act in Appendix CI; the CBC includes it in Section 3109.

#### STEP 2 — What Type of Structure?

| Structure Type | Route |
|---|---|
| **Wood fence** (board, picket, shadowbox, lattice) | Height/material check, post structural check |
| **Vinyl/PVC fence** | Same as wood but verify UV stability and wind rating |
| **Chain link fence** | Height check, mesh size check (pool barrier: <=1-3/4" openings) |
| **Wrought iron / ornamental metal fence** | Height check, picket spacing (<=4" for pool barrier) |
| **Masonry/CMU block wall** | Full masonry checklist — foundation, reinforcement, mortar |
| **Retaining wall** | Engineering trigger check (>4 ft from bottom of footing to top) |
| **Pool barrier / enclosure** | Pool barrier checklist — height, gaps, gate hardware, drowning prevention |
| **Combination** (e.g., block wall base + iron fence top) | Check total height and both material requirements |

#### STEP 3 — Does It Need a Permit?

| Condition | Permit Required? | Code Section |
|---|---|---|
| Fences not over 7 feet high | NO (exempt per state code) | CRC R105.2 |
| Fences over 7 feet high | YES | CRC R105.2 |
| Retaining walls <=4 ft (footing to top), no surcharge | NO (exempt per state code) | CRC R105.2 |
| Retaining walls >4 ft OR supporting surcharge | YES | CRC R105.2 |
| Pool barrier / enclosure (new pool or remodel) | YES (part of pool permit) | CRC Appendix CI / CBC 3109 |
| Any fence/wall in a city with lower thresholds | Check city overlay — many cities require permits below 7 ft | City municipal code |

**Important:** The state exemption at 7 ft is a ceiling, not a floor. Most California cities set their permit-exempt threshold at 6 ft or lower. Always check the city overlay skill for the applicable jurisdiction.

#### STEP 4 — Review Checklist

Walk each item in order. For every check, record PASS / FAIL / FLAG / N/A with the code section cited.

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 1 | **Permit Exemption** | Fences <=7 ft are exempt from permit per state code. Retaining walls <=4 ft without surcharge are exempt. Cities may have lower thresholds — check city overlay. | CRC R105.2 | `fence-height-materials.md` |
| 2 | **Height Measurement** | Fence/wall height measured from finished grade on the higher side. For fences on retaining walls, total combined height measured from lower grade. Where fence on top of wall, both structures must independently comply. | CRC R105.2; local practice | `fence-height-materials.md` |
| 3 | **Material Suitability** | Wood: naturally durable species or pressure-treated (AWPA U1, Use Category 4B for ground contact). Vinyl: UV-stabilized, manufacturer wind rating. Chain link: galvanized or vinyl-coated, minimum 9 gauge. Masonry: ASTM C90 CMU; mortar selected under Table R606.2.8 / ASTM C270 by use and SDC, including Type N where permitted. Metal: galvanized, powder-coated, or corrosion-resistant. | CRC R304, R606.2; CBC 2103 | `fence-height-materials.md` |
| 4 | **Post Spacing & Size** | Wood fence posts: typically 4x4 minimum, 6 ft to 8 ft OC maximum. Metal posts: per manufacturer specs. Post size increases with fence height and wind exposure. | Industry standard / manufacturer | `post-structural.md` |
| 5 | **Post Embedment Depth** | Minimum 1/3 of total post length below grade (rule of thumb). For 6 ft fence: minimum 24" deep. For 8 ft fence: minimum 32" deep. Concrete footings recommended: minimum 8" diameter for 4x4 post, 10" for 4x6 or 6x6. Post must extend below frost line (minimal concern in most of CA). | CBC 1807.3 | `post-structural.md` |
| 6 | **Concrete Footing** | Concrete backfill: minimum f'c 2,000 psi. Hole minimum 4" larger than post diameter. Footing should extend 1-2" above grade and slope away from post for drainage. Clean sand backfill with tamping is alternative. | CBC 1807.3.3 | `post-structural.md` |
| 7 | **Wind Load** | Fences and freestanding walls must resist wind loads per ASCE 7-22 / CBC 1609. Solid fences (board-on-board, masonry) receive full wind pressure. Open fences (chain link, wrought iron, picket) receive reduced pressure proportional to solidity ratio. Most of California: 110-115 mph basic wind speed. | CBC 1609; ASCE 7-22 | `post-structural.md` |
| 8 | **Masonry/Block Wall — Materials and Bond** | CMU: ASTM C90. Mortar: Table R606.2.8 or ASTM C270, with type selected by use and SDC under R606.2.8.1–R606.2.8.3. Use running or stack bond under R606.3.7; stack bond requires the R606.3.7.2 horizontal reinforcement. | CRC R606.2, R606.3.7 | `masonry-block-walls.md` |
| 9 | **Masonry/Block Wall — Reinforcement** | Establish the wall function, assigned SDC, thickness, bond, unit/grout construction, and loads. Where applicable, use R606.12 with Figures R606.11(1)-(3), or an approved TMS 402/403 design. Fill cells containing reinforcement solidly with grout. | CRC R606.3.5.3, R606.12; Figures R606.11(1)-(3); TMS 402/403 | `masonry-block-walls.md` |
| 10 | **Masonry/Block Wall — Foundation** | Size the footing and dowels for the wall loads, soil, assigned SDC, and applicable CRC/CBC design path. Do not use a wall-height-only footing or dowel schedule without an applicable code figure/table or fully sourced approved design. | CRC R403; CBC 1807.1.6 | `masonry-block-walls.md` |
| 11 | **Masonry/Block Wall — Control Joints** | Locate and detail control joints under the applicable current TMS provision or approved project design. Do not apply a fixed spacing without the exact standard, edition, provision, and project scope. | TMS 402/602 or approved design | `masonry-block-walls.md` |
| 12 | **Retaining Wall — Permit Trigger** | Retaining walls >4 ft from bottom of footing to top of wall require a permit. Retaining walls supporting surcharge loads (driveways, structures, slopes) require a permit regardless of height. | CRC R105.2 | `retaining-walls.md` |
| 13 | **Retaining Wall — Engineering Required** | Retaining walls >4 ft require design by a registered design professional (California licensed civil/structural engineer or architect). Soils report typically required. Must address overturning, sliding, bearing pressure, and water uplift. Safety factor: minimum 1.5 (1.1 with seismic). | CBC 1807.2 | `retaining-walls.md` |
| 14 | **Retaining Wall — Drainage** | Drainage behind retaining walls is critical. Weep holes: 4" diameter at 6-8 ft OC along base, or perforated drain pipe behind wall with outlet. Filter fabric behind gravel drain fill to prevent soil migration. Surface drainage: grade away from top of wall. | CBC 1807.2; engineering practice | `retaining-walls.md` |
| 15 | **Retaining Wall — Guards** | Guards required at retaining walls within 36" of walking surfaces where the drop exceeds 30" measured vertically. Guard height: 42" minimum (residential). Guard openings: <=4" sphere passage. | CBC 1807.2.5; CRC R321 | `retaining-walls.md` |
| 16 | **Pool Barrier — Enclosure Height** | Minimum 60 inches (5 ft) for private pool enclosures (Swimming Pool Safety Act, HS Code 115923). Public pool enclosures: minimum 60 inches effective perpendicular height (CBC 3119B.1). | HS Code 115923; CBC 3119B.1 | `pool-barriers.md` |
| 17 | **Pool Barrier — Openings & Gaps** | No gaps allowing passage of a 4-inch diameter sphere. Maximum ground clearance: 2 inches at bottom. Chain link: maximum 1-3/4 inch mesh openings (CBC 3119B.1). No horizontal members that could serve as ladder for children — horizontal members spaced at least 48" apart (public pools). | HS Code 115923; CBC 3119B.1 | `pool-barriers.md` |
| 18 | **Pool Barrier — Climbability** | Outside surface free of protrusions, cavities, or physical characteristics that enable a child under 5 to climb. No planters or climbable structures within 5 ft of outside of pool enclosure (public pools). | HS Code 115923(e); CBC 3119B.1 | `pool-barriers.md` |
| 19 | **Pool Barrier — Gates** | Gates open away from pool. Self-closing and self-latching required. Latch placement: no lower than 60 inches above ground (private pools per HS Code 115923). Public pools: hand hardware 42-44 inches above deck (CBC 3119B.2). Gates must be lockable when pool is closed (public). | HS Code 115923; CBC 3119B.2 | `pool-barriers.md` |
| 20 | **Pool — Drowning Prevention Features** | New or remodeled private pools must have at least 2 of 7 drowning prevention features: (1) code-compliant enclosure, (2) removable mesh fencing (ASTM F2286), (3) safety pool cover (ASTM F1346-23), (4) exit alarms on doors/windows, (5) self-closing/self-latching device at 54"+ on doors, (6) pool alarm (ASTM F2208), (7) other approved means. Certain combinations prohibited. | HS Code 115922 | `pool-barriers.md` |
| 21 | **Glazing Near Pools** | Glazing in walls, enclosures, or fences adjacent to pools where the bottom edge is less than 60" above standing surface is a hazardous location — safety glazing required (CPSC 16 CFR 1201 or ANSI Z97.1). Exception: glazing more than 60" horizontally from water's edge. | CRC R324.4.5 | `pool-barriers.md` |
| 22 | **Property Line / Setbacks** | State code does not prescribe fence setbacks from property lines. Cities regulate setbacks through zoning code. Common city requirements: 0 ft setback (on property line) for side/rear, 15-20 ft setback in front yards, reduced height in front yard (3-4 ft typical). Always check city overlay. | City zoning code | `fence-height-materials.md` |
| 23 | **Sight Distance Triangle** | State code does not prescribe sight triangles — this is a city/county traffic engineering requirement. Typical: 10 ft x 10 ft triangle at intersections and driveways, maximum fence/wall height of 36 inches within the triangle. Purpose: maintain driver visibility. Always check city overlay. | City traffic/zoning code | `fence-height-materials.md` |
| 24 | **Wood Decay Protection** | Wood fence posts in ground contact must be naturally durable species (redwood heartwood, cedar heartwood, black locust) or pressure-treated per AWPA U1, Use Category 4B. Metal post bases (Simpson, etc.) can elevate wood above grade to avoid ground contact. | CRC R304.1, R304.4 | `fence-height-materials.md` |
| 25 | **Contractor Licensing** | C-13 (Fencing) license for fencing work. C-29 (Masonry) for block/masonry walls. B (General Building) may also perform this work. C-12 (Earthwork/Paving) for grading associated with retaining walls. Workers' compensation insurance required. | B&P Code 7028 | N/A |

#### STEP 5 — Output Format

For each checklist item, produce:

```
## [#]. [Check Name]
**Result:** PASS | FAIL | FLAG | N/A
**Code:** [Section number]
**Finding:** [1-2 sentence explanation of what was verified or what failed]
```

- **PASS** -- Requirement met per submitted information
- **FAIL** -- Requirement not met; cite code section and explain the deficiency
- **FLAG** -- Cannot determine from submitted data; explain what additional info is needed
- **N/A** -- Does not apply to this project (e.g., pool barrier checks when no pool is involved)

---

### Quick-Reference Tables

#### Permit Exemption Thresholds (State Code)

| Structure | Permit Exempt? | Condition | Code |
|---|---|---|---|
| Fence | YES | Height <=7 ft | CRC R105.2 |
| Fence | NO | Height >7 ft | CRC R105.2 |
| Retaining wall | YES | <=4 ft (footing to top), no surcharge | CRC R105.2 |
| Retaining wall | NO | >4 ft OR supporting surcharge | CRC R105.2 |

**Note:** Most cities use 6 ft as their permit-exempt threshold for fences. The 7 ft state threshold is a maximum — cities may (and commonly do) adopt lower thresholds.

#### Post Embedment Guidelines

| Fence Height | Minimum Post Depth | Minimum Footing Diameter | Post Size (wood) |
|---|---|---|---|
| 3-4 ft | 18" | 8" | 4x4 |
| 5-6 ft | 24" | 8"-10" | 4x4 |
| 7-8 ft | 30"-36" | 10"-12" | 4x6 or 6x6 |

#### Pool Barrier Requirements Summary

| Requirement | Private Pool (HS Code 115923) | Public Pool (CBC 3119B) |
|---|---|---|
| Minimum height | 60 inches (5 ft) | 60 inches (5 ft) |
| Maximum ground clearance | 2 inches | 2 inches |
| Maximum opening (sphere test) | 4 inches | 4 inches |
| Chain link max mesh opening | 1-3/4 inches | 1-3/4 inches |
| Gate swing direction | Away from pool | Away from pool |
| Gate self-closing/self-latching | Required | Required |
| Latch height (minimum) | 60 inches above ground | 42-44 inches above deck |
| Climbability | No handholds/footholds | No horizontal members within 48" |
| Drowning prevention features | 2 of 7 required | N/A (public pool rules differ) |

#### Masonry Wall Design Route

| Check | Route |
|---|---|
| Bond pattern | Running or stack bond under R606.3.7; apply R606.3.7.2 reinforcement where the head-joint offset is less than the running-bond minimum |
| Mortar | Table R606.2.8 or ASTM C270; select the type by use and SDC under R606.2.8.1–R606.2.8.3 |
| Reinforcement | Establish wall function, assigned SDC, thickness, bond, unit/grout construction, and loads; use applicable R606.12 provisions with Figures R606.11(1)-(3), or an approved TMS 402/403 design |
| Grouted cells | Fill cells containing reinforcement solidly with grout under R606.3.5.3 |

**Removed schedule boundary:** The former wall-height table prescribing #4 bars at 24-in. or 32-in. spacing, fixed footing widths/depths, a 48-bar-diameter splice, and a top-course/intermediate bond-beam schedule is not established as a statewide CRC recipe. Restore a local standard detail only with the named jurisdiction, current document and edition or effective date, page/table/detail locator, geographic and project-type scope, and confirmation that the source remains current.

**TMS corpus gap:** R606.12 incorporates TMS 402/403 as an approved design path, but the full TMS text is not available in the reviewed corpus. Do not quote a TMS numerical recipe until the applicable current standard and exact provision are available and scoped to the project.

#### Retaining Wall Engineering Triggers

| Condition | Engineering Required? |
|---|---|
| Height <=4 ft, no surcharge, level backfill | No (prescriptive OK) |
| Height >4 ft | Yes |
| Any height with surcharge (driveway, building, slope above) | Yes |
| Adverse soil conditions (expansive, liquefiable, fill) | Yes |
| Slope above or below wall | Typically yes |
| Tiered walls within influence zone | Yes |

---

### Key Principles

1. **State permit threshold is 7 ft, but cities go lower.** The CRC exempts fences <=7 ft from permits, but nearly all California cities set their threshold at 6 ft or lower. Always verify the local threshold before telling an applicant no permit is needed.
2. **Retaining walls are different from fences.** Retaining walls hold back soil and must resist lateral earth pressure. The 4 ft height trigger (from bottom of footing to top of wall) is the state threshold for requiring a permit and typically engineering.
3. **Pool barriers are life-safety critical.** The Swimming Pool Safety Act requires specific enclosure characteristics (60" height, 4" sphere test, self-closing/self-latching gates) and at least 2 of 7 drowning prevention features for new/remodeled private pools.
4. **Masonry reinforcement is project-specific.** Establish the wall's structural role, assigned SDC, thickness, bond, unit/grout construction, and loads before selecting the applicable R606.12 provisions with Figures R606.11(1)–R606.11(3), or an approved TMS 402/403 design. Cells containing reinforcement must be filled solidly with grout under R606.3.5.3.
5. **Wind loads matter.** Solid fences and walls act as wind sails. Post size, embedment depth, and footing size must account for wind exposure, especially in coastal and high-wind areas.
6. **Height is measured from finished grade.** For fences on slopes or retaining walls, height is measured from the higher adjacent grade. Combined fence-on-retaining-wall height is measured from the lower grade.
7. **Sight distance triangles are city-regulated.** The state code does not prescribe sight triangles, but virtually all cities restrict fence/wall height within sight triangles at intersections and driveways (typically 36" max within a 10x10 ft triangle).
8. **Wood in ground contact must be protected.** Ground-contact posts must be naturally durable species or pressure-treated per AWPA U1. Untreated pine, fir, or spruce posts will rot.
