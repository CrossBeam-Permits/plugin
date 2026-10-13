---
name: residential-addition
description: "Residential Addition permits in Laguna Beach, CA. Floor area or outdoor living area added to an existing dwelling, at any size, including a new or enlarged deck, balcony, or covered porch. Always a plan set. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against the Laguna Beach rules and the City submittal checklists, and prepares a portal-ready submission; (B) CITY REVIEWER — checks a submittal against the Laguna Beach rules and produces tight corrections output. California code compliance comes from the CrossBeam connector when it is connected. Use when the user mentions residential addition in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2 CBC, Part 2.5 CRC, Part 3 CEC, Part 4 CMC, Part 5 CPC, Part 6 Energy, Part 11 CALGreen); Urgency Ord. 1732 (LBMC 25.05.040, 25.05.045, 25.56.011); LBMC Ch. 25.07, 25.45; Major Remodel Interpretation Quick Guide (Updated October 2026); LBMC 14.52.030; Title 15 §1103.5.4; Building Plan Check Submittal Requirements (May 2026)"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-10-10"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Residential Addition Permit

Handles residential addition permits in Laguna Beach end-to-end. Scope: Floor area or outdoor living area added to an existing dwelling, at any size, including a new or enlarged deck, balcony, or covered porch. Always a plan set.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a residential addition permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Residential Addition Permit

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

**Base skill:** the California Residential Addition rules, which come from the CrossBeam connector (see "California Code Compliance" below)
**This skill contains ONLY items where Laguna Beach differs from state code.**
**All state checklist items apply unless explicitly overridden below.**

---

### Decision Tree Router

#### STEP 1: What Kind of Project?

| Project Type | Route |
|-------------|-------|
| **Kitchen remodel** (same configuration, minor structural) | OTC eligible |
| **Bathroom remodel** (same configuration, minor structural) | OTC eligible |
| **Room alteration/remodel** | OTC eligible if minor |
| **Window/door replacement** (same openings) | OTC eligible |
| **Exterior siding replacement** | OTC eligible |
| **Deck/balcony/patio cover repair** (no extension) | OTC eligible |
| **Addition or major remodel** | Full plan review → STEP 2 |

#### STEP 2: Is It a Major Remodel?

Determine whether the project crosses the 50% threshold: it decides Design Review, the Coastal Development Permit and the new-building rules in STEP 3. Use the correct calculation method based on location. Apply the City's Major Remodel Interpretation Quick Guide, Updated October 2026 [source: https://www.lagunabeachcity.net/home/showpublisheddocument/23171/639264703759000000, as of 2026-10-09].

| Location | Calculation Method | What Counts |
|----------|-------------------|-------------|
| **Coastal zone appealable area** | Foundation LF + Wall LF (each floor) + Roof SF | Removal AND reinforcement |
| **Coastal zone non-appealable area** | Exterior wall LF only (each floor) | Removal only (not reinforcement) |

- Run the test for **each building or structure** on the site independently.
- Compute one wall percentage **for each floor**, and the whole-structure total (all floors of that structure). The October 2026 handout does not state how floors combine. Apply this rule:
  1. Every floor under 50% → wall test not met.
  2. At least one floor at 50%+ AND whole-structure total at 50%+ → wall test met.
  3. At least one floor at 50%+ BUT whole-structure total under 50% → do not decide. Return FLAG (not FAIL, not PASS); the City must confirm how floors combine. Show both numbers.

**Major remodel = 50%+ demolition/reinforcement OR greater than 50% cumulative addition to that structure since its Jan 13, 1993 baseline**

- **Expansion floor area (October 2026):** attached garage and other attached non-habitable area excluded; a detached non-habitable structure counts in full; a garage conversion is a FLAG. Apply the rules in `references/city-major-remodel.md` → Expansion Floor Area.

When the principal structure is a major remodel, all associated accessory structures and improvements "shall lose their legal, nonconforming status" (October 2026 handout). See `references/city-major-remodel.md`.

