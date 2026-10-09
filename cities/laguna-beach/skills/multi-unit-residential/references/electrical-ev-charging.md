---
title: "Electrical — EV Charging Requirements for Multifamily Dwellings"
category: mep
relevance: "Load for any multi-unit project with parking. California's 2025 CALGreen code (effective Jan 1, 2026) mandates EV receptacles for every dwelling unit and Level 2 chargers in 25% of unassigned spaces. CEC Article 625 governs EVSE installation, dedicated circuits, and personnel protection."
key_code_sections: "CALGreen 4.106.4, 4.106.4.2, 4.106.4.2.2; CEC Article 625, 625.40, 625.41, 625.42, 625.54"
---

## EV Charging Requirements for Multifamily Dwellings

### Applicability

CALGreen Section 4.106.4 applies to all new construction. Multifamily dwellings, hotels, motels, and new residential parking facilities must comply with Section 4.106.4.2. EVSE must comply with the California Electrical Code (CEC Article 625). (CALGreen 4.106.4)

**Exceptions** — EV charging infrastructure is not required when:
1. The local enforcing agency determines it is infeasible (no utility power supply, or utility infrastructure costs would adversely impact construction cost) (CALGreen 4.106.4, Exception 1)
2. ADUs and JADUs without additional parking facilities (CALGreen 4.106.4, Exception 2)

Calculations for required spaces are always **rounded up** to the nearest whole number. (CALGreen 4.106.4.2)

### Definitions: EV-Capable vs. EV-Ready vs. EVCS

| Term | What Is Installed | Description |
|------|-------------------|-------------|
| **EV Capable** | Raceway + panel space reserved | Conduit from panel to parking space; breaker space labeled "EV CAPABLE" — no circuit, no receptacle |
| **EV Ready** | Receptacle installed (low-power Level 2) | Dedicated branch circuit with a 208/240V receptacle (NEMA 6-20R, 14-30R, or 14-50R) at the parking space |
| **EVCS (EV Charging Station)** | Level 2 charger installed | Fully operational EV charger with J1772 or J3400 connector, available for use |

Note: The 2025 CALGreen code for multifamily requires **EV-ready** (receptacles) and **EVCS** (chargers) — it goes beyond the older EV-capable conduit-only approach. (CALGreen 4.106.4.2.2)

### Multifamily EV Ready Spaces — Receptacles (CALGreen 4.106.4.2.2(1))

#### Assigned Parking (4.106.4.2.2(1)(a))

Where dwelling units have **assigned parking spaces** equal to or greater than the number of units:
- **At least one low-power Level 2 EV charging receptacle** per dwelling unit, installed at an assigned space

Where total dwelling units **exceed** assigned parking spaces:
- **All** assigned parking spaces shall have a low-power Level 2 EV charging receptacle

(CALGreen 4.106.4.2.2(1)(a))

**Exception:** Parking areas served by parking lifts (including automated mechanical-access open parking garages) or areas otherwise incapable of supporting EV charging.

#### Unassigned Parking (4.106.4.2.2(1)(b))

Where dwelling units have **unassigned parking spaces** equal to or greater than the number of units:
- **At least one low-power Level 2 EV charging receptacle** per dwelling unit, installed at an unassigned space

Where total dwelling units **exceed** unassigned parking spaces:
- **All** unassigned parking spaces shall have a low-power Level 2 EV charging receptacle

(CALGreen 4.106.4.2.2(1)(b))

**Exception:** Same parking lift exception as assigned parking.

#### Mixed Assigned + Unassigned Parking (4.106.4.2.2(1)(c))

Where a building has **both** assigned and unassigned parking, with combined total equal to or greater than the number of units:
- At least one low-power Level 2 EV charging receptacle per dwelling unit at **either** the assigned or unassigned space, **but not both**

(CALGreen 4.106.4.2.2(1)(c))

#### Receptacle Power Source (4.106.4.2.2(1)(d))

