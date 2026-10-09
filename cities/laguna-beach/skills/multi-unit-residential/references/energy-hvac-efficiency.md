---
title: "Energy Code Sections 160.2, 160.3, 170.2(c) — HVAC Efficiency, Ventilation, and Compliance Paths for Multifamily"
category: energy
relevance: "All multi-unit residential projects — HVAC equipment efficiency minimums, duct insulation and sealing, thermostat requirements, ventilation and compartmentalization, refrigerant charge verification, and performance vs. prescriptive compliance paths. These requirements apply to every dwelling unit and common area in a multifamily building."
key_code_sections: "CEC 110.1, 110.2(b), 110.2(c), 160.2(a), 160.2(b), 160.3(a), 160.3(b), 170.1, 170.2(c), Table 170.2-K"
---

# HVAC Efficiency Requirements — Multifamily Buildings

Source: 2025 California Energy Code (Title 24, Part 6), Sections 160.2, 160.3, 170.1, 170.2(c), and Table 170.2-K (Subchapters 10 and 11, Multifamily Buildings). Effective January 1, 2026.

This reference covers the HVAC-specific energy requirements for multifamily buildings: equipment efficiency minimums, ventilation and compartmentalization, duct insulation and sealing, thermostat controls, refrigerant charge verification, and the two compliance paths (performance and prescriptive). Envelope energy requirements are in the companion file `energy-envelope.md`; mechanical code duct/damper/fire protection requirements are in `mechanical-hvac.md`.

---

## Section 160.2 — Ventilation and Compartmentalization (Mandatory)

Section 160.2 is mandatory for all multifamily buildings regardless of compliance path. Every attached dwelling unit must comply with 160.2(b); common use areas must comply with 160.2(c).

### Low-Rise vs. High-Rise Testing Distinction

- **Low-rise (3 habitable stories or fewer):** Field verification per Residential Appendices RA3.7, RA3.8. Testing by ECC-Rater. (CEC 160.2(a)1)
- **High-rise (4 or more habitable stories):** Field verification per Nonresidential Appendices NA1, NA2. Testing by ECC-Rater or certified Mechanical Acceptance Test Technician (CMATT). (CEC 160.2(a)1)

### Compartmentalization — Air Leakage (160.2(b)2Aivb2)

Each dwelling unit must demonstrate:

- **Air leakage rate not exceeding 0.3 cfm at 50 Pa per sq ft of dwelling unit envelope surface area**
- Confirmed by ECC-Rater field verification and diagnostic testing per Reference Appendix RA3.8 (low-rise) or NA2.3 (high-rise)
- For buildings with 4+ habitable stories, testing may alternatively be performed by a certified CMATT per NA1.9

This is a per-unit test. For a 35-unit project, every unit is tested individually. Sealing quality of party walls, floors, ceilings, exterior walls, and all penetrations (electrical, plumbing, HVAC) directly determines pass/fail.

### Ventilation System Type (160.2(b)2Aivb1)

All dwelling units must use **balanced or supply ventilation** (not exhaust-only). Balanced systems with heat or energy recovery (HRV/ERV) serving a single dwelling unit shall have fan efficacy of **1.0 W/cfm or less**. (CEC 160.2(b)2Aivb1)

All dwelling units in a multifamily building must use the **same whole-dwelling unit ventilation system type**. (CEC 160.2(b)2Aivb)

### Whole-Dwelling Ventilation Rate (Equation 160.2-B)

**Q_tot = 0.03 x A_floor + 7.5 x (N_br + 1)**

Where:
- A_floor = dwelling unit floor area (sq ft)
- N_br = number of bedrooms (minimum 1)

| Unit Size | Bedrooms | Min Ventilation (cfm) |
|-----------|----------|-----------------------|
| 750 sq ft | 1 | 37.5 |
| 1,000 sq ft | 2 | 52.5 |
| 1,200 sq ft | 2 | 58.5 |
| 1,200 sq ft | 3 | 66.0 |
| 1,500 sq ft | 3 | 75.0 |

