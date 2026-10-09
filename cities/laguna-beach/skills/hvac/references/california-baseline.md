# California Baseline — HVAC

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Residential HVAC — State Regulatory Decision Engine

This skill contains California state-level residential HVAC installation rules extracted from five Title 24 codes: CMC (mechanical), CPC (plumbing/gas), CEC (electrical), CRC (residential building), and Energy Code. It covers the full scope of residential HVAC work -- heating, cooling, ventilation, and all supporting trades.

**What this covers**: State code requirements that apply everywhere in California for residential HVAC installations. Every city must enforce at least these standards.

**What this does NOT cover**: City-specific ordinances, local permit processes, local fee schedules, or project-specific engineering. Use the city-level HVAC skill (e.g., `costa-mesa-hvac`) for those.

### How to Use This Skill

When reviewing an HVAC permit or answering an HVAC code question, follow the decision tree below. Each step tells you which reference files to load. Load only what you need -- most reviews require 3-5 reference files depending on the system type.

After loading references, check the **Quick-Reference Tables** below for the key numbers that come up in almost every HVAC review.

---

### Decision Tree Router

#### STEP 1: What Type of System Is This?

| System Type | Load These References |
|-------------|----------------------|
| **Gas furnace** (new or replacement) | `equipment-location.md`, `combustion-air.md`, `venting-chimneys.md`, `gas-piping.md`, `electrical-disconnect.md`, `energy-code-hvac.md`, `smoke-co-alarms.md` |
| **A/C condenser** (new or replacement) | `air-conditioning-refrigerant.md`, `electrical-disconnect.md`, `energy-code-hvac.md` |
| **Split system** (furnace + A/C condenser) | All references for gas furnace PLUS `air-conditioning-refrigerant.md`, `ductwork.md` |
| **Heat pump** (electric, no gas) | `equipment-location.md`, `air-conditioning-refrigerant.md`, `electrical-disconnect.md`, `energy-code-hvac.md`, `ductwork.md`, `smoke-co-alarms.md` |
| **Mini-split / ductless** | `equipment-location.md`, `air-conditioning-refrigerant.md`, `electrical-disconnect.md`, `energy-code-hvac.md` |
| **Ductwork only** (new or replacement) | `ductwork.md`, `energy-code-hvac.md` |
| **Wall heater or floor furnace** | `equipment-location.md`, `combustion-air.md`, `venting-chimneys.md`, `gas-piping.md`, `smoke-co-alarms.md` |
| **Whole house fan** | `electrical-disconnect.md` |

#### STEP 1B: What Is the Installation Location?

| Location | Additional Reference |
|----------|---------------------|
| **Attic** | `equipment-location.md` (attic section), `clearance-combustibles.md` |
| **Closet or alcove** | `clearance-combustibles.md` |
| **Garage** | `equipment-location.md` (garage section) |
| **Rooftop** | `equipment-location.md` (rooftop section) |
| **Crawl space** | `equipment-location.md` (crawl space section) |

#### STEP 2: Walk the Review Checklist

