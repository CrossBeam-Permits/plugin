---
name: demolition
description: "Demolition (Full Structure) permits in Laguna Beach, CA. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against the Laguna Beach rules and the City submittal checklists, and prepares a portal-ready submission; (B) CITY REVIEWER — checks a submittal against the Laguna Beach rules and produces tight corrections output. California code compliance comes from the CrossBeam connector when it is connected. Use when the user mentions demolition in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2), Chapter 33; 2025 California Existing Building Code (Title 24, Part 10), Chapter 15; 2025 California Green Building Standards Code (Title 24, Part 11), §4.408 / §5.408; SCAQMD Rule 1403; BAAQMD Regulation 11 Rule 2; EPA Lead Renovation, Repair & Painting Rule (40 CFR Part 745, Subpart E); CDPH Title 17 CCR §35001 et seq.; California Government Code §§7260–7277; Urgency Ord. 1732 (LBMC 25.05.040, 25.05.045, 25.45.004, 25.45.010); LBMC Ch. 25.07, 25.45.014; Urgency Ord. 1713 (LBMC 25.17.010(e)(2)(D), 25.17.020(c)(2)); Major Remodel Interpretation Quick Guide (Updated October 2026); LBMC 14.50.132"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-10-10"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Demolition (Full Structure) Permit

Handles demolition (full structure) permits in Laguna Beach end-to-end.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a demolition (full structure) permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Demolition (Full Structure) Permit

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

**Base skill:** the California Demolition (Full Structure) rules, which come from the CrossBeam connector (see "California Code Compliance" below)
**This skill contains ONLY items where Laguna Beach differs from state code.**
**All state checklist items apply unless explicitly overridden below.**

Note: Demolition rules are predominantly local — most of this skill's content represents city-specific requirements.

---

### Decision Tree Router

| Topic | Route |
|-------|-------|
| **Full demolition of a structure** | Demolition Notification form + the permits below |
| **Partial demolition (remodel)** | Run the major-remodel test first (`../residential-remodel/references/city-major-remodel-methodology.md`) |
| **Garage demolished for an ADU** | Reviewed and issued with the ADU application (Ord. 1713, LBMC 25.17.010(e)(2)(D); coastal: 25.17.020(c)(2)(A)(i)). Load `../adu/SKILL.md` |
| **Historic resource** | §25.45.014 demolition procedure (below) |

---

### Demolition Requirements

#### Demolition Notification
- **Demolition Notification form required** (standard-plans/demolition-notification.pdf)
- Must be submitted to Building Division before permit issuance

#### Required Permits/Reviews

| Trigger | Required |
|---------|----------|
| Any demolition | Building Permit + Demolition Notification |
| Property in Coastal Zone | **CDP review.** "Development" includes "the construction, reconstruction, demolition or alteration of the size of any structure" (§25.07.006). No §25.07.008 exemption names demolition. A CDP is required unless Planning finds an exemption or a categorical exclusion (§25.07.010; E-93-1 covers single-family residential development in eleven areas, subject to Special Condition 8). Demolition of a historic resource always requires a CDP (§25.45.014(A)). Whether E-93-1 clears a stand-alone single-family demolition is UNSETTLED; confirm with Planning at pre-application |
| Demolition that is part of a major remodel | **Design Review**, §25.05.040(B)(1)(a); heard by the Design Review Board for a single-family or two-family project (§25.05.040(F)(1)) |
| Demolition that is not part of a major remodel | **Zone Clearance**, §25.05.040(B)(2)(a) ("Demolition, alteration, or addition that does not constitute a major remodel"), unless another (B)(1) item or the ESA override applies |
| Full demolition followed by a new building | The new building is Design Review, §25.05.040(B)(1)(b), unless it is an ADU or a Chapter 25.13 primary dwelling ((B)(2)(h), (z)). File the demolition with the new-building application |
| Full demolition with no replacement | Zone Clearance (B)(2)(a) is the closest list item. UNSETTLED; confirm with Planning at pre-application |
| Historic resource (§25.45.004) | Heritage Committee recommendation, CEQA, then a public hearing before the design review authority (§25.45.014(B)-(C)). An approved demolition waits 90 calendar days for relocation or documentation, with monthly newspaper advertisement for the first two months; the authority may extend the wait up to 180 days if relocation is imminent (§25.45.014) |
| Any demolition | **SCAQMD Rule 1403 notification** required for ALL demolitions (SCAQMD defines demolition broadly as "wrecking or taking out of any load-supporting structural member") |

**Historic resource** means a property or structure on the City's historic register, listed on or officially determined eligible for the California Register or the National Register, or one "the City is mandated by law to treat as a historic resource based on substantial evidence in light of the whole record" (§25.45.004, as amended by Ord. 1732). Building age alone is not a code trigger. Staff may ask for a historic resource assessment of an older building (UNSETTLED; confirm with Planning at pre-application).

