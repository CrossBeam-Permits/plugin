---
name: patio-cover
description: "Patio Cover permits in Laguna Beach, CA. A roofed cover over a patio or deck, attached or freestanding, new or replaced. NOT skylights or small repairs on an existing cover. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions patio cover in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Residential Code (Title 24, Part 2.5) — Appendix BF and Sections R301, R304, R403, R802, R803, R902 and R905"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2026"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Patio Cover Permit

Handles patio cover permits in Laguna Beach end-to-end. Scope: A roofed cover over a patio or deck, attached or freestanding, new or replaced. NOT skylights or small repairs on an existing cover.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a patio cover permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Patio Cover Permit

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

For related existing deck/patio repair rules, also see `../deck-patio-repair/SKILL.md`.

---

### Key Delta Summary

| Topic | State Default | Laguna Beach Override |
|---|---|---|
| OTC eligibility | Varies | Only **deck, balcony, patio cover repairs** with no extension/replacement are listed as OTC-eligible in the city reference |
| New patio cover | State plan review only | New patio covers are exterior physical improvements and require zoning/planning review; may require Administrative Design Review, DRB, CDP, and WUI review depending on site |
| Design review | State silent | Slabs/patios at or below natural grade are design-review exempt; elevated deck/patio structures over 3 ft can trigger Administrative Design Review or DRB depending on scope/site |
| Coastal zone | State CDP framework | Most of Laguna is coastal; SFR improvement exemption must be checked against LBMC Section 25.07.008 exceptions |
| Oceanfront/bluff | State defers to local | Patio/deck cover projections on oceanfront lots must respect Section 25.50.004(B)(4) stringline/bluff setback rules |
| WUI | State WUI applies in mapped areas | Laguna applies Ch. 14.70 WUI to exterior materials for new buildings, additions, alterations, and repairs in city WUI areas |
| Geotech | State project-specific | Laguna geotech handout flags coastal bluff, steep hillside, non-conventional foundations, and Building Official discretion |

---

### Decision Tree Router

| Scope | Laguna Route |
|---|---|
| Repair only; no extension/replacement | OTC candidate if no structural expansion, no CDP/design-review trigger, and not part of major remodel |
| New attached patio cover | Building permit + zoning review; structural ledger review per state skill; check DR/CDP/WUI/geotech |
| New freestanding patio cover | Building permit + zoning review; check detached-structure CDP exceptions in coastal appealable area |
| Oceanfront or bluff-adjacent cover | Require bluff setback/stringline review and likely CDP/geotech review |
| Patio cover with electrical lighting/fans/heaters | Add electrical permit/review under state CEC plus Laguna permit routing |
| Part of addition or major remodel | Route to `residential-addition` or `residential-remodel` city skill |

---

### Laguna-Specific Checks

#### 1. OTC Eligibility

Laguna's the city reference lists **deck, balcony, patio cover repairs (no extension/replacement)** as OTC-eligible. Do not classify a new patio cover, footprint expansion, roof conversion, or structural replacement as OTC.

OTC candidates still need the city-specific overlay checks below. OTC means faster plan review, not exemption from zoning, CDP, WUI, or geotechnical constraints.

#### 2. Design Review

Use LBMC Section 25.05.040 and the city's zoning plan-check table:

- Slabs and patios at or below natural grade are exempt from design review.
- Elevated decks 3 ft or less above adjacent existing grade are exempt.
- Elevated decks more than 3 ft above adjacent existing grade are Administrative Design Review candidates.
- All structures and physical improvements on lots with slope greater than 30% or in environmentally sensitive areas are Design Review Board/Planning Commission candidates unless a specific exception applies.
- If the patio cover is part of an addition, upper-story work, >15 ft height condition, or >=50% aggregate addition/major remodel, route to the complex residential skill.

#### 3. Coastal/CDP Review

Most Laguna parcels require a coastal-zone check. For SFR properties, LBMC Section 25.07.008(A)(1) may exempt improvements normally associated with a single-family dwelling, but exceptions commonly matter for patio covers:

- Within 50 ft of coastal bluff edge, beach, wetland/stream, ESA, or highly scenic area.
- In appealable area with a detached structure, 10% floor-area increase, or 10% height increase.
- Prior CDP condition requiring future CDP.
- Significant landform or vegetation alteration.

If any exception applies or cannot be ruled out, flag CDP review.

#### 4. Oceanfront Bluff and Projection Rules

For oceanfront/bluff lots, apply LBMC Section 25.50.004(B)(4):

- No new building, addition, structure, or improvement may encroach beyond the applicable building stringline or be closer than 25 ft to top of oceanfront bluff, whichever is more restrictive, unless a specific projection rule applies.
- Balconies, patios, decks more than 30 in above finished grade, including patio deck covers, may project up to 5 ft beyond the applicable building setback or to the deck stringline, whichever is least restrictive, but never closer than 10 ft to top of bluff.
- Decks, patios, and similar improvements 30 in or less above grade must not encroach closer than 10 ft to top of bluff.

Require a bluff edge determination when the site is oceanfront/bluff-adjacent and the plans do not clearly establish the bluff edge.

#### 5. WUI / VHFHSZ Exterior Construction

Laguna Ch. 14.70 applies to exterior materials, systems, and assemblies for new buildings, additions, alterations, and repairs in WUI areas. For patio covers:

- Solid roof covers must use Class A roof assembly if roofed.
- Exterior wall/soffit/adjacent assemblies must use noncombustible, ignition-resistant, or approved fire-retardant materials as applicable.
- Plastic skylights/sloped glazing are not allowed.
- Defensible space and fuel modification requirements may apply to new construction/major remodels in fuel modification areas.
- Minor repairs with same materials require Building Official approval under Section 14.70.015 exception.

---

### Review Checklist - Laguna Patio Cover

| ID | Check | Pass Criteria |
|---|---|---|
| LB-PAT-1 | OTC classification | Scope is repair only, no extension/replacement, and no larger project trigger |
| LB-PAT-2 | Zoning/design-review path | Section 25.05.040 category identified: exempt, Administrative Design Review, or DRB/Planning Commission |
| LB-PAT-3 | Coastal/CDP status | Coastal zone status and Section 25.07.008 exemption/exceptions documented |
| LB-PAT-4 | Bluff/topographic constraints | Oceanfront/bluff setbacks and projection limits checked; bluff edge determination requested if needed |
| LB-PAT-5 | WUI materials | Ch. 14.70 exterior material and Class A roof/skylight requirements applied |
| LB-PAT-6 | Geotech trigger | Hillside, bluff, slope >1V:2H, non-conventional foundation, or Building Official discretion checked |
| LB-PAT-7 | Electrical add-ons | Lighting/fans/heaters routed to electrical review and shown on plans |
| LB-PAT-8 | Plan submittal | Site plan shows setbacks, property lines, structures, easements, bluff line if applicable, and distances to adjacent structures |

---

## California Checklist

The California checklist for this permit is in `references/california-baseline.md`. Walk its decision tree and every checklist row after the Laguna Beach rules above. For each row, decide whether it is checked at plan check or verified by the inspector in the field. Do not list inspection items as corrections.

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/appendix-bf-patio-covers.md` — CRC Appendix BF — Patio Covers
- `references/footings-posts.md` — Patio-Cover Footings, Posts and Connections
- `references/ledger-attachment.md` — Attached Patio-Cover Wall Connection Routing
- `references/roof-framing-spans.md` — Patio-Cover Roof Framing and Coverings

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
