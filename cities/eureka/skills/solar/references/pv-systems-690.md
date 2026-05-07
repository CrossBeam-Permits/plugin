---
title: "CEC Article 690 -- Solar Photovoltaic (PV) Systems"
category: "Core PV Requirements"
relevance: "Every solar PV review"
key_code_sections: "CEC 690.1, 690.2, 690.4, 690.6, 690.7, 690.8, 690.9, 690.11, 690.12, 690.13, 690.15, 690.31, 690.33"
---

# CEC Article 690 -- Solar Photovoltaic (PV) Systems

Source: 2025 California Electrical Code (Title 24, Part 3), Article 690.

## Scope (690.1)

Applies to solar PV systems including array circuits, inverters, and controllers. Covers interactive (grid-tied), stand-alone, or both. AC or DC output. Does not cover large-scale PV supply stations (see Article 691).

## System Types (690.2, 690.6)

| Type | Definition | Key Rule |
|------|-----------|----------|
| **Microinverter** | Module-level DC-to-AC converter; DC input typically <80V | Output is inverter output circuit (AC) |
| **AC Module (ACM)** | Listed module with integral inverter; defined in CEC 690.2 | PV source circuit requirements do not apply; internal components (CEC 690.6) |
| **String Inverter** | Central inverter receiving series-connected module strings | Full Article 690 DC circuit requirements apply |
| **DC-to-DC Converter** | Optimizes module output before string inverter | Separate voltage/current calc rules (690.7(B), 690.8(A)(1)(b)) |

## General Requirements (690.4)

- **(A)** PV systems permitted to supply building in addition to other supplies
- **(B)** Electronic power converters, modules, combiners, PVRSE, PVHCE, PVHCS, charge controllers shall be **listed** or field-evaluated and labeled
- **(C)** Installation by **qualified persons only** (CEC 690.4(C), H&S Code 25916)
- **(D)** Multiple PV systems on one building: directory per 705.10 at each disconnect
- **(E)** PV equipment and disconnects **not permitted in bathrooms**
- **(F)** Electronic power converters permitted on roofs/non-readily-accessible locations

## Equipment Listing (690.4(B), CRC R329.3.1)

| Equipment | Required Listing Standard |
|-----------|--------------------------|
| PV Modules | UL 1703 or UL 61730-1 and -2 |
| Inverters | UL 1741 |
| Mounting Systems | UL 2703 |
| BIPV Roof Coverings | UL 7103 |
| PVHCS (Hazard Control) | UL 3741 |
| PV Wire | UL 4703 |
| ESS | UL 9540 |

---

## Maximum Voltage (690.7)

### General Rules
- Max voltage = highest voltage between any two circuit conductors or any conductor and ground
- **1- and 2-family dwellings: 600V DC maximum** (690.7 item 2)
- Systems on/in buildings: 1000V DC maximum (690.7 item 1)

### Calculation Methods (690.7(A))
For PV source circuits, calculate using one of:
1. Sum of module Voc x temperature coefficient per manufacturer instructions
2. Sum of module Voc x correction factor from **Table 690.7(A)** (crystalline/multicrystalline silicon)
3. For >=100 kW: documented stamped design by licensed PE

### Table 690.7(A) -- Voltage Correction Factors

| Ambient Temp (C) | Factor | Ambient Temp (F) |
|-------------------|--------|-------------------|
| 24 to 20 | 1.02 | 76 to 68 |
| 19 to 15 | 1.04 | 67 to 59 |
| 14 to 10 | 1.06 | 58 to 50 |
| 9 to 5 | 1.08 | 49 to 41 |
| 4 to 0 | 1.10 | 40 to 32 |
| -1 to -5 | 1.12 | 31 to 23 |
| -6 to -10 | 1.14 | 22 to 14 |
| -11 to -15 | 1.16 | 13 to 5 |
| -16 to -20 | 1.18 | 4 to -4 |
| -21 to -25 | 1.20 | -5 to -13 |
| -26 to -30 | 1.21 | -14 to -22 |
| -31 to -35 | 1.23 | -23 to -31 |
| -36 to -40 | 1.25 | -32 to -40 |