### Air Filtration (160.2(b)1)

All mechanical systems supplying air through ductwork exceeding 10 ft, mechanical supply-only ventilation systems, and balanced ventilation systems shall be provided with MERV 13 or higher air filters. (CEC 160.2(b)1C)

Filter specifications:
- **Minimum depth**: 2-inch nominal, or 1-inch nominal sized per Equation 160.2-A (max face velocity 150 ft/min)
- **Maximum clean-filter pressure drop**: Determined by system design (2-inch) or 25 Pa / 0.1 in. w.c. (1-inch sized per equation)
- Filter racks or grilles shall be gasketed/sealed to prevent bypass
- All filter locations shall be labeled with design airflow rate and max clean-filter pressure drop

### Local Exhaust — Kitchens and Bathrooms (160.2(b)2Avi)

| Space | Demand-Controlled | Continuous |
|-------|-------------------|------------|
| **Enclosed kitchen** | Per Table 160.2-E and 160.2-G (capture efficiency or cfm by unit size) | 5 ACH based on kitchen volume |
| **Nonenclosed kitchen** | Per Table 160.2-E and 160.2-G | N/A (demand-controlled required) |
| **Bathroom** | 50 cfm | 20 cfm |

Kitchen range hood requirements vary by dwelling unit floor area and fuel type (CEC Table 160.2-G):

| Unit Floor Area | Hood Over Electric Range | Hood Over Gas Range |
|-----------------|------------------------|---------------------|
| > 1,500 sq ft | 50% CE or 110 cfm | 70% CE or 180 cfm |
| > 1,000-1,500 sq ft | 50% CE or 110 cfm | 80% CE or 250 cfm |
| 750-1,000 sq ft | 55% CE or 130 cfm | 85% CE or 280 cfm |
| < 750 sq ft | 65% CE or 160 cfm | 85% CE or 280 cfm |

CE = capture efficiency per ASTM E3087.

### Central Ventilation System Duct Leakage (160.2(b)2C)

Central ventilation ducts serving multiple dwelling units and providing continuous or balanced ventilation shall:
- Meet CMC Section 603.10 duct sealing requirements
- Have leakage no greater than **6% of design airflow rate**
- Leakage tested at 25 Pa (serving 6 or fewer units) or 50 Pa (serving more than 6 units)
- Confirmed per NA7.18.3

Exception: Not required for buildings with 3 or fewer habitable stories in Climate Zone 6. (Exception to CEC 160.2(b)2C)

### Window Operation Prohibition (160.2(b)2Ai)

Window operation is **not** a permissible method of providing whole-dwelling ventilation. Mechanical ventilation is required. (CEC 160.2(b)2Ai)

---

## Section 160.3 — Space-Conditioning Systems (Mandatory)

### Dwelling Unit Thermostats (160.3(a)1, 110.2(c))

All heating or cooling systems not controlled by a central EMCS shall have a **setback thermostat** per Section 110.2(c). (CEC 160.3(a)1)

Setback thermostat requirements:
- Clock mechanism allowing the occupant to **program temperature setpoints for at least 4 periods within 24 hours** (CEC 110.2(c)1)
- Heat pump thermostats shall also meet supplementary heater control requirements of Section 110.2(b)

**Exceptions** (not required to have setback thermostat):
- Gravity gas wall/floor/room heaters
- Noncentral electric heaters
- Fireplaces or decorative gas appliances
- Wood stoves
- Room air conditioners and room air-conditioner heat pumps

### Heat Pump Supplementary Heater Controls (110.2(b))

Heat pumps with backup electric resistance heaters shall have controls that:
1. Prevent supplementary heater operation when the heat pump alone can meet the load
2. Supplementary heating cut-on temperature is **lower** than heat pump cut-on
3. Supplementary heating cut-off temperature is **lower** than heat pump cut-off