#### STEP 3: What Permits/Reviews Are Needed?

| Trigger | Required |
|---------|----------|
| Any construction/alteration | Building Permit |
| Addition constitutes a major remodel | **Design Review** under current §25.05.040(B)(1)(a), heard by the Design Review Board for a single-family or two-family project (§25.05.040(F)(1)) |
| Addition includes any improvement over 15 ft | **Design Review** under §25.05.040(B)(1)(c) |
| Non-major addition and all improvements are no more than 15 ft | **Zone Clearance**, not Design Review, under §25.05.040(B)(2)(a)-(b), unless another closed-list trigger or ESA override applies |
| Property in Coastal Zone (most of city), addition is a major remodel | **Coastal Development Permit** (Ch. 25.07; a major remodel is new development). In a Categorical Exclusion E-93-1 area: UNSETTLED, confirm with Planning |
| Property in Coastal Zone, addition is not a major remodel | Normally **exempt** as an improvement to a single-family dwelling (§25.07.008(A)(1)), recorded by Planning (§25.07.008(B)). **CDP required** if any of (A)(1)(b)-(g) applies: e.g., within 50 ft of a bluff edge, in an ESA or highly scenic area, or, only between the sea and the first public road or within 300 ft of the beach, a 10% or greater floor-area increase or a height increase over 10% |
| Major remodel triggered | Classified as a new building under §25.56.011: current zone standards, undergrounding, required dedications, and new-development fees |
| Property in VHFHSZ or Fuel Modification area | **WUI compliance** (Ch. 14.70). The VHFHSZ alone does not require sprinklers in an existing house; the retrofit triggers below do. For a major remodel on an FM or VHFHSZ parcel, Fire Safety Standards Review (§25.05.040(C)(4)) |
| Addition adds one or more stories, OR reaches ≥50% of the building, OR the three-year cumulative valuation exceeds 50% of the pre-work valuation (≥50% of the exterior alone: UNSETTLED, give both readings) | **Full sprinkler retrofit** of the entire dwelling + attached garage — Ch. 14.52.030 **and** Title 15 §1103.5.4, either one fires |
| Hillside property | **Geotechnical report** may be required |
| Property is a historic resource (city register, California or National Register listed or determined eligible, or one the City must treat as historic; §25.45.004 as amended by Ord. 1732) | Major modification: **Design Review** (B)(1)(d). Qualifying minor alteration: **Administrative Design Review** (B)(3)(a)(iv), no hearing waiver. Either way the Heritage Committee reviews and recommends first (§25.45.010). Age alone is not a code trigger; staff may ask for a historic resource assessment on an older structure (UNSETTLED; confirm with Planning at pre-application) |

---

### Full Review Checklist (Addition/Major Remodel)

| # | Check | What to Verify |
|---|-------|---------------|
| 1 | Major remodel threshold? | Calculate using correct method (coastal zone appealable vs non-appealable), for each structure, walls on each floor |
| 2 | Coastal Zone? | Major remodel: CDP. Non-major addition: check the §25.07.008(A)(1) exemption and its (b)-(g) exceptions; the 10% items apply only in the first-road/300-ft strip |
| 3 | Current planning route? | Match Ord. 1732's closed lists. Major remodel → Design Review `(B)(1)(a)`; improvement over 15 ft → Design Review `(B)(1)(c)`; otherwise a non-major addition/improvement no more than 15 ft → Zone Clearance `(B)(2)(a)-(b)`, unless another trigger or the ESA override applies. |
| 4 | VHFHSZ compliance? | Sprinklers, fire-resistive construction per Ch. 14.70 |
| 4a | Sprinkler retrofit? | **Two triggers, either one fires** — see `../residential-remodel/references/city-sprinkler-retrofit.md`. (A) Ch. 14.52.030: cumulative additions/alterations/repairs in any 3-year period > 50% of pre-work valuation. (B) Title 15 §1103.5.4: ≥50% of building altered, or a story added. **An addition of a story above grade fires (B) outright.** Whether ≥50% of the exterior alone fires (B), and whether a new basement or lower level is an "added story", are UNSETTLED; confirm with Building and Fire at pre-application. Addition valuation counts toward (A). |
| 5 | Zoning compliance? | Setbacks, height, coverage, FAR per zoning table |
| 6 | Historic resource? | Ch. 25.45 definition; (B)(1)(d) or (B)(3)(a)(iv) |
| 7 | Geotech required? | Hillside properties may need geotechnical report |
| 8 | Submittal complete? | 4 sets 24"x36" plans for additions >=500 SF; 2 sets for additions <500 SF + 2 sets calcs (structural, energy, geotech) |
| 9 | State code compliance? | CBC/CRC per state skills + city amendments |
| 10 | Neighbor notification? | 21 calendar days notice for DRB hearings; 14 calendar days for Administrative Design Review (§25.05.065(D)) |

