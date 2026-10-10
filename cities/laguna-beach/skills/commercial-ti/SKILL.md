---
name: commercial-ti
description: "Commercial Tenant Improvement permits in Laguna Beach, CA. Tenant improvement in a commercial or mixed-use space, including outdoor dining build-outs. Always a plan set in Laguna. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against the Laguna Beach rules and the City submittal checklists, and prepares a portal-ready submission; (B) CITY REVIEWER — checks a submittal against the Laguna Beach rules and produces tight corrections output. California code compliance comes from the CrossBeam connector when it is connected. Use when the user mentions commercial ti in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Part 2), California Existing Building Code (Part 10), California Fire Code (Part 9), California Mechanical Code (Part 4), California Electrical Code (Part 3), California Energy Code (Part 6 — §141.0), California Green Building Standards Code / CALGreen (Part 11 — Ch.3, Ch.5), ADA Title III (28 CFR 36.403); LBMC Title 14 (Building Code amendments), Title 15 (Fire Code amendments), Title 25 (Zoning / Coastal / Specific Plans / Heritage); 2025 CBC/CFC/CWUIC effective 2026-01-01; Ord. 1725/1726"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-07-22"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Commercial Tenant Improvement Permit

Handles commercial tenant improvement permits in Laguna Beach end-to-end. Scope: Tenant improvement in a commercial or mixed-use space, including outdoor dining build-outs. Always a plan set in Laguna.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a commercial tenant improvement permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Commercial Tenant Improvement Permit

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

Use this skill for any non-residential tenant improvement, change of occupancy, or commercial alteration in the City of Laguna Beach. This is a **COMPLEX** permit type — full plan review with multi-department routing. Exterior scope no longer automatically adds Design Review; classify it under Ord. 1732's closed lists while screening CDP/CUP independently.

---

### Critical First Checks

| Check | Laguna Beach rule |
|-------|-------------------|
| **Planning route** | Match Ord. 1732's closed lists. Design Review, if triggered for non-residential development, routes to Planning Commission under §25.05.040(F); Zone Clearance and ADR use their respective authorities. Exterior work is not a default trigger. |
| **Interior-only work** | Interior modification with no exterior modification takes Zone Clearance under current §25.05.040(B)(2)(d). Historic work separately routes as major Design Review `(B)(1)(d)` or qualifying minor ADR `(B)(3)(a)(iv)`. |
| **Coastal Development Permit** | Required for nearly all commercial TI within the Coastal Zone (~95% of city) under Ch. 25.07 — **change in intensity of use** is the principal commercial trigger (retail→restaurant, low→high occupancy, parking-deficient conversions). De minimis waiver / Administrative CDP / hearing CDP tiers apply. Appealable to CCC within 10 working days if within 300 ft of beach/MHW or seaward face of coastal bluff. |
| **Sprinkler retrofit (commercial)** | **LBMC §14.50.104 (amending CBC §903.6)** — valuation-based, 50% of pre-work valuation cumulative over a rolling 3-year window AND the completed building would be required to be sprinklered under Laguna's tightened §903.2 thresholds. **This is DISTINCT from Title 15 §1103.5.4 (Group R only).** Use §14.50.104 for all commercial occupancies. |
| **Sprinkler thresholds (new state)** | Laguna tightens CBC §903.2 for Group A, B, E, F-1, M, S-1, S-2 to "**>2 stories OR >5,000 sf**"; Group M with upholstered furniture display sprinklered regardless of size; Group A occupant-load thresholds (100 / 300) unchanged. |
| **WUI / VHFHSZ exterior** | LBMC Ch. 14.70 applies to ANY commercial exterior work in VHFHSZ. Class A roof citywide regardless of VHFHSZ status. Noncombustible/ignition-resistant walls, vinyl-window welded corners, glass-only skylights, 144-sq-in vent openings, defensible space, fuel modification. |
| **Heritage Committee** | Properties 50+ years old or on the 1980-81 inventory route through Heritage Committee (Ch. 25.45). Interior alterations to historic structures are NOT exempt from design review. |
| **LBFD (not OCFA)** | Laguna runs its own municipal fire department. Routing, forms, and contact channel are LBFD-specific. LBFD review is **mandatory and concurrent** for all commercial TIs at both entitlement and building-plan-check phases. **Current §25.05.040(C)(4) requires Fire Department or Building Division review, as applicable, before Design Review action on new construction and major remodels.** The former 50%-alteration Fire-Department-only trigger is not current. |
| **Construction hours** | **Weekdays only, 7:30 AM – 6:00 PM** (§7.25.080(A)). **Saturday, Sunday, federal holidays all PROHIBITED** (§7.25.080(B) — no Sat window in Laguna). Materially stricter than Costa Mesa / OC norm. |
| **Submittal sequence** | Planning (zoning) → Public Works → Building Division plan check. Building does not accept submittals without Planning and Public Works sign-offs. |
| **Sheet sets** | 3 sets 24"×36" (arch / structural / MEP / energy / green) + 2 sets supporting (geotech / structural calcs / energy calcs). |
| **OTC eligibility** | Commercial **signs** (and simple sign change-outs) are OTC-eligible. Full commercial TIs are not OTC. |

