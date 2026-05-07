---
title: "CEC Article 705 -- Interconnected Electric Power Production Sources"
category: "Utility Interconnection"
relevance: "Every grid-tied solar review"
key_code_sections: "CEC 705.10, 705.11, 705.12, 705.13, 705.28, 705.30, 705.40"
---

# CEC Article 705 -- Interconnected Electric Power Production Sources

Source: 2025 California Electrical Code (Title 24, Part 3), Article 705.

## Scope (705.1)

Covers installation of one or more electric power production sources operating in parallel with a primary source of electricity (e.g., utility supply).

---

## Identification of Power Sources (705.10)

Permanent plaques, labels, or directories at each service equipment location:
1. Denote location of each power source disconnecting means
2. Indicate emergency telephone numbers of off-site service entities
3. Marked: **"CAUTION: MULTIPLE SOURCES OF POWER"** -- per 110.21(B)

**Exception**: Multiple colocated sources may be identified as a group.

---

## Supply-Side Connections (705.11)

### Connection Methods (705.11(A))
PV may connect to service by:
1. New service per 230.2(A)
2. Supply side of service disconnecting means per 230.82(6)
3. Additional service entrance conductors per 230.40, Exception No. 5

### Conductor Requirements (705.11(B))
- Ampacity >= sum of power source max circuit current per 705.28(A)
- Not smaller than **#6 AWG copper** or **#4 AWG aluminum**
- Sized per 705.28

### Service Disconnecting Means (705.11(D))
- Per Parts VI-VII of Article 230
- Disconnects all ungrounded conductors of power source from other systems

### Overcurrent Protection (705.11(F))
- Per Part VII of Article 230
- OCPD rating determines if ground-fault protection required per 230.95

---

## Load-Side Connections (705.12)

PV output may connect to load side of service disconnect at any distribution equipment. Where feeders or distribution equipment fed simultaneously by utility and PV:

### Feeder Connections (705.12(A))
1. Feeder ampacity >= **125% of power source output current**
2. If connection not at opposite end from primary source OCPD, load-side feeder must be protected by:
   - Feeder ampacity >= primary OCPD rating + 125% of PV output current, OR
   - OCPD at load side of connection rated <= feeder ampacity, OR
   - Tap rules per 240.21(B)(2) or (B)(4)

### Busbar Connections (705.12(B)) -- The Critical Rules

**Method 1 -- 100% Rule (705.12(B)(1))**:
Sum of (125% x PV output current) + main OCPD rating <= **100% of busbar rating**

No restriction on PV breaker location.

**Method 2 -- 120% Rule (705.12(B)(2))**:
Sum of (125% x PV output current) + main OCPD rating <= **120% of busbar rating**

Requirements:
- Two sources only (primary + one PV source)
- PV breaker at **opposite end** of busbar from main breaker/input feeder
- Busbar sized for connected loads per Article 220
- Permanent warning label adjacent to back-fed breaker:

> WARNING: POWER SOURCE OUTPUT DO NOT RELOCATE THIS OVERCURRENT DEVICE.

**Method 3 -- Sum of All OCPDs (705.12(B)(3))**:
Sum of ALL overcurrent devices (load + supply), EXCLUDING main breaker, <= busbar ampacity. Main breaker <= busbar rating.

**Method 4 -- Center-Fed Panelboards (705.12(B)(4))**:
For dwellings with center-fed panels, connection at either end permitted if:
Sum of (125% x PV output current) + main OCPD rating <= **120% of busbar rating**

### Quick Calculation -- 120% Rule

```
Max PV OCPD = (Busbar Rating x 1.20) - Main OCPD Rating
```

| Busbar (A) | Main (A) | Max PV OCPD (A) |
|------------|----------|-----------------|
| 100 | 100 | 20 |
| 125 | 100 | 50 |
| 125 | 125 | 25 |
| 200 | 150 | 90 |
| 200 | 175 | 65 |
| 200 | 200 | 40 |
| 225 | 175 | 95 |
| 225 | 200 | 70 |
| 225 | 225 | 45 |

*Standard plans typically limit system size to <=10 kW and OCPD to <=60A.*

---

## Energy Management Systems (705.13)

An EMS per 750.30 may limit current and loading on busbars and conductors from interconnected power sources. This can allow larger PV systems on smaller services.

---

## Source Disconnecting Means (705.20)

Disconnect requirements:
1. Manually operable switch/breaker, load-break pull-out, power-operated/remote switch (opens on control power loss), or listed device
2. Simultaneously disconnect all ungrounded conductors
3. **Readily accessible**
4. Externally operable without exposed live parts
5. Plainly indicates open/closed position
6. Rated for max circuit current, fault current, and voltage
7. If line/load terminals energized when open, warning label required

---

## Circuit Sizing and Current (705.28)

### Maximum Current (705.28(A))
1. Sum of continuous output current ratings at nominal system voltage
2. For EMS-controlled: EMS current setpoint
3. Combination of (1) and (2)

### Conductor Ampacity (705.28(B))
Not less than the larger of:
1. Max current x **125%** without adjustment/correction factors
2. Max current with adjustment/correction factors applied
3. If connected to feeders: sized per 240.21(B) tap rules

**Exception**: Equipment listed for 100% continuous operation may use 100%.

---

## Overcurrent Protection (705.30)

### Device Ratings (705.30(B))
- Rated >= **125% of max current** per 705.28(A)
- May round up per 240.4(B) and (C)
- Exception: 100% rated assemblies

### Suitable for Backfeed (705.30(D))
- Fused disconnects: suitable for backfeed unless otherwise marked
- Circuit breakers not marked "line"/"load": suitable for backfeed
- Circuit breakers marked "line"/"load": only if specifically rated for backfeed/reverse current

### Fastening (705.30(E))
Listed plug-in breakers backfed from listed interactive power sources: **additional fastener not required** (normally required by 408.36(D)).

---

## Loss of Primary Source / Anti-Islanding (705.40)

Interactive PV equipment shall:
- **Automatically disconnect** from all ungrounded conductors of primary source when any phase opens
- **Not reconnect** until all phases of primary source are restored
- Not applicable to emergency/legally required standby systems

**Exception**: Listed interactive inverters may cease exporting power (trip) rather than physically disconnect, and may automatically or manually resume export after all phases restored.

**Island mode**: Interactive PV equipment permitted to operate in island mode to supply loads that have been disconnected from the utility.

---

## Ground-Fault Protection (705.32)

Where ground-fault protection of equipment is installed in AC circuits:
- PV output shall connect to **supply side** of ground-fault protection
- **Exception**: Load-side connection permitted per 705.11 or where GFP covers all fault current sources
