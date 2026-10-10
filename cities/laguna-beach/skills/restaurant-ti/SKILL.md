---
name: restaurant-ti
description: "Restaurant Tenant Improvement permits in Laguna Beach, CA. A restaurant or food-service tenant improvement, with its hood, grease, and health requirements. Always a plan set. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against the Laguna Beach rules and the City submittal checklists, and prepares a portal-ready submission; (B) CITY REVIEWER — checks a submittal against the Laguna Beach rules and produces tight corrections output. California code compliance comes from the CrossBeam connector when it is connected. Use when the user mentions restaurant ti in Laguna Beach."
metadata:
  version: "2.0"
  source: "California Retail Food Code (CRFC) 2025, AB 671, AB 592, CBC Part 2, CMC Part 4, CPC Part 5, CFC Part 9, Energy Code Part 6, Existing Building Code Part 10; LBMC Title 14 (Building), Title 15 (Fire), Title 25 (Zoning); 2025 CBC/CFC/CMC/CPC/CEC; California Retail Food Code (HSC Division 104 Part 7); AB 592; AB 671"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-10-10"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Restaurant Tenant Improvement Permit

Handles restaurant tenant improvement permits in Laguna Beach end-to-end. Scope: A restaurant or food-service tenant improvement, with its hood, grease, and health requirements. Always a plan set.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a restaurant tenant improvement permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Restaurant Tenant Improvement Permit

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

**Skill stack (load in order):**

1. the California Restaurant Tenant Improvement rules, which come from the CrossBeam connector (see "California Code Compliance" below) — CRFC, AB 671, AB 592, Title 24 baseline.
2. a CrossBeam reference that is not included in this plugin — OCHCA prescriptive material rules, sink dimensions, dishmachine, lighting, finish-material approvals. (Orange County Health Care Agency reviews ALL Laguna Beach restaurants; **OCHCA rules apply unchanged**.)
3. **This skill** — Laguna planning entitlements, LBFD fire review, coastal, parking, ROW dining, sprinkler retrofit, construction hours.
4. `../city-reference/SKILL.md` — citywide code cycle, climate, VHFHSZ, CDP background.

**Important: LBFD replaces OCFA.** Laguna Beach operates its own fire department. Do NOT apply OCFA hood/sprinkler/alarm submittal mechanics in the OC overlay's "OCFA" section; load `references/lbfd-fire-prevention.md` instead. OCHCA Environmental Health rules from the OC overlay DO apply.

---

### Critical First Checks

