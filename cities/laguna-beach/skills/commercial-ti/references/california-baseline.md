# California Baseline — Commercial Tenant Improvement

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Commercial TI — State Regulatory Decision Engine

This skill contains California state-level commercial Tenant Improvement (TI) rules synthesized from Title 24 Parts 2, 3, 4, 6, 9, 10, and 11, plus the federal ADA Title III "path-of-travel" overlay. It covers every interior alteration to an existing non-residential building EXCEPT:

- **Restaurant TI** — handled by `california-restaurant-ti` (Type-1 hoods, grease interceptors, CRFC health construction). Restaurant scopes ALWAYS route to that sibling skill. See `cross-reference-restaurant-ti.md`.
- **OSHPD** (hospitals, SNFs, clinics under HCAI jurisdiction) and **DSA** (K-12 + community colleges) — separate state agencies, not the local Building Department.
- **Group H** high-hazard occupancies (hazmat storage/use, semiconductor fab) — requires separate Hazardous Materials Inventory Statement (HMIS) review.

**What this covers**: State law — the floor that every California jurisdiction must enforce. Cities/counties may add requirements (e.g., local energy reach codes, demolition fees, business-license overlays) but cannot waive these.

**What this does NOT cover**: City/county-specific submittal portals, fee schedules, local amendments, or project-specific engineering. Use the city-level `commercial-ti` skill for those.

### How to Use This Skill

When reviewing a commercial TI submission, follow the 3-step decision tree below. Each step tells you which reference files to load. Load only what you need — most reviews require 3-6 reference files, not all 7.

---

### Decision Tree Router

#### STEP 1: Classify the Project Type

What kind of commercial TI is this?

| Project Type | Always Load | Description |
|---|---|---|
| **Like-for-like refresh** (paint, carpet, ceiling tiles, no system changes) | `occupancy-classification.md` only | CEBC Level 1 alteration — minimal review |
| **Interior remodel, same occupancy** (new walls, doors, finishes, lighting) | `occupancy-classification.md`, `accessibility-upgrades.md`, `energy-alterations.md` | CEBC Level 2 — most common TI |
| **Major interior overhaul** (work area >50% of building) | `occupancy-classification.md`, `accessibility-upgrades.md`, `energy-alterations.md`, `fire-life-safety.md`, `structural-alterations.md` | CEBC Level 3 — full Level-3 trigger set |
| **Change of occupancy** (e.g., B → A-3 yoga studio, M → A-2 — route to restaurant-ti, S → B office) | All 6 disciplinary refs + `cross-reference-restaurant-ti.md` if food | CEBC Ch.10 triggers cascade |
| **Restaurant scope detected** (kitchen with cooking, grease, food prep) | `cross-reference-restaurant-ti.md` then STOP — hand off | Route to `california-restaurant-ti` skill |

#### STEP 2: Load Discipline-Specific References

Load each reference whose trigger condition is met. Most TIs hit 4-5 of these.

##### Occupancy Classification (CBC Ch. 3) — applies to ALL TIs

| Condition | Load These References |
|---|---|
| **Always** | `occupancy-classification.md` — A/B/M/F/S/U group determination, change-of-occupancy detection, mixed-use separations, occupant-load factors |

##### Accessibility (CBC Ch. 11B + ADA Title III) — applies to ALL TIs

| Condition | Load These References |
|---|---|
| **Always** (any alteration to a public-accommodation, commercial, or public building) | `accessibility-upgrades.md` — 11B-202.3 element compliance, 11B-202.4 path-of-travel, 20% disproportionality rule, restroom/parking/signage triggers |
| EVCS installation in scope | `accessibility-upgrades.md` — 11B-202.4 Exception 10 (EVCS-only 20% cap) |
| Multistory building / mezzanine work | `accessibility-upgrades.md` — 11B-202.4 Exception 9 (multistory 20% PoT) |

##### Fire & Life Safety (CBC Ch. 9, CFC, CEBC 1011.2) — applies broadly

