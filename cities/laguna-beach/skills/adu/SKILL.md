---
name: adu
description: "ADU (Accessory Dwelling Unit) permits in Laguna Beach, CA. A new accessory dwelling unit or JADU, attached, detached, or converted from existing space. Always a plan set. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against the Laguna Beach rules and the City submittal checklists, and prepares a portal-ready submission; (B) CITY REVIEWER — checks a submittal against the Laguna Beach rules and produces tight corrections output. California code compliance comes from the CrossBeam connector when it is connected. Use when the user mentions adu in Laguna Beach."
metadata:
  version: "2.0"
  source: "HCD ADU Handbook, January 2025 (54 pages) + January 2026 Addendum (pages 55-58)"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2026"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — ADU (Accessory Dwelling Unit) Permit

Handles adu (accessory dwelling unit) permits in Laguna Beach end-to-end. Scope: A new accessory dwelling unit or JADU, attached, detached, or converted from existing space. Always a plan set.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a adu (accessory dwelling unit) permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach ADU (Accessory Dwelling Unit) Permit

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

**Base skill:** the California ADU (Accessory Dwelling Unit) rules, which come from the CrossBeam connector (see "California Code Compliance" below)
**This skill contains ONLY items where Laguna Beach differs from state code.**
**All state checklist items apply unless explicitly overridden below.**

**Laguna Beach ADUs are significantly more complex than typical CA cities** because most of the city is in the Coastal Zone, requiring a Coastal Development Permit (CDP) before a building permit can issue.

---

### Decision Tree Router

#### STEP 1: Is the Property in the Coastal Zone?

**Most of Laguna Beach IS in the Coastal Zone.** If unsure, assume yes and check.

| Location | CDP Required? | Process |
|----------|--------------|---------|
| NOT in Coastal Zone | NO | Ministerial → 60-day shot clock |
| IN Coastal Zone, converting existing livable space | NO (exempt) — **see note below** | Ministerial → 60-day shot clock |
| IN Coastal Zone, new construction/addition | **YES** | CDP process (de minimis / minor / standard) |

#### STEP 2: ADU or JADU?

| Type | CDP Required? | Key Rules |
|------|--------------|-----------|
| **JADU** (≤500 sf, within SFR) | **NO** — always exempt from CDP | Building permit only, 60-day shot clock |
| **ADU** (not in Coastal Zone) | **NO** | Building permit only, 60-day shot clock |
| **ADU** (Coastal Zone, converting livable space) | **NO** (exempt) — **see note below** | Building permit only, 60-day shot clock |
| **ADU** (Coastal Zone, new construction) | **YES** | See CDP process below |

**CDP exemption-loss note**: The "converting existing livable space = CDP exempt" rule is LOST under §25.07.008(A)(1)(b)-(g) when the project is: near a bluff edge, within ESHA (environmentally sensitive habitat area), in a scenic area, or when the project increases floor area by more than 10%. In those cases, a CDP is required even for conversions.

#### STEP 3: For ADUs Requiring CDP — Which Category?

| Category | When to Use | Fee | Hearing? | Appeal? |
|----------|-----------|-----|----------|---------|
| **De minimis** | No adverse coastal impact, not in appealable area, no LCP questions, no public opposition | $125 | No | N/A |
| **Minor** | No adverse coastal impact, no LCP questions, no other discretionary entitlements | $952 | Only if requested | Yes |
| **Standard** | When de minimis and minor don't apply | $952 | Yes (public hearing) | Yes |

#### STEP 4: Review Checklist

| # | Check | What to Verify |
|---|-------|---------------|
| 1 | Coastal Zone status? | Determine if property is in Coastal Zone |
| 2 | ADU or JADU? | JADU always exempt from CDP |
| 3 | New construction or conversion? | Converting existing livable space = CDP exempt |
| 4 | CDP category? | De minimis / minor / standard based on circumstances |
| 5 | State ADU standards met? | Size limits, setbacks, height per state skill |
| 6 | LBMC Ch. 25.17 standards met? | Local development standards |
| 7 | LCP conformity? | Certified Local Coastal Program compliance |
| 8 | Coastal resource impacts? | Public views, habitat, access — private views NOT considered |
| 9 | Other discretionary approvals? | Grading, elevated decks, etc. → separate process |
| 10 | Building code compliance? | CBC/CRC per state code + city amendments (sprinklers!) |

---

