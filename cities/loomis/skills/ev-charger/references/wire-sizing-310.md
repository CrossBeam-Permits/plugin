---
title: "CEC Table 310.16 — Conductor Ampacity and Wire Sizing"
category: "Wire Sizing"
relevance: "Every EV charger review involving wire sizing"
key_code_sections: "CEC Table 310.16, Table 250.122, 310.15(B), 310.15(C)(1), 240.4(D)"
---

# CEC Table 310.16 — Conductor Ampacity for EV Charger Installations

Source: 2025 California Electrical Code (Title 24, Part 3), Article 310.

## Table 310.16 — Allowable Ampacities of Insulated Conductors

**Conditions**: Rated 0-2000 volts, not more than 3 current-carrying conductors in raceway/cable/earth, ambient temperature 30°C (86°F). Copper conductors.

| Size (AWG) | 60°C (TW, UF) | 75°C (THWN, XHHW) | 90°C (THHN, XHHW-2) |
|-----------|---------------|-------------------|---------------------|
| 14 | 15A | 20A | 25A |
| 12 | 20A | 25A | 30A |
| 10 | 30A | 35A | 40A |
| 8 | 40A | 50A | 55A | *See note below* |
| 6 | 55A | 65A | 75A |
| 4 | 70A | 85A | 95A |
| 3 | 85A | 100A | 115A |
| 2 | 95A | 115A | 130A |

### Critical Note: #8 AWG and 50A EV Circuits

**#8 AWG at 75°C is rated exactly 50A** per the table above, but **#6 AWG is the required minimum for 50A EV circuits.** Here's why: EV loads are continuous (CEC 625.42). Per CEC 210.20(A), branch circuit conductors supplying continuous loads must have ampacity >= 125% of the continuous load, OR the overcurrent device must be listed for continuous operation at 100%. Since most residential breakers are NOT listed for 100% continuous duty, the conductor must be sized for the full 125% rule — meaning for a 40A charger, the conductor needs 50A ampacity minimum. While #8 at 75°C technically meets 50A, it is at the absolute ceiling with zero margin for voltage drop, ambient temperature, or conduit fill derating. The industry standard and all quick-reference tables in this skill specify **#6 AWG for 50A circuits**. Do not accept #8 AWG on a 50A EV circuit.

### Which Column to Use

**For EV charger installations, use the 75°C column** in most cases:
- THHN wire is rated 90°C but most terminations (breakers, EVSE connections) are rated 75°C
- Per CEC 110.14(C), conductor ampacity is limited by the lowest-rated termination
- For circuits ≤100A: use 75°C column values

### EV Charger Wire Sizing Quick Reference

Based on 75°C column (standard for residential installations with THHN/THWN wire):

| Circuit Breaker | Min. Wire Size | 75°C Ampacity | Conduit (EMT) | Conduit (PVC/FMC) |
|----------------|---------------|---------------|---------------|-------------------|
| 20A | #12 AWG | 25A | 1/2" | 1/2" |
| 30A | #10 AWG | 35A | 1/2" | 1/2" |
| 40A | #8 AWG | 50A | 3/4" | 3/4" |
| 50A | #6 AWG | 65A | 3/4" | 3/4" |
| 60A | #6 AWG | 65A | 3/4" | 3/4" |
| 70A | #4 AWG | 85A | 1" | 1" |
| 80A | #4 AWG | 85A | 1" | 1" |
| 100A | #2 AWG | 115A | 1" | 1" |

**Note on conduit sizing**: Based on 4 wires in conduit (2 current-carrying conductors + 1 grounded (neutral) conductor + 1 equipment grounding conductor). EMT = Electrical Metallic Tubing, PVC = Rigid Nonmetallic Conduit Schedule 40, FMC = Flexible Metal Conduit. For 240V-only circuits without a neutral (3 wires total), 1/2" EMT is acceptable for 40A.

### NMC (Romex) Alternative

Non-metallic sheathed cable (NM-B / Romex) is permitted where:
- Protected inside wall cavity, attic, or ceiling space
- Not exposed to physical damage
- Not in wet/damp locations

NMC uses the 60°C ampacity column regardless of conductor insulation rating. This means larger wire sizes may be needed:

| Circuit Breaker | Min. Wire (NMC/60°C) | Min. Wire (THHN in conduit/75°C) |
|----------------|----------------------|----------------------------------|
| 40A | #8 AWG (40A) | #8 AWG (50A) |
| 50A | #6 AWG (55A) | #6 AWG (65A) |
| 60A | #4 AWG (70A) | #6 AWG (65A) |

> For 60A circuits with NMC, you need #4 AWG (not #6) because the 60°C ampacity of #6 is only 55A.

