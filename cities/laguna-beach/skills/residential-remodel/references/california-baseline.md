# California Baseline — Residential Remodel

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Residential Remodel Permit Review

This skill is the **parent dispatcher** for state-level review of any residential alteration, remodel, or addition in California. Its value-add is the trip-wire and phantom-remodel detection logic — the underlying component reviews (kitchen, bath, addition, coastal CDP) live in dedicated sub-skills that this skill routes to.

**What this covers:**
- Scope classification per CEBC Chapter 6 (Level 1 / 2 / 3 alterations, additions, change of occupancy, repairs, historic, relocated)
- State Trip Wire 1 — Coastal "replacement structure" detection per 14 CCR §13252(b) + CCC enforcement formula
- State Trip Wire 2 — CEBC §604 Level 3 alteration (work area >50% of building area)
- State Trip Wire 3 — CEBC §202 + §906.2 Substantial Structural Alteration (gravity elements >30% of floor + roof, rolling 5 yrs)
- 5-signal phantom-remodel detector with 2-of-5 / 3-of-5 decision rule
- CEBC Chapter 11 additions framework (5% gravity-load trigger; structural-independence test)
- CRC §R309.2 Exception 1 sprinkler-retrofit state exemption (and explicit routing to city overlay for local triggers)
- Title 24 Part 6 §150.2 component-based energy code triggers for alterations and additions
- Sub-skill dispatch (kitchen-bath, addition, coastal, window/door/siding/reroof city skills)
- Cross-reference to `coastal-development` skill for CDP analysis when any trip wire fires in the coastal zone

**What this does NOT cover:**
- Kitchen/bath component-level requirements — see `../../kitchen-bath-remodel/references/california-baseline.md`
- Addition-specific compliance — see `../../residential-addition/references/california-baseline.md`
- CDP process and coastal-zone analysis — see `../../coastal-development/references/california-baseline.md`
- ADU-specific rules — see `../../adu/references/california-baseline.md`
- Window/door/siding/reroof component checks — see city skills (the `city` skills in this plugin, etc.)
- City-specific major-remodel definitions and sprinkler retrofit triggers — see city overlay skill (the `city` skills in this plugin)
- City-specific bluff overlays, view ordinances, design review — see city overlay skill
- Historic building review (CHBC, Part 8 Title 24)

---

### How to Use This Skill

1. Read the cover sheet, get **address, APN, declared valuation, existing building gross floor area, new floor area (if any), coastal-zone status, and project type label.**
2. Walk the **Decision Tree Router** below.
3. Run the **Trip Wire Checklist** (always — all three trip wires regardless of label).
4. Run the **Phantom-Remodel Detection** module (always — 5 signals).
5. Apply the **Sub-skill Dispatch** for any matching scope component.
6. Always invoke the **city overlay skill** (the `city` skills in this plugin or city-specific sub-skill).
7. Assemble output per the **Output Format** spec.
8. See `../SKILL.md` for the full reference file catalog.

---

### Decision Tree Router

#### STEP 1 -- Read Cover Sheet + Existing-Conditions Plan

| Input | Source on Submittal |
|---|---|
| Project address + APN | Cover sheet (T-1 / A-0) |
| Declared valuation | Cover sheet "Valuation" / "Estimated Cost of Construction" |
| Existing building gross floor area | A-1.0 existing-conditions plan; sometimes T-1 project-data table |
| New gross floor area (if addition) | A-1.0 / A-1.1 proposed plan |
| Coastal zone Y/N | CCC GIS lookup by APN |
| Appealable zone Y/N | CCC GIS appealable-area layer |
| Project type label | Cover sheet "Scope of Work" |

#### STEP 2 -- Determine Scope Bucket

