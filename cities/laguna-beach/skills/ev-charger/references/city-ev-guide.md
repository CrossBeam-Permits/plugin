# Laguna Beach EV Charger — Installation Guidelines & Load Calculation

Source: `ev-charger-installation-guidelines.pdf` (Building Division)
Source: `ev-charging-code-compliance-checklist.pdf` (Residential)

---

## Load Calculation Estimator (NEC 220.83(A))

Laguna Beach provides a load calculation worksheet for estimating whether an existing electrical service can handle the added EV charger load.

### Worksheet Line Items

| Category | Description | Typical Watts |
|----------|-------------|---------------|
| **General Lighting** | Square footage of house x 3 | 3 watts/sq. ft. |
| **Kitchen Circuits** | Kitchen circuits (always checked) | 3,000 |
| | Electric oven | 2,000 |
| | Electric stove top | 5,000 |
| | Microwave | 1,500 |
| | Garbage disposal | 1,000 |
| | Automatic dishwasher | 3,500 |
| | Garbage compactor | 1,000 |
| | Instantaneous hot water at sink | 1,500 |
| **Laundry Circuit** | Laundry circuit (always checked) | 1,500 |
| | Electric clothes dryer | 4,500 |
| **HVAC** | Central heating (gas) and A/C | 6,000 |
| | Window mounted A/C | 1,000 |
| | Whole-house or attic fan | 500 |
| | Central electric furnace | 8,000 |
| | Evaporative cooler | 500 |
| **Other Loads** | Electric water heater (storage) | 4,000 |
| | Electric tankless water heater | 15,000 |
| | Swimming pool or spa | 3,500 |
| | Other (describe) | varies |
| **EV Charger** | Electric vehicle charger rating* | varies |

*Use nameplate rating in watts or calculate as: (Ampere rating of circuit x 240 volts = Watts)

**CRITICAL REVIEW STEP**: Independently add up ALL checked line items. Do NOT trust the applicant's stated "Total Watts Used." Compare your sum to theirs. Arithmetic errors on load calcs are the #1 most common mistake.

---

## Panel Sizing Table (NEC 220.83(A))

Apply the Total Watts Used to this table to determine if the existing panel is adequate:

| Total Watts Used | Minimum Required Service Panel (Main Breaker) |
|------------------|----------------------------------------------|
| up to 24,000 | 60 amp |
| 24,001 to 48,000 | 100 amps |
| 48,001 to 63,000 | 125 amps |
| 63,001 to 78,000 | 150 amps |
| 78,001 to 108,000 | 200 amps |
| 108,001 to 123,000 | 225 amps |

**CAUTION**: This table is ONLY for adding EV charger loads to EXISTING dwelling electrical service. It is NOT for sizing a NEW or UPGRADED panel — that requires a completely different load calculation methodology by a qualified electrical contractor or engineer.

---

## Wire & Conduit Sizing Table

| Circuit Breaker | Min. Conductor (THHN) | EMT | RNC (Sch 40) | FMC |
|----------------|----------------------|-----|-------------|-----|
| 20 amp | #12 | 1/2" | 1/2" | 1/2" |
| 30 amp | #12 | 1/2" | 1/2" | 1/2" |
| 40 amp | #10 | 1/2" | 1/2" | 1/2" |
| 50 amp | #8 | 3/4" | 3/4" | 3/4" |
| 60 amp | #6 | 3/4" | 3/4" | 3/4" |
| 70 amp | #6 | 3/4" | 3/4" | 3/4" |

***Based on 4 wires in conduit (2 current-carrying conductors, 1 grounded conductor, 1 equipment ground).

**Alternate**: Nonmetallic Sheathed Cable (Romex/NMC) may be used if protected from physical damage inside a wall cavity or attic space separated from occupied space by drywall or plywood.

---

## Conduit Support Requirements

| Support Type | EMT | RNC (Sch 40) | FMC | NMC |
|-------------|-----|-------------|-----|-----|
| **Support intervals** | 10' | 3' | 4-1/2' | 4-1/2' |
| **Max distance from box to support** | 3' | 3' | 1' | 1' |

---

## Residential Code Compliance Checklist Items

The city's residential EV charging code compliance checklist verifies:

### Permit Submittal Requirements
- Completed Electrical Permit Application
- Manufacturer's specifications sheets and installation guidelines
- Schematic Site Plan (NOT required for single-family, duplex or ADU)
- Signed Electrical Plans (NOT required for single-family, duplex or ADU)
  - Single line diagram
  - Existing electrical service size and number of meters
  - Size, type, insulation ratings of all conductors
  - Type, size, material of raceways
  - Feeder or service load calculations for EVCS requiring >40A OCPD

### Code Requirements — Installation
1. **Separate Branch Circuit** — EV outlet must be on its own branch circuit with no other outlets (CEC §210.17)
2. **Disconnecting Means** — Required for EVSE rated >60A or >150V to ground; must be readily accessible and lockable in open position per CEC §110.25 (CEC §625.42)

### Code Requirements — EV Charging Equipment
3. **General** — All equipment/wiring per Article 625; flexible cords must be extra-hard usage type (CEC §511.10(B)(1))
4. **Connector Location** — No connector within a Class I location per 511.3 (CEC §511.10(B)(2))
5. **Plug Connections** — Overhead suspended cords: lowest sag point min 6" above floor (CEC §511.10(B)(3))

### Outdoor Installations
- Parked vehicle and ALL EVCS components must NOT be in Public Right of Way (on/over sidewalk) unless approved by Dept. of Public Works

### Statement of Compliance
- Applicant signs attestation that load calc per CEC 220.83(A) shows existing panel is adequate
- Voluntary compliance alternative — city recommends professional evaluation

---

## CalGreen EV Raceway Requirement (Ch. 14.86, §4.106.4.5)

> **Note**: This is a **local CalGreen amendment** adopted by Laguna Beach via §14.86.011, not the state CalGreen standard directly. It applies to **new construction and major remodels only** — NOT to standalone EV charger installations. A standalone EV charger permit does not trigger this raceway requirement.

For **new dwellings** and **existing dwellings approved for major remodel**:

- Must install a **listed raceway** (trade size 1 / nominal 1" inside diameter)
- Raceway runs from main service or subpanel to a listed cabinet/box near proposed EV charger location
- Raceways must be **continuous** at enclosed, inaccessible, or concealed areas
- Service panel must reserve capacity for a **40-ampere 208/240-volt** dedicated branch circuit
- Space reserved for branch circuit overcurrent protective device

This means new construction and major remodels in Laguna Beach are pre-wired for EV charging — the raceway is already in place, making future EV charger installation simpler.

---

## Key Differences: Laguna Beach Residential vs. Buena Park

| Item | Buena Park | Laguna Beach | Delta |
|------|-----------|--------------|-------|
| **Load calc worksheet** | City-specific with 10,000W threshold | City worksheet, standard NEC 220.83(A) | Similar format, standard NEC method |
| **Panel sizing table** | Same ranges | Same ranges | Matches |
| **Wire/conduit table** | Same values | Same values | Matches |
| **Site plan required** | Yes | NOT required for SFR/duplex/ADU | **Laguna Beach is less burdensome** |
| **Electrical plans** | Yes | NOT required for SFR/duplex/ADU | **Laguna Beach is less burdensome** |
| **Load calc trigger** | All installations | Only for EVCS requiring >40A OCPD | **Laguna Beach has higher threshold** |
