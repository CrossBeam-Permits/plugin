# California Baseline — Multi-Unit Residential

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Multi-Unit Residential Code Decision Engine

This skill contains the California state-level code requirements for multi-unit residential construction (townhomes, condominiums, apartments) extracted from the 2025 Title 24 corpus. It covers the California Building Code (CBC), California Residential Code (CRC), California Electrical Code (CEC), California Mechanical Code (CMC), California Plumbing Code (CPC), California Energy Code, California Fire Code (CFC), and California Green Building Standards Code (CALGreen).

**What this covers**: State building code — the requirements that apply to every multi-unit residential project in California regardless of city.

**What this does NOT cover**: City/county-specific ordinances, local zoning standards (setbacks, parking ratios, design guidelines), federal requirements (FHA, ADA beyond CBC 11A/11B), or project-specific engineering calculations.

### ⚠️ Density Feasibility Discipline (read before answering any unit-count question)

When a user asks whether N units "fit" on a parcel, **never conclude infeasibility from General Plan / zoning du-per-acre arithmetic alone.** That arithmetic is the *starting* number, not the answer — California's housing-law stack routinely carries projects far past it, and cities process real entitlement applications on exactly that basis. Before answering any density/unit-count feasibility question, load `density-zoning.md` and reason through, in order:

1. **The operative standard may not be the GP range.** Specific-plan districts (downtown SPs, precise plans) carry their own density/height/FAR standards that control over the General Plan designation shown in GIS. A "30–50 du/ac" GP designation over a specific-plan parcel is context, not a cap.
2. **Density Bonus Law (Gov. Code §65915)** — a *mandatory* state entitlement, not a local program: sliding-scale bonus up to 50% (the AB 1287 stacked second bonus can approach ~100%; 100%-affordable projects get 80% and, in qualifying transit/low-VMT areas, **no density limit at all**), 1–5 concessions, and an **unlimited number of waivers** of any development standard (height, setbacks, parking geometry) that would physically preclude the bonus project. The city must grant these absent narrow §65915(d)/(e) written findings. Even a small set-aside (e.g., 2 affordable units in a ~26-unit base) opens the waiver door.
3. **Housing Accountability Act (Gov. Code §65589.5(j))** — for a compliant housing project, the city may deny or reduce density **only** on written findings, by a preponderance of the evidence, of a specific adverse health/safety impact with no feasible mitigation. "Too dense for the neighborhood" is not a lawful basis.
4. **SB 330 preliminary applications** (Gov. Code §65941.1) freeze the applicable standards and fees at filing and cap public hearings at five.
5. **Ministerial paths**: SB 423/35 streamlining, AB 2011 commercial corridors — see `density-zoning.md` and `permit-process.md`.

**Frame the answer as a path, not a verdict**: "here is the affordability mix / waiver package / entitlement route that supports N units, and here is what the city can and cannot lawfully require" — then flag what needs confirmation with planning. Telling the user to "right-size" the unit count without walking this stack first is a wrong answer.

### How to Use This Skill

When answering a multi-unit residential question, follow the 4-step decision tree below. Each step tells you which reference files to load. Load only what you need — most questions require 4-8 reference files, not all 26.

After loading references, check the **Quick-Reference Thresholds** table below for the key numbers that come up in almost every review.

---

### Decision Tree Router

#### STEP 1: Classify the Project

What type of multi-unit residential project is this?

| Project Type | Load These References | Code Regime |
|-------------|----------------------|-------------|
| **Townhomes** (≤3 stories, separate exterior exit per unit) | `occupancy-classification.md`, `construction-types.md` | CRC (R-3) |
| **Apartments / Condos** (common corridors, shared exits) | `occupancy-classification.md`, `construction-types.md` | CBC (R-2) |
| **Mixed-use** (residential over commercial/retail) | `occupancy-classification.md`, `construction-types.md` | CBC (R-2 + other) |
| **Unsure / classification question** | `occupancy-classification.md` (start here — has the R-2 vs R-3 boundary) | — |

