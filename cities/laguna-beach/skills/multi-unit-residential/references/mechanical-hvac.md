---
title: "Multi-Unit Residential HVAC & Ventilation — CMC 405, 501, 601-606, CBC 717, CBC 1202"
category: "mep"
relevance: "Townhome and multi-family projects — whole-unit ventilation, local exhaust, compartmentalization, and duct fire protection at rated assemblies"
key_code_sections: "CMC 405.1, 405.1.1, CMC 501.1, CMC 601.2, 603.1.5, 603.4(11), 606.1, 606.2, 606.4, CBC 717.1, 717.3.2.1, 717.5.1, 717.5.2, 717.5.3, 717.5.4, 717.6.1, 717.7, CBC 1202.1, 1202.5.1"
---

# Multi-Unit Residential HVAC & Ventilation Requirements

Source: 2025 California Mechanical Code (Title 24, Part 4), Chapters 4, 5, and 6; 2025 California Building Code (Title 24, Part 2), Sections 717 and 1202.

---

## Whole-Unit Ventilation — ASHRAE 62.2 / CMC 405

### Applicability (CMC 405.1)

All rooms or occupied spaces within residential occupancies where occupants are **nontransient** shall be designed with mechanical ventilation and exhaust in accordance with CMC 405.2 through 405.5. This applies to each dwelling unit in a multi-unit project individually.

For multi-unit residential (townhomes, apartments, condos), each unit must comply independently.

### Natural Ventilation Exception (CMC 405.1.1)

Natural ventilation is permitted **only** where approved by the Authority Having Jurisdiction and the building is in:
- Climate Zone 1 or Climate Zone 2; or
- Is thermally conditioned for **less than 876 hours per year**

In practice, most multi-unit residential projects in California (Climate Zones 3-16) cannot use this exception and must provide mechanical ventilation.

### Whole-Unit Ventilation Rates (ASHRAE 62.2 via CMC 405)

The minimum continuous whole-building ventilation rate per dwelling unit is calculated as:

**Q_total = 0.03 x A_floor + 7.5 x (N_br + 1)**

Where:
- A_floor = conditioned floor area of the dwelling unit (sq ft)
- N_br = number of bedrooms (0 for studio)

| Unit Size | Bedrooms | Min Continuous CFM |
|-----------|----------|--------------------|
| 750 sq ft | 1 | 37.5 |
| 1,000 sq ft | 2 | 52.5 |
| 1,200 sq ft | 2 | 58.5 |
| 1,200 sq ft | 3 | 66.0 |
| 1,500 sq ft | 3 | 75.0 |
| 1,800 sq ft | 4 | 91.5 |
| 2,000 sq ft | 4 | 97.5 |

This ventilation may be provided by:
- A dedicated supply fan (ERV/HRV preferred for energy recovery)
- An exhaust-only strategy with passive makeup air inlets
- A balanced system (supply + exhaust)

### 35-Unit Townhome Application

Each townhome unit has its own HVAC system. Whole-unit ventilation is calculated and provided per unit. The mechanical plans must show the ventilation strategy (supply, exhaust, or balanced) and the calculated cfm rate for each unit type/floor plan.

---

## Local Exhaust Requirements — CMC 501, Table 403.7

### Applicability (CMC 501.1)

Chapter 5 covers environmental air ducts and exhaust systems. For multi-unit residential, every dwelling unit kitchen and bathroom requires local exhaust.

### Kitchen Exhaust

| Method | Minimum Rate |
|--------|-------------|
| Range hood (intermittent) | **100 cfm** |
| Downdraft or equivalent (intermittent) | **100 cfm** |
| Continuous kitchen exhaust | **50 cfm** |

Range hoods shall be vented to the exterior. Recirculating hoods do **not** satisfy code exhaust requirements.

### Bathroom Exhaust

| Method | Minimum Rate |
|--------|-------------|
| Intermittent (switched) | **50 cfm** |
| Continuous | **25 cfm** |

Each bathroom (full bath, half bath, or powder room with a water closet) requires exhaust. Exhaust shall be ducted to the exterior of the building.

### Laundry Rooms

Where a laundry room is provided in a dwelling unit, mechanical exhaust is required per Table 403.7.

---

## Compartmentalization — Air Sealing Between Units

### Why It Matters