---

### Decision Tree Router

#### STEP 2 — Classify the TI by Scope

| Scope archetype | DR route | CDP route | LBFD route | Heritage |
|-----------------|----------|-----------|------------|----------|
| Interior-only, no exterior, no occupancy change, no historic action | Zone Clearance (§25.05.040(B)(2)(d)) | Likely exempt unless intensity-of-use change | Building-plan-check review | Screen property/status |
| Interior + storefront / signage / awning / lighting / paint / roof equipment | Match current closed lists; `needs_source` if no category matches | Determine independently | Entitlement + plan-check review as applicable | Required if historic action |
| Change of occupancy (e.g., retail B → restaurant A-2) | Planning Commission DR | Required — intensity-of-use trigger | Entitlement + plan-check review | Required if 50+ yr / inventory |
| Major remodel | Planning Commission DR if a (B)(1) category matches (LBFD/Building concurrent review under current §25.05.040(C)(4)) | Required | Entitlement + plan-check review | Required if 50+ yr / inventory |
| Demolition + commercial rebuild | Planning Commission DR | Required; appealable analysis if within 300 ft beach/MHW/bluff | Entitlement + plan-check review | Required if 50+ yr / inventory |
| Sign-only (within approved sign program) | Administrative (Director) | Typically exempt | Skip unless illuminated > thresholds | Skip |

Then load:

- `references/design-review.md` — Planning Commission DR mechanics, notice, hearings, ADR, sign programs.
- `references/coastal-development-permit.md` — CDP tiers, exemptions, intensity-of-use, appealable area.
- `references/sprinkler-retrofit-commercial.md` — §14.50.104 valuation math + §903.2 tightened thresholds + NFPA 13 amendments.
- `references/wui-commercial.md` — WUI exterior, Class A roof, noncombustible walls, vinyl windows, skylights, vents.
- `references/heritage.md` — Heritage Committee, 50-year inventory, historic interior alterations.
- `references/specific-plans.md` — Downtown Specific Plan, Arch Beach Heights, Three Arch Bay, North Coast Highway corridor.
- `references/submittal-package.md` — sheet sets, applications, supporting docs, department sequence.

#### STEP 3 — Apply State Floor + City Overrides

For each loaded state checklist item, run the state rule first. Then apply Laguna overrides:

- **Sprinkler threshold tightening** (§14.50.104 amending §903.2) overrides state §903.2 trigger areas for A/B/E/F-1/M/S-1/S-2.
- **Sprinkler retrofit** (§14.50.104(2)) — independent trigger when work ≥50% of pre-work valuation (3-year rolling) AND completed building would be required to be sprinklered.
- **Sprinkler retrofit additional triggers** (§14.50.104(3) and (4)) — any addition to an already-sprinklered building; any addition ≥33% of existing area and >1,000 sf within 2 years.
- **Atrium sprinklers** (§14.50.052) — required throughout atrium-containing buildings.
- **High-rise** (§14.50.044) — triggered at >55 ft above lowest fire-department-access level for Group I-2 and high-rise occupancies (lower trigger than state).
- **Class A roof** (§14.50.120) — required citywide for any new roofing / reroofing on any building.
- **Standpipes** (§14.50.106) — Class I standpipe hose connections per local amendment.
- **Duct smoke detectors** (§14.50.107) — local §907.3.1 amendment.
- **Alternative extinguishing systems** (§14.50.105) — monitored by building fire-alarm/monitoring system per NFPA 72.
- **Adjoining property protection** (§14.50.132) — 30-day excavation notice; retention systems; protection of adjacent property during demo/construction.
- **Spec / shell buildings** (§15.01.070 amending NFPA 13 §9.4.3.1) — quick-response sprinklers required.
- **FDC** (§15.01.070 amending NFPA 13) — minimum two 2½" inlets (four if ≥500 gpm or standpipe), painted OSHA red, ≤150 ft from public hydrant, on street-address side.
- **Hydrant flow test** (§15.01.070 amending NFPA 13 §28.1.3) — ≤6 months old at working-plan submittal.
- **Fire alarm — Group A ≥100 occupant load** (§15.01.035 amending CFC §907.2.1) — manual fire alarm w/ occupant notification.
- **HMMP / HMIS** (§15.01.050) — required at fire-code-official discretion; dry cleaners, photo labs, salons, bulk-CO2 restaurants routinely tripped.
- **Permit exemptions** (§14.50.022 amending CBC §105.2) — painting, papering, tiling, carpeting, cabinets, counter tops, similar finish work exempt; non-fixed movable fixtures/cases/racks/counters/partitions ≤5'9" exempt.
- **Construction hours** — Mon–Fri 7–6, Sat 8–5, Sun/holiday prohibited.

