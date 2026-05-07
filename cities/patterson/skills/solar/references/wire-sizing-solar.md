---
title: "Wire Sizing and Conduit for Solar PV Circuits"
category: "Electrical Sizing"
relevance: "Every solar PV review involving conductor or conduit sizing"
key_code_sections: "CEC Table 310.16, Table 690.31(A), Table 690.7(A), 690.8, 690.9, 310.15"
---

# Wire Sizing and Conduit for Solar PV Circuits

Source: 2025 California Electrical Code (Title 24, Part 3), Articles 690, 310, 240.

---

## Overview: Why Solar Wire Sizing Is Different

Solar PV conductors on rooftops are subject to elevated ambient temperatures. The CEC requires:
1. **125% continuous duty multiplier** on maximum current (690.8(B)(1))
2. **Temperature correction** for ambient temperatures above 30C (86F)
3. **Conduit fill adjustment** for multiple current-carrying conductors

For rooftop solar, the ambient temperature includes a **22C adder** for conduit exposed to direct sunlight mounted >0.5" (13mm) above the roof surface. This means a typical California rooftop in summer has an effective ambient of approximately **47C** for feeders (no sunlight adder) and up to **69C** for array wiring in direct sunlight.

---

## Table 310.16 -- Standard Conductor Ampacity

Ampacities for insulated conductors rated 0-2000V, not more than 3 current-carrying conductors in raceway/cable/earth, based on 30C ambient (copper):

| AWG | 60C (TW, UF) | 75C (THWN, XHHW, USE) | 90C (THHN, XHHW-2, USE-2) |
|-----|-------------|----------------------|---------------------------|
| 14 | 15 | 20 | 25 |
| 12 | 20 | 25 | 30 |
| 10 | 30 | 35 | 40 |
| 8 | 40 | 50 | 55 |
| 6 | 55 | 65 | 75 |
| 4 | 70 | 85 | 95 |
| 3 | 85 | 100 | 115 |
| 2 | 95 | 115 | 130 |
| 1 | 110 | 130 | 145 |
| 1/0 | 125 | 150 | 170 |
| 2/0 | 145 | 175 | 195 |
| 3/0 | 165 | 200 | 225 |
| 4/0 | 195 | 230 | 260 |

*Source: CEC Table 310.16. Use 75C column for standard terminal ratings per 110.14(C).*

---

## Table 690.31(A)(3)(1) -- PV Wire Ampacity (105C and 125C)

For PV wire and cable rated for higher temperatures:

| AWG | 105C (PVC, CPE, XLPE) | 125C (XLPE, EPDM) |
|-----|----------------------|-------------------|
| 18 | 15 | 16 |
| 16 | 19 | 20 |
| 14 | 29 | 31 |
| 12 | 36 | 39 |
| 10 | 46 | 50 |
| 8 | 64 | 69 |
| 6 | 81 | 87 |
| 4 | 109 | 118 |
| 3 | 129 | 139 |
| 2 | 143 | 154 |
| 1 | 168 | 181 |
| 1/0 | 193 | 208 |
| 2/0 | 229 | 247 |
| 3/0 | 263 | 284 |
| 4/0 | 301 | 325 |

*Not more than 3 current-carrying conductors, based on 30C ambient.*

---

## Temperature Correction Factors

### Table 690.31(A)(3)(2) -- For PV Wire (105C/125C)

| Ambient Temp (C) | 105C Factor | 125C Factor | Ambient Temp (F) |
|-------------------|-------------|-------------|-------------------|
| 30 | 1.00 | 1.00 | 86 |
| 31-35 | 0.97 | 0.97 | 87-95 |
| 36-40 | 0.93 | 0.95 | 96-104 |
| 41-45 | 0.89 | 0.92 | 105-113 |
| 46-50 | 0.86 | 0.89 | 114-122 |
| 51-55 | 0.82 | 0.86 | 123-131 |
| 56-60 | 0.77 | 0.83 | 132-140 |
| 61-65 | 0.73 | 0.79 | 141-149 |
| 66-70 | 0.68 | 0.76 | 150-158 |
| 71-75 | 0.63 | 0.73 | 159-167 |
| 76-80 | 0.58 | 0.69 | 168-176 |
| 81-85 | 0.52 | 0.65 | 177-185 |
| 86-90 | 0.45 | 0.61 | 186-194 |
| 91-95 | 0.37 | 0.56 | 195-203 |
| 96-100 | 0.26 | 0.51 | 204-212 |

### Rooftop Temperature Adder

