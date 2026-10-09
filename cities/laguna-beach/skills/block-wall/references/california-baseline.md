# California Baseline — Block Wall

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Block Wall (CMU Masonry) — State Regulatory Decision Engine

This skill contains California state-level requirements for **freestanding concrete masonry unit (CMU) block walls** extracted from the 2025 California Building Code (CBC), California Residential Code (CRC), and referenced standards TMS 402/602. It covers the most common residential and light commercial block wall types.

**What this covers**: State building code — the requirements that apply everywhere in California. Every city must enforce at least these standards.
- Freestanding property line walls, boundary walls, privacy walls, garden walls, screen walls
- CMU material specifications (ASTM C90, mortar, grout, rebar)
- Reinforcement requirements (vertical, horizontal, bond beams, seismic minimums)
- Foundation/footing design by wall height
- Seismic design requirements (SDC D — most of California)
- Wind loads on freestanding solid walls
- Expansion/control joints, grouting, cleanouts, capping
- Permit thresholds, engineering triggers, contractor licensing

**What this does NOT cover**: City-specific ordinances, local standard detail sheets, city-specific height limits or setbacks, aesthetic requirements (ornamental block mandates, color restrictions), HOA or CC&R requirements, city permit fee schedules. Use the city-level block-wall skill for those. Does NOT cover retaining walls (see `../../retaining-wall/references/california-baseline.md`), load-bearing structural walls in buildings, foundation walls, or sound walls.

---

### How to Use This Skill

When reviewing a block wall permit or answering a block wall code question, follow the decision tree below. Each step tells you which reference files to load. Load only what you need — most reviews require 2-3 reference files, not all of them.

After loading references, check the **Quick-Reference Tables** below for the key numbers that come up in almost every block wall review.

---

### Decision Tree Router

#### STEP 1 — Does This Project Need a Permit?

| Condition | Permit Required? | Code Section | Reference File |
|---|---|---|---|
| Freestanding wall <=7 ft high | NO (exempt per state code) | CRC R105.2 | `permit-thresholds.md` |
| Freestanding wall >7 ft high | YES | CRC R105.2 | `permit-thresholds.md` |
| Any height wall in a city with lower threshold | Check city overlay — most cities set 6 ft or lower | City municipal code | `permit-thresholds.md` |
| Block wall functioning as retaining wall (holds soil) | Use retaining wall thresholds (4 ft) | CRC R105.2 | `permit-thresholds.md` |
| Block wall combined with retaining wall (wall on top of retaining wall) | Both structures must independently comply; total height from lower grade | CRC R105.2 | `permit-thresholds.md` |

**Critical note:** The state exemption at 7 ft is a ceiling, not a floor. Nearly all California cities set their block wall permit threshold at 6 ft or lower. Some cities (e.g., Laguna Hills) exempt block walls up to 6 ft; others require permits at 4 ft. Always check the city overlay skill.

#### STEP 2 — What Type of Review Is This?

| Review Type | Load These References |
|---|---|
| **Full permit review** (plans submitted, pass/fail) | `materials-specifications.md`, `reinforcement-design.md`, `foundation-footing.md`, `construction-details.md` |
| **Permit threshold question only** (do I need a permit?) | `permit-thresholds.md` |
| **Engineering requirement question** (do I need an engineer?) | `permit-thresholds.md` |
| **Material/specification question** (what block, mortar, grout?) | `materials-specifications.md` |
| **Reinforcement question** (rebar size, spacing, seismic) | `reinforcement-design.md` |
| **Footing/foundation question** (width, depth, dowels) | `foundation-footing.md` |
| **Construction detail question** (control joints, grouting, capping) | `construction-details.md` |
| **Wind load question** | `reinforcement-design.md` |

#### STEP 3 — Walk the Review Checklist

