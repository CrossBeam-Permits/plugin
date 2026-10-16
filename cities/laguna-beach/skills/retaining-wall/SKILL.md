---
name: retaining-wall
description: "Retaining Wall permits in Laguna Beach, CA. A wall that holds back soil or carries a surcharge, measured footing to top. NOT a garden, privacy, or property-line wall standing on level ground. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions retaining wall in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2 CBC), 2025 California Residential Code (Title 24, Part 2.5 CRC), ASCE 7-22"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2025"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Retaining Wall Permit

Handles retaining wall permits in Laguna Beach end-to-end. Scope: A wall that holds back soil or carries a surcharge, measured footing to top. NOT a garden, privacy, or property-line wall standing on level ground.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a retaining wall permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Retaining Wall Permit

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

### Key Delta Summary

| Topic | State Default | Laguna Beach Override |
|---|---|---|
| Permit exemption | CRC/CBC exempt certain retaining walls <=4 ft | LBMC Section 14.50.022 exempts retaining walls not over **48 in measured from bottom of footing to top of wall**, unless supporting surcharge, impounding flammable liquids, or within 3 ft of property line/public ROW |
| Planning route (Ord. 1732) | State silent | Exposed height 5 ft or less: Zone Clearance, LBMC 25.05.040(B)(2)(j). Over 5 ft exposed height: Design Review, 25.05.040(B)(1)(g). Any wall in an environmentally sensitive area (including slopes of 30% or more): Design Review under 25.05.040(B)(1)(e) unless a peer-reviewed licensed professional finds no impact |
| Geotech report | CBC project-specific | Laguna geotech handout requires soils report for retaining walls greater than 5 ft high measured from bottom of footing, retaining walls supporting surcharge, steep slopes, bluff/oceanfront areas, soil/structure failure, or Building Official direction |
| Coastal/bluff walls | State coastal framework | Repair/maintenance of seawalls, bluff retaining walls, shoreline protective work, and work near bluff/ESHA often loses CDP exemption under LBMC Section 25.07.008 |
| Property line/ROW | Local permit trigger | Any retaining wall within 3 ft of property line or public right-of-way requires permit even if height would otherwise be exempt |

---

### Decision Tree Router

| Scope | Laguna Route |
|---|---|
| <=48 in from footing bottom to wall top; no surcharge; not within 3 ft of property/ROW | Building permit may be exempt; still check zoning/CDP/drainage |
| >48 in or any surcharge | Building permit + structural review |
| >5 ft exposed height | Design Review, 25.05.040(B)(1)(g): Design Review Board for a single-family or two-family lot, Planning Commission otherwise (25.05.040(F)(1)) |
| >5 ft measured from bottom footing, or surcharge | Geotechnical report required by city handout |
| Bluff/oceanfront retaining wall or shoreline protective work | CDP analysis required; exemption often unavailable |
| Grading over 20 cu yd outside the building footprint | Design Review, 25.05.040(B)(1)(f) (20 cu yd or less: Zone Clearance, (B)(2)(i)); also check geotech, WQMP, erosion control |

---

### Laguna-Specific Checks

#### 1. Permit Threshold

LBMC Section 14.50.022 exempts retaining walls not over 48 in high measured from bottom of footing to top of wall **unless**:

- The wall supports a surcharge.
- The wall impounds flammable liquids.
- The wall is within 3 ft of a property line.
- The wall is within 3 ft of a public right-of-way.

If any exception applies, require permit review.

#### 2. Planning Route (Ord. 1732, LBMC 25.05.040(B))

Source: the City source document (not included in this plugin).

- **Exposed height 5 ft or less:** Zone Clearance, 25.05.040(B)(2)(j). The Community Development Department checks zoning compliance (25.05.045).
- **Exposed height over 5 ft:** Design Review at a public hearing, 25.05.040(B)(1)(g). The Design Review Board hears it on a single-family or two-family lot; the Planning Commission hears it on any other lot and anywhere in the Downtown Specific Plan area (25.05.040(F)(1)(i)-(ii)).
- **Environmentally sensitive area** (ESA, which includes slopes of 30% or greater, 25.08 as amended by Ord. 1732): any wall goes to Design Review under 25.05.040(B)(1)(e) unless a licensed professional finds, subject to peer review, that it does not impact the ESA. The (B)(2) preamble bars Zone Clearance for ESA work without that finding.
- **Grading** over 20 cu yd outside the building footprint is its own Design Review item, 25.05.040(B)(1)(f).
- The Director may refer a Zone Clearance project up to the Design Review Board or Planning Commission (25.05.040(A)(2)(d)).
- A Coastal Development Permit is a separate question under Ch. 25.07 (25.05.040(A)(2)(e)); see section 4.