#### STEP 2: Classify the Construction Type

What is the construction type and how many stories?

| Construction Type | Load These References |
|-------------------|----------------------|
| **Type V-A** (wood frame, 1-hr rated) — most common | `construction-types.md`, `fire-resistance-ratings.md` |
| **Type V-B** (wood frame, unrated) | `construction-types.md`, `fire-resistance-ratings.md` |
| **Type III-A/B** (noncombustible exterior, combustible interior) | `construction-types.md`, `fire-resistance-ratings.md` |
| **Height/area feasibility question** | `construction-types.md` (has Tables 504.3, 504.4, 506.2) |

#### STEP 3: Route to Critical Code Areas

What discipline is the question about? Load the relevant reference files.

| Discipline | Load These References |
|-----------|----------------------|
| **Fire separation / party walls** | `fire-separation.md`, `fire-resistance-ratings.md` |
| **Sprinkler system** | `fire-sprinkler.md` |
| **Fire access / hydrants** | `fire-access.md` |
| **Egress — occupant load** | `egress-occupant-load.md` |
| **Egress — exits and travel distance** | `egress-exits.md` |
| **Egress — corridors** | `egress-corridors.md` |
| **Egress — stairs** | `egress-stairs.md` |
| **Accessibility — dwelling units** | `accessibility-units.md` |
| **Accessibility — common areas / parking** | `accessibility-common.md` |
| **Structural — seismic / lateral** | `structural-lateral.md` |
| **Structural — party walls** | `structural-party-walls.md` |
| **Structural — foundations** | `structural-foundation.md` |
| **Mechanical / HVAC** | `mechanical-hvac.md` |
| **Plumbing** | `plumbing-fixtures.md` |
| **Electrical — service sizing** | `electrical-service.md` |
| **Electrical — EV charging** | `electrical-ev-charging.md` |
| **Energy — envelope** | `energy-envelope.md` |
| **Energy — HVAC efficiency** | `energy-hvac-efficiency.md` |
| **Energy — lighting** | `energy-lighting.md` |
| **Green building / CALGreen** | `calgreen-mandatory.md` |
| **Parking** | `parking-requirements.md` |
| **Density / zoning bonuses** | `density-zoning.md` |
| **Permit process / streamlining** | `permit-process.md` |

#### STEP 4: Check Situational Modifiers

Does any of the following apply? Load additional references.

| Situation | Load These References |
|-----------|----------------------|
| **Affordable housing component** | `density-zoning.md` (density bonus, concessions), `permit-process.md` (SB 423 streamlining) |
| **Near major transit stop** (½ mile) | `parking-requirements.md` (AB 2097 — no parking minimums), `density-zoning.md` |
| **4+ stories** | `fire-sprinkler.md` (NFPA 13 vs 13R), `egress-stairs.md` (2-hr enclosure), `construction-types.md` |
| **Mixed-use (ground-floor commercial)** | `occupancy-classification.md` (508 mixed occupancy), `fire-separation.md` |
| **Seismic Design Category E** | `structural-lateral.md`, `structural-foundation.md` |
| **Fire hazard severity zone** | `fire-access.md`, `fire-sprinkler.md` |
| **Density bonus application** | `density-zoning.md` (Gov. Code 65915) |
| **SB 423 / SB 35 streamlined project** | `permit-process.md`, `density-zoning.md` |

---

### Quick-Reference Thresholds

These numbers come up in almost every multi-unit residential review. Check here first before loading a reference file.

