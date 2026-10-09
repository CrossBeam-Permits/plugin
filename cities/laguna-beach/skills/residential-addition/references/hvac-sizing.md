---
title: "HVAC Sizing and Duct Design"
category: "Mechanical/Energy"
relevance: "Additions with HVAC — Manual J/S/D, duct insulation, leakage, ventilation requirements"
key_code_sections: "Energy Code 150.0(h), 150.0(o), 150.2(a)1C, 150.2(a)1E, 150.2(b)1D, Table 150.2-A, Table 150.2-B, Table 150.2-C, Table 150.2-D"
---

# HVAC Sizing and Duct Design

Source: 2025 California Energy Code (Title 24, Part 6), Sections 150.0 and 150.2.

---

## Extending Existing HVAC vs. New System

### Extending Existing System (Exception 3 to Section 150.2(a))
When heating or cooling is extended from the existing system to serve the addition:
- **Existing equipment need NOT comply with Part 6**
- Existing heating capacity must be adequate to meet CRC R303.10 (maintain 68F at 3 ft above floor)
- However, new ducts MUST comply with insulation and leakage requirements (Section 150.2(b)1D)

### New or Replacement System
When a new system is installed for the addition:
- Must comply with all Part 6 requirements
- Manual J load calculation required (Section 150.0(h))
- Maximum capacity limits per Tables 150.2-A and 150.2-B
- Heat pump required (no electric resistance as primary heat)

---

## Manual J Load Calculations (Section 150.0(h))

### When Required
- Any new or replacement space-conditioning system
- Equipment sizing must be based on ACCA Manual J (or approved equivalent)
- Climate zone design criteria from Table R301.2

### Load Calculation Inputs
- Building orientation, area, volume
- Insulation values (walls, ceiling, floor)
- Fenestration area, U-factor, SHGC
- Infiltration rate (per Table 150.2-C for additions)
- Internal heat gains
- Outdoor design conditions for the climate zone

### Maximum Infiltration for Load Calculations (Table 150.2-C)

| Floor Area | 1-Story Heating | 1-Story Cooling | 2-Story Heating | 2-Story Cooling |
|---|---|---|---|---|
| <=900 SF | 0.61 ACH | 0.32 ACH | 0.79 ACH | 0.41 ACH |
| 901-1,500 SF | 0.45 ACH | 0.23 ACH | 0.80 ACH | 0.30 ACH |
| 1,501-2,000 SF | 0.38 ACH | 0.20 ACH | 0.50 ACH | 0.26 ACH |
| 2,001-3,000 SF | 0.32 ACH | 0.16 ACH | 0.41 ACH | 0.21 ACH |
| >=3,001 SF | 0.28 ACH | 0.15 ACH | 0.37 ACH | 0.19 ACH |

**Exception:** If envelope leakage is field-verified per RA3.8, tested values may be used.

---

## Maximum System Capacity

### Maximum Heating Capacity (Table 150.2-A)

| System Type | Heating Only | Heat Pump (HL > CL) | Heat Pump (CL > HL by <12 kBtu/h) | Heat Pump (CL > HL by >=12 kBtu/h) |
|---|---|---|---|---|
| Single-speed | HL + 6 kBtu/h | No maximum | HL + 12 kBtu/h | No maximum |
| Variable/multi-speed (max) | HL + 6 kBtu/h | No maximum | HL + 12 kBtu/h | No maximum |
| Variable/multi-speed (min) | 80% of HL | 80% of HL | No maximum | No maximum |

### Maximum Cooling Capacity (Table 150.2-B)

| System Type | Cooling Only | Heat Pump (HL > CL) | Heat Pump (CL > HL by <12 kBtu/h) | Heat Pump (CL > HL by >=12 kBtu/h) |
|---|---|---|---|---|
| Single-speed | CL + 6 kBtu/h | No maximum | CL + 6 kBtu/h | CL + 6 kBtu/h |
| Variable/multi-speed (max) | CL + 6 kBtu/h | No maximum | CL + 6 kBtu/h | CL + 6 kBtu/h |
| Variable/multi-speed (min) | 80% of CL | No maximum | 80% of CL | 80% of CL |

**Exception 1:** Ductless systems (mini-splits) — no maximum capacity limit.

**Exception 2:** If airflow is field-verified at >=350 cfm/ton, no maximum capacity limit.

---

## Heat Pump Requirement (Section 150.1(c)6, Table 150.1-A)

For new construction and new systems in additions:
- Electric resistance is NOT allowed as primary heat source
- Heat pump is the prescriptive standard
- Exception: Supplemental heating unit <=2 kW (7,000 Btu/h) with 30-min time-limiting device

