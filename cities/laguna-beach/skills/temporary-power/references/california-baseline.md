# California Baseline — Temporary Power

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Temporary Power — State Regulatory Decision Engine

This skill contains California state-level temporary power installation rules extracted from the 2025 California Electrical Code (CEC), Title 24 Part 3, and the California Fire Code (CFC), Title 24 Part 9. It covers both temporary power poles (utility-fed) and temporary generators used during construction, events, or emergencies.

**What this covers**: State electrical and fire code -- the requirements that apply everywhere in California. Every city must enforce at least these standards.

**What this does NOT cover**: City-specific ordinances, local utility requirements (e.g., specific SCE or PG&E forms), local fee schedules, SCAQMD permit application details, or project-specific engineering. Use the city-level temporary power skill (e.g., `costa-mesa-temporary-power`) for those.

### How to Use This Skill

When reviewing a temporary power permit or answering a temporary power code question, follow the decision tree below. Each step tells you which reference files to load. Load only what you need -- most reviews require 2-4 reference files, not all of them.

After loading references, check the **Quick-Reference Tables** below for the key numbers that come up in almost every temporary power review.

---

### Decision Tree Router

#### STEP 1: What Type of Installation Is This?

| Installation Type | Load These References |
|------------------|----------------------|
| **Temporary generator** (construction or event) | `temporary-installations-590.md`, `generator-requirements.md`, `grounding-bonding-250.md` |
| **Temporary power pole** (utility-fed) | `temporary-installations-590.md`, `temporary-power-pole.md`, `grounding-bonding-250.md` |
| **Either type — full permit review** | All of the above + `panelboard-overcurrent-240-408.md`, `conductors-wiring-methods.md`, `fire-code-temporary-power.md` |

#### STEP 2: What Aspect Is Being Reviewed?

| Review Focus | Load These References |
|-------------|----------------------|
| **Grounding / bonding question** | `grounding-bonding-250.md` |
| **GFCI / receptacle question** | `temporary-installations-590.md` |
| **Conductor sizing / wiring method question** | `conductors-wiring-methods.md` |
| **Panelboard / breaker / enclosure question** | `panelboard-overcurrent-240-408.md` |
| **Fire permit / fueled equipment / required emergency power / project-specific fuel or access** | `fire-code-temporary-power.md`, `generator-requirements.md` |
| **Load calculation / generator sizing** | `generator-requirements.md`, `conductors-wiring-methods.md` |
| **Transfer switch question** | `generator-requirements.md` |
| **General temporary power code question** | `temporary-installations-590.md` |

#### STEP 3: Walk the Review Checklist