Supplementary heater may operate during defrost cycles and transient start-up periods if controls provide intelligent recovery/staging.

### Common Area Controls (160.3(a)2)

Common use area heating/cooling systems shall comply with 160.3(a)2A through 160.3(a)2J:
- **Individual thermostatic control** for each zone (160.3(a)2A)
- Heating thermostat settable down to **55 deg F or lower** (160.3(a)2Bi)
- Cooling thermostat settable up to **85 deg F or higher** (160.3(a)2Bii)
- **Deadband of at least 5 deg F** between heating and cooling setpoints (160.3(a)2Biii)
- **Shut-off and reset controls** with automatic time switch, occupancy sensor, or 4-hour timer (160.3(a)2D)
- **Economizer FDD** for air handlers > 33,000 BTU/h with economizer (160.3(a)2H)
- **DDC** for systems > 300 kBTU/h serving more than 3 zones (Table 160.3-C)
- **Optimum start/stop** for systems with DDC to zone level (160.3(a)2J)

### Building Load Calculations (160.3(b)1-2)

Heating and cooling loads for dwelling units shall be determined using:
- ASHRAE Handbook; OR
- SMACNA Residential Comfort System Installation Standards Manual; OR
- **ACCA Manual J**

Design conditions:
| Parameter | Value |
|-----------|-------|
| Indoor heating design temp | 68 deg F |
| Indoor cooling design temp | 75 deg F |
| Outdoor heating | 99.0% Heating Dry Bulb or Winter Median of Extremes |
| Outdoor cooling | 1.0% Cooling Dry Bulb and Mean Coincident Wet Bulb |

(CEC 160.3(b)1, 160.3(b)2)

### Outdoor Condensing Unit Clearance (160.3(b)3)

- Minimum **5 ft clearance** from dryer vent outlet (CEC 160.3(b)3A)
- **Liquid line filter drier** required if specified by manufacturer (CEC 160.3(b)3B)

---

## Duct Insulation and Sealing Requirements (Mandatory)

### Dwelling Unit Duct Insulation (160.3(b)5A)

Supply-air and return-air ducts and plenums of space conditioning systems shall be insulated:
- **Minimum R-6.0** for all ducts (CEC 160.3(b)5Aiia)
- No insulation required where the duct system is located **entirely in conditioned space**, confirmed by field verification per RA3.1.4.3.8 (CEC 160.3(b)5Aiib)

Exception: Portions of ducts in conditioned space below the ceiling separating occupiable space from the attic are not required to be insulated if the duct is entirely inside the thermal envelope AND all penetrations into unconditioned space are draft stopped and air-sealed with R-6.0 insulation. (Exception to CEC 160.3(b)5Aiia)

### Common Area Duct Insulation (160.3(c)2B)

Ducts in common areas located in unconditioned spaces shall be insulated to **minimum R-8**:
- Outdoors
- Space between roof and insulated ceiling
- Space directly under roof with fixed vents
- Unconditioned crawl space
- Other unconditioned spaces

Supply-air ducts NOT in those spaces (including ducts in concrete slab) shall be insulated to **minimum R-4.2** or enclosed in directly conditioned space. (CEC 160.3(c)2B)

### Prescriptive Duct Insulation by Climate Zone (Table 170.2-K)

| Climate Zone | Min Duct Insulation in Unconditioned Space |
|-------------|-------------------------------------------|
| CZ 1, 4, 8-16 | **R-8** |
| CZ 2, 3, 5, 6, 7 | **R-6** |

### Duct Sealing and Leakage Testing — Dwelling Units (160.3(b)5K)

For forced air duct systems serving individual dwelling units:
- **Total leakage** shall not exceed **12%** of air handler airflow (per RA3.1.4.3.1); OR
- **Leakage to outside** shall not exceed **6%** of air handler airflow (per RA3.1.4.3.4)

