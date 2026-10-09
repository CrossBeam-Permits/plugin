---
title: "CEC Article 230 — Service Entrance Requirements for Panel Upgrades"
category: "Service Entrance"
relevance: "Every panel upgrade review — service sizing, disconnect, location, working clearance"
key_code_sections: "CEC 110.26, 230.42, 230.70, 230.71, 230.79, 230.85, 230.90, 240.24"
---

# CEC Article 230 — Service Entrance Requirements

Source: 2025 California Electrical Code (Title 24, Part 3), Articles 110, 230, and 240.

These are the core service entrance requirements that apply to every residential panel upgrade.

---

## 230.79 — Minimum Service Disconnect Rating

The service disconnect must be rated not less than the calculated load. Absolute minimums:

| Installation Type | Minimum Rating |
|------------------|---------------|
| One-circuit installations | 15A |
| Two-circuit installations | 30A |
| **One-family dwelling** | **100A, 3-wire** |
| All other installations | 60A |

A single-family home can never go below 100A service. Common upgrade targets:

| Target Size | Typical Use Case |
|------------|------------------|
| 100A | Minimum code. Small home, gas appliances, no major electrical loads. |
| 125A | Moderate loads. Gas heating, electric dryer, small A/C. |
| 150A | Growing loads. Electric water heater, larger A/C. |
| 200A | **Most common upgrade target.** Accommodates EV charger, heat pump, modern appliance loads. |
| 225A | High-demand home. Multiple high-draw appliances, EV, pool/spa. |
| 320A | Large home or heavy loads. Dual EV, all-electric, pool + spa. |
| 400A | Maximum typical residential. Often requires CT (current transformer) metering. |

---

## 230.42 — Service-Entrance Conductor Sizing

Service-entrance conductors shall have ampacity not less than the maximum load to be served, determined per Article 220. They must also be sized not less than the minimum service disconnect rating per 230.79.

### Conductor Sizing Table (Service Entrance)

Based on CEC Table 310.16 (75C column, which governs most residential terminations):

| Service Size | Min. Copper Conductor | Min. Aluminum Conductor |
|-------------|----------------------|------------------------|
| 100A | #4 AWG (85A at 75C) | #2 AWG (90A at 75C) |
| 125A | #2 AWG (115A at 75C) | #1/0 AWG (120A at 75C) |
| 150A | #1 AWG (130A at 75C) | #2/0 AWG (135A at 75C) |
| 200A | #2/0 AWG (175A at 75C) | #4/0 AWG (205A at 75C) |
| 225A | #3/0 AWG (200A at 75C) | 250 kcmil (255A at 75C) |
| 320A | 350 kcmil (310A at 75C) | 500 kcmil (380A at 75C) |
| 400A | 500 kcmil (380A at 75C) | 750 kcmil (490A at 75C) |

**Important**: Most residential service equipment has 75C-rated terminations. Per CEC 110.14(C), conductor ampacity is limited by the lowest-rated termination, even if the wire insulation is rated higher. Use the 75C column for sizing.

---

## 230.71 — Maximum Number of Disconnects

Each service shall have only one disconnecting means, unless the service consists of not more than six switches or sets of circuit breakers grouped in a single enclosure or group of separate enclosures (the "six-throw rule").

In practice: most modern residential panel upgrades use a **single main breaker** as the service disconnect. If the existing installation uses fused disconnects or multiple mains, the upgrade should consolidate to a single main breaker.

---

## 230.85 — Emergency Disconnect (2025 CEC)

**This is new in the 2025 code cycle and catches many contractors off guard.**

For all 1- and 2-family dwelling units, an emergency disconnecting means must be installed:

### Location Requirements
- Readily accessible **outdoor** location
- At a height not exceeding 2.0 m (6 ft 7 in) measured to the center of the operating handle (when in highest position)

### Marking Requirements
The emergency disconnect must be marked:
- "EMERGENCY DISCONNECT" in all caps
- Additional marking depends on type (service disconnect, meter disconnect, or other listed disconnect)
- Letters not less than 12.7 mm (1/2 in) high, in a color contrasting with the background

### Types of Emergency Disconnect
One of the following qualifies:
1. **Service disconnect** — the main breaker itself, if located outdoors
2. **Meter disconnect** — integral to the meter mounting equipment, installed per 230.82
3. **Other listed disconnect** — a separate switch or breaker on the supply side of the service disconnect, marked suitable for use as service equipment

### What This Means for Panel Upgrades
- If the panel is **indoors**: an outdoor emergency disconnect must be added (or the meter disconnect qualifies if it meets 230.85)
- If the panel is **outdoors**: the main breaker can serve as both the service disconnect and emergency disconnect
- **Existing installations**: 230.85 applies when upgrading the service — it's triggered by the panel upgrade itself

---

## 230.70 — Service Disconnect Location

The service disconnect must be:
1. **Readily accessible** — no ladders, crawl spaces, or locked rooms
2. **Nearest the point of entrance** of the service conductors — at or near where the utility feed enters the building
3. **Marked** to indicate position (on/off)

### Outdoor vs. Indoor
- Outdoor panel: must have a weatherproof (NEMA 3R minimum) enclosure
- Indoor panel: service conductors from the meter to the panel must be as short as practical

---

## 230.90 — Overcurrent Protection