For a full permit review, check each item in order. Record PASS / FAIL / FLAG / N/A with the code section cited.

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 1 | **Permit Required?** | Freestanding walls <=7 ft are exempt per state code. Cities commonly set lower thresholds (4-6 ft). Block walls functioning as retaining walls use the 4 ft threshold. Check city overlay. | CRC R105.2 | `permit-thresholds.md` |
| 2 | **Height Measurement** | Height measured from finished grade on the higher side to top of wall (including cap). For walls on slopes, measure from the higher adjacent grade. For walls on retaining walls, combined height measured from lower grade. | CRC R105.2; local practice | `permit-thresholds.md` |
| 3 | **Engineering Required?** | Walls over 6 ft typically require structural engineering by a CA licensed civil/structural engineer. Walls 4-6 ft may use prescriptive city standard details OR engineering. Cities set their own engineering trigger heights. | CBC 2101.2; city code | `permit-thresholds.md` |
| 4 | **CMU Block Specification** | ASTM C90, load-bearing concrete masonry units. Grade N (moisture-controlled) for exterior. Minimum f'm = 1,500 psi. Standard: 8" x 8" x 16" nominal (7-5/8" x 7-5/8" x 15-5/8" actual). Running bond required (CRC R606.8). | CRC R606.2.1; CBC 2103.1; ASTM C90 | `materials-specifications.md` |
| 5 | **Mortar Type** | Type M or S required for structural masonry in California seismic zones. Type M (2,500 psi) preferred for below-grade/ground contact. Type S (1,800 psi) acceptable above-grade. Type N NOT acceptable for freestanding exterior walls. Must comply with ASTM C270. | CRC R606.2.8.3; CBC 2103.2 | `materials-specifications.md` |
| 6 | **Grout Specification** | ASTM C476, minimum f'c = 2,000 psi. Slump 8-11 inches (pourable). Fine grout for cells <=2" wide; coarse grout for cells >2" wide. All cells with rebar fully grouted. Consolidation by mechanical vibration or puddling required. | CRC R606.2.12; CBC 2103.3 | `materials-specifications.md` |
| 7 | **Rebar Specification** | ASTM A615 or A706, Grade 60 (60,000 psi yield). Minimum bar size: #4 (1/2" diameter). Minimum cover: 5/8" in grouted cells. Lap splice: 48 bar diameters minimum (#4 = 24" minimum). | TMS 402/602 | `materials-specifications.md` |
| 8 | **Vertical Reinforcement** | Vertical rebar resists overturning from wind and seismic. Spacing by height: #4@32" OC for walls <=4 ft, #4@24" OC for 4-6 ft, #5 or per engineering for >6 ft. Extends from footing through full wall height. | CRC R606.11; TMS 402 | `reinforcement-design.md` |
| 9 | **Horizontal Reinforcement** | Bond beam with #4 rebar at top course minimum. Additional bond beams every 24" OC for walls >4 ft. Joint reinforcement (9 gauge ladder/truss type) as alternative at intermediate courses. | CRC R606.11; TMS 402 | `reinforcement-design.md` |
| 10 | **Seismic Reinforcement (SDC D)** | Most of California is SDC D. Minimum horizontal AND vertical reinforcement each >= 0.0007 Ag, total >= 0.002 Ag. Maximum spacing 48" OC. Rebar at all corners, ends, and adjacent to openings. Unreinforced masonry NOT permitted. All cells with rebar fully grouted. | CBC 2106.1; TMS 402 Ch. 7 | `reinforcement-design.md` |
| 11 | **Footing Width & Depth** | Continuous reinforced concrete footing required. Width increases with wall height: 12" for <=3 ft, 12-18" for 3-4 ft, 18-24" for 4-5 ft, 24-30" for 5-6 ft. Minimum 12" depth. Footing below grade: 12" minimum cover. | CRC R403; CBC 1807.1.6 | `foundation-footing.md` |
| 12 | **Footing Reinforcement** | Minimum 2-#4 bars continuous, placed 3" from top and bottom. Concrete: f'c >= 2,500 psi. Footing centered under wall with minimum 6" on each side. | CRC R403; ACI 318 | `foundation-footing.md` |
| 13 | **Footing Dowels** | Vertical dowels from footing into wall matching wall vertical rebar size and spacing. Minimum 24" embedment into footing (hooked bars) or per lap splice length. Dowels extend minimum 24" above footing into wall. | TMS 402/602 | `foundation-footing.md` |
| 14 | **Expansion/Control Joints** | Maximum spacing: 20-25 ft (TMS 402 recommendation based on L/H ratio). Also required at changes in height, thickness, direction, and at connections to buildings. Rebar does NOT cross control joints. Sealed with backer rod and elastomeric sealant. | TMS 402 | `construction-details.md` |
| 15 | **Grouting** | All reinforced cells fully grouted. Maximum lift height: 5 ft without cleanouts. Consolidate by mechanical vibration. Reconsolidate 3-5 minutes after initial pour. Maximum grout pour: 8 ft per lift (CRC R606.3.5.1). | CRC R606.3.5; TMS 602 | `construction-details.md` |
| 16 | **Cleanout Openings** | Required at base of grouted cells where grout lift >5 ft (64 inches). Minimum 3" x 3" opening. Clean debris before grouting. Seal before grout placement. Walls <=4 ft: cleanouts typically not required (single lift with reconsolidation). | CRC R606.3.5.2; TMS 602 | `construction-details.md` |
| 17 | **Wall Cap / Top Course** | Bond beam block at top course with continuous #4 rebar minimum. Cap must shed water. Options: precast concrete cap, stone cap, stucco-over-block, exposed bond beam with tooled joints. Drip edge recommended. | TMS 402; engineering practice | `construction-details.md` |
| 18 | **Wind Load** | Freestanding solid walls must resist wind per ASCE 7-22 / CBC 1609. Most of California: 110-115 mph basic wind speed. Solid walls receive full wind pressure (no solidity ratio reduction). Wind governs post/footing design for walls <=4 ft. Seismic governs for taller walls. | CBC 1609; ASCE 7-22 | `reinforcement-design.md` |
| 19 | **Property Line / Setbacks** | State code does not prescribe setbacks. Cities regulate via zoning code. Common: 0 ft for side/rear, 15-20 ft in front yards, reduced height in front. Some cities require Common Property Line Wall Agreement for shared walls. Always check city overlay. | City zoning code | `permit-thresholds.md` |
| 20 | **Sight Distance Triangle** | State code does not prescribe sight triangles — city/county requirement. Typical: 10x10 ft triangle at intersections/driveways, max 36" wall height within triangle. | City traffic/zoning code | `permit-thresholds.md` |
| 21 | **Contractor Licensing** | C-29 (Masonry) required for block/masonry wall construction. B (General Building) may also perform. C-13 (Fencing) is NOT correct for masonry block walls. Workers' compensation insurance required. | B&P Code 7028 | N/A |
| 22 | **Soil Bearing** | Footing must bear on undisturbed native soil or engineered fill. Minimum assumed bearing: 1,500 psf per CRC Table R401.4.1(1). Expansive soils: may require Type V cement, deeper footings, or soils report. | CRC R401.4; CBC 1803 | `foundation-footing.md` |