Multi-unit residential buildings must prevent air (and contaminant) transfer between dwelling units. Sound, smoke, cooking odors, and secondhand pollutants migrate through shared walls, floors, and ceilings if not properly sealed.

### Air Leakage Testing Requirements

California Energy Code (Title 24, Part 6) Section 160.2(b)2 requires multifamily dwelling units to demonstrate:

- **Enclosure leakage not exceeding 0.30 cfm50/sq ft** of dwelling unit envelope surface area (at 50 Pa test pressure); or
- Compliance via prescriptive sealing of all penetrations through the unit boundary (walls, floors, ceilings shared with other units, corridors, or unconditioned spaces)

All penetrations through rated assemblies between dwelling units shall be sealed with fire-rated caulk, putty pads, or listed firestop systems, including:
- Electrical boxes and conduit penetrations
- Plumbing pipe penetrations
- HVAC duct penetrations
- Recessed can lights in rated ceiling assemblies

### Party Wall / Party Floor Construction

Party walls between townhome units are typically 1-hour fire-resistance-rated assemblies (fire partitions per CBC 708). Party walls in apartment buildings may be 1-hour fire partitions or, where serving as fire barriers, 2-hour assemblies.

All HVAC duct penetrations through these assemblies require damper protection per CBC 717 (see below).

---

## Duct Penetrations Through Fire-Rated Assemblies — CBC 717

### General Rule (CBC 717.1)

Section 717 governs protection of duct penetrations and air transfer openings in assemblies required to be protected. Every duct that passes through a fire-resistance-rated wall, floor/ceiling, or roof/ceiling assembly must be evaluated for damper requirements.

### Critical Restriction: Flexible Ducts (CBC 717.7)

**Flexible ducts and air connectors shall not pass through any fire-resistance-rated assembly.** Flexible air connectors shall not pass through any wall, floor, or ceiling. This is absolute — no exceptions.

Similarly, CMC 603.1.5 states: "Ducts listed and labeled to UL 181 shall not penetrate a fire-resistance-rated assembly or construction." And CMC 603.4 item (11): "Flexible air ducts shall not penetrate a fire-resistance-rated assembly or construction."

All penetrations of rated assemblies must use **rigid metal ductwork**.

### Ducts Without Dampers (CBC 717.1.2)

Where ducts penetrate fire-resistance-rated walls and are not required by Section 717 to have fire dampers, they shall still comply with through-penetration firestop requirements of CBC 714.3 through 714.4.3 (walls) or CBC 714.5 through 714.6.2 (horizontal assemblies).

---

## Fire Damper Requirements by Assembly Type

### Fire Walls (CBC 717.5.1)

Ducts and air transfer openings permitted in fire walls per CBC 706.11 shall be protected with **listed fire dampers**. However, note that CBC 706.11 is highly restrictive — ducts are generally **not permitted to penetrate fire walls** unless specifically allowed. Fire walls are not the same as fire barriers or fire partitions.

Where a fire wall serves as a horizontal exit, a **listed smoke damper** is additionally required at each penetration point (CBC 717.5.1.1).

### Fire Barriers (CBC 717.5.2)

For **Group R occupancies** (which includes multi-unit residential), the California amendment [SFM] requires ducts and air transfer openings penetrating fire barriers to be protected with **approved fire AND smoke dampers** (i.e., combination fire/smoke dampers).

Ducts shall NOT penetrate enclosures for interior exit stairways, ramps, or exit passageways (except per CBC 1023.5 and 1024.6).

**Exceptions** (SFM version for Group R):
1. Fire dampers not required where penetrations are tested per ASTM E119 as part of the rated assembly
2. Fire and smoke dampers not required where ducts are part of an approved smoke control system per Section 909

### Shaft Enclosures (CBC 717.5.3)

Shaft enclosures penetrated by ducts shall be protected with **listed fire AND smoke dampers**.

**Key exception for multi-unit residential** (Exception 2): In Group B and R occupancies equipped throughout with an automatic sprinkler system (per 903.3.1.1), smoke dampers are not required at shaft penetrations where **all** of the following are met:
1. Kitchen, clothes dryer, bathroom, and toilet room exhaust openings use steel exhaust subducts with wall thickness >= 0.0187 in. (No. 26 gage)
2. Subducts extend not less than **22 inches vertically** within the shaft
3. An exhaust fan at the upper terminus of the shaft operates **continuously** per Section 909.11