#### STEP 4 — Output the Review Result

For each loaded checklist item, output **PASS / FAIL / FLAG / N/A** with citation. City-specific items use the **LB-CTI-#** numbering below.

---

### Quick-Reference Thresholds

#### Sprinkler Triggers (Laguna-Tightened §903.2)

| Occupancy | State CBC §903.2 trigger | Laguna §14.50.104 trigger |
|-----------|--------------------------|---------------------------|
| Group A | Fire area >12,000 sf OR occupant load ≥300 OR not on level of exit discharge OR >5,000 sf for A-1/A-2/A-3/A-4 | >2 stories OR >5,000 sf; occupant-load (100 multi-theater / 300 single) thresholds unchanged |
| Group B | Fire area >12,000 sf OR >3 stories OR combined ≥24,000 sf | **>2 stories OR >5,000 sf** |
| Group E | Fire area >12,000 sf | **>2 stories OR >5,000 sf** |
| Group F-1 | Fire area >12,000 sf OR >3 stories OR combined ≥24,000 sf | **>2 stories OR >5,000 sf** |
| Group M | Fire area >12,000 sf OR >3 stories OR combined ≥24,000 sf OR upholstered furniture/mattress display >5,000 sf | **>2 stories OR >5,000 sf**; **upholstered furniture/mattress display = sprinklered regardless of size** |
| Group S-1 / S-2 | Fire area >12,000 sf OR >3 stories OR combined ≥24,000 sf | **>2 stories OR >5,000 sf** |

#### Sprinkler Retrofit Math (§14.50.104(2))

Both prongs must be true to trigger full retrofit of an unsprinklered commercial building:

1. **Sprinklers-required test** — Building post-work would be required to be sprinklered under Laguna's tightened §903.2 (table above); AND
2. **Valuation test** — Cumulative valuation of additions/alterations/repairs over a **rolling 3-year window** ≥ **50% of building's pre-work valuation**, using the City's resolution-based valuation schedule.

Additional independent retrofit triggers (§14.50.104(3) and (4)):

- **Already-sprinklered building** — any addition to a building already equipped with an automatic sprinkler system triggers extension throughout the addition (regardless of whether originally required).
- **Addition size** — any addition ≥33% of existing building area AND >1,000 sf within a 2-year period.

#### Public Notice (§25.05.065(D))

| Track | Mailed notice | Posted notice |
|-------|---------------|---------------|
| Planning Commission Design Review | ≥21 calendar days | ≥10 calendar days |
| Administrative Design Review (Director) | ≥14 calendar days | — |
| Default minor notice | ≥10 calendar days | — |

Notice radius: **300 ft property owners**; **100 ft commercial/apartment tenants** (within site or 100 ft); **300 ft HOA/master associations**; **Coastal Commission** if CDP involved.

#### Appeals

- DR decision → City Council, **14 calendar days** (§25.05.070).
- Appealable CDP → California Coastal Commission, **10 working days** after city's final action (§25.07.016).

#### CDP Lifecycle (§25.07.012(I)(3))

CDPs lapse after **2 years** if work not commenced.

#### Building Permit Lifecycle (§14.50.024)