(CEC 160.3(b)5K)

Exception 1: For buildings with 4+ habitable stories, installer self-certifies testing per applicable procedures (no ECC-Provider data registry required). (Exception 1 to CEC 160.3(b)5K)

Exception 2: Dwelling units in buildings with 4+ habitable stories in Climate Zones 1, 3, 5, and 7. (Exception 2 to CEC 160.3(b)5K)

### System Airflow Rate and Fan Efficacy (160.3(b)5L)

Space-conditioning systems supplying cooling to an individual dwelling unit shall demonstrate:
- **Minimum 350 cfm per ton** of nominal cooling capacity through return grilles (CEC 160.3(b)5Lii)
- **Fan efficacy** not exceeding:
  - 0.45 W/cfm for gas furnace air-handling units
  - 0.58 W/cfm for non-gas-furnace air-handling units
- Small duct high-velocity systems: minimum **250 cfm per ton**, max fan efficacy **0.62 W/cfm** (CEC 160.3(b)5Liv)

### Duct Construction Standards

All duct joints and seams:
- Metal connections mechanically fastened (CEC 160.3(b)5A)
- Sealed with mastic, UL 181/181A/181B compliant tape, or UL 723 aerosol sealant (CEC 160.3(b)5Aiv)
- Openings > 1/4 inch require mastic plus mesh or tape combination
- Building cavities shall **not** be used as ducts or plenums (CEC 160.3(b)5Av)
- Cloth back rubber adhesive duct tape prohibited unless used with mastic and drawbands

---

## HVAC Equipment Efficiency Minimums

### Federal Minimums Apply (CEC 110.1, 170.2(c)3B)

All space heating and cooling equipment shall comply with minimum Appliance Efficiency Regulations per Sections 110.0 through 110.2. For residential-size equipment (under 65,000 BTU/h), federal DOE minimum standards govern. The Energy Code does not set equipment efficiency above federal minimums for the prescriptive path, but the performance path (Section 170.1) may require higher-rated equipment to meet the energy budget. (CEC 170.2(c)3B)

Table 170.2-K specifies "MIN" for SEER2, HSPF2, and AFUE across all 16 climate zones, meaning the federal minimum is the prescriptive standard.

### Residential Equipment Minimums (Federal / DOE, effective 1/1/2023)

Southwest region (all California climate zones). Source: 10 CFR 430.32, DOE M1 testing procedure.

| Equipment Type | Min SEER2 | Min EER2 | Min HSPF2 | Min AFUE |
|---------------|-----------|----------|-----------|----------|
| Central A/C, split system (<45k BTU) | 14.3 | 11.7 | — | — |
| Central A/C, split system (≥45k BTU) | 13.8 | 11.2 | — | — |
| Central A/C, single package | 13.4 | 10.6 | — | — |
| Heat pump, split system (all capacities) | 14.3 | — | 7.5 | — |
| Heat pump, single package | 13.4 | — | 6.7 | — |
| Mini-split heat pump | 14.3 | — | 7.5 | — |
| Gas furnace | — | — | — | 80% |

> **EER2 breakpoint note:** In the Southwest region, the EER2 minimum depends on the unit's rated SEER2. Units with SEER2 < 15.2 must meet the higher EER2 shown above. Units with SEER2 ≥ 15.2 qualify for a lower EER2 (9.8 for split AC). The 15.2 value is a tier divider for EER2 requirements, NOT a minimum SEER2 rating.

SEER2 and HSPF2 replaced SEER and HSPF as of January 1, 2023 under the DOE M1 testing procedure. The 2025 Energy Code references these federal minimums.

### Commercial-Size Equipment (>= 65,000 BTU/h)

Minimum efficiencies per Energy Code Table 110.2-A (EER/IEER values by size category). Common area HVAC systems may exceed this threshold and must meet the applicable commercial minimums.

