---
name: ev-charger
description: "EV Charger permits in Laguna Beach, CA. An EV charging circuit and its panel or service work at a dwelling or parking area. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions ev charger in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Electrical Code (Title 24, Part 3) — Articles 625, 220, 230, 240, 250, 310, 210, 110"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2025"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — EV Charger Permit

Handles ev charger permits in Laguna Beach end-to-end. Scope: An EV charging circuit and its panel or service work at a dwelling or parking area.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a ev charger permit, or (B) a city reviewer checking a submitted one?"

- Mode A → walk **MODE A — Builder / Homeowner Intake** below
- Mode B → walk **MODE B — City Reviewer** below

Both modes share the same rules. The Laguna Beach rules come first; the California checklist applies wherever Laguna does not override it.

---

## City Info

| | |
|---|---|
| Permit system | Tyler EnerGov Civic Access |
| Permit portal | https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/home |
| Municipal code | https://ecode360.com/LA4953 |
| Fire agency | Laguna Beach Fire |
| Code edition | Title 14 Building & Housing · 2025 CBC/CRC |
| Code prefix | LBMC |

---

## Citywide Overlays

These apply to every permit in Laguna Beach before the rules below.

- **Wildfire — the whole city.** Treat every Laguna Beach parcel as inside a Fire Hazard Severity Zone / WUI area. Say so plainly: "assumed FHSZ based on citywide coverage; confirm the parcel on the City's adopted 2025 LRA map." Never tell an applicant a parcel is outside the zone without that map.
  Exterior work follows the California WUI Code (Title 24 Part 7; CBC Ch. 7A / CRC R337) as amended by LBMC Ch. 14.70, whose scope is set by LBMC §14.70.015. Class A roofing applies to any building in the City (LBMC §14.50.120, amending CBC §1505.1). Details: `../wildfire-wui/SKILL.md`.
- **Coastal zone — most of the city.** Check the parcel against the City's coastal zone map before naming a Planning route. Report a parcel that straddles the boundary as straddling. Coastal Development Permit analysis: `../coastal-development/SKILL.md`.

---

## MODE A — Builder / Homeowner Intake

### A1. Intake

Start by reading `../../references/homeowner-journey.md`; its opening exchange applies when this skill is selected directly. Read any files and answers the user already gave. For an idea-stage request with no files, briefly explain the help available and ask at most three opening questions: the address, the scope, and whether drawings exist.

Then establish, from evidence, the facts the **Laguna Beach Rules** below turn on: the Planning route, the coastal zone, overlays, and any triggers they name. Unknown answers stay unknown. Do not assume a route, an exemption, or compliance. Use the checklists below as the coverage floor for what to ask, without interrogating. When preparing files or navigating intake, read `../../SKILL.md` for the canonical artifact and transaction workflow.

### A2. Pre-submission Compliance Check

Once you have enough information, walk the Laguna Beach rules and then the California checklist using the user's answers. For every item:
- **FAIL** → tell the user the specific change needed before they submit
- **FLAG** → tell them what information or documentation they still need
- **PASS** → confirm and move on

### A3. Submission Guide

When compliance is clean (or flag-only), produce a submission guide. Do not promise over-the-counter issuance unless the Laguna Beach rules below say the scope qualifies.

```
## Ready to Submit — Laguna Beach EV Charger Permit

**Planning route:** [from the Laguna Beach rules, or "none required"]
**Parallel applications:** [Coastal Development Permit, Design Review, or none]

### Required uploads
[Generated per skill — plans, product data sheets, calculations, waste management plan if applicable, Laguna Beach Fire clearance if overlay-triggered, etc.]

### Inspection sequence
[Generated per skill — standard inspection milestones]
```

### A4. Filing

Hand the confirmed facts and filing theory to this plugin's included `laguna-permit-preparer` skill. It fills only verified official forms, uses a visible browser when portal filing is supported, and stops at `portal_ready` with an exact handoff when browser control is unavailable. It never submits without a fresh final approval and a confirmation receipt.

---

## MODE B — City Reviewer

### Procedure

1. Accept the submitted material (form data, PDF, photos, or pasted text)
2. Extract the key facts: project type, scope, materials, dimensions, parcel address, contractor
3. Walk the Laguna Beach rules, then the California checklist, in order
4. Produce output in the format below — hard fails first, then flags, then local flags, then a compliant bundle, then inspection deferrals

### Output format

