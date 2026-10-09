# California Baseline — Residential Addition

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Residential Addition Permit Review

This skill covers **state-level** California requirements for residential additions and major remodels. It applies to single-family dwellings, duplexes, and townhouses not exceeding three stories (CRC scope). For larger or mixed-use projects, defer to the CBC (Part 2).

**What this covers:**
- Room additions (bedrooms, bathrooms, family rooms, kitchens)
- Second-story additions over existing first-floor structures
- Major remodels that expand conditioned floor area
- Foundation (new footings, connection to existing)
- Framing (walls, floors, roof — span tables, lumber grades)
- Lateral bracing (shear walls, hold-downs, braced wall panels)
- Connection to existing structure
- HVAC system sizing for addition (Manual J/S/D)
- Duct design and insulation
- Energy code compliance (Part 6: envelope, HVAC, lighting, solar-ready)
- Insulation (walls, ceiling, floor)
- Electrical: new circuits, panel capacity, AFCI/GFCI, smoke/CO alarms
- Plumbing: fixture counts, water supply, DWV (when bath/kitchen in addition)
- Egress (bedroom windows, exits)
- Fire separation (garage-to-house, property line)
- Accessibility (when triggered by additions)
- CALGreen requirements
- Soils/foundation report requirements

**What this does NOT cover:**
- ADU construction (see california-adu skill)
- Solar PV installation (see california-solar skill)
- Reroof-only projects (see california-reroof skill)
- Commercial tenant improvements
- New ground-up single-family construction (shares many requirements but different scope/process)
- Historical/landmark building exemptions
- Seismic retrofit of existing structure (unless triggered by addition)

---

### How to Use This Skill

1. Determine whether the project is a **simple addition** (single trade, small scope) or a **complex multi-trade addition**
2. Walk through the Decision Tree Router below
3. For each checklist section, load the referenced file from `/` as needed
4. See `../SKILL.md` for the full reference file catalog

---

### Decision Tree Router

#### STEP 0 — Wildfire / WUI Pre-Check

For Laguna Beach the wildfire overlay is set citywide: use the `wildfire: 'all'` row below, and the `wildfire-wui` skill in this plugin for the Chapter 7A / WUI Code details.

| Overlay status                  | What to do                                                                                                                                                                                                                |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Not loaded (no FHSZ in city)    | Skip WUI / Chapter 7A — the standard addition checks below are complete on their own.                                                                                                                                     |
| Loaded — `wildfire: 'partial'`  | City has some FHSZ parcels but not the whole jurisdiction. Surface Chapter 7A findings **conditionally** with a disclaimer pointing applicants to the CalFire FHSZ viewer (osfm.fire.ca.gov). Do not fail on WUI grounds without parcel confirmation. |
| Loaded — `wildfire: 'all'`      | Entire or substantial majority of the city is FHSZ. Apply Chapter 7A findings, prefaced with a brief "assumed FHSZ based on city coverage; confirm via osfm.fire.ca.gov — if outside, the WUI findings below do not apply" disclaimer. |

When the overlay is loaded, follow `../../wildfire-wui/SKILL.md` Steps 1–3 for component checks (roof assemblies at new and replaced roof areas, eaves/vents on the addition envelope, walls/windows/doors/decks on the new exterior, defensible space if the addition footprint changes) and fold those findings into the addition review output. Note that additions to existing dwellings in a FHSZ generally apply Chapter 7A to the new construction only (existing portions are not retroactively triggered unless materially altered).

#### STEP 1 — Determine Code Path

| Building Type | Code | Key Chapters |
|---|---|---|
| Single-family dwelling, duplex, townhouse <=3 stories | CRC (Part 2.5) | Ch. 3 (Planning), Ch. 4 (Foundations), Ch. 5 (Floors), Ch. 6 (Walls), Ch. 8 (Roof), Ch. 6 (Wall Bracing) |
| Additions >3 stories or mixed-use | CBC (Part 2) | Defer to engineering — outside prescriptive CRC scope |

**California amendment R301.1.3.1:** When any portion of the structure deviates from conventional framing, a California licensed architect or engineer must stamp those documents.