Building permit expiration and extension are a citywide rule (§14.50.024) — see `../city-reference/SKILL.md` §"Permit Expiration".

---

### Review Checklist — City-Specific Items

| # | Item | Requirement | Source |
|---|------|-------------|--------|
| **LB-CTI-1** | Design review authority | Non-residential development routes to **Planning Commission** (not DRB). Administrative Design Review (Director) available for limited minor scope under §25.05.040(B). | LBMC §25.05.040(F)(1)(b) |
| **LB-CTI-2** | Current planning route | Match actual scope to the 16/28/17 closed lists. Record the exact category; do not use exterior visibility as a residual trigger. | LBMC §25.05.040(B); Ord. 1732 §7 |
| **LB-CTI-3** | Interior-only route | Interior modification with no exterior modification → Zone Clearance. Historic-resource actions separately route under current `(B)(1)(d)` or `(B)(3)(a)(iv)`. | LBMC §25.05.040(B)(2)(d) |
| **LB-CTI-4** | DR public notice | ≥21 calendar days mailed (Planning Commission); ≥14 days (ADR); ≥10 days posted on site. Notice radius 300 ft owners / 100 ft tenants / 300 ft HOA / CCC if CDP. | LBMC §25.05.065(D) |
| **LB-CTI-5** | DR appeal window | 14 calendar days to City Council after decision. | LBMC §25.05.070 |
| **LB-CTI-6** | Fire Safety Standards Review on DR | For new construction and major remodels, the Fire Department or Building Division, as applicable, must review/approve or conditionally approve prior to Design Review action. Public-safety conditions cannot be modified without that review authority's concurrence. The former 50%-alteration Fire-Department-only trigger is not current. | LBMC §25.05.040(C)(4) |
| **LB-CTI-7** | CDP required in Coastal Zone | Required for development in Coastal Zone except for items specifically exempted in §§25.07.008 / 25.07.010. ~95% of city is Coastal Zone. | LBMC §25.07.004 |
| **LB-CTI-8** | CDP intensity-of-use trigger | Improvements to non-SFR structures exempt **UNLESS** improvement results in a change in the intensity of use (the principal commercial trigger), OR is in the SFR-exemption-restricted areas (between sea and first public road, near bluff/wetland/ESHA), OR is a conversion of multi-unit/visitor-serving commercial to fee/long-term-leasehold ownership, OR significant landform alteration. | LBMC §25.07.008(A)(2) |
| **LB-CTI-9** | CDP de minimis waiver | Director may waive CDP for development that is non-appealable, consistent with LCP, no adverse effect, with similar projects routinely approved without conditions. 10-day public notice. | LBMC §25.07.009 |
| **LB-CTI-10** | Administrative CDP | Public hearing may be waived for "minor development" with Director consistency finding; 15-working-day public-hearing-request window; deemed approved if no request. | LBMC §25.07.013 |
| **LB-CTI-11** | Appealable CDP / CCC appeal | Appealable to CCC within **10 working days** if project is between sea and first public road, within 300 ft of inland extent of beach/MHW, within 100 ft of wetland/estuary/stream, within 300 ft of seaward face of coastal bluff, OR major public works / energy facility. | LBMC §25.07.016, §25.07.006 |
| **LB-CTI-12** | CDP effective date | Non-appealable: effective on adequate notice of final action. Appealable: not effective until 10-working-day CCC appeal period expires with no appeal. | LBMC §25.07.012 |
| **LB-CTI-13** | CDP lapse | CDP lapses after **2 years** if work not commenced. | LBMC §25.07.012(I)(3) |
| **LB-CTI-14** | Commercial sprinkler thresholds | Group A/B/E/F-1/M/S-1/S-2 sprinklered at **>2 stories OR >5,000 sf**. Group M with upholstered furniture display sprinklered regardless of size. | LBMC §14.50.104 amending CBC §903.2 |
| **LB-CTI-15** | Commercial sprinkler retrofit | Full retrofit required when (a) post-work building would be required to be sprinklered AND (b) work valuation ≥50% of pre-work valuation cumulative over 3-year rolling window. | LBMC §14.50.104(2) amending CBC §903.6 |
| **LB-CTI-16** | Retrofit — already-sprinklered building | Any addition to an already-sprinklered building extends system throughout the addition. | LBMC §14.50.104(3) |
| **LB-CTI-17** | Retrofit — large addition | Any addition ≥33% of existing area AND >1,000 sf within 2 years triggers full retrofit. | LBMC §14.50.104(4) |
| **LB-CTI-18** | Spec/shell quick-response sprinklers | Quick-response sprinklers required in shell/spec commercial buildings of undetermined use (other than warehouses). | LBMC §15.01.070 amending NFPA 13 §9.4.3.1 |
| **LB-CTI-19** | FDC configuration | Minimum two 2½" inlets (four if ≥500 gpm or standpipe), painted OSHA red, ≤150 ft from public hydrant, on the street-address side. | LBMC §15.01.070 amending NFPA 13 |
| **LB-CTI-20** | Hydrant flow test currency | Hydrant flow test ≤6 months old at the time of working-plan submittal. Submit `fire-hydrant-flow-form.pdf` (doc ID 11178). | LBMC §15.01.070 amending NFPA 13 §28.1.3 |
| **LB-CTI-21** | Fire alarm — Group A ≥100 OL | Manual fire alarm system with occupant notification required for Group A occupancies with occupant load ≥100. | LBMC §15.01.035 amending CFC §907.2.1 |
| **LB-CTI-22** | Alternative extinguishing monitoring | Alternative fire-extinguishing systems must be monitored by building fire-alarm/monitoring system per NFPA 72. | LBMC §14.50.105 amending CBC §904.3.5 |
| **LB-CTI-23** | Class I standpipe | Class I standpipe hose connections per local amendment. | LBMC §14.50.106 amending CBC §905.4 |
| **LB-CTI-24** | Duct smoke detectors | Local §907.3.1 amendment. | LBMC §14.50.107 |
| **LB-CTI-25** | Atrium sprinklers | Sprinklers throughout atrium-containing buildings. | LBMC §14.50.052 amending CBC §404.3 |
| **LB-CTI-26** | High-rise threshold | High-rise + Group I-2 triggered at >55 ft above lowest fire-department-access level. | LBMC §14.50.044 amending CBC §403.1 |
| **LB-CTI-27** | HMMP / HMIS | Hazardous Materials Management Plan / Inventory Statement required where required by fire code official (commercial occupancies with chemical storage — dry cleaners, photo labs, salons, restaurants with bulk CO2). | LBMC §15.01.050 amending CFC Ch. 50 |
| **LB-CTI-28** | Class A roof citywide | Class A roof assembly required citywide for any building, new or reroof. | LBMC §14.50.120 amending CBC §1505; Ch. 14.70 §14.70.020 |
| **LB-CTI-29** | WUI exterior materials | In VHFHSZ, exterior walls noncombustible/ignition-resistant; vinyl windows welded corners + metal reinforcing; skylights glass only (no plastic); vent openings ≤144 sq in or 1⅜" solid-core door equivalent. Exception: minor repair/replacement of exterior materials with same materials. | LBMC Ch. 14.70 (§§14.70.015 / 14.70.025 / 14.70.030 / 14.70.035 / 14.70.040) |
| **LB-CTI-30** | Defensible space | All habitable structures in VHFHSZ must maintain defensible space per August 2021 guideline; maintenance obligation regardless of permit status. | LBMC §14.70.060; CFC §304.1.3.2 |
| **LB-CTI-31** | Fuel modification | For new construction or major remodels in Fuel Modification designation areas — preliminary plans concurrent with tentative map; final plans approved by Fire Code Official before building permit issuance. | LBMC §14.70.070; CFC §324 |
| **LB-CTI-32** | Heritage Committee review | Properties 50+ years old or on 1980-81 inventory route through Heritage Committee for alterations, Mills Act, Historic Register placement. Demolition of historic-register structure requires published newspaper notice. | LBMC Ch. 25.45; §25.05.065(F) |
| **LB-CTI-33** | Historic alterations | Qualifying minor action → ADR after Heritage Committee recommendation; major action → Design Review after recommendation. Apply current §25.45.010. | LBMC §25.05.040(B)(1)(d), (B)(3)(a)(iv); §25.45.010 |
| **LB-CTI-34** | Downtown Specific Plan | Apply Ch. 25.40 standards, then match current §25.05.040 lists. Do not use the repealed DSP Public Works ADR exclusion; CIP routing now uses major/de minimis/minor CIP categories. | LBMC Ch. 25.40; §25.05.040(B)(1)(p), (B)(2)(bb), (B)(3)(a)(xvii) |
| **LB-CTI-35** | Specific Plan / overlay districts | Identify any applicable specific plan: Downtown SP (Ch. 25.40), Arch Beach Heights SP (Ch. 25.35), Three Arch Bay (private community — separate application doc ID 11971), Village Entrance / North Coast Highway corridor (Coastal commercial frontage; CDP + Planning Commission DR very likely; CCC appealability check). | LBMC Title 25, Chs. 25.35 / 25.40 |
| **LB-CTI-36** | Sign programs (Ch. 25.54) | Planning Commission may delegate administrative approval to Director for new signs or changes to existing signs **subject to an approved sign program**. Without an approved program, exterior signs route to hearing. Sign sizing: 1 sf per linear foot of frontage, 150 sf max per site, 75 sf max per sign. Commercial signs are OTC-eligible at counter. | LBMC Ch. 25.54 |
| **LB-CTI-37** | LBFD review (not OCFA) | Multi-family, commercial, industrial new construction and remodel projects route to LBFD at entitlement and at building-plan-check. Contact: fireprevention@lagunabeachcity.net / (949) 497-0352. | LBFD Fire Prevention Division |
| **LB-CTI-38** | Submittal sets | 3 sets 24"×36" construction drawings (architectural, structural, MEP, energy, green building) + 2 sets supporting (geotech soils report, structural calcs, energy calcs). | the city reference / Plan Check FAQ |
| **LB-CTI-39** | Submittal sequence | Planning Division (Zoning Plan Check) → Public Works → Building Division. Building does not accept without Planning and Public Works sign-offs. | City policy |
| **LB-CTI-40** | Applications required | Building application (doc ID 216); EMP permit application (doc ID 11955); Planning application (doc ID 23183); Design Review application (doc ID 25175) only if a current `(B)(1)` category matches; CDP application (doc ID 25230) if not exempt; Demolition Notification (doc ID 10699) if demo; Subcontractor list (doc ID 5143). | Permit manifest |
| **LB-CTI-41** | Caltrans encroachment | Required when work touches PCH (Coast Hwy / Hwy 1) or Laguna Canyon Road (Hwy 133) frontages. | State |
| **LB-CTI-42** | Public Works encroachment | Encroachment / right-of-way work (sidewalk café, ADA path-of-travel improvements in ROW) — revocable encroachment permits (doc ID 18755). | City policy |
| **LB-CTI-43** | Permit exemptions (interior finishes) | Painting, papering, tiling, carpeting, cabinets, counter tops, similar finish work exempt. Non-fixed movable fixtures/cases/racks/counters/partitions ≤5'9" exempt. | LBMC §14.50.022 amending CBC §105.2 |
| **LB-CTI-44** | Adjoining property protection | Protection of adjoining property during construction/demo; 30-day excavation notice; excavation retention systems required where applicable. | LBMC §14.50.132 amending CBC §3307 |
| **LB-CTI-45** | Construction hours | **Weekdays 7:30 AM – 6:00 PM only** per §7.25.080(A). **Saturday, Sunday, federal holidays all PROHIBITED** per §7.25.080(B) — no Saturday window in Laguna. Materially stricter than Costa Mesa; frequent enforcement in Downtown / Heisler Park / Forest Ave commercial-residential interface. Memorial Day–Labor Day downtown moratorium applies to construction in DSP-area frontages. | LBMC §7.25.080 |
| **LB-CTI-46** | Permit lifecycle | Building permit expiration and extension per `../city-reference/SKILL.md` §"Permit Expiration". CDP lapses after 2 years. DR approval effective 14 days after decision; lapses per approval terms. | LBMC §14.50.024; §25.07.012; §25.05.040(K) |
| **LB-CTI-47** | OTC eligibility | Commercial **signs** (and simple sign change-outs) are OTC-eligible at counter (Mon 7:30–4:30; Tue–Thu 7:30–1:00). Full commercial TIs are not OTC. | City counter policy |
| **LB-CTI-48** | Reinspection fees | Reinspection fees per §14.50.026 (CBC §109.7 amendment). | LBMC §14.50.026 |
| **LB-CTI-49** | Water Quality / WELO | Non-priority development checklist + notes (doc IDs 5149/5151). WELO required only if landscape >500 sf modified (doc IDs 14292/14294). | Permit manifest |