```
PLAN CHECK — {address} ({permit})

❌ CORRECTIONS REQUIRED (N)
   [plan-check severity=fail items that are not satisfied]

⚠️ VERIFY BEFORE ISSUANCE (N)
   [plan-check severity=flag items needing documentation or clarification]

ℹ️ LOCAL FLAGS (N) — city discretion
   [LBMC-specific items — parcel overlays, city-specific checks]

✓ {N} checks PASS (expand for detail)

➡ {N} checks deferred to inspection

—
Generated by CrossBeam Permits · crossbeam-permits.com
```

Summary verdict at the end: **APPROVE** | **CORRECTIONS REQUIRED** | **NEED ADDITIONAL INFO**

Do not list inspection items as corrections. Do not enumerate every passing item unless the user asks. Respect the plan checker's time.

---

## Laguna Beach Rules

> Laguna Beach's local layer for this permit. It adds to or overrides the California checklist below. Paths are relative to this file.

**Base skill:** `references/california-baseline.md`
**This skill contains ONLY items where Laguna Beach differs from state code.**
**All state checklist items apply unless explicitly overridden below.**

---

### Decision Tree Router

#### STEP 1: What's the Question About?

| Topic | Load These References |
|-------|----------------------|
| **Residential permit review** | `references/city-ev-guide.md` + state skill |
| **Non-residential or multi-family permit review** | `references/city-ev-checklists.md` + state skill |
| **Load calculation verification** | `references/city-ev-guide.md` (load calc worksheet + panel sizing table) |
| **Wire/conduit sizing** | `references/city-ev-guide.md` (wire/conduit table) |
| **Permit process / timeline** | This SKILL.md (below) |
| **Local ordinance** | This SKILL.md + `references/city-ev-ordinance.md` (Ch. 14.85; source text the City source document (not included in this plugin)) |
| **Planning / coastal approval?** | "Planning Route" below |

#### STEP 2: Determine Building Type

| Building Type | Checklist | Key Differences |
|--------------|-----------|-----------------|
| **Single-family / Duplex / ADU** | Residential checklist | No site plan or signed electrical plans required; load calc only for >40A OCPD |
| **Non-residential** | Non-residential checklist | Site plan + electrical plans required; CALGreen + ADA accessibility compliance |
| **Multi-family** | Multi-family checklist | Site plan + electrical plans required; CALGreen 10% EV-ready parking requirement |

#### STEP 3: For Residential Permit Review — Walk the Checklist

Use the state skill's checklist but augment with city-specific details from `references/city-ev-guide.md`:

| # | Check | City-Specific Detail | Reference |
|---|-------|---------------------|-----------|
| 1 | Charger amperage valid? | City covers Level 1 through 100A (Level 2 - 19.2kW highest). The 70A is the wire sizing table's upper range; the code compliance checklists cover up to 100A. | `references/city-ev-guide.md` |
| 2 | Wire sizing correct? | **Use city wire/conduit table** (20A=#12 through 70A=#6) | `references/city-ev-guide.md` |
| 3 | Conduit sizing correct? | **City table covers EMT, RNC, FMC sizes per breaker** | `references/city-ev-guide.md` |
| 4 | Load calc arithmetic correct? | **CRITICAL — independently add up every checked line item. Do NOT trust applicant's Total Watts Used.** Compare your sum to theirs. Verify against panel sizing table. | `references/city-ev-guide.md` |
| 5 | Panel has capacity? | Total watts vs. city panel sizing table (24kW→60A, 48kW→100A, etc.) | `references/city-ev-guide.md` |
| 6 | Separate branch circuit? | CEC §210.17 — no other outlets on EV circuit | State skill |
| 7 | Disconnect (>60A or >150V)? | CEC §625.42 — lockable in open position per §110.25 | State + city checklist |
| 8 | Equipment listed (NRTL)? | UL 2202/UL 2200 listing mark required | City checklist |
| 9 | Not in public ROW? | **Outdoor installations: vehicle + ALL EVCS components must NOT be in public ROW** unless approved by Public Works | City checklist |
| 10 | Conduit support spacing? | EMT=10', RNC=3', FMC=4.5', NMC=4.5' | `references/city-ev-guide.md` |
| **11** | **Submittal complete?** | Electrical permit app + manufacturer specs. **Site plan and electrical plans NOT required for SFR/duplex/ADU.** | `references/city-ev-guide.md` |

#### STEP 4: Output the Review Result

Same format as state skill — PASS/FAIL/FLAG/N/A per item with code citations.

> **Reminder**: For checklist item #4 (load calc arithmetic), always show your independent addition of the line items. This is the most common error.

---

### Planning Route

- **Building review is administrative and nondiscretionary** (§14.85.060(a)). A use permit is possible only on a building-official finding of a specific adverse health/safety impact (§14.85.060(d)-(e)); denial is appealable to the Planning Commission under §25.05.070, which Ord. 1732 replaced (appeal within 14 calendar days on the City form).
- **Planning (Ord. 1732): a Zone Clearance sign-off is needed, at the counter.** "A zoning clearance shall be obtained before the City issues a new or modified building permit" (§25.05.045(B)(3)), so every EV charger building permit gets a Planning Zone Clearance first. No list item names EV chargers. A charger in a garage is interior work, Zone Clearance item §25.05.040(B)(2)(d); an exterior wall unit or pedestal is a non-major-remodel alteration, Zone Clearance (B)(2)(a). City practice: the Planning counter takes EV chargers over the counter (`../guide/references/process-timeline-appeals.md` step 4). Do not tell the applicant no Planning step is needed. Related items that do have a route: a new transformer or utility cabinet under 4 ft is Zone Clearance (B)(2)(w), 4 ft or taller is ADR (B)(3)(a)(xiv); a new or widened driveway at the street is Design Review (B)(1)(k); any exterior work in an environmentally sensitive area is Design Review (B)(1)(e) absent a peer-reviewed no-impact finding.
- **Commercial or multifamily chargers that change parking:** commercial parking and loading areas are Design Review (B)(1)(l), heard by the Planning Commission (§25.05.040(F)(1)(ii)). Check Ch. 25.52 for lost required spaces.
- **City projects (chargers in a City lot or at a City building):** not (B)(1)(l). They follow the City capital-project track: the Director classifies the project de minimis, minor or major ((B)(2)(bb), (B)(3)(a)(xvii), (B)(1)(p)), and a hearing goes to the Planning Commission. A parking lot is public works, so the coastal improvement exemption does not apply: expect a CDP, appealable when the project is a major public works project by cost (§25.07.006). Ask which lot: some City lots sit in areas the Coastal Commission has not certified (`../guide/references/coastal-development-permits.md`).
- **Coastal:** on a single-family lot, a charger is normally an exempt improvement (§25.07.008(A)(1)); utility connections are exempt under §25.07.008(A)(4).

---

### Quick-Reference: Laguna Beach vs. State Code

| Standard | State Code (CEC) | Laguna Beach | Delta |
|----------|------------------|-------------|-------|
| **Wire/conduit sizing** | Table 310.16 (general) | City table with specific conduit combos | **City provides simplified lookup** |
| **Panel sizing table** | Per calculation | City lookup table (24kW→60A, etc.) | **City provides simplified lookup** |
| **Site plan (SFR)** | N/A | **NOT required** for SFR/duplex/ADU | **City simplification** |
| **Electrical plans (SFR)** | N/A | **NOT required** for SFR/duplex/ADU | **City simplification** |
| **Load calc trigger** | All installations | Only for >40A OCPD | **City has higher threshold** |
| **Permit timeline** | N/A | **3 business days** (expedited) / 10 days (standard) — per administrative checklists, not ordinance | **City-specific** |
| **Signing requirement** | N/A | CA Licensed Electrical Engineer or C-10 contractor | **City-specific** |
| **HOA override** | Civil Code § 4080 | Same — HOA cannot block EVCS permit | Matches state |
| **Public ROW** | N/A | Vehicle + components must NOT be in ROW | **City adds** |

---

### Key Laguna Beach EV Charger Facts

- **Municipal code**: Chapter 14.85 — Electric Vehicle Charging Station Permits
- **Permit type**: Streamlined (ministerial, no discretionary review)
- **Expedited review timeline**: Up to **3 business days** if all checklist items pass (per city administrative checklists)
- **Standard review timeline**: Up to **10 business days** (per city administrative checklists)
- **Ordinance timeline language**: Ch. 14.85 states applications are "promptly processed" with no specific day count. The 3-business-day (expedited) and 10-business-day (standard) timelines come from the city's administrative code compliance checklists, not the ordinance itself.
- **CUP trigger**: Building official may require conditional use permit if EVCS could have specific adverse impact on public health/safety (§14.85.060(d))
- **Checklists available**: Residential, Non-Residential, Multi-Family (3 separate checklists)
- **Residential submittal**: Electrical permit app + manufacturer specs only (no site plan, no electrical plans for SFR/duplex/ADU)
- **Non-res/multi-family submittal**: Site plan + electrical plans + single-line diagram + load calc + manufacturer specs
- **Contractor**: Licensed Electrical Engineer or C-10 electrical contractor
- **HOA protection**: EVCS permit approval is NOT subject to HOA approval (Civil Code § 4080)

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Charger amperage valid?** | ❌ **fail** | Standard breaker size, individual branch circuit, continuous duty (125% rule) | CEC 625.40, 625.41, 625.42, 240.6(A) |
| 2 | **Wire sizing correct?** | ❌ **fail** | Conductor matches amperage per Table 310.16 (75°C column for THHN) | CEC Table 310.16 |
| 3 | **Equipment grounding conductor (EGC) correct?** | ❌ **fail** | EGC sized per Table 250.122 based on breaker rating (21-60A = #10 Cu, 61-100A = #8 Cu) | CEC Table 250.122 |
| 4 | **Conduit sizing correct?** | ❌ **fail** | Conduit type and size appropriate for number/size of conductors + EGC | CEC Chapter 9 Tables |
| 5 | **Load calc arithmetic correct?** | ❌ **fail** | **CRITICAL: Do NOT trust the applicant's stated Total General Load.** Independently extract every checked line item and its wattage, sum them yourself, and compare to the stated total. Flag any discrepancy. Then verify the service load formula (first 10,000W at 100% + remainder at 40% for city worksheets, or first 8,000 VA for CEC default). See detailed sub-steps below. | CEC 220.83(A), 230.42 |
| 6 | **Service panel has capacity?** | ❌ **fail** | Total service load (from verified calc) vs. existing panel size per sizing table | CEC 220.83(A), 230.42 |
| 7 | **Equipment location compliant?** | ❌ **fail** | Coupling means height: indoor min 18" above floor, outdoor min 24" above grade (CEC 625.50). Maximum coupling height 48" above floor/grade per accessibility requirements (ADA / CBC Chapter 11B). | CEC 625.50, CBC 11B |
| 8 | **Working space adequate?** | ⚠️ **flag** | Min. 30" wide x 36" deep x 6'6" high clear space around EVSE and panel; no storage in working space | CEC 110.26 |
| 9 | **GFCI protection?** | ❌ **fail** | Required for garage and outdoor receptacles; all EV receptacles per 625.54 | CEC 210.8(A), 625.54 |
| 10 | **Disconnect means (if >60A)?** | ❌ **fail** | Lockable disconnect in readily accessible location | CEC 625.43 |
| 11 | **Ventilation?** | ⚠️ **flag** | Indoor: vehicle batteries must be listed for indoor charging without ventilation, OR mechanical ventilation required | CEC 625.52 |
| 12 | **Equipment listed?** | ❌ **fail** | All EVSE must be listed by NRTL (UL, etc.) | CEC 625.6 |
| 13 | **Weatherproof enclosure (if outdoor)?** | ❌ **fail** | Wet-location receptacles need weatherproof enclosure with extra-duty hood | CEC 625.56 |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 14 | **Installed per manufacturer instructions?** | All EVSE installed per manufacturer's installation instructions. Equipment labeling durable, weather-resistant, and visible. | CEC 110.3(B) |
| 15 | **Conductor protection adequate?** | Conductors protected against physical damage (CEC 300.4). NM cable secured within 12 in. of box and every 4-1/2 ft (CEC 334.30). EMT secured within 10 ft of box and every 10 ft (CEC 358.30). Nail plates where conductors within 1-1/4 in. of framing face. | CEC 300.4, 334.30, 358.30 |
| 16 | **Grounding and bonding complete?** | EGC sized per Table 250.122; grounding connections per 250.8 (listed methods only); bonding per 250.4 (effective ground-fault current path); ground connection methods per 250.130. | CEC 250.4, 250.8, 250.122, 250.130 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/ev-systems-625.md` — CEC Article 625 — Electric Vehicle Power Transfer System
- `references/gfci-location.md` — GFCI Protection and Equipment Location for EV Chargers
- `references/load-calc-220.md` — CEC 220.83 — Optional Calculation for Existing Dwelling Units
- `references/wire-sizing-310.md` — CEC Table 310.16 — Conductor Ampacity for EV Charger Installations

**Laguna Beach rules**

- `references/city-ev-checklists.md` — Laguna Beach EV Charger — Code Compliance Checklists (Non-Residential & Multi-Family)
- `references/city-ev-guide.md` — Laguna Beach EV Charger — Installation Guidelines & Load Calculation
- `references/city-ev-ordinance.md` — Laguna Beach EV Charger — Municipal Code Ch. 14.85

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