| Condition | Load These References |
|---|---|
| Change of occupancy in any direction | `fire-life-safety.md` — sprinkler retrofit per CEBC 1011.2.1, fire-alarm thresholds per 1011.2.2 |
| Fire area increases OR demising walls altered OR occupancy load >=100 | `fire-life-safety.md` — A-2/B/M/F-1/S-1 sprinkler triggers (CBC 903.2.x) |
| Egress changes (new exit, dead-end corridor, travel-distance change) | `fire-life-safety.md` — egress + alarm thresholds, fire-area separation |
| Mixed occupancy in tenant (e.g., S-1 storage adjacent to B office) | `fire-life-safety.md` — mixed-occupancy separation per CBC 508/Table 508.4 |

##### Energy (Title 24 Part 6 §141.0) — applies whenever envelope, lighting, HVAC, or service-water-heating systems are touched

| Condition | Load These References |
|---|---|
| Any lighting alteration touching >=10% of luminaires in an enclosed space | `energy-alterations.md` — §141.0(b)2I lighting alteration triggers, three compliance paths (i/ii/iii) |
| HVAC equipment replaced / added / extended | `energy-alterations.md` — §141.0(b)2C HVAC alteration rules, Table 141.0-E-1 packaged-unit requirements |
| Duct work extended or replaced | `energy-alterations.md` — §141.0(b)2D duct sealing + leakage testing |
| Roof altered (recover/recoat/replace, >2,000 sf or >50% of roof) | `energy-alterations.md` — §141.0(b)2B cool-roof + insulation triggers |
| Vertical fenestration: added >50 sf OR replaced >150 sf | `energy-alterations.md` — §141.0(b)1E fenestration triggers, Table 141.0-A U-factor |
| Service water heater replaced / added | `energy-alterations.md` — §141.0(b)2N |
| Existing wall area: >=25% altered | `energy-alterations.md` — §141.0(b)2Q air-leakage requirement |

##### Structural / Existing Building Code (CEBC Part 10) — applies to any TI with system or structural reconfiguration

| Condition | Load These References |
|---|---|
| **Always** (every TI is by definition an alteration to an existing building) | `structural-alterations.md` — Ch.6 alteration-level classification, Ch.7 Level 1, Ch.8 Level 2, Ch.9 Level 3, Ch.10 change-of-occupancy structural |
| Roof-mounted equipment added (RTUs, solar, screens) | `structural-alterations.md` — gravity load reverification per Level 2/3 |
| Change of occupancy to higher Risk Category (II → III/IV) | `structural-alterations.md` — CEBC 1006.3 seismic; lateral-system re-evaluation required |
| Live-load increase area > 5% demand-capacity bump | `structural-alterations.md` — CEBC 1006.1 live load |

##### CALGreen Nonresidential (Title 24 Part 11) — applies to permitted alterations >= $200K valuation

| Condition | Load These References |
|---|---|
| Alteration valuation >= $200K (BSC scope) | `calgreen-nonresidential.md` — all mandatory measures, §301.3 |
| ANY permitted alteration (regardless of cost) | `calgreen-nonresidential.md` — §5.408 construction waste 65% diversion is required for ALL permitted alterations per §301.3.2 |
| Plumbing fixtures updated | `calgreen-nonresidential.md` — §5.303 indoor water use + CCR §1101.1 retroactive fixture replacement for "commercial real property" |
| Adhesives / sealants / paints / floor finishes specified | `calgreen-nonresidential.md` — §5.504 pollutant control (VOC limits) |

##### Cross-Reference: Restaurant Boundary

| Condition | Load These References |
|---|---|
| Project includes ANY commercial cooking, food prep sink, walk-in cooler, grease-producing equipment, or A-2 dining occupancy | `cross-reference-restaurant-ti.md` — then route to `california-restaurant-ti` for the food-service envelope |

#### STEP 3: Walk the Review Checklist

Eight discipline tables, 112 rows. Each row carries an **ID**, an applicability **Tag**, the pass criteria, the governing **Code Section**, and the **Likely sheets** where the evidence lives.

