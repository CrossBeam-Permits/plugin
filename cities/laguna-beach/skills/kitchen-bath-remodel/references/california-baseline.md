# California Baseline — Kitchen/Bath Remodel

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Kitchen & Bathroom Remodel Permit Review

This skill covers **state-level** California requirements for residential kitchen and bathroom remodel permits. It addresses plumbing, electrical, mechanical ventilation, energy code, waterproofing, and safety requirements triggered by kitchen and bathroom renovations.

**What this covers:**
- Plumbing fixtures: water closets, lavatories, showers, bathtubs, kitchen sinks, faucets
- Water efficiency: CALGreen maximum flow rates for all fixtures
- Electrical: GFCI/AFCI protection, countertop outlet spacing, dedicated appliance circuits, tamper-resistant receptacles
- Ventilation: bathroom exhaust fans, kitchen range hoods, duct termination
- Energy code: lighting efficacy (JA8), water heater alterations, pipe insulation
- Waterproofing: shower pans, lining materials, tile substrate, testing
- Safety glazing near tubs and showers
- Smoke and carbon monoxide alarm upgrades
- Whirlpool/spa requirements
- Fixture clearances and accessibility

**What this does NOT cover:**
- New construction (full house builds)
- Commercial kitchen/restaurant hood systems (Type I hoods)
- Structural engineering for load-bearing wall removal (see structural engineer)
- Gas line sizing calculations (see mechanical engineer)
- Accessibility upgrades beyond basic fixture clearances (see CBC Chapter 11A/11B)
- City-specific overlay requirements (see city overlay skill)

---

### How to Use This Skill

1. Determine whether the project is a **kitchen remodel**, **bathroom remodel**, or **both**
2. Determine if the scope involves **layout reconfiguration** or **structural modifications** (triggers full review)
3. Walk through the Decision Tree Router below
4. For each checklist item, load the referenced file from `/` as needed
5. See `../SKILL.md` for the full reference file catalog

---

### Decision Tree Router

#### STEP 1 -- Determine Scope of Work

| Scope | What It Triggers |
|---|---|
| Fixture replacement in same location (no layout change) | Standard checklist below |
| Layout reconfiguration (moving fixtures, adding fixtures) | Standard checklist + plumbing sizing verification + sewer video for added fixtures |
| Structural modification (removing walls, enlarged openings) | Standard checklist + structural engineering review required |
| Cosmetic only (paint, mirrors, towel bars, floor covering -- no other work) | No permit required (maintenance item) |

#### STEP 2 -- What Type of Review Is This?

| Review Type | Load These References |
|---|---|
| **Full kitchen remodel review** | `electrical-kitchen-bath.md`, `ventilation-exhaust.md`, `plumbing-fixtures.md`, `energy-lighting.md` |
| **Full bathroom remodel review** | `electrical-kitchen-bath.md`, `ventilation-exhaust.md`, `plumbing-fixtures.md`, `waterproofing.md`, `energy-lighting.md` |
| **Combined kitchen + bath** | All five reference files |
| **Plumbing fixture question only** | `plumbing-fixtures.md` |
| **Electrical question only** | `electrical-kitchen-bath.md` |
| **Ventilation question only** | `ventilation-exhaust.md` |
| **Shower pan / waterproofing question** | `waterproofing.md` |
| **Lighting / energy question** | `energy-lighting.md` |

#### STEP 3 -- Review Checklist

Walk each item in order. For every check, record PASS / FAIL / FLAG / N/A with the code section cited.