---

### OTC-Eligible Remodels

These projects qualify for over-the-counter (same-day) plan review:

- Kitchen remodel (same configuration, minor structural)
- Bathroom remodel (same configuration, minor structural)
- Room alteration/remodel (minor scope)
- Window/door replacement (same openings or minor structural mods)
- Exterior siding replacement
- Deck/balcony/patio cover repairs (no extension/replacement)

**OTC availability**: see `../city-reference/SKILL.md` §"Permit Processing Tracks" for hours, the full 11-item OTC list, and the disqualifiers.

**Important**: Even OTC remodels may need Zoning/Planning approval if exterior changes are involved.

---

### Current Design Review / Zone Clearance Pathway

Urgency Ordinance No. 1732 inverted the former exterior-work default. Use the three closed lists in §25.05.040(B), not the retired project-tier table:

- **Design Review:** a major remodel under (B)(1)(a), an improvement over 15 feet under (B)(1)(c), or another listed (B)(1) trigger. The Design Review Board hears single-family and two-family projects; the Planning Commission hears three or more units, Downtown Specific Plan projects and non-residential work (§25.05.040(F)(1)).
- **Zone Clearance:** a non-major demolition/alteration/addition under (B)(2)(a) and an improvement no more than 15 feet under (B)(2)(b), unless another trigger applies.
- **Administrative Design Review:** only when the work matches one of the 17 categories in (B)(3); it is no longer the residual route for exterior work.

Development in an environmentally sensitive area routes to Design Review unless a licensed professional determines, subject to peer review, that it does not impact the ESA. A CDP may still be required. If no closed-list category can be matched, return `needs_source` instead of applying the old default.

**Early neighbor communication**: For DRB projects, applicant must contact property owners within 300 ft per §25.05.040(C)(1).

**Staking requirements** per §25.05.040(C)(2): Staking poles and connecting ribbons representing the full extent of the proposed structure (including decks and eaves) must be constructed and certified by a registered land surveyor at least 21 calendar days before the first DRB/Planning Commission hearing, or 14 calendar days before an Administrative Design Review hearing when staking applies. Section 25.05.065(D) separately uses the same 21/14 periods for mailed hearing notice. A deposit for staking removal is required before the project is scheduled for public hearing; poles must be removed within 20 calendar days after final decision or the deposit is forfeited.

**Fire Safety Standards Review** per §25.05.040(C)(4): Prior to deliberation on a design review application for new construction and major remodels, the Fire Department or Building Division, as applicable, shall review and approve or conditionally approve the application, including proposed fuel modification programs. Public-safety conditions may not be modified by the design review authority without that review authority's concurrence. The former 50%-alteration Fire-Department-only trigger is not current.

---

### CalGreen Major Remodel Triggers

City adopts CalGreen via Ch. 14.86. Major remodels trigger CalGreen requirements — see state CalGreen skill for specific requirements.

---

### Key Laguna Beach Residential Facts