| # | Discipline | Reference file | Rows | Tags present |
|---|---|---|---|---|
| 1 | Occupancy classification | `occupancy-classification.md` | OC-1..OC-10, OCC-11..OCC-12 | `ALL`, `ASSEMBLY-50+`, `CHANGE-OF-OCCUPANCY`, `CITY-DELTA` |
| 2 | Egress / means of egress | `egress-life-safety.md` | EG-1..EG-10 | `ALL`, `ASSEMBLY-50+`, `CHANGE-OF-OCCUPANCY` |
| 3 | Fire & life safety | `fire-life-safety.md` | FL-1..FL-12, FP-13..FP-14 | `ALL`, `CHANGE-OF-OCCUPANCY`, `SPRINKLERED`, `CITY-DELTA` |
| 4 | Accessibility | `accessibility-upgrades.md` | AC-1..AC-16 | `ALL`, `ACCESSIBILITY-TRIGGERED` |
| 5 | Structural / existing building | `structural-alterations.md` | ST-1..ST-18 | `ALL`, `CHANGE-OF-OCCUPANCY`, `STRUCTURAL-TOUCHED`, `LEVEL-2+`, `LEVEL-3` |
| 6 | MEP scope & completeness | `mep-scope.md` | MEP-1..MEP-10 | `ALL`, `CHANGE-OF-OCCUPANCY` |
| 7 | Energy (Title 24 Part 6) | `energy-alterations.md` | EN-1..EN-19 | `ALL`, `NEW-WORK`, `SITE` |
| 8 | CALGreen (Title 24 Part 11) | `calgreen-nonresidential.md` | CG-1..CG-13 | `ALL`, `CITY-DELTA` |

| Tag | Dispatch when |
|---|---|
| `ALL` | Always — the default for a commercial TI |
| `ACCESSIBILITY-TRIGGERED` | Any alteration to a public-accommodation / commercial building (i.e. effectively always; the tag exists to separate element compliance from path-of-travel scoping) |
| `CHANGE-OF-OCCUPANCY` | The cover declares, or the evidence shows, a change of occupancy classification |
| `NEW-WORK` | Envelope, roof, or fenestration is added or replaced |
| `SITE` | Scope extends outside the building envelope — site lighting, signs, parking |
| `ASSEMBLY-50+` | Any assembly, classroom, or dining space at or above the occupant-load posting threshold |
| `STRUCTURAL-TOUCHED` | Structural elements, roof loads, or excavation/shoring are in scope |
| `LEVEL-2+` / `LEVEL-3` | The CEBC alteration level classified in ST-1 reaches Level 2 or Level 3 |
| `SPRINKLERED` | The building is sprinklered (head relocation, hydraulic continuity) |
| `CITY-DELTA` | Always evaluated, but the THRESHOLD comes from the city overlay — never answer one of these from state law alone |

**Known cross-discipline duplicates — emit ONE finding, not two:**
- `FL-12` and `EG-8` are the same check (exit signs + egress illumination, CBC 1008/1013).
- `ST-14` and `MEP-4` are the same check (fixture recount on a change of occupancy, CEBC 1009.1).

**Why the five `CITY-DELTA` review rows ARE here.** `CG-4`, `FP-13`, `FP-14`, `OCC-11`, `OCC-12` are dispatched on EVERY commercial-TI review — the tag means *always evaluated, threshold supplied by the city overlay*, not *skip until a city is onboarded*. For a city with no overlay content the honest answer is a `verify` naming the missing city input; it is never a silent PASS. Leaving them out would drop live review capability (`FP-13`, city sprinkler thresholds, is life-safety-adjacent).

#### STEP 4: Output the Review Result

For each checklist item in the loaded reference files, output one of:
- **PASS** — requirement met, cite code section
- **FAIL** — requirement not met, cite code section and explain
- **FLAG** — cannot determine from submitted data, explain what info is needed
- **N/A** — does not apply to this project

---

### Quick-Reference Thresholds

These come up in nearly every commercial TI review. Check here first.

#### Sprinkler Trigger Thresholds (CBC 903.2.x) — New Construction Basis