Per CEC 310.15(B)(4) (referenced via 690.31(A)):
- Conduit exposed to sunlight on rooftops: add temperature adder to ambient
- Mounted **>13mm (0.5") above roof**: add **22C (40F)**
- Mounted **on roof surface**: add **33C (60F)**

**Example**: California summer ambient 45C + 22C rooftop adder = **67C effective** for rooftop array wiring in conduit. At 67C, the 90C (THHN) correction factor from Table 310.16 = approximately 0.58, and PV wire 125C factor = 0.76.

### Conduit Fill Adjustment (310.15(C)(1))

| Current-Carrying Conductors | Adjustment Factor |
|----------------------------|-------------------|
| 1-3 | 1.00 |
| 4-6 | 0.80 |
| 7-9 | 0.70 |
| 10-20 | 0.50 |

**Note**: 3 circuits of 2 conductors each = 6 current-carrying conductors in one raceway. Neutral conductors that carry only unbalanced current are not counted.

---

## Microinverter Branch Circuit Sizing

Standard combinations for residential microinverter systems (from standard plan tables). Conditions: copper conductors, 90C wet-rated insulation, rooftop with 22C adder, <=6 current-carrying conductors (3 circuits) in raceway.

| Branch Current (A) | Branch Power (W) | OCPD (A) | Min. Conductor (AWG) | Min. Metal Conduit |
|-------------------|-----------------|----------|---------------------|-------------------|
| 12 | 2880 | 15 | #12 | 3/4" |
| 16 | 3840 | 20 | #10 | 3/4" |
| 20 | 4800 | 25 | #8 | 1" |
| 24 | 5760 | 30 | #8 | 1" |

*Derived from CEC 690.8, Table 310.16 with rooftop corrections per Table 690.31(A).*

---

## Solar Load Center Feeder Sizing

For feeder from solar load center to main panel. Conditions: copper, 90C wet-rated, ambient 47C (no rooftop sunlight adder -- feeder typically not on roof), <=3 current-carrying conductors in raceway.

| Circuit Current (A) | Circuit Power (W) | OCPD (A) | Min. Bus Bar (A) | Min. Conductor (AWG) | Min. Metal Conduit |
|-------------------|-----------------|----------|-----------------|---------------------|-------------------|
| 24 | 5760 | 30 | 30 | #10 | 1/2" |
| 28 | 6720 | 35 | 35 | #8 | 3/4" |
| 32 | 7680 | 40 | 40 | #8 | 3/4" |
| 36 | 8640 | 45 | 45 | #8 | 3/4" |
| 40 | 9600 | 50 | 50 | #8 | 3/4" |
| 41.6 | <=10000 | 60 | 60 | #8 | 3/4" |

*Derived from CEC 690.8, Table 310.16 with correction for 47C ambient.*

---

## PV Wire Strand Requirements (Table 690.31(C)(4))

For flexible fine-stranded PV wire connected to tracking arrays or requiring flexibility:

| PV Wire AWG | Minimum Strands |
|-------------|----------------|
| 18 | 17 |
| 16-10 | 19 |
| 8-4 | 49 |
| 2 | 130 |
| 1 AWG - 1000 MCM | 259 |

---

## Sizing Procedure -- Step by Step

### Step 1: Determine Maximum Circuit Current
- **PV source circuit**: Sum of parallel module Isc x 125% (690.8(A)(1)(a))
- **Inverter output**: Inverter continuous output current rating (690.8(A)(1)(e))
- **Microinverter branch**: Number of microinverters x rated AC output current

### Step 2: Size Conductors (690.8(B))
Take the **larger** of:
- Max current x 125% (no correction/adjustment) -- this is the "156.25% rule" for PV source circuits
- Max current with applicable correction and adjustment factors

### Step 3: Apply Temperature Correction
1. Determine effective ambient temperature:
   - Rooftop array wiring: ambient + 22C (conduit >0.5" above roof)
   - Feeder not on rooftop: ambient temperature only
2. Look up correction factor from Table 310.16 or Table 690.31(A)(3)(2)
3. Derated ampacity = Table ampacity x correction factor

### Step 4: Apply Conduit Fill Adjustment
If >3 current-carrying conductors in one raceway, apply adjustment factor from 310.15(C)(1).

### Step 5: Select OCPD
- OCPD >= 125% of max current per 690.8(A) -- per 690.9(B)
- Round up to next standard size per 240.4(B) if needed
- Standard sizes: 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100A

### Step 6: Verify Conductor Ampacity >= OCPD Rating
Final selected conductor ampacity (after corrections) must be >= OCPD rating, unless overcurrent protection is not required per 690.9(A)(1).
