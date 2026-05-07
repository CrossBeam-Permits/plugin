---
title: "Conductors, Wiring Methods, and Neutral/EGC Identification"
category: "Wiring"
relevance: "Reviews involving conductor sizing, wiring methods, and conductor identification"
key_code_sections: "CEC 590.4(B), 590.4(C), 590.4(J), Table 310.16, Table 400.4, 400.5, 310.15, 200.6, 200.7, 250.119"
---

# Conductors, Wiring Methods, and Neutral/EGC Identification

Source: 2025 California Electrical Code (Title 24, Part 3), Articles 590, 310, 400, 200, 250.

---

## Temporary Wiring Methods Allowed (CEC 590.4)

Article 590 provides **relaxations** from permanent wiring requirements. All permanent wiring rules still apply except as specifically modified.

### Feeders (590.4(B))

| Wiring Method | Permitted? | Notes |
|--------------|-----------|-------|
| Cable assemblies | Yes | Standard permanent wiring method |
| Multiconductor cords/cables per Table 400.4 | Yes | Must be rated for **hard usage** or **extra-hard usage** |
| Type NM (Romex) | Yes | No height, building type, or concealment limitation |
| Type NMC | Yes | No height, building type, or concealment limitation |
| Type SE | Yes | No height, building type, or concealment limitation; permitted in raceway underground |
| Single insulated conductors | Only per 590.3(C) | Emergencies/tests only, accessible only to qualified persons |
| Conduit (RMC, IMC, EMT, PVC) | Yes | Standard permanent wiring methods always permitted |

### Branch Circuits (590.4(C))

Same allowances as feeders. All branch circuits shall originate in an approved power outlet, switchgear, switchboard, panelboard, motor control center, or fused switch enclosure.

**Exception for 590.3(B) or (C)**: Branch circuits may be run as single insulated conductors. For holiday lighting (590.3(B)):
- Voltage to ground not exceeding 150V
- Wiring not subject to physical damage
- Conductors supported on insulators at intervals not more than 10 ft

### Support Requirements (590.4(J))

- Cable assemblies and flexible cords/cables shall be **supported in place** to protect from physical damage
- Support by staples, cable ties, straps, or similar fittings
- **Branch circuits and feeders shall NOT be installed on the floor or ground**
- Extension cords exempt from support requirements
- Vegetation shall NOT be used for support (exception: holiday lighting with strain relief)

### Physical Protection (590.4(H))

- Flexible cords and cables protected from accidental damage
- Sharp corners and projections avoided
- Protection where passing through doorways or pinch points

---

## Conductor Ampacity (CEC Table 310.16)

Standard ampacity for copper conductors at 60°C, 75°C, and 90°C:

| Wire Size (AWG) | 60°C (TW, UF) | 75°C (THWN, XHHW) | 90°C (THHN, XHHW-2) |
|----------------|---------------|-------------------|---------------------|
| 14 | 15A | 20A | 25A |
| 12 | 20A | 25A | 30A |
| 10 | 30A | 35A | 40A |
| 8 | 40A | 50A | 55A |
| 6 | 55A | 65A | 75A |
| 4 | 70A | 85A | 95A |
| 3 | 85A | 100A | 115A |
| 2 | 95A | 115A | 130A |
| 1 | 110A | 130A | 145A |
| 1/0 | 125A | 150A | 170A |
| 2/0 | 145A | 175A | 195A |
| 3/0 | 165A | 200A | 225A |
| 4/0 | 195A | 230A | 260A |
| 250 | 215A | 255A | 290A |
| 300 | 240A | 285A | 320A |
| 350 | 260A | 310A | 350A |
| 400 | 280A | 335A | 380A |
| 500 | 320A | 380A | 430A |

> **Important**: For most temporary installations using THHN/THWN in conduit, use the **75°C column** per CEC 110.14(C)(1) — equipment terminal ratings typically limit the allowable ampacity to the 75°C value.

### Ambient Temperature Correction

- For above-ground temporary installations exposed to direct sunlight or high ambient temperatures, apply correction factors per **Table 310.15(B)(3)(C)**
- For flexible cords and cables, apply correction per **CEC 400.5(A)(3)**

### Conductor Fill Adjustment

When more than 3 current-carrying conductors are in a raceway, ampacity must be reduced per **Table 310.15(C)(1)**:

| Number of Current-Carrying Conductors | Percent of Table 310.16 Values |
|---------------------------------------|-------------------------------|
| 4-6 | 80% |
| 7-9 | 70% |
| 10-20 | 50% |
| 21-30 | 45% |
| 31-40 | 40% |
| 41+ | 35% |

---

## Flexible Cord and Cable Requirements (CEC Table 400.4, 400.5)

For temporary installations, cords and cables must be rated for the conditions of use:

### Usage Rating Requirements

| Usage Rating | Required For |
|-------------|-------------|
| Hard usage | Minimum for feeders and branch circuits per 590.4(B)/(C) |
| Extra-hard usage | Recommended for construction sites and harsh conditions |

### Common Cord Types for Temporary Power

| Type | Usage Rating | Description |
|------|-------------|-------------|
| S, SO, SOW | Hard usage | Flexible rubber cord, suitable for damp locations |
| ST, STO, STOW | Hard usage | Flexible thermoplastic cord |
| W | Extra-hard usage | Weather-resistant, rated for outdoor use |
| G, G-GC | Hard usage | Portable power cable for generators |
| Type W | Extra-hard usage | Rated 2000V, suitable for industrial/construction |

### Cord/Cable Ampacity (CEC 400.5)

- Ampacity determined per Table 400.5
- Apply ambient temperature correction factor for above-ground installations
- Specify cord/cable type per Table 400.4 suitable for conditions of use and location

---

## Conductor Identification

### Neutral (Grounded) Conductors (CEC 200.6, 200.7)

- **#6 AWG and smaller**: factory-applied **white** or **gray** insulation (200.6(A))
- **#4 AWG and larger**: white or gray **tape** encircling the ends (200.6(B))
- White conductors shall NOT be used for ungrounded conductors (200.7(A))
  - **Exception**: White conductors in cable assembly acceptable as ungrounded if re-identified with tape (not white, gray, or green) encircling the ends (200.7(C))

### Equipment Grounding Conductors (CEC 250.119)

- **#6 AWG and smaller**: factory insulated with **green** (or green with yellow stripes)
- **#4 AWG and larger**: identified with **green tape or labels** encircling conductor at each end and every accessible point
- **Green shall NEVER be used for neutral or ungrounded conductors**

### Ungrounded (Hot) Conductors

- Any color EXCEPT white, gray, or green
- Common convention: black, red, blue (for 3-phase)
- High-leg delta systems: phase with higher voltage to ground marked with **orange** label at each connection point (CEC 110.15)

---

## High-Leg Delta Systems (CEC 408.3(E))

For 4-wire delta-connected systems with midpoint on one phase grounded:

- Panel phase arrangement A, B, C from left to right: **B phase** is the phase with higher voltage to ground (408.3(E)(1))
- Each switchboard/panel shall have permanent label: **"CAUTION -- PHASE HAS ___ VOLTS TO GROUND"** (408.3(E)(2))
- "Slash-rated" breakers (e.g., 120/240V) shall NOT be used if lower rating is less than highest voltage to ground in panel (CEC 240.85)