EV charging receptacles at **assigned** parking spaces shall be provided with a **dedicated branch circuit connected to the dwelling unit's electrical panel**, unless determined infeasible by the project builder/designer with local enforcing agency concurrence.

(CALGreen 4.106.4.2.2(1)(d))

This is significant for electrical design: each unit's panel must have capacity for its own EV circuit, and conduit routing must connect the unit panel to the assigned parking space.

#### Receptacle Configurations (4.106.4.2.2(1)(e))

208/240V EV charging receptacles shall be one of:

| Amperage | NEMA Configuration | Typical Use |
|----------|-------------------|-------------|
| 20A | **NEMA 6-20R** | Low-power Level 2 (~3.8 kW at 240V) |
| 30A | **NEMA 14-30R** | Mid-power Level 2 (~7.2 kW at 240V) |
| 50A | **NEMA 14-50R** | Full-power Level 2 (~12 kW at 240V) |

(CALGreen 4.106.4.2.2(1)(e))

### Multifamily EV Charger Spaces — Level 2 Chargers (CALGreen 4.106.4.2.2(2))

#### 25% of Unassigned/Common Use Spaces (4.106.4.2.2(2)(a))

**In addition to** the receptacle requirements above, **25% of unassigned or common use parking spaces** not already provided with low-power Level 2 receptacles must be equipped with **Level 2 EV chargers** available for use by all residents or guests.

(CALGreen 4.106.4.2.2(2)(a))

#### Charger Connectors (4.106.4.2.2(2)(b))

EV chargers shall be equipped with **J1772 or J3400** (formerly NACS/Tesla) connectors. (CALGreen 4.106.4.2.2(2)(b))

#### Automatic Load Management Systems (ALMS) (4.106.4.2.2(2)(c))

An ALMS may be used to reduce the maximum required electrical capacity per space. When ALMS is used:
- The electrical system and on-site distribution transformers must deliver **at least 3.3 kW simultaneously** to each EVCS served by the ALMS
- Branch circuit minimum capacity: **40 amperes**
- Installed EV chargers minimum capacity: **not less than 30 amperes**

(CALGreen 4.106.4.2.2(2)(c))

ALMS is a critical tool for managing electrical demand in large multifamily projects. It allows the total building electrical service to be sized below the theoretical maximum of all chargers operating at full power simultaneously, while still guaranteeing a minimum 3.3 kW per station.

### EVCS Space Dimensions and Accessibility

#### Space Dimensions (4.106.4.2.2.1.1)

- Minimum length: **18 feet** (5486 mm)
- Minimum width: **9 feet** (2743 mm)
- 1 in every 25 EVCS spaces (minimum 1) must have an **8-foot wide minimum aisle** (or 5-foot aisle if the EVCS space is widened to 12 feet)
- Surface slope for accessible EVCS: not exceeding **2.083%** in any direction
- Accessible EVCS must be adjacent to an accessible parking space (CBC Chapter 11A) or located on an accessible route

(CALGreen 4.106.4.2.2.1.1)

#### Accessibility (4.106.4.2.2.1.2)

All EV chargers must comply with CBC Chapter 11B accessibility provisions. EV ready spaces and EVCS in multifamily must comply with CBC Chapter 11A, Section 1109A. (CALGreen 4.106.4.2.2.1.2)

### Signage (4.106.4.2.5)

EV ready spaces must be identified by signage or pavement markings in compliance with **Caltrans Traffic Operations Policy Directive 13-01** (Zero Emission Vehicle Signs and Pavement Markings) or its successor. (CALGreen 4.106.4.2.5)

### CEC Article 625 — EVSE Installation Requirements

#### Scope (625.1)

Article 625 covers electrical conductors and equipment connecting an electric vehicle to premises wiring for charging, power export, or bidirectional current flow. All EVSE must be **listed** (625.6). New construction EV charging must also comply with CALGreen Chapter 4 and Chapter 5. (CEC 625.1, 625.1.1, 625.6)

#### Dedicated Branch Circuits (625.40)