| Scope | What It Triggers |
|---|---|
| Interior-only, no kitchen/bath | Parent applies CEBC Ch. 7/8/9 directly per Level test |
| Kitchen and/or bathroom | Dispatch to `../../kitchen-bath-remodel/references/california-baseline.md` |
| Window/door replacement | Dispatch to city skill the `city` skills in this plugin |
| Siding/cladding | Dispatch to city skill the `city` skills in this plugin |
| Reroof | Dispatch to city skill the `city` skills in this plugin + apply Title 24 Pt 6 §150.2(b)1I if >50% replaced |
| Added floor area (any) | Dispatch to `../../residential-addition/references/california-baseline.md` + apply CEBC Ch. 11 + Title 24 Pt 6 §150.2(a) |
| Coastal zone (any) | Always invoke `../../coastal-development/references/california-baseline.md` after trip-wire check |
| ADU | Dispatch to `../../adu/references/california-baseline.md` (CRC §R309.2 Exception 2 applies) |

Full classifier in `scope-classification-decision-tree.md`.

#### STEP 3 -- Apply CEBC Alteration Level

Compute work area / building area per CEBC §202 (verbatim definition in `cebc-classification-of-work.md`):
- **Like-for-like only** → Level 1 (Ch. 7).
- **Add/eliminate door/window OR system reconfig OR added equipment, AND ratio ≤50%** → Level 2 (Ch. 7 + 8).
- **Ratio >50%** → **Level 3 (Ch. 7 + 8 + 9). TRIP WIRE 2 fires.** See `cebc-alteration-levels.md`.

#### STEP 4 -- Trip Wire Checklist (ALWAYS — all three)

| # | Trip Wire | Threshold | Consequence | Reference File |
|---|-----------|-----------|-------------|----------------|
| 1 | **Coastal "replacement structure"** | ≥50% of SFR replaced (CCC formula: ≥50% of exterior wall LF, floor-by-floor, structural elements only; or ≥50% of roof framing, floor framing, foundation) | Loses repair/maintenance exemption; CDP required; in appealable zone, reviewed under current LCP. **Cite both 14 CCR §13252(b) AND the CCC enforcement formula.** | `coastal-replacement-structure.md` |
| 2 | **CEBC Level 3 alteration** | Work area >50% of building area | Comply with CEBC Ch. 7 + 8 + 9 cumulative (sprinkler, structural, energy, ERCES) | `cebc-alteration-levels.md` (Level 3 section) |
| 3 | **CEBC Substantial Structural Alteration** | Gravity load-carrying elements altered within rolling **5-year** period support >30% of total floor + roof area | Lateral load-resisting system upgraded to current CBC §1609 (wind) + CEBC §304.3.2 (seismic). §906.2 Exception 1 applies only to R ≤5 units AND **conventional light-frame** construction (not engineered) | `cebc-substantial-structural-alteration.md` |

**Important — rolling-window discipline:**
- Trip Wire 1 (Coastal): no specified window in regulation; CCC enforcement aggregates "scope of work" across phased permits.
- Trip Wire 3 (SSA): **5-year rolling lookback** — must check prior permits at APN.
- Phantom Signal 5 (below): **18-month rolling lookback.**
- Track each window independently; do not conflate.

#### STEP 5 -- NOT a Trip Wire: Sprinkler Retrofit

⚠️ **The original plan draft listed CRC R313.2 sprinkler retrofit as State Trip Wire 4. There is no state-level SFR sprinkler retrofit trigger in 2025 CA CRC.** California amended out the IRC R313.2 ≥50%-walls-AND-≥50%-roof retrofit. **CRC §R309.2 Exception 1** explicitly exempts existing un-sprinklered SFRs from sprinkler retrofit on additions or alterations. (R313 in 2025 CA CRC is "ceiling height," not sprinklers.)

**Output framing:** *"No state-level sprinkler retrofit triggered (CRC §R309.2 Exception 1). Local jurisdiction may impose a retrofit trigger via city fire-code amendment — see city overlay."*

Always invoke the city overlay (the `city` skills in this plugin or city sprinkler section). Examples:
- **Laguna Beach LBMC Title 15 §1103.5.4** — alteration of ≥50% of building OR ≥50% of exterior OR added story → full sprinkler retrofit.