**California amendment R301.1.3.2:** All wood-frame dwellings more than two stories and basement require architect/engineer stamped plans.

#### STEP 2 — What Type of Review Is This?

| Review Type | Load These References |
|---|---|
| **Full permit review** (all trades) | All reference files as triggered by checklist |
| **Structural only** (foundation + framing) | `structural-framing.md`, `foundation-requirements.md`, `lateral-bracing.md` |
| **Energy compliance question** | `energy-envelope.md`, `hvac-sizing.md` |
| **Electrical question** | `electrical-additions.md` |
| **Fire separation / egress question** | `fire-separation.md`, `egress-requirements.md` |
| **Foundation / soils question** | `foundation-requirements.md` |

#### STEP 3 — Determine Addition Size Threshold

The Energy Code (Part 6) has different requirements based on addition size. Determine which tier applies:

| Addition Size | Energy Code Tier | Key Differences |
|---|---|---|
| **<=300 SF** | Minimal | Exempt from roofing requirements of Section 150.1(c)11 |
| **<=400 SF** | Small | Max fenestration: greater of 75 SF or 30% of addition CFA |
| **<=700 SF** | Medium | Reduced prescriptive requirements; QII not required; simplified insulation |
| **>700 SF** | Full | Full prescriptive requirements of Section 150.1(c) with modifications for additions |
| **<=1,000 SF** | — | Exempt from whole-dwelling mechanical ventilation; exempt from ventilation cooling (WHF) |
| **>1,000 SF** | — | Full whole-dwelling mechanical ventilation based on entire dwelling CFA |

PV systems (Section 150.1(c)14) are **NOT required for additions** per Exception 6 to Section 150.2(a).

#### STEP 4 — Review Checklist

Walk each section in order. For every check, record PASS / FAIL / FLAG / N/A with the code section cited.

---

### SECTION A: STRUCTURAL

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| A1 | **Soils / Geotechnical** | Verify whether a soils report is required. Required where expansive, compressible, or shifting soils are likely present. Building official may waive if soil conditions are known. Presumptive bearing values: crystalline bedrock 12,000 psf, sand/gravel 3,000 psf, clay/silt 1,500 psf (Table R401.4.1(1)). | CRC R401.4, R401.4.1 | `foundation-requirements.md` |
| A2 | **Foundation Design** | New footings: min 12" wide x 18" deep for one-story, 15" wide x 24" deep for two-story (or per local frost/soil). Concrete min 2,500 psi (Table R402.2). Rebar: min one #4 bar continuous within 12" of top. Foundation bolts: 1/2" dia., 7" embedment, max 6 ft OC, within 12" of each end. | CRC R403.1, R403.1.6, Table R403.1(1) | `foundation-requirements.md` |
| A3 | **Connection to Existing Foundation** | New foundation must tie into existing. Verify dowel spacing, epoxy specification, and match of footing depth. Stepped footings: max 2:1 horizontal-to-vertical ratio. | CRC R403.1.5 | `foundation-requirements.md` |
| A4 | **Floor Framing** | Verify joist species, grade, size, and span per Tables R502.3.1(1) and R502.3.1(2). Live load: 40 psf habitable, 30 psf sleeping. Dead load: 10 or 20 psf. Bearing on supports: min 1.5" on wood/metal, 3" on masonry. | CRC R502.3, R502.6 | `structural-framing.md` |
| A5 | **Wall Framing** | Studs: min No. 3 / Standard / Stud grade. 2x4 at 16" OC for single-story, 2x6 at 16" OC for two-story or if insulation requires it. Max stud height per Table R602.3(5). Headers per Tables R602.7(1) and R602.7(2). Double top plates with min 24" lap splice. | CRC R602.2, R602.3, R602.7 | `structural-framing.md` |
| A6 | **Roof Framing** | Rafter spans per Tables R802.5.1(1)-(8). Ridge board: min 1" nominal, depth >= cut end of rafter. Collar ties: upper 1/3 of attic, max 4 ft OC. Ceiling joist-rafter connections per Table R802.5.2(1). Uplift connections per R802.11. | CRC R802.3, R802.5, R802.11 | `structural-framing.md` |
| A7 | **Lateral Bracing** | Braced wall panels required per R602.10. Methods: WSP (wood structural panels), LIB (let-in bracing), PBS (portal frame), etc. Min bracing amounts per Table R602.10.3(1). Continuous sheathing may substitute for individual panels. Hold-down connectors at braced wall panel ends in SDC D. | CRC R602.10, R602.10.3, R602.10.6 | `lateral-bracing.md` |
| A8 | **Connection to Existing Structure** | Verify tie-in method for new framing to existing. New top plates must lap or be spliced to existing. Roof framing connections: valley, hip, or ridge intersections. Floor diaphragm continuity between new and existing. | CRC R602.3 | `structural-framing.md` |
| A9 | **Engineered Design Required?** | If any element exceeds prescriptive limits (spans, openings, non-conventional framing), engineered design by CA licensed architect/engineer is required. Any wood-frame >2 stories + basement requires stamped plans. | CRC R301.1.3, R301.1.3.1, R301.1.3.2 | `structural-framing.md` |

