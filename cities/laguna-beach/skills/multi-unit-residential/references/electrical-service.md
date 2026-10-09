---
title: "CEC 220/210/230 — Electrical Service Requirements for Multi-Unit Residential"
category: mep
relevance: "Multi-unit residential permit reviews requiring electrical service sizing, branch circuit verification, demand factor calculations, and metering configuration"
key_code_sections: "CEC 210.11(C), 210.25, 220.41, 220.45, 220.52, 220.53, 220.54, 220.55, 220.82, 220.84, 230.40, 230.42, 230.70, 230.71, 230.79, 230.90"
---

# Multi-Unit Residential Electrical Service Requirements

Source: 2025 California Electrical Code (Title 24, Part 3), Articles 210, 220, and 230.

This reference covers electrical service sizing, branch circuit requirements, load calculations, demand factors, metering, and service entrance requirements for multi-unit residential buildings (3+ dwelling units). It addresses both individual dwelling unit requirements and the building-level service calculation using CEC optional methods.

---

## 1. Individual Dwelling Unit Load Calculation (CEC 220.82)

Each dwelling unit's connected load must be calculated before applying building-level demand factors. CEC 220.82 provides the optional calculation method for dwelling units served by a single 120/240V or 208Y/120V 3-wire set of conductors with ampacity of 100A or greater `[CEC 220.82(A)]`.

### General Loads (220.82(B))

The general calculated load is: **100% of the first 10 kVA plus 40% of the remainder** of all the following loads combined:

| Load Type | How to Calculate | Code Reference |
|-----------|-----------------|----------------|
| General lighting & receptacles | 3 VA per sq ft of dwelling (outside dimensions, excluding open porches, garages, unfinished non-adaptable spaces) | `CEC 220.82(B)(1), 220.5(C)` |
| Small-appliance branch circuits | 1,500 VA per circuit (minimum 2 circuits required) | `CEC 220.82(B)(2), 210.11(C)(1)` |
| Laundry branch circuit | 1,500 VA per circuit | `CEC 220.82(B)(2), 210.11(C)(2)` |
| Fastened-in-place appliances | Nameplate rating | `CEC 220.82(B)(3)(a)` |
| Ranges, ovens, cooktops | Nameplate rating | `CEC 220.82(B)(3)(b)` |
| Clothes dryer | Nameplate rating | `CEC 220.82(B)(3)(c)` |
| Water heater | Nameplate rating | `CEC 220.82(B)(3)(d)` |
| Permanently connected motors | Nameplate ampere or kVA rating | `CEC 220.82(B)(4)` |

### Heating and Air-Conditioning Load (220.82(C))

Include the **largest** of the following six selections only:

1. 100% of air conditioning and cooling nameplate `[CEC 220.82(C)(1)]`
2. 100% of heat pump (without supplemental heating) `[CEC 220.82(C)(2)]`
3. 100% of heat pump compressor + 65% of supplemental electric heating `[CEC 220.82(C)(3)]`
4. 65% of electric space heating (fewer than 4 separately controlled units) `[CEC 220.82(C)(4)]`
5. 40% of electric space heating (4 or more separately controlled units) `[CEC 220.82(C)(5)]`
6. 100% of electric thermal storage (continuous load at full nameplate) `[CEC 220.82(C)(6)]`

**Total unit load = General Load result + Heating/AC selection.**

---

## 2. Multifamily Dwelling Demand Factors (CEC 220.84)

For buildings with **3 or more dwelling units**, the optional calculation in CEC 220.84 allows a significant demand factor reduction on the building service or main feeder. This is the primary method for sizing the building's total electrical service.

### Conditions for Use (220.84(A))

All three conditions must be met:
1. No dwelling unit is supplied by more than one feeder `[CEC 220.84(A)(1)]`
2. Each dwelling unit has electric cooking equipment `[CEC 220.84(A)(2)]`
3. Each dwelling unit has electric space heating or air conditioning (or both) `[CEC 220.84(A)(3)]`

**Exception**: When the Part III standard calculation for units WITHOUT electric cooking exceeds the Part IV optional calculation for identical units WITH electric cooking (at 8 kW per unit), the lesser load is permitted `[CEC 220.84(A), Exception]`.

### Demand Factor Table (Table 220.84(B))