Each outlet supplying EVSE **greater than 16 amperes or 120 volts** must be supplied by an **individual branch circuit**.

**Exception:** Branch circuits may feed multiple EVSEs where permitted by an Energy Management System (625.42(A)) or EVSE with adjustable settings (625.42(B)). (CEC 625.40)

#### Overcurrent Protection (625.41)

Overcurrent protection for feeders and branch circuits supplying EVSE must be:
- Sized for **continuous duty**
- Rated at **not less than 125%** of the maximum load of the equipment

EV charging loads are considered **continuous loads**. (CEC 625.41, 625.42)

For example: a 40A EV circuit requires a **50A breaker** (40A x 125% = 50A).

#### Energy Management Systems (625.42(A))

Where an EMS per Section 750.30 provides load management, the maximum equipment load on service and feeder is the maximum permitted by the EMS. The EMS may be integral to one piece of equipment or a listed multi-equipment system. (CEC 625.42(A))

This aligns with CALGreen's ALMS provisions — the EMS/ALMS allows service sizing below the sum of all individual charger ratings while maintaining minimum delivery guarantees.

#### GFCI Protection (625.54)

**All receptacles** installed for EV charging connection shall have **ground-fault circuit-interrupter (GFCI) protection for personnel**. (CEC 625.54)

This applies to every EV receptacle in the parking facility, whether assigned or unassigned.

#### Outdoor/Wet Location Requirements (625.56)

Receptacles in **wet locations** for EV charging must have a weatherproof enclosure with plug inserted or removed. Outlet box hoods must be listed and identified as **extra duty**. (CEC 625.56)

#### Equipment Height (625.50)

Unless specifically listed for the location, the coupling means of EVSE must be stored or located at:
- Indoor locations: not less than **18 inches** above floor level
- Outdoor locations: not less than **24 inches** above grade level

(CEC 625.50)

#### Cord and Cable Length (625.17(C))

Overall usable cord/cable length shall not exceed **25 feet** unless equipped with a cable management system that is part of the listed EVSE. (CEC 625.17(C))

#### Ventilation (625.52)

Indoor EV charging using listed equipment that does not require ventilation (modern sealed battery EVs) does not need mechanical ventilation (625.52(A)). Where equipment is listed for EVs requiring ventilation, mechanical supply and exhaust ventilation must be provided per the tables in 625.52(B). (CEC 625.52)

### Electrical Capacity Planning for Multifamily

#### Panel and Service Sizing Considerations

For each dwelling unit with assigned parking:
- The unit's electrical panel must accommodate a **dedicated EV branch circuit** (CALGreen 4.106.4.2.2(1)(d))
- Minimum circuit sizing depends on receptacle type: 20A circuit for NEMA 6-20R, 30A for NEMA 14-30R, 50A for NEMA 14-50R
- Overcurrent protection at 125% of continuous load (CEC 625.41)

For common/unassigned EVCS:
- 40A minimum branch circuit capacity when using ALMS (CALGreen 4.106.4.2.2(2)(c))
- 3.3 kW minimum simultaneous delivery per EVCS when using ALMS
- Without ALMS, each charger circuit must be individually sized at full rated capacity

#### Raceway and Conduit Planning

- Raceways must be **continuous** at enclosed, inaccessible, or concealed areas (per 4.106.4.1 principle, applicable to multifamily infrastructure design)
- Route conduit from electrical panels to parking spaces during rough-in — retrofitting is significantly more expensive
- For assigned spaces in podium or structured parking, coordinate vertical conduit runs with structural design

### 35-Unit Test Case Calculation

For a 35-unit multifamily building:

**Scenario: 35 assigned spaces + 35 unassigned guest/visitor spaces (70 total)**