##### ELECTRICAL

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 1 | **GFCI Protection** | Kitchen: all countertop outlets GFCI protected. Bathroom: 20A GFCI outlet within 36" of each sink basin. | CEC 210.8(A)(1), (6) | `electrical-kitchen-bath.md` |
| 2 | **AFCI Protection** | Kitchen: all countertop outlets AFCI protected. AFCI installed in readily accessible location. | CEC 210.12(A) | `electrical-kitchen-bath.md` |
| 3 | **Tamper-Resistant Receptacles** | All new receptacles shall be listed as tamper-resistant. | CEC 406.4(D)(5) | `electrical-kitchen-bath.md` |
| 4 | **Kitchen Countertop Outlets** | Countertops 12"+ wide require outlet. Outlets within 24" of any countertop location. Max 20" above countertop. Appliances/sinks break runs. Islands and peninsulas included. | CEC 210.52(C) | `electrical-kitchen-bath.md` |
| 5 | **Small Appliance Circuits** | Kitchen: two (2) 20A small appliance circuits required, balanced, no other outlets. | CEC 210.52(B)(1), (2) | `electrical-kitchen-bath.md` |
| 6 | **Dedicated Appliance Circuits** | Individual dedicated circuits for dishwasher, garbage disposal, built-in microwave, trash compactor. Exception: DW+disposal on single 20A if combined <10A. | CEC 210.11(C)(1); CEC 422.10(A) | `electrical-kitchen-bath.md` |
| 7 | **Appliance Cord Length** | Garbage disposal cord: 18-36". Dishwasher cord: 18-36" (Romex with plug not approved). | CEC 422.16(B)(1), (2) | `electrical-kitchen-bath.md` |
| 8 | **Bathroom Branch Circuit** | Min (1) 20A circuit for bathroom receptacles, no other outlets. May serve multiple bathrooms. | CEC 210.11(C)(3) | `electrical-kitchen-bath.md` |
| 9 | **Electrical Exclusion Zone** | No cord-connected/hanging fixtures within 3' horizontal / 8' vertical of tub/shower edge. Luminaires in tub/shower area: damp-rated, solid lens, GFCI protected. | CEC 410.10 | `electrical-kitchen-bath.md` |
| 10 | **Lighting Efficacy** | Kitchen and bathroom luminaires shall be high efficacy (JA8 compliant, 45 lm/W) or controlled by vacancy sensor (manual on, auto off). Recessed cans: IC and AT rated in insulated ceilings. | Energy Code 150.0(k); 150.2(b)1K | `energy-lighting.md` |

##### MECHANICAL / VENTILATION

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 11 | **Bathroom Exhaust Fan** | Required regardless of window. Min 50 CFM intermittent / 20 CFM continuous. Max 3 Sone. Back draft damper. Ducted to outdoors (no recirculating). ENERGY STAR compliant. Humidistat control required unless part of whole-house ventilation. | CMC 405.1, 504.3; ASHRAE 62.2; CALGreen 4.506 | `ventilation-exhaust.md` |
| 12 | **Kitchen Range Hood** | Ducted residential exhaust hood required. Min 100 CFM. Max 3 Sone. Metal smooth-interior duct (no flex). Back draft damper. Recirculating hoods not allowed. | CMC 504.3; ASHRAE 62.2; Energy Code 150.0(o)1G | `ventilation-exhaust.md` |
| 13 | **Exhaust Duct Termination** | Min 3' from property lines and any building openings (windows, doors, skylights, attic vents). | CMC 502.2.1 | `ventilation-exhaust.md` |
| 14 | **Cook Top Clearance** | Household floor-mounted or built-in cooking top has 30" vertical clearance to combustible material or metal cabinets, unless a permitted 24" protection/hood configuration or listed-appliance installation path applies. | CMC 919.4.2, 919.5.2 | `ventilation-exhaust.md` |

##### PLUMBING

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 15 | **Fixture Flow Rates** | Water closets: 1.28 gpf max (WaterSense). Lavatory faucets: 1.2 gpm. Kitchen faucets: 1.8 gpm (2.2 temp max). Showerheads: 1.8 gpm (WaterSense). Multi-showerhead: 1.8 gpm combined or single-outlet operation. | CPC 407-420; CALGreen 4.303.1 | `plumbing-fixtures.md` |
| 16 | **Anti-Scald Valves** | Showers and tub-shower combos: pressure balance/thermostatic valves required. Max 120F from showerhead and bathtub filler. ASSE 1016 compliant. | CPC 408.4, 409.4 | `plumbing-fixtures.md` |
| 17 | **Fixture Clearances** | Water closets: 15" center to wall, 30" center-to-center, 24" clear in front. Verify adequate clearance for all fixtures. | CPC 402.5 | `plumbing-fixtures.md` |
| 18 | **Waste/Drain Sizing** | Lavatory tailpiece: 1-1/4" min. Shower drain: 2" min. Kitchen/bathtub: 1-1/2" min. Max 3 WCs on 3" waste; 4th requires 4" line. | CPC 407.5, 408.5, 409.2, 420.4 | `plumbing-fixtures.md` |
| 19 | **Hot Water Valve Position** | Left-hand control shall control hot water when facing fixture. | CPC 417.5 | `plumbing-fixtures.md` |
| 20 | **Access Panels** | Min 12" x 12" access panel for concealed slip joint connections. Exception: weld-on waste/overflow eliminates requirement. | CPC 402.10 | `plumbing-fixtures.md` |
| 21 | **Dishwasher Air Gap** | Listed air gap required for dishwasher drain. | CPC 807.3 | `plumbing-fixtures.md` |
| 22 | **Gas Piping** | Gas test: 10 PSI for 15 min (max 15 PSI gauge). Shutoff valve and sediment trap before each appliance. Gas lines under slab: approved vented gas-tight conduit. Max 6' gas flex connector for freestanding range. All gas piping sized per CPC 1215. | CPC 1210-1215 | `plumbing-fixtures.md` |

