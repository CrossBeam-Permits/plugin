---
name: restaurant-ti
description: "Restaurant Tenant Improvement permits in Laguna Beach, CA. A restaurant or food-service tenant improvement, with its hood, grease, and health requirements. Always a plan set. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions restaurant ti in Laguna Beach."
metadata:
  version: "2.0"
  source: "California Retail Food Code (CRFC) 2025, AB 671, AB 592, CBC Part 2, CMC Part 4, CPC Part 5, CFC Part 9, Energy Code Part 6, Existing Building Code Part 10; LBMC Title 14 (Building), Title 15 (Fire), Title 25 (Zoning); 2025 CBC/CFC/CMC/CPC/CEC; California Retail Food Code (HSC Division 104 Part 7); AB 592; AB 671"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-07-22"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Restaurant Tenant Improvement Permit

Handles restaurant tenant improvement permits in Laguna Beach end-to-end. Scope: A restaurant or food-service tenant improvement, with its hood, grease, and health requirements. Always a plan set.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a restaurant tenant improvement permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Restaurant Tenant Improvement Permit

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

**Skill stack (load in order):**

1. `references/california-baseline.md` — CRFC, AB 671, AB 592, Title 24 baseline.
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
| **Planning route** | Match Ord. 1732's closed lists; exterior work is not a default Design Review trigger. Interior-only work takes Zone Clearance `(B)(2)(d)`. If Design Review is independently triggered for non-residential scope, the Planning Commission is the authority. ADR applies only to its 17 listed categories. |
| **Coastal Development Permit (Ch. 25.07)** | Presumptively required. Virtually all of Laguna is in the Coastal Zone. Sec. 25.07.006 defines "development" to include any change in intensity of use; retail-to-restaurant conversion is an "intensification of use" and trips CDP independently of any building scope. Categories: exempt, de-minimis waiver (Sec. 25.07.009), administrative CDP w/ public-hearing waiver (Sec. 25.07.013), non-appealable CDP, appealable CDP (within ~300 ft of sea / first public road — 10-working-day CCC appeal window before effective date). |
| **Conditional Use Permit (Sec. 25.05.030)** | REQUIRED — even in the Downtown Specific Plan where most uses became by-right in the 2022 CCC-certified update — for restaurants serving alcohol, restaurants with entertainment, late-hour operation, drive-thru/drive-up, outdoor dining beyond temporary, and any "intensification of use" (use change that requires more parking than the prior legal use). Planning-Commission-issued. |
| **Outdoor dining** | Public ROW (sidewalk) = Public Works encroachment permit + Temporary Use Permit (Sec. 25.05.035); 3 ft min unobstructed sidewalk; ADA path-of-travel; AB 592 preempts over-restriction but local ROW conditions apply. Private property (patios, parking-lot conversions) = AUP or CUP + DRB if visible + CDP + revised parking calc (outdoor seating counts toward GFA). |
| **Parking (Ch. 25.52)** | Citywide food-service ratio: **1 space per 100 sf GFA** (including outdoor seating) OR 1 per 3 seats, whichever is greater. **Downtown Specific Plan area: 3 spaces per 1,000 sf** for non-residential (much more lenient). In-lieu fee program available. Compare prior legal use to proposed restaurant — any parking increase = intensification of use → CUP + CDP. |
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
| **Q3.** Does the operation include alcohol, entertainment, late hours, drive-thru, outdoor dining beyond temporary, or any use intensification? | `references/conditional-use-permit.md` — Sec. 25.05.030 triggers, Downtown Specific Plan CUP carve-out, conditions of approval |

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

- **Public ROW (sidewalk cafe):** Public Works encroachment permit + Temporary Use Permit (Sec. 25.05.035). AB 592 (2024) preempts over-restriction; 3 ft min unobstructed sidewalk; ADA path-of-travel; no blocking of entries.
- **Private property:** Administrative Use Permit or CUP depending on zone + intensity; DRB if visible; CDP; revised parking calc (outdoor seating counts toward GFA).

#### Step 5 — Sprinkler Retrofit

Always check both triggers and apply whichever fires first:

- **LBMC Sec. 14.50.104 (Group A — restaurant proper):** Valuation-based retrofit. When permitted work value exceeds 50% of building value over any 3-year rolling period, a full automatic sprinkler system per CBC Sec. 903.3 is required throughout the Group A fire area. Tracks with CBC Sec. 903.6 framework.
- **LBMC Title 15 Sec. 1103.5.4 (Group R component above):** Scope-based retrofit, independent of valuation. Any one of: (i) alteration of 50%+ of the building, (ii) work on 50%+ of the exterior, (iii) addition of one or more stories. Carve-out: fire-resistant siding only.

For mixed-use buildings (restaurant downstairs, residential above), both triggers can fire on the same project — and the residential prong is scope-based, so even a moderate restaurant TI may push the building past the 50%-of-exterior threshold if combined with façade/storefront work.

Load `references/sprinkler-retrofit-triggers.md` for the analysis worksheet.

#### Step 6 — Parking & Intensification of Use

Load `references/parking-intensification.md`. Compute:

1. Prior legal use parking demand (often retail @ 1 space per 250 sf or office @ 1 per 300 sf).
2. Proposed restaurant parking demand (citywide: 1 per 100 sf GFA incl. outdoor seating, or 1 per 3 seats — whichever greater; DSP: 3 per 1,000 sf non-res).
3. If proposed > prior → "intensification of use" per Sec. 25.07.006 → CDP trigger + CUP trigger independent of any other scope.
4. Shortfall? Use in-lieu fee program (citywide) or parking demand study with planning-director discretion.

#### Step 7 — Construction Hours & Noise

Load `references/construction-hours-noise.md`. Apply Sec. 7.25.080 hours:

- Weekdays (Mon-Fri) only, **7:30 AM – 6:00 PM**
- **Saturday, Sunday, AND federal holidays all PROHIBITED** (no Sat window in Laguna — §7.25.080(B))
- Downtown summer moratorium (Memorial Day – Labor Day) for street-front projects
- CBD1/CBD2 noise zones (Sec. 7.25) add receiver-side limits for outdoor mechanical equipment (hood exhaust, RTUs)

Required note on Sheet G-1.

#### Step 8 — Submittal Package & Sequencing

Load `references/submittal-package.md`. The submittal sequence is parallel-track:

1. **Planning Division** — DR application, CDP application, CUP application (if triggered), TUP application (if outdoor dining). Public hearings sequence first when required.
2. **Building Division** — CBC/CMC/CPC/CEC/Title 24 plan check after Planning sign-off (or concurrent at staff discretion).
3. **LBFD Fire Prevention** — Hood/suppression/sprinkler/alarm plan check.
4. **Public Works** — Encroachment permit for ROW dining or street-facing improvements.
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
| Alcohol / late hours / intensification | 4-8 weeks | 6-10 weeks | 8-12 weeks | 12-20 weeks | 30-50 weeks |

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

## California Checklist

The California checklist for this permit is in `references/california-baseline.md`. Walk its decision tree and every checklist row after the Laguna Beach rules above. For each row, decide whether it is checked at plan check or verified by the inspector in the field. Do not list inspection items as corrections.

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/ab671-pathways.md` — AB 671 — Restaurant TI Fast-Track Pathways
- `references/building-occupancy-egress.md` — Building Occupancy, Egress, and Accessibility
- `references/energy-efficiency.md` — Energy Efficiency — Lighting Power Density, HVAC, Alterations
- `references/existing-building.md` — Existing Building Code — Alterations and Change of Occupancy
- `references/fire-suppression-assembly.md` — Fire — Hood Suppression and Assembly Fire Requirements
- `references/health-construction.md` — Health Construction — Floors, Walls, Ceilings, Lighting, Ventilation, Enclosure
- `references/health-equipment.md` — Health Equipment — Sinks, Equipment Installation, Spacing, Certification
- `references/health-food-safety.md` — Health Food Safety — Layout Requirements for Food Handling and Storage
- `references/health-plumbing-sanitation.md` — Health Plumbing & Sanitation — Handwashing, Water, Waste, Restrooms, Janitorial
- `references/mechanical-ventilation.md` — Mechanical Ventilation — Type I/II Hoods, Exhaust, Makeup Air, Ducts
- `references/outdoor-dining.md` — AB 592 — Outdoor Dining and Open-Front Restaurant Operations
- `references/plumbing-grease.md` — Plumbing — Grease Interceptors, Fixture Counts, Restroom Requirements

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