### Prescriptive Heating System Type Requirements (170.2(c)3A)

| Building Type | CZ 1 | CZ 2-15 | CZ 16 |
|--------------|-------|---------|-------|
| **3 stories or fewer** | Heat pump | Heat pump | A/C with furnace |
| **4+ stories** | Dual-fuel heat pump | Heat pump | Dual-fuel heat pump |

(CEC 170.2(c)3Ai, 170.2(c)3Aii)

Exception: A supplemental heating unit may be installed if capacity does not exceed **2 kW or 7,000 BTU/h** and is controlled by a time-limiting device not exceeding 30 minutes.

Systems that cannot meet these prescriptive requirements (e.g., multi-zone systems, central boilers/chillers) shall comply with the **performance path** (Section 170.1).

---

## Refrigerant Charge Verification (170.2(c)3Bi)

When refrigerant charge verification or fault indicator display (FID) is required by Table 170.2-K, the system shall comply with verification procedures.

### Climate Zones Requiring Refrigerant Charge Verification (Table 170.2-K)

| Requirement | Climate Zones |
|------------|--------------|
| **Required (REQ)** | CZ 2, 8, 9, 10, 11, 12, 13, 14, 15 |
| **Not Required (NR)** | CZ 1, 3, 4, 5, 6, 7, 16 |

### Verification Procedure for Air-Cooled Systems (170.2(c)3Bia)

For air-cooled air conditioners and air-source heat pumps (ducted splits, packaged, small duct high-velocity, mini-splits):

1. **Measurement access holes (MAH)** installed per RA3.2.2.3
2. **System airflow rate** confirmed:
   - Standard systems: >= 350 cfm per ton
   - Small duct high-velocity: >= 250 cfm per ton
3. **Refrigerant charge** verified via:
   - Standard charge procedure per RA3.2.2 (installer and ECC-Rater); OR
   - Weigh-in charging procedure per RA3.2.3.1 (installer charges, ECC-Rater verifies per RA3.2.2)

Exception: Packaged systems factory-precharged and unaltered do not require field charge verification. Installer shall certify the precharged status. (Exception 1 to CEC 170.2(c)3Bi)

Exception: For buildings with 4+ habitable stories, installer self-certifies (no ECC-Provider data registry required). (Exception 2 to CEC 170.2(c)3Bi)

### Fault Indicator Display (FID) (170.2(c)3Bvi)

All HRV/ERV systems serving individual dwelling units shall have a **fault indicator display (FID)** that is manufacturer certified per Joint Appendix JA17.4. The FID certification shall be verified by an ECC-Rater. (CEC 170.2(c)3Bvi)

---

## Balanced Ventilation with Heat/Energy Recovery (170.2(c)3Biv)

### Climate Zones Requiring HRV/ERV (CZ 1, 2, 4, 11-14, 16)

In these climate zones, balanced ventilation systems must use HRV or ERV with:

**Individual dwelling unit systems** (CEC 170.2(c)3Biva):
- Minimum **sensible recovery efficiency of 67%** (rated at 32 deg F)
- Fan efficacy **<= 0.6 W/cfm**
- Field verified per RA3.7.4.4 (low-rise) or NA2.2.4.1.5 (high-rise)

**Central systems serving multiple units in 4+ story buildings** (CEC 170.2(c)3Bivb):
- Minimum **sensible recovery efficiency or effectiveness of 67%** (rated at 32 deg F)
- Fan power per Section 170.2(c)4A
- **Recovery bypass** or control to economize with ventilation air based on outdoor temperature limits in Table 170.2-G
- Field verified per NA7.18.4

### Climate Zones 5-10 and 15 — Non-HRV/ERV Balanced Ventilation (170.2(c)3Bv)

In buildings with 3 or fewer habitable stories where a heat pump is installed per 170.2(c)3Ai, balanced ventilation systems without HRV/ERV shall have fan efficacy **<= 0.4 W/cfm**. (CEC 170.2(c)3Bv)

