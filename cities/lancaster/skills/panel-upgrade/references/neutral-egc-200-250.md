---
title: "CEC Articles 200 & 250 — Neutral Conductors, EGCs, and Conductor Identification"
category: "Neutral and EGC Requirements"
relevance: "Every panel upgrade review — neutral/ground separation, conductor identification, EGC sizing and types"
key_code_sections: "CEC 200.2(B), 200.4(A), 200.4(B), 200.6(A), 200.6(B), 200.7(A), 200.7(C), 240.22, 250.118, 250.119, 250.119(A), 250.120(A), 250.121, 250.122, 250.134(C), Table 250.122"
---

# CEC Articles 200 & 250 — Neutrals, EGCs, and Conductor Identification

Source: 2025 California Electrical Code (Title 24, Part 3), Articles 200 and 250.

Proper neutral and equipment grounding conductor (EGC) handling is one of the most critical aspects of a panel upgrade. When a panel is replaced, every conductor must be properly identified, terminated, and separated (in subpanels) or bonded (in service panels). These requirements are among the most commonly cited violations.

---

## Article 200 — Neutral (Grounded) Conductor Rules

### 200.2(B) — Neutral Continuity

The continuity of a grounded (neutral) conductor shall **not depend on the enclosure** it passes through. In practice: neutral conductors must be connected to terminal buses or spliced with wire connectors, not rely on contact with the metal enclosure for continuity.

### 200.4(A) — One Neutral Per Circuit

Each neutral conductor shall serve **only one branch circuit** or one multiwire branch circuit (MWBC). Sharing a neutral between two separate (non-MWBC) circuits is prohibited.

### 200.4(B) — Neutral Identification in Boxes

Where more than one neutral passes through a box, each neutral shall be **identified or grouped** with its associated ungrounded (hot) conductors. Methods:
- Wire ties or tape grouping at each box
- Cable assemblies that keep conductors together

### 200.4(B)(2) — Identification Without Loops or Splices

Each neutral shall be identified or grouped with its associated ungrounded conductors in a box **without requiring loops or splices** to determine which neutral belongs to which circuit.

---

## Neutral Conductor Identification (Color)

### 200.6(A) — Factory-Applied White or Gray

| Conductor Size | Identification Method |
|---------------|----------------------|
| **#6 AWG or smaller** | Must have **factory-applied** white or gray outer finish, or three continuous white or gray stripes along the entire length |
| **#4 AWG or larger** | May be identified with **white or gray tape** encircling the conductor at each accessible point (200.6(B)) |

### 200.7(A) — White Wire Restriction

A white or gray conductor shall **not be used** as an ungrounded (hot) conductor.

### 200.7(C) — Exception for Cable Assemblies

The white conductor of a cable assembly (e.g., NM cable) may be used as an ungrounded conductor if it is **re-identified** by taping or painting at each accessible point with a color other than white, gray, or green.

**Common violation**: Using the white wire of a 14/2 NM cable as a switch leg without re-identifying it.

---

## Overcurrent Protection and Neutrals

### 240.22 — No OCPD in Series with Neutral

Overcurrent devices (breakers, fuses) shall **not be connected in series with the neutral conductor** except:
1. Where the OCPD simultaneously opens all other conductors of the circuit
2. Where required for motor overload protection

This means: you cannot put a breaker on just the neutral. Multi-pole breakers that disconnect neutral and hot(s) simultaneously are acceptable.

---

## Equipment Grounding Conductors (EGCs)

### Types of EGCs (250.118)

| Type | CEC Section | Notes |
|------|-------------|-------|
| **Wire-type (copper, aluminum, copper-clad aluminum)** | 250.118(1) | Solid or stranded, bare, covered, or insulated |
| **Rigid metal conduit (RMC)** | 250.118(2) | Acceptable as EGC |
| **Intermediate metal conduit (IMC)** | 250.118(2) | Acceptable as EGC |
| **Electrical metallic tubing (EMT)** | 250.118(2) | Acceptable as EGC |
| **AC cable armor** | 250.118(2) | With listed fittings |
| **Flexible metal conduit (FMC)** | 250.118(5) | Max 20A OCPD, max 6 ft length, max 1-1/4" trade size |
| **Liquidtight flexible metal conduit (LFMC)** | 250.118(6) | Max 60A OCPD, 3/4" to 1-1/4" trade size |

