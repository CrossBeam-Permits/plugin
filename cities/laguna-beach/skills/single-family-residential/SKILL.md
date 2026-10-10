---
name: single-family-residential
description: "New Single-Family Home permits in Laguna Beach, CA. A new single-family dwelling, or a rebuild that replaces one. Always a plan set. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against the Laguna Beach rules and the City submittal checklists, and prepares a portal-ready submission; (B) CITY REVIEWER — checks a submittal against the Laguna Beach rules and produces tight corrections output. California code compliance comes from the CrossBeam connector when it is connected. Use when the user mentions single family residential in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Standards Code (Title 24, Parts 2, 2.5, 3, 4, 5, 6, 11); LBMC Title 14, Title 15, Title 25; Building Plan Check Submittal Requirements; Bluff Edge Determinations; Zoning Plan-Check Project Submittal Requirements table"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-08-10"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — New Single-Family Home Permit

Handles new single-family home permits in Laguna Beach end-to-end. Scope: A new single-family dwelling, or a rebuild that replaces one. Always a plan set.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a new single-family home permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach New Single-Family Home Permit

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

Use this skill for new one-family dwellings, replacement dwellings, and plan-review routing where a Laguna Beach remodel may become new construction or a major remodel. If the project is an alteration to an existing dwelling, also load `../residential-remodel/SKILL.md` to run the major-remodel and existing-building sprinkler tests.

---

### Critical First Checks

| Check | Laguna Beach rule |
|-------|-------------------|
| **New SFD routing** | Default new-building route is Design Review under current §25.05.040(B)(1)(b). A qualifying new primary dwelling may instead elect Chapter 25.13 and take Zone Clearance under §25.05.040(B)(2)(z), but only when both the Chapter 25.13 development gate and the adopted 2026 objective-design gate pass. |
| **Chapter 25.13** | Optional, not automatic: one story/≤15 ft, primary ≤1,500 sf, possible second primary ≤800 sf, garage ≤400 sf/two spaces, +20% setbacks, Table A FAR, landscape/light/roof-deck limits, all 13 General Design Standards, and every standard in one applicant-selected Form Group. Major remodels are ineligible; CDP may remain required. |
| **Coastal zone** | Most parcels are coastal. New SFD is "development" under Ch. 25.07 and is not the routine SFR-improvement exemption. CDP determination is required before building permit issuance. |
| **Bluff/oceanfront** | No building/addition/structure/improvement may be beyond the applicable stringline or closer than 25 ft to oceanfront bluff top; more restrictive rule controls. |
| **R-1 height** | Slope-based max height: 25 ft at 0-15% slope, then 26/27/28/29 ft at 16/17/18/19%, and 30 ft at 20%+. Additional front/rear-yard height setbacks can reduce the envelope. |
| **R-1 site coverage** | Max 44% for lots <=4,000 sf; 35% for lots >=8,000 sf; interpolation formula for 4,000-8,000 sf. Oceanfront lots use the reduced "A" area landward of the more restrictive oceanfront setback/bluff line. |
| **Parking** | 2 covered spaces for each SFD; add 1 uncovered space at 3,600+ sf gross floor area unless approved relief/alternative is supported by a parking demand study. |
| **Access/frontage** | Chapter 25.53 access from usable vehicular ROW to required parking; new development may require curbs, gutters, sidewalks, paving, and site/right-of-way improvement plans as determined by the city engineer. |
| **Sprinklers** | All new one- and two-family dwellings and attached garages must be sprinklered. A garage within 10 ft counts as attached. |
| **WUI/VHFHSZ** | Treat WUI/VHFHSZ as active unless parcel-specific evidence shows otherwise. Local amendments require Class A roof, ignition-resistant/noncombustible wall covering options, vinyl-window reinforcing, glass skylights, 144 sq in max vents, defensible space/fuel-modification review. |
| **Submittal package** | New SFRs use the full Building Plan Check package: 4 plan sets, record survey, building data/coverage sheets, structural/geotech/energy/CALGreen/WQMP/stormwater, Fire site access when required, and deferred sprinkler plans. |
| **Three Arch Bay (Ch. 25.44)** | If parcel is inside TAB: apply the 5 ft side / 25 ft rear / 4-parking standards, §25.44.050(M)'s 3:12 roof pitch/no-roof-deck rule (2.5:12 view-corridor exception), the two current §25.44.060 findings when Design Review applies, and qualified TABA + TABCSD sequencing. See `references/three-arch-bay.md`. |
| **Heritage (Ch. 25.45)** | If existing structure on lot is 50+ years old or property is Historic Register-listed: Heritage Committee review precedes demolition; DR authority may extend demolition waiting period up to 180 days. See `references/heritage-historic-committee.md`. |
| **Floodplain (Ch. 25.38)** | If parcel is in a FEMA SFHA (V-zone, A-zone): separate Floodplain Development Permit per §25.38.042; V-zone needs open-pile foundation per §25.38.057 + BFE adjusted for 75-yr SLR. Ch. 25.38 (Title 25, Zoning) is the operative chapter — Ch. 14.78 does NOT exist. See `references/floodplain.md`. |