### Prescriptive Fan Efficacy by Climate Zone (Table 170.2-K)

| Component | CZ 1, 2, 4, 11-14, 16 | CZ 3 | CZ 5-10, 15 |
|-----------|----------------------|-------|-------------|
| HRV/ERV sensible recovery efficiency | 0.67 | NR | NR |
| HRV/ERV fan efficacy | 0.6 W/cfm | 1.0 W/cfm | 1.0 W/cfm |
| Non-HRV/ERV fan efficacy | NR | NR | 0.4 W/cfm |

---

## Duct and Air Handler Location (170.2(c)3Bii)

All space-conditioning systems shall meet one of:

**Option A — High performance attics** (170.2(c)3Biia): Air handlers or ducts in ventilated attic spaces when the roof and ceiling insulation meets Option B in Table 170.2-A.

**Option B — Conditioned space** (170.2(c)3Biib): Duct systems and air handlers located in conditioned space, confirmed by field verification per RA3.1.4.3.8.

Gas heating appliances in conditioned spaces must meet CMC Chapter 7 combustion air requirements.

### HVAC System Bypass Ducts Prohibited (170.2(c)3C)

Bypass ducts that deliver conditioned supply air directly to the return duct airflow shall **not** be used. (CEC 170.2(c)3C)

---

## Pipe Insulation — Space-Conditioning Systems (160.3(c)1)

All refrigerant suction, chilled water, brine, steam, steam condensate, and hot water fluid distribution piping for space-conditioning systems shall be insulated per Table 160.3-D:

| Fluid Temperature Range | Pipe < 1 in. | Pipe 1 to < 1.5 in. | Pipe 1.5 to < 4 in. | Pipe 4+ in. |
|------------------------|-------------|--------------------|--------------------|------------|
| 105-140 deg F (heating) | 1.0 in. | 1.5 in. | 1.5 in. | 1.5 in. |
| 40-60 deg F (cooling) | 0.75 in. | 0.75 in. | 1.0 in. | 1.0 in. |

(CEC 160.3(c)1, Table 160.3-D)

Exception: Heat pump refrigerant vapor line requires minimum **0.75 in. or R-6.0 insulation**; no insulation required on refrigerant liquid line. (Exception to CEC 160.3(c)1Aii)

Insulation exposed to weather shall be protected with a water-retardant, UV-shielding cover. Chilled water and refrigerant suction piping outside conditioned space shall include a Class I or Class II vapor retarder.

---

## Performance vs. Prescriptive Compliance Paths (Sections 170.1, 170.2)

### General Rule (170.0(a))

All multifamily buildings must meet:
1. Appliance efficiency requirements (Sections 110.0-110.10)
2. Mandatory requirements (Section 160.0)
3. **Either** the performance standards (Section 170.1) **or** the prescriptive standards (Section 170.2)

### Performance Path — Section 170.1

A building complies if its calculated energy consumption (proposed design) is **no greater than the energy budget** (standard design), using CEC-certified compliance software. (CEC 170.1)

The energy budget has two components:
- **Efficiency LSC**: Sum of long-term system cost for space conditioning, water heating, mechanical ventilation, lighting, and self-utilization credit (CEC 170.1(a)1A)
- **Total LSC**: Efficiency LSC plus PV, battery storage (BESS), and demand flexibility energy (CEC 170.1(a)1B)
- **Source energy budget**: Determined using standard design with consumer gas/propane water heater (CEC 170.1(a)2)

The performance path allows trade-offs: a less efficient HVAC system can be offset by better envelope, more PV, or other measures, so long as total energy consumption stays within budget.

**Field verification when performance requires above-minimum equipment** (170.1(b)):