**ESA override.** Zone Clearance "may not be used for any listed project in an environmentally sensitive area" (now including slopes of 30% or more, §25.08 as amended by Ord. 1732) unless a licensed professional finds, subject to peer review, no impact; otherwise Design Review applies (§25.05.040(B)(2), (B)(1)(e)).

#### Major Remodel Connection
Demolition of 50%+ of exterior walls (computed on each floor and for the whole structure; if a floor is at 50%+ but the whole-structure total is under 50%, return FLAG — how floors combine is UNSETTLED, see `../residential-remodel/references/city-major-remodel-methodology.md`), or, in the coastal zone appealable area, of the roof, exterior walls, load-bearing interior walls, and foundation combined, measured for each building or structure separately, makes the work a major remodel (Major Remodel Interpretation Quick Guide, Updated October 2026). The structure is then a new building subject to current zoning, undergrounding, dedications and new-development fees (§25.56.011). In the non-appealable area only removal counts; reinforcement does not.

**ADU demolition is EXEMPT** from the major remodel calculation (except Coastal Act section 30253 work on bluff-top, beachfront and coastal-canyon lots; Ord. 1713, LBMC 25.17.020(d)(2)).

---

### Additional Demolition Requirements

#### Utility Meter Removal
Utility meters (gas, electric, water) must be removed/disconnected before demolition. Coordinate with utility providers for meter pulls prior to permit issuance.

#### Green Halo Program — C&D Recycling/Diversion
Construction & demolition (C&D) debris recycling/diversion is required under the Green Halo Program. Demolition projects must comply with waste diversion requirements.

#### Protection of Adjoining Property
Per §14.50.132, the applicant must provide:
- **30-day written notice** to owners of adjoining property before demolition
- **Bond** for protection of adjoining property

---

### Key Facts

- **Demolition Notification**: Required form, submitted to Building Division
- **Planning route**: major-remodel demolition → Design Review (B)(1)(a); other demolition → Zone Clearance (B)(2)(a), subject to the ESA override
- **Historic resource**: §25.45.014 — Heritage Committee, CEQA, hearing, CDP; age alone is not a code trigger
- **Coastal Zone**: demolition is development (§25.07.006); CDP unless Planning finds an exemption or exclusion
- **Garage for an ADU**: reviewed and issued with the ADU (Ord. 1713, 25.17.010(e)(2)(D))
- **SCAQMD**: Rule 1403 notification required for ALL demolitions
- **Utility meters**: Must be removed/disconnected before demolition
- **C&D diversion**: Green Halo Program recycling/diversion required
- **Adjoining property**: 30-day notice + bond required (§14.50.132)

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

This plugin does not carry the California code checklist for Demolition (Full Structure) plan sets: the building, residential, structural, fire and life-safety, energy, green-building, plumbing, mechanical, electrical and accessibility requirements. That check comes from CrossBeam.

**When the CrossBeam connector is connected** (the host has tools whose names start with `crossbeam_`):

1. Call `crossbeam_get_review_requirements` with `city: "laguna-beach"` and `permit_type: "demolition"`. It returns the review lanes, the required documents and the packaging rules, with citations. Read it beside the City checklists above. Where they differ, tell the user and cite both. Coverage `none` means CrossBeam has no data, not that nothing is required.
2. Ask code questions with `crossbeam_ask`. Send the city (Laguna Beach, CA), the permit type and the project facts you have, and follow up with its `conversation_id`. A code section the answer cites that is not in its citations is unverified.
3. To check a plan set against the code, use a CrossBeam check. For a set drawn with CrossBeam's permit-drawings skill, call `crossbeam_get_skill` with `skill_id: "permit-drawings"` and follow `../../references/plan-sheets.md` section 2; permit-drawings runs the check. For a set drawn by someone else, the user uploads it for a CrossBeam check in the CrossBeam app, because the connector does not upload plans; then read the results with `crossbeam_list_projects`, `crossbeam_get_project_summary` and `crossbeam_get_findings`. A CrossBeam check is paid. Start one only with the user's approval.

CrossBeam cites the current 2025 California Building Standards Code (Title 24, effective 2026-01-01). Use its citations over code sections you remember. Apply the Laguna Beach rules above on top of them.

**When the connector is not connected**, or a tool is missing or needs sign-in:

- Do not check the design against the California codes from memory, and never report a California code item as passing.
- Do the Laguna Beach rules and the City checklists in full, then list California code compliance as **not checked**.
- Say it plainly, once: "This plugin checks the Laguna Beach rules and the City's submittal checklists for Demolition (Full Structure) permits. It cannot check the plans against the California building codes. For that, connect CrossBeam (crossbeam-permits.com) and run a CrossBeam check before you file."
- Then carry on with intake, the City checklists and filing.

---

## References

Load these on demand. Paths are relative to this file.

- `../../requirements/README.md` — the City submittal checklists, plan-sheet matrix and issuance checklist
- `../plan-set-check/SKILL.md` — checks a plan set against the City checklists
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