### Altered Space-Heating Systems (Section 150.2(b)1G)
- No electric resistance as primary heat
- Exceptions only if existing system is already electric resistance (and only certain conditions)

---

## Duct Design and Insulation

### Duct Insulation (Table 150.2-D)

| Climate Zones | Min Duct R-Value |
|---|---|
| CZ 3, 5-7 | R-6 |
| CZ 1-2, 4, 8-16 | R-8 |

These values apply to new ducts located in unconditioned space.

### Duct Leakage Requirements

| Duct System Type | Max Leakage | Test Method |
|---|---|---|
| **Entirely new or complete replacement** | 5% of air handler airflow | RA3.1.4.3.1 |
| **Extension of existing** (Option 1) | 10% of air handler airflow | RA3.1.4.3.1 |
| **Extension of existing** (Option 2) | 7% of leakage to outside | RA3.1.4.3.4 |
| **Extension of existing** (Option 3) | Seal all accessible leaks | Visual + smoke test by ECC-Rater (RA3.1.4.3.5) |

**Entirely new or complete replacement duct system:** Constructed of at least 75% new duct material; up to 25% may be reused parts from existing system.

### Ducts in Garage Spaces
When ducts, air handlers, or coils are in a garage, the system must comply with:
- Max 6% leakage (RA3.1.4.3.1), OR
- Seal all accessible leaks in garage + visual/smoke test by ECC-Rater

### Field Verification
All duct leakage testing must be confirmed through field verification and diagnostic testing by a certified ECC-Rater per Reference Residential Appendix RA3.1.

---

## Duct and Air Handler Location

### Conditioned Space Requirement (Section 150.1(c)9B)
For new construction: ducts and air handlers must be in conditioned space and verified per RA3.1.4.3.8.

### High Performance Attics (Section 150.1(c)9A)
Air handlers or ducts may be in ventilated attic spaces when roof and ceiling insulation meet Option B in Table 150.1-A (below-roof-deck insulation plus ceiling insulation).

### For Additions
When extending existing duct system in unconditioned space: insulation and leakage testing required, but existing location may remain in unconditioned space.

---

## Mechanical Ventilation (Section 150.2(a)1C, 150.0(o))

### Whole-Dwelling Ventilation

| Addition Size | Requirement |
|---|---|
| <=1,000 SF | Exempt from whole-dwelling ventilation airflow |
| >1,000 SF | Whole-dwelling ventilation based on entire dwelling CFA (existing + addition) |
| New dwelling unit (e.g., JADU addition) | Full ventilation based on new unit CFA |

Whole-dwelling ventilation per ASHRAE 62.2:
- Continuous mechanical ventilation
- Airflow rate based on number of bedrooms and conditioned floor area

### Local Mechanical Exhaust (Always Required)

| Location | Requirement |
|---|---|
| Kitchen | Range hood vented to outdoors; min 100 cfm intermittent or per capture efficiency |
| Bathroom | Exhaust fan: min 50 cfm intermittent or 20 cfm continuous |

Fans must be rated for airflow and sound per ASHRAE 62.2 Sections 7.1 and 7.3.

---

## Refrigerant Charge Verification

### When Required (Table 150.1-A)
- **Air conditioners:** Required in CZ 2, 8-15
- **Heat pumps:** Required in ALL climate zones

### Verification Process
1. Measurement access holes (MAH) installed per RA3.2.2.3
2. System airflow rate verified: min 350 cfm/ton (or 250 cfm/ton for small-duct high-velocity)
3. Refrigerant charge verified by installer, confirmed by ECC-Rater per RA3.2.2 or weigh-in procedure per RA3.2.3.1

---

## Whole-House Fan (Section 150.1(c)12)

### When Required (Table 150.1-A)
Required in CZ 8-14 for new construction.

### For Additions
Additions <=1,000 SF: exempt from ventilation cooling (WHF) requirements (Exception 5 to Section 150.2(a)).

### Requirements When Applicable
- Total airflow: >=1.5 cfm per SF of conditioned floor area
- Attic vent free area: >=1 SF per 750 cfm of rated fan airflow
- Listed in Home Ventilating Institute Certified Products Directory
- Homeowner information sheet required

---

## CF-1R Mechanical Documentation

The CF-1R (Certificate of Compliance) must document:
- HVAC system type and capacity
- Manual J load calculation results (heating load, cooling load)
- Duct insulation R-value
- Duct location (conditioned/unconditioned)
- Duct leakage test requirement
- Ventilation system specifications
- Refrigerant charge verification requirement