Each ungrounded service conductor must have overcurrent protection with a rating or setting not higher than the conductor ampacity. In practice: the main breaker rating must not exceed the ampacity of the service entrance conductors.

---

## 110.26 — Working Clearance

Working space about electrical equipment must be maintained for safe operation and maintenance.

### Minimum Working Space Dimensions

| Dimension | Requirement |
|-----------|-------------|
| **Depth** | 900 mm (3 ft) minimum from front of panel |
| **Width** | 762 mm (30 in) minimum, or width of equipment, whichever is greater |
| **Height** | 2.0 m (6 ft 7 in) from floor to ceiling/obstruction |

These are for Condition 1 (exposed live parts on one side, no live or grounded parts on the other), which is the typical residential panel situation (0-150V to ground).

### Common Violations
- Storage in front of panel (boxes, shelving, water heaters)
- Panel installed in a tight closet without sufficient depth
- Equipment or structures overhead reducing headroom

---

## 240.24 — Overcurrent Device Location (Panel Location Restrictions)

Overcurrent devices (including the main breaker/panel) must be:
- **Readily accessible** — not behind locked doors or above furniture
- **Not in the vicinity of easily ignitable material** (e.g., clothes closets)
- **Not in bathrooms** — overcurrent devices shall not be located in the vicinity of bathroom sinks or bathing areas

### Prohibited Locations
- Bathrooms
- Clothes closets
- Over steps of a stairway

### Permitted Locations (Common Residential)
- Garage (most common for upgrades)
- Exterior wall (with weatherproof enclosure)
- Utility room / laundry room
- Hallway
- Basement

---

## California Fire and Electrical Codes — Panel Access and Marking (CFC 603; CEC 110, 230, 240, 408)

The California Fire Code (Title 24, Part 9) includes requirements for electrical panels that apply statewide. These are commonly cited alongside CEC requirements during panel upgrade inspections.

### CEC 110.21 — Marking and Labeling

CEC 110.21(A) requires electrical equipment to bear the manufacturer's name,
trademark, or another descriptive marking that identifies the organization
responsible for the product. Voltage, current, wattage, and other ratings are
marked when another CEC provision requires them. Equipment markings must be
sufficiently durable for the environment involved.

When the CEC requires a field-applied caution, warning, or danger marking,
110.21(B) requires an effective hazard marking that is durable for the
environment and permanently affixed. It cannot be handwritten except for
legible variable information. Section 110.21 does not independently require
every panel to display every possible rating or require reflective and
weather-resistant label material.

### CEC 408.4 / CFC 603.4 — Circuit Directory and Access

- Panels shall include a circuit directory identifying each circuit's purpose, location, and specific loads
- **Clear access** shall be maintained to panels at all times
- Panels shall not be blocked or obstructed by storage, equipment, or building elements

### CEC 110.27(B), 110.28 — Enclosures

Electrical panels and equipment must be housed in appropriate enclosures rated for the type of installation and environmental conditions, including protection from moisture, dust, and physical damage.

### CEC 110.27(B) — Physical Damage Protection

Electrical equipment shall be protected against physical damage, including installation of guards, barriers, or enclosures where necessary.

### CEC 110.25, 230.85(E) — Lockable Panels and Disconnects

- CEC 110.25 applies **when another CEC provision requires a disconnecting
  means to be lockable open**. In that case, it must be capable of being locked
  in the open position, and the locking provision must remain in place with or
  without the lock installed.
- CEC 230.85 separately requires an outdoor emergency disconnect for one- and
  two-family dwelling units, subject to its stated scope and exceptions.
  Section 230.85(E) requires the exact marking applicable to the disconnect
  type: `EMERGENCY DISCONNECT, SERVICE DISCONNECT`; `EMERGENCY DISCONNECT,
  METER DISCONNECT, NOT SERVICE EQUIPMENT`; or `EMERGENCY DISCONNECT, NOT
  SERVICE EQUIPMENT`. The marking must be on the outside front of the
  enclosure, with a red background, white text, and letters at least 1/2 inch
  high.

### CEC 110.22, 240.24, 408.4 — Residential Occupancies

In Group R (residential) occupancies, electrical panels and disconnects must be in **readily accessible locations** and properly labeled to indicate purpose and areas served.

### CEC 230.85 — Dwelling Emergency Disconnect Access

For a one- or two-family dwelling within the scope of 230.85, install the
emergency disconnect in a readily accessible outdoor location on or within
sight of the dwelling and apply the exact 230.85(E) marking for the selected
disconnect type. Do not infer from 110.25 that every panel or disconnect must
be lockable, or from 230.85(E) that locking a device creates an emergency
disconnect.

---

## Utility Coordination Notes

While not part of the CEC, utility coordination is a practical requirement for panel upgrades:

- **Southern California Edison (SCE)**: Must be notified for any service size change. SCE may need to upgrade the meter base, service drop, or transformer.
- **Permit vs. utility**: The city permit covers the customer side (panel, conductors, grounding). The utility side (meter, service drop, transformer) is handled separately through SCE.
- **Meter base**: Most panel upgrades also require a new meter base (or meter-main combo). The meter base is typically provided by or approved by the utility.
- **Timeline**: Utility-side work can take 2-6 weeks after the customer-side work is complete and inspected. Flag this for applicants.
