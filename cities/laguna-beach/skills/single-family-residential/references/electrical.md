---
title: Electrical Requirements
category: electrical
relevance: high
key_code_sections:
  - CEC 210.8 (GFCI Protection)
  - CEC 210.12 (AFCI Protection)
  - CEC 210.52 (Receptacle Placement)
  - CEC 220.82 (Dwelling Unit Load Calculations)
  - CEC 230.2, 230.42, 230.70, 230.71, 230.72, 230.79, 230.85 (Services)
  - CEC 250.24, 250.50, 250.52, 250.53, 250.66 (Grounding and Bonding)
  - CRC R317.6 and CALGreen 4.106.4.1 (EV Charging Readiness)
  - CRC R338 (EV Charging Equipment / Ventilation Interface)
  - CRC R310 (Smoke Alarms)
  - CRC R311 (Carbon Monoxide Alarms)
---

# Electrical Requirements for Single-Family Residential

California Electrical Code (CEC), Title 24, Part 3 — 2025 Edition.
California Residential Code (CRC), Title 24, Part 2.5 — 2025 Edition.
This reference covers service sizing, load calculations, branch circuits,
receptacle placement, GFCI, AFCI, smoke/CO alarms, EV charging, grounding,
and panel requirements for single-family dwellings.

---

## 1. Service Sizing

### Minimum Service Size
- Minimum 100 amperes for single-family dwellings (CEC 230.79(C))
- A 200-ampere service may be a design/utility-coordination choice, but it is
  not a code recommendation triggered by a list of appliance types; use the
  calculated load and serving-utility requirements

### Service Entrance Conductors
- Shall have adequate ampacity for the computed load (CEC 230.42)
- Under the CEC 310.12(A) whole-load dwelling allowance, 100A uses 4 AWG copper
  or 2 AWG aluminum/copper-clad aluminum
- Under the same whole-load dwelling conditions, 200A uses 2/0 AWG copper or
  4/0 AWG aluminum/copper-clad aluminum; apply adjustment/correction rules
  where the allowance does not apply

### Number of Services
A building shall be supplied by only one service unless permitted by
exceptions in CEC 230.2 (e.g., fire pumps, emergency systems, capacity
requirements exceeding 2000A).

### Service Disconnecting Means
- One service disconnect is the default; two through six are permitted only in
  one of the equipment arrangements in CEC 230.71(B), grouped under CEC 230.72
- Readily accessible, generally at or near the point of service entrance
- Marked as suitable for use as service equipment

---

## 2. Load Calculation — Dwelling Unit Method

### Optional Calculation for Dwelling Units (CEC 220.82)
This method is permitted for a dwelling unit supplied by a single 3-wire,
120/240V or 208Y/120V service or feeder with ampacity at least 100A:

**Step 1 — General Loads (at 100%):**
- 3 VA per square foot of floor area for general lighting and receptacles
- 1500 VA for each 20A small-appliance branch circuit (minimum 2 required)
- 1500 VA for laundry branch circuit
- Nameplate loads for fastened/specific-circuit appliances, ranges/ovens/cooking
  units, clothes dryers, water heaters, and permanently connected motors

**Step 2 — Apply demand factor to general loads:**
- First 10 kVA at 100%
- Remainder at 40%

**Step 3 — Add largest of the following (CEC 220.82(C)):**
- Air conditioning load at 100%, OR
- Heat pump compressor at 100% where there is no supplemental electric heat, OR
- Heat pump compressor at 100% plus supplemental electric heat at 65%; omit the
  compressor where controls prevent simultaneous operation, OR
- 65% of electric space heating if fewer than 4 separately controlled units, OR
- 40% of electric space heating if 4 or more separately controlled units, OR
- Electric thermal-storage or other continuous heating at 100%

### Standard Calculation Method
The standard method may also be used and may be required for specific
situations. Key sections: 220.41 (dwelling lighting loads), 220.45 (demand factors),
220.54 (dryer loads), 220.55 (cooking equipment).

---

## 3. Branch Circuit Requirements

### Required Dedicated Circuits

| Circuit | Rating | Purpose | Code Section |
|---|---|---|---|
| Kitchen small appliance (2 minimum) | 20A | Countertop receptacles | CEC 210.11(C)(1) |
| Bathroom receptacle(s) | 20A | Bathroom receptacles | CEC 210.11(C)(3) |
| Laundry | 20A | Laundry area receptacle | CEC 210.11(C)(2) |
| Dishwasher / disposal | Per nameplate and listing | Follow manufacturer instructions and applicable load/GFCI rules; no categorical dedicated/shared configuration is asserted | Applicable branch-circuit provisions |
| Furnace/HVAC | Per equipment | Dedicated | CEC 422.12 |
| Fixed storage water heater <= 120 gal | Per equipment | Treat as 125% of nameplate under CEC 422.13; follow listing and applicable branch-circuit rules | CEC 422.13 |
| Garage/accessory building | 20A | At least one circuit, ordinarily with no other outlets; it may supply outdoor receptacles, and in a single-vehicle-bay garage may supply other equipment outlets permitted by 210.23(B) | CEC 210.11(C)(4) |