---

### Output Format

Every Laguna Beach commercial TI review should include these city findings:

```markdown
## Laguna Beach City Overlay — Commercial TI
**Planning route:** Planning Commission DR | ADR | Zone Clearance | needs_source
**Coastal/CDP:** Required (full hearing) | Administrative CDP | De minimis waiver | Exempt | CCC-appealable
**LBFD review:** Entitlement + plan-check | Plan-check only | N/A
**Sprinkler — new threshold (LB-CTI-14):** PASS | FAIL | FLAG
**Sprinkler retrofit (LB-CTI-15):** PASS | FAIL | FLAG | N/A
**WUI / Class A roof (LB-CTI-28/29):** PASS | FAIL | FLAG
**Heritage (LB-CTI-32/33):** Required | N/A
**Specific Plan / overlay:** DSP | Arch Beach Heights | Three Arch Bay | Village Entrance / N. Coast Hwy | None
**Construction hours acknowledgment:** PASS | FLAG
**Submittal completeness (3-set + 2-supporting + apps):** PASS | FAIL | FLAG
```

Return citations for every FAIL or FLAG. Do not substitute Title 15 §1103.5.4 (Group R) language for the commercial retrofit math — use **§14.50.104** for all commercial occupancies.

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

This plugin does not carry the California code checklist for Commercial Tenant Improvement plan sets: the building, residential, structural, fire and life-safety, energy, green-building, plumbing, mechanical, electrical and accessibility requirements. That check comes from CrossBeam.