| Number of Dwelling Units | Demand Factor (%) |
|--------------------------|-------------------|
| 3-5 | 45 |
| 6-7 | 44 |
| 8-10 | 43 |
| 11 | 42 |
| 12-13 | 41 |
| 14-15 | 40 |
| 16-17 | 39 |
| 18-20 | 38 |
| 21 | 37 |
| 22-23 | 36 |
| 24-25 | 35 |
| 26-27 | 34 |
| 28-30 | 33 |
| 31 | 32 |
| 32-33 | 31 |
| 34-36 | 30 |
| 37-38 | 29 |
| 39-42 | 28 |
| 43-45 | 27 |
| 46-50 | 26 |
| 51-55 | 25 |
| 56-61 | 24 |
| 62+ | 23 |

### Loads Included in the Demand Factor Calculation (220.84(C))

The connected load per unit to which the demand factor applies includes:

1. General lighting and receptacles: 3 VA/sq ft `[CEC 220.84(C)(1)]`
2. Small-appliance and laundry circuits: 1,500 VA each `[CEC 220.84(C)(2)]`
3. Nameplate ratings of all fastened-in-place appliances, ranges/ovens/cooktops, clothes dryers, water heaters `[CEC 220.84(C)(3)]`
4. All permanently connected motors `[CEC 220.84(C)(4)]`
5. The larger of air conditioning or fixed electric space heating `[CEC 220.84(C)(5)]`

### House Loads (220.84(B))

House loads (common area loads) are calculated separately using the **standard method (Part III)** and added to the dwelling unit demand calculation. House loads do NOT receive the Table 220.84(B) demand factor `[CEC 220.84(B)]`.

---

## 3. Additional Demand Factor Tables for Specific Loads

### Lighting Load Demand Factors (Table 220.45) — Dwelling Units

| Portion of Lighting Load | Demand Factor |
|--------------------------|---------------|
| First 3,000 VA | 100% |
| 3,001 to 120,000 VA | 35% |
| Over 120,000 VA | 25% |

These apply only when using the standard (Part III) calculation method, not the optional method of 220.82/220.84.

### Appliance Demand Factor (220.53)

A 75% demand factor is permitted for 4 or more fastened-in-place appliances rated 1/4 hp or greater, or 500W or greater, served by the same feeder or service in a multifamily dwelling. This does NOT apply to: cooking equipment, clothes dryers, space heating, air conditioning, or EVSE `[CEC 220.53]`.

### Electric Clothes Dryers (Table 220.54)

| Number of Dryers | Demand Factor (%) |
|------------------|-------------------|
| 1-4 | 100 |
| 5 | 85 |
| 6 | 75 |
| 7 | 65 |
| 8 | 60 |
| 9 | 55 |
| 10 | 50 |
| 11 | 47 |
| 12-23 | 47% minus 1% per dryer over 11 |
| 24-42 | 35% minus 0.5% per dryer over 23 |
| 43+ | 25 |

Load per dryer: 5,000W or nameplate, whichever is larger `[CEC 220.54]`.

### Electric Cooking Appliances (Table 220.55, Column C)

For appliances over 1-3/4 kW, not over 12 kW rating each:

| Number of Appliances | Max Demand (kW) |
|----------------------|-----------------|
| 1 | 8 |
| 2 | 11 |
| 3 | 14 |
| 5 | 20 |
| 10 | 25 |
| 15 | 30 |
| 20 | 35 |
| 25 | 40 |
| 26-30 | 15 kW + 1 kW per range |
| 31-40 | 15 kW + 1 kW per range |
| 41-50 | 25 kW + 3/4 kW per range |

For ranges over 12 kW through 27 kW, increase Column C values by 5% for each kW (or major fraction) over 12 kW `[Table 220.55, Note 1]`.

---

## 4. Required Branch Circuits Per Dwelling Unit (CEC 210.11(C))

Each dwelling unit requires these minimum dedicated branch circuits:

| Circuit Type | Min. Rating | Min. Quantity | Code Reference |
|--------------|-------------|---------------|----------------|
| General lighting | 15A or 20A | Per calculated load (3 VA/sq ft) | `CEC 210.11(A), 220.41` |
| Small-appliance (kitchen/dining) | 20A | 2 minimum | `CEC 210.11(C)(1)` |
| Laundry | 20A | 1 minimum (dedicated, no other outlets) | `CEC 210.11(C)(2)` |
| Bathroom receptacles | 20A | 1 minimum (dedicated) | `CEC 210.11(C)(3)` |
| Garage receptacles | 20A | 1 minimum (dedicated) | `CEC 210.11(C)(4)` |

