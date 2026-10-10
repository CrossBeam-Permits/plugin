---
name: multi-unit-residential
description: "Multi-Unit Residential permits in Laguna Beach, CA. Two or more dwelling units, new or substantially altered. Always a plan set. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against the Laguna Beach rules and the City submittal checklists, and prepares a portal-ready submission; (B) CITY REVIEWER — checks a submittal against the Laguna Beach rules and produces tight corrections output. California code compliance comes from the CrossBeam connector when it is connected. Use when the user mentions multi unit residential in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Standards Code (Title 24, Parts 2, 2.5, 3, 4, 5, 6, 9, 11); LBMC Title 14, 15, 25; 2025 CBC/CRC; Gov. Code §65915 et seq.; 6th-cycle Housing Element"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-07-22"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Multi-Unit Residential Permit

Handles multi-unit residential permits in Laguna Beach end-to-end. Scope: Two or more dwelling units, new or substantially altered. Always a plan set.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a multi-unit residential permit, or (B) a city reviewer checking a submitted one?"

- Mode A → walk **MODE A — Builder / Homeowner Intake** below
- Mode B → walk **MODE B — City Reviewer** below

Both modes share the same rules. This skill carries the Laguna Beach layer: the City rules, the City submittal checklists and the filing steps. California code compliance comes from the CrossBeam connector (see **California Code Compliance** below).

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

Then establish, from evidence, the facts the **Laguna Beach Rules** below turn on: the Planning route, the coastal zone, overlays, and any triggers they name. Unknown answers stay unknown. Do not assume a route, an exemption, or compliance. Use the Laguna Beach rules and the City submittal checklists below as the coverage floor for what to ask, without interrogating. When preparing files or navigating intake, read `../../SKILL.md` for the canonical artifact and transaction workflow.

### A2. Pre-submission Compliance Check

Once you have enough information, walk the Laguna Beach rules and the City submittal checklists using the user's answers. When a plan set exists, run the plan-set check (`../plan-set-check/SKILL.md`). For California code compliance, follow **California Code Compliance** below. For every item:
- **FAIL** → tell the user the specific change needed before they submit
- **FLAG** → tell them what information or documentation they still need
- **PASS** → confirm and move on
- **NOT CHECKED** → a California code item with no CrossBeam result: say so, and recommend a CrossBeam check before filing

### A3. Submission Guide

When compliance is clean (or flag-only), produce a submission guide. Do not promise over-the-counter issuance unless the Laguna Beach rules below say the scope qualifies.

```
## Ready to Submit — Laguna Beach Multi-Unit Residential Permit

**Planning route:** [from the Laguna Beach rules, or "none required"]
**Parallel applications:** [Coastal Development Permit, Design Review, or none]
**California code compliance:** [CrossBeam result, or "not checked: run a CrossBeam check before filing"]

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
3. Walk the Laguna Beach rules and the City submittal checklists, in order. Get California code compliance as **California Code Compliance** below says
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

⛔ NOT CHECKED — California code compliance [unless a CrossBeam result covers it]

—
Generated by CrossBeam Permits · crossbeam-permits.com
```

Summary verdict at the end: **APPROVE** | **CORRECTIONS REQUIRED** | **NEED ADDITIONAL INFO**

Without a CrossBeam result, the verdict covers the Laguna Beach rules and the City checklists only. Say so beside it, and never call the set compliant with the California codes.

Do not list inspection items as corrections. Do not enumerate every passing item unless the user asks. Respect the plan checker's time.

---

## Laguna Beach Rules

> Laguna Beach's local layer for this permit. It adds to or overrides California law, which comes from the CrossBeam connector. Paths are relative to this file.