For a full permit review, check each item in order. The checklist tells you which reference file has the answer and what code section applies.

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 1 | **Purpose and duration valid?** | Installation remains within the CEC 590.3 purpose/duration that applies: construction work, 90-day decorative/event use, emergency/test use, or an allowed experiment/development use. Any local permit condition is separately sourced. | CEC 590.3 | `temporary-installations-590.md` |
| 2 | **Equipment listed?** | Generator and all distribution equipment listed by NRTL (UL, etc.); installed per manufacturer instructions | CEC 110.3(B) | `generator-requirements.md` |
| 3 | **Load calculations provided?** | Article 220 load calc; continuous load adjustments (125%); largest motor load; generator kW sufficient for load | CEC 220, 590.4(B) | `generator-requirements.md` |
| 4 | **Single line diagram complete?** | Shows transfer of loads; feeder/wiring methods; equipment ratings (V, A, AIC); grounding details; breakers/fuses; panelboard; disconnects | CEC 590.4 | `generator-requirements.md` |
| 5 | **Conductor sizing correct?** | Conductors sized per Table 310.16 (75 deg C column for THHN in conduit); ambient temperature correction applied for above-ground runs | CEC Table 310.16, 310.15, 400.5 | `conductors-wiring-methods.md` |
| 6 | **Wiring methods compliant?** | Cables rated for hard usage or extra-hard usage per Table 400.4; not on floor/ground; supported and protected from damage | CEC 590.4(B), (C), (H), (J), Table 400.4 | `conductors-wiring-methods.md` |
| 7 | **Overcurrent protection correct?** | Breakers sized for load; listed for panel; back-fed breakers secured; service OCPDs current-limiting if >10kA AIC | CEC 240.4, 408.36(D), 590.8 | `panelboard-overcurrent-240-408.md` |
| 8 | **GFCI protection provided?** | All 125V, 1-phase, 15/20/30A receptacles have GFCI; generator receptacles on 15 kW or less generators have GFCI; all temporary receptacles GFCI-protected | CEC 590.6 | `temporary-installations-590.md` |
| 9 | **Grounding electrode system?** | For power poles: full GES per 250.50; for portable generators on trailer with tires: ground rod NOT required per 250.34; for separately derived systems: GES per 250.30 | CEC 250.34, 250.50 | `grounding-bonding-250.md` |
| 10 | **GEC and EGC sizing correct?** | GEC per Table 250.66; EGC per Table 250.122; bonding jumpers per Table 250.102(C)(1) | CEC 250.66, 250.122 | `grounding-bonding-250.md` |
| 11 | **Neutral/EGC separation correct?** | Service panels: bonded; subpanels: neutrals NOT bonded; EGCs and neutrals on separate terminals; back-fed panels: "neutrals isolated from grounding connections" | CEC 250.24, 408.41 | `grounding-bonding-250.md` |
| 12 | **Transfer switch compliant?** | Listed by UL; voltage, amperage, poles specified; automatic or manual noted; unused loads disconnected; back-fed breakers have hold-down kits | Generator-specific | `generator-requirements.md` |
| 13 | **AIC rating adequate?** | Available fault current from utility and generator shown; all equipment rated for available fault current | CEC 590.8(B) | `generator-requirements.md` |
| 14 | **Temporary fire permit and fueled-equipment scope?** | If CFC 105 requires a permit, apply CFC 107. Portable fueled equipment is not stored, operated or repaired inside a building unless a stated CFC 313.1 exception applies. | CFC 107, 313.1 | `fire-code-temporary-power.md` |
| 15 | **Fuel/fire review sourced?** | Fuel type, capacity and location are identified and the applicable current CFC/local provisions are cited; no invented 313 tank/setback/containment table is used. | Project-specific CFC/local source | `fire-code-temporary-power.md` |
| 16 | **Physical protection provided where required?** | Temporary conductors are protected from damage; any vehicle-impact barrier is tied to an applicable project-specific provision and design. | CEC 590.4(H); applicable CFC/design source | `fire-code-temporary-power.md` |
| 17 | **Required identification complete?** | CEC-required directories/identification are complete; any generator/fuel/emergency sign has an applicable current source. | CEC 408.4; source-specific | `fire-code-temporary-power.md` |
| 18 | **Local screening/fencing source?** | Apply screening or fencing only from a current named jurisdiction/utility/permit source with exact locator and scope. | Local/utility source | `fire-code-temporary-power.md` |
| 19 | **Exhaust/ventilation path?** | CFC 313.1 indoor fueled-equipment prohibition/exceptions are resolved; any allowed indoor or required-system installation follows its approved design, listing and applicable CFC 1203/NFPA route. | CFC 313.1, 1203; approved design/listing | `fire-code-temporary-power.md` |
| 20 | **Air quality approval?** | SCAQMD approval required (Southern CA); generators >50 BHP or gas turbines >2,975,000 BTU/hr need Permit to Construct | SCAQMD Rules | `generator-requirements.md` |
| 21 | **Utility notification?** | Serving utility (SCE, PG&E, etc.) notified and approved prior to installation | Utility requirements | `generator-requirements.md` |
| 22 | **Site plan complete?** | Property lines, buildings, distances, north arrow, streets, driveways, generator/pole location, conduit routing (above/below grade), fire access, screening | Plan review | `temporary-power-pole.md` |
| 23 | **Panelboard requirements met?** | Vertical installation; dead-front cover; circuit directory; proper torque; wire bending space per Table 312.6(A); fill limits (40% splices, 75% total); cables secured to cabinet (312.5(C)); not face-up (408.43 Ex.2) | CEC 240.33, 408.4, 408.38, 312.5(C), 312.6, 312.7, 312.8, 408.43 | `panelboard-overcurrent-240-408.md` |
| 24 | **Panel location restrictions met?** | Not exposed to physical damage (240.24(C)); not near ignitable materials (240.24(D)); not in bathrooms (240.24(E)); not over stairway steps (240.24(F)). Breaker ON/OFF position correct (up = ON for vertical, 240.81). | CEC 240.24(C-F), 240.81 | `panelboard-overcurrent-240-408.md` |
| 25 | **Wire bending space adequate?** | Wire bending space at terminals per Table 312.6(A): #14-10 = not specified; #8-6 = 1-1/2 in.; #4-3 = 2 in.; #2 = 2-1/2 in.; #1 = 3 in.; #1/0-2/0 = 3-1/2 in.; #3/0-4/0 = 4 in. (1 wire per terminal). | CEC Table 312.6(A) | `panelboard-overcurrent-240-408.md` |
| 26 | **One wire per terminal?** | No double-tapped breakers unless terminal is listed for two conductors (110.14(A)). Neutrals and EGCs on separate terminals (408.41). | CEC 110.14(A), 408.41 | `panelboard-overcurrent-240-408.md` |
| 27 | **Neutral identification and continuity?** | White or gray factory finish for #6 and smaller; white/gray tape for #4 and larger (200.6). No OCPD in series with neutral (240.22). Neutral pigtailed in MWBCs -- continuity must not depend on connected device (300.13(B)). | CEC 200.6, 240.22, 300.13(B) | `conductors-wiring-methods.md` |
| 28 | **MWBC requirements met?** | MWBCs on opposite legs (208/240V between hots); simultaneous disconnect via 2-pole breaker or handle ties (210.4(B), 240.15(B)(1)). | CEC 210.4(A), 210.4(B), 240.15(B)(1) | `panelboard-overcurrent-240-408.md` |
| 29 | **Subpanel bonding correct?** | Feeder-supplied panels: neutrals NOT bonded to ground; bonding jumper removed; feeder origin label required (408.4(B)). | CEC 250.24(A)(5), 408.4(B) | `grounding-bonding-250.md` |
| 30 | **Fire/electrical code routes complete?** | CEC Article 590 governs temporary wiring; CFC 603 routes CFC/CBC-required electrical equipment to the CEC; CFC 107/313.1/1203 apply only in their stated scopes. CFC 605 is not a temporary-power section. | CEC 590; CFC 107, 313.1, 603, 1203 | `fire-code-temporary-power.md` |