This exception is commonly used in multi-story apartment buildings with central exhaust shafts.

### Fire Partitions — Party Walls (CBC 717.5.4)

For **Group R occupancies** (California [SFM] amendment), ducts and air transfer openings penetrating fire partitions shall be protected with **listed fire dampers**.

**Exceptions** (SFM version for Group R):
1. Fire dampers not required in corridor penetrations where the duct is steel >= 0.019 in. thick, protected as a through penetration per Section 713, and has no openings serving the corridor
2. Fire dampers not required where the duct penetrating the wall complies with all of the following:
   - Duct does not exceed 100 sq in.
   - Duct is steel >= 0.0217 in. thick
   - Duct has no openings communicating the corridor with adjacent spaces
   - Duct is installed above a ceiling
   - Duct does not terminate at a wall register in the fire-rated wall
   - Through-penetration firestop protection per Section 714, OR a 12 in. steel sleeve centered in the opening with retaining angles and mineral wool batting

### Corridor Penetrations (CBC 717.5.4.1)

For Group R occupancies [SFM], a **listed smoke damper** shall also be provided at each point a duct or air transfer opening penetrates a fire-resistance-rated corridor enclosure required to have smoke and draft doors per CBC 716.2.2.1.

**Exceptions**:
1. Smoke dampers not required where ducts are part of an approved smoke control system per Section 909
2. Smoke dampers not required in corridor penetrations where the duct is steel >= 0.019 in. thick and has no openings serving the corridor

---

## Horizontal Assembly Penetrations (CBC 717.6)

### Through Penetrations — Floor/Ceiling (CBC 717.6.1)

A duct penetrating a fire-resistance-rated floor/ceiling assembly connecting **not more than two stories** is permitted without a shaft enclosure, provided a **listed fire damper** is installed at the floor line (or the duct is firestopped per CBC 714.5).

**Exception**: In occupancies other than Groups I-2 and I-3, a duct may penetrate **three floors or fewer** without a fire damper at each floor if all of the following are met:
1. Duct is within a wall cavity, steel >= 0.0187 in. (No. 26 gage)
2. Duct opens into only one dwelling unit and is continuous to the building exterior
3. Duct does not exceed 4 in. nominal diameter, total area <= 100 sq in. per 100 sq ft of floor
4. Annular space around duct prevents passage of flame and hot gases per ASTM E119 criteria
5. Grille openings in fire-rated ceiling assemblies have ceiling radiation dampers

### Nonfire-Resistance-Rated Floor Assemblies (CBC 717.6.3)

Ducts penetrating non-rated floor assemblies connecting not more than two stories require only approved noncombustible material around the annular space. For three stories, a **fire damper at each floor line** is required (unless within an individual dwelling unit, per exception).

---

## Fire Damper and Smoke Damper Specifications — CMC 606

### Fire Dampers (CMC 606.2)

Fire dampers shall comply with **UL 555**, be installed per manufacturer's instructions, and be tested for closure under airflow conditions. Label must show maximum airflow and direction of flow.

### Smoke Dampers (CMC 606.1)

Smoke dampers shall comply with **UL 555S** and be installed per manufacturer's instructions where required by CBC.

### Combination Fire/Smoke Dampers (CMC 606.4)

Combination fire/smoke dampers shall comply with **both UL 555 and UL 555S**. When a combination damper activates automatically, the HVAC system serving it shall **immediately shut down** (CMC 606.4.1). The system shall not restart until all dampers are reset and fully opened.

### Damper Ratings (CBC 717.3.2.1)

| Assembly Rating | Minimum Fire Damper Rating |
|----------------|---------------------------|
| Less than 3-hour | **1.5-hour** |
| 3-hour or greater | **3-hour** |

Smoke damper leakage ratings shall be **Class I or II**. Elevated temperature rating shall be not less than **250 deg F** (CBC 717.3.2.2).

### Damper Actuation (CBC 717.3.3)

- **Fire dampers**: Fusible link at approximately 50 deg F above normal duct temperature, but not less than **160 deg F** (CBC 717.3.3.1)
- **Smoke dampers**: Close upon actuation of a listed smoke detector installed within 5 ft of the damper inside the duct, or by area smoke detection system (CBC 717.3.3.2)
- **Combination fire/smoke dampers**: Both fire and smoke actuation methods required (CBC 717.3.3.3)