> **Volume context.** Multi-unit residential is RARE in Laguna Beach (<5 ground-up R-3 permits/year expected; city is built-out, predominantly VHFHSZ, almost entirely in the Coastal Zone, 394-unit 6th-cycle RHNA met primarily via rezones of church/hospital surface lots plus one active condo expansion at Pyne Castle, 770 Hillcrest Dr). This skill is **deliberately lean** and optimizes for the paths actually used: (a) ADU additions to existing multi-family under Ch. 25.17(D)(3); (b) condominium conversions under Ch. 25.47/§25.07.008(A)(2)(c); (c) Downtown Specific Plan upper-floor mixed-use; (d) state-preempted streamlined paths. Ground-up R-3 is covered at the basics only.

---

### Critical First Checks — Route Before Reviewing

These determine which path the skill takes. Run them in order; first match wins.

| Check | Route to |
|-------|----------|
| **Is this actually an ADU addition to a multi-family lot?** (Project narrative says "add 1-2 units to existing apartment/condo lot," <=25% of existing unit count, or <=2 detached at 18 ft / 4 ft setbacks.) | **STOP — route to `../adu/SKILL.md` skill**. Ch. 25.17(D)(3) is the controlling chapter, not Ch. 25.14. Multi-unit precheck does not apply. |
| **Is this a condominium conversion of existing apartments?** (No physical new units; tenure change only, or tenure change + interior reconfiguration.) | Load `references/condo-conversion.md`. Ch. 25.47 process + **CDP always required** per §25.07.008(A)(2)(c). |
| **Is this in the Downtown Specific Plan (DSP) boundary with residential over commercial?** | Load `references/dsp-mixed-use.md`. DSP density rules govern, NOT Title 25 R-3. |
| **Is the applicant invoking a state-preempted streamlined path?** (SB 9 / SB 35 / SB 423 / AB 2011 / Density Bonus Law / AB 1287 stacked bonus / Ch. 25.96 inclusionary.) | Load `references/state-preemption.md`. State law overrides Laguna's local restrictions (including the 36 ft height cap) for qualifying projects. |
| **Ground-up new R-3 (3+ units) on an R-3 / R-2 parcel?** | Load `references/zoning-r2-r3-envelope.md` + the full overlay stack (Planning Commission Design Review + CDP + WUI + sprinklers + hillside). |

---

### Citywide Baseline Deltas (Apply Unless Routed Out Above)