**Additional dedicated circuits** are typically required for:
- Electric range/oven/cooktop: 40A or 50A individual branch circuit
- Electric dryer: 30A individual branch circuit
- Dishwasher: 20A individual branch circuit
- Garbage disposal: 20A individual branch circuit (may share with dishwasher in some jurisdictions)
- HVAC equipment: sized per equipment nameplate
- Water heater: sized per equipment nameplate
- EV charger: sized per EVSE rating `[CEC 220.57]`

### Branch Circuit Separation Between Units (210.25)

- Branch circuits in each dwelling unit shall supply ONLY loads within that unit `[CEC 210.25(A)]`
- Common area circuits (lobbies, corridors, stairways, laundry rooms, mechanical rooms, parking, elevators) must NOT be supplied from any individual dwelling unit's panel `[CEC 210.25(B)]`

### Laundry Exception for Multifamily

A laundry receptacle is not required in individual dwelling units of a multifamily building where laundry facilities are provided on the premises for all building occupants `[CEC 210.52(F), Exception No. 1]`. However, the 1,500 VA laundry circuit load is still included in the load calculation unless no laundry facilities are provided at all.

---

## 5. Service Entrance Requirements (CEC 230)

### Number of Services (230.2)

A building is generally supplied by only one service. Additional services are permitted for:
- Fire pumps, emergency systems, standby systems `[CEC 230.2(A)]`
- Multiple-occupancy buildings with no accessible space for shared service equipment (by special permission) `[CEC 230.2(B)]`
- Capacity requirements exceeding 2,000A at 1,000V or less `[CEC 230.2(C)]`
- Different voltages, frequencies, or phases `[CEC 230.2(D)]`

### Service-Entrance Conductor Sets (230.40)

For multifamily dwellings, multiple sets of service-entrance conductors are permitted from a single service drop or lateral:
- One set per occupancy or group of occupancies `[CEC 230.40, Exception No. 1]`
- Two to six disconnects grouped at one location from one service `[CEC 230.40, Exception No. 2]`
- One set to supply common area circuits per 210.25 `[CEC 230.40, Exception No. 4]`

### Main Service Disconnect (230.70, 230.71)

- Each service requires one disconnecting means, or up to six disconnects permitted `[CEC 230.71(B)]`
- Located at a readily accessible location, outside or inside nearest the point of entrance `[CEC 230.70(A)(1)]`
- Not installed in bathrooms `[CEC 230.70(A)(2)]`
- Must simultaneously disconnect all ungrounded conductors `[CEC 230.74]`
- Each occupant must have access to their service disconnecting means `[CEC 230.72(C)]`

**Exception**: In multiple-occupancy buildings where electrical maintenance is provided by building management under continuous supervision, service disconnecting means may be accessible to authorized management personnel only `[CEC 230.72(C), Exception]`.

### Service Conductor Sizing (230.42)

Service-entrance conductors must have ampacity not less than the maximum calculated load per Part III, IV, or V of Article 220. For continuous loads, ampacity must be at least the noncontinuous load plus 125% of the continuous load `[CEC 230.42(A)(1)]`.

### Minimum Service Disconnect Rating (230.79)

| Installation Type | Minimum Rating |
|-------------------|---------------|
| One-circuit installations | 15A |
| Two-circuit installations | 30A |
| One-family dwelling | 100A, 3-wire |
| **All other installations** | **60A** |

For multifamily buildings, the minimum is 60A per 230.79(D), but the calculated load will determine the actual required size, which is typically much larger.

### Overcurrent Protection (230.90)

Each ungrounded service conductor requires overload protection with a rating not higher than the conductor ampacity. Two to six circuit breakers or fuse sets are permitted as the overcurrent device, and their sum may exceed conductor ampacity if the calculated load does not `[CEC 230.90(A), Exception No. 3]`.

### Ground-Fault Protection of Equipment (230.95)

Required for solidly grounded wye services over 150V to ground, not exceeding 1,000V phase-to-phase, where the service disconnect is rated 1,000A or more. Maximum setting: 1,200A; maximum time delay: 1 second at 3,000A or greater `[CEC 230.95]`. Performance testing by a qualified person is required at initial installation.

### Surge Protection (230.67)

All services supplying dwelling units must have a Type 1 or Type 2 SPD with a nominal discharge current rating of at least 10 kA, integral to or immediately adjacent to the service equipment `[CEC 230.67]`.