### Access and Identification (CMC 606.8, CBC 717.4)

All fire and smoke dampers shall have approved access openings large enough for inspection and maintenance. Access shall not require tools. Access points shall be permanently labeled with letters >= 1/2 in. high reading one of:
- "FIRE DAMPER"
- "SMOKE DAMPER"
- "FIRE/SMOKE DAMPER"

### Periodic Testing (CMC 606.6)

- Fire dampers: tested per **NFPA 80**
- Smoke dampers: tested per **NFPA 105**
- Combination fire/smoke dampers: tested per **both NFPA 80 and NFPA 105**

---

## Natural Ventilation Alternative — CBC 1202

### General (CBC 1202.1)

Buildings shall be provided with natural ventilation per Section 1202.5, **or** mechanical ventilation per the California Mechanical Code.

**Important**: Dwelling units complying with the air leakage requirements of the California Energy Code shall be ventilated by **mechanical means** per CMC 403 (CBC 1202.1). Since all new multi-unit residential must meet Energy Code air leakage limits, mechanical ventilation is effectively mandatory.

### Natural Ventilation Area (CBC 1202.5.1)

Where natural ventilation is used (and approved), the openable area of openings to the outdoors shall be **not less than 4% of the floor area** being ventilated.

For adjoining rooms without outdoor openings ventilated through an adjacent room, the connecting opening shall be not less than **8% of the interior room's floor area**, but not less than **25 sq ft** (CBC 1202.5.1.1).

### Contaminant Exhaust (CBC 1202.5.2)

Even in naturally ventilated spaces, contaminant sources shall be removed per the CMC. Specifically, **bathrooms** containing bathtubs, showers, or spas shall always be **mechanically ventilated** per the CMC (CBC 1202.5.2.1).

---

## Shaft Requirements for Multi-Story Duct Runs

### Vertical Risers (CMC 603.1.4)

Ducts listed and labeled to UL 181 (flexible and certain nonmetallic ducts) shall **not be used for vertical risers** in air-duct systems serving more than two stories. Use rigid metal ductwork for multi-story vertical runs.

### Shaft Enclosure (CBC 713 referenced via 717.6)

Ducts penetrating more than two stories of a fire-resistance-rated floor/ceiling assembly generally require a **shaft enclosure** per CBC 713, with fire and smoke dampers at each penetration per CBC 717.5.3.

For townhome projects (typically 2-3 stories per unit), ducts staying within a single dwelling unit and connecting no more than two stories can avoid shaft enclosures if a fire damper is installed at the floor line (CBC 717.6.1).

---

## Duct System General Requirements — CMC Chapter 6

### Duct Sizing (CMC 601.2)

Residential duct systems shall be sized per **ACCA Manual D**, **ACCA Manual Zr** (for zoned systems), or other approved methods.

### Seal Class (CMC 603.1.1)

All ducts regardless of pressure classification shall be sealed to **Seal Class A**.

### Duct Insulation (CMC 605.1)

Air ducts conveying air at temperatures exceeding 140 deg F shall be insulated. Coverings shall not penetrate a fire-resistance-rated assembly (CMC 605.1.2). See the California Energy Code for climate-zone-specific R-value requirements.

### Corridors (CMC 602.7)

Corridors shall **not** be used to convey air to or from rooms where the corridor is required to be of fire-resistive construction. Corridors shall not serve as supply, return, exhaust, relief, or ventilation air ducts.

---

## 35-Unit Townhome — Practical Application

For a typical 35-unit attached townhome project where each unit has individual HVAC:

1. **Whole-unit ventilation**: Calculate per ASHRAE 62.2 formula for each floor plan. Show cfm rate, fan type (ERV/HRV or exhaust-only), and duct routing on mechanical plans.

2. **Local exhaust**: Each unit needs a ducted range hood (100 cfm intermittent) and bathroom exhaust fans (50 cfm intermittent or 25 cfm continuous per bathroom). All exhaust must terminate at the building exterior.

3. **Party walls (fire partitions)**: Where any duct penetrates a 1-hour party wall between units, install a **listed fire damper** rated at 1.5 hours minimum. For Group R per [SFM], fire dampers are required unless one of the exceptions in CBC 717.5.4 applies (e.g., small steel duct with sleeve and mineral wool, or sprinklered building with continuous steel duct).

