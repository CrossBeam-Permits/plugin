---
name: block-wall
description: "Block Wall permits in Laguna Beach, CA. A freestanding masonry or CMU wall built with footing and reinforcement, taller than a fence permit covers. NOT a wall that holds soil. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions block wall in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2 CBC Chapter 21), 2025 California Residential Code (Title 24, Part 2.5 CRC R606), TMS 402/602-22, ASCE 7-22"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2026"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Block Wall Permit

Handles block wall permits in Laguna Beach end-to-end. Scope: A freestanding masonry or CMU wall built with footing and reinforcement, taller than a fence permit covers. NOT a wall that holds soil.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a block wall permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Block Wall Permit

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

For broader fence/wall guidance and the city standard detail reference, see `../fence/SKILL.md`.

---

### Scope

This skill covers **freestanding CMU/block walls** that do not retain soil. If soil is retained on one side, route to `../retaining-wall/SKILL.md`.

---

### Key Delta Summary

| Topic | State Default | Laguna Beach Override |
|---|---|---|
| Permit threshold | State fence/wall exemption generally higher | LBMC 14.50.022 (Building item 1) exempts walls and fences **not over 72 in** high unless within 3 ft of a property line or public ROW. The City standard block-wall detail (General Note 2) says a block wall over **30 in** from adjacent grade needs a permit. See "Permit trigger conflict" below |
| Survey/location | Varies | Licensed surveyor must certify location before footing inspection when wall is within 3 ft of property line or public ROW |
| Zoning approval | State silent | Zoning/Planning approval required before building permit issuance |
| Standard detail limits | State skill general CMU | City standard detail applies only to freestanding non-retaining wall with slope <10%, grade offset <=6 in, no surcharge, no adverse soil/liquefaction/flood conditions |
| Planning route (Ord. 1732) | State silent | A wall that meets LBMC 25.50.012 height limits (4 ft front yard, 3 ft front yard on a corner lot, 6 ft side/rear) needs Zone Clearance, 25.05.040(B)(2)(l). Decorative posts/columns up to 12 in above the front-yard limit: Administrative Design Review, (B)(3)(a)(vii). In an environmentally sensitive area (including slopes of 30% or more): Design Review, (B)(1)(e), unless a peer-reviewed licensed professional finds no impact |
| Utility/fire clearances | State/project-specific | City detail requires 36 in from fire hydrant and 12 in from water meter |

---

### Decision Tree Router

| Scope | Laguna Route |
|---|---|
| Freestanding CMU/block wall, no retained soil | This skill + state block-wall skill |
| Wall retaining soil | Route to Laguna retaining-wall skill |
| Wood/metal fence | Route to Laguna fence skill |
| Block wall on slope >=10%, adverse soil, liquefaction, flood hazard, surcharge, or >6 in grade offset | Standard detail not applicable; require registered design professional |
| Within 3 ft of property line or public ROW | Permit + surveyor location certification before footing inspection |

---

### Laguna Standard Detail Requirements

Use `../fence/references/city-block-wall-detail.md` for the city standard detail. Key local requirements:

- City detail General Note 2: permit required for block wall over 30 in high from adjacent grade (see conflict note below).
- Permit required for any wall/fence within 3 ft of property line or public ROW.
- Zoning approval required before building permit issuance.
- Surveyor certification required before footing inspection for walls within 3 ft of property line or public ROW.
- Standard detail not valid for retaining walls, surcharge, expansive/adverse soils, liquefaction/flood hazard, slope >=10%, or grade offset more than 6 in.
- Wall plus railing/guard/screen must not exceed 6 ft above lowest adjacent grade.
- Required inspections: footing, reinforcing steel, final.
- Fire hydrant clearance: 36 in. Water meter/foundation clearance: 12 in.

#### Permit trigger conflict (UNSETTLED)

LBMC 14.50.022 (Ord. 1725, 2025-12-18), Building item 1, reads: "Walls and fences not over 72 inches high, unless located within three feet of a property line or public right-of-way." LBMC 14.52.014 (CRC R101.4) applies that list to homes too. The City's standard block-wall detail (June 2026, General Note 2) still says a block wall over 30 in from adjacent grade needs a building permit. For a block wall between 31 and 72 in that is more than 3 ft from every property line and the right-of-way, the code says no permit and the City detail says permit. The code text is the ordinance; the detail is a Building Division handout. **UNSETTLED: confirm with the Building Division before telling a resident no permit is needed.** Either way, Planning (Zone Clearance) and the CDP check still apply.