### General Lighting Branch Circuits
- 10A circuits under the restrictions of CEC 210.23(A), or 15A/20A circuits
  under 210.23(B)
- Minimum load allowance: 3 VA per square foot (CEC 220.41)
- Apply the required small-appliance and laundry circuit outlet limits and the
  bathroom single-bathroom exception; do not impose a blanket room-wide ban on
  shared lighting/receptacle circuits

---

## 4. Receptacle Placement

### General Receptacle Spacing — Habitable Rooms (CEC 210.52(A))
- No point along the floor line of any wall space shall be more than
  6 feet from a receptacle outlet
- Receptacles required in any wall space 2 feet or wider
- Floor receptacles within 18 inches of the wall count toward spacing
- Result: maximum 12 feet between receptacles along a wall

### Kitchen Countertop Receptacles (CEC 210.52(C))
- Receptacles required for each counter space 12 inches or wider
- No point along the wall line shall be more than 24 inches from a
  receptacle (measured horizontally), subject to the sink/range configuration
  and closest-practicable exceptions in 210.52(C)(1)
- Island and peninsula receptacles are optional; where none is installed,
  provision for a future receptacle is required. Installed units follow
  210.52(C)(3).
- All kitchen countertop receptacles served by 20A small-appliance circuits

### Bathroom Receptacles (CEC 210.52(D))
- At least one receptacle outlet within 36 inches of the outside edge
  of each basin
- May be on an adjacent wall/partition, on the countertop, or on the side/face
  of the sink cabinet, and no more than 12 inches below the sink/countertop top
- Served by a 20A branch circuit (may serve multiple bathroom receptacles
  but no other outlets), or use the single-bathroom exception subject to
  210.23(B) load conditions

### Hallway Receptacles (CEC 210.52(H))
- At least one receptacle in hallways 10 feet or longer

### Outdoor Receptacles (CEC 210.52(E))
- At least two receptacles — one each at front and back of dwelling
- Accessible from grade level, not more than 6-1/2 feet above grade
- A balcony, deck, or porch within 4 inches horizontally of the dwelling has
  at least one receptacle no more than 6-1/2 ft above its walking surface

### Garage Receptacles (CEC 210.52(G))
- At least one receptacle in each vehicle bay in attached and detached
  garages
- At least one receptacle in each accessory building with electric power

### Laundry Receptacle (CEC 210.52(F))
- At least one receptacle in the designated laundry area; the section does not
  impose a universal 6-ft equipment distance

---

## 5. GFCI Protection Locations

### Dwelling Unit GFCI Requirements (CEC 210.8(A))
All 125V through 250V receptacles supplied by single-phase branch circuits
rated 150V or less to ground shall have GFCI protection in:

| Location | Notes |
|---|---|
| Bathrooms | All receptacles |
| Garages and accessory buildings | Garages and qualifying nonhabitable rooms/areas at or below grade used for storage, work, or similar use |
| Outdoors | All outdoor receptacles |
| Crawl spaces | At or below grade |
| Basements | All receptacles |
| Kitchens | All receptacles |
| Areas with sinks and permanent food/beverage prep | All receptacles |
| Laundry areas | All receptacles |
| Sinks (other areas) | Within 6 ft of the top inside edge of the bowl |
| Boathouses | All receptacles |
| Bathtub/shower stall areas | Within 6 ft of the outside edge |
| Indoor damp/wet locations | All receptacles |

### Exceptions to GFCI (CEC 210.8(A))
- Receptacle not readily accessible and supplied by a branch circuit
  dedicated to electric snow-melting, deicing, or pipeline and vessel
  heating equipment — Exception 1
- Receptacle supplying only a permanently installed premises security
  system — Exception 2
- A listed weight-supporting attachment fitting/support-purpose ceiling
  receptacle with compatible equipment; any integral convenience receptacle
  remains within the limitation — Exception 3
- A factory-installed internal, not-readily-accessible receptacle in a listed
  bathroom exhaust fan installed to its instructions — Exception 4

### Crawl Space Lighting (CEC 210.8(C))
GFCI protection required for lighting outlets not exceeding 120V
installed in crawl spaces.