For a full HVAC permit review, check each item in order. The checklist tells you which reference file has the answer and what code section applies.

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 1 | **Equipment location valid?** | Bedroom/bathroom furnace or boiler installation follows a permitted CMC 904.2 configuration; proper access, passageway, platform per installation type | CMC 904.2, 304.4, 305.1 | `equipment-location.md` |
| 2 | **Clearance to combustibles OK?** | Per manufacturer's instructions; closet/alcove volume rule; floor installation uses a complete CMC 904.4 method or exception | CMC 303.1, 303.2, 904.4 | `clearance-combustibles.md` |
| 3 | **System properly sized?** | Load calc per ACCA Manual J; equipment selected per Manual S; capacity within limits | Energy Code 150.0(h) | `energy-code-hvac.md` |
| 4 | **Equipment efficiency meets minimum?** | SEER2/HSPF2/AFUE meets federal minimums | Energy Code 110.1 | `energy-code-hvac.md` |
| 5 | **Thermostat compliant?** | Programmable setback thermostat (4 periods/24 hr); heat pump supplementary heater controls | Energy Code 110.2(c), 110.2(b) | `energy-code-hvac.md` |
| 6 | **Gas piping correct?** (gas systems only) | Shutoff valve within 6 ft, sediment trap, proper connectors, CSST bonding, pressure test | CPC 1212.6, 1212.9, 1213.3 | `gas-piping.md` |
| 7 | **Combustion air adequate?** (gas systems only) | Indoor air volume OR outdoor openings sized to BTU load | CMC 701.1-701.11 | `combustion-air.md` |
| 8 | **Venting correct?** (gas systems only) | Type B/direct vent per listing; 5 ft above collar; proper termination height; clearance to combustibles | CMC 802.0-803.0 | `venting-chimneys.md` |
| 9 | **Ductwork compliant?** (ducted systems) | Sized per Manual D; sealed to Class A; insulated to R-6/R-8; leakage test | CMC 601.2, 603.9; Energy Code 150.2(b) | `ductwork.md` |
| 10 | **Condenser installation correct?** (A/C or heat pump) | Equipment selected for the calculated load; pad/support and anchorage compliant; refrigerant piping supported | CMC 1105.1, 1105.2, 1109.6 | `air-conditioning-refrigerant.md` |
| 11 | **Electrical disconnect provided?** | Disconnect in sight of equipment; dedicated circuit for furnace; 120V receptacle within 25 ft | CMC 301.4; CEC 422.10, 440.14 | `electrical-disconnect.md` |
| 12 | **Condensate drain installed?** | Primary drain with 1/8 in./ft slope; overflow protection (pan, switch, or secondary drain) where damage could result | CMC 310.1, 310.2 | `air-conditioning-refrigerant.md` |
| 13 | **Refrigerant charge verified?** (cooling system replacement) | Standard charge or weigh-in procedure; minimum 300 CFM/ton airflow | Energy Code 150.2(b)1F | `energy-code-hvac.md` |
| 14 | **A/C electrical requirements met?** | Disconnect rating min 115% of nameplate rated-load current or branch-circuit selection current (440.12(A)(1)); disconnect within sight and readily accessible from equipment, not on access panels or obscuring nameplates (440.14); branch circuit conductor sizing per compressor nameplate (440.32, 440.33); motor controller disconnect accessible (440.13); A/C equipment anchored/secured including seismic (CEC 440.12, CMC 303.4). | CEC 440.12, 440.13, 440.14, 440.32, 440.33; CMC 303.4 | `electrical-disconnect.md` |
| 15 | **Smoke and CO alarms compliant?** | Smoke alarms in all required locations (retrofit on permitted work); CO alarms where fuel appliances exist | CRC R310, R311 | `smoke-co-alarms.md` |

#### STEP 3: Output the Review Result

For each checklist item, output one of:
- **PASS** -- requirement met, cite code section
- **FAIL** -- requirement not met, cite code section and explain what is wrong
- **FLAG** -- cannot determine from submitted data, explain what additional info is needed
- **N/A** -- does not apply to this installation type

---

### Quick-Reference Tables

#### Attic Installation Requirements

| Requirement | Dimension | Code |
|------------|-----------|------|
| Access opening | >= 22 in. x 30 in. (or largest component) | CMC 304.4 |
| Passageway max distance | 20 ft (if headroom < 6 ft) | CMC 304.4.1 |
| Walkway width | 24 in. minimum solid floor | CMC 304.4.2 |
| Work platform | 30 in. x 30 in. at service side | CMC 304.4.3 |
| Floor under furnace | Noncombustible construction/finish or fire-resistive slab/arch, with no combustible material against the underside; listed-unit or approved-protection exceptions allowed | CMC 904.4 |
| Light and receptacle | Required near unit; switch at access opening | CMC 304.4.4 |
| Wiring protection | Guard strip within 6 ft of scuttle | CEC 334.23 |
| Weight limit (conventional framing) | 350 lbs max without engineering | Structural practice |

#### Combustion Air Sizing

| Method | Sizing Rule |
|--------|-------------|
| Indoor air only (standard) | 50 cu ft per 1,000 BTU/h room volume |
| Two openings, direct exterior or vertical ducts | 1 sq in. per 4,000 BTU/h each opening |
| Two openings, horizontal ducts | 1 sq in. per 2,000 BTU/h each opening |
| Single opening, direct exterior | 1 sq in. per 3,000 BTU/h |
| Mechanical supply | 0.35 CFM per 1,000 BTU/h |

#### Gas Vent Termination Heights

| Condition | Minimum Height |
|-----------|---------------|
| Above draft hood/flue collar (Type B/L) | 5 ft vertical |
| Above roof (slope < 6:12, vent <= 12 in.) | 12 in. |
| Above roof (vent > 12 in.) | 2 ft |
| Above forced air inlet within 10 ft | 3 ft |

#### Vent Clearance to Combustibles

| Vent Type | Clearance |
|-----------|----------|
| Type B double-wall | Per listing and manufacturer installation instructions |
| Single-wall metal pipe | Applicable CMC Table 802.7.3.3 appliance/draft-hood row and conditions |
| Direct vent | Per manufacturer |