#### 3. Geotechnical Report

Laguna's geotechnical handout requires a soils/geotechnical report for:

- Retaining walls greater than 5 ft high measured from bottom of footing.
- Retaining walls supporting any surcharge.
- Sloped lots steeper than 1 unit vertical to 2 units horizontal.
- Beach/oceanfront properties, coastal bluff top properties, steep hillside, or liquefaction zone.
- Any construction or repair where soil failure or structure failure has occurred.
- Non-conventional foundation systems or Building Official direction.

Require the signed report, dated within one year of submittal, when the handout applies. The handout's paper copy count is never a missing item (the Online Permit Services Supervisor, 2026-10-13).

#### 4. Coastal and Bluff Retaining Walls

LBMC Section 25.07.008 has specific repair/maintenance exceptions for seawalls, bluff retaining walls, revetments, breakwaters, groins, culverts, outfalls, and similar shoreline work. CDP exemption is not available when work involves substantial foundation alteration, rip-rap/solid material on beach or coastal waters, replacement of 20% or more of certain shoreline protective work, mechanized equipment/materials in protected coastal areas, or work in/near ESHA, sand areas, bluff edge, coastal waters, or streams.

For oceanfront parcels, also apply Section 25.50.004(B)(4) bluff setback and bluff-edge determination rules.

---

### Review Checklist - Laguna Retaining Wall