**How to use**: Adjusted Voc = Module Voc(STC) x Number of modules in series x Correction Factor. Result must be <= 600V for residential.

**For microinverters**: Max DC input voltage is typically <=79V per module. Verify module Voc(STC) x correction factor does not exceed microinverter max DC input rating.

### Marking (690.7(D))
Permanent, readily visible label showing highest maximum DC voltage at one of:
1. DC PV system disconnecting means
2. PV electronic power conversion equipment
3. Distribution equipment associated with PV system

---

## Circuit Sizing and Current (690.8)

### Maximum Current Calculation (690.8(A))

| Circuit Type | Maximum Current Formula |
|-------------|------------------------|
| PV source circuit | Sum of parallel module Isc x 125% |
| DC-to-DC converter circuit | Sum of parallel converter continuous output current ratings |
| Inverter output circuit | Inverter continuous output current rating |

### Conductor Ampacity (690.8(B))
Conductors sized to the **larger** of:
1. Max current (690.8(A)) x **125%** -- without adjustment/correction factors
2. Max current (690.8(A)) -- with adjustment and correction factors applied

**Exception**: Equipment listed for 100% continuous operation may use 100% rating.

### Multiple String Circuits (690.8(D))
Where OCPD protects multiple parallel-connected PV strings, each conductor ampacity >= OCPD rating + sum of max currents of other parallel strings.

---

## Overcurrent Protection (690.9)

### General (690.9(A))
PV DC circuits and inverter output conductors shall be protected against overcurrent.

**Exceptions where OCPD not required (690.9(A)(1))**:
1. Conductors have ampacity for max circuit current, AND
2. Currents from all sources <= max OCPD rating of module or electronic power converter

### Device Ratings (690.9(B))
- OCPD rated >= **125% of max current** per 690.8(A)
- May round up to next standard size per 240.4(B)
- OCPDs in PV source circuits shall be **listed for use in PV systems**
- Electronic backfeed prevention devices permitted as overcurrent protection on PV array side

### DC Circuit OCPD (690.9(C))
- Single OCPD may protect modules, converters, and conductors of each circuit
- All OCPDs in same polarity for all circuits within a PV system
- Accessible but not required to be readily accessible

---

## Arc-Fault Protection (690.11)

**Required for**: PV systems with DC circuits operating at **>=80V DC** between any two conductors.

**Protection**: Listed PV arc-fault circuit interrupter or equivalent system components. Must detect and interrupt arcing faults from failure in conductor continuity, connections, modules, or other components.

**Exceptions**:
1. PV DC circuits not on/in buildings, AND
2. Circuits in metal raceways, MC cable, or underground

---

## Rapid Shutdown (690.12)

**Applies to**: PV system circuits installed on or in buildings.

**Exceptions**:
1. Ground-mounted circuits entering buildings that solely house PV equipment
2. Nonenclosed detached structures (carports, parking shades, solar trellises)

### Controlled Conductors (690.12(A))
1. PV system DC circuits
2. Inverter output circuits from inverters located within the array boundary

### Controlled Limits (690.12(B))

| Location | Requirement | Time |
|----------|-------------|------|
| **Outside array boundary** (>1 ft from array) | <=30V between any two conductors or any conductor and ground | Within 30 seconds of initiation |
| **Inside array boundary** | Option 1: PVHCS per UL 3741 listed for the installation | Per manufacturer instructions |
| **Inside array boundary** | Option 2: <=80V between any two conductors or any conductor and ground | Within 30 seconds of initiation |

**Array boundary** = 1 ft (305 mm) from the array in all directions.

### Initiation Device (690.12(C))
- **1- and 2-family dwellings**: at a readily accessible **outdoor** location
- Single PV system: operation of any single initiation device triggers shutdown
- May be: service disconnect, PV system disconnect, or labeled switch (on/off indicated)
- Multiple PV systems on one service: max 6 switches/breakers in single/grouped enclosures