---

### Decision Tree

#### Step 2 - Classify Planning Route

Ask whether the applicant elects the optional Chapter 25.13 pathway.

- **No election or Chapter 25.13 ineligible:** a new building requires Design Review under current §25.05.040(B)(1)(b). For one-family residential projects, apply the approval-authority rules in §25.05.040(F).
- **Chapter 25.13 elected:** run `references/objective-primary-dwelling-ch25-13.md`, then load `references/objective-design-standards-2026.md` and exactly one applicant-selected Form Group reference. Return Zone Clearance under §25.05.040(B)(2)(z) and §25.05.045 only when both the development and design gates pass.
- **Major remodel:** cannot use Chapter 25.13; route to Design Review under §25.05.040(B)(1)(a), and apply §25.56.011's new-building consequences.

Required planning outputs:

- Route: Design Review, Zone Clearance under Chapter 25.13, or `indeterminate`.
- Matched closed-list category and Chapter 25.13 election/eligibility.
- Objective-design Form Group: A, B, C, D, or `unknown`; never infer it from the parcel or neighborhood.
- Separate findings for all 13 General Design Standards and every applicable standard in the selected group, with sheet evidence.
- If a standard fails, preserve all three applicant choices: revise/resubmit, seek discretionary DRB/Planning Commission review, or withdraw.
- Staking when a Design Review hearing is required; poles/ribbons must represent the full proposed structure, including decks and eaves, and be in place/certified 21 calendar days before the first hearing.
- Fire Safety Standards Review: required before Design Review action for new construction and major remodels; Fire Department or Building Division, as applicable.
- Current Design Review criteria when that route applies: Access, Design Articulation, Environmental Context, General Plan Compliance, Historic Preservation, Landscaping, Lighting and Glare, Neighborhood Compatibility, Pedestrian Orientation, Privacy, and View Equity.

Use `references/planning-coastal-routing.md` and the shared `../residential-remodel/references/city-design-review-tiers.md`.

**Three Arch Bay parcels:** Load `references/three-arch-bay.md` and run the City/private sequencing check at intake. Section 25.44.060 describes TABA review and a comment letter only **to the extent permitted by law**; do not turn that qualifier into an unconditional City entitlement prerequisite. Separate owner consent is still required for work on TABA- or TABCSD-owned property.

**50+ year existing structure:** If a structure 50 years or older is on the lot (or the lot is on the Historic Register), Heritage Committee review precedes demolition. The design review authority may extend the demolition waiting period up to 180 days for relocation. Load `references/heritage-historic-committee.md`.

#### Step 3 - Determine Coastal / Bluff / Hillside Overlays

For coastal-zone parcels, new SFD construction is development under Ch. 25.07. Do not treat it as the routine "improvements to single-family dwellings" exemption because there is no existing SFD improvement scope; it is new construction.

For oceanfront/bluff parcels:

- Apply the 25 ft bluff-top setback and stringline rule.
- Apply the 10 ft bluff floor for decks, patios, balconies, and similar projections.
- Recalculate site coverage using the reduced oceanfront lot area under Section 25.50.020.
- Require the bluff-edge/geologic report stack when the city handout applies.

Use `../residential-remodel/references/city-cdp-coastal-zone.md`, `../residential-remodel/references/city-bluff-overlay.md`, and a CrossBeam reference that is not included in this plugin.

**Floodplain check (Ch. 25.38):** Independently, check the parcel against the FEMA FIRM panel. If in an SFHA (V-zone or A-zone), a separate Floodplain Development Permit (§25.38.042) is required and V-zone projects need open-pile foundations (§25.38.057) with BFE adjusted for 75-yr SLR. Ch. 25.38 (Title 25, Zoning) is the operative floodplain chapter — Ch. 14.78 does NOT exist. Load `references/floodplain.md`.

#### Step 4 - Apply R-1 Zoning Envelope

Use `references/zoning-r1-development-standards.md`.

Minimum core checks:

- Lot area, width, depth, and one dwelling per lot.
- Slope-based height plus any more restrictive front/rear-yard height setback.
- 20 ft front and rear yards, side yards at 10% of average lot width with the stated minimums.
- Site coverage and landscaped open-space calculations.
- Residential compatibility with immediate neighborhood scale, mass, and height.
- Special height standards in Section 25.10.010 if the parcel is in a listed area.

If the parcel is not R-1, do not force R-1 numbers. Identify the actual zone and require the applicable district standards before issuing a zoning finding. In particular, for **Three Arch Bay (Ch. 25.44)** parcels, use the TAB-specific standards (5 ft side yard, 25 ft rear yard, 4 parking spaces, sliding-scale coverage, and §25.44.050(M) roof rules) from `references/three-arch-bay.md`.

#### Step 5 - Apply Parking and Access

Use `references/parking-access-standards.md`.

Minimum parking finding:

- Under 3,600 sf GFA: 2 covered spaces.
- 3,600+ sf GFA: 2 covered spaces plus 1 uncovered space unless an approved parking demand study supports an in-lieu fee, reduction, or alternative.
- Tandem parking and additional covered parking require the Section 25.52.012(G) design-review findings.
- Site plan must dimension parking spaces, access, aisles, circulation, and adjacent on-street parking.

Access finding:

- Confirm usable vehicular right-of-way access to required parking.
- Require site/right-of-way improvement plan when triggered.
- Route narrow, steep, private, unimproved, or fire-access-constrained streets to the city engineer and LBFD.

#### Step 6 - Apply Local Fire, Sprinkler, and WUI Amendments

Use `references/fire-wui-local-amendments.md`.

For every new SFD:

- Require automatic residential fire sprinkler system in the dwelling and attached garage. A garage within 10 ft counts as attached.
- Plans must note "FIRE SPRINKLERS REQUIRED" when applicable.
- NFPA 13D plans may be deferred, but must comply with Laguna's local alarm/coverage amendments.
- Apply WUI/VHFHSZ exterior-material checks unless parcel-specific evidence shows WUI/VHFHSZ is not active.
- For fuel-modification-designation areas, final fuel modification plans must be approved by the fire code official before building permit issuance. Apply the LBFD Zone A / B / C / D framework (typical total ~170 ft from each combustible structure; Zone A 0-20 ft non-combustible setback, Zone B ~30 ft irrigated, Zone C ~50 ft native thinning, Zone D ~70 ft native cut). Off-site fuel-mod across property lines needs a recorded easement or HOA-maintenance covenant. See `references/fire-wui-local-amendments.md`.
- When an objective design standard conflicts with the fire code in the VHFHSZ, the more restrictive standard governs. Zone 0 areas are exempt from the objective standards' Chapter 2 landscaping rules.

#### Step 7 - Verify Building Plan Check Submittal

Use `references/submittal-requirements.md`.

For a new SFR, require:

- 4 complete 24 in x 36 in plan sets.
- Record of survey for new construction.
- Cover sheet with building data, lot area, floor area, occupancy, construction type, coverage, codes, and sprinkler note.
- Site/plot plan with setbacks, lot dimensions, all structures, distance to property lines and bluff top if applicable, easements, and north arrow.
- Architectural, structural, MEP, energy, CALGreen, stormwater/WQMP, grading/drainage, erosion-control, and construction-staging documents as applicable.
- Geotech/soils report and peer review deposit when required.
- Hydrology calculations and WQMP when required.
- Deferred 2-copy residential sprinkler submittal when sprinklers are required.
- For an elected Chapter 25.13 path, the completed Chapter 2 checklist plus exactly one selected Chapter 3 Form Group checklist, with the corresponding plan sheet identified for each standard. Until City staff confirms the intake consequence, omission is a nonblocking staff-verification item under the Planning intake policy.

---

### Output Format

Every Laguna Beach new SFR review should include these city findings:

```markdown
## Laguna Beach City Overlay - New SFR
**Planning route:** Design Review | Chapter 25.13 Zone Clearance | indeterminate
**Chapter 25.13 development gate:** elected and pass | not elected | fail | unknown
**Objective-design Form Group:** A | B | C | D | unknown
**Objective-design conformance:** PASS | FAIL | INDETERMINATE | N/A
**Objective-design checklist:** present | missing—staff verification | N/A
**Coastal/CDP:** Required | Exempt | Needs Planning determination
**Bluff/oceanfront:** PASS | FAIL | FLAG | N/A
**R-1 zoning:** PASS | FAIL | FLAG (height, setbacks, coverage, landscaped open space)
**Three Arch Bay (Ch. 25.44):** PASS | FAIL | FLAG | N/A
**Parking/access:** PASS | FAIL | FLAG
**Sprinklers/LBFD:** PASS | FAIL | FLAG
**WUI/fuel modification (Zones A-D):** PASS | FAIL | FLAG | N/A
**Heritage/historic (Ch. 25.45):** PASS | FAIL | FLAG | N/A
**Floodplain (Ch. 25.38):** PASS | FAIL | FLAG | N/A
**Submittal completeness:** PASS | FAIL | FLAG
```