#### STEP 4 — Output the Review Result

For each checklist item, output one of:
- **PASS** -- Requirement met per submitted information
- **FAIL** -- Requirement not met; cite code section and explain the deficiency
- **FLAG** -- Cannot determine from submitted data; explain what additional info is needed
- **N/A** -- Does not apply to this project

```
## [#]. [Check Name]
**Result:** PASS | FAIL | FLAG | N/A
**Code:** [Section number]
**Finding:** [1-2 sentence explanation of what was verified or what failed]
```

---

### Quick-Reference Tables

#### Permit and Engineering Thresholds

| Condition | Permit? | Engineering? | Code Section |
|---|---|---|---|
| Freestanding wall <=7 ft (state code) | No | No (prescriptive OK) | CRC R105.2 |
| Freestanding wall >7 ft | Yes | Typically yes | CRC R105.2 |
| City threshold (common: 6 ft) | Check city | Varies (4-6 ft trigger) | City municipal code |
| Block wall also retaining soil | 4 ft threshold applies | Yes if >4 ft | CRC R105.2 |
| Wall near slope or surcharge | Check retaining wall rules | Likely yes | CBC 1807.2 |

#### Prescriptive Reinforcement by Wall Height

| Wall Height | Vertical Rebar | Horizontal Rebar | Bond Beams |
|---|---|---|---|
| Up to 3 ft | #4 @ 32" OC | #4 bond beam at top | Top course |
| 3-4 ft | #4 @ 32" OC | #4 bond beam at top | Top course |
| 4-5 ft | #4 @ 24" OC | #4 @ 24" OC | Top + every 24" |
| 5-6 ft | #4 @ 24" OC | #4 @ 24" OC | Top + every 24" |
| Over 6 ft | #5 or per engineering | Per engineering | Per engineering |