| Occupancy | Sprinkler Required When |
|---|---|
| **A-2** (food/drink assembly) | Fire area > 5,000 sf OR occupant load >=100 OR not on exit-discharge level (CBC 903.2.1.2) |
| **A-1/A-3/A-4** | Fire area > 12,000 sf OR occupant load >=300 OR not on exit-discharge level (CBC 903.2.1.1/.3/.4) |
| **B** (office/business) | Not generally sprinkler-required by occupancy alone (CBC 903.2.2 — ambulatory care + lithium battery R&D only) |
| **F-1** (moderate factory) | Fire area > 12,000 sf OR > 3 stories above grade OR combined > 24,000 sf (CBC 903.2.4) |
| **M** (retail/merc) | Fire area > 12,000 sf OR > 3 stories OR combined > 24,000 sf (CBC 903.2.7) |
| **S-1** (moderate storage) | Fire area > 12,000 sf OR > 3 stories OR combined > 24,000 sf (CBC 903.2.9) |

Per CEBC 1011.2.1, when a **change of occupancy** crosses a new sprinkler threshold, the sprinkler installation is required in the change-of-occupancy area plus all areas not separated by a fire wall.

#### Fire Alarm Trigger Thresholds (CBC 907.2.x)

| Occupancy | Manual Fire Alarm Required When |
|---|---|
| **A** | Occupant load >=300 in assembly OR Group A occupant load > 100 above/below level of exit discharge (CBC 907.2.1) |
| **A** (1,000+ occupants) | Emergency voice/alarm communication (CBC 907.2.1.1) |
| **B** | Combined occupant load >=500 OR > 100 occupants above/below exit-discharge level (CBC 907.2.2) |
| **M** | Combined occupant load >=500 OR > 100 above/below exit-discharge level (CBC 907.2.7) |

Sprinkler exception: where the building is fully sprinklered to NFPA 13, the manual pull-stations may be eliminated and notification operates via waterflow.

#### Occupancy Reclassification Quick-Map (CBC 303-312)

| Old Use → New Use | Classification Change | Notes |
|---|---|---|
| Office → Office (B → B) | Same occupancy — Level 1/2/3 alteration only | Most common TI |
| Retail → Office (M → B) | LOWER hazard per Tables 1011.5/1011.6 | Existing elements deemed acceptable |
| Office → Retail (B → M) | Hazard category 4 → 3 (Table 1011.5) — HIGHER | CEBC Ch.10 triggers |
| Warehouse → Office (S-1 → B) | Both Category 4 means-of-egress — equal | But CEBC 1006.3 seismic check still required if Risk Category bumps |
| Office → Yoga / Fitness (B → A-3 if OL>=50 / B if OL<50 / B if room<750 sf) | Verify OL first | CBC 303.1.1, 303.1.2 — small-assembly carve-outs |
| Retail → Restaurant (M → A-2) | **Route to california-restaurant-ti** | See cross-reference |
| Office → Childcare (B → E or I-4) | OUT OF SCOPE for this skill | Title 22 + DSS licensing |
| Office → Medical clinic (B → B Ambulatory Care or I-2) | Stays B if outpatient + ambulatory; I-2 if 24-hr or >=4 non-ambulatory | CBC 304.3, 422 (ambulatory care) |

#### Occupant Load Factors (CBC Table 1004.5) — TI-Relevant Subset

| Function | Factor (sf per occupant) |
|---|---|
| Accessory storage, mech equipment room | 300 gross |
| Business areas (general office) | 150 gross |
| Concentrated business (call center, trading floor, data entry) | 50 gross (per 1004.8 minimum) |
| Mercantile (sales area, all floors) | 60 gross |
| Storage, stock, shipping areas | 300 gross |
| Industrial areas | 100 gross |
| Assembly, concentrated (chairs only, non-fixed) | 7 net |
| Assembly, standing space | 5 net |
| Assembly, unconcentrated (tables & chairs) | 15 net |
| Exercise rooms | 50 gross |
| Day care | 35 net |
| Library reading rooms | 50 net |
| Library stack area | 100 gross |

#### Accessibility Path-of-Travel "20% Rule" Quick Logic (CBC 11B-202.4 Exception 8)