### Appliance GFCI (CEC 210.8(D))
GFCI required for branch circuit or outlet supplying (150V or less,
60A or less):
- Automotive vacuum machines, drinking water coolers,
  high-pressure spray washing machines
- Tire inflation devices, vending machines, sump pumps
- Dishwashers, electric ranges, wall-mounted ovens,
  counter-mounted cooking units
- Clothes dryers, microwave ovens

### Outdoor Outlets — Dwellings (CEC 210.8(F))
All outdoor outlets supplied by single-phase branch circuits rated 150V
or less to ground, 50A or less, shall have GFCI protection.

Exception: Listed HVAC equipment (expires September 1, 2026)
(CEC 210.8(F) Exception 2).

---

## 6. AFCI Protection

### Required Locations (CEC 210.12(B))
All 120V, single-phase, 10-, 15-, and 20-ampere branch circuits
supplying outlets or devices in the following locations shall be
AFCI protected:

| Location |
|---|
| Kitchens |
| Family rooms |
| Dining rooms |
| Living rooms |
| Parlors |
| Libraries |
| Dens |
| Bedrooms |
| Sunrooms |
| Recreation rooms |
| Closets |
| Hallways |
| Laundry areas |
| Similar rooms or areas |

### Implementation Methods (CEC 210.12(A))
1. Listed combination-type AFCI at the panel protecting entire circuit
2. Listed branch/feeder AFCI at origin + listed outlet branch-circuit
   AFCI at the first outlet
3. Listed supplemental arc protection breaker + outlet branch-circuit
   AFCI at the first outlet, with continuous wiring, maximum 50 ft for 14 AWG
   or 70 ft for 12 AWG, and required first-box marking
4. Outlet branch-circuit AFCI at first receptacle (with listed breaker
   and continuous wiring, the same conductor-length/first-box conditions,
   and identification as a system combination-type)
5. The exact permitted metal raceway/MC/AC cable, grounding, and metal-box
   conditions to the first outlet, then an outlet AFCI
6. The exact permitted raceway/cable and box/enclosure system encased in
   2 inches of concrete to the first outlet, then an outlet AFCI

### Exceptions
- Individual branch circuit for fire alarm system installed in metal
  raceway, MC or AC cable — Exception 1

### Modifications to Existing Circuits (CEC 210.12(E))
When branch-circuit wiring is modified, replaced, or extended in AFCI
areas, the branch circuit shall be protected by an AFCI.

Exception: Extensions of 6 feet or less, measured to the enclosure/cabinet/
junction-box rule in 210.12(E), with no additional outlets or devices other
than splicing devices.

---

## 7. Smoke and CO Alarm Circuits

### Smoke Alarms (CRC R310)
- Required in each sleeping room, outside each sleeping area, and on
  each story including basements and habitable attics, plus the other R310.3
  higher-ceiling and sleeping-loft locations
- In new construction, primary power from permanent building wiring with
  battery backup and no prohibited disconnect; apply all R310.6 existing- and
  limited-work exceptions
- Where more than one is required, interconnected so activation of one triggers
  all alarms, subject to all four R310.4 existing- and limited-work exceptions

### Carbon Monoxide Alarms (CRC R311)
- Required in dwelling units with a fuel-fired appliance or fireplace, or an
  attached garage with an opening communicating with the dwelling
- Located outside each sleeping area in the immediate vicinity
- May be combined smoke/CO units
- In new construction, primary power from permanent building wiring with
  battery backup, subject to the R311.6 exceptions
- Where more than one CO alarm is required, the CO alarms interconnect with
  each other, subject to the R311.5 exceptions

### Circuit Requirements
Where permanent wiring applies, smoke and CO alarms shall have no disconnecting
switch other than overcurrent protection under CRC R310.6/R311.6. Treat any
shared-circuit configuration as design practice unless an exact governing
provision is identified.

---

## 8. EV Charging Readiness (CRC R317.6 / CALGreen 4.106.4)

### Requirement for New Single-Family Dwellings
Each dwelling unit with an attached private garage shall install one of
the following (CALGreen 4.106.4.1):

**Option A — EV Capable (raceway only):**
- Listed raceway, trade size 1 (nominal 1-inch ID) minimum
- From main service or subpanel to a listed cabinet/box near the
  proposed EV charger location
- Raceway continuous at concealed/inaccessible areas
- Panel shall have capacity for a 40A, 208/240V dedicated branch circuit
- Reserved space for overcurrent protective device

**Option B — EV Ready (circuit installed):**
- Minimum 40A, 208/240V dedicated branch circuit installed to the
  proposed EV charger location

