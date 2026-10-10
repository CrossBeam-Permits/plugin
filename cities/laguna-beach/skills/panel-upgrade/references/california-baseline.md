# California Baseline — Electrical Panel Upgrade

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Panel Upgrade — State Regulatory Decision Engine

This skill contains California state-level residential electrical panel upgrade rules extracted from the 2025 California Electrical Code (CEC), Title 24 Part 3, and the California Fire Code. It covers the full scope of a residential service panel upgrade — service entrance conductors, grounding electrode system, disconnect means, load calculations, working clearance, panel enclosure installation, internal wiring, neutral/EGC handling, multiwire branch circuits, supply-side bonding, and intersystem bonding.

**What this covers**: State electrical code and California Fire Code — the requirements that apply everywhere in California. Every city must enforce at least these standards.

**What this does NOT cover**: City-specific ordinances, local fee schedules, utility coordination procedures, construction hours, business license requirements, or project-specific engineering. Use the city-level panel upgrade skill (e.g., `costa-mesa-panel-upgrade`) for those.

### How to Use This Skill

When reviewing a panel upgrade permit or answering a panel upgrade code question, follow the decision tree below. Each step tells you which reference files to load. Load only what you need — most reviews require 3-4 reference files, not all of them.

After loading references, check the **Quick-Reference Tables** below for the key numbers that come up in almost every panel upgrade review.

---

### Decision Tree Router

#### STEP 1: What Type of Review Is This?

| Review Type | Load These References |
|-------------|----------------------|
| **Full permit review** (form data in -> pass/fail out) | `service-entrance-230.md`, `grounding-bonding-250.md`, `load-calc-220.md`, `wire-sizing-310.md`, `panel-wiring-312-408.md`, `neutral-egc-200-250.md` |
| **Service sizing question only** | `wire-sizing-310.md`, `load-calc-220.md` |
| **Grounding/bonding question** | `grounding-bonding-250.md`, `bonding-supply-side-250.md` |
| **Working clearance or panel location** | `service-entrance-230.md` |
| **Panel wiring or enclosure question** | `panel-wiring-312-408.md` |
| **Neutral, EGC, or conductor identification** | `neutral-egc-200-250.md` |
| **Multiwire branch circuit question** | `mwbc-210.md` |
| **Bonding question (supply-side, piping, intersystem)** | `bonding-supply-side-250.md` |
| **General panel upgrade code question** | `service-entrance-230.md`, `panel-wiring-312-408.md` |

#### STEP 2: Walk the Review Checklist

For a full permit review, check each item in order. The checklist tells you which reference file has the answer and what code section applies.

##### A. Service and Sizing

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 1 | **Target service size valid?** | Standard residential sizes: 100A, 125A, 150A, 200A, 225A, 320A, 400A. Minimum 100A for single-family. | CEC 230.79(C) | `service-entrance-230.md` |
| 2 | **Service load calculation** | 220.83(A) optional calc for existing dwellings. First 8,000W at 100%, remainder at 40%. Total service load must not exceed new panel rating. | CEC 220.83(A) | `load-calc-220.md` |
| 3 | **Service entrance conductors sized?** | Must match panel amperage per Table 310.16. 100A=#4 Cu, 200A=#2/0 Cu (typical at 75C). | CEC 230.42, Table 310.16 | `wire-sizing-310.md` |
| 4 | **Overcurrent protection** | Main breaker sized to panel rating. Must not exceed conductor ampacity. | CEC 230.90, 240.4 | `wire-sizing-310.md` |