```
If adjusted construction cost <= current state valuation threshold (DSA-published annually; 2026 = $209,208.00, eff. 1/19/2026):
  PoT compliance is REQUIRED but cost is CAPPED at 20% of project adjusted construction cost.
Else (project exceeds threshold):
  Full PoT compliance is REQUIRED unless local enforcing agency makes a written unreasonable-hardship finding.
  Minimum PoT spend is still 20% of adjusted construction cost.
```

**Aggregation rule** (CBC 11B-202.4 Exception 8 final paragraph): If a path of travel was previously left un-upgraded during an alteration in the prior 3 years, the cumulative cost across those alterations counts toward the 20%.

**Priority order** when partial PoT is provided:
1. Accessible entrance
2. Accessible route to altered area
3. At least one accessible restroom per sex OR one unisex
4. Accessible telephones
5. Accessible drinking fountains
6. Other (parking, signage, alarms)

#### ADA Title III Federal Overlay (28 CFR 36.403)

The 20% disproportionality rule is *also* federal ADA — California's 11B-202.4 Exception 8 was written to track 28 CFR 36.403. The federal rule applies regardless of California valuation threshold, so for federally-covered public accommodations both are in play. Where federal is stricter (e.g., "primary function area" alterations always trigger PoT regardless of cost), federal wins.

#### Energy Alteration Quick Triggers (Title 24 Part 6 §141.0(b))

| Trigger | Threshold | Section |
|---|---|---|
| Lighting alteration compliance | >=10% of luminaires in an enclosed space | §141.0(b)2I |
| Vertical fenestration U-factor mandate (Table 141.0-A) | > 150 sf of building vertical fenestration replaced | §141.0(b)1E.1 |
| Added vertical fenestration to 120.7(d) | > 50 sf added | §141.0(b)1E.2 |
| Cool-roof / insulation triggers | Roof replace/recover, > 2,000 sf or > 50% of roof area (whichever is less) | §141.0(b)2B |
| HVAC packaged unit (DX < 65,000 Btu/h) | New or replacement on retail / grocery / school / office / library | Table 141.0-E-1 |
| Demand-responsive thermostat | Any altered space-conditioning unit | §141.0(b)2E.i |
| Duct leakage acceptance test | Entirely new / complete-replacement duct system | §141.0(b)2D.i |
| Wall air-leakage spec | >=25% of an existing envelope wall altered | §141.0(b)2Q |

#### CALGreen Nonresidential Scope (Title 24 Part 11 §301.3)

| Trigger | What Applies |
|---|---|
| New construction OR addition >=1,000 sf OR alteration permit valuation >= $200K | Full Chapter 5 mandatory measures (with [A] banner sections limited to scope of altered area) |
| ANY permitted alteration (regardless of valuation) | §5.408 — 65% C&D waste diversion plan |
| Alteration updates plumbing fixtures only | §301.3.1 + CCR §1101.1 commercial-real-property fixture replacement triggers (CA Civil Code 1101.3+) |
| Addition >=1,000 sf OR alteration valuation >= $200K | §5.408.2 — verify prohibited universal-waste (lamps/ballasts, mercury thermostats, batteries, e-waste) diverted; prohibited-materials list in construction documents |

---

### Key Definitions

