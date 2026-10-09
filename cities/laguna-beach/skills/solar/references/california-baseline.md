# California Baseline — Solar PV

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Residential Solar PV -- State Regulatory Decision Engine

This skill contains California state-level residential solar PV installation rules extracted from the 2025 California Electrical Code (CEC), California Fire Code (CFC), and California Residential Code (CRC). It covers the most common permit type: grid-tied, flush-mounted, residential rooftop solar PV systems with or without energy storage.

**What this covers**: State electrical, fire, and building code -- the requirements that apply everywhere in California. Every city must enforce at least these standards.

**What this does NOT cover**: City-specific ordinances, expedited/insta-permit processes, local fee schedules, utility interconnection agreements, or project-specific structural engineering. Use the city-level solar skill (e.g., `costa-mesa-solar`) for those.

### How to Use This Skill

When reviewing a solar PV permit or answering a solar code question, follow the decision tree below. Each step tells you which reference files to load. Load only what you need -- most reviews require 2-4 reference files, not all of them.

After loading references, check the **Quick-Reference Tables** below for the key numbers that come up in almost every solar PV review.

---

### Decision Tree Router

#### STEP 1: What Type of Review Is This?

| Review Type | Load These References |
|-------------|----------------------|
| **Full permit review** (standard plan form data in, pass/fail out) | `pv-systems-690.md`, `interconnection-705.md`, `fire-setbacks-cfc.md`, `wire-sizing-solar.md` |
| **Microinverter/AC module standard plan** | `pv-systems-690.md`, `interconnection-705.md`, `wire-sizing-solar.md` |
| **Wire/conduit sizing question only** | `wire-sizing-solar.md` |
| **Fire setback or access pathway question** | `fire-setbacks-cfc.md` |
| **Rapid shutdown question** | `pv-systems-690.md` (Section 690.12) |
| **Interconnection / busbar / 120% rule question** | `interconnection-705.md` |
| **Grounding and bonding question** | `grounding-bonding-690.md` |
| **Structural / roof loading question** | `structural-roof-crc.md` |
| **Energy Storage System (ESS) question** | `ess-requirements.md` |
| **Labeling and marking question** | `labeling-marking-690.md` |
| **General solar code question** | `pv-systems-690.md` |

#### STEP 2: Walk the Review Checklist