### Labeling
- Panel circuit directory: label reserved space "EV CAPABLE"
- Raceway termination: permanently and visibly marked "EV CAPABLE"
  (CALGreen 4.106.4.1.1)

### Exceptions
- ADUs and JADUs without additional parking are exempt
- Where the local enforcing agency determines EV infrastructure is
  not feasible (no utility power, adverse cost impact)

### Ventilation (CRC R338.3)
Mechanical exhaust ventilation per CEC Article 625 or CBC Section 1203,
whichever is greater, when required. Ventilation interlocked with
charging equipment (CRC R338.4).

---

## 9. Grounding Electrode System

### Required Grounding Electrodes (CEC 250.50)
All grounding electrodes present at a new building shall be bonded together.
At an existing building, apply the inaccessible-concrete-encased-electrode
exception in CEC 250.50:
- Metal underground water pipe with at least 10 ft direct earth contact and
  continuity to the connection points (250.52(A)(1))
- One or more metal in-ground support structures with at least 10 ft vertical
  direct earth contact (250.52(A)(2))
- Concrete-encased electrode (Ufer ground): 20 ft of 4 AWG copper or
  1/2 inch rebar in concrete footing (250.52(A)(3))
- Ground ring: 2 AWG bare copper encircling building (250.52(A)(4))

### Supplemental Electrode
If the only electrode is a water pipe, a supplemental electrode is
required (CEC 250.53(D)(2)). Concrete-encased electrodes and ground
rings do not require supplementation.

### Grounding Electrode Conductor Sizing (CEC 250.66)
| Service Conductor Size (Cu) | GEC Size (Cu) |
|---|---|
| 2 AWG or smaller | 8 AWG |
| 1 AWG or 1/0 AWG | 6 AWG |
| 2/0 AWG or 3/0 AWG | 4 AWG |
| Over 3/0 AWG through 350 kcmil | 2 AWG |

### Bonding
The bonding jumper connecting the grounded (neutral) conductor to the
equipment grounding conductor shall be installed at the service equipment
only. Downstream panels shall keep neutral and ground separate (CEC 250.24).

---

## 10. Panel Location and Clearance

### Working Space (CEC 110.26)
- Depth: 36 inches minimum in front of the panel
- Width: 30 inches minimum (or width of equipment, whichever is greater)
- Height: normally 6-1/2 feet minimum (or equipment height, whichever is
  greater); apply the existing-dwelling service equipment/enclosed-panelboard
  exception for equipment not over 200A and any other applicable specialized exception
- Clear and unobstructed at all times

### Panel Height
- Maximum mounting height for the highest overcurrent device operating
  handle: 6 feet 7 inches above floor or working platform, subject to the
  listed exceptions (CEC 240.24(A))

### Indoor vs Outdoor
Panels may be installed indoors or outdoors. When installed outdoors,
they shall have a weatherproof enclosure selected for the actual condition
under CEC 312.2 and Table 110.28. Type 3R is a common rainproof selection, not
a universal minimum for every outdoor condition.

### Dedicated Equipment Space
Indoor dedicated electrical space occupies the equipment width/depth footprint
from the floor to 6 ft above the equipment or the structural ceiling, whichever
is lower (CEC 110.26(E)). Removable suspended ceilings are permitted. Foreign
systems above that zone require protection from condensation, leaks, or breaks.

---

## Key Code Sections

- **CEC 210.8** — GFCI protection locations and requirements
- **CEC 210.12** — AFCI protection locations and methods
- **CEC 210.52** — Receptacle outlet placement (walls, counters, outdoor, garage)
- **CEC 220.82** — Optional dwelling unit load calculation method
- **CEC 230** — Services (sizing, disconnecting means, number of services)
- **CEC 250** — Grounding and bonding (electrodes, conductor sizing)
- **CEC 110.26** — Working space around electrical equipment
- **CRC R310** — Smoke alarms (locations, power source, interconnection)
- **CRC R311** — Carbon monoxide alarms
- **CRC R317.6 / CALGreen 4.106.4** — Electric vehicle charging infrastructure
- **CRC R338** — Electric vehicle charging equipment, ventilation, and electrical interface
- **CALGreen 4.106.4** — EV charging infrastructure requirements

## Cross-References

- [energy.md](energy.md) — PV system electrical, battery storage ready
- [calgreen-mandatory.md](calgreen-mandatory.md) — EV charging infrastructure (4.106.4)
- [mechanical-hvac.md](mechanical-hvac.md) — HVAC equipment circuits, combustion air
- [plumbing.md](plumbing.md) — Electric water heater circuits