| Feature | Field Verification |
|---------|-------------------|
| SEER2/HSPF2/EER2 above Table 170.2-K minimum | Per RA3 applicable sections |
| Variable capacity heat pump (VCHP) option | Per RA3.4.4.3 |
| Low leakage air handler | Per RA3.1.4.3.9 |
| Heat pump rated heating capacity (47 deg F, 17 deg F) | Per RA3.4.4.2 |
| Dwelling unit enclosure leakage below standard design | Per RA3.8 |
| Quality insulation installation (QII) | Per RA3.5 |

### Prescriptive Path — Section 170.2

A building complies by meeting **all** requirements for the applicable climate zone shown in Table 170.2-A (envelope) and Table 170.2-K (mechanical). (CEC 170.2)

The prescriptive path is deterministic: no trade-offs. Each component must individually meet its minimum. For HVAC:
- Equipment efficiency at federal minimum (SEER2, HSPF2, AFUE = "MIN" in Table 170.2-K)
- Heating system type as specified by climate zone (heat pump required in most zones)
- Duct insulation, sealing, and leakage per mandatory sections
- Refrigerant charge verification where required
- HRV/ERV with specified recovery efficiency in applicable climate zones
- All mandatory ventilation and compartmentalization requirements

### When to Use Which Path

| Scenario | Recommended Path |
|----------|-----------------|
| Standard split systems meeting all prescriptive requirements | **Prescriptive** — simpler, no modeling needed |
| Central boiler/chiller systems | **Performance** — required per 170.2(c)3A |
| Multi-zone systems | **Performance** — required per 170.2(c)3A |
| Client wants to trade envelope for better HVAC | **Performance** — allows trade-offs |
| Client wants minimum-spec HVAC with extra PV | **Performance** — PV offsets in total LSC |

---

## 35-Unit Project — Practical Application

For a typical 35-unit attached townhome/apartment project:

1. **Individual split systems typical**: Each unit gets its own heat pump (split system or mini-split). At 14.3 SEER2 / 7.5 HSPF2, the federal minimum meets prescriptive requirements in all climate zones. (Table 170.2-K: SEER2 = MIN, HSPF2 = MIN)

2. **Compartmentalization testing**: All 35 units tested individually for air leakage at **0.3 cfm at 50 Pa per sq ft of envelope area**. This is the single most common field failure on multifamily projects. Seal all penetrations through unit boundaries before testing. (CEC 160.2(b)2Aivb2)

3. **Ventilation**: Each unit requires balanced or supply ventilation with calculated cfm per Equation 160.2-B. All units must use the same ventilation system type. For CZ 8 (Southern California coastal), HRV/ERV is not required prescriptively but may be used. (CEC 160.2(b)2Aivb)

4. **Thermostat**: Every unit requires a programmable setback thermostat with at least 4-period/24-hour capability. Heat pump thermostats must prevent unnecessary supplementary heating. (CEC 110.2(c), 110.2(b))

5. **Duct insulation**: R-8 minimum in unconditioned spaces (CZ 8 per Table 170.2-K); R-6 minimum in all other locations unless entirely in conditioned space.

6. **Duct leakage**: Total leakage <= 12% of air handler airflow, or leakage to outside <= 6%. Each unit tested individually. (CEC 160.3(b)5K)

7. **Refrigerant charge verification**: Required in CZ 8. Standard charge procedure or weigh-in with ECC-Rater verification. Measurement access holes required. Minimum 350 cfm/ton airflow. (CEC 170.2(c)3Bia, Table 170.2-K)

8. **Common area HVAC**: Lobby, corridors, fitness rooms, etc. require individual zone controls, shut-off/reset controls, and economizer FDD if applicable. Duct sealing to Seal Class A with leakage testing per NA7.5.3. (CEC 160.3(a)2, 160.3(c)2H)

9. **System airflow**: 350 cfm/ton minimum through return grilles, fan efficacy <= 0.58 W/cfm (non-gas-furnace AHU). Confirmed by field verification. (CEC 160.3(b)5L)