- **Major remodel threshold**: 50% (demolition/reinforcement or cumulative addition)
- **Two calculation methods**: Coastal zone appealable (more restrictive) vs. coastal zone non-appealable; walls counted on each floor; each structure tested independently
- **Baseline date**: January 13, 1993, for each structure (or date of subsequent new construction/major remodel of that structure)
- **ADU construction**: EXEMPT from major remodel calculation
- **Design Review**: required for a major remodel, an improvement over 15 ft, or another enacted (B)(1) category
- **Zone Clearance**: current route for a non-major addition/improvement no more than 15 ft when no other trigger applies
- **Administrative Design Review**: applies only to the 17 enacted (B)(3) categories; it is not the residual exterior-work route
- **Public hearing**: a Design Review or ADR hearing carries mailed notice, site posting and staking deadlines per §25.05.065(D)-(E). Day counts are in `../city-reference/SKILL.md` §"Design Review / Zone Clearance"
- **Early neighbor communication**: DRB projects require applicant to contact property owners within 300 ft (§25.05.040(C)(1))

---

### Additional Submittal / Process Requirements

These are additional city-specific submittal and process requirements from the Building Plan Check Submittal Requirements handout:

- **Water Quality Management Plan (WQMP)**: deposit and review fee required (amounts: fee tool, `estimate_fees`)
- **Construction Staging Plan and Affidavit**: Required for constrained sites (limited access, narrow streets, or adjacent to public areas)
- **Green Halo Program**: Sign-up required for C&D recycling and waste diversion compliance
- **School Fee Receipt**: LBUSD school fee receipt required if applicable to the project
- **City Business License**: Required for all contractors performing work in Laguna Beach

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

This plugin does not carry the California code checklist for Residential Addition plan sets: the building, residential, structural, fire and life-safety, energy, green-building, plumbing, mechanical, electrical and accessibility requirements. That check comes from CrossBeam.

**When the CrossBeam connector is connected** (the host has tools whose names start with `crossbeam_`):

1. Call `crossbeam_get_review_requirements` with `city: "laguna-beach"` and `permit_type: "residential-addition"`. It returns the review lanes, the required documents and the packaging rules, with citations. Read it beside the City checklists above. Where they differ, tell the user and cite both. Coverage `none` means CrossBeam has no data, not that nothing is required.
2. Ask code questions with `crossbeam_ask`. Send the city (Laguna Beach, CA), the permit type and the project facts you have, and follow up with its `conversation_id`. A code section the answer cites that is not in its citations is unverified.
3. To check a plan set against the code, use a CrossBeam check. For a set drawn with CrossBeam's permit-drawings skill, call `crossbeam_get_skill` with `skill_id: "permit-drawings"` and follow `../../references/plan-sheets.md` section 2; permit-drawings runs the check. For a set drawn by someone else, the user uploads it for a CrossBeam check in the CrossBeam app, because the connector does not upload plans; then read the results with `crossbeam_list_projects`, `crossbeam_get_project_summary` and `crossbeam_get_findings`. A CrossBeam check is paid. Start one only with the user's approval.

CrossBeam cites the current 2025 California Building Standards Code (Title 24, effective 2026-01-01). Use its citations over code sections you remember. Apply the Laguna Beach rules above on top of them.

**When the connector is not connected**, or a tool is missing or needs sign-in:

- Do not check the design against the California codes from memory, and never report a California code item as passing.
- Do the Laguna Beach rules and the City checklists in full, then list California code compliance as **not checked**.
- Say it plainly, once: "This plugin checks the Laguna Beach rules and the City's submittal checklists for Residential Addition permits. It cannot check the plans against the California building codes. For that, connect CrossBeam (crossbeam-permits.com) and run a CrossBeam check before you file."
- Then carry on with intake, the City checklists and filing.

---

## References

Load these on demand. Paths are relative to this file.

- `../../requirements/README.md` — the City submittal checklists, plan-sheet matrix and issuance checklist
- `../plan-set-check/SKILL.md` — checks a plan set against the City checklists
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**Laguna Beach rules**

- `references/city-major-remodel.md` — Laguna Beach — Major Remodel Interpretation

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