---

### SECTION B: ENERGY CODE (Part 6)

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| B1 | **Wall Insulation** | Additions >700 SF: framed walls max U-0.048 (most CZs) or U-0.065 (CZ 6-7). Additions <=700 SF or extensions of existing walls: cavity insulation R-15 in 2x4, R-21 in 2x6. When existing siding not removed, continuous insulation not required. | Energy Code 150.2(a)1A, 150.2(a)1B, Table 150.1-A | `energy-envelope.md` |
| B2 | **Ceiling/Roof Insulation** | Additions >700 SF: per Table 150.1-A (R-38 typical for vented attic in CZ 1-2, 4, 8-16; R-30 in CZ 3, 5-7). Additions <=700 SF: U-0.025 (or R-38) in CZ 1-2, 4, 8-16; U-0.031 (or R-30) in CZ 3, 5-7. Radiant barrier in CZ 2-15 for additions <=700 SF. | Energy Code 150.2(a)1A, 150.2(a)1B | `energy-envelope.md` |
| B3 | **Floor Insulation** | Raised floors: R-19 (U-0.037) in all climate zones per Table 150.1-A. Slab perimeter: NR except CZ 16 (R-7). | Energy Code Table 150.1-A | `energy-envelope.md` |
| B4 | **Fenestration** | Max U-factor per Table 150.1-A (0.27-0.30 depending on CZ). Max SHGC 0.23 in CZ 2, 4, 6-14; max SHGC 0.20 in CZ 15 (2025 CEC, orientation-neutral). Max total fenestration area: >700 SF additions = greater of 175 SF or 20% CFA; <=700 SF but >400 SF = greater of 120 SF or 25% CFA; <=400 SF = greater of 75 SF or 30% CFA. Max west-facing: per table or 60-70 SF limits. | Energy Code 150.2(a)1A, 150.2(a)1B, Table 150.1-A | `energy-envelope.md` |
| B5 | **HVAC System Sizing** | If new system: Manual J load calc required per Section 150.0(h). Max capacity limits per Tables 150.2-A/B. If extending existing: existing equipment need not comply with Part 6 (Exception 3) but must have adequate capacity per CRC R303.10. If >1,000 SF addition with new system: whole-dwelling ventilation required. | Energy Code 150.2(a)1E, 150.0(h) | `hvac-sizing.md` |
| B6 | **Duct Design & Insulation** | New ducts in unconditioned space: R-6 (CZ 3, 5-7) or R-8 (CZ 1-2, 4, 8-16) per Table 150.2-D. Entirely new duct system: max 5% leakage. Extension of existing: max 10% leakage (or 7% to outside). Field verification required. Per Title 24 Section 150.1(c)13, if the total new or replacement duct surface area exceeds 40 SF, HERS-verified duct leakage testing is required. New duct: <=5% leakage. Extended existing duct: <=10% leakage. | Energy Code 150.1(c)13, 150.2(a)1, 150.2(b)1D | `hvac-sizing.md` |
| B7 | **Mechanical Ventilation** | Additions <=1,000 SF: exempt from whole-dwelling ventilation airflow requirements. Additions >1,000 SF: whole-dwelling ventilation based on entire dwelling CFA. Local exhaust (kitchen/bath) always required per Section 150.0(o). | Energy Code 150.2(a)1C | `hvac-sizing.md` |
| B8 | **Water Heater** | If additional water heater installed: must be heat pump water heater (HPWH) with communication interface, or NEEA Tier 3+ HPWH, or electric point-of-use for additions <=500 SF. No gas water heaters for new installations. **Exception:** Replacement of an existing gas water heater with a like-kind gas appliance in the existing (unaltered) portion of the dwelling is governed by state plumbing code efficiency standards, not this prohibition — this prohibition applies to new water heater installations in addition footprints or new buildings. | Energy Code 150.2(a)1D | `energy-envelope.md` |
| B9 | **Space Heating Type** | Heat pump required for new construction. No electric resistance as primary heat source. Additions extending existing system: existing equipment exempt. New/replacement systems: heat pump per Table 150.1-A. | Energy Code 150.1(c)6, 150.2(b)1G | `hvac-sizing.md` |
| B10 | **Cool Roof** | Additions >300 SF: steep-slope aged reflectance >=0.20, emittance >=0.75 (or SRI >=16) in CZ 10-15 for new construction. Additions <=300 SF exempt. | Energy Code 150.1(c)11, 150.2(a) Exception 1 | `energy-envelope.md` |
| B11 | **Quality Insulation Installation (QII)** | Required for additions >700 SF per Table 150.1-A. Not required for additions <=700 SF. | Energy Code 150.2(a)1B | `energy-envelope.md` |
| B12 | **Lighting** | All luminaires must meet efficacy requirements of Section 150.0(k) — JA8-compliant high-efficacy light sources. | Energy Code 150.0(k) | `energy-envelope.md` |

