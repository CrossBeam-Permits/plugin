---
name: pool-demolition
description: "Pool Demolition permits in Laguna Beach, CA. An existing pool or spa demolished or filled, with utilities disconnected and backfill. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions pool demolition in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2) — Chapters 18, 33, Appendix J; 2025 California Electrical Code (Title 24, Part 3) — Article 680; 2025 California Plumbing Code (Title 24, Part 5) — Chapters 3, 6, 7, 12"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2025"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Pool Demolition Permit

Handles pool demolition permits in Laguna Beach end-to-end. Scope: An existing pool or spa demolished or filled, with utilities disconnected and backfill.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a pool demolition permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Pool Demolition Permit

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
| Demolition notification | Varies | Use Laguna Demolition Notification/SCAQMD Rule 1403 screening where shell, structural, or load-supporting demolition is involved |
| Coastal zone | State Coastal Act | LBMC Section 25.07.006 includes demolition in "development"; coastal-zone pool/spa demolition requires CDP unless a specific exemption applies |
| Bluff/oceanfront | State project-specific | Pool/spa work on oceanfront bluff lots must check Section 25.50.004(B)(4), bluff edge, geotech, and coastal hazards |
| Geotech/backfill | State structural baseline | Laguna geotech handout flags soil/structure failure, steep hillside, coastal bluff, liquefaction, floodplain, and Building Official discretion |
| Drainage/floodplain | State/CBC baseline | Finished grade and fill/excavation must coordinate with floodplain permit, WQMP, erosion control, and city drainage requirements where applicable |
| Larger project | Permit-specific | If pool demo is part of addition, new construction, or major remodel, route to complex residential skill |

---

### Decision Tree Router

| Scope | Laguna Route |
|---|---|
| Partial pool/spa demo for landscape only | Pool-demolition skill + city overlay; no structure over backfilled area unless full removal/geotech path is approved |
| Full pool removal or future structure over pool area | Require geotech/backfill support; may need full excavation, compaction report, and structural/geotech review |
| Coastal-zone pool/spa demolition | CDP analysis required before permit clearance |
| Oceanfront/bluff/hillside lot | Bluff edge/geotech/drainage review; do not treat as simple backfill |
| Pool demo bundled with remodel/addition/new SFR | Route to corresponding complex city skill |

---

### Laguna-Specific Checks

#### 1. Demolition Notification / SCAQMD

Use the Laguna Demolition Notification form when the scope removes structural pool shell elements, related structural components, or otherwise meets the Rule 1403 demolition definition. Require SCAQMD confirmation and asbestos/abatement documentation where applicable.

If the applicant asserts the pool demo is not Rule 1403 demolition, keep the finding as `ask_the_city` unless the city form or Building Division confirms the exemption.

#### 2. Coastal Development Permit

Pool/spa demolition in the coastal zone is development unless exempt. Because LBMC Section 25.07.006 includes demolition in the development definition, the reviewer must document a Section 25.07.008 exemption before clearing a coastal-zone pool demo.

Watch for exemption loss when the work:

- Is on a beach, in wetland/stream, within 50 ft of coastal bluff edge, in ESA, or in a highly scenic area.
- Causes significant landform alteration or vegetation removal.
- Involves mechanized equipment/materials in protected coastal areas.
- Is tied to shoreline protective work or bluff retaining wall work.

#### 3. Geotech, Backfill, and Drainage

Laguna's terrain makes pool demolition backfill higher risk than flatland cities. Flag geotechnical review when:

- Lot is steep hillside, coastal bluff top, liquefaction zone, floodplain, or oceanfront.
- Soil failure or structural failure has occurred.
- A future structure, footing, patio cover, ADU, addition, or new SFR is proposed over the former pool area.
- Fill/excavation materially changes drainage.

#### 4. Floodplain / Water Quality

If fill/excavation is in a FEMA flood zone or floodway, require floodplain permit screening. If pool water discharge, backfill, stockpiles, or grading can affect storm drains, require erosion control and water-quality notes.

---

### Review Checklist - Laguna Pool Demolition