##### WATERPROOFING (Bathroom Only)

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 23 | **Shower Pan Construction** | Site-built: watertight, dense, nonabsorbent materials. Dam/curb: 2" min to 9" max depth, 1" lower than sides. Floor slope: 1/8" to 1/2" per foot to drain. Receptor min 1024 sq in, encompass 30" circle. | CPC 408.6, 408.7, 408.8 | `waterproofing.md` |
| 24 | **Shower Lining** | Subfloor and walls lined min 3" above dam/threshold. Approved materials: PVC (ASTM D4551), CPE (ASTM D4068), sheet lead, sheet copper, or 3-layer 15 lb felt. Pitched 1/4" per foot to weep holes. No nailing below 1" above dam. | CPC 408.8 | `waterproofing.md` |
| 25 | **Shower Pan Test** | Fill to 2" depth for minimum 15 minutes. Both sides of subpan tested at drain clamp. | CPC 408.8.5 | `waterproofing.md` |
| 26 | **Tile Substrate** | Green board drywall prohibited in shower enclosures. Cement board (Durock, Hardiebacker, or equivalent) required over water barrier with approved fasteners. | Industry standard; CPC 408.8 | `waterproofing.md` |
| 27 | **Wall Finish Height** | Tub/shower walls with showerhead: smooth, non-absorbent surface to 72" above standing surface. | Industry standard | `waterproofing.md` |
| 28 | **Safety Glazing** | Required for glazing <60" above standing surface AND within 60" horizontal of tub/shower water's edge. | CRC 308.4.5 | `waterproofing.md` |

##### WHIRLPOOL / SPA (If Applicable)

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 29 | **Whirlpool Access & Installation** | Accessible access panel. Pump above crown weir of trap. Self-draining piping. Suction fittings per ASME A112.19.7. | CPC 409.6 | `plumbing-fixtures.md` |
| 30 | **Whirlpool Electrical** | Accessible disconnects and GFCI protection for pump, aerator, heater. Max 120F water temp via ASSE 1070 device. | CEC 210.8; CPC 409.4 | `electrical-kitchen-bath.md` |

##### ENERGY CODE

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 31 | **Water Heater (if altered)** | Replacement must be: gas/propane, heat pump (with R-10 base, comm interface), NEEA Tier 3+, or consumer electric (if existing is electric resistance). Pipe insulation on new/accessible piping. Demand recirc only. | Energy Code 150.2(b)1H | `energy-lighting.md` |

##### SAFETY

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 32 | **Smoke & CO Alarms** | Projects over $1,000: all dwelling alarms must meet current code. Smoke alarms in bedrooms, outside sleeping areas, each story. CO alarms where fuel-burning appliances or attached garage. Interconnected when multiple required. Battery OK if no wall/ceiling removal and no attic/crawl access. | CRC R314, R315 | `electrical-kitchen-bath.md` |
| 33 | **Contractor Licensing** | C-36 (Plumbing), C-10 (Electrical), C-20 (HVAC), or B (General Building) as applicable. Workers' compensation required. | B&P Code 7028 | N/A |

#### STEP 4 -- Output Format

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
- **N/A** -- Does not apply to this project (e.g., shower pan checks when scope is kitchen-only)

---

### Quick-Reference Tables

#### Maximum Fixture Flow Rates (CALGreen / CPC)

| Fixture | Maximum Flow Rate | Certification | Code Section |
|---|---|---|---|
| Water closet (toilet) | 1.28 gpf | WaterSense | CPC 411.2; CALGreen 4.303.1.1 |
| Residential lavatory faucet | 1.2 gpm @ 60 psi | -- | CPC 407.2.2; CALGreen 4.303.1.4.1 |
| Kitchen faucet | 1.8 gpm @ 60 psi (2.2 temp boost) | -- | CPC 420.2.2; CALGreen 4.303.1.4.4 |
| Showerhead (single) | 1.8 gpm @ 80 psi | WaterSense | CPC 408.3; CALGreen 4.303.1.3.1 |
| Multiple showerheads (combined) | 1.8 gpm @ 80 psi total | -- | CPC 408.3.2; CALGreen 4.303.1.3.2 |

