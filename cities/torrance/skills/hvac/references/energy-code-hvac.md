---
title: "Energy Code — Equipment Efficiency, Load Calcs, Thermostats"
category: "Energy Compliance"
relevance: "All HVAC installations — new and replacement"
key_code_sections: "Energy Code 110.1, 110.2(b), 110.2(c), 150.0(h), 150.0(i), 150.2(b)1C, 150.2(b)1F, 150.2(b)1G"
---

# Energy Code Requirements for HVAC

Source: 2025 California Energy Code (Title 24, Part 6), Sections 110.2, 150.0, and 150.2.

## Equipment Efficiency (Energy Code 110.1)

All HVAC equipment shall be certified to meet minimum federal efficiency standards. For residential systems under 65,000 BTU/h, the federal minimums per DOE/AHRI standards apply.

### Residential A/C and Heat Pump Minimums (Federal / DOE)

As of January 1, 2023 (DOE regional standards for the Southwest region including California). Source: 10 CFR 430.32, DOE M1 testing procedure.

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
>
> Federal minimum SEER2 ratings replaced SEER as of 1/1/2023. The 2025 Energy Code references federal minimums. For residential < 65,000 BTU/h, the federal standards govern.

### Commercial-Size Equipment (>= 65,000 BTU/h)

Minimum efficiencies per Energy Code Table 110.2-A (see EER/IEER values by size category).

---

## Space-Conditioning Load Calculations (Energy Code 150.0(h))

### Load Calculation Methods (150.0(h)1)

Building heating and cooling loads shall be determined using:
- ASHRAE Handbook (Equipment, Applications, Fundamentals volumes); OR
- SMACNA Residential Comfort System Installation Standards Manual; OR
- **ACCA Manual J**

### Design Conditions (150.0(h)2)

| Parameter | Value |
|-----------|-------|
| Indoor heating design temp | 68 deg F |
| Indoor cooling design temp | 75 deg F |
| Outdoor heating | 99.0% Heating Dry Bulb or Heating Winter Median of Extremes |
| Outdoor cooling | 1.0% Cooling Dry Bulb and Mean Coincident Wet Bulb |

### Equipment Sizing (150.0(h)5)

Equipment shall be selected in accordance with:
- **ACCA Manual S** for equipment selection
- System capacity limits per Table 150.2-A (heating) and Table 150.2-B (cooling)

#### Maximum Capacity — Alterations (Table 150.2-A / 150.2-B)

For single-speed systems:
- **Heating only**: Max capacity = Design Heating Load + 6 kBTU/h
- **Cooling only**: Max capacity = Design Cooling Load + 6 kBTU/h

For variable/multi-speed at lowest speed: 80% of design load.

**Exception**: If airflow is field-verified to be >= 350 CFM/ton, there is no maximum capacity limit.

### Outdoor Condensing Unit Clearances (150.0(h)3)

- Condenser shall have clearance of at least **5 ft from dryer vent outlet**
- A **liquid line filter drier** shall be installed if required by manufacturer

### Furnace Temperature Rise (150.0(h)4)

Central forced-air furnace installations shall be configured to operate within the manufacturer's **maximum inlet-to-outlet temperature rise** specifications.

---

## Thermostat Requirements (Energy Code 110.2(c))

All heating or cooling systems not controlled by a central EMCS shall have a **setback thermostat**.

### Setback Capabilities (110.2(c)1)

All thermostats shall have a clock mechanism allowing the occupant to **program temperature setpoints for at least 4 periods within 24 hours**.

Heat pump thermostats shall also meet the supplementary heater control requirements of Section 110.2(b).

**Exceptions** (not required to have setback thermostat):
- Gravity gas wall heaters, gravity floor heaters, gravity room heaters
- Noncentral electric heaters
- Fireplaces or decorative gas appliances
- Wood stoves
- Room air conditioners and room air-conditioner heat pumps

---

## Heat Pump Supplementary Heater Controls (Energy Code 110.2(b))

Heat pumps with supplementary (backup) electric resistance heaters shall have controls that:
1. Prevent supplementary heater operation when the heat pump alone can meet the load
2. Cut-on temperature for heat pump heating is HIGHER than cut-on for supplementary heating
3. Cut-off temperature for heat pump heating is HIGHER than cut-off for supplementary heating

**Exceptions**: Supplementary heater may operate during:
- Defrost cycles
- Transient periods (start-ups, setpoint advance) if controls provide intelligent recovery/staging

---

## Altered Space-Heating Systems (Energy Code 150.2(b)1G)

Altered or replacement space-heating systems shall **NOT use electric resistance as the primary heat source**.

**Exceptions**:
1. Nonducted electric resistance, if the existing system is already electric resistance
2. Ducted electric resistance, if existing is electric resistance AND no ducted cooling is being replaced/installed
3. Electric resistance in Climate Zone 7 or 15, if existing is electric resistance

---

## Refrigerant Charge Verification (Energy Code 150.2(b)1F)

When a space-conditioning system with mechanical cooling is altered by replacing refrigerant-containing components (compressor, coil, etc.):

1. **All thermostats** shall be replaced with setback thermostats per 110.2(c)
2. **Minimum system airflow**: >= 300 CFM/ton (or >= 250 CFM/ton for small duct high-velocity)
3. **Refrigerant charge** shall be verified via:
   - Standard charge verification procedure (RA3.2.2); OR
   - Weigh-in charging procedure (RA3.2.3.1) with ECC-Rater verification

---

## Minimum Airflow Rate (Energy Code 150.2(b)1Fiia)

| System Type | Minimum Airflow |
|------------|----------------|
| Standard ducted system | >= 300 CFM/ton |
| Small duct high-velocity | >= 250 CFM/ton |

---

## Quick Reference — Energy Code Checklist

| Item | Requirement | Code |
|------|------------|------|
| Load calculation | ACCA Manual J (or ASHRAE/SMACNA) | 150.0(h)1 |
| Equipment selection | ACCA Manual S | 150.0(h)5 |
| Thermostat | Programmable setback (4 periods/24 hr) | 110.2(c) |
| Heat pump backup controls | Prevent unnecessary supplementary heat | 110.2(b) |
| Refrigerant charge verification | Standard or weigh-in procedure, ECC-Rater | 150.2(b)1F |
| Minimum airflow | >= 300 CFM/ton (ducted) | 150.2(b)1Fiia |
| Max capacity (single-speed) | Design load + 6 kBTU/h | Table 150.2-A/B |
| No electric resistance primary | Unless replacing existing electric resistance | 150.2(b)1G |
| Furnace temperature rise | Per manufacturer's specs | 150.0(h)4 |