For a full permit review, check each item in order. The checklist tells you which reference file has the answer and what code section applies.

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 1 | **System type identified?** | Microinverter, AC module, or string inverter; number of modules, branches, total AC power rating | CEC 690.1, 690.2, 690.6 | `pv-systems-690.md` |
| 2 | **Equipment listed?** | Modules listed per UL 1703 or UL 61730; inverters listed per UL 1741; mounting per UL 2703 | CEC 690.4(B), CRC R329.3.1 | `pv-systems-690.md` |
| 3 | **Max DC voltage correct?** | Voc x temperature correction factor (Table 690.7(A)) does not exceed 600V for 1- and 2-family dwellings | CEC 690.7, 690.7(A) | `pv-systems-690.md` |
| 4 | **Circuit sizing correct?** | Branch circuit conductors sized at 125% of max current; OCPD rated per 690.9(B); conduit sized for conductor fill | CEC 690.8, 690.9, 310.16 | `wire-sizing-solar.md` |
| 5 | **Ambient temperature correction applied?** | Rooftop conductors derated for elevated temps (22C adder for rooftop, Table 690.31(A) correction factors) | CEC 690.31(A), Table 310.16 | `wire-sizing-solar.md` |
| 6 | **Arc-fault protection?** | AFCI required for DC circuits >=80V; exception for metal raceways/MC cable not on buildings | CEC 690.11 | `pv-systems-690.md` |
| 7 | **Rapid shutdown compliant?** | Outside array boundary: <=30V within 30 sec; inside array boundary: PVHCS listed per UL 3741 or <=80V within 30 sec; initiation device at readily accessible outdoor location | CEC 690.12 | `pv-systems-690.md` |
| 8 | **Fire setbacks met?** | Ridge setback (18" or 36" depending on array coverage); 36" pathways; hip/valley clearances; emergency escape openings clear | CFC 1205.2, CRC R329.6 | `fire-setbacks-cfc.md` |
| 9 | **DC conductor routing correct?** | DC circuits inside buildings in metal raceways or MC cable; labeled every 10 ft; rooftop conduit minimizes trip hazards | CEC 690.31(D), CFC 1205.2.4 | `pv-systems-690.md` |
| 10 | **Interconnection method valid?** | Load-side: 120% busbar rule (705.12(B)(2)); supply-side: utility-approved adapter or listed service equipment | CEC 705.12, 705.11 | `interconnection-705.md` |
| 11 | **Busbar capacity adequate?** | Combined inverter OCPD + main OCPD <= busbar rating x (100% or 120% depending on position) | CEC 705.12(B) | `interconnection-705.md` |
| 12 | **Grounding and bonding correct?** | Module frames bonded; EGC sized per Table 250.122; connection to building grounding electrode system | CEC 690.43, 690.45, 690.47 | `grounding-bonding-690.md` |
| 13 | **Disconnect means provided?** | PV system disconnect readily accessible, lockable, marked "PV SYSTEM DISCONNECT"; max 6 switches per system | CEC 690.13 | `pv-systems-690.md` |
| 14 | **Labeling complete?** | Rapid shutdown label at service equipment; DC circuit labels (white on red, 3/8" min); power source directory per 705.10; max voltage label at disconnect | CEC 690.12(D), 690.31(D)(2), 690.7(D), 705.10 | `labeling-marking-690.md` |
| 15 | **Structural adequate?** | Roof designed for dead + live loads with PV weight; wind loading per Table R301.2.1; penetrations flashed/sealed | CRC R329.4.1, R329.4.3 | `structural-roof-crc.md` |
| 16 | **Fire classification?** | PV system fire rating matches required roof assembly rating | CRC R329.4.2, R902 | `structural-roof-crc.md` |
| 17 | **ESS requirements met (if applicable)?** | Listed per UL 9540; apply the R330.1 habitable-space exception path and R330.4 sleeping-room restrictions; verify smoke/heat alarms, impact protection, and capacity limits in Table R330.5 | CRC R330, CFC 1207 | `ess-requirements.md` |
| 18 | **Inverter anti-islanding?** | Interactive inverter ceases export on grid outage per 705.40; reconnects only after all phases restored | CEC 705.40 | `interconnection-705.md` |

#### STEP 3: Output the Review Result

For each checklist item, output one of:
- **PASS** -- requirement met, cite code section
- **FAIL** -- requirement not met, cite code section and explain what is wrong
- **FLAG** -- cannot determine from submitted data, explain what additional info is needed
- **N/A** -- does not apply to this installation

---

### Quick-Reference Tables

#### Microinverter Branch Circuit OCPD and Conductor Sizing

Standard combinations for residential microinverter systems. Based on CEC 690.8, 210.19(A)(1). Conductors are copper, 90C wet-rated. Values assume rooftop conditions: max ambient 69C (includes 22C rooftop adder), exposed to direct sunlight, mounted >0.5" above roof, <=6 current-carrying conductors (3 circuits) in raceway.

| Circuit Current (A) | Circuit Power (W) | OCPD (A) | Min. Conductor Size (AWG) | Min. Metal Conduit |
|---------------------|-------------------|----------|--------------------------|-------------------|
| 12 | 2880 | 15 | #12 | 3/4" |
| 16 | 3840 | 20 | #10 | 3/4" |
| 20 | 4800 | 25 | #8 | 1" |
| 24 | 5760 | 30 | #8 | 1" |

*Source: CEC 690.8, Table 310.16 with rooftop temperature correction per Table 690.31(A).*

#### Solar Load Center Feeder Sizing

For systems using a solar load center (combiner panel) between the array and main panel. Based on CEC 690.8, 210.19(A)(1). Conductors copper, 90C wet-rated, ambient 47C (no rooftop adder), <=3 current-carrying conductors in raceway.

| Circuit Current (A) | Circuit Power (W) | OCPD (A) | Min. Bus Bar (A) | Min. Conductor (AWG) | Min. Conduit |
|---------------------|-------------------|----------|-----------------|---------------------|-------------|
| 24 | 5760 | 30 | 30 | #10 | 1/2" |
| 28 | 6720 | 35 | 35 | #8 | 3/4" |
| 32 | 7680 | 40 | 40 | #8 | 3/4" |
| 36 | 8640 | 45 | 45 | #8 | 3/4" |
| 40 | 9600 | 50 | 50 | #8 | 3/4" |
| 41.6 | <=10000 | 60 | 60 | #8 | 3/4" |

*Source: CEC 690.8, Table 310.16 with correction factors for 47C ambient.*

#### Maximum Combined Inverter Output Circuit OCPD (120% Busbar Rule)

For load-side connections where PV OCPD is at opposite end from main breaker (CEC 705.12(B)(2)):

| Bus Bar (A) | Main OCPD (A) | Max Combined Inverter OCPD (120% rule) |
|-------------|---------------|-----------------------------------------|
| 100 | 100 | 20 |
| 125 | 100 | 50 |
| 125 | 125 | 25 |
| 200 | 150 | 90 |
| 200 | 175 | 65 |
| 200 | 200 | 40 |
| 225 | 175 | 95 |
| 225 | 200 | 70 |
| 225 | 225 | 45 |

*Formula: Max PV OCPD = (Bus Bar x 120%) - Main OCPD. Standard plans typically limit system size to <=10kW and OCPD to <=60A, but actual code values are shown above. Source: CEC 705.12(B)(2).*

#### Voltage Correction Factors -- Crystalline/Multicrystalline Silicon Modules

For calculating maximum DC voltage at lowest expected ambient temperature (CEC Table 690.7(A)):

| Ambient Temp (C) | Factor | Ambient Temp (F) |
|-------------------|--------|-------------------|
| 24 to 20 | 1.02 | 76 to 68 |
| 19 to 15 | 1.04 | 67 to 59 |
| 14 to 10 | 1.06 | 58 to 50 |
| 9 to 5 | 1.08 | 49 to 41 |
| 4 to 0 | 1.10 | 40 to 32 |
| -1 to -5 | 1.12 | 31 to 23 |
| -6 to -10 | 1.14 | 22 to 14 |

*Most California coastal/inland locations use 1.12 (-1 to -5C). Mountain areas may require 1.14 or higher.*

#### Fire Setback Requirements -- Residential Rooftop (CFC 1205.2.1 / CRC R329.6)

| Requirement | Dimension | Code Section |
|-------------|-----------|-------------|
| Pathways to ridge (min 2, on separate planes) | 36" (914 mm) wide | CFC 1205.2.1.1 / CRC R329.6.1 |
| Ridge setback (array <=33% of roof area) | 18" (457 mm) both sides | CFC 1205.2.1.2 / CRC R329.6.2 |
| Ridge setback (array >33% of roof area) | 36" (914 mm) both sides | CFC 1205.2.1.2 / CRC R329.6.2 |
| Ridge setback with sprinklers (array <=66%) | 18" (457 mm) both sides | CFC 1205.2.1.3 / CRC R329.6.2.1 |
| Ridge setback with sprinklers (array >66%) | 36" (914 mm) both sides | CFC 1205.2.1.3 / CRC R329.6.2.1 |
| Hip/valley clearance | 18" (457 mm) each side | CFC Appendix BB103.2.2 |
| Smoke ventilation clear area | 3' x 3' (914 mm) each side of ridge | CFC Appendix BB103.4 |
| Emergency escape/rescue opening | No panels below; 36" pathway to opening | CFC 1205.2.2 / CRC R329.6.3 |

*Exceptions: Detached nonhabitable structures (garages, carports); roofs with slope <=2:12; BIPV listed per UL 3741.*

#### Wire Bending Space at Terminals (CEC Table 312.6(A))

Minimum wire-bending space at terminals in panelboards, combiner boxes, and disconnects (1 wire per terminal):

| Wire Size (AWG or kcmil) | Min. Bending Space (in.) |
|--------------------------|--------------------------|
| #14 - #10 | Not specified |
| #8 - #6 | 1-1/2 |
| #4 - #3 | 2 |
| #2 | 2-1/2 |
| #1 | 3 |
| #1/0 - #2/0 | 3-1/2 |
| #3/0 - #4/0 | 4 |
| 250 kcmil | 4-1/2 |
| 300 - 350 kcmil | 5 |
| 400 - 500 kcmil | 6 |

*Measured in a straight line from the end of the lug/connector to the wall, barrier, or obstruction. For 2+ wires per terminal, larger spaces required -- see full table. Source: CEC Table 312.6(A).*

#### Ambient Temperature Correction Factors -- Standard Conductors (CEC Table 310.16)

For conductors in conduit NOT on rooftop (no 22C adder). Apply to Table 310.16 ampacity values:

| Ambient Temp (C) | 60C Conductor Factor | 75C Conductor Factor | 90C Conductor Factor |
|-------------------|---------------------|---------------------|---------------------|
| 21-25 | 1.00 | 1.00 | 1.00 |
| 26-30 | 0.91 | 0.94 | 0.96 |
| 31-35 | 0.82 | 0.88 | 0.91 |
| 36-40 | 0.71 | 0.82 | 0.87 |
| 41-45 | 0.58 | 0.75 | 0.82 |
| 46-50 | 0.41 | 0.67 | 0.76 |
| 51-55 | -- | 0.58 | 0.71 |
| 56-60 | -- | 0.47 | 0.65 |

*Source: CEC Table 310.16 correction factors. For rooftop conduit, add 22C to ambient before looking up factor per Table 690.31(A).*

#### Equipment Grounding Conductor Sizing (CEC Table 250.122)

| OCPD Rating (A) | Min. EGC -- Copper (AWG) | Min. EGC -- Aluminum (AWG) |
|-----------------|--------------------------|---------------------------|
| 15 | #14 | #12 |
| 20 | #12 | #10 |
| 30 | #10 | #8 |
| 40 | #10 | #8 |
| 60 | #10 | #8 |
| 100 | #8 | #6 |
| 200 | #6 | #4 |
| 300 | #4 | #2 |
| 400 | #3 | #1 |

*Source: CEC Table 250.122. EGC for PV sized per 690.45 using assumed OCPD rating per 690.9(B) where no OCPD present.*

---

### Key Principles

1. **PV currents are continuous**: All PV system output currents are treated as continuous. Conductors must be sized at 125% of maximum current before correction/adjustment factors, or at maximum current after correction/adjustment factors, whichever is larger (CEC 690.8(B)).

2. **600V max for residential**: PV system DC circuits on one- and two-family dwellings shall not exceed 600 volts. Calculate maximum voltage using Voc x temperature correction factor for lowest expected ambient temperature (CEC 690.7).

3. **Rapid shutdown is mandatory on buildings**: PV circuits on buildings must include rapid shutdown. Outside array boundary: <=30V within 30 sec. Inside array boundary: PVHCS per UL 3741 or <=80V within 30 sec. Initiation device at readily accessible outdoor location for 1- and 2-family dwellings (CEC 690.12).

4. **120% busbar rule for load-side connections**: Combined PV OCPD + main OCPD cannot exceed 120% of busbar rating when PV breaker is at opposite end from main. If not at opposite end, use 100% (CEC 705.12(B)(2)).

5. **Fire access pathways required**: At least two 36"-wide pathways on separate roof planes from lowest edge to ridge. One must be on street/driveway side. Ridge setbacks of 18" or 36" depending on array coverage percentage (CFC 1205.2.1 / CRC R329.6).

6. **DC circuits inside buildings require metal enclosures**: PV DC circuits >30V or >8A inside buildings must be in metal raceways, MC cable, or metal enclosures. Labeled "PHOTOVOLTAIC POWER SOURCE" in white on red, 3/8" min letters, every 10 ft (CEC 690.31(D)).

7. **Anti-islanding required**: Interactive inverters must automatically cease exporting power when grid goes down and not reconnect until all phases are restored (CEC 705.40).

8. **Qualified persons only**: Installation of PV equipment shall be performed only by qualified persons. California requires contractor licenses C-46 (Solar), C-10 (Electrical), or A/B general (CEC 690.4(C), H&S Code 25916).
