---
title: "CEC Table 310.16 — Conductor Ampacity for Panel Upgrades"
category: "Wire Sizing"
relevance: "Every panel upgrade review involving service entrance conductor sizing"
key_code_sections: "CEC Table 310.16, 310.15(B), 310.15(C)(1), 240.4, 240.6(A)"
---

# CEC Table 310.16 — Conductor Ampacity for Service Entrance

Source: 2025 California Electrical Code (Title 24, Part 3), Article 310.

## Table 310.16 — Allowable Ampacities of Insulated Conductors

**Conditions**: Rated 0-2000 volts, not more than 3 current-carrying conductors in raceway/cable/earth, ambient temperature 30C (86F).

### Copper Conductors

| Size (AWG/kcmil) | 60C (TW, UF) | 75C (THWN, XHHW) | 90C (THHN, XHHW-2) |
|-------------------|--------------|-------------------|---------------------|
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

### Aluminum Conductors

| Size (AWG/kcmil) | 60C (TW, UF) | 75C (THWN, XHHW) | 90C (THHN, XHHW-2) |
|-------------------|--------------|-------------------|---------------------|
| 12 | 15A | 20A | 25A |
| 10 | 25A | 30A | 35A |
| 8 | 30A | 40A | 45A |
| 6 | 40A | 50A | 60A |
| 4 | 55A | 65A | 75A |
| 3 | 65A | 75A | 85A |
| 2 | 75A | 90A | 100A |
| 1 | 85A | 100A | 115A |
| 1/0 | 100A | 120A | 135A |
| 2/0 | 115A | 135A | 150A |
| 3/0 | 130A | 155A | 175A |
| 4/0 | 150A | 180A | 205A |
| 250 | 170A | 205A | 230A |
| 300 | 195A | 230A | 260A |
| 350 | 210A | 250A | 280A |
| 400 | 225A | 270A | 305A |
| 500 | 260A | 310A | 350A |
| 600 | 285A | 340A | 385A |
| 750 | 320A | 385A | 435A |

### Which Column to Use

**For service entrance installations, use the 75C column** in most cases:
- Most residential service equipment has 75C-rated terminations
- Per CEC 110.14(C), conductor ampacity is limited by the lowest-rated termination
- For circuits >100A: some equipment is rated 75/90C — check the listing

---

## Service Entrance Conductor Quick Reference

Based on 75C column. These are the minimum conductor sizes for each standard service size:

### Copper Service Entrance Conductors

| Service Size | Min. Wire Size | 75C Ampacity | Conduit (EMT) |
|-------------|---------------|--------------|---------------|
| 100A | #4 AWG | 85A | 1-1/4" |
| 125A | #2 AWG | 115A | 1-1/4" |
| 150A | #1 AWG | 130A | 1-1/2" |
| 200A | #2/0 AWG | 175A | 2" |
| 225A | #3/0 AWG | 200A | 2" |
| 320A | 350 kcmil | 310A | 3" |
| 400A | 500 kcmil | 380A | 3" |

### Aluminum Service Entrance Conductors

| Service Size | Min. Wire Size | 75C Ampacity | Conduit (EMT) |
|-------------|---------------|--------------|---------------|
| 100A | #2 AWG | 90A | 1-1/4" |
| 125A | #1/0 AWG | 120A | 1-1/2" |
| 150A | #2/0 AWG | 135A | 1-1/2" |
| 200A | #4/0 AWG | 180A | 2" |
| 225A | 250 kcmil | 205A | 2-1/2" |
| 320A | 500 kcmil | 310A | 3" |
| 400A | 750 kcmil | 385A | 3-1/2" |

**Note on aluminum**: Aluminum conductors are common for service entrance wiring because they are significantly cheaper than copper in larger sizes. They are code-compliant when properly terminated with AL-rated lugs and anti-oxidant compound.

---

## Overcurrent Protection (240.4)

The overcurrent protection (main breaker) must not exceed the conductor ampacity:
- **Small conductors** have hard limits: #14=15A, #12=20A, #10=30A
- **#8 AWG and larger**: overcurrent may be sized up to the next standard size per 240.4(B)

### Standard Breaker Sizes (240.6(A))

10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, **100**, 110, **125**, **150**, 175, **200**, **225**, 250, 300, **320**, 350, **400** (and up)

Bolded sizes are the standard residential service panel sizes.

---

## Adjustment and Correction Factors

### Ambient Temperature Correction (310.15(B))

If ambient temperature exceeds 30C (86F), apply correction factors:

| Ambient Temp C | 60C Conductor | 75C Conductor | 90C Conductor |
|----------------|--------------|--------------|--------------|
| 31-35 | 0.91 | 0.94 | 0.96 |
| 36-40 | 0.82 | 0.88 | 0.91 |
| 41-45 | 0.71 | 0.82 | 0.87 |
| 46-50 | 0.58 | 0.75 | 0.82 |

> For most California residential service entrance installations, ambient temperature corrections are not typically needed. Exception: conductors routed through attics or subject to direct sunlight may need derating.

### Conductor Fill Adjustment (310.15(C)(1))

If more than 3 current-carrying conductors in a raceway:

| Number of Conductors | Adjustment Factor |
|---------------------|------------------|
| 4-6 | 0.80 |
| 7-9 | 0.70 |
| 10-20 | 0.50 |

> For a typical residential service (2 ungrounded + 1 grounded conductor), only 2 are "current-carrying" for this calculation. No adjustment needed.

---

## Conduit Sizing for Service Entrance

| Service Size | Conductor Size (Cu) | Conductor Size (Al) | Min. EMT | Min. RNC Sch 40 |
|-------------|--------------------|--------------------|----------|-----------------|
| 100A | #4 AWG | #2 AWG | 1-1/4" | 1-1/4" |
| 200A | #2/0 AWG | #4/0 AWG | 2" | 2" |
| 320A | 350 kcmil | 500 kcmil | 3" | 3" |
| 400A | 500 kcmil | 750 kcmil | 3" | 3-1/2" |

Based on 4 conductors in conduit (2 ungrounded + 1 grounded + 1 equipment grounding conductor).
