---
title: "CEC Article 625 — Electric Vehicle Power Transfer System"
category: "Core EV Requirements"
relevance: "Every EV charger review"
key_code_sections: "CEC 625.1, 625.1.1, 625.6, 625.40, 625.41, 625.42, 625.43, 625.44, 625.50, 625.52, 625.54"
---

# CEC Article 625 — Electric Vehicle Power Transfer System

Source: 2025 California Electrical Code (Title 24, Part 3), Article 625.

## Scope (625.1)

Covers electrical conductors and equipment connecting an electric vehicle to premises wiring for charging, power export, or bidirectional current flow.

## California Amendment — New Construction (625.1.1)

In addition to Article 625, electric vehicle charging in new construction shall comply with the California Green Building Standards Code (CALGreen) Chapter 4, Division 4.1 and Chapter 5, Division 5.1.

> This is a California-specific requirement not in the base NEC.

## Listed Equipment (625.6)

All electric vehicle power transfer system equipment for charging, power export, or bidirectional current flow **shall be listed** by a nationally recognized testing laboratory (e.g., UL).

## Voltages (625.4)

- Nominal AC system voltages: 120, 120/240, 208Y/120, 240, 480Y/277, 480, 600Y/347, 600, or 1000 volts
- DC system input voltages: up to 1000 volts

---

## Branch Circuit Requirements

### Individual Branch Circuit (625.40)

Each outlet installed for supplying EVSE **greater than 16 amperes or 120 volts** shall be supplied by an **individual branch circuit** (no other outlets on the circuit).

**Exception**: Branch circuits may feed multiple EVSEs as permitted by 625.42(A) (Energy Management System) or 625.42(B) (adjustable settings).

### Overcurrent Protection (625.41)

Overcurrent protection for feeders and branch circuits supplying EVSE shall be:
- Sized for **continuous duty**
- Current rating **not less than 125% of maximum load** of the equipment
- Where noncontinuous loads also served from the same feeder: rating ≥ sum of noncontinuous loads + 125% of continuous loads

### Rating / Continuous Duty (625.42)

- EVSE shall have sufficient rating to supply the load served
- **Electric vehicle charging loads are considered continuous loads**
- Service and feeder sized per product ratings unless overall rating limited through controls

**625.42(A) — Energy Management System (EMS)**:
- Where EMS per 750.30 provides load management, the maximum equipment load on service and feeder is the maximum load permitted by the EMS
- EMS may be integral to one piece of equipment or a listed system of multiple pieces
- System must be marked to indicate load management control is provided

**625.42(B) — EVSE With Adjustable Settings**:
- EVSE with restricted-access ampere adjusting means per 750.30(C) is permitted
- Adjusted rating label must have sufficient durability for the environment
- EVSE ampere ratings may equal the adjusted current setting

---

## Disconnect Means (625.43)

For EVSE rated **more than 60 amperes** or **more than 150 volts to ground**:
- Disconnecting means **shall be provided**
- Installed in a **readily accessible location**
- If remote from equipment: a plaque denoting location shall be installed on the equipment
- Disconnecting means shall be **lockable in the open position** per 110.25

> For typical residential Level 2 chargers (≤60A), no separate disconnect is required — the circuit breaker in the panel serves as the disconnect.

---

## Equipment Connection Methods (625.44)

### Portable Equipment (625.44(A))

Connected via:
1. 2-pole, 3-wire grounding receptacle: 125V, 15 or 20A
2. 2-pole, 3-wire grounding receptacle: 250V, 15 or 20A
3. 2-pole, 3-wire or 3-pole, 4-wire grounding receptacle: 250V, 30 or 50A; or 125/250V, 30, 50, or 60A
4. 2-pole, 3-wire grounding receptacle: ≤60V DC, 15 or 20A

### Fastened-in-Place Equipment (625.44(B))