### EGC Identification (250.119)

| Conductor Size | Identification Method |
|---------------|----------------------|
| **#6 AWG or smaller** | Factory-insulated with **green** or **green with yellow stripe** |
| **#4 AWG or larger** | Identified with **green tape or labels** encircling the conductor at each end and at every accessible point (250.119(A)) |

### 250.119 — Green is Reserved

Green (or green with yellow stripe) shall **never** be used for neutral or ungrounded (hot) conductors. This color is exclusively reserved for equipment grounding conductors.

---

## EGC Installation Requirements

### 250.120(A) — Fittings for Raceways as EGC

Raceways and cable armor used as EGCs shall have **approved fittings**; all joints, fittings, and connections shall be made tight.

### 250.121(A) — GEC Not to Be Used as EGC

A grounding electrode conductor (GEC) shall **not** be used as an equipment grounding conductor (EGC).

**Exception**: Where the GEC complies with both grounding and bonding requirements and carries no objectionable current.

### 250.121(B) — Building Steel Not as EGC

Metal building frames or structures shall **not** serve as equipment grounding conductors.

### 250.134(C) — EGC Must Run with Circuit Conductors

Equipment grounding conductors shall be installed in the same raceway, cable, or trench as the circuit conductors they serve.

**Exception**: Replacement of non-grounding type receptacles per 250.130(C).

---

## EGC Sizing (Table 250.122)

Size the EGC based on the **rating of the overcurrent device** (breaker) ahead of the equipment:

| OCPD Rating (Amps) | Min. EGC Size — Copper | Min. EGC Size — Aluminum |
|--------------------|----------------------|------------------------|
| 15 | #14 AWG | #12 AWG |
| 20 | #12 AWG | #10 AWG |
| 30 | #10 AWG | #8 AWG |
| 40 | #10 AWG | #8 AWG |
| 60 | #10 AWG | #8 AWG |
| 100 | #8 AWG | #6 AWG |
| 200 | #6 AWG | #4 AWG |
| 300 | #4 AWG | #2 AWG |
| 400 | #3 AWG | #1 AWG |

*Per CEC Table 250.122*

### 250.122(B) — Increased for Voltage Drop

Where ungrounded conductors are increased in size (e.g., for voltage drop), EGCs must be increased proportionally.

### 250.122(C) — Multiple Circuits in One Raceway

When multiple circuits share a raceway, a single EGC is acceptable if sized based on the **largest OCPD** of any circuit in the raceway.

---

## Neutral and Ground at Service vs. Subpanel

This is the single most important neutral/EGC distinction in a panel upgrade:

### Service Panel (250.24(B))

In the **service panel** (the first disconnecting means):
- Neutral, EGCs, and the enclosure **SHALL be bonded together**
- Main bonding jumper (green screw or strap) must be installed
- Neutral and ground buses may be on the same bar

### Subpanel (250.24(A)(5))

In a **subpanel** (any panel downstream of the service disconnect):
- Neutral and EGC buses **SHALL be separated** (isolated)
- The bonding jumper (green screw) must be **REMOVED**
- Ground wires go to the grounding bus (bonded to enclosure)
- Neutral wires go to the neutral bus (insulated from enclosure)

**Common panel upgrade scenario**: The old main panel becomes a subpanel when a new meter-main is installed outside. The bonding jumper must be removed from the old panel, and neutral/ground buses must be separated.

---

## Common Neutral/EGC Inspection Failures

1. **Neutral and ground on same terminal** — even in service panels, each wire needs its own terminal
2. **Bonding jumper left in subpanel** — neutral and ground improperly bonded downstream
3. **Missing bonding jumper in service panel** — neutral and ground not bonded at service
4. **White wire used as hot without re-identification** — no tape marking at accessible points
5. **Green wire used for neutral** — color code violation
6. **EGC undersized for breaker rating** — using #14 EGC on a 20A circuit
7. **Neutral shared between non-MWBC circuits** — two separate circuits sharing one neutral
8. **EGC not run with circuit conductors** — separate path from hot conductors
