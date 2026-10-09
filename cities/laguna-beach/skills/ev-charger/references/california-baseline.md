# California Baseline — EV Charger

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California EV Charger — State Regulatory Decision Engine

This skill contains California state-level EV charger installation rules extracted from the 2025 California Electrical Code (CEC), Title 24 Part 3. It covers residential Level 2 EV charger installations — the most common permit type.

**What this covers**: State electrical code — the requirements that apply everywhere in California. Every city must enforce at least these standards.

**What this does NOT cover**: City-specific ordinances, expedited permitting processes, local fee schedules, or project-specific engineering. Use the city-level EV skill (e.g., `buena-park-ev-charger`) for those.

### How to Use This Skill

When reviewing an EV charger permit or answering an EV charger code question, follow the decision tree below. Each step tells you which reference files to load. Load only what you need — most reviews require 2-3 reference files, not all of them.

After loading references, check the **Quick-Reference Tables** below for the key numbers that come up in almost every EV charger review.

---

### Decision Tree Router

#### STEP 1: What Type of Review Is This?

| Review Type | Load These References |
|-------------|----------------------|
| **Full permit review** (form data in → pass/fail out) | `ev-systems-625.md`, `wire-sizing-310.md`, `load-calc-220.md` |
| **Wire/breaker sizing question only** | `wire-sizing-310.md` |
| **Service panel capacity question** | `load-calc-220.md` |
| **GFCI or location question** | `ev-systems-625.md`, `gfci-location.md` |
| **Working space or clearance question** | `gfci-location.md` |
| **Grounding conductor sizing question** | `wire-sizing-310.md` |
| **General EV code question** | `ev-systems-625.md` |

#### STEP 2: Walk the Review Checklist