Connected via:
1. 2-pole, 3-wire grounding receptacle: 125V or 250V, up to 50A
2. 3-pole, 4-wire grounding receptacle: 250V 3-phase, up to 50A
3. 3-pole, 4-wire grounding receptacle: 125/250V single-phase, 30, 50, or 60A
4. 2-pole, 3-wire grounding receptacle: ≤60V DC, 15 or 20A

### Fixed-in-Place Equipment (625.44(C))

All other EVSE shall be **permanently wired** and fixed-in-place to the supporting surface.

---

## Equipment Location (625.50)

EVSE shall be located for direct electrical coupling of the EV connector. Unless specifically listed and marked otherwise, the coupling means shall be stored or located at a height of:

- **Indoor**: Not less than **450 mm (18 inches)** above floor level
- **Outdoor**: Not less than **600 mm (24 inches)** above grade level

**Exception**: Does not apply to portable EVSE per 625.44(A).

---

## Ventilation (625.52)

### Ventilation Not Required (625.52(A))

Mechanical ventilation is NOT required where:
- Electric vehicle storage batteries are used, OR
- Equipment is **listed for indoor charging without ventilation**

> Most modern EVs with lithium-ion batteries and listed Level 2 EVSE do NOT require ventilation. This requirement primarily applies to older lead-acid battery vehicles.

### Ventilation Required (625.52(B))

Where EVSE is listed for charging vehicles that require ventilation for indoor charging:
- **Mechanical ventilation (fan) shall be provided**
- Include both supply and exhaust equipment
- Permanently installed, intake from and vent directly to outdoors
- Supply circuit electrically interlocked with EVSE — remains energized during entire charging cycle

### California Amendment — Ventilation Marking (625.52(C))

EVSE listed/labeled as suitable for charging EVs that require ventilation shall be marked clearly: **"Ventilation Required"**. Marking shall be visible after installation.

### Ventilation Rate Table (625.52(B)(1))

For residential Level 2 (240V single-phase), minimum ventilation per vehicle:

| Ampere Rating | Cubic Feet per Minute (cfm) |
|--------------|---------------------------|
| 15A | 74 |
| 20A | 99 |
| 30A | 148 |
| 40A | 197 |
| 50A | 246 |
| 60A | 296 |
| 100A | 493 |

---

## GFCI Protection for Personnel (625.54)

**All receptacles installed for electric vehicle charging shall have GFCI protection for personnel.**

This is in addition to the location-based GFCI requirements in 210.8 (garages, outdoors). See `gfci-location.md` for the complete GFCI picture.

---

## Personnel Protection System (625.22)

- EVSE shall have a listed system of protection against electric shock
- For cord-and-plug-connected equipment: interrupting device required per 625.17(A)
- **Exception**: Not required for EVSE supplying less than 60 volts DC

---

## Cord and Cable Requirements (625.17)

### Power-Supply Cord (625.17(A))

- Portable EVSE with protection inside enclosure: cord ≤ 300 mm (12 in.)
- Portable EVSE with protection at plug: cord ≤ 4.6 m (15 ft)
- Fastened-in-place EVSE: cord ≤ 1.8 m (6 ft), installed at height preventing floor contact

### Output Cable to Vehicle (625.17(B))

Shall be listed Type EV, EVJ, EVE, EVT, or EVJT flexible cable, OR integral part of listed EVSE.

### Overall Length (625.17(C))

Maximum usable length: **7.5 m (25 ft)** unless equipped with a cable management system that is part of the listed EVSE.

---

## Loss of Primary Source (625.46)

Means shall be provided such that upon loss of utility voltage, energy cannot be back-fed through the EV and EVSE to premises wiring (unless permitted by 625.48 for interactive/bidirectional equipment).

## Interactive / Bidirectional Equipment (625.48)

EVSE incorporating power export (V2H, V2G) shall be listed and marked as suitable. Must comply with Article 702 (optional standby) or Article 705 (power production source) as applicable.