10. **Compliance path decision**: Individual heat pump split systems with standard ductwork typically qualify for the prescriptive path. Central plant systems (boiler/chiller) or multi-zone systems must use the performance path and energy modeling software. (CEC 170.2(c)3A)

---

## Cross-References

| Topic | Reference |
|-------|-----------|
| Mandatory envelope insulation U-factors and fenestration | `energy-envelope.md` |
| Mechanical code duct penetrations, fire/smoke dampers, compartmentalization | `mechanical-hvac.md` |
| Residential HVAC equipment efficiency (single-family context) | `../../hvac/references/energy-code-hvac.md` |
| Ductwork sizing, sealing, and materials | `../../hvac/references/ductwork.md` |
| Combustion air for gas-fired equipment | `../../hvac/references/combustion-air.md` |
| Equipment location (attic, crawl space, garage) | `../../hvac/references/equipment-location.md` |
| Plumbing fixture counts and water heating | `plumbing-fixtures.md` |
| CALGreen mandatory measures | `calgreen-mandatory.md` |

---

## Key Code Sections

| Code | Section | Topic |
|------|---------|-------|
| CEC | 110.1 | Appliance efficiency — federal minimums govern |
| CEC | 110.2(b) | Heat pump supplementary heater controls |
| CEC | 110.2(c) | Setback thermostat — programmable, 4 periods/24 hr |
| CEC | 160.2(a)1 | Low-rise vs. high-rise testing protocol distinction |
| CEC | 160.2(b)1 | Air filtration — MERV 13 minimum |
| CEC | 160.2(b)2Aivb1 | Balanced or supply ventilation required; HRV/ERV fan efficacy <= 1.0 W/cfm |
| CEC | 160.2(b)2Aivb2 | Compartmentalization — 0.3 cfm at 50 Pa per sq ft envelope |
| CEC | 160.2(b)2Avi | Local exhaust — kitchen and bathroom rates |
| CEC | 160.2(b)2C | Central ventilation duct leakage — 6% of design airflow |
| CEC | 160.3(a)1 | Dwelling unit thermostat — setback per 110.2(c) |
| CEC | 160.3(a)2 | Common area controls — zone thermostats, shut-off, reset, DDC |
| CEC | 160.3(b)1-2 | Load calculations — Manual J, design conditions 68/75 deg F |
| CEC | 160.3(b)3 | Outdoor condensing unit — 5 ft from dryer vent |
| CEC | 160.3(b)5Aii | Duct insulation — R-6 minimum (dwelling units) |
| CEC | 160.3(b)5K | Duct leakage — 12% total or 6% to outside |
| CEC | 160.3(b)5L | Airflow >= 350 cfm/ton, fan efficacy <= 0.58 W/cfm |
| CEC | 160.3(c)1 | Pipe insulation — Table 160.3-D by fluid temp and pipe diameter |
| CEC | 160.3(c)2B | Common area duct insulation — R-8 in unconditioned space |
| CEC | 170.1 | Performance path — energy budget via certified software |
| CEC | 170.1(a) | Energy budget — Efficiency LSC + Total LSC + source energy |
| CEC | 170.1(b) | Field verification for above-minimum equipment |
| CEC | 170.2(c)3A | Prescriptive heating system type — heat pump required most CZs |
| CEC | 170.2(c)3Bi | Refrigerant charge verification — climate zone dependent |
| CEC | 170.2(c)3Bii | Duct/AHU location — conditioned space or high-performance attic |
| CEC | 170.2(c)3Biv | HRV/ERV requirements — CZ 1, 2, 4, 11-14, 16 |
| CEC | 170.2(c)3Bvi | Fault indicator display (FID) for HRV/ERV — per JA17.4 |
| CEC | 170.2(c)3C | Bypass ducts prohibited |
| CEC | Table 170.2-K | Mechanical component package by climate zone |