Full text in `crc-r309-sprinkler-state-exemption.md`.

#### STEP 6 -- Phantom-Remodel Detection (ALWAYS)

Run the 5 signals. Decision rule:
- **0–1 fired:** routine review.
- **2 fired:** manual review path with phantom-remodel checklist.
- **3+ fired:** **presumptive new construction.** Re-run Steps 3, 4 with the *actual* reconstructed scope; cite **11 Lagunita LLC v. CCC (2020)** in the corrections-letter body if coastal.

| # | Signal | Threshold | Where to Find |
|---|--------|-----------|---------------|
| 1 | **Valuation ratio** | ≥40% yellow, ≥50% red. Coastal SFR remodels typically $200–400/sf; >$500/sf = phantom signal. | Cover sheet valuation ÷ assessor improvement value |
| 2 | **Demo vs structural mismatch** | "existing" wall hatching ≥50% of footprint on A-sheets, BUT S-sheets show new continuous footings, new shear panels, or new hold-downs at every "existing" stud bay | A-sheets demo plan + S-sheets foundation/framing |
| 3 | **Framing key tells** | Framing schedule ~all "N" (new); plate-height changes at "existing" walls; roof-pitch changes at "existing" walls | S-3/S-4 framing plan + schedule + A-sheet sections |
| 4 | **Window/door schedule = 100% new** | Every fenestration "N" while wall plan claims existing-to-remain | A-7/A-8 schedules |
| 5 | **Phased permit history** | ≥2 permits within rolling 18 months at same APN, cumulative valuation >50% of structure value | City permit-history API |

**Graceful degradation:** any signal whose data is unavailable is logged as "manual review needed" — never silently passed. Full extraction guidance in `phantom-remodel-detection.md`.

#### STEP 7 -- Cross-Reference Coastal Skill

If parcel is in the coastal zone AND any trip wire fires (or scope includes added SF, exterior work, or hardscape that may require CDP), **invoke** `../../coastal-development/references/california-baseline.md`. Do not duplicate that skill's content here — let the dispatcher route to it for CDP analysis, appealable-area determination, categorical-exclusion check, and resource-protection review.

#### STEP 8 -- Apply Sub-skill Dispatch

For each scope component identified in Step 2, invoke the matching sub-skill. The parent skill aggregates the sub-skill outputs into the final corrections-ready review.

#### STEP 9 -- Output Format

For each fired trip wire, fired signal, and dispatched sub-skill, produce:

```
## [Trip Wire / Signal / Sub-skill] -- [Name]
**Result:** FIRED | NOT FIRED | FLAG | DISPATCHED
**Code:** [Section number]
**Finding:** [What was verified or what failed; 1–3 sentences]
**Citation:** [Verbatim quote of the operative threshold]
**Action required:** [What the applicant must do]
```

For the overall review:
- **PASS** -- Review complete, no trip wires, no phantom signals; routine path.
- **MANUAL REVIEW** -- 2 phantom signals OR 1 trip wire fired; planner-side review required.
- **PRESUMPTIVE NEW CONSTRUCTION** -- 3+ phantom signals OR 2+ trip wires; major-remodel determination required, CDP review (if coastal), full code stack applied.

---

### Trip Wire Quick-Reference Tables

#### State Trip Wires (3 independent tests)

| Trip Wire | Authority | Threshold | Lookback | Consequence | Source File |
|-----------|-----------|-----------|----------|-------------|-------------|
| 1. Coastal replacement structure | 14 CCR §13252(b) + CCC enforcement | ≥50% replacement of SFR (per CCC: exterior wall LF, floor-by-floor, structural only; OR roof framing OR floor framing OR foundation) | None in regulation; CCC aggregates across permits | CDP required; in appealable zone, current-LCP review | `coastal-replacement-structure.md` |
| 2. CEBC Level 3 alteration | 2025 CEBC §604 | Work area >50% of building area | Single-permit | Comply with Ch. 7 + 8 + 9 cumulative | `cebc-alteration-levels.md` |
| 3. Substantial Structural Alteration | 2025 CEBC §202 + §906.2 | Gravity elements support >30% of floor + roof area | **Rolling 5 years** | Lateral system upgraded to CBC §1609 + CEBC §304.3.2 | `cebc-substantial-structural-alteration.md` |