### Critical Laguna Beach ADU Rules

#### Fire Sprinklers
ADUs require fire sprinklers ONLY if the primary dwelling is already sprinklered or if the ADU project fires a sprinkler retrofit trigger on the primary dwelling. If the primary dwelling has no sprinklers, the ADU itself is exempt per §25.17.050(D) — state ADU law bars a sprinkler requirement on an ADU where the primary dwelling is not required to have one.

There are **two retrofit triggers on the primary dwelling, and either one fires** (full rule: `../residential-remodel/references/city-sprinkler-retrofit.md`):
- **Ch. 14.52.030** (valuation) — cumulative additions, alterations and repairs in any three-year period exceeding 50% of the pre-work valuation.
- **Title 15 §1103.5.4** (scope) — alteration of ≥50% of the building, OR work on ≥50% of the exterior, OR an added story.

An attached ADU or a conversion that reworks the main house can fire either one. A detached new ADU generally does not.

#### Design Review
ADUs are ministerial approvals and should NOT require Design Review Board hearing. However, if the ADU project includes other discretionary components (grading, elevated decks), those components go through normal discretionary process.

#### Major Remodel Exemption
ADU construction and remodeling are **EXEMPT** from major remodel calculation. Building an ADU does not count toward the 50% threshold. **Exception**: §25.17.030(A)(3) carves out blufftop, beachfront, and canyon projects — these may still be treated as major remodels even when an ADU is involved.

#### Opposition Cannot Block ADU
For CDP hearings, the decision-maker can ONLY consider LCP conformity and coastal resource impacts. **Opposition to the ADU itself cannot be considered.** City cannot deny CDP based on private view impacts.

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

This plugin does not carry the California code checklist for ADU (Accessory Dwelling Unit) plan sets: the building, residential, structural, fire and life-safety, energy, green-building, plumbing, mechanical, electrical and accessibility requirements. That check comes from CrossBeam.

**When the CrossBeam connector is connected** (the host has tools whose names start with `crossbeam_`):

1. Call `crossbeam_get_review_requirements` with `city: "laguna-beach"` and `permit_type: "adu"`. It returns the review lanes, the required documents and the packaging rules, with citations. Read it beside the City checklists above. Where they differ, tell the user and cite both. Coverage `none` means CrossBeam has no data, not that nothing is required.
2. Ask code questions with `crossbeam_ask`. Send the city (Laguna Beach, CA), the permit type and the project facts you have, and follow up with its `conversation_id`. A code section the answer cites that is not in its citations is unverified.
3. To check a plan set against the code, use a CrossBeam check. For a set drawn with CrossBeam's permit-drawings skill, call `crossbeam_get_skill` with `skill_id: "permit-drawings"` and follow `../../references/plan-sheets.md` section 2; permit-drawings runs the check. For a set drawn by someone else, the user uploads it for a CrossBeam check in the CrossBeam app, because the connector does not upload plans; then read the results with `crossbeam_list_projects`, `crossbeam_get_project_summary` and `crossbeam_get_findings`. A CrossBeam check is paid. Start one only with the user's approval.

CrossBeam cites the current 2025 California Building Standards Code (Title 24, effective 2026-01-01). Use its citations over code sections you remember. Apply the Laguna Beach rules above on top of them.

**When the connector is not connected**, or a tool is missing or needs sign-in:

- Do not check the design against the California codes from memory, and never report a California code item as passing.
- Do the Laguna Beach rules and the City checklists in full, then list California code compliance as **not checked**.
- Say it plainly, once: "This plugin checks the Laguna Beach rules and the City's submittal checklists for ADU (Accessory Dwelling Unit) permits. It cannot check the plans against the California building codes. For that, connect CrossBeam (crossbeam-permits.com) and run a CrossBeam check before you file."
- Then carry on with intake, the City checklists and filing.

---

## References

Load these on demand. Paths are relative to this file.

- `../../requirements/README.md` — the City submittal checklists, plan-sheet matrix and issuance checklist
- `../plan-set-check/SKILL.md` — checks a plan set against the City checklists
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**Laguna Beach rules**

- `references/city-adu-faq.md` — Laguna Beach ADU/JADU — FAQ & Coastal Development Permit Process
- `references/city-adu-ordinance.md` — Laguna Beach ADU/JADU Development Standards — Quick Reference
- `references/city-coastal-permits.md` — Laguna Beach ADU — Coastal Development Permit Requirements

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