---

## 6. Panel and Metering Requirements

### Individual Dwelling Unit Panels

- **Minimum 200A per dwelling unit** is typical for modern all-electric construction. CEC minimum for a one-family dwelling is 100A `[CEC 230.79(C)]`, but most multifamily projects use 200A per unit to accommodate electric cooking, HVAC, EV charging, and future electrification.
- Each unit panel must supply only loads within that unit `[CEC 210.25(A)]`.
- Panel must be in a readily accessible location within the unit, not in bathrooms `[CEC 230.70(A)]`.

### House Panel for Common Areas

- A separate "house panel" (or house meter/panel combination) must serve all common area loads `[CEC 210.25(B)]`.
- Common area loads include: corridor and stairway lighting, parking area lighting, elevator equipment, fire alarm systems, lobby and amenity space circuits, irrigation, exterior lighting, HVAC for common areas, laundry rooms, mechanical rooms, and trash compactors.
- House loads are calculated using the standard method (Part III of Article 220) and are added on top of the dwelling unit demand `[CEC 220.84(B)]`.

### Metering Configuration

- **Individual unit meters**: Each dwelling unit receives its own meter (or CT metering for larger services), typically in a common meter bank or meter room.
- **House meter**: A separate meter for common area loads, billed to the building owner/HOA.
- Meter sockets are listed and rated for the voltage and current but are not considered service equipment `[CEC 230.66(B)]`.
- For buildings with more than one service or combination of services, a permanent plaque or directory must be installed at each disconnect location identifying all other services and the areas served `[CEC 230.2(E)]`.

---

## 7. Worked Example: 35-Unit Apartment Building

**Assumptions** (typical mid-rise multifamily in California):
- 35 dwelling units, each 900 sq ft
- All-electric: electric range (12 kW), electric water heater (4,500W), electric dryer (5,000W), heat pump HVAC (5,000W), dishwasher (1,500W), garbage disposal (1,000W)
- Common areas: lobby, corridors, elevator, parking garage lighting, laundry room
- 120/208Y three-phase service

### Step 1: Calculate Connected Load Per Unit

| Load | VA |
|------|----|
| General lighting & receptacles: 900 sq ft x 3 VA | 2,700 |
| Small-appliance circuits: 2 x 1,500 | 3,000 |
| Laundry circuit | 1,500 |
| Electric range (nameplate) | 12,000 |
| Electric water heater | 4,500 |
| Electric clothes dryer | 5,000 |
| Dishwasher | 1,500 |
| Garbage disposal | 1,000 |
| Heat pump HVAC (larger of heating or cooling) | 5,000 |
| **Total connected load per unit** | **36,200** |

### Step 2: Apply Multifamily Demand Factor (Table 220.84(B))

For 35 units, the demand factor is **30%**.

```
Total dwelling unit demand = 35 units x 36,200 VA x 30%
                           = 35 x 36,200 x 0.30
                           = 380,100 VA
                           = 380.1 kVA
```

### Step 3: Calculate House Loads (Standard Method, Part III)

| Common Area Load | VA |
|------------------|----|
| Corridor/stairway lighting (estimate 5,000 sq ft x 1.5 VA) | 7,500 |
| Lobby/amenity (estimate 2,000 sq ft x 1.5 VA) | 3,000 |
| Parking garage lighting (estimate 15,000 sq ft x 0.3 VA) | 4,500 |
| Elevator (30 hp, ~25,000 VA) | 25,000 |
| Fire alarm and life safety | 5,000 |
| Laundry room (common, 10 machines) | 15,000 |
| Exterior/landscape lighting | 3,000 |
| Domestic water booster pump | 5,000 |
| Trash compactor | 3,000 |
| **Total house loads** | **71,000** |

Note: House loads are calculated at Part III demand factors. For simplicity, using 100% here as a conservative estimate. In practice, lighting demand factors from Table 220.45 may apply to the lighting portion.

### Step 4: Total Building Service Load

```
Total service load = Dwelling unit demand + House loads
                   = 380,100 + 71,000
                   = 451,100 VA
                   = 451.1 kVA
```

### Step 5: Determine Service Size

For a 120/208V three-phase service:

```
Service amperage = 451,100 VA / (208V x 1.732)
                 = 451,100 / 360.3
                 = 1,252 A
```