| Item | Laguna Beach rule | State baseline | Delta |
|------|-------------------|----------------|-------|
| **Primary multi-family zone** | R-3 Residential High Density (Ch. 25.14); R-2 (Ch. 25.12) two-family | No state zone | City-specific |
| **R-3 density** | **1 dwelling unit / 2,000 sf net lot area** (Ch. 25.14); historic-preservation bonus to 1 du / 1,000 sf available via Ch. 25.96 | No state density limit | City-specific |
| **Height** | **36 ft citywide cap** (LBMC §25.51.010); applies to ALL zones, no by-right exceptions absent state-preempted density bonus relief | None | **City cap** |
| **Front yard (R-3)** | >=20 ft | None | City-specific |
| **Side/rear setbacks, open space** | §25.14.008(C): 20 ft front; side = 10% avg lot width (max 12 ft, min 4 ft); 10 ft rear; open space per §25.50.010 plus 50 sf per attached du/guest house/guest room. See `references/zoning-r2-r3-envelope.md`. | None | City-specific |
| **Planning route** | A new building requires Design Review under current §25.05.040(B)(1)(b); apply §25.05.040(F) for the proper authority. Other scopes must match the current closed lists. DR mailed notice, staking, posting and appeal deadlines are in `../city-reference/SKILL.md` §"Design Review / Zone Clearance". | None | City-specific |
| **Coastal Development Permit (CDP)** | Required for almost every multi-unit project under Ch. 25.07.004. **§25.07.008(A)(2)(c) carves out condominium / stock cooperative conversions from the "improvements to existing structures" CDP exemption — they ALWAYS need a CDP.** Appealable area triggers Coastal Commission jurisdiction. | None | City-specific |
| **VHFHSZ / WUI** | Ch. 14.70 with local amendments: Class A roof (§14.70.020), noncombustible/ignition-resistant exterior (§14.70.030), vinyl windows welded+reinforced (§14.70.035), **no plastic skylights — glass only** (§14.70.040), vent openings <=144 sq in (§14.70.025), defensible space (§14.70.060), fuel modification plans (§14.70.070) | CBC Ch. 7A / CRC R327 ignition-resistant in FHSZ | **More restrictive** |
| **Sprinklers — new R-2/R-3 multi-family (CBC track, 3+ units)** | **NFPA 13R baseline per CBC §903.3.1.2.** Laguna does NOT override 13R to 13D for multi-family. The Ch. 14.52.030 local amendment targets CRC R309.2 — that's the 1- and 2-family stack (and CRC-track townhomes), not 3+ unit R-2/R-3. **Confirm hydraulic design and LBFD review with the Building Official (CBO).** | CBC 903.3.1.2 (13R) | **Conforming (no override)** |
| **Sprinkler retrofit — existing R-2/R-3 multi-family** | Run both applicable city frameworks: **Title 15 §1103.5.4** (scope: alteration >=50%, exterior work >=50%, or added story; fire-resistant-siding-only exception) and **LBMC §14.50.104/CBC §903.6(1),(5)** (Group R valuation >=50% over any three-year period, or a Building Official substantial-renovation finding). | None | **City retrofit triggers** |
| **Multi-family parking ratio** | Ch. 25.52 (§25.52.012 sub-section) | None |  |
| **Tandem parking** | §25.52.008(D) — only allowed for required residential spaces with DRB approval for SFR/two-family; **multi-family tandem not by-right** | None | City-specific |
| **Density Bonus parking override** | Gov. Code §65915(p): 0.5/studio, 1/1BR, 1.5/2-3BR, 2.5/4+BR for qualifying affordable projects — **preempts Laguna's local ratios** | None | State preempt |
| **Coastal Zone parking** | Cannot drop below replacement minimum per Ch. 25.07 coastal access policy | None | City-specific |
| **Hillside / bluff** | Most R-3 parcels are hillside or coastal-bluff. Geotechnical report required; bluff-edge determinations on bluff-top sites; structural calcs must reconcile geotech with CBC Ch. 16 (Risk Cat II, SDC D, Site Class per geotech); SWPPP for pads >50 cy | None | City-specific |
| **Heritage Committee** | Required for buildings >=50 years old. Many R-3 buildings in Laguna are 1950s-70s vintage — automatic trigger. | None | City-specific |
| **Fire agency** | **LBFD (Laguna Beach Fire Department)** — NOT OCFA. Own department. Title 15 fire-flow, hydrant flow, fire access | None | City-specific |
| **Roof class** | Class A on ALL roofs and re-roofs citywide (§14.70.020 — VHFHSZ overlay applies citywide for practical purposes) | CBC Table 1505.1 allows Class B/C in some configurations | **More restrictive** |
| **Construction hours** | Mon-Fri 7:00 AM - 6:00 PM; Sat 8:00 AM - 5:00 PM; Sun + federal holidays PROHIBITED | None | **More restrictive than neighbors** |
| **Permit portal** | Tyler EnerGov CivicAccess — lagunabeachca-energovweb.tylerhost.net/apps/SelfService | None | City-specific |

---

### Decision Tree

#### Step 2 — Run the Five Critical First Checks (top of this file)

The most likely scenarios route OUT of this skill or to a narrow reference. Run those checks first before applying the citywide baseline.

#### Step 3 — Apply Current Design Review Routing

Use `../residential-remodel/references/city-design-review-tiers.md` (shared) for the full DR tier matrix. Multi-unit specifics:

- New 3+ unit construction: **Design Review under §25.05.040(B)(1)(b)** before the Planning Commission under §25.05.040(F), not Administrative Design Review.
- Do not borrow the Design Review Board's meeting schedule for a Planning Commission project; verify the current hearing calendar.
- Noticing: 21 calendar days before hearing (§25.05.065(D)).
- Appeals: 14 calendar days to City Council (§25.05.070(B)(2)).
- Pre-DRB submittal: massing study, story poles where required, materials/color board.
- Findings: both current §25.05.040(I) findings, applying the 11 criteria in §25.05.040(H).
- Fire Department review required **before** design-review action for new construction.