#### STEP 4: Output the Review Result

For each checklist item, output one of:
- **PASS** -- requirement met, cite code section
- **FAIL** -- requirement not met, cite code section and explain what is wrong
- **FLAG** -- cannot determine from submitted data, explain what additional info is needed
- **N/A** -- does not apply to this installation type

---

### Quick-Reference Tables

#### Wire Bending Space at Terminals (CEC Table 312.6(A))

Minimum wire-bending space at terminals in panelboards and disconnects (1 wire per terminal):

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

*Measured in a straight line from the end of the lug/connector to the wall, barrier, or obstruction. Source: CEC Table 312.6(A).*

#### Generator Grounding Decision

| Scenario | Ground Rod Required? | Code Section |
|----------|---------------------|-------------|
| Portable generator on wheels/trailer, supplies only cord-and-plug equipment through its own receptacles, frame bonded | **No** | CEC 250.34(A) |
| Vehicle/trailer-mounted generator, frame bonded to vehicle frame, supplies only equipment on vehicle/trailer and/or cord-and-plug | **No** | CEC 250.34(B) |
| Generator as separately derived system (neutral not interconnected with utility) | **Yes** — full GES per 250.30 | CEC 250.30 |
| Generator feeding building service panel through transfer switch | **Yes** — existing building GES applies | CEC 250.50 |

#### Fuel Tank Setback Requirements

| Tank Capacity (Gallons) | Setback to Property Line | Setback to Adjacent Building |
|------------------------|-------------------------|------------------------------|
| 0-275 | 10 feet | 5 feet |
| 276-750 | 20 feet | 5 feet |
| 751-1000 | 30 feet | 5 feet |

