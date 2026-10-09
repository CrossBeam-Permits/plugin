---
name: kitchen-bath-remodel
description: "Kitchen/Bath Remodel permits in Laguna Beach, CA. A kitchen or bathroom remodelled in place: cabinets, fixtures, finishes, and the electrical, plumbing, and mechanical that serve them. A worksheet kind, so it runs as a plan set. A tub or shower swapped in place with no layout change is general-building. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions kitchen bath remodel in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2.5 CRC, Part 3 CEC, Part 4 CMC, Part 5 CPC, Part 6 Energy, Part 11 CALGreen); Residential Kitchen Remodel Handout, Residential Bathroom Renovation Handout, Residential Room Alteration/Remodel Checklist, Ch. 14.50 (CBC amendments), Ch. 14.52 (CRC amendments), Ch. 14.86 (CalGreen amendments)"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2025"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Kitchen/Bath Remodel Permit

Handles kitchen/bath remodel permits in Laguna Beach end-to-end. Scope: A kitchen or bathroom remodelled in place: cabinets, fixtures, finishes, and the electrical, plumbing, and mechanical that serve them. A worksheet kind, so it runs as a plan set. A tub or shower swapped in place with no layout change is general-building.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a kitchen/bath remodel permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Kitchen/Bath Remodel Permit

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

This skill covers Laguna Beach's city-specific requirements for residential kitchen and bathroom remodels. **Sprinkler retrofit triggers and major remodel thresholds make Laguna Beach kitchen/bath projects more complex than typical CA cities.**

**How this skill relates to state code**: The `california-kitchen-bath-remodel` skill covers all state-level plumbing, electrical, mechanical, waterproofing, energy, and safety requirements. This skill covers what Laguna Beach adds or changes. **Load state code first**, then this skill.

---

### Decision Tree Router

#### STEP 1: Determine OTC Eligibility

| Project Scope | Permit Track |
|--------------|--------------|
| **Same-configuration** kitchen or bath remodel (fixtures stay in same locations, minor structural only) | **OTC eligible** -- same-day counter review |
| Layout reconfiguration (moving fixtures, adding fixtures) | **Full plan review** required |
| Structural modification (wall removal, enlarged openings) | **Full plan review** + structural engineering |
| Cosmetic only (paint, mirrors, towel bars, floor covering -- no other work) | **No permit required** |

**OTC-eligible per the city reference OTC item 1** — residential kitchen and bathroom remodels with minor structural modifications. Hours and the full OTC list: `../city-reference/SKILL.md` §"Permit Processing Tracks".

**Important**: Even OTC-eligible remodels still require compliance with all items below.

#### STEP 2: Check Sprinkler Retrofit Trigger

**CRITICAL CHECK** -- This is the most commonly missed requirement in Laguna Beach kitchen/bath remodels.

**Sprinkler retrofit: two triggers, either one fires.** Load
`../residential-remodel/references/city-sprinkler-retrofit.md` and run both. Do not restate
the rule here.

- **Trigger A — Ch. 14.52.030 (valuation).** Cumulative value of additions, alterations and
  repairs in any three-year period exceeds 50% of the pre-work valuation.
- **Trigger B — Title 15 §1103.5.4 (scope).** Alteration of ≥50% of the building, OR work on
  ≥50% of the exterior, OR an added story.

**Kitchen/bath-specific note.** Trigger A is the one that usually fires on this permit type. A
high-end kitchen or a kitchen-plus-bath pair carries a large valuation while altering a small
share of the building, so it can cross the valuation threshold with Trigger B nowhere near
firing. Sum this project's valuation with every prior permit inside the three-year window
before answering. If the submitted documents do not state a valuation, report it as
undetermined and request it — do not assume.

#### STEP 3: Check Major Remodel Threshold

If the kitchen/bath remodel involves **wall removal or reinforcement**, check whether the project crosses the 50% major remodel threshold. This is an area-based calculation, separate from the valuation-based sprinkler trigger.

| Location | What Counts | Method |
|----------|-------------|--------|
| **Coastal zone appealable area** | Foundation LF + Wall LF (each floor) + Roof SF | Removal AND reinforcement |
| **Coastal zone non-appealable area** | Exterior wall LF only (each floor) | Removal only (not reinforcement) |

The City's Major Remodel Interpretation Quick Guide (Updated June 2026) counts walls on each floor and tests each building or structure on the site independently [source: https://www.lagunabeachcity.net/home/showpublisheddocument/23171/639179723814800000, as of 2026-09-29]. Compute each floor's wall percentage and the whole-structure total. The handout does not state how floors combine. If every floor is under 50%, the wall test is not met. If a floor is at 50% or more and the whole-structure total is also at 50% or more, the test is met. If a floor is at 50% or more but the whole-structure total is under 50%, return FLAG (not FAIL, not PASS), show both numbers, and state that the City must confirm how floors combine. Full rule: `../residential-remodel/references/city-major-remodel-methodology.md`.

**Interior-only kitchen/bath remodels generally do NOT trigger major remodel** because the calculation is based on exterior walls, foundation, and roof. However:
- Removing/reinforcing exterior walls to accommodate kitchen/bath enlargement counts
- Cumulative work since January 13, 1993 baseline is tracked
- If major remodel is triggered, project is treated as new construction (full plan review, DRB hearing, CalGreen triggers)

#### STEP 4: Check Sewer Video Requirement

| Trigger | Requirement |
|---------|-------------|
| **Any increase in plumbing fixture count** | Sewer video required |
| Work valued at **over $100,000** AND located **north of Cardinal Drive** | Sewer video required |

This is a city-specific requirement not found in state code. The sewer video must be provided before or at the time of plan check submittal.

#### STEP 5: Additional City-Specific Checks