| Threshold | Value | Reference File |
|-----------|-------|----------------|
| **R-2 vs R-3 boundary** | >2 dwelling units with common exits = R-2 | `occupancy-classification.md` |
| **CRC scope** | Townhouses ≤3 stories with separate means of egress | `occupancy-classification.md` |
| **Type V-A max stories (R-2, S13R)** | 4 stories, 50 ft | `construction-types.md` |
| **Type V-A max stories (R-2, NFPA 13)** | 4 stories, 60-70 ft | `construction-types.md` |
| **Type V-A max area (R-2, NS)** | 12,000 sf per story | `construction-types.md` |
| **Fire wall rating (R-3)** | 2 hours (Table 706.4) | `fire-separation.md` |
| **Fire wall rating (R-2, Type V)** | 2 hours (706.4 exception) | `fire-separation.md` |
| **Townhouse common wall (sprinklered)** | 1 hour (CRC R302.2.2) | `fire-separation.md` |
| **Townhouse common wall (unsprinklered)** | 2 hours (CRC R302.2.2) | `fire-separation.md` |
| **Dwelling unit fire partition** | 1 hour (CBC 708.3) | `fire-separation.md` |
| **Sound transmission — walls** | STC 50 (CBC 1206.2) | `fire-separation.md` |
| **Sound transmission — floors** | IIC 50 (CBC 1206.3) | `fire-separation.md` |
| **Interior noise** | 45 dB max (CBC 1206.4) | `fire-separation.md` |
| **Sprinklers required** | All new Group R (CBC 903.2.8) | `fire-sprinkler.md` |
| **NFPA 13D allowed** | R-3 townhouses only | `fire-sprinkler.md` |
| **NFPA 13R max height** | 4 stories, roof <45 ft above fire access | `fire-sprinkler.md` |
| **Fire apparatus access width** | 20 ft min; 26 ft with hydrant | `fire-access.md` |
| **Fire access reach** | 150 ft from all building portions | `fire-access.md` |
| **Exit travel distance (R, sprinklered)** | 250 ft (CBC 1017.2) | `egress-exits.md` |
| **Corridor width** | 44 in (CBC Table 1020.3); 36 in if OL <50 | `egress-corridors.md` |
| **Dead-end corridor (R, sprinklered)** | 50 ft (CBC 1020.5 Exception 2); 20 ft base | `egress-corridors.md` |
| **Stair width** | 44 in (OL >50); 36 in otherwise | `egress-stairs.md` |
| **Stair rise/run (CBC)** | 7 in max / 11 in min | `egress-stairs.md` |
| **Stair enclosure** | 1-hr (≤3 stories); 2-hr (4+) | `egress-stairs.md` |
| **Parapet height** | 30 in above roof (with exceptions) | `fire-separation.md` |
| **Envelope — wall U-factor (2x6)** | 0.069 max | `energy-envelope.md` |
| **Envelope — fenestration U-factor** | 0.58 max | `energy-envelope.md` |
| **Compartmentalization** | ≤0.3 cfm/sf at 50 Pa | `energy-hvac-efficiency.md` |
| **EV charging** | 1 Level 2 receptacle per unit (assigned) | `electrical-ev-charging.md` |
| **Water fixtures** | Toilets ≤1.28 GPF, showers ≤1.8 GPM | `calgreen-mandatory.md` |
| **Construction waste diversion** | 65% minimum | `calgreen-mandatory.md` |
| **AB 2097 parking** | No minimums within ½ mile of transit | `parking-requirements.md` |

---

### Key Principles

1. **Dual code regime**: Townhomes with separate exterior exits use the CRC; apartments with common corridors use the CBC. The classification drives everything that follows.

2. **Sprinklers are mandatory**: All new Group R buildings require automatic sprinkler systems (CBC 903.2.8). The sprinkler type (13D/13R/13) affects party wall ratings, height/area, and egress.

3. **Fire walls create separate buildings**: Each portion separated by a fire wall per CBC 706 is a separate building for height, area, and construction type (CBC 503.1). This is how large townhome developments achieve compliance.

4. **Party walls serve dual function**: Fire separation AND structural element AND acoustic barrier. A single wall assembly must satisfy fire rating, structural independence, and STC 50.

5. **Accessibility depends on elevator**: Non-elevator buildings require only ground-floor accessible units. Elevator buildings trigger full Chapter 11A coverage for all served floors.

6. **State housing laws override local restrictions**: Density Bonus Law, SB 423 streamlining, Housing Accountability Act, and AB 2097 parking elimination constrain what cities can deny or require.