#### GFCI Requirements for Temporary Power (CEC 590.6)

| Receptacle Type | GFCI Required? | Code Section |
|----------------|---------------|-------------|
| 125V, 1-phase, 15/20/30A — NOT part of permanent wiring | **Yes** | 590.6(A)(1) |
| 125V, 1-phase, 15/20/30A — part of permanent wiring used for temp power | **Yes** | 590.6(A)(2) |
| 125V and 125/250V, 15/20/30A on portable generator 15 kW or less | **Yes** | 590.6(A)(3) |
| Other receptacles (>30A, 3-phase, etc.) | GFCI or assured EGC program | 590.6(B) |

#### Equipment Grounding Conductor Sizing (CEC Table 250.122)

| Overcurrent Device Rating (A) | Min. EGC Copper (AWG) | Min. EGC Aluminum (AWG) |
|-------------------------------|----------------------|------------------------|
| 15 | 14 | 12 |
| 20 | 12 | 10 |
| 60 | 10 | 8 |
| 100 | 8 | 6 |
| 200 | 6 | 4 |
| 300 | 4 | 2 |
| 400 | 3 | 1 |

#### GEC Maximum Size by Electrode Type (CEC 250.66)

| Electrode Type | Maximum GEC Size |
|---------------|-----------------|
| Rod, pipe, or plate electrode only | #6 Cu / #4 Al |
| Concrete-encased electrode (Ufer) | #4 Cu |
| Ground ring | #2 Cu |

#### Time Limits

| Installation Purpose | Maximum Duration | Code Section |
|---------------------|-----------------|-------------|
| Construction, remodeling, maintenance, demolition | Duration of construction | CEC 590.3(A) |
| Holiday lighting, similar purposes | 90 days | CEC 590.3(B) |
| CFC temporary permit, where required | Time-limited; no more than 180 days, with extension for demonstrated cause | CFC 107.1 |
| Emergencies and tests | As approved by AHJ | CEC 590.3(C) |

---

### Key Principles

1. **Permanent wiring rules still apply**: Article 590 provides specific relaxations, but all other CEC requirements for permanent wiring apply to temporary installations (CEC 590.2(A)).

2. **GFCI is mandatory for construction sites**: All 125V, single-phase, 15/20/30A receptacles on temporary power must have GFCI protection — whether on a power pole, generator, or existing permanent wiring used for construction (CEC 590.6).

3. **Portable generators on wheels may not need a ground rod**: Per CEC 250.34, a portable generator that only supplies cord-and-plug-connected equipment through its own receptacles, with the frame properly bonded, does not require a grounding electrode. This is one of the most common questions on temporary generator permits.

4. **Fire-code scope is conditional**: CFC 313.1 prohibits portable fueled
   equipment inside a building except under its stated exceptions; it does not
   create a universal 20-foot generator setback or two-hour room. Other fuel,
   access, impact, extinguisher and location requirements must be selected from
   the applicable project-specific source.

5. **Air quality permits may be required**: In the South Coast AQMD, generators with ICEs >50 BHP or gas turbines >2,975,000 BTU/hr need a separate Permit to Construct. Even smaller generators must verify compliance with SCAQMD rules.

6. **Utility requirements are source-specific**: Apply notification, service and
   pole details from the serving utility's current identified standard.

7. **Duration follows purpose and permit**: CEC 590.3 supplies purpose-specific
   durations; a CFC 107 permit, where required, cannot exceed 180 days absent an
   extension for demonstrated cause. Do not invent a statewide 90-day generator
   permit.

8. **Branch circuits and feeders shall NOT be on the floor or ground**: This is a common violation on construction sites (CEC 590.4(J)).

9. **Transfer switches must be listed**: Where a generator feeds a building panel through a transfer switch, the switch must be listed by UL, and notes must indicate unused loads disconnected and neutrals isolated in fed panelboards.

10. **Temporary does not mean sloppy**: All conductor terminations must be torqued per manufacturer specs (CEC 110.14(D)), panels need dead-front covers (CEC 408.38), circuit directories must be complete (CEC 408.4(A)), and knockouts must be filled (CEC 110.12(A)).