| Requirement | Calculation | Result |
|-------------|-------------|--------|
| Assigned space receptacles (4.106.4.2.2(1)(a)) | 1 per dwelling unit = 35 | **35 EV receptacles** at assigned spaces |
| Unassigned space receptacles (4.106.4.2.2(1)(b)) | Already met via assigned spaces under (1)(c) mixed rule | **0 additional** (if using mixed parking rule) |
| Level 2 chargers at unassigned spaces (4.106.4.2.2(2)(a)) | 25% of unassigned spaces not already served = 0.25 x 35 = 8.75, rounded up | **9 Level 2 EV chargers** at unassigned/common spaces |
| Accessible EVCS (4.106.4.2.2.1.1) | 1 per 25 EVCS, minimum 1 = ceil(9/25) | **1 accessible EVCS** (8-ft aisle, 2.083% max slope) |

**Electrical load summary (with ALMS):**
- 35 assigned receptacles: If NEMA 6-20R (20A/240V = 4.8 kW each) — dedicated circuits from unit panels
- 9 Level 2 chargers: 40A branch circuits, 3.3 kW minimum simultaneous delivery via ALMS = 29.7 kW minimum transformer/service capacity for EVCS
- Without ALMS: 9 chargers at 30A+ continuous = 9 x 7.2 kW = 64.8 kW minimum

**Scenario: 35 assigned spaces only (no unassigned)**

| Requirement | Calculation | Result |
|-------------|-------------|--------|
| Assigned space receptacles | 1 per unit = 35 | **35 EV receptacles** |
| Level 2 chargers | 25% applies to unassigned/common use only — 0 unassigned spaces | **0 Level 2 chargers required** |

The 25% charger requirement only applies to **unassigned or common use** spaces beyond those already served by receptacles.

### Additions and Alterations (4.106.4.3)

When existing multifamily parking facilities are altered or new spaces added (requiring a building permit), each space added or altered must have access to either a low-power Level 2 EV receptacle or Level 2 EV charger, unless determined infeasible by the project builder/designer with enforcing agency concurrence. (CALGreen 4.106.4.3)

**Exception:** Work limited to installing 120V receptacles for Level 1 EV charging.

---

### Cross-References

- **CBC Chapter 11A, Section 1109A** — Accessible EV charging spaces in multifamily
- **CBC Chapter 11B** — Public accommodation EV charger accessibility
- **CEC Article 625** — Complete EVSE installation requirements (circuits, protection, wiring methods)
- **CEC Section 750.30** — Energy Management Systems for load management
- **CALGreen Chapter 5, Division 5.1** — Nonresidential/commercial EV requirements (hotels, motels also reference 4.106.4.2.6)
- **Caltrans Policy Directive 13-01** — EV signage and pavement markings
- **Vehicle Code Section 22511.2** — EV charging space counts toward minimum parking requirements

### Key Code Sections

- **CALGreen 4.106.4** — EV charging for new construction (scope, exceptions)
- **CALGreen 4.106.4.2** — Multifamily dwellings, hotels/motels, residential parking facilities
- **CALGreen 4.106.4.2.2(1)** — EV ready spaces with receptacles (assigned, unassigned, mixed)
- **CALGreen 4.106.4.2.2(1)(e)** — Receptacle configurations (NEMA 6-20R, 14-30R, 14-50R)
- **CALGreen 4.106.4.2.2(2)** — EV charger spaces (25% of unassigned, J1772/J3400 connectors, ALMS)
- **CALGreen 4.106.4.2.2.1.1** — EVCS space dimensions (18 ft x 9 ft, accessible aisle)
- **CALGreen 4.106.4.2.5** — EV ready space signage
- **CALGreen 4.106.4.3** — Additions and alterations to existing parking
- **CEC 625.1** — Scope of EV power transfer system article
- **CEC 625.6** — Listed equipment requirement
- **CEC 625.40** — Individual branch circuit per EVSE outlet (>16A or >120V)
- **CEC 625.41** — Overcurrent protection at 125% continuous load
- **CEC 625.42** — Rating and load management (EMS, adjustable settings)
- **CEC 625.54** — GFCI protection for all EV receptacles
- **CEC 625.56** — Weatherproof enclosures for wet locations