**When the CrossBeam connector is connected** (the host has tools whose names start with `crossbeam_`):

1. Call `crossbeam_get_review_requirements` with `city: "laguna-beach"` and `permit_type: "commercial-ti"`. It returns the review lanes, the required documents and the packaging rules, with citations. Read it beside the City checklists above. Where they differ, tell the user and cite both. Coverage `none` means CrossBeam has no data, not that nothing is required.
2. Ask code questions with `crossbeam_ask`. Send the city (Laguna Beach, CA), the permit type and the project facts you have, and follow up with its `conversation_id`. A code section the answer cites that is not in its citations is unverified.
3. To check a plan set against the code, use a CrossBeam check. For a set drawn with CrossBeam's permit-drawings skill, call `crossbeam_get_skill` with `skill_id: "permit-drawings"` and follow `../../references/plan-sheets.md` section 2; permit-drawings runs the check. For a set drawn by someone else, the user uploads it for a CrossBeam check in the CrossBeam app, because the connector does not upload plans; then read the results with `crossbeam_list_projects`, `crossbeam_get_project_summary` and `crossbeam_get_findings`. A CrossBeam check is paid. Start one only with the user's approval.

CrossBeam cites the current 2025 California Building Standards Code (Title 24, effective 2026-01-01). Use its citations over code sections you remember. Apply the Laguna Beach rules above on top of them.