Walk each item. For every check, record PASS / FAIL / FLAG / N/A.

| # | Check | What to Verify | Source |
|---|-------|---------------|--------|
| 1 | **Sprinkler retrofit trigger** | Run BOTH triggers. (A) 3-year cumulative valuation vs. 50% of pre-work valuation. (B) scope: ≥50% of building altered / ≥50% of exterior / added story. Either one firing requires the retrofit. | Ch. 14.52.030 **and** Title 15 §1103.5.4 |
| 2 | **Sewer video** | Required if adding fixtures or if >$100K north of Cardinal Dr | City handout |
| 3 | **Major remodel threshold** | Calculate if wall removal/reinforcement approaches 50% | Major Remodel Handout |
| 4 | **Design Review** | Interior-only remodels are generally EXEMPT from Design Review. Exterior changes (new windows, enlarged openings visible from public) may trigger Administrative Design Review. | S25.05.040 |
| 5 | **Coastal Development Permit** | Most of city is in Coastal Zone. Interior-only remodels may be exempt, but check if scope changes trigger CDP. | Ch. 25.07 |
| 6 | **VHFHSZ window compliance** | If replacing windows as part of remodel: welded vinyl corners + metal reinforcing required, no plastic skylights (glass only) | Ch. 14.70 |
| 7 | **Heritage review** | Property 50+ years old may require Heritage Committee review | City policy |
| 8 | **Window specifications** | New/replacement windows must be dual pane with one pane tempered | Room Alteration Checklist |
| 9 | **City business license** | Contractor must hold a Laguna Beach business license | City policy |
| 10 | **Green Halo Program** | Sign-up required for C&D recycling and waste diversion compliance | City policy |

---

### CalGreen Triggers via Major Remodel

If the project triggers major remodel status (directly or cumulatively), the following CalGreen amendments apply:

| Trigger | Requirement | Code Section |
|---------|-------------|-------------|
| Major remodel of SFR | **Wood-burning fireplace retrofit** -- existing wood-burning fireplace must be retrofitted to comply with U.S. EPA Phase II emission limits (retrofit insert, gas conversion, or other approved device) | Ch. 14.86.013, S4.503.2 |
| Major remodel of SFR with attached garage | **EV charger raceway** -- trade size 1 raceway from main panel to proposed EV charger location, with 40A 208/240V capacity reserved | Ch. 14.86.011, S4.106.4.5 |
| Any new gas fireplace | Must be direct-vent sealed-combustion type | Ch. 14.86.013, S4.503.1 |

---

### Submittal Requirements (Full Plan Review)

When a kitchen/bath remodel requires full plan review (layout reconfiguration, structural modification, or triggered escalation), the following submittals are required per the city's Residential Room Alteration/Remodel checklist:

| Document | Requirement |
|----------|-------------|
| **Plan sets** | 2 sets of 24"x36" scaled drawings |
| **Title sheet** | Owner name, address, project address, scope of work, index, vicinity map, deferred submittals |
| **Adopted codes statement** | Reference 2025 editions of all California codes + local ordinances |
| **Floor plan** | New and existing layout with doors, windows, headers, outlets, switches, FAU, registers, fixtures |
| **Section cuts** | Through addition/modification showing framing, relationship to existing structure |
| **Structural plans** | Framing members, beams, lateral system, footings, details (if structural work) |
| **Structural calculations** | 2 sets justifying framing, beams, footings, lateral system (if structural work) |
| **Energy compliance forms** | 2 sets (Title 24 CF-1R, MF-1R) |
| **Sewer video** | If fixture count increases or >$100K north of Cardinal Drive |

---

### Key Laguna Beach Kitchen/Bath Remodel Facts

- **OTC eligible**: Yes, the city reference OTC item 1 -- same configuration, minor structural only
- **Sprinkler retrofit**: Two triggers, either fires — Ch. 14.52.030 (50% of pre-work valuation cumulative over any 3-year period) and Title 15 §1103.5.4 (scope). See `../residential-remodel/references/city-sprinkler-retrofit.md`
- **Sprinkler standard**: NFPA 13D + flow switch + exterior alarm + interconnected smoke-detector activation; separate control valves require alarm-service supervision
- **Sewer video**: Required for any fixture count increase, or >$100K north of Cardinal Dr
- **Major remodel**: 50% threshold, two calculation methods (coastal zone appealable vs non-appealable); walls counted on each floor
- **Planning route**: Interior-only work takes Zone Clearance under current §25.05.040(B)(2)(d); exterior scope must match the current closed lists and does not default to ADR
- **No local plumbing amendments**: Ch. 14.64 adopts CPC without modification
- **No local mechanical amendments**: Ch. 14.54 adopts CMC without modification
- **No local electrical amendments**: Ch. 14.68 adopts CEC without modification

---

## California Checklist

The California checklist for this permit is in `references/california-baseline.md`. Walk its decision tree and every checklist row after the Laguna Beach rules above. For each row, decide whether it is checked at plan check or verified by the inspector in the field. Do not list inspection items as corrections.

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/electrical-kitchen-bath.md` — Electrical Requirements — Kitchen & Bathroom Remodel
- `references/energy-lighting.md` — Energy Code & Lighting — Kitchen & Bathroom Remodel
- `references/plumbing-fixtures.md` — Plumbing Fixtures — Kitchen & Bathroom Remodel
- `references/ventilation-exhaust.md` — Ventilation & Exhaust — Kitchen & Bathroom Remodel
- `references/waterproofing.md` — Waterproofing — Kitchen & Bathroom Remodel

**Laguna Beach rules**

- `references/city-sewer-video-submittals.md` — Laguna Beach -- Sewer Video Requirements and Submittal Rules for Kitchen/Bath Remodels

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