**Approximate service size: 1,200A to 1,600A, 120/208V 3-phase, 4-wire.**

A typical configuration for this building would be:
- Main switchboard rated 1,600A
- CT metering cabinet with 35 unit meters + 1 house meter
- Individual 200A panels in each dwelling unit
- House panel(s) for common areas

**Note**: At 1,000A or greater on a solidly grounded wye system, ground-fault protection of equipment is required per CEC 230.95. This building would require GFP on the main service disconnect.

---

## 8. EVSE Considerations for Multi-Unit Residential

Electric vehicle supply equipment load is calculated at 7,200 VA or nameplate rating, whichever is larger `[CEC 220.57]`. For multifamily buildings, EVSE loads can significantly increase the service size. Energy management systems (EMS) may be used to limit feeder or service current per CEC 220.70 and 750.30, allowing load management across multiple EVSE units without oversizing the service.

California requires EV-ready infrastructure in new multifamily construction (CALGreen). Coordinate EVSE load with the electrical engineer to determine whether managed charging (with EMS) or full-capacity wiring is specified.

---

## Cross-References

| Topic | Code Section | Notes |
|-------|-------------|-------|
| Floor area calculation | CEC 220.5(C) | Outside dimensions, exclude porches/garages/unfinished |
| Dwelling unit minimum lighting load | CEC 220.41 | 3 VA/sq ft for all dwelling types |
| Small-appliance circuits required | CEC 210.11(C)(1) | Min 2 x 20A circuits for kitchen/dining |
| Laundry circuit required | CEC 210.11(C)(2) | Min 1 x 20A dedicated circuit |
| Bathroom circuit required | CEC 210.11(C)(3) | Min 1 x 20A dedicated circuit |
| Garage circuit required | CEC 210.11(C)(4) | Min 1 x 20A dedicated circuit |
| Branch circuit separation | CEC 210.25 | Unit circuits serve only that unit; common areas separate |
| GFCI protection — dwelling units | CEC 210.8(A) | Bathrooms, kitchens, garages, outdoors, laundry, etc. |
| AFCI protection — dwelling units | CEC 210.12(B) | Kitchens, bedrooms, living areas, hallways, closets, laundry |
| Noncoincident loads | CEC 220.60 | Use larger of heating or A/C, not both |
| Neutral load calculation | CEC 220.61 | 70% reduction permitted for ranges/dryers/loads over 200A |
| Grounding electrode system | CEC 250.50 | Required at service entrance |
| GEC sizing | CEC 250.66, Table 250.66 | Based on service conductor size |
| Working clearance | CEC 110.26 | Min 36 in. deep, 30 in. wide, headroom per equipment rating |

## Key Code Sections

- **CEC 210.11(C)** -- Required branch circuits for dwelling units (small-appliance, laundry, bathroom, garage)
- **CEC 210.25** -- Branch circuit separation: unit circuits stay in unit, common areas on separate supply
- **CEC 220.41** -- Dwelling unit minimum lighting load: 3 VA/sq ft
- **CEC 220.45, Table 220.45** -- Lighting load demand factors for standard calculation
- **CEC 220.52** -- Small-appliance (1,500 VA each) and laundry (1,500 VA) loads
- **CEC 220.53** -- 75% demand for 4+ fastened-in-place appliances (excludes cooking, dryer, HVAC, EVSE)
- **CEC 220.54, Table 220.54** -- Electric clothes dryer demand factors
- **CEC 220.55, Table 220.55** -- Electric cooking appliance demand factors
- **CEC 220.82** -- Optional calculation for individual dwelling unit load
- **CEC 220.84, Table 220.84(B)** -- Optional calculation for multifamily dwelling service (3+ units)
- **CEC 230.2** -- Number of services permitted
- **CEC 230.40** -- Service-entrance conductor sets for multifamily buildings
- **CEC 230.42** -- Service conductor sizing (ampacity >= calculated load)
- **CEC 230.70** -- Service disconnect location (readily accessible, not in bathrooms)
- **CEC 230.71** -- Maximum number of disconnects (1, or 2-6 permitted)
- **CEC 230.72(C)** -- Each occupant must have access to their disconnect
- **CEC 230.79** -- Minimum service disconnect ratings
- **CEC 230.90** -- Service overcurrent protection requirements
- **CEC 230.95** -- Ground-fault protection of equipment (required at 1,000A+)
- **CEC 230.67** -- Surge protection required for dwelling unit services