| ID | Check | Pass Criteria |
|---|---|---|
| LB-PDEMO-1 | Correct permit route | Pool/spa demolition only; larger remodel/addition/new construction routed separately |
| LB-PDEMO-2 | City demolition/SCAQMD | Demolition Notification and Rule 1403 screening completed where structural/shell demolition applies |
| LB-PDEMO-3 | Coastal/CDP | Coastal-zone status and Section 25.07.008 exemption/exceptions documented |
| LB-PDEMO-4 | Bluff/hillside/geotech | Bluff edge, slope, liquefaction, failure history, and future structure-over-fill checked |
| LB-PDEMO-5 | Backfill/compaction | State pool-demolition backfill, compaction, filter fabric, and disclosure requirements shown |
| LB-PDEMO-6 | Drainage/water quality | Finished drainage, dechlorinated discharge, erosion controls, and WQMP/floodplain triggers checked |
| LB-PDEMO-7 | Utilities | Electrical, gas, water, sewer, and pool equipment disconnections/caps shown |

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Permit type correct?** | ❌ **fail** | Pool/spa demolition permit; partial demo (shell remains below grade) for landscape use only. If structure will be built over the area, full removal with geotech report is required -- different permit process. | CBC 105.1 |
| 2 | **Site plan complete?** | ❌ **fail** | Property lines with dimensions, all buildings/structures shown, pool/spa location, easements/setbacks, driveways, streets, north arrow, fence locations with heights, electrical panel and gas meter locations, proposed fill material specified, debris/backfill storage location, erosion control measures. | CBC 107.2.6 |
| 3 | **Scope of work defined?** | ❌ **fail** | Permit is for demolition of existing pool/spa including capping of associated plumbing and electrical. No other improvements allowed under this permit. | CBC 3303.1 |
| 4 | **Pool dimensions provided?** | ⚠️ **flag** | Length, width, deepest depth, shallowest depth, estimated volume in gallons. These determine backfill quantity and inspection scope. | -- |
| 5 | **Drainage holes adequate?** | ❌ **fail** | Pool: 2 holes at 36" dia, one at lowest point. Spa: 1 hole at 36" dia at lowest point. Holes equally spaced across deep end and levels. | CBC 3303.5 |
| 6 | **Gravel layer specified?** | ❌ **fail** | 12-inch layer of #4 rock (1" to 2.5" Class II permeable free-draining rock) over drain holes and pool shell bottom. | CBC 3303.5 |
| 7 | **Coping/bond beam removal adequate?** | ❌ **fail** | Remove pool coping, bond beam, and steel rebar around entire perimeter to at least 18 inches below finished grade. | CBC 3303.4 |
| 8 | **Backfill material specified?** | ❌ **fail** | Self-compacting fill sand (SE25 type), clean fill dirt, or as specified in soils report. No organic material, construction debris, cobbles, or boulders. Fill to within 30 inches of final surface, then planting medium for upper 18 inches. | CBC 1804.3, J107.4 |
| 9 | **Compaction method specified?** | ❌ **fail** | Hand compaction equipment, 6-inch lifts, prudent use of water. 90% minimum (90-95% typical) per ASTM D1557 Modified Proctor. Soil compaction report required at final inspection. | CBC 1804.6, 1705.6, J107.5 |
| 10 | **Geotechnical filter fabric?** | ⚠️ **flag** | Filter fabric applied after backfilling, before planting medium layer. Separates structural backfill from planting medium. | -- |
| 16 | **Pool water discharge plan?** | ❌ **fail** | Water must be de-chlorinated before discharge to storm drain. Chlorinated/contaminated water must go off-site. No filter backwash or cleaning wastewater to storm drain. | NPDES/BMP |
| 17 | **Drainage/grading adequate?** | ❌ **fail** | Finished grade slopes minimum 2% away from all existing structures. Drainage pattern does not increase runoff to neighboring properties. | CBC 1804.4 |
| 18 | **Erosion control measures?** | ❌ **fail** | BMP measures during construction: silt fencing, gravel bags at storm drains, covered stockpiles. Erosion control on finished slopes before final inspection. | CBC 3304.1.5, J110.1 |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 11 | **Electrical properly decommissioned?** | Sub-panel and all related conductors removed back to service supply connection. Pool bonding system disconnected. Separate permit required if converting electrical for other uses. | CEC 680.13, CBC 3303.6 |
| 12 | **Gas line capped at both ends?** | Gas line disconnected and capped gastight at BOTH the meter AND the equipment location. Must use screw joint fitting. | CPC 1206.3, 1210.8.1 |
| 13 | **Water supply capped?** | Water supply line to pool fill/autofill disconnected and capped at nearest active branch. | CPC 601.1, 309.6 |
| 14 | **Sewer/drain capped?** | Pool drain connection to sanitary sewer properly capped to prevent sewer gas and debris entry. | CPC 305.1, 701.1 |
| 15 | **Above-ground equipment removed?** | All above-ground pool equipment (pump, filter, heater, chlorinator, etc.) and associated plumbing removed. | CBC 3303.6 |
| 19 | **Owner disclosure signed?** | Owner acknowledges: area for landscape only, no structures; differential settlement risk; disclosure upon sale required (size, location, partial demolition method, backfilled). | -- |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/demolition-structural-cbc.md` — CBC Demolition & Structural Requirements
- `references/drainage-grading-erosion.md` — Drainage, Grading & Erosion Control
- `references/electrical-disconnect-cec.md` — CEC Article 680 — Electrical Disconnection for Pool Demolition
- `references/plumbing-gas-capping-cpc.md` — CPC Plumbing & Gas Line Capping Requirements

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