**When the connector is not connected**, or a tool is missing or needs sign-in:

- Do not check the design against the California codes from memory, and never report a California code item as passing.
- Do the Laguna Beach rules and the City checklists in full, then list California code compliance as **not checked**.
- Say it plainly, once: "This plugin checks the Laguna Beach rules and the City's submittal checklists for Commercial Tenant Improvement permits. It cannot check the plans against the California building codes. For that, connect CrossBeam (crossbeam-permits.com) and run a CrossBeam check before you file."
- Then carry on with intake, the City checklists and filing.

---

## References

Load these on demand. Paths are relative to this file.

- `../../requirements/README.md` — the City submittal checklists, plan-sheet matrix and issuance checklist
- `../plan-set-check/SKILL.md` — checks a plan set against the City checklists
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**Laguna Beach rules**

- `references/coastal-development-permit.md` — Laguna Beach — Commercial TI Coastal Development Permit (CDP)
- `references/design-review.md` — Laguna Beach — Current Commercial TI Planning Route (Ord. 1732)
- `references/heritage.md` — Laguna Beach — Heritage Committee / Historic Resources for Commercial TI
- `references/specific-plans.md` — Laguna Beach — Specific Plans and Overlay Districts for Commercial TI
- `references/sprinkler-retrofit-commercial.md` — Laguna Beach — Commercial Sprinkler Retrofit (LBMC §14.50.104)
- `references/submittal-package.md` — Laguna Beach — Commercial TI Submittal Package
- `references/wui-commercial.md` — Laguna Beach — WUI / VHFHSZ Requirements for Commercial TI

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