| Check | Laguna Beach rule |
|-------|-------------------|
| **Health review agency** | OCHCA Environmental Health (same as unincorporated OC). Building permit issuance is conditioned on OCHCA plan-approval letter. |
| **Fire review agency** | **LBFD Fire Prevention** (NOT OCFA). Required for all commercial new construction and remodels prior to building permit issuance. Contact: fireprevention@lagunabeachcity.net / 949-497-0352. |
| **Planning route** | Match Ord. 1732's closed lists; exterior work is not a default Design Review trigger. Interior-only work takes Zone Clearance `(B)(2)(d)`. If Design Review is independently triggered for non-residential scope, the Planning Commission is the authority. ADR applies only to its 17 listed categories. A major remodel is Design Review under `(B)(1)(a)`; measure it with `../residential-remodel/references/city-major-remodel-methodology.md` (the City's guide applies it to a "residence or commercial building"). |
| **Coastal Development Permit (Ch. 25.07)** | Virtually all of Laguna is in the Coastal Zone. Sec. 25.07.006 defines "intensification of use" as a change of use that "requires more off-street parking than did the immediately preceding legal use", so test it by required parking under the parcel's governing plan: under Ch. 25.52 (food service 1/100 sf vs. retail 1/250 sf) retail-to-restaurant usually intensifies and needs a CDP; in the Downtown Specific Plan retail and food service share one ratio (3 per 1,000 sf), so a same-size change is not intensification by parking (`references/coastal-development-permit.md`). The CDP is decided by the body that decides the project's other permit (25.07.012(D)). Categories: exempt, de-minimis waiver (Sec. 25.07.009), administrative CDP w/ public-hearing waiver (Sec. 25.07.013), non-appealable CDP, appealable CDP (within ~300 ft of sea / first public road — 10-working-day CCC appeal window before effective date). |
| **Conditional Use Permit** | Set by the **zone chapter's use lists**; Sec. 25.05.030 is only the procedure. Examples: Local Business Professional — all cafes, full-service and take-out restaurants are CUP (25.18.004); C-N — full-service restaurants without alcohol are permitted, with alcohol or take-out are CUP (25.19.002, .006); C-1 — full-service without alcohol or entertainment permitted, with alcohol/entertainment, take-out or drive-in are CUP (25.20.004, .006); SLV — restaurants are listed as CUP uses (25.25.006); CH-M — only incidental to a hotel, CUP (25.21.004); Downtown Specific Plan — Ch. 25.40 use tables and full-service-restaurant special findings. Read the zone from site facts and quote its list. Planning Commission decides; its CUP makes it the Design Review body too (25.05.040(F)(1)(ii)). Parking relief by joint use, shared parking, valet, off-site spaces or the 25.52.006(G) incentive reduction also needs a CUP (Ch. 25.52); Ord. 1732 § 46 moved the incentive CUP from the City Council to the Planning Commission. No citywide late-hour CUP trigger appears in our sources; hours are set by CUP conditions. |
| **Outdoor dining** | Public ROW (sidewalk): the use approval from the zone's use table (Downtown Specific Plan: "Outdoor Dining" is DA, Director administrative approval, in the CBD districts; elsewhere the zone list) + a Revocable Encroachment Permit for the right-of-way (Ch. 11.50; the City application list names it for a sidewalk café; noticed hearing before the design review authority, ADR (B)(3)(a)(viii) when no DRB/PC project rides with it) + Public Works for any street work. A TUP only for a temporary or seasonal program. 3 ft min unobstructed sidewalk; ADA path-of-travel; AB 592 preempts over-restriction but local ROW conditions apply. Private property (patios, parking-lot conversions): use status per the zone list (e.g. C-1 permits outdoor tables for a non-alcohol full-service restaurant operated within a building, 25.20.004; alcohol or take-out seating needs the CUP) + Ord. 1732 route for the physical work (a commercial parking area is Design Review (B)(1)(l), Planning Commission) + CDP + revised parking calc (outdoor seating counts toward GFA). |
| **Parking (Ch. 25.52)** | Citywide food-service ratio: **1 space per 100 sf GFA** (including outdoor seating) OR 1 per 3 seats, whichever is greater. **Downtown Specific Plan area: 3 spaces per 1,000 sf** for non-residential (much more lenient). In-lieu parking certificates only in Council-designated special parking districts (25.52.006(E)); four or more need a parking demand study. Compare prior legal use to proposed restaurant — any parking increase = intensification of use (25.07.006) → CDP (25.07.008(A)(2)(b)), and the added spaces must be provided or relieved (CUP options above). |
| **Sprinkler retrofit** | **LBMC Sec. 14.50.104 (Group A trigger, CBC Sec. 903.6 valuation-based, 50% over 3-year rolling)** applies to restaurant-only buildings. **LBMC Title 15 Sec. 1103.5.4 (scope-based: alteration of 50%+ of building OR work on 50%+ of exterior OR added story)** applies to any Group R component above or attached to the restaurant in a mixed-use building. New restaurants in shell buildings are sprinklered as new under Sec. 903.2. |
| **Construction hours (Sec. 7.25.080)** | **Weekdays only, 7:30 AM – 6:00 PM**. **Saturday, Sunday, and federal holidays all PROHIBITED** — Saturday is a weekend day per §7.25.080(B), no Sat window in Laguna. Downtown summer moratorium Memorial Day – Labor Day. Note on Sheet G-1 General Notes. |
| **Submittal package** | Multi-track. Architectural + Mech (hood/HVAC/grease duct) + Plumbing (sinks/grease interceptor) + Electrical + Fire Sprinkler (deferred) + Fire Alarm (deferred) + Signage (if exterior). Exterior-touching scope adds DR exhibits (elevations, materials board, color samples, lighting cut sheets, awning details). |