#### Step 4 — Apply CDP Routing

Use `../residential-remodel/references/city-cdp-coastal-zone.md` (shared) for full CDP analysis. Multi-unit-specific deltas:

- **Condominium / stock cooperative conversions are NEVER CDP-exempt** per §25.07.008(A)(2)(c). This is the most-litigated CDP delta in Laguna.
- Appealable-area determination (§25.07.006): between sea and first public road, within 300 ft of beach/mean high tide, within 100 ft of wetland/stream, within 300 ft of coastal bluff top. Triggers Coastal Commission appeal jurisdiction.
- Multi-unit projects on Coast Hwy, Cliff Dr, or bluff-top condos almost always land in appealable area.
- Public access dedications (lateral / vertical / view corridor easements) may be conditioned for appealable parcels.
- De minimis waiver (§25.07.009) and administrative CDP (§25.07.013) paths exist but generally not applicable to ground-up multi-unit.
- Bluff-edge determinations required for bluff-top sites.

#### Step 5 — Apply R-3 / R-2 Zoning Envelope

Load `references/zoning-r2-r3-envelope.md`.

Minimum checks for ground-up R-3:

- Lot area >= density / unit count math (1 du / 2,000 sf net lot area; or 1 du / 1,000 sf with historic-preservation bonus under Ch. 25.96).
- Height <= **36 ft per §25.51.010** (citywide cap; no by-right exceptions absent state-preempted density bonus).
- Front yard >= 20 ft.
- Side/rear setbacks, open space per §25.14.008(C) — verified verbatim 2026-05-12.
- Design Review compliance per Ch. 25.40 (baked into R-3 purpose statement).
- DSP boundary check — if inside DSP, switch to `references/dsp-mixed-use.md` and use DSP density rules, NOT Title 25.

#### Step 6 — Apply Local Fire, Sprinkler, and WUI Amendments

Use `../residential-remodel/references/city-vhfhsz-wui.md` and `../residential-remodel/references/city-sprinkler-retrofit.md` (shared). Multi-unit-specific deltas:

- **New 3+ unit R-2/R-3 sprinkler design: NFPA 13R per CBC §903.3.1.2.** Do NOT use NFPA 13D — that's 1- and 2-family only under Ch. 14.52.030. Laguna does not override 13R for multi-family.
- LBFD review required for sprinklers, fire access, hydrant flow, fire-flow calcs.
- LBFD review required before DRB action for new construction.
- Defensible space + fuel modification plans required for new construction / major remodels in VHFHSZ.
- For existing R-2/R-3 retrofits, run **both** Title 15 §1103.5.4 (scope) and LBMC §14.50.104/CBC §903.6(1),(5) (Group R valuation/substantial-renovation). Do not treat §903.6 as non-residential-only.

#### Step 7 — Apply Hillside / Geotech / Coastal Bluff

Use `../residential-remodel/references/city-bluff-overlay.md` (shared). Multi-unit specifics:

- Most R-3 parcels are hillside or coastal-bluff (flat parcels in Laguna are virtually all R-1 + DSP).
- Geotechnical report required: slope stability, soil bearing, foundation recommendations, seismic shaking (SDC D).
- Bluff-edge setback calculated by geotech based on 75-100 year erosion projection (typically 25 ft minimum landward of bluff edge).
- Structural calcs must reconcile geotech with CBC Ch. 16 seismic (Risk Cat II, SDC D, Site Class per geotech).
- SWPPP + grading/drainage plan for any pad >50 cy or hillside development.

#### Step 8 — Check Heritage Committee Trigger

- Buildings >=50 years old: Heritage Committee review may be required (city historic register / California Register placement process).
- Many R-3 buildings in Laguna are 1950s-70s vintage = automatic trigger.
- If retaining any existing structure as part of the project, route through Heritage screening early.