| Term | Definition | Source |
|---|---|---|
| **Tenant Improvement (TI)** | Construction or alteration of the interior of an existing nonresidential building, generally for a new tenant or to reconfigure an existing tenant's space. Always an "alteration" under CEBC Part 10 (Level 1, 2, or 3 per Ch. 6). | CEBC Ch.6 (alteration definitions) |
| **Change of Occupancy** | A change in the purpose or level of activity within a building that involves a change of occupancy classification or a change in fire-protection-system threshold per CBC Ch.9. | CEBC 202, 1001.1 |
| **Work Area** | The portion of a building consisting of all reconfigured spaces, identified on construction documents per CEBC 601.2. The work-area percentage drives Level 2 vs Level 3 classification. | CEBC 202, 601.2 |
| **Alteration Level 1** | Removal/replacement/covering of existing materials with same-purpose materials (cosmetic/like-for-like). Governed by CEBC Ch.7. | CEBC 602 |
| **Alteration Level 2** | Addition/elimination of doors/windows, reconfiguration of systems, additional equipment; work area <=50% of building area. Governed by CEBC Ch.7 + Ch.8. | CEBC 603 |
| **Alteration Level 3** | Same scope as Level 2 but work area >50% of building. Governed by CEBC Ch.7, Ch.8, and Ch.9. | CEBC 604 |
| **Adjusted Construction Cost** | The total cost of alterations, structural repairs, or additions used to evaluate the 20% PoT disproportionality cap. Excludes the cost of PoT compliance itself. | CBC 11B-202.4 Exception 8 |
| **Valuation Threshold** | Annually-published dollar amount (set by DSA, escalated by the ENR 20-Cities CCI from a Jan-1981 $50,000 base) above which the 20%-cap moves to an unreasonable-hardship finding rather than a hard cap. Current figure: $209,208.00, effective 1/19/2026 (2025: $203,611.00). Verify the current-year DSA value before finalizing PoT scope. | CBC Chapter 2 (Definitions §202); annual DSA publication; CBC 11B-202.4 Exception 8 |
| **Primary Function Area** | An area where a major activity of the facility takes place (e.g., the dining area of a restaurant, retail sales floor, classrooms). Federal ADA hooks the 20% PoT obligation to primary-function-area alterations specifically. | 28 CFR 36.403(b); CBC 11B-202.4 Exception 10 (EVCS context) |
| **Risk Category** | I-IV building classification (ASCE 7) used to size structural loads. Bumping the risk category during a change of occupancy can trigger seismic re-evaluation per CEBC 1006.3. | CBC 1604.5; CEBC 1006.3 |

---

### Key Principles

1. **Every TI is an alteration under CEBC Part 10.** Before anything else, classify the alteration level (1/2/3) per CEBC Ch. 6 and decide whether the project is *also* a change of occupancy per Ch. 10. These two questions answer 80% of the review.

2. **CBC Chapter 34 is RESERVED in California.** California removed Ch. 34 of the IBC. All existing-building rules live in **Part 10 (CEBC)**. If you see a "CBC 3401" citation in submittal documents, ask the applicant to re-cite it to CEBC.

3. **Accessibility upgrades cascade outward.** Any alteration to a "primary function area" pulls in path-of-travel (entrance + restroom + drinking fountain + signs + telephones). The 20% cap is your safety valve — but the *path itself* must be brought up, in priority order, until the 20% is spent.

4. **Sprinkler retrofit can be triggered by occupancy alone.** When a change of occupancy crosses a new CBC Ch.9 threshold (e.g., M to A-2 where the existing M fire area was 8,000 sf and A-2 now requires sprinklers at 5,000 sf), CEBC 1011.2.1 retrofits the area of change plus all non-fire-wall-separated areas. This is the silent killer of M → A-2 conversions in older shells.

5. **Energy alterations have soft triggers.** Touching 10% of luminaires triggers the entire §141.0(b)2I lighting alteration package. Touching 25% of an envelope wall triggers air-leakage requirements. Reviewers must read drawings/specs for triggers — applicants frequently miss them.

6. **CALGreen §5.408 (waste diversion) applies to ALL permitted alterations.** Not just $200K+ projects. This is a frequent miss in small TI submittals.

7. **Restaurant work routes out.** The moment commercial cooking equipment, grease, or A-2 dining is in scope, hand the project to `california-restaurant-ti`. Do not attempt CRFC / Type-1 hood / grease interceptor review in this skill.

8. **Federal ADA is a parallel track.** A reviewer cannot grant relief from federal ADA Title III — only California-specific accessibility provisions. When the submittal claims "hardship," confirm both 11B-202.4 Exception 8 (California) AND 28 CFR 36.403 (federal) treatments.

9. **Progressive disclosure is mandatory.** Read this SKILL.md, then the submittal, then load ONLY the 3-6 reference files that the decision tree calls out. Never load all 7.

10. **State law is the floor — cities can add.** This skill never speaks for a particular city. The city overlay skill (e.g., a CrossBeam reference that is not included in this plugin) handles local amendments, fees, portal mechanics, and local energy reach codes.