#### Fixture Clearances

| Fixture | Min. to Side Wall | Min. Center-to-Center | Min. Clear in Front |
|---|---|---|---|
| Water closet | 15" from center | 30" | 24" |
| Bidet | 15" from center | 30" | 24" |
| Lavatory | -- | -- | 24" |

#### Kitchen Electrical Quick-Reference

| Requirement | Value | Code Section |
|---|---|---|
| Small appliance circuits | 2 x 20A (balanced) | CEC 210.52(B) |
| Countertop outlet spacing | Within 24" of any point | CEC 210.52(C)(1) |
| Min countertop width for outlet | 12" | CEC 210.52(C) |
| Max height above countertop | 20" | CEC 210.52(C)(3) |
| Disposal cord length | 18-36" | CEC 422.16(B)(1) |
| Dishwasher cord length | 18-36" | CEC 422.16(B)(2) |
| DW + disposal shared circuit | Single 20A if combined <10A | CEC 210.23 |

#### Bathroom Electrical Quick-Reference

| Requirement | Value | Code Section |
|---|---|---|
| GFCI outlet distance from sink | Within 36" | CEC 210.8(A)(1) |
| Bathroom branch circuit | Min 1 x 20A, no other outlets | CEC 210.11(C)(3) |
| Exclusion zone horizontal | 3' from tub/shower edge | CEC 410.10 |
| Exclusion zone vertical | 8' above tub rim/shower threshold | CEC 410.10 |

#### Ventilation Rates

| Space | Intermittent | Continuous | Max Sound | Code |
|---|---|---|---|---|
| Bathroom | 50 CFM | 20 CFM | 3 Sone | ASHRAE 62.2 |
| Kitchen (range hood) | 100 CFM | -- | 3 Sone | ASHRAE 62.2 |

#### Shower Pan Dimensions

| Requirement | Value | Code Section |
|---|---|---|
| Min shower area | 1024 sq in | CPC 408.7 |
| Min circle diameter | 30" | CPC 408.7 |
| Min dam height | 2" | CPC 408.6 |
| Max dam height | 9" | CPC 408.6 |
| Min door opening | 22" | CPC 408.6 |
| Floor slope to drain | 1/8" to 1/2" per foot | CPC 408.6 |
| Wall finish height | 72" above standing surface | -- |

#### Maximum Water Temperature by Fixture

| Fixture | Max Temp | Limiting Device | Code Section |
|---|---|---|---|
| Showerhead | 120F | ASSE 1016 valve | CPC 408.4.2 |
| Bathtub filler | 120F | ASSE 1070 or ASSE 1084 | CPC 409.4 |
| Bidet | 110F | ASSE 1070 or CSA B125.3 | CPC 410.2 |
| Public lavatory | 120F | ASSE 1070 or ASSE 1084 | CPC 407.3 |

---

### Key Principles

1. **Kitchen and bath remodels trigger current code compliance.** Even a simple fixture swap requires the entire system (electrical, plumbing, mechanical, energy) to meet the current edition of all applicable California codes.
2. **GFCI is mandatory everywhere water meets electricity.** Kitchen countertop outlets, bathroom outlets near sinks, and any receptacle within the tub/shower exclusion zone must be GFCI protected. Kitchen outlets also require AFCI.
3. **Low-flow is the law.** California mandates WaterSense-certified toilets (1.28 gpf), low-flow showerheads (1.8 gpm), low-flow lavatory faucets (1.2 gpm), and low-flow kitchen faucets (1.8 gpm). No exceptions for residential remodels.
4. **Ducted exhaust is required, not optional.** Recirculating range hoods and recirculating bathroom fans do not satisfy code. Both kitchen and bathroom must have ducted exhaust venting to the outdoors with back draft dampers.
5. **Shower waterproofing is a critical inspection.** Site-built shower pans must be tested (2" water for 15 min). Lining must extend 3" above the dam. Green board drywall is prohibited in showers -- cement board over a water barrier is required.
6. **Lighting efficacy is enforced on alteration.** All altered luminaires must be JA8 compliant (45 lm/W) or controlled by a vacancy sensor. Recessed cans in insulated ceilings must be IC and AT rated.
7. **Smoke and CO alarms are verified at final.** Any remodel over $1,000 triggers whole-dwelling alarm compliance -- working alarms in all bedrooms, outside sleeping areas, and on each floor level.
8. **Layout changes escalate the review.** Moving fixtures, adding fixtures, or removing walls triggers additional requirements: structural review for wall removal, sewer video for added fixtures, and full plumbing sizing verification.