#### Step 9 — State Preemption Cross-Check

Load `references/state-preemption.md` if applicant invokes ANY state housing law. State preemption **overrides Laguna's local restrictions** — including the 36 ft height cap, density limits, parking ratios, and DRB discretion — for qualifying projects.

Key paths:

- **SB 35 / SB 423** (Gov. Code §65913.4) — Ministerial streamlining for qualifying mixed-income projects when city lags RHNA. Laguna has historically lagged. SB 423 narrowed Coastal Zone exemption — some Coastal Zone parcels are now eligible.
- **AB 2011** (Gov. Code §65912.100-65912.139) — Ministerial approval for 100% affordable on commercial corridors, and mixed-income on commercial corridors. Pairs with DSP Phase II direction.
- **AB 1287** (effective Jan 1 2024) — Stacked density bonus, up to 100% bonus for very-low + moderate-income projects. Layers on top of Ch. 25.96.
- **Density Bonus Law** (Gov. Code §65915) — Codified in Laguna at Ch. 25.96. Forces concessions, parking reductions, waiver of development standards (including the 36 ft cap) when no feasibility-justified denial is supported.
- **SB 9** (Gov. Code §66411.7) — Codified at Ch. 25.95 with restrictive Laguna posture (1,000 sf cap, 16 ft height, 3-year owner-occupancy, no rooftop decks). SB 9 is an R-1 pathway but can produce duplex/4-plex outcomes that flow through this skill.

#### Step 10 — Verify Submittal Package

For ground-up multi-unit:

- 3 sets of 24" x 36" construction drawings (architectural, structural, MEP, energy, green building).
- 2 sets geotech / structural calcs / energy calcs.
- DRB submittal package: massing study, story poles, materials/color board, 21-day noticing list.
- CDP application (concurrent with entitlement; 2-year approval lifespan + extensions).
- Affordable / Density Bonus application (Ch. 25.96) if invoking bonus/concessions/waivers.
- Title 15 / LBFD review package: sprinkler plans, fire access, hydrant flow, fire-flow calcs.
- Geotech + grading for hillside/bluff sites.
- Construction phasing + hours plan (Laguna stricter than neighbors: weekdays 7:30 AM–6 PM only; **Saturday/Sunday/federal holidays all PROHIBITED** per §7.25.080(B) — no Sat window).
- WQMP / SWPPP for sites >50 cy grading.

For condo conversions: use `references/condo-conversion.md` — Ch. 25.47 process + tenant noticing + parking compliance + **CDP always required**.

---

### Output Format

Every Laguna Beach multi-unit residential review should include these city findings:

```markdown
## Laguna Beach City Overlay — Multi-Unit Residential
**Routing check:** Ground-up R-3 | ADU-to-MF (routed to ADU skill) | Condo conversion | DSP mixed-use | State-preempted streamlined
**Planning route:** Design Review | Zone Clearance | ADR | state-preempted route; include exact current category and staking if applicable
**Coastal/CDP:** Required (always for condo conversions) | Standard CDP | Appealable area | Admin CDP | De minimis waiver
**R-3 zoning:** PASS | FAIL | FLAG (density, 36 ft height, setbacks, coverage, open space)
**Parking:** PASS | FAIL | FLAG (multi-family ratio, guest parking, density-bonus override applied)
**Sprinklers/LBFD:** PASS | FAIL | FLAG (NFPA 13R for new MF; Title 15 §1103.5.4 plus LBMC §14.50.104/CBC §903.6 retrofit checks for alterations)
**WUI/fuel modification:** PASS | FAIL | FLAG (Class A roof, ignition-resistant exterior, glass skylights, 144 sq in vents)
**Hillside/bluff/geotech:** PASS | FAIL | FLAG | N/A
**Heritage:** Required | N/A
**State preemption:** N/A | SB 35/423 | AB 2011 | Density Bonus | AB 1287 (overrides local)
**Submittal completeness:** PASS | FAIL | FLAG
```