Return citations for every FAIL or FLAG. Do not cite state code for city zoning numbers, and do not use Laguna's existing-building retrofit logic as a substitute for the new-construction sprinkler requirement.

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

This plugin does not carry the California code checklist for New Single-Family Home plan sets: the building, residential, structural, fire and life-safety, energy, green-building, plumbing, mechanical, electrical and accessibility requirements. That check comes from CrossBeam.

**When the CrossBeam connector is connected** (the host has tools whose names start with `crossbeam_`):

1. Call `crossbeam_get_review_requirements` with `city: "laguna-beach"` and `permit_type: "single-family-residential"`. It returns the review lanes, the required documents and the packaging rules, with citations. Read it beside the City checklists above. Where they differ, tell the user and cite both. Coverage `none` means CrossBeam has no data, not that nothing is required.
2. Ask code questions with `crossbeam_ask`. Send the city (Laguna Beach, CA), the permit type and the project facts you have, and follow up with its `conversation_id`. A code section the answer cites that is not in its citations is unverified.
3. To check a plan set against the code, use a CrossBeam check. For a set drawn with CrossBeam's permit-drawings skill, call `crossbeam_get_skill` with `skill_id: "permit-drawings"` and follow `../../references/plan-sheets.md` section 2; permit-drawings runs the check. For a set drawn by someone else, the user uploads it for a CrossBeam check in the CrossBeam app, because the connector does not upload plans; then read the results with `crossbeam_list_projects`, `crossbeam_get_project_summary` and `crossbeam_get_findings`. A CrossBeam check is paid. Start one only with the user's approval.

CrossBeam cites the current 2025 California Building Standards Code (Title 24, effective 2026-01-01). Use its citations over code sections you remember. Apply the Laguna Beach rules above on top of them.

**When the connector is not connected**, or a tool is missing or needs sign-in:

- Do not check the design against the California codes from memory, and never report a California code item as passing.
- Do the Laguna Beach rules and the City checklists in full, then list California code compliance as **not checked**.
- Say it plainly, once: "This plugin checks the Laguna Beach rules and the City's submittal checklists for New Single-Family Home permits. It cannot check the plans against the California building codes. For that, connect CrossBeam (crossbeam-permits.com) and run a CrossBeam check before you file."
- Then carry on with intake, the City checklists and filing.

---

## References

Load these on demand. Paths are relative to this file.

- `../../requirements/README.md` — the City submittal checklists, plan-sheet matrix and issuance checklist
- `../plan-set-check/SKILL.md` — checks a plan set against the City checklists
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**Laguna Beach rules**

- `references/fire-wui-local-amendments.md` — Laguna Beach - Fire, Sprinkler, WUI, and Fuel-Modification Amendments for New SFR
- `references/floodplain.md` — Laguna Beach - Floodplain Overlay (LBMC Ch. 25.38)
- `references/heritage-historic-committee.md` — Laguna Beach - Heritage Committee Review (50+ Year Structures)
- `references/objective-design-form-group-a-2026.md` — Laguna Beach Objective Design Standards — Form Group A
- `references/objective-design-form-group-b-2026.md` — Laguna Beach Objective Design Standards — Form Group B
- `references/objective-design-form-group-c-2026.md` — Laguna Beach Objective Design Standards — Form Group C
- `references/objective-design-form-group-d-2026.md` — Laguna Beach Objective Design Standards — Form Group D
- `references/objective-design-standards-2026.md` — Laguna Beach - 2026 Objective Design Standards pathway
- `references/objective-primary-dwelling-ch25-13.md` — Laguna Beach — Optional Chapter 25.13 Primary-Dwelling Path
- `references/parking-access-standards.md` — Laguna Beach - SFR Parking and Access Standards
- `references/planning-coastal-routing.md` — Laguna Beach - Planning, Design Review, Coastal, and Bluff Routing for New SFR
- `references/submittal-requirements.md` — Laguna Beach - New SFR Submittal Requirements
- `references/three-arch-bay.md` — Laguna Beach - Three Arch Bay Overlay Sequencing (Ch. 25.44)
- `references/zoning-r1-development-standards.md` — Laguna Beach - R-1 Development Standards for New SFR

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