##### B. Disconnect and Location

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 5 | **Disconnect means** | Max 6 throws to disconnect all power (or single main breaker). Emergency disconnect required outdoors for 1- and 2-family dwellings (2025 CEC). | CEC 230.71, 230.85 | `service-entrance-230.md` |
| 6 | **Panel location** | Readily accessible, not in bathrooms or clothes closets. Not over stairway steps. Not face-up. | CEC 240.24, 408.43 | `service-entrance-230.md`, `panel-wiring-312-408.md` |
| 7 | **Panel orientation** | Mounted vertically. Max breaker handle height 6 ft 7 in above floor. | CEC 240.33, 240.24(A) | `panel-wiring-312-408.md` |
| 8 | **Working clearance** | 36" deep, 30" wide, 78" high minimum in front of panel. No storage. | CEC 110.26, CFC 603.4 | `service-entrance-230.md` |

##### C. Grounding Electrode System

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 9 | **Grounding electrode system** | Must bond to water pipe (if metallic), ground rod, Ufer (concrete-encased). All existing electrodes must be bonded. | CEC 250.50, 250.52, 250.53 | `grounding-bonding-250.md` |
| 10 | **Supplemental electrode** | Single ground rod must be supplemented by second electrode unless resistance test shows <=25 ohms. Min 6 ft spacing (16 ft preferred). | CEC 250.53(A)(2), 250.53(A)(3) | `grounding-bonding-250.md` |
| 11 | **Water pipe electrode** | If metallic water pipe exists with 10 ft in earth, must be bonded AND supplemented. Bond around meters/regulators. | CEC 250.52(A)(1), 250.53(D) | `grounding-bonding-250.md` |
| 12 | **Main bonding jumper** | Required at service panel. Sized per Table 250.102(C)(1). Green screw/strap installed. | CEC 250.28 | `grounding-bonding-250.md` |
| 13 | **GEC sizing** | GEC sized per Table 250.66 based on largest service entrance conductor. #2/0 Cu -> #4 Cu GEC. #4/0 Al -> #4 Cu or #2 Al GEC. Ground rod/Ufer electrode: #6 Cu max (250.66(A) exception). | CEC 250.66, Table 250.66 | `grounding-bonding-250.md` |

##### D. Panel Enclosure and Wiring

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 14 | **Enclosure installation** | Flush in combustible walls, max 1/4" setback in noncombustible. Max 1/8" plaster gap. | CEC 312.3, 312.4 | `panel-wiring-312-408.md` |
| 15 | **Knockouts and openings** | All unused knockouts filled. Fill plates in empty breaker slots. | CEC 110.12(A) | `panel-wiring-312-408.md` |
| 16 | **Dead-front cover** | Interior panel cover present preventing access to live bus bars. | CEC 408.38 | `panel-wiring-312-408.md` |
| 17 | **Circuit directory** | All circuits legibly identified with specific purpose. Spare positions labeled. | CEC 408.4(A) | `panel-wiring-312-408.md` |
| 18 | **Breakers listed for panel** | Only breakers listed/classified for the specific panel. Installed per manufacturer instructions. Torqued per specs. | CEC 110.3(B) | `panel-wiring-312-408.md` |
| 19 | **Back-fed breakers secured** | Solar/generator back-fed breakers must be fastened in place. | CEC 408.36(D) | `panel-wiring-312-408.md` |
| 20 | **Breaker position indication** | ON/OFF clearly indicated. Vertical breakers: UP = ON. | CEC 240.81 | `panel-wiring-312-408.md` |
| 21 | **One wire per terminal** | No double-tapped breakers unless terminal is listed for two. EGCs and neutrals on separate terminals. | CEC 408.41, 110.14(A) | `panel-wiring-312-408.md` |
| 22 | **Conductor fill** | Splices/taps max 40% of space. All conductors max 75% of cross-section. No crowding. | CEC 312.7, 312.8 | `panel-wiring-312-408.md` |
| 23 | **Cables secured** | Each cable secured to cabinet with appropriate connector. | CEC 312.5(C) | `panel-wiring-312-408.md` |
| 24 | **Aluminum conductor treatment** | Antioxidant applied on aluminum conductors per manufacturer instructions. | CEC 110.14 | `panel-wiring-312-408.md` |