#### Duct Leakage Limits (Energy Code)

| Scenario | Maximum Leakage |
|----------|----------------|
| Entirely new/replacement duct system | <= 5% of air handler airflow |
| Equipment replacement (total leakage) | <= 10% of air handler airflow |
| Equipment replacement (leakage to outside) | <= 7% of air handler airflow |
| Ducts in garage space | <= 6% of air handler airflow |

#### Duct Insulation by Climate Zone (Alterations)

| Climate Zone | Minimum R-Value |
|-------------|----------------|
| 3, 5-7 | R-6 |
| 1, 2, 4, 8-16 | R-8 |

#### Condensate Drain Pipe Sizing

| Equipment (Tons) | Min. Pipe Diameter |
|-----------------|-------------------|
| Up to 20 | 3/4 in. |
| 21-40 | 1 in. |
| 41-90 | 1-1/4 in. |

#### Key Clearance Dimensions

| Item | Clearance | Code |
|------|----------|------|
| Disconnect to condenser | Within sight (50 ft max) | CEC 440.14 |
| Service receptacle to equipment | Within 25 ft | CMC 301.4 |
| Garage ignition source height | >= 18 in. (unless FVIR) | CMC 305.1 |
| Gas shutoff valve to appliance | Within 6 ft | CPC 1212.6 |
| Smoke alarm to supply register | >= 36 in. | NFPA 72 29.8.3.4 |
| Working space at electrical | 30 in. x 36 in. x 6 ft 6 in. | CEC 110.26 |

> **Condenser and dryer exhaust:** CEnC §150.0(h)3A requires installed air-conditioner and heat-pump outdoor condensing units to be at least 5 feet from the outlet of any dryer vent. CMC 311.2 governs air filters and is not the source of this clearance.

---

### Key Principles

1. **Manufacturer's instructions govern clearances**: Where the code says "per manufacturer's installation instructions," those instructions are the minimum standard. The code sets fallback values only when manufacturer data is unavailable. Always check the equipment spec sheet first.

2. **HVAC is multi-trade**: A single HVAC permit touches mechanical (CMC), plumbing (CPC for gas piping), electrical (CEC), energy (Part 6), and building/life safety (CRC). Miss any trade and the review is incomplete.

3. **Gas vs. electric changes everything**: Gas-fired equipment triggers combustion air, venting, gas piping, sediment trap, and CO alarm requirements. Electric heat pumps skip all of these. The decision tree branches heavily on fuel type.

4. **Energy Code applies on replacement**: California requires duct leakage testing, refrigerant charge verification, setback thermostats, and minimum efficiency standards even on simple equipment replacements -- not just new construction. Section 150.2(b) is the governing section for alterations.

5. **Smoke and CO alarms are triggered by permits**: Any HVAC permit triggers smoke alarm retrofit compliance for the entire dwelling unit (CRC R310.2.2). CO alarms are required wherever fuel-fired appliances exist (CRC R311.2.1). This is frequently the most-missed item.

6. **Attic installations have the most requirements**: Access opening size, passageway length, walkway width, work platform, a complete CMC 904.4 floor method or exception, lighting, receptacle, guard strip on wiring, framing adequacy, and vent termination height all apply. Review every sub-item.

7. **Duct leakage testing has exceptions**: Systems with less than 40 linear feet of duct, previously tested systems, and asbestos-containing duct systems are exempt from leakage testing on equipment replacement (Energy Code 150.2(b)1E exceptions).

8. **Duct testing trigger conditions**: Duct leakage testing is required when (a) more than 25% of the duct system is replaced or modified per Energy Code 150.2(b)1H, (b) equipment is replaced (per 150.2(b)1E), or (c) an entirely new duct system is installed. The 25% duct replacement threshold is the most commonly encountered trigger on partial HVAC replacements. If less than 40 linear feet of duct is accessible, testing is exempt.

9. **Contractor licensing for gas piping**: A C-20 (Warm-Air Heating, Ventilating and Air Conditioning) license covers HVAC equipment and ductwork but does NOT cover gas piping work. Gas piping installation, modification, or capping requires a C-36 (Plumbing) license per CSLB regulations. For fuel-switch projects (gas-to-electric heat pump), the gas line capping must be performed by a C-36 contractor or a B (General Building) contractor with appropriate scope. This is a common licensing trap on heat pump conversions.

10. **Load calculations are required by state code**: ACCA Manual J for loads and Manual S for equipment selection are mandated by Energy Code 150.0(h). This is not just best practice -- it is California law.