Return citations for every FAIL or FLAG. Do not cite state code for Laguna's local zoning numbers, do not use Ch. 14.52.030 as the multi-family sprinkler citation (it reaches only 1&2-family), do not omit LBMC §14.50.104/CBC §903.6 on a CBC-track Group R retrofit, and do not treat condo conversions as CDP-exempt under any circumstances.

---

## City Submittal Checklists

The City's own lists of what a submittal must contain. They ship in this plugin; paths are relative to this file.

- `../../requirements/README.md` — the index: which checklist covers which scope
- `../../requirements/plan-sheets/plan-sheet-matrix.md` — which plan sheets the project needs and what each sheet must show
- `../../requirements/building/` — the Building Division submittal checklists
- `../../requirements/planning/application-index.md` — which Planning application to file
- `../../requirements/issuance/issuance-checklist.md` — what is due after approval, before the permit issues

Choose the checklists from the project scope the evidence shows, not from the permit name. When a plan set exists, run `../plan-set-check/SKILL.md` on it. These are completeness checks. They do not check the design against the code.

---

## California Code Compliance

This plugin does not carry the California code checklist for Multi-Unit Residential plan sets: the building, residential, structural, fire and life-safety, energy, green-building, plumbing, mechanical, electrical and accessibility requirements. That check comes from CrossBeam.

**When the CrossBeam connector is connected** (the host has tools whose names start with `crossbeam_`):

1. Call `crossbeam_get_review_requirements` with `city: "laguna-beach"` and `permit_type: "multi-unit-residential"`. It returns the review lanes, the required documents and the packaging rules, with citations. Read it beside the City checklists above. Where they differ, tell the user and cite both. Coverage `none` means CrossBeam has no data, not that nothing is required.
2. Ask code questions with `crossbeam_ask`. Send the city (Laguna Beach, CA), the permit type and the project facts you have, and follow up with its `conversation_id`. A code section the answer cites that is not in its citations is unverified.
3. To check a plan set against the code, use a CrossBeam check. For a set drawn with CrossBeam's permit-drawings skill, call `crossbeam_get_skill` with `skill_id: "permit-drawings"` and follow `../../references/plan-sheets.md` section 2; permit-drawings runs the check. For a set drawn by someone else, the user uploads it for a CrossBeam check in the CrossBeam app, because the connector does not upload plans; then read the results with `crossbeam_list_projects`, `crossbeam_get_project_summary` and `crossbeam_get_findings`. A CrossBeam check is paid. Start one only with the user's approval.

CrossBeam cites the current 2025 California Building Standards Code (Title 24, effective 2026-01-01). Use its citations over code sections you remember. Apply the Laguna Beach rules above on top of them.

**When the connector is not connected**, or a tool is missing or needs sign-in:

- Do not check the design against the California codes from memory, and never report a California code item as passing.
- Do the Laguna Beach rules and the City checklists in full, then list California code compliance as **not checked**.
- Say it plainly, once: "This plugin checks the Laguna Beach rules and the City's submittal checklists for Multi-Unit Residential permits. It cannot check the plans against the California building codes. For that, connect CrossBeam (crossbeam-permits.com) and run a CrossBeam check before you file."
- Then carry on with intake, the City checklists and filing.

---

## References

Load these on demand. Paths are relative to this file.

- `../../requirements/README.md` — the City submittal checklists, plan-sheet matrix and issuance checklist
- `../plan-set-check/SKILL.md` — checks a plan set against the City checklists
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**Laguna Beach rules**

- `references/condo-conversion.md` — Laguna Beach Condominium Conversion (Ch. 25.47)
- `references/dsp-mixed-use.md` — Laguna Beach Downtown Specific Plan — Mixed-Use Residential
- `references/state-preemption.md` — State Housing Law Preemption — Laguna Beach Multi-Unit
- `references/zoning-r2-r3-envelope.md` — Laguna Beach R-2 / R-3 Zoning Envelope

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