---

## Equipment Grounding Conductor (EGC) Sizing — Table 250.122

The equipment grounding conductor protects against ground faults. It must be sized based on the rating of the overcurrent device (breaker) protecting the circuit, per CEC Table 250.122.

| Breaker Size (Amps) | Min. EGC Size (Copper) |
|---------------------|----------------------|
| 15A | #14 AWG |
| 20A | #12 AWG |
| 21–60A | #10 AWG |
| 61–100A | #8 AWG |
| 101–200A | #6 AWG |

*Table 250.122 uses "not exceeding" thresholds: 15, 20, 60, 100, 200A. For any breaker between two thresholds, use the higher threshold's EGC size.*

> **Key point for EV charger review**: For breakers from 21A through 60A (which covers 30A, 40A, 50A, and 60A EV circuits), the EGC is always #10 AWG minimum (copper). For 70A, 80A, and 100A circuits, the EGC is #8 AWG. The EGC is NOT required to be larger than the circuit conductors themselves.

### Complete EV Charger Wiring Table (Conductors + EGC + Conduit)

This table combines Table 310.16 (75°C column), Table 250.122, and conduit fill calculations for a standard residential EV charger circuit: 2 current-carrying conductors + 1 neutral + 1 EGC, THHN copper.

| Breaker (A) | Circuit Wire | EGC Wire | EMT | PVC (Sch 40) | FMC |
|-------------|-------------|----------|-----|-------------|-----|
| 20 | #12 AWG | #12 AWG | 1/2" | 1/2" | 1/2" |
| 30 | #10 AWG | #10 AWG | 1/2" | 1/2" | 1/2" |
| 40 | #8 AWG | #10 AWG | 3/4" | 3/4" | 3/4" |
| 50 | #6 AWG | #10 AWG | 3/4" | 3/4" | 3/4" |
| 60 | #6 AWG | #10 AWG | 3/4" | 3/4" | 3/4" |
| 70 | #4 AWG | #8 AWG | 1" | 1" | 1" |
| 80 | #4 AWG | #8 AWG | 1" | 1" | 1" |
| 100 | #2 AWG | #8 AWG | 1" | 1" | 1" |

*Source: CEC Table 310.16 (75°C column), Table 250.122, Chapter 9 Tables for conduit fill.*

---

## Adjustment and Correction Factors

### Ambient Temperature Correction (310.15(B))

If ambient temperature exceeds 30°C (86°F), apply correction factors:

| Ambient Temp °C | 60°C Conductor | 75°C Conductor | 90°C Conductor |
|----------------|---------------|---------------|---------------|
| 31-35 | 0.91 | 0.94 | 0.96 |
| 36-40 | 0.82 | 0.88 | 0.91 |
| 41-45 | 0.71 | 0.82 | 0.87 |
| 46-50 | 0.58 | 0.75 | 0.82 |

> For most California residential installations (garage, exterior), ambient temperature corrections are not typically needed. Exception: attic runs in hot climates may require derating.

### Conductor Fill Adjustment (310.15(C)(1))

If more than 3 current-carrying conductors in a raceway:

| Number of Conductors | Adjustment Factor |
|---------------------|------------------|
| 4-6 | 0.80 |
| 7-9 | 0.70 |
| 10-20 | 0.50 |

> For a typical single EV charger circuit (2 current-carrying + 1 ground + 1 equipment ground), only 2 are "current-carrying." No adjustment needed.

---

## Overcurrent Protection Limits (240.4(D))

Small conductors have maximum overcurrent protection limits:
- **#14 AWG**: 15A maximum
- **#12 AWG**: 20A maximum
- **#10 AWG**: 30A maximum

These are hard limits — you cannot put #12 wire on a 30A breaker even if the 75°C ampacity is 25A. For #8 AWG and larger, the overcurrent protection may be sized up to the next standard size per 240.4(B).

---

## Conduit Support Requirements

| Conduit Type | Support Interval | Max Distance from Box |
|-------------|-----------------|----------------------|
| EMT (Electrical Metallic Tubing) | 10 ft | 3 ft |
| RNC (Rigid Nonmetallic Conduit Sch. 40) | 3 ft | 3 ft |
| FMC (Flexible Metal Conduit) | 4.5 ft | 1 ft |
| NMC (Non-Metallic Cable / Romex) | 4.5 ft | 1 ft |

---

## Standard Breaker Sizes (240.6(A))

Available standard ampere ratings for fuses and circuit breakers:

10, 15, 20, 25, **30**, 35, **40**, 45, **50**, **60**, **70**, 80, 90, **100**, 110, 125, 150, 175, 200 (and up)

Bolded sizes are the most common for residential EV charger circuits.