For a full permit review, check each item in order. The checklist tells you which reference file has the answer and what code section applies.

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 1 | **Charger amperage valid?** | Standard breaker size, individual branch circuit, continuous duty (125% rule) | CEC 625.40, 625.41, 625.42, 240.6(A) | `ev-systems-625.md` |
| 2 | **Wire sizing correct?** | Conductor matches amperage per Table 310.16 (75°C column for THHN) | CEC Table 310.16 | `wire-sizing-310.md` |
| 3 | **Equipment grounding conductor (EGC) correct?** | EGC sized per Table 250.122 based on breaker rating (21-60A = #10 Cu, 61-100A = #8 Cu) | CEC Table 250.122 | `wire-sizing-310.md` |
| 4 | **Conduit sizing correct?** | Conduit type and size appropriate for number/size of conductors + EGC | CEC Chapter 9 Tables | `wire-sizing-310.md` |
| 5 | **Load calc arithmetic correct?** | **CRITICAL: Do NOT trust the applicant's stated Total General Load.** Independently extract every checked line item and its wattage, sum them yourself, and compare to the stated total. Flag any discrepancy. Then verify the service load formula (first 10,000W at 100% + remainder at 40% for city worksheets, or first 8,000 VA for CEC default). See detailed sub-steps below. | CEC 220.83(A), 230.42 | `load-calc-220.md` |
| 6 | **Service panel has capacity?** | Total service load (from verified calc) vs. existing panel size per sizing table | CEC 220.83(A), 230.42 | `load-calc-220.md` |
| 7 | **Equipment location compliant?** | Coupling means height: indoor min 18" above floor, outdoor min 24" above grade (CEC 625.50). Maximum coupling height 48" above floor/grade per accessibility requirements (ADA / CBC Chapter 11B). | CEC 625.50, CBC 11B | `ev-systems-625.md` |
| 8 | **Working space adequate?** | Min. 30" wide x 36" deep x 6'6" high clear space around EVSE and panel; no storage in working space | CEC 110.26 | `gfci-location.md` |
| 9 | **GFCI protection?** | Required for garage and outdoor receptacles; all EV receptacles per 625.54 | CEC 210.8(A), 625.54 | `gfci-location.md` |
| 10 | **Disconnect means (if >60A)?** | Lockable disconnect in readily accessible location | CEC 625.43 | `ev-systems-625.md` |
| 11 | **Ventilation?** | Indoor: vehicle batteries must be listed for indoor charging without ventilation, OR mechanical ventilation required | CEC 625.52 | `ev-systems-625.md` |
| 12 | **Equipment listed?** | All EVSE must be listed by NRTL (UL, etc.) | CEC 625.6 | `ev-systems-625.md` |
| 13 | **Weatherproof enclosure (if outdoor)?** | Wet-location receptacles need weatherproof enclosure with extra-duty hood | CEC 625.56 | `gfci-location.md` |
| 14 | **Installed per manufacturer instructions?** | All EVSE installed per manufacturer's installation instructions. Equipment labeling durable, weather-resistant, and visible. | CEC 110.3(B) | `ev-systems-625.md` |
| 15 | **Conductor protection adequate?** | Conductors protected against physical damage (CEC 300.4). NM cable secured within 12 in. of box and every 4-1/2 ft (CEC 334.30). EMT secured within 10 ft of box and every 10 ft (CEC 358.30). Nail plates where conductors within 1-1/4 in. of framing face. | CEC 300.4, 334.30, 358.30 | `wire-sizing-310.md` |
| 16 | **Grounding and bonding complete?** | EGC sized per Table 250.122; grounding connections per 250.8 (listed methods only); bonding per 250.4 (effective ground-fault current path); ground connection methods per 250.130. | CEC 250.4, 250.8, 250.122, 250.130 | `wire-sizing-310.md` |

#### Checklist Item #5 — Load Calc Verification (Detailed Sub-Steps)

This is the most common source of errors on EV charger applications. Applicants frequently make arithmetic mistakes when adding up their loads. **You must independently verify the addition, not just the formula.**

**Step 5A — Extract line items**: Read each checked row on the load calc worksheet. Record the description and the "Watts Used" value for every checked item.

**Step 5B — Independent summation**: Add up all the wattage values yourself. Write out the addition so it's auditable:
```
Example: 4,200 + 3,000 + 1,500 + 1,000 + 3,500 + 1,500 + 6,000 + 9,600 = 30,300
```

**Step 5C — Cross-check the stated total**: Compare your independent sum to the applicant's "Total General Load" value. If they don't match, this is a **FAIL** — note the discrepancy, show the correct sum, and identify which line item(s) may have been missed or miscalculated.

**Step 5D — Verify the service load formula**: Only after confirming the Total General Load is correct, verify the demand factor calculation:
```
First 10,000W at 100%  =  10,000  (or 8,000 VA if using CEC default)
Remainder at 40%       =  (Total General Load - 10,000) × 0.40
Total Service Load     =  Sum of above
```

**Step 5E — Panel sizing lookup**: Compare Total Service Load to the panel sizing table. Check against the applicant's stated existing panel size.

> **Why this matters**: If the applicant's addition is wrong but the formula is applied correctly to the wrong number, the service load and panel sizing could be off. Even if the final pass/fail result doesn't change, the form must be accurate before permit issuance.

#### STEP 3: Output the Review Result

For each checklist item, output one of:
- **PASS** — requirement met, cite code section
- **FAIL** — requirement not met, cite code section and explain what's wrong
- **FLAG** — cannot determine from submitted data, explain what additional info is needed
- **N/A** — does not apply to this installation

---

### Quick-Reference Tables

#### EV Charger Wire and Breaker Sizing (Residential Level 2)

These are the standard combinations for residential EV charger installations. The breaker must be rated at 125% of continuous load (CEC 625.41). EGC sized per Table 250.122.

| Charger Amperage | Breaker Size (125%) | Min. Wire Size (THHN/75°C) | Min. EGC (Cu) | Notes |
|-----------------|---------------------|----------------------------|--------------|-------|
| 16A | 20A | #12 AWG | #12 AWG | Smallest Level 2 |
| 24A | 30A | #10 AWG | #10 AWG | Common home charger |
| 32A | 40A | #8 AWG | #10 AWG | Common home charger |
| 40A | 50A | #6 AWG | #10 AWG | Higher-power home |
| 48A | 60A | #6 AWG | #10 AWG | Tesla Wall Connector max |
| 56A | 70A | #4 AWG | #8 AWG | Near max residential |
| 64A | 80A | #4 AWG | #8 AWG | High-power Level 2 |
| 80A | 100A | #2 AWG | #8 AWG | Level 2 - 19.2kW max |

*Wire sizes based on CEC Table 310.16, 75°C column, copper conductors. EGC per Table 250.122.*

> **Note on #8 AWG and 50A circuits:** CEC Table 310.16 rates #8 AWG THHN at 50A (75°C column), which might appear sufficient for a 50A breaker. However, for continuous EV loads (CEC 625.42), conductors must support the full breaker rating with margin for voltage drop and derating. The industry standard for 50A EV circuits is **#6 AWG**. Do not accept #8 AWG on a 50A EV circuit. See `wire-sizing-310.md` for the detailed rationale.

#### Wire Bending Space at Terminals (CEC Table 312.6(A))

Minimum wire-bending space at terminals in panelboards and EVSE disconnects (1 wire per terminal):

| Wire Size (AWG or kcmil) | Min. Bending Space (in.) |
|--------------------------|--------------------------|
| #14 - #10 | Not specified |
| #8 - #6 | 1-1/2 |
| #4 - #3 | 2 |
| #2 | 2-1/2 |
| #1 | 3 |
| #1/0 - #2/0 | 3-1/2 |
| #3/0 - #4/0 | 4 |

*Measured in a straight line from the end of the lug/connector to the wall, barrier, or obstruction. Source: CEC Table 312.6(A).*

#### Standard Breaker Sizes (CEC 240.6(A))

Available standard sizes relevant to EV: 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100A

#### Service Panel Capacity — Quick Lookup

Based on CEC 220.83(A) optional calculation for existing dwellings:

| Total Service Load (Watts) | Minimum Panel Size |
|---------------------------|-------------------|
| Up to 24,000 | 100A |
| 24,001 – 30,000 | 125A |
| 30,001 – 36,000 | 150A |
| 36,001 – 48,000 | 200A |
| 48,001 – 54,000 | 225A |

---

### Key Principles

1. **EV loads are continuous**: All EV charging loads are treated as continuous loads (CEC 625.42). This means overcurrent protection must be rated at 125% of the maximum load.

2. **Individual branch circuit**: Each EVSE outlet >16A or >120V must be on its own dedicated branch circuit with no other outlets (CEC 625.40).

3. **Listed equipment only**: All EVSE must be listed by a nationally recognized testing laboratory (CEC 625.6).

4. **California amendment for new construction**: New construction must also comply with CALGreen Chapter 4/5 EV-ready requirements (CEC 625.1.1).

5. **Energy Management Systems**: Where an EMS per 750.30 manages EV load, the maximum equipment load on service/feeder is the EMS-managed maximum — this can allow multiple EVSEs on a smaller service (CEC 625.42(A)).

6. **Equipment grounding conductor**: Every EV circuit needs an EGC sized per Table 250.122. For breakers 21A-60A, the minimum EGC is #10 AWG copper. For 61A-100A (including 70A and 80A circuits), it is #8 AWG copper.

7. **Working space**: All electrical equipment (panel, EVSE, disconnects) must maintain minimum 30" wide x 36" deep x 6'6" high clear working space per CEC 110.26. No storage allowed in working space.

---

### Advisory Notes

#### Voltage Drop on Long Conduit Runs (>30 ft)

For conduit runs exceeding 30 feet, check voltage drop. While not a hard code requirement on the permit form, excessive voltage drop reduces charging efficiency and can trip GFCI protection.

**Formula:** VD = (2 x L x I x R) / 1000

Where:
- L = one-way conductor length in feet
- I = load current in amps (continuous)
- R = conductor resistance per 1000 ft (copper: #6 = 0.491 ohm, #4 = 0.308 ohm, #8 = 0.778 ohm)

**Flag if voltage drop exceeds 3%** (7.2V on a 240V circuit).

Example: #6 AWG, 48A continuous, 50 ft run:
VD = (2 x 50 x 48 x 0.491) / 1000 = 2.36V → 2.36/240 = 0.98% — OK

Example: #6 AWG, 48A continuous, 100 ft run:
VD = (2 x 100 x 48 x 0.491) / 1000 = 4.71V → 4.71/240 = 1.96% — OK but getting close

If voltage drop exceeds 3%, recommend upsizing conductors (e.g., #4 AWG for long runs). This is an advisory — include in review notes, not as a FAIL.
