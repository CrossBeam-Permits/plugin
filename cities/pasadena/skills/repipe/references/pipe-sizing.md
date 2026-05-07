---
title: "CPC Section 610 — Water Supply Pipe Sizing"
category: "Pipe Sizing"
relevance: "Every repipe review with fixture count"
key_code_sections: "CPC 610.0, Table 610.3, Table 610.4"
---

# CPC Section 610 — Water Supply Pipe Sizing

Source: 2025 California Plumbing Code (Title 24, Part 5), Chapter 6.

## Overview

Water supply pipe sizing uses the **fixture unit method**: count fixtures, convert to Water Supply Fixture Units (WSFU), then look up the minimum pipe size based on available pressure and developed pipe length.

---

## Water Supply Fixture Units — Table 610.3

Each fixture type has an assigned WSFU value for cold, hot, and total demand:

### Residential (Private Use) Fixtures

| Fixture | Cold WSFU | Hot WSFU | Total WSFU |
|---------|-----------|----------|------------|
| Water Closet, 1.6 GPF (gravity tank) | 2.5 | — | 2.5 |
| Bathtub (with or without shower) | 1.0 | 1.0 | 1.4 |
| Shower (single head) | 1.0 | 1.0 | 1.4 |
| Kitchen Sink (domestic) | 1.0 | 1.0 | 1.4 |
| Lavatory | 0.5 | 0.5 | 0.7 |
| Clothes Washer | 1.0 | 1.0 | 1.4 |
| Dishwasher (domestic) | — | 1.4 | 1.4 |
| Hose Bibb / Sill Cock | 2.5 | — | 2.5 |
| Laundry Tray (1-3 compartments) | 1.0 | 1.0 | 1.4 |

### Calculating Total WSFU for a Repipe

**Step 1**: List all fixtures in the dwelling
**Step 2**: Assign WSFU from Table 610.3
**Step 3**: Sum total WSFU
**Step 4**: Use total to determine building supply pipe size from Table 610.4

**Example — Typical 3-bed/2-bath house (12 fixtures):**

| Fixture | Qty | WSFU Each | Subtotal |
|---------|-----|-----------|----------|
| Water Closet | 2 | 2.5 | 5.0 |
| Bathtub/Shower | 2 | 1.4 | 2.8 |
| Lavatory | 2 | 0.7 | 1.4 |
| Kitchen Sink | 1 | 1.4 | 1.4 |
| Dishwasher | 1 | 1.4 | 1.4 |
| Clothes Washer | 1 | 1.4 | 1.4 |
| Hose Bibb | 2 | 2.5 | 5.0 |
| Laundry Sink | 1 | 1.4 | 1.4 |
| **Total** | **12** | | **19.8** |

---

## Pipe Sizing by Pressure and Length — Table 610.4

Once total WSFU is known, the building supply pipe size depends on:
1. **Available water pressure** (from the street main, after meter loss)
2. **Developed length** of the piping run (longest run from meter to farthest fixture)

### Sizing Table (Simplified from Table 610.4)

#### 30-45 psi Range

| Meter Size | Supply Pipe | Max Length 40' | Max Length 60' | Max Length 80' | Max Length 100' |
|-----------|-------------|---------------|---------------|---------------|----------------|
| 3/4" | 3/4" | 16 WSFU | 14 WSFU | 11 WSFU | 9 WSFU |
| 3/4" | 1" | 29 WSFU | 25 WSFU | 21 WSFU | 17 WSFU |
| 1" | 1" | 36 WSFU | 31 WSFU | 27 WSFU | 23 WSFU |
| 1" | 1-1/4" | 54 WSFU | 47 WSFU | 41 WSFU | 36 WSFU |

#### 46-60 psi Range

| Meter Size | Supply Pipe | Max Length 40' | Max Length 60' | Max Length 80' | Max Length 100' |
|-----------|-------------|---------------|---------------|---------------|----------------|
| 3/4" | 3/4" | 21 WSFU | 19 WSFU | 17 WSFU | 14 WSFU |
| 3/4" | 1" | 39 WSFU | 34 WSFU | 29 WSFU | 25 WSFU |
| 1" | 1" | 48 WSFU | 42 WSFU | 37 WSFU | 32 WSFU |
| 1" | 1-1/4" | 78 WSFU | 68 WSFU | 58 WSFU | 50 WSFU |

#### Over 60 psi Range

| Meter Size | Supply Pipe | Max Length 40' | Max Length 60' | Max Length 80' | Max Length 100' |
|-----------|-------------|---------------|---------------|---------------|----------------|
| 3/4" | 3/4" | 28 WSFU | 25 WSFU | 22 WSFU | 19 WSFU |
| 3/4" | 1" | 50 WSFU | 44 WSFU | 38 WSFU | 33 WSFU |
| 1" | 1" | 63 WSFU | 55 WSFU | 48 WSFU | 42 WSFU |

---

## Minimum Pipe Sizes (610.8, CRC P2903.7)

| Component | Minimum Size | Code Section |
|-----------|-------------|-------------|
| **Water service (building supply)** | 3/4" | CPC 610.8, CRC P2903.7 |
| **Branch to single fixture** | 1/2" (except where Table 610.3 specifies larger) | CPC 610.8 |
| **Water closet supply** | 3/8" (stop valve to fixture) | CPC 610.8 |
| **Hose bibb** | 1/2" | CPC 610.8 |
| **Distribution lines <= 60 ft.** | 3/8" permitted IF meter pressure >= 40 psi | CPC 610.8, CRC P2903.8.2 |

### Water Heater Manifold Rule (610.8, CRC P2903.8.2)

Where the water heater is fed from the END of a cold-water manifold, the manifold shall be **one size larger** than the water heater supply line.

---

## Branch Pipe Sizing (610.9)

Branch pipes serving a group of fixtures are sized the same way as building supply — calculate WSFU for fixtures on the branch, then use Table 610.4.

**Key rule**: No branch pipe shall be sized larger than necessary for the total demand of all fixtures it serves. Branch sizing follows the same fixture-unit-to-pipe-size methodology.

---

## Pipe Sizing Procedure — Summary

1. **Count fixtures** and assign WSFU from Table 610.3
2. **Sum total WSFU** for the building
3. **Determine available pressure** at the meter (ask water utility or test)
4. **Measure developed length** of longest run (meter to farthest fixture)
5. **Look up pipe size** in Table 610.4 for pressure range and length
6. **Verify minimum sizes**: 3/4" building supply, 1/2" branches
7. **Size branches** using same method for fixture groups