---

### Decision Tree Router

#### Step 2 — Determine Discretionary Review Track

For each scope, answer the three entitlement questions in order:

| Question | If YES, load |
|----------|--------------|
| **Q1.** What current §25.05.040 closed-list category matches each interior/exterior component? | `references/planning-design-review-routing.md` — Design Review, Zone Clearance, ADR, or `needs_source`; no exterior-work default |
| **Q2.** Is the parcel in the Coastal Zone (assume YES unless parcel-specific evidence shows otherwise)? | `references/coastal-development-permit.md` — Ch. 25.07 categories, intensification-of-use trigger, CCC appeal window |
| **Q3.** Does the zone list make this restaurant a CUP use (alcohol, entertainment, take-out, drive-in, or all restaurants in some zones), or does parking relief need a CUP? | `references/conditional-use-permit.md` — zone-by-zone CUP lists, Downtown Specific Plan, conditions of approval |

If the TI is interior-only, it still requires Zone Clearance under §25.05.040(B)(2)(d), in addition to the applicable Building, LBFD, and OCHCA tracks.

#### Step 3 — LBFD Fire Prevention (Replaces OCFA)

Always load `references/lbfd-fire-prevention.md` when commercial cooking equipment, sprinklers, or fire alarm work is in scope. Covers:

- Type I hood + grease duct submittal (separate plan set, submitted together as one application)
- Ansul / UL-300 wet chemical suppression
- NFPA 13 sprinkler additions/modifications under LBMC Sec. 15.01 amendments
- Fire alarm tie-in with 24-hour UL central station monitoring (Title 15 amended Sec. 6.16.1)
- FDC location/size — minimum two 2½" inlets, OSHA red, ≤150 ft from public hydrant (LBMC-amended NFPA 13 Sec. 16.12.1)
- Hydrant flow test ≤6 months old required (LBMC Sec. 28.1.3)

#### Step 4 — Outdoor Dining Path

If outdoor dining is in scope, load `references/outdoor-dining-row.md`. Two parallel paths:

- **Public ROW (sidewalk cafe):** use approval per the zone's use table (Downtown Specific Plan: Director administrative approval, "DA") + Revocable Encroachment Permit (Ch. 11.50) for the right-of-way + Public Works for any street work; a TUP only for a temporary or seasonal program. AB 592 (2024) preempts over-restriction; 3 ft min unobstructed sidewalk; ADA path-of-travel; no blocking of entries.
- **Private property:** use status per the zone list (CUP where the zone requires it); Ord. 1732 route for the physical work (Planning Commission if Design Review); CDP; revised parking calc (outdoor seating counts toward GFA).

#### Step 5 — Sprinkler Retrofit

Always check both triggers and apply whichever fires first:

- **LBMC Sec. 14.50.104 (Group A — restaurant proper):** Valuation-based retrofit. When permitted work value exceeds 50% of building value over any 3-year rolling period, a full automatic sprinkler system per CBC Sec. 903.3 is required throughout the Group A fire area. Tracks with CBC Sec. 903.6 framework.
- **LBMC Title 15 Sec. 1103.5.4 (Group R component above):** Scope-based retrofit, independent of valuation. Any one of: (i) alteration of 50%+ of the building, (ii) work on 50%+ of the exterior, (iii) addition of one or more stories. Carve-out: fire-resistant siding only.

For mixed-use buildings (restaurant downstairs, residential above), both triggers can fire on the same project — and the residential prong is scope-based, so even a moderate restaurant TI may push the building past the 50%-of-exterior threshold if combined with façade/storefront work.