#### CEBC Alteration Levels

| Level | Threshold | Required Chapters |
|-------|-----------|-------------------|
| 1 | Like-for-like, same purpose | Ch. 7 |
| 2 | Add/eliminate door/window OR reconfig system OR add equipment; work area ≤50% | Ch. 7 + 8 |
| 3 | Work area >50% of building area | Ch. 7 + 8 + 9 (cumulative) |

#### Sprinkler Retrofit Framing

| Jurisdiction Layer | Trigger | Source |
|--------------------|---------|--------|
| State (CRC §R309.2 Exception 1) | **None** — existing un-sprinklered SFRs exempt from retrofit on additions/alterations | `crc-r309-sprinkler-state-exemption.md` |
| State (CRC §R309.1 Exception) | **None** — existing un-sprinklered townhouses exempt | `crc-r309-sprinkler-state-exemption.md` |
| State (CRC §R309.2 Exception 2) | **None** for ADUs ≤1,200 sf on lot with un-sprinklered primary | `crc-r309-sprinkler-state-exemption.md` |
| City overlay (e.g., Laguna LBMC Title 15 §1103.5.4) | ≥50% alteration OR ≥50% exterior OR added story → full retrofit | City overlay skill |

#### Title 24 Pt 6 §150.2 Energy Triggers (component-based, not %-based)

| Trigger | Subsection | Notes |
|---------|------------|-------|
| Adding fenestration | §150.2(b)1A | ≤16 sf added → exempt from total-area requirements |
| Replacing fenestration | §150.2(b)1B | ≤75 sf with U ≤0.40, SHGC ≤0.35 → exempt |
| New/replacement HVAC system | §150.2(b)1C | Full §150.0 stack |
| New ducts >25 ft | §150.2(b)1D | Insulation + sealing + field-verify |
| HVAC component swap | §150.2(b)1E + 1F | Setback thermostat + airflow + refrigerant charge |
| New/replacement heater | §150.2(b)1G | No electric resistance primary (3 exceptions) |
| Water heater swap | §150.2(b)1H | Limited to gas, heat pump w/ R-10, NEEA Tier 3+, or consumer electric (if existing electric resistance) |
| Reroof >50% | §150.2(b)1I | Cool-roof + roof-deck insulation per Climate Zone (Tables 150.2-E, F) |
| Vented attic alteration | §150.2(b)1J | R-49+ insulation, air-seal ceiling plane (CZ-specific) |
| Altered lighting | §150.2(b)1K | JA8 luminaire efficacy |
| Adding exterior door area | §150.2(b)1N | U-factor per §150.1(c)5 |
| Performance path | §150.2(b)2 | LSC budget alternative |
| Whole building | §150.2(c) | Bring entire building to current Title 24 |

Full trigger list with verbatim text in `energy-code-additions-alterations.md`.

#### Additions (CEBC Ch. 11) — Always Relevant When Scope Adds SF

| Trigger | Section | Threshold | Consequence |
|---------|---------|-----------|-------------|
| Addition itself | §1101.1 | Any added SF | Addition meets new-construction code |
| Nonconformity worsening | §1101.2 | Addition extends/creates nonconformity | Existing systems must be brought into compliance |
| Gravity load on existing element | §1103.1 | >5% load increase on any element | That element replaced/altered to current CBC capacity |
| Lateral structural independence | §1103.2 | Addition not independent of existing | Combined system to current CBC §1609 + CEBC §304.3.1 (10% D/C exception) |
| Flood hazard substantial improvement | §1103.3 | Cost ≥50% of market value | Whole building to CBC §1612 / CRC §R306 |