##### E. Neutral and EGC

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 25 | **Neutral/ground bonding (service)** | Neutral, EGCs, and enclosure bonded in service panel. | CEC 250.24(B) | `neutral-egc-200-250.md` |
| 26 | **Neutral/ground separation (subpanel)** | Neutrals NOT bonded to ground in subpanels. Bonding jumper removed. | CEC 250.24(A)(5) | `neutral-egc-200-250.md` |
| 27 | **Neutral identification** | White or gray factory finish (#6 and smaller). White/gray tape (#4 and larger). | CEC 200.6(A), 200.6(B) | `neutral-egc-200-250.md` |
| 28 | **EGC identification** | Green or green/yellow (#6 and smaller). Green tape (#4 and larger). Green never used for hot or neutral. | CEC 250.119 | `neutral-egc-200-250.md` |
| 29 | **EGC sizing** | Sized per Table 250.122 based on OCPD rating. | CEC 250.122, Table 250.122 | `neutral-egc-200-250.md` |
| 30 | **Grounding terminal bar** | Required if wire-type EGCs are present. Bonded to enclosure. | CEC 408.40 | `neutral-egc-200-250.md` |
| 31 | **One neutral per circuit** | Each neutral serves only one branch circuit or MWBC. | CEC 200.4(A) | `neutral-egc-200-250.md` |

##### F. Multiwire Branch Circuits

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 32 | **MWBC hots on opposite legs** | Two hots must have voltage between them (opposite phases). | CEC 100 (definition) | `mwbc-210.md` |
| 33 | **MWBC simultaneous disconnect** | 2-pole breaker or handle-tied single-pole breakers required. | CEC 210.4(B), 240.15(B)(1) | `mwbc-210.md` |
| 34 | **MWBC neutral pigtailed** | Neutral continuity must not depend on connected device. Pigtail at each device box. | CEC 300.13(B) | `mwbc-210.md` |

##### F2. Arc-Fault Circuit-Interrupter (AFCI) Protection

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 34a | **AFCI protection on required circuits** | For new panels or panel replacements: AFCI protection required on all 15A and 20A, 120V branch circuits supplying outlets/devices in kitchens, family rooms, dining rooms, living rooms, parlors, libraries, dens, bedrooms, sunrooms, recreation rooms, closets, hallways, laundry areas, and similar rooms/areas. NOT required on: bathrooms (dedicated circuit), outdoors, garages, unfinished basements. | CEC 210.12(A), 210.12(B) | `panel-wiring-312-408.md` |
| 34b | **AFCI type** | Must be listed combination-type AFCI breaker (or listed outlet branch-circuit type AFCI at first outlet with appropriate breaker). | CEC 210.12(A) | `panel-wiring-312-408.md` |

##### G. Supply-Side and Intersystem Bonding

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 35 | **Supply-side bonding** | Service raceways bonded with proper means (not standard locknuts). Bonding jumpers around concentric KOs. | CEC 250.92 | `bonding-supply-side-250.md` |
| 36 | **Intersystem bonding termination** | IBT device installed at service equipment. External, accessible, min 3 terminals for communication bonds. | CEC 250.94 | `bonding-supply-side-250.md` |
| 37 | **Water pipe bonding** | Sized per Table 250.102(C)(1). Continuity around meters/regulators. | CEC 250.104, 250.53(D)(1) | `bonding-supply-side-250.md` |
| 38 | **Metal piping bonding** | Gas piping, metal ducts, other piping capable of becoming energized must be bonded. | CEC 250.104(B) | `bonding-supply-side-250.md` |
| 39 | **GEC protection** | #8 GEC in raceway/armor. #6+ on surface OK if not exposed to damage. Steel conduit bonded at both ends. | CEC 250.64(B), 250.64(E) | `bonding-supply-side-250.md` |
| 40 | **GEC connections accessible** | All GEC connections accessible except buried/encased. Listed clamps (DB for buried). | CEC 250.68(A), 250.70 | `bonding-supply-side-250.md` |

##### H. Overhead Line Clearances and Pool Clearances

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 41 | **Overhead conductor clearances** | Service conductors: min 8 ft 6 in. above roof surface (maintained 3 ft from roof edge); 10 ft above sidewalks/pedestrian areas; 12 ft above residential driveways; 18 ft above public streets/alleys/areas subject to truck traffic. Exceptions: 3 ft above roof with slope >=4:12 and voltage <=300V; 18 in. above overhanging portion if <=6 ft of conductor passes over overhang. Point of attachment min 10 ft above finished grade. | CEC 230.24(A), 230.24(B), 230.26 | `service-entrance-230.md` |
| 42 | **Swimming pool electrical clearances** | Overhead conductors: min 22.5 ft (6.9 m) clearance in any direction from water level, edge of water surface, base of diving platform, or permanently anchored raft for insulated cables 0-750V with grounded messenger; min 14.5 ft (4.4 m) to observation stands/towers/diving platforms. See CEC Table 680.9(A) for full clearance values. Service equipment and panelboards shall not be located within 5 ft of inside wall of pool per CEC 680.11. | CEC 680.9, Table 680.9(A), 680.11 | `service-entrance-230.md` |

##### I. Equipment and Fire Code

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 43 | **Equipment listed and labeled** | All equipment listed by NRTL. Installed per manufacturer specs. | CEC 110.3(B) | `panel-wiring-312-408.md` |
| 44 | **Enclosure rated for environment** | Appropriate enclosure for location (NEMA 3R minimum for outdoor). Protected from moisture, dust, physical damage. | CEC 110.27(B), 110.28 | `service-entrance-230.md` |
| 45 | **Equipment and hazard markings** | Equipment identifies the responsible organization; ratings required by other CEC provisions are present; markings withstand the environment. Any CEC-required field hazard marking is effective and permanently affixed under 110.21(B). | CEC 110.21 | `service-entrance-230.md` |
| 46 | **Conditional lockability and dwelling emergency marking** | Where another CEC provision requires a disconnect to be lockable open, the locking provision complies with 110.25. For a one- or two-family dwelling within 230.85, verify the outdoor emergency disconnect and exact 230.85(E) marking for its disconnect type. | CEC 110.25, 230.85(E) | `service-entrance-230.md` |

#### STEP 3: Output the Review Result

For each checklist item, output one of:
- **PASS** — requirement met, cite code section
- **FAIL** — requirement not met, cite code section and explain what's wrong
- **FLAG** — cannot determine from submitted data, explain what additional info is needed
- **N/A** — does not apply to this installation

---

### Quick-Reference Tables

#### Service Entrance Conductor Sizing (Copper, 75C / THHN)

| Service Size | Min. Conductor (Cu) | Min. Conductor (Al) | GEC Size (Cu) | GEC Size (Al) |
|-------------|--------------------|--------------------|---------------|---------------|
| 100A | #4 AWG | #2 AWG | #8 AWG | #6 AWG |
| 125A | #2 AWG | #1/0 AWG | #6 AWG | #4 AWG |
| 150A | #1 AWG | #2/0 AWG | #6 AWG | #4 AWG |
| 200A | #2/0 AWG | #4/0 AWG | #4 AWG | #2 AWG |
| 225A | #3/0 AWG | 250 kcmil | #4 AWG | #2 AWG |
| 320A | 350 kcmil | 500 kcmil | #2 AWG | #1/0 AWG |
| 400A | 500 kcmil | 750 kcmil | #1/0 AWG | #3/0 AWG |

*Conductor sizes from CEC Table 310.16 (75C column). GEC sizes from Table 250.66.*

#### Main Bonding Jumper Sizing (Table 250.102(C)(1))

| Largest Ungrounded Conductor (Cu) | Bonding Jumper (Cu) | Bonding Jumper (Al) |
|----------------------------------|--------------------|--------------------|
| #2 or smaller | #8 | #6 |
| #1 or #1/0 | #6 | #4 |
| #2/0 or #3/0 | #4 | #2 |
| Over #3/0 through 350 kcmil | #2 | #1/0 |
| Over 350 through 600 kcmil | #1/0 | #3/0 |

#### EGC Sizing (Table 250.122)

| OCPD Rating | Min. EGC (Cu) | Min. EGC (Al) |
|-------------|---------------|---------------|
| 15A | #14 | #12 |
| 20A | #12 | #10 |
| 30A | #10 | #8 |
| 60A | #10 | #8 |
| 100A | #8 | #6 |
| 200A | #6 | #4 |
| 300A | #4 | #2 |
| 400A | #3 | #1 |

#### Wire Bending Space at Terminals (CEC Table 312.6(A))

Minimum wire-bending space at terminals in panelboards (1 wire per terminal):

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

*Measured in a straight line from the end of the lug/connector to the wall, barrier, or obstruction. For 2+ wires per terminal, larger spaces required -- see CEC Table 312.6(A). Source: CEC Table 312.6(A).*

#### Standard Breaker Sizes (CEC 240.6(A))

15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, **100**, 110, **125**, **150**, 175, **200**, **225**, 250, 300, **320**, 350, **400**

Bolded sizes are the standard residential service panel sizes.

#### Service Panel Capacity — Quick Lookup

Based on CEC 220.83(A) optional calculation for existing dwellings:

| Total Calculated Service Load (Watts) | Minimum Panel Size |
|---------------------------------------|-------------------|
| Up to 24,000 | 100A |
| 24,001 - 30,000 | 125A |
| 30,001 - 36,000 | 150A |
| 36,001 - 48,000 | 200A |
| 48,001 - 54,000 | 225A |
| Over 54,000 | 320A or 400A |

---

### Key Principles

1. **Minimum 100A for single-family**: CEC 230.79(C) requires a minimum 100A, 3-wire service disconnect for any one-family dwelling.

2. **Emergency disconnect required (2025 CEC)**: For all 1- and 2-family dwellings, an emergency disconnecting means must be installed in a readily accessible outdoor location per CEC 230.85. This is new in the 2025 code cycle.

3. **Grounding electrode system — all that exist**: CEC 250.50 requires that ALL grounding electrodes present at the building (water pipe, ground rod, Ufer, building steel) be bonded together. You cannot pick and choose.

4. **Single ground rod needs a supplement**: A single ground rod must be supplemented by a second electrode unless a certified test report shows 25 ohms or less resistance to earth (CEC 250.53(A)(2)).

5. **Utility coordination**: Changing service size typically requires SCE (or the local utility) to install a new meter base and potentially upgrade the transformer. This is outside the permit scope but should be flagged.

6. **Working clearance is non-negotiable**: 36" x 30" x 78" clear working space in front of the panel, no storage, no obstructions (CEC 110.26).

7. **One wire per terminal**: No double-tapping unless the terminal is listed for multiple conductors. EGCs and neutrals get separate terminals even when on the same bus bar (CEC 408.41).

8. **Service vs. subpanel bonding**: Neutral and ground are bonded at the service panel (250.24(B)) but SEPARATED at all subpanels (250.24(A)(5)). When a panel upgrade converts the old main to a subpanel, the bonding jumper must be removed.

9. **AFCI protection on panel upgrades**: CEC 210.12 requires AFCI protection on 15A and 20A, 120V branch circuits serving most habitable rooms. When a panel is replaced, the AHJ may require AFCI breakers on all affected circuits. Rooms requiring AFCI: kitchens, family rooms, dining rooms, living rooms, parlors, libraries, dens, bedrooms, sunrooms, recreation rooms, closets, hallways, laundry areas, and similar. Rooms NOT requiring AFCI: bathrooms (on dedicated circuits), outdoor circuits, garages, and unfinished basements.