**SDC D minimum (most of CA):** Horizontal AND vertical each >= 0.0007 Ag, total >= 0.002 Ag. Max spacing 48" OC.

#### Footing Dimensions by Wall Height

| Wall Height | Min Footing Width | Min Footing Depth | Footing Rebar |
|---|---|---|---|
| Up to 3 ft | 12" | 12" | 2-#4 continuous |
| 3-4 ft | 12"-18" | 12" | 2-#4 continuous |
| 4-5 ft | 18"-24" | 18" | 2-#4 continuous |
| 5-6 ft | 24"-30" | 18"-24" | 2-#5 or 3-#4 continuous |

Footing concrete: f'c >= 2,500 psi. Footing width typically 2x-2.5x wall thickness (8" wall = 16"-20").

#### Material Specifications Summary

| Material | Standard | Key Requirement |
|---|---|---|
| CMU block | ASTM C90, Grade N | f'm >= 1,500 psi, 8x8x16 nominal |
| Mortar | ASTM C270, Type M or S | Type M: 2,500 psi; Type S: 1,800 psi |
| Grout | ASTM C476 | f'c >= 2,000 psi, 8-11" slump |
| Rebar | ASTM A615/A706, Grade 60 | Minimum #4 (1/2" dia) |
| Lap splice | 48 bar diameters | #4 = 24" min; #5 = 30" min |

#### Seismic Design Category Reference

| SDC | Reinforcement Requirement | Typical Locations |
|---|---|---|
| A, B | Minimal; prescriptive OK | Low-seismicity areas (rare in CA) |
| C | Horizontal reinforcement required per TMS 402 Sec. 7.4.3 | Limited areas in CA |
| **D (most of CA)** | **Reinforced masonry required. V + H each >= 0.0007 Ag, total >= 0.002 Ag. Max 48" OC. Rebar at corners, ends, openings. All grouted.** | **Most California cities** |
| E, F | Same as D with additional requirements | High-seismicity areas (e.g., near active faults) |

#### Expansion/Control Joint Spacing

| Method | Maximum Spacing |
|---|---|
| TMS 402 (L/H ratio) | Typically 20-25 ft for 6 ft wall |
| Common city standard details | 20-30 ft |
| Rule of thumb | 2.5x wall height (6 ft wall = 15 ft) to 3x height |

Also required at: changes in height, changes in thickness, changes in direction, connections to buildings, and near openings.

---

### Key Principles

1. **Unreinforced masonry is not acceptable in California.** Most of California is SDC D or higher. Every freestanding CMU block wall must have both vertical and horizontal reinforcement with grouted cells. There is no such thing as a code-compliant dry-stacked or unreinforced block wall for exterior use.

2. **The 7 ft state threshold rarely applies in practice.** While CRC R105.2 exempts fences and freestanding walls <=7 ft from permits, nearly all cities set their threshold at 6 ft or lower. Some cities exempt block walls below their threshold but still require structural design due to seismic conditions.

3. **Block walls are NOT fences for licensing purposes.** A block wall requires a C-29 (Masonry) contractor or B (General Building) contractor. A C-13 (Fencing) contractor is the wrong license class for masonry construction.

4. **Height measurement matters.** Height is from finished grade on the higher side to top of wall including cap. For walls on slopes, stepped footings affect how height is measured segment by segment. For block walls on retaining walls, total height is from the lower grade.

5. **Footing design scales with wall height.** A 3 ft garden wall needs a 12" wide footing; a 6 ft property line wall needs 24-30". The footing must bear on undisturbed soil, be centered under the wall, and have dowels matching the wall's vertical rebar.

6. **Wind loads govern short walls; seismic governs tall walls.** For walls <=4 ft in most of California, wind pressure on the solid face is the critical load case. For walls >4 ft, seismic overturning forces typically control the design.

7. **Control joints prevent random cracking.** CMU walls expand and contract with temperature and moisture changes. Without properly spaced control joints, walls develop unsightly random cracks. Space at 20-25 ft maximum and at all changes in geometry.

8. **Grouting quality is the most common construction deficiency.** Voids in grouted cells from poor consolidation are invisible after construction. Require mechanical vibration, reconsolidation, and cleanout openings for lifts over 5 ft.