Full reference: `cebc-additions.md`.

---

### Sub-skill Dispatch Cheat Sheet

| Scope element triggers | Dispatch to |
|------------------------|-------------|
| Kitchen and/or bathroom | `../../kitchen-bath-remodel/references/california-baseline.md` |
| Added gross floor area | `../../residential-addition/references/california-baseline.md` |
| Coastal zone (any trip wire fires, or work in appealable area) | `../../coastal-development/references/california-baseline.md` |
| ADU as part of scope | `../../adu/references/california-baseline.md` |
| Window/door replacement | the `city` skills in this plugin |
| Siding | the `city` skills in this plugin |
| Reroof | the `city` skills in this plugin |
| **Always** | the `city` skills in this plugin city overlay (major-remodel definition, sprinkler retrofit, design review, bluff/view overlays) |

The parent skill **does not duplicate** the content of dispatched sub-skills. It detects, routes, and aggregates.

---

### Key Principles

1. **Classify before applying.** CEBC §601.1 binds: every project must be classified per Chapter 6 before any other code section applies. The applicant's label ("remodel") is not the operational classification — compute work area / building area independently.

2. **Three trip wires fire independently.** Coastal §13252(b), CEBC §604 Level 3, and CEBC §202 SSA are independent tests. A project can fire one, two, or all three simultaneously. Run all three on every submittal.

3. **No state-level sprinkler retrofit trigger for SFRs.** CRC §R309.2 Exception 1 is explicit: existing un-sprinklered SFRs are exempt on additions and alterations. The original draft's "CRC R313.2" citation was wrong — R313 in 2025 CA CRC is ceiling height. Sprinkler retrofit triggers exist only at the city level. Always invoke the city overlay.

4. **Phantom remodels are the highest-stakes false-negative.** 11 Lagunita LLC v. CCC (2020) shows the cost: $1M penalty + cease-and-desist + seawall removal for a Laguna Beach owner who pulled "remodel" permits on what was operationally a teardown. The 5-signal detector exists to catch these on submittal, before the city issues a permit it cannot defend.

5. **Decision rule re-routes, does not auto-reject.** 2-of-5 → manual review. 3-of-5 → presumptive new construction. The detector is a **review prioritization tool**, not a gatekeeper. Frame externally that way to avoid blowback from legitimate-remodel applicants.

6. **Cite verbatim. Distinguish regulation from interpretation.** §13252(b) does not contain the "≥50% exterior wall LF" formula — that is CCC's settled enforcement interpretation, codified into LCPs. Always cite both, and label which is which. Same discipline for any threshold: regulation text first, enforcement gloss second.

7. **Track lookback windows independently.** Coastal: no specified window. SSA: rolling 5 years. Phantom Signal 5: rolling 18 months. (City sprinkler triggers: typically scope-based, no window — but verify.) Conflating windows is a common error.

8. **Energy code is component-based for SFR alterations.** Title 24 Pt 6 §150.2(b) does not have a global %-of-floor-area threshold. Walk the trigger list (§150.2(b)1A–N) component-by-component. The performance path (§150.2(b)2) and whole-building path (§150.2(c)) are always available as alternatives.

9. **Always invoke the city overlay.** State law sets the floor; city overlays add (a) sprinkler retrofit triggers, (b) major-remodel definitions and DRB review thresholds, (c) bluff and view overlays, (d) historic district rules, (e) design-review tiers. The state skill's output is incomplete without the city skill.

10. **Cross-reference, never duplicate.** Kitchen/bath compliance lives in `../../kitchen-bath-remodel/SKILL.md`. Addition rules live in `../../residential-addition/SKILL.md`. CDP analysis lives in `../../coastal-development/SKILL.md`. The parent's job is detection, classification, and routing — not re-implementing the sub-skills.