---

### SECTION C: ELECTRICAL

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| C1 | **Panel Capacity** | Verify existing panel has capacity for new circuits. Standard service: 100A min for existing homes; 200A typical for additions. Load calculation per CEC Article 220. If panel upgrade needed, separate permit may apply. | CEC Article 220, 230 | `electrical-additions.md` |
| C2 | **Branch Circuits** | Bedrooms: 15A or 20A general lighting circuits. Kitchen: two 20A small-appliance circuits required. Bathroom: one 20A circuit (may serve multiple bath outlets in same dwelling). Laundry: one 20A dedicated circuit. | CEC 210.11, 210.52 | `electrical-additions.md` |
| C3 | **AFCI Protection** | Arc-fault circuit interrupter protection required for all 120V, 15A and 20A branch circuits supplying outlets/devices in: kitchens, family rooms, dining rooms, living rooms, parlors, libraries, dens, bedrooms, sunrooms, recreation rooms, closets, hallways, laundry areas, and similar rooms. | CEC 210.12(A) | `electrical-additions.md` |
| C4 | **GFCI Protection** | Ground-fault circuit interrupter protection required for receptacles in: bathrooms, garages, outdoors, crawl spaces, unfinished basements, kitchens (serving countertop surfaces), laundry areas, and within 6 ft of sinks. | CEC 210.8(A) | `electrical-additions.md` |
| C5 | **Receptacle Spacing** | Max 12 ft between receptacles along wall (6 ft from any point along wall to a receptacle). Kitchen countertops: max 24" from end, max 48" between receptacles. Island/peninsula: one receptacle per applicable rules. | CEC 210.52 | `electrical-additions.md` |
| C6 | **Smoke Alarms** | Required in each sleeping room, outside each sleeping area, on each story. Hardwired with battery backup. Interconnected so activation of one triggers all. For additions: all new sleeping rooms get alarms; existing dwelling must be brought to current alarm standards. | CRC R310.2.2, R310.3, R310.4 | `electrical-additions.md` |
| C7 | **Carbon Monoxide Alarms** | Required if dwelling has fuel-fired appliance or attached garage. Outside each sleeping area, on each occupiable level. For additions: new CO alarms required unless work is limited to exterior. Hardwired with battery backup. Interconnected. | CRC R311.2.2, R311.3, R311.5, R311.6 | `electrical-additions.md` |
| C8 | **Interconnection** | Smoke alarms: interconnected required when interior wall/ceiling finishes are removed. CO alarms: interconnected required, with wireless exception. Pre-2011 buildings: interconnection exception if no interior finishes removed. | CRC R310.4, R311.5 | `electrical-additions.md` |