### Building Labels (690.12(D))
Permanent label at each service equipment location:

> SOLAR PV SYSTEM IS EQUIPPED WITH RAPID SHUTDOWN.
> TURN RAPID SHUTDOWN SWITCH TO THE "OFF" POSITION TO SHUT DOWN
> PV SYSTEM AND REDUCE SHOCK HAZARD IN ARRAY.

- Title in capitals, minimum 3/8" (9.5 mm) height
- All text legible, contrasting background
- Include simple diagram of building with roof

### Rapid Shutdown Switch Label (690.12(D)(2))
Label on or within 3 ft of switch:

> RAPID SHUTDOWN SWITCH FOR SOLAR PV SYSTEM

- Reflective, all capitals, minimum 3/8" height, white on red background

---

## Disconnecting Means (690.13)

### PV System Disconnect
- Required to disconnect PV from all wiring systems (power, ESS, utilization equipment)
- **Readily accessible** location (690.13(A)(1))
- Enclosure doors exposing energized parts at >30V: **locked or tool-required** (690.13(A)(2))
- Marked **"PV SYSTEM DISCONNECT"** with open/closed indication (690.13(B))
- If line/load terminals energized in open position: warning label required (690.13(B))
- **Max 6 disconnects** per PV system, grouped in single/grouped enclosures (690.13(C))
- Ratings sufficient for max circuit current, available fault current, voltage (690.13(D))
- Capable of being **locked in accordance with 110.25** (690.13(E))

### Equipment Disconnect (690.15)
- Required for: AC modules, fuses, DC-to-DC converters, inverters, charge controllers
- Types: equipment disconnect per 690.15(C), listed isolating device, or isolating device for <=30A circuits
- Isolating devices marked "Do Not Disconnect Under Load" if not rated for interrupting
- Location: within equipment, within sight/10 ft, or lockable

---

## Wiring Methods (690.31)

### Readily Accessible Locations (690.31(A)(2))
PV DC circuits >30V in readily accessible locations to unqualified persons: MC cable, multiconductor jacketed cable, or raceway required.

### PV Wire Ampacity (690.31(A)(3))
105C and 125C conductor ampacities per Table 690.31(A)(3)(1). Correction factors per Table 690.31(A)(3)(2) for ambient >30C.

### Conductor Separation (690.31(B)(1))
PV DC circuits shall not occupy same enclosure, cable, or raceway as non-PV circuits unless separated by barrier.

### DC Conductor Identification (690.31(B)(2))
- Identified at all termination, connection, splice points
- Positive: imprinted "+" or "POSITIVE" or "POS" -- not green, white, or gray
- Negative: imprinted "-" or "NEGATIVE" or "NEG" -- not green, white, gray, or red
- White wire only for solidly grounded systems

### DC Circuits Inside Buildings (690.31(D))
PV DC circuits >30V or >8A inside buildings:
- **Metal raceways**, MC cable per 250.118(A)(10)(b)/(c), or **metal enclosures**
- Exception: PVHCS per 690.12(B)(2)(1) may use nonmetallic

### DC Circuit Marking/Labeling (690.31(D)(2))
Raceways, cable trays, pull box covers, unused conduit bodies marked:

> PHOTOVOLTAIC POWER SOURCE

or

> SOLAR PV DC CIRCUIT

- All capitals, minimum **3/8" (9.5 mm) height**
- **White on red** background
- Visible after installation
- Every section separated by enclosures/walls/partitions/ceilings/floors
- Spacing between labels: **not more than 10 ft (3 m)**
- Labels suitable for installed environment

---

## Mating Connectors (690.33)

- **Polarized** and non-interchangeable with other receptacles (690.33(A))
- **Latching or locking** type (690.33(C))
- Readily accessible connectors at >30V DC or >15V AC: require tool to open
- If not rated for interrupting current: marked "Do Not Disconnect Under Load" (690.33(D)(2))
- Different brand connectors: must be listed and identified for intermatability