---

### Review Checklist - Laguna Block Wall

| ID | Check | Pass Criteria |
|---|---|---|
| LB-BLK-1 | Correct skill route | Wall is freestanding and non-retaining; retaining walls routed elsewhere |
| LB-BLK-2 | Permit trigger | Not within 3 ft of property line/ROW and not over 72 in (14.50.022) if claiming no permit; flag the 30 in City-detail conflict for walls 31-72 in |
| LB-BLK-3 | Standard detail applicability | Slope <10%, no surcharge, no retaining function, no adverse soil/liquefaction/flood hazard, grade offset <=6 in |
| LB-BLK-4 | Zoning approval | Planning/Zoning approval shown before building permit issuance |
| LB-BLK-5 | Survey certification | Within 3 ft of property line/ROW has licensed surveyor certification before footing inspection |
| LB-BLK-6 | Structural table | Rebar, footing, expansion joints, cleanouts, block specs match city standard detail or engineered design |
| LB-BLK-7 | Clearances | 36 in from fire hydrants, 12 in from water meters, no unauthorized ROW projection |
| LB-BLK-8 | Planning route | Zone Clearance (25.05.040(B)(2)(l)) only if the wall meets 25.50.012 heights and is outside an ESA; front-yard posts over the limit = ADR (B)(3)(a)(vii); ESA without peer-reviewed no-impact finding = Design Review (B)(1)(e) |
| LB-BLK-9 | Coastal/CDP | Coastal zone and Section 25.07.008 detached/fence exceptions checked where applicable |

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Permit Required?** | ❌ **fail** | Freestanding walls <=7 ft are exempt per state code. Cities commonly set lower thresholds (4-6 ft). Block walls functioning as retaining walls use the 4 ft threshold. Check city overlay. | CRC R105.2 |
| 2 | **Height Measurement** | ❌ **fail** | Height measured from finished grade on the higher side to top of wall (including cap). For walls on slopes, measure from the higher adjacent grade. For walls on retaining walls, combined height measured from lower grade. | CRC R105.2; local practice |
| 3 | **Engineering Required?** | ❌ **fail** | Walls over 6 ft typically require structural engineering by a CA licensed civil/structural engineer. Walls 4-6 ft may use prescriptive city standard details OR engineering. Cities set their own engineering trigger heights. | CBC 2101.2; city code |
| 4 | **CMU Block Specification** | ❌ **fail** | ASTM C90, load-bearing concrete masonry units. Grade N (moisture-controlled) for exterior. Minimum f'm = 1,500 psi. Standard: 8" x 8" x 16" nominal (7-5/8" x 7-5/8" x 15-5/8" actual). Running bond required (CRC R606.8). | CRC R606.2.1; CBC 2103.1; ASTM C90 |
| 5 | **Mortar Type** | ❌ **fail** | Type M or S required for structural masonry in California seismic zones. Type M (2,500 psi) preferred for below-grade/ground contact. Type S (1,800 psi) acceptable above-grade. Type N NOT acceptable for freestanding exterior walls. Must comply with ASTM C270. | CRC R606.2.8.3; CBC 2103.2 |
| 6 | **Grout Specification** | ❌ **fail** | ASTM C476, minimum f'c = 2,000 psi. Slump 8-11 inches (pourable). Fine grout for cells <=2" wide; coarse grout for cells >2" wide. All cells with rebar fully grouted. Consolidation by mechanical vibration or puddling required. | CRC R606.2.12; CBC 2103.3 |
| 7 | **Rebar Specification** | ❌ **fail** | ASTM A615 or A706, Grade 60 (60,000 psi yield). Minimum bar size: #4 (1/2" diameter). Minimum cover: 5/8" in grouted cells. Lap splice: 48 bar diameters minimum (#4 = 24" minimum). | TMS 402/602 |
| 8 | **Vertical Reinforcement** | ❌ **fail** | Vertical rebar resists overturning from wind and seismic. Spacing by height: #4@32" OC for walls <=4 ft, #4@24" OC for 4-6 ft, #5 or per engineering for >6 ft. Extends from footing through full wall height. | CRC R606.11; TMS 402 |
| 9 | **Horizontal Reinforcement** | ❌ **fail** | Bond beam with #4 rebar at top course minimum. Additional bond beams every 24" OC for walls >4 ft. Joint reinforcement (9 gauge ladder/truss type) as alternative at intermediate courses. | CRC R606.11; TMS 402 |
| 10 | **Seismic Reinforcement (SDC D)** | ❌ **fail** | Most of California is SDC D. Minimum horizontal AND vertical reinforcement each >= 0.0007 Ag, total >= 0.002 Ag. Maximum spacing 48" OC. Rebar at all corners, ends, and adjacent to openings. Unreinforced masonry NOT permitted. All cells with rebar fully grouted. | CBC 2106.1; TMS 402 Ch. 7 |
| 11 | **Footing Width & Depth** | ❌ **fail** | Continuous reinforced concrete footing required. Width increases with wall height: 12" for <=3 ft, 12-18" for 3-4 ft, 18-24" for 4-5 ft, 24-30" for 5-6 ft. Minimum 12" depth. Footing below grade: 12" minimum cover. | CRC R403; CBC 1807.1.6 |
| 12 | **Footing Reinforcement** | ❌ **fail** | Minimum 2-#4 bars continuous, placed 3" from top and bottom. Concrete: f'c >= 2,500 psi. Footing centered under wall with minimum 6" on each side. | CRC R403; ACI 318 |
| 13 | **Footing Dowels** | ❌ **fail** | Vertical dowels from footing into wall matching wall vertical rebar size and spacing. Minimum 24" embedment into footing (hooked bars) or per lap splice length. Dowels extend minimum 24" above footing into wall. | TMS 402/602 |
| 14 | **Expansion/Control Joints** | ⚠️ **flag** | Maximum spacing: 20-25 ft (TMS 402 recommendation based on L/H ratio). Also required at changes in height, thickness, direction, and at connections to buildings. Rebar does NOT cross control joints. Sealed with backer rod and elastomeric sealant. | TMS 402 |
| 17 | **Wall Cap / Top Course** | ⚠️ **flag** | Bond beam block at top course with continuous #4 rebar minimum. Cap must shed water. Options: precast concrete cap, stone cap, stucco-over-block, exposed bond beam with tooled joints. Drip edge recommended. | TMS 402; engineering practice |
| 18 | **Wind Load** | ❌ **fail** | Freestanding solid walls must resist wind per ASCE 7-22 / CBC 1609. Most of California: 110-115 mph basic wind speed. Solid walls receive full wind pressure (no solidity ratio reduction). Wind governs post/footing design for walls <=4 ft. Seismic governs for taller walls. | CBC 1609; ASCE 7-22 |
| 19 | **Property Line / Setbacks** | ⚠️ **flag** | State code does not prescribe setbacks. Cities regulate via zoning code. Common: 0 ft for side/rear, 15-20 ft in front yards, reduced height in front. Some cities require Common Property Line Wall Agreement for shared walls. Always check city overlay. | City zoning code |
| 20 | **Sight Distance Triangle** | ⚠️ **flag** | State code does not prescribe sight triangles — city/county requirement. Typical: 10x10 ft triangle at intersections/driveways, max 36" wall height within triangle. | City traffic/zoning code |
| 21 | **Contractor Licensing** | ❌ **fail** | C-29 (Masonry) required for block/masonry wall construction. B (General Building) may also perform. C-13 (Fencing) is NOT correct for masonry block walls. Workers' compensation insurance required. | B&P Code 7028 |
| 22 | **Soil Bearing** | ⚠️ **flag** | Footing must bear on undisturbed native soil or engineered fill. Minimum assumed bearing: 1,500 psf per CRC Table R401.4.1(1). Expansive soils: may require Type V cement, deeper footings, or soils report. | CRC R401.4; CBC 1803 |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 15 | **Grouting** | All reinforced cells fully grouted. Maximum lift height: 5 ft without cleanouts. Consolidate by mechanical vibration. Reconsolidate 3-5 minutes after initial pour. Maximum grout pour: 8 ft per lift (CRC R606.3.5.1). | CRC R606.3.5; TMS 602 |
| 16 | **Cleanout Openings** | Required at base of grouted cells where grout lift >5 ft (64 inches). Minimum 3" x 3" opening. Clean debris before grouting. Seal before grout placement. Walls <=4 ft: cleanouts typically not required (single lift with reconsolidation). | CRC R606.3.5.2; TMS 602 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/construction-details.md` — Block Wall Construction Details, Sequence, and Inspections
- `references/foundation-footing.md` — Block Wall Foundation and Footing Requirements
- `references/materials-specifications.md` — Block Wall Material Specifications
- `references/permit-thresholds.md` — Block Wall Permit Thresholds and Engineering Triggers
- `references/reinforcement-design.md` — Block Wall Reinforcement and Structural Design

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