Load `references/sprinkler-retrofit-triggers.md` for the analysis worksheet.

#### Step 6 — Parking & Intensification of Use

Load `references/parking-intensification.md`. Compute:

1. Prior legal use parking demand (retail and general office are both 1 space per 250 sf GFA under LBMC 25.52.012).
2. Proposed restaurant parking demand (citywide: 1 per 100 sf GFA incl. outdoor seating, or 1 per 3 seats — whichever greater; DSP: 3 per 1,000 sf non-res).
3. If proposed > prior → "intensification of use" per Sec. 25.07.006 → CDP trigger independent of any other scope (25.07.008(A)(2)(b)), and the added spaces are required (25.52.004).
4. Shortfall? In-lieu parking certificates only inside a Council-designated special parking district (25.52.006(E)); otherwise a CUP for joint use, shared parking, valet, off-site spaces, or the 25.52.006(G) incentive reduction (Planning Commission, Ord. 1732 § 46), or a variance.

#### Step 7 — Construction Hours & Noise

Load `references/construction-hours-noise.md`. Apply Sec. 7.25.080 hours:

- Weekdays (Mon-Fri) only, **7:30 AM – 6:00 PM**
- **Saturday, Sunday, AND federal holidays all PROHIBITED** (no Sat window in Laguna — §7.25.080(B))
- Downtown summer moratorium (Memorial Day – Labor Day) for street-front projects
- CBD1/CBD2 noise zones (Sec. 7.25) add receiver-side limits for outdoor mechanical equipment (hood exhaust, RTUs)

Required note on Sheet G-1.

#### Step 8 — Submittal Package & Sequencing

Load `references/submittal-package.md`. The submittal sequence is parallel-track:

1. **Planning Division** — DR application, CDP application, CUP application (if triggered), outdoor dining use approval (DSP: Director administrative approval) and Revocable Encroachment Permit (if sidewalk dining). Public hearings sequence first when required.
2. **Building Division** — CBC/CMC/CPC/CEC/Title 24 plan check after Planning sign-off (or concurrent at staff discretion).
3. **LBFD Fire Prevention** — Hood/suppression/sprinkler/alarm plan check.
4. **Public Works** — Right-of-way permit for street work (curb, sidewalk, utility connection) tied to ROW dining or street-facing improvements.
5. **OCHCA Environmental Health** — Parallel external submittal. 3 sets of plans + application + plan-check fee to 1241 E Dyer Rd Suite 120, Santa Ana. ~20 working days. plancheck@ochca.com / 714-433-6074. Building permit issuance is conditioned on OCHCA plan-approval letter.

#### Step 9 — Output the Review Result

For each Laguna-specific checklist item, output PASS / FAIL / FLAG / N/A with the LBMC citation. State CRFC and OC overlay findings come from those skills, not this one.

---

### Realistic Timeline

| Scope | Building plan check | Add for DR | Add for CDP | Add for CUP | Total |
|-------|---------------------|------------|-------------|-------------|-------|
| Interior-only, no entitlement | 4-8 weeks | — | — | — | 4-8 weeks |
| Exterior touched (Admin DR only) | 4-8 weeks | 4-6 weeks | 2-4 weeks (admin) | — | 10-18 weeks |
| Exterior + appealable CDP | 4-8 weeks | 6-10 weeks (PC hearing) | 8-12 weeks (incl. CCC appeal window) | — | 18-30 weeks |
| Alcohol / entertainment CUP (zone list) or parking-relief CUP | 4-8 weeks | 6-10 weeks | 8-12 weeks | 12-20 weeks | 30-50 weeks |

Most full-scope restaurant TIs in Laguna realistically run 4-8 months end-to-end. Plan the OCHCA submittal in parallel from day 1 — it is the most common late-stage blocker.

---

### Contacts (Laguna-Specific)