4. **Flexible ducts**: Cannot penetrate any fire-resistance-rated assembly. Transition to rigid metal ductwork before crossing party walls or rated floor/ceiling assemblies.

5. **Floor penetrations**: Ducts passing between floors within the same unit and connecting no more than two stories need a fire damper at the floor line (CBC 717.6.1). Within an individual dwelling unit in a non-rated floor assembly, fire dampers are not required (CBC 717.6.3, Exception).

6. **Shaft enclosures**: Not typically needed for townhomes where each unit has its own HVAC and ducts stay within the unit boundary. If a central exhaust shaft is used (e.g., for stacked bathroom exhaust in an apartment-style building), fire and smoke dampers are required at each shaft penetration unless the subduct exception applies (CBC 717.5.3, Exception 2).

7. **Compartmentalization**: Seal all duct penetrations through the unit envelope with listed firestop systems. Confirm air leakage per Energy Code Section 160.2(b)2 (0.30 cfm50/sq ft of dwelling unit envelope surface area or prescriptive sealing).

8. **Automatic shutoff**: HVAC systems supplying air in excess of 2,000 cfm to enclosed spaces require duct smoke detection and automatic shutoff (CMC 609.1). Individual townhome units rarely exceed this threshold, but verify for large floor plans.

---

## Cross-References

| Topic | Reference |
|-------|-----------|
| Ductwork sizing, sealing, and leakage testing | `../../hvac/references/ductwork.md` |
| Combustion air for gas-fired equipment | `../../hvac/references/combustion-air.md` |
| Equipment location (attic, crawl space, garage) | `../../hvac/references/equipment-location.md` |
| Energy code HVAC efficiency requirements | `../../hvac/references/energy-code-hvac.md` |
| Fire-rated assemblies and firestop (general) | `../../ltia-demolition/references/fire-rated-assemblies-cbc707-714.md` |
| Smoke and CO alarms triggered by HVAC permits | `../../hvac/references/smoke-co-alarms.md` |

---

## Key Code Sections

| Code | Section | Topic |
|------|---------|-------|
| CMC | 405.1 | Mechanical ventilation required for nontransient residential |
| CMC | 405.1.1 | Natural ventilation exception (CZ 1, 2 only) |
| CMC | 501.1 | Exhaust system applicability |
| CMC | 601.2 | Duct sizing — ACCA Manual D/Zr |
| CMC | 602.7 | Corridors shall not convey air |
| CMC | 603.1.4 | UL 181 ducts prohibited as vertical risers > 2 stories |
| CMC | 603.1.5 | UL 181 ducts shall not penetrate rated assemblies |
| CMC | 603.4(11) | Flexible air ducts shall not penetrate rated assemblies |
| CMC | 603.9 | Duct joints and seams — Seal Class A |
| CMC | 606.1 | Smoke dampers — UL 555S |
| CMC | 606.2 | Fire dampers — UL 555 |
| CMC | 606.4 | Combination fire/smoke dampers — UL 555 + UL 555S |
| CMC | 606.4.1 | HVAC shutdown on combination damper activation |
| CMC | 606.8 | Damper access and identification |
| CMC | 609.1 | Duct smoke detection and auto shutoff (> 2,000 cfm) |
| CBC | 717.1 | Duct penetration protection — general |
| CBC | 717.3.2.1 | Fire damper rating table (1.5-hr / 3-hr) |
| CBC | 717.3.3 | Damper actuation methods |
| CBC | 717.5.1 | Fire walls — fire dampers required (ducts generally prohibited) |
| CBC | 717.5.2 | Fire barriers — fire + smoke dampers (Group R, SFM) |
| CBC | 717.5.3 | Shaft enclosures — fire + smoke dampers (with subduct exception) |
| CBC | 717.5.4 | Fire partitions — fire dampers required (Group R, SFM) |
| CBC | 717.5.4.1 | Corridor penetrations — smoke dampers |
| CBC | 717.6.1 | Floor/ceiling penetrations — fire damper at floor line |
| CBC | 717.6.3 | Non-rated floor assemblies — noncombustible annular fill |
| CBC | 717.7 | Flexible ducts shall not pass through rated assemblies |
| CBC | 1202.1 | Ventilation — natural or mechanical required |
| CBC | 1202.5.1 | Natural ventilation — openable area >= 4% of floor area |
| CBC | 1202.5.2.1 | Bathrooms always require mechanical exhaust |