---

### SECTION D: FIRE SEPARATION & EGRESS

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| D1 | **Exterior Wall Fire Separation** | Walls at <5 ft fire separation distance: 1-hour fire-resistance rated (both sides). 3-5 ft: openings limited to 25% of wall area. <3 ft: no openings permitted. Projections <2 ft: not allowed. 2-5 ft: 1-hour underside. | CRC R302.1, Table R302.1(1) | `fire-separation.md` |
| D2 | **Garage-to-House Separation** | Walls/ceilings between garage and dwelling: min 1/2" gypsum board on garage side. Ceiling below habitable space above garage: 5/8" Type X. No openings from garage directly into sleeping room. Self-closing door: solid wood >=1-3/8", solid steel, or 20-min fire-rated. | CRC R302.6, Table R302.6 | `fire-separation.md` |
| D3 | **Dwelling Unit Separation (Duplex)** | Vertical/horizontal assemblies separating units: 1-hour fire-rated (or 1/2-hour with sprinklers). Continuous from foundation to roof sheathing. Supporting construction must have equal or greater rating. | CRC R302.3 | `fire-separation.md` |
| D4 | **Fireblocking** | Required in concealed spaces of walls, floors, ceilings at: stud cavities at ceiling/floor levels, soffit connections, stairway enclosures, dropped ceilings. Materials: 2" nominal lumber, 23/32" wood structural panels, 1/2" gypsum, batts/blankets. | CRC R302.11 | `fire-separation.md` |
| D5 | **Draftstopping** | Required in floor/ceiling assemblies where usable space (attic, crawl) exceeds 1,000 SF. Located at supporting walls and at dwelling unit separations. | CRC R302.12 | `fire-separation.md` |
| D6 | **Emergency Escape & Rescue Openings (Egress)** | Every sleeping room must have an egress window/door. Min net clear opening: 5.7 SF (5.0 SF at grade). Min height: 24". Min width: 20". Max sill height: 44" above floor. New basements with sleeping rooms require egress. | CRC R319.1, R319.2, R319.6 | `egress-requirements.md` |
| D7 | **Means of Egress** | Min one exit per dwelling. Max travel distance to exterior exit: 200 ft. Min hallway width: 36". Doors: min 32" clear width, 80" height. Stairs: min 36" width, max 7-3/4" riser, min 10" tread, max 3/8" variation between risers/treads. Handrails 34-38" height. | CRC R318, R318.3, R318.7 | `egress-requirements.md` |
| D8 | **Guards & Window Fall Protection** | Guards required at open sides >30" above grade. Min 36" high (42" at open stairs). Window sill <24" above floor where >72" above grade: window opening control device or fall prevention per ASTM F2090. | CRC R321, R321.1 | `egress-requirements.md` |

---

### SECTION E: PLUMBING (When Addition Includes Bath/Kitchen)

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| E1 | **Fixture Counts** | Verify fixture units for new fixtures per CPC Table 702.1. Typical: water closet (4 DFU), lavatory (1 DFU), bathtub (2 DFU), shower (2 DFU), kitchen sink (2 DFU). Total building DFU determines drain/supply sizing. | CPC 702.1, Table 702.1 | N/A (city overlay) |
| E2 | **Water Supply** | Hot and cold water supply to all new fixtures. Minimum pipe sizing per CPC. Anti-scald valves for showers/tubs (max 120F). Water conservation fixtures per CALGreen: toilets <=1.28 gpf, showerheads <=2.0 gpm, lavs <=1.2 gpm, kitchen faucets <=1.8 gpm. | CPC 609, CALGreen 4.303.1, 4.303.2 | N/A (city overlay) |
| E3 | **Drain/Waste/Vent (DWV)** | Proper slope: 1/4" per foot for 3" and smaller; 1/8" per foot for 4" and larger. Each fixture requires a trap. Vent sizing per CPC. Cleanouts accessible. Connection to existing sewer/septic must be verified. | CPC 708, 710 | N/A (city overlay) |
| E4 | **Water Heater Sizing** | If new water heater: must be heat pump (see B8). Sizing per first-hour rating method. Location: not in sleeping room, not in closet unless listed for closet installation. Seismic strapping required in California. T&P relief valve discharge to approved location. | CPC 507, CMC 507 | N/A (city overlay) |

---

### SECTION F: GENERAL REQUIREMENTS

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| F1 | **Minimum Room Sizes** | Habitable rooms: min 70 SF, min 7 ft any horizontal dimension. Kitchens: no minimum area but min 7 ft dimension. Bathrooms: no minimum area stated, but fixture clearances govern. | CRC R312 | N/A |
| F2 | **Ceiling Height** | Habitable rooms: min 7 ft. Bathrooms, laundry, toilet rooms: min 7 ft. Beams/girders/ducts: may project to within 6 ft 4 in from floor. Sloped ceilings: min 7 ft over at least 50% of required floor area, no portion less than 5 ft. | CRC R313 | N/A |
| F3 | **Light & Ventilation** | Habitable rooms: aggregate glazing >= 8% of floor area. Openable area >= 4% of floor area (or mechanical ventilation). Bathrooms: window (1.5 SF openable) or exhaust fan (50 cfm intermittent, 20 cfm continuous). | CRC R325 | N/A |
| F4 | **Accessibility** | Additions to buildings with 3+ dwelling units or 4+ condos must comply with CBC Chapter 11A. Single-family and duplex: no accessibility trigger for additions unless creating 3+ units total. | CRC R322, CBC Chapter 11A | N/A |
| F5 | **CALGreen Requirements** | Storm water management during construction. EV charging: new dwelling with attached garage requires EV-capable raceway (1" conduit, 40A/240V capacity). Construction waste: 65% diversion from landfill. Low-flow fixtures required (see E2). Moisture management per Section 4.505. | CALGreen 4.106.2, 4.106.4, 4.408, 4.303, 4.505 | N/A |
| F6 | **Contractor Licensing** | B (General Building) license required for additions. Specialty licenses for subcontracted trades: C-10 (Electrical), C-20 (HVAC), C-36 (Plumbing), C-5 (Framing/Rough Carpentry). Workers' compensation insurance required. | B&P Code 7028 | N/A |

---

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
- **N/A** -- Does not apply to this project (e.g., plumbing checks when no bath/kitchen in addition)

---

### Quick-Reference Tables

#### Addition Size Thresholds (Energy Code)

| Addition Size | Key Energy Code Differences |
|---|---|
| <=300 SF | Exempt from roofing product requirements (Section 150.1(c)11) |
| <=400 SF | Max fenestration: greater of 75 SF or 30% addition CFA |
| <=500 SF | Electric point-of-use water heater option available |
| <=700 SF | QII not required; simplified insulation; radiant barrier required CZ 2-15 |
| >700 SF | Full prescriptive per Section 150.1(c) with addition modifications |
| <=1,000 SF | Exempt from whole-dwelling mechanical ventilation; exempt from WHF |
| >1,000 SF | Whole-dwelling ventilation required based on entire dwelling CFA |

#### Prescriptive Wall Insulation (Energy Code Table 150.1-A)

| Climate Zones | Max U-Factor (Framed Walls) | Cavity Insulation Equivalent |
|---|---|---|
| CZ 1-5, 8-16 | U-0.048 | R-21 + continuous insulation, or R-15 cavity + R-4 CI |
| CZ 6-7 | U-0.065 | R-15 or R-21 cavity only |

For additions extending existing walls: cavity insulation only (R-15 in 2x4, R-21 in 2x6) when existing siding is not being removed.

#### Ceiling/Roof Insulation (Energy Code Table 150.1-A)

| Climate Zones | Vented Attic (Option C) | Radiant Barrier |
|---|---|---|
| CZ 1-2, 4, 8-16 | R-38 | Required in CZ 2, 4, 8-16 |
| CZ 3, 5-7 | R-30 | Required in CZ 2-7 |

#### Foundation Minimum Dimensions (CRC Table R403.1)

| Stories Supported | Min Width | Min Depth | Rebar |
|---|---|---|---|
| 1 story | 12" | 18" | 1-#4 bar within 12" of top |
| 2 story | 15" | 24" | 1-#4 bar within 12" of top |
| 3 story | 18" | 30" | 2-#4 bars per local |

Concrete: min 2,500 psi. Foundation bolts: 1/2" dia., 7" embedment, max 6 ft OC, within 12" of each end/splice.

#### Floor Joist Spans — Douglas Fir-Larch #2 (CRC Table R502.3.1)

| Joist Size | 12" OC | 16" OC | 24" OC |
|---|---|---|---|
| 2x6 | 11'-10" | 10'-9" | 9'-5" |
| 2x8 | 15'-7" | 14'-2" | 12'-4" |
| 2x10 | 19'-10" | 17'-4" | 14'-3" |
| 2x12 | 23'-4" | 20'-1" | 16'-5" |

(Live load = 40 psf, dead load = 10 psf, L/360 deflection)

#### Fire Separation Distance Requirements (CRC Table R302.1(1))

| Fire Separation Distance | Walls | Openings | Projections |
|---|---|---|---|
| 0 ft | 1-hour rated (both sides) | Not allowed | Not allowed (<2 ft) |
| 3 ft | 1-hour rated (both sides) | 25% max wall area | 1-hour underside (2-5 ft) |
| 5+ ft | No rating required | Unlimited | No rating required |

#### Emergency Escape Opening Minimums (CRC R319.2)

| Dimension | Requirement |
|---|---|
| Net clear opening area | 5.7 SF (5.0 SF at grade) |
| Min net clear height | 24" |
| Min net clear width | 20" |
| Max sill height above floor | 44" |

#### Smoke & CO Alarm Requirements for Additions

| Alarm Type | Location | Trigger for Additions | Power |
|---|---|---|---|
| **Smoke** | Each sleeping room, outside sleeping areas, each story | All new sleeping rooms; existing dwelling must comply | Hardwired + battery backup |
| **CO** | Outside sleeping areas, each occupiable level | If dwelling has fuel-fired appliance or attached garage | Hardwired + battery backup |
| **Interconnection** | All alarms within dwelling | Required when interior wall/ceiling finishes removed | Hardwired or wireless |

---

### Key Principles

1. **Additions must comply with current code.** An addition triggers full code compliance for the new work. Existing portions not being altered are generally not required to be brought to current code, with specific exceptions (smoke/CO alarms, energy code ceiling insulation).

2. **Energy Code has size-based tiers.** The California Energy Code treats additions differently based on square footage. Know the thresholds: 300, 400, 500, 700, and 1,000 SF each trigger different requirements.

3. **Existing HVAC can be extended without upgrading.** When heating/cooling is extended from the existing system to serve the addition, the existing equipment need not comply with Part 6 — but capacity must be adequate (CRC R303.10). New ducts must still meet insulation and leakage requirements.

4. **PV is NOT required for additions.** Exception 6 to Section 150.2(a) exempts additions from photovoltaic requirements.

5. **Heat pump is now the standard.** For new or replacement space-conditioning systems, electric resistance is not permitted as primary heat. Heat pump required per Table 150.1-A.

6. **Smoke and CO alarms are triggered by additions.** Additions requiring a permit trigger alarm compliance for the entire dwelling unit, not just the new space. Interconnection is required when interior finishes are removed.

7. **Fire separation is distance-based.** Know the property line distance. Walls within 5 ft of the property line need fire-resistance rating. Within 3 ft, openings are prohibited.

8. **Every bedroom needs egress.** No exceptions for additions. Each new sleeping room must have an emergency escape and rescue opening meeting minimum dimensions.

9. **California requires licensed professionals for non-conventional framing.** Any structural element exceeding prescriptive CRC limits requires a California licensed architect or engineer stamp. All wood-frame >2 stories + basement requires stamped plans.

10. **Connection to existing is critical.** The tie-in between new and existing structure is often the most scrutinized aspect of an addition. Foundation dowels, wall plate connections, roof framing intersections, and diaphragm continuity must all be detailed.