| ID | Check | Pass Criteria |
|---|---|---|
| LB-RET-1 | Permit exemption tested | Height <=48 in from footing bottom to top of wall and no surcharge/liquid/property-line/ROW exception |
| LB-RET-2 | Planning route | Exposed height <=5 ft: Zone Clearance (25.05.040(B)(2)(j)); >5 ft: Design Review (B)(1)(g), DRB on SFR/duplex lots, Planning Commission otherwise; ESA override (B)(1)(e) applied |
| LB-RET-3 | Geotech report | Required triggers checked and report provided where required |
| LB-RET-4 | Coastal/CDP analysis | Section 25.07.008 repair and SFR improvement exceptions checked; bluff/shoreline work not cleared as exempt without support |
| LB-RET-5 | Bluff-edge constraints | Oceanfront bluff setback, original/buried bluff edge, and safety-factor analysis requested where applicable |
| LB-RET-6 | Drainage/grading | Drainage does not increase runoff to neighbors; grading/drainage/WQMP needs checked |
| LB-RET-7 | Property-line/ROW survey | Wall within 3 ft of property line or public ROW flagged for permit and location verification |
| LB-RET-8 | State structural checks | CBC 1807, surcharge, drainage, guard, and structural-calculation items handled by state skill |

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Permit required?** | ❌ **fail** | Height >4 ft (footing to top), or any height with surcharge, or impounding flammable liquids. Measure from bottom of footing to top of wall, not exposed face only. | CRC R105.2 |
| 2 | **Engineering required?** | ❌ **fail** | Walls >4 ft, surcharge loads, adverse soils, slopes above or below, tiered walls within influence zone, walls supporting structures/driveways, walls near ROW or property lines. Must be designed by CA licensed civil/structural engineer or architect. | CBC 1807.2 |
| 3 | **Soils report provided?** | ❌ **fail** | Required when: adverse soil conditions (expansive, liquefiable, fill), slopes, or per AHJ. Report must include allowable bearing pressure, lateral soil parameters, groundwater level, and recommendations. | CBC 1803.2, 1803.5.3 |
| 4 | **Lateral soil loads calculated?** | ❌ **fail** | Design for lateral earth pressure using equivalent fluid method or Rankine/Coulomb. Must account for at-rest vs active conditions, soil type, groundwater, and surcharge. Seismic lateral earth pressure for walls >6 ft in SDC D/E/F. | CBC 1807.2.2, 1610; ASCE 7-22 |
| 5 | **Surcharge loads accounted for?** | ❌ **fail** | Identify all surcharges: vehicles/driveways, buildings, slopes, stored materials, adjacent walls. Surcharge adds equivalent height to lateral pressure calculation. Typical: 2 ft equivalent for residential driveways, 4 ft for heavy vehicles. | CBC 1807.2.2 |
| 6 | **Stability analysis adequate?** | ❌ **fail** | Check safety factors: overturning >=1.5 (1.1 with seismic), sliding >=1.5 (1.1 with seismic). Bearing pressure within allowable. Uses 0.7x nominal earthquake loads + 1.0x other nominal loads. Standard load combinations of CBC 1605 do NOT apply to retaining wall stability. | CBC 1807.2.3 |
| 7 | **Footing design adequate?** | ❌ **fail** | Footing width, depth, reinforcement, and key (if provided). Footing below frost line (minimal in most CA) and minimum 12" below lower grade. Bearing area sufficient for soil capacity. | CBC 1807.2, 1809 |
| 8 | **Wall stem design adequate?** | ❌ **fail** | Stem thickness, vertical and horizontal reinforcement, concrete or masonry strength, dowel connections to footing. CMU walls: cells grouted, bond beams provided. | CBC 1807.2; ACI 318 / TMS 402 |
| 9 | **Drainage system shown?** | ❌ **fail** | Drainage behind wall is critical. Verify: drain rock (12" min width), perforated drain pipe at base (4" min, sloped to daylight), filter fabric between drain rock and native soil. Weep holes as supplemental (4" dia, 6-8 ft OC). Surface drainage graded away from wall top. | Engineering practice; CBC 1805 |
| 10 | **Waterproofing addressed?** | ⚠️ **flag** | Below-grade portions: dampproofing or waterproofing per CBC 1805 where wall retains habitable space or where required by design. Waterproofing membrane on soil side of wall below grade. | CBC 1805 |
| 11 | **Guards/railings required?** | ❌ **fail** | Guards required where retaining wall is within 36" of a walking surface AND the drop exceeds 30" from the walking surface to grade below. Guard height: 42" min above walking surface. Openings: 4" sphere test. Loads: 200 lb concentrated at top. | CBC 1807.2.5; CRC R321.1.1-R321.1.3 (2025 CRC; formerly R312.1); loads Table R301.5 |
| 12 | **Material specifications shown?** | ❌ **fail** | Structural concrete strength/durability follows CBC 1904.1/ACI 318 and the exposure/design; the 3,000-psi minimum is limited to CBC 1904.1's stated Group R-2/R-3 weather-exposed vertical surfaces. Verify CMU/mortar/grout/rebar/SRW specifications under the applicable design. Timber uses an R304.1 naturally durable or treated path; R304.1.2 ground-contact treatment applies only in its stated scope. | CBC 1904.1, 2103; CRC R304.1, R304.1.2; applicable ASTM/ACI/TMS design |
| 13 | **Tiered walls analyzed correctly?** | ❌ **fail** | If multiple walls, check spacing. Influence zone = 2x height of lower wall measured from base of lower wall. Walls within influence zone must be analyzed as a single composite wall. Walls outside influence zone may be designed independently. | CBC 1807.2 |
| 14 | **Grading plan consistent?** | ⚠️ **flag** | If retaining wall is part of a grading project, verify consistency with grading plan. Grading permits per CBC Appendix J when cut/fill exceeds thresholds (typically 50 cu yd or 5 ft depth of cut). | CBC Appendix J |
| 15 | **Contractor licensing adequate?** | ❌ **fail** | B (General Building) or C-8 (Concrete) for concrete walls. C-29 (Masonry) for CMU walls. C-12 (Earthwork/Paving) for grading. A (General Engineering) for walls with engineered grading. | B&P Code 7028 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/drainage-waterproofing.md` — Retaining Wall Drainage and Waterproofing Requirements
- `references/materials-construction.md` — Retaining Wall Materials and Construction Methods
- `references/permit-engineering-triggers.md` — Retaining Wall Permit Exemptions, Engineering Triggers, and Guard Requirements
- `references/structural-design-cbc1807.md` — Structural Design of Retaining Walls — CBC 1807

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