| Item | Detail |
|------|--------|
| Building and Planning Divisions | phones, emails and the counter address: `../city-reference/references/contacts-hours.md` |
| Building Official (the Building Official (CBO)) | (949) 497-0719 |
| Inspections | lbinspectors@lagunabeachcity.net |
| **LBFD Fire Prevention** | fireprevention@lagunabeachcity.net / (949) 497-0352 |
| Public Works (encroachment) | via City Hall |
| Permit Portal | lagunabeachca-energovweb.tylerhost.net/apps/SelfService |
| OCHCA Plan Check (parallel) | plancheck@ochca.com / (714) 433-6074 / 1241 E Dyer Rd Ste 120, Santa Ana |

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

This plugin does not carry the California code checklist for Restaurant Tenant Improvement plan sets: the building, residential, structural, fire and life-safety, energy, green-building, plumbing, mechanical, electrical and accessibility requirements. That check comes from CrossBeam.

**When the CrossBeam connector is connected** (the host has tools whose names start with `crossbeam_`):

1. Call `crossbeam_get_review_requirements` with `city: "laguna-beach"` and `permit_type: "restaurant-ti"`. It returns the review lanes, the required documents and the packaging rules, with citations. Read it beside the City checklists above. Where they differ, tell the user and cite both. Coverage `none` means CrossBeam has no data, not that nothing is required.
2. Ask code questions with `crossbeam_ask`. Send the city (Laguna Beach, CA), the permit type and the project facts you have, and follow up with its `conversation_id`. A code section the answer cites that is not in its citations is unverified.
3. To check a plan set against the code, use a CrossBeam check. For a set drawn with CrossBeam's permit-drawings skill, call `crossbeam_get_skill` with `skill_id: "permit-drawings"` and follow `../../references/plan-sheets.md` section 2; permit-drawings runs the check. For a set drawn by someone else, the user uploads it for a CrossBeam check in the CrossBeam app, because the connector does not upload plans; then read the results with `crossbeam_list_projects`, `crossbeam_get_project_summary` and `crossbeam_get_findings`. A CrossBeam check is paid. Start one only with the user's approval.

CrossBeam cites the current 2025 California Building Standards Code (Title 24, effective 2026-01-01). Use its citations over code sections you remember. Apply the Laguna Beach rules above on top of them.

**When the connector is not connected**, or a tool is missing or needs sign-in:

- Do not check the design against the California codes from memory, and never report a California code item as passing.
- Do the Laguna Beach rules and the City checklists in full, then list California code compliance as **not checked**.
- Say it plainly, once: "This plugin checks the Laguna Beach rules and the City's submittal checklists for Restaurant Tenant Improvement permits. It cannot check the plans against the California building codes. For that, connect CrossBeam (crossbeam-permits.com) and run a CrossBeam check before you file."
- Then carry on with intake, the City checklists and filing.

---

## References

Load these on demand. Paths are relative to this file.

- `../../requirements/README.md` — the City submittal checklists, plan-sheet matrix and issuance checklist
- `../plan-set-check/SKILL.md` — checks a plan set against the City checklists
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**Laguna Beach rules**

- `references/coastal-development-permit.md` — Laguna Beach — Coastal Development Permit for Restaurant TI
- `references/conditional-use-permit.md` — Laguna Beach — Conditional Use Permit for Restaurant TI
- `references/construction-hours-noise.md` — Laguna Beach — Construction Hours & Noise
- `references/lbfd-fire-prevention.md` — Laguna Beach — LBFD Fire Prevention for Restaurant TI
- `references/outdoor-dining-row.md` — Laguna Beach — Outdoor Dining / Sidewalk Cafe
- `references/parking-intensification.md` — Laguna Beach — Parking & Intensification of Use for Restaurant TI
- `references/planning-design-review-routing.md` — Laguna Beach — Current Restaurant TI Planning Route
- `references/sprinkler-retrofit-triggers.md` — Laguna Beach — Sprinkler Retrofit Triggers for Restaurant TI
- `references/submittal-package.md` — Laguna Beach — Restaurant TI Submittal Package & Sequencing

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
