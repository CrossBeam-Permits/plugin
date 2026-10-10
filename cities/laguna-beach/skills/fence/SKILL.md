---
name: fence
description: "Fence/Wall permits in Laguna Beach, CA. Fences, gates, and freestanding garden or privacy walls that hold no soil, at or below the local height limit. A garden wall that only encloses a yard is a fence. NOT a wall retaining soil. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions fence in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2 CBC, Part 2.5 CRC)"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2025"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Fence/Wall Permit

Handles fence/wall permits in Laguna Beach end-to-end. Scope: Fences, gates, and freestanding garden or privacy walls that hold no soil, at or below the local height limit. A garden wall that only encloses a yard is a fence. NOT a wall retaining soil.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a fence/wall permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Fence/Wall Permit

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

Note: Fence/wall rules are predominantly local — most of this skill's content represents city-specific requirements.

---

### Decision Tree Router

#### STEP 1: What Type of Wall/Fence?

| Type | Route |
|------|-------|
| **CMU block wall (standard detail)** | Use city standard detail → `references/city-block-wall-detail.md` |
| **Wood or metal fence** | OTC-eligible; survey waiver if within 3' of property line or public ROW |
| **Retaining wall** | NOT covered by standard detail → requires registered design professional |
| **Custom masonry / stone** | NOT covered by standard detail → requires engineering |

#### STEP 2: Does It Need a Permit?

| Condition | Permit Required? |
|-----------|-----------------|
| Block wall >30" height from adjacent grade | YES per City block-wall detail Note 2. LBMC 14.50.022 exempts walls/fences up to 72" (unless within 3' of property line/ROW). UNSETTLED for 31"-72" block walls: see `../block-wall/SKILL.md` |
| ANY wall/fence within 3' of property line or public right-of-way | YES |
| Any wall/fence >72" (6') | YES (LBMC 14.50.022 Building item 1) |
| Wood/metal fence ≤6' and >3' from property line and ROW | NO building permit (LBMC 14.50.022 Building item 1). Planning still applies (STEP 4) |

#### STEP 3: Additional Requirements Check

| Trigger | Requirement |
|---------|------------|
| Within 3' of property line or public ROW | Licensed surveyor must certify location BEFORE footing inspection |
| ANY wall/fence | Zoning/Planning must approve BEFORE building permit issued |
| Near fire hydrant | No wall/fence within 36" |
| Near water meter | No wall/fence/foundation within 12" |
| Wall + railing/guard/screen **built to the City standard block-wall detail** | Total height must not exceed 6'-0" above lowest adjacent grade (a limit of the standard detail, Note 13; a taller assembly needs an engineered design, not a variance) |
| Guard or railing **required by the building code** (drop over 30 in) on a wall | Permitted in any yard: "Barricades, railings and security fencing required by the building code are permitted in any yard" (LBMC 25.50.012(B)(2)). Railings are Zone Clearance (B)(2)(r). A rail or screen that is not code-required counts toward the 25.50.012(B)(1)/(3) fence height (4 ft front, 6 ft side and rear) |
| Slope >10% or adverse soil | Standard detail NOT applicable — engineer required |

#### STEP 4: Planning Route (Ord. 1732, LBMC 25.05.040(B))

No building permit does not mean no Planning approval. Source: the City source document (not included in this plugin); heights from LBMC 25.50.012(B).

| Fence/wall | Planning route |
|---|---|
| Meets 25.50.012 heights: 4 ft in the front yard (3 ft front yard on a corner lot), 6 ft in side and rear yards | Zone Clearance, 25.05.040(B)(2)(l) |
| Permanent chain link or similar woven metal fence, or vinyl that does not simulate natural material (any height) | Design Review, 25.05.040(B)(1)(m). Design Review Board on a single-family or two-family lot; Planning Commission otherwise (25.05.040(F)(1)) |
| Decorative posts or brick/stone columns up to 12 in above the front-yard limit | Administrative Design Review, 25.05.040(B)(3)(a)(vii) |
| Any fence/wall in an environmentally sensitive area (includes slopes of 30% or more) | Design Review, 25.05.040(B)(1)(e), unless a licensed professional finds, subject to peer review, no impact on the ESA |
| Taller than 25.50.012 allows | Not Zone Clearance. Needs relief from the height standard (variance, LBMC 25.05.025). Confirm with Planning |
| Pedestrian entry feature (arbor, arched entry, arcade or finials only) above the fence height, up to 8 ft high and 6 ft wide, transitions no wider than 3 ft each side | Meets 25.50.012(B)(6) as amended by Ord. 1732 § 45, which deleted "subject to design review": Zone Clearance, 25.05.040(B)(2)(l). The City intake matrix still lists "Pedestrian entry feature" as ADR; confirm with Planning at pre-application |
| Other metal (non-woven, e.g. wrought iron) fences in residential areas | 25.50.012(B)(5) still says "Chain link fences and other metal fences in residential areas are subject to design review" (not amended by Ord. 1732), but Ord. 1732 (B)(1)(m) names only chain link/woven metal and non-natural vinyl. **UNSETTLED: confirm the route with Planning at pre-application** |

The Director may refer any Zone Clearance or Administrative Design Review fence up to the Design Review Board or Planning Commission (25.05.040(A)(2)(d)). A Coastal Development Permit is a separate check under Ch. 25.07: fences on a single-family lot are normally exempt (25.07.008(A)(1)), but not where an exception applies, e.g. a new fence between the sea and the first public road or within 300 ft of the beach/mean high tide line (25.07.008(A)(1)(c)(3)), or in an ESA, highly scenic area, or within 50 ft of a bluff edge (25.07.008(A)(1)(b)).

---

### Full Review Checklist (Standard CMU Block Wall)

| # | Check | What to Verify | Reference |
|---|-------|---------------|-----------|
| 1 | Permit required? | Height >30" OR within 3' of property line or public ROW | `references/city-block-wall-detail.md` |
| 2 | Zoning approval? | Planning Division reviewed height, location, community design standards | City policy |
| 3 | Survey required? | Within 3' of property line or public ROW → surveyor must certify before footing inspection | `references/city-block-wall-detail.md` |
| 4 | Site conditions ok? | Slope <10%, no expansive soil/liquefaction/flood hazard | `references/city-block-wall-detail.md` |
| 5 | Grade equal? | Max 6" offset between sides, no surcharge loads | `references/city-block-wall-detail.md` |
| 6 | Block specs correct? | f'm ≥ 1,500 psi, Grade N, ASTM C90, running bond, solid grouted | `references/city-block-wall-detail.md` |
| 7 | Steel sizing correct? | Vertical: <4' = #4@32"OC, 4'-6' = #4@24"OC; Horizontal: #4@24"OC | `references/city-block-wall-detail.md` |
| 8 | Footing sized correctly? | Per table: 3'-4' wall = 18" or 24" footing; 5' = 24" or 30"; 6' = 30" or 36" | `references/city-block-wall-detail.md` |
| 9 | Clearances ok? | 36" from hydrant, 12" from water meter, no ROW projections | `references/city-block-wall-detail.md` |
| 10 | Expansion joints? | Max 30' spacing | `references/city-block-wall-detail.md` |
| 11 | Clean-outs? | Required for lifts >4' | `references/city-block-wall-detail.md` |
| 12 | Attachments? | On the standard detail: wall + railing/guard ≤6'-0" above lowest adjacent grade. Code-required guards are allowed in any yard (25.50.012(B)(2)); the zoning height cap does not apply to them | `references/city-block-wall-detail.md` |

---

### Key Laguna Beach Wall/Fence Facts

- **Standard detail available**: Yes — city provides pre-engineered CMU block wall detail
- **Permit trigger**: >30" height OR any height within 3' of property line or public right-of-way
- **Survey required**: Licensed surveyor must certify location before footing inspection (walls within 3' of property line or public ROW)
- **Survey waiver**: Available for wood/metal fences (not CMU) via Request to Waive Survey form. Survey waiver form requires notarization.
- **Retaining wall exemption**: Retaining walls not over 48" from footing to top are exempt from permit UNLESS supporting surcharge, impounding flammable liquids, or within 3' of property line/ROW (§14.50.022)
- **Current planning route**: see STEP 4. Zone Clearance (§25.05.040(B)(2)(l)) for fences/walls meeting §25.50.012; Design Review (§25.05.040(B)(1)(m)) for chain link/woven metal/non-natural vinyl; ESA override (§25.05.040(B)(1)(e)).
- **Zoning approval**: Required BEFORE building permit — Planning reviews height, location, design standards
- **Design criteria**: Seismic D, 95 mph basic wind speed exposure C (2025 CBC / ASCE 7-22), 1,500 psf soil bearing
- **Standard-detail CMU**: both footing alternates are 6" min, solid grouted; a partially grouted wall has left the detail and needs an engineered design
- **Inspections**: 3 required (footing, reinforcing steel, final)

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Permit Exemption** | ❌ **fail** | Fences <=7 ft are exempt from permit per state code. Retaining walls <=4 ft without surcharge are exempt. Cities may have lower thresholds — check city overlay. | CRC R105.2 |
| 2 | **Height Measurement** | ❌ **fail** | Fence/wall height measured from finished grade on the higher side. For fences on retaining walls, total combined height measured from lower grade. Where fence on top of wall, both structures must independently comply. | CRC R105.2; local practice |
| 3 | **Material Suitability** | ❌ **fail** | Wood: naturally durable species or pressure-treated (AWPA U1, Use Category 4B for ground contact). Vinyl: UV-stabilized, manufacturer wind rating. Chain link: galvanized or vinyl-coated, minimum 9 gauge. Masonry: ASTM C90 CMU; mortar selected under Table R606.2.8 / ASTM C270 by use and SDC, including Type N where permitted. Metal: galvanized, powder-coated, or corrosion-resistant. | CRC R304, R606.2; CBC 2103 |
| 4 | **Post Spacing & Size** | ❌ **fail** | Wood fence posts: typically 4x4 minimum, 6 ft to 8 ft OC maximum. Metal posts: per manufacturer specs. Post size increases with fence height and wind exposure. | Industry standard / manufacturer |
| 5 | **Post Embedment Depth** | ❌ **fail** | Minimum 1/3 of total post length below grade (rule of thumb). For 6 ft fence: minimum 24" deep. For 8 ft fence: minimum 32" deep. Concrete footings recommended: minimum 8" diameter for 4x4 post, 10" for 4x6 or 6x6. Post must extend below frost line (minimal concern in most of CA). | CBC 1807.3 |
| 6 | **Concrete Footing** | ❌ **fail** | Concrete backfill: minimum f'c 2,000 psi. Hole minimum 4" larger than post diameter. Footing should extend 1-2" above grade and slope away from post for drainage. Clean sand backfill with tamping is alternative. | CBC 1807.3.3 |
| 7 | **Wind Load** | ❌ **fail** | Fences and freestanding walls must resist wind loads per ASCE 7-22 / CBC 1609. Solid fences (board-on-board, masonry) receive full wind pressure. Open fences (chain link, wrought iron, picket) receive reduced pressure proportional to solidity ratio. Most of California: 110-115 mph basic wind speed. | CBC 1609; ASCE 7-22 |
| 8 | **Masonry/Block Wall — Materials and Bond** | ❌ **fail** | CMU: ASTM C90. Mortar: Table R606.2.8 or ASTM C270, with type selected by use and SDC under R606.2.8.1–R606.2.8.3. Use running or stack bond under R606.3.7; stack bond requires the R606.3.7.2 horizontal reinforcement. | CRC R606.2, R606.3.7 |
| 9 | **Masonry/Block Wall — Reinforcement** | ❌ **fail** | Establish the wall function, assigned SDC, thickness, bond, unit/grout construction, and loads. Where applicable, use R606.12 with Figures R606.11(1)-(3), or an approved TMS 402/403 design. Fill cells containing reinforcement solidly with grout. | CRC R606.3.5.3, R606.12; Figures R606.11(1)-(3); TMS 402/403 |
| 10 | **Masonry/Block Wall — Foundation** | ❌ **fail** | Size the footing and dowels for the wall loads, soil, assigned SDC, and applicable CRC/CBC design path. Do not use a wall-height-only footing or dowel schedule without an applicable code figure/table or fully sourced approved design. | CRC R403; CBC 1807.1.6 |
| 12 | **Retaining Wall — Permit Trigger** | ❌ **fail** | Retaining walls >4 ft from bottom of footing to top of wall require a permit. Retaining walls supporting surcharge loads (driveways, structures, slopes) require a permit regardless of height. | CRC R105.2 |
| 13 | **Retaining Wall — Engineering Required** | ❌ **fail** | Retaining walls >4 ft require design by a registered design professional (California licensed civil/structural engineer or architect). Soils report typically required. Must address overturning, sliding, bearing pressure, and water uplift. Safety factor: minimum 1.5 (1.1 with seismic). | CBC 1807.2 |
| 14 | **Retaining Wall — Drainage** | ❌ **fail** | Drainage behind retaining walls is critical. Weep holes: 4" diameter at 6-8 ft OC along base, or perforated drain pipe behind wall with outlet. Filter fabric behind gravel drain fill to prevent soil migration. Surface drainage: grade away from top of wall. | CBC 1807.2; engineering practice |
| 15 | **Retaining Wall — Guards** | ❌ **fail** | Guards required at retaining walls within 36" of walking surfaces where the drop exceeds 30" measured vertically. Guard height: 42" minimum (residential). Guard openings: <=4" sphere passage. | CBC 1807.2.5; CRC R321 |
| 16 | **Pool Barrier — Enclosure Height** | ❌ **fail** | Minimum 60 inches (5 ft) for private pool enclosures (Swimming Pool Safety Act, HS Code 115923). Public pool enclosures: minimum 60 inches effective perpendicular height (CBC 3119B.1). | HS Code 115923; CBC 3119B.1 |
| 17 | **Pool Barrier — Openings & Gaps** | ❌ **fail** | No gaps allowing passage of a 4-inch diameter sphere. Maximum ground clearance: 2 inches at bottom. Chain link: maximum 1-3/4 inch mesh openings (CBC 3119B.1). No horizontal members that could serve as ladder for children — horizontal members spaced at least 48" apart (public pools). | HS Code 115923; CBC 3119B.1 |
| 18 | **Pool Barrier — Climbability** | ❌ **fail** | Outside surface free of protrusions, cavities, or physical characteristics that enable a child under 5 to climb. No planters or climbable structures within 5 ft of outside of pool enclosure (public pools). | HS Code 115923(e); CBC 3119B.1 |
| 19 | **Pool Barrier — Gates** | ❌ **fail** | Gates open away from pool. Self-closing and self-latching required. Latch placement: no lower than 60 inches above ground (private pools per HS Code 115923). Public pools: hand hardware 42-44 inches above deck (CBC 3119B.2). Gates must be lockable when pool is closed (public). | HS Code 115923; CBC 3119B.2 |
| 20 | **Pool — Drowning Prevention Features** | ❌ **fail** | New or remodeled private pools must have at least 2 of 7 drowning prevention features: (1) code-compliant enclosure, (2) removable mesh fencing (ASTM F2286), (3) safety pool cover (ASTM F1346-23), (4) exit alarms on doors/windows, (5) self-closing/self-latching device at 54"+ on doors, (6) pool alarm (ASTM F2208), (7) other approved means. Certain combinations prohibited. | HS Code 115922 |
| 21 | **Glazing Near Pools** | ❌ **fail** | Glazing in walls, enclosures, or fences adjacent to pools where the bottom edge is less than 60" above standing surface is a hazardous location — safety glazing required (CPSC 16 CFR 1201 or ANSI Z97.1). Exception: glazing more than 60" horizontally from water's edge. | CRC R324.4.5 |
| 22 | **Property Line / Setbacks** | ⚠️ **flag** | State code does not prescribe fence setbacks from property lines. Cities regulate setbacks through zoning code. Common city requirements: 0 ft setback (on property line) for side/rear, 15-20 ft setback in front yards, reduced height in front yard (3-4 ft typical). Always check city overlay. | City zoning code |
| 23 | **Sight Distance Triangle** | ⚠️ **flag** | State code does not prescribe sight triangles — this is a city/county traffic engineering requirement. Typical: 10 ft x 10 ft triangle at intersections and driveways, maximum fence/wall height of 36 inches within the triangle. Purpose: maintain driver visibility. Always check city overlay. | City traffic/zoning code |
| 24 | **Wood Decay Protection** | ❌ **fail** | Wood fence posts in ground contact must be naturally durable species (redwood heartwood, cedar heartwood, black locust) or pressure-treated per AWPA U1, Use Category 4B. Metal post bases (Simpson, etc.) can elevate wood above grade to avoid ground contact. | CRC R304.1, R304.4 |
| 25 | **Contractor Licensing** | ❌ **fail** | C-13 (Fencing) license for fencing work. C-29 (Masonry) for block/masonry walls. B (General Building) may also perform this work. C-12 (Earthwork/Paving) for grading associated with retaining walls. Workers' compensation insurance required. | B&P Code 7028 |

### Checklist rows to place

These state rows have no current stage tag. For each one, decide from its text whether it is a plan-check item (and whether a miss is a correction or a flag) or an inspection item.

| # | Check | What to verify | Code |
|---|---|---|---|
| 11 | **Masonry/Block Wall — Control Joints** | Locate and detail control joints under the applicable current TMS provision or approved project design. Do not apply a fixed spacing without the exact standard, edition, provision, and project scope. | TMS 402/602 or approved design |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/fence-height-materials.md` — Fence Height Limits, Materials, and Installation
- `references/masonry-block-walls.md` — Masonry (CMU) Block Wall Construction Requirements
- `references/pool-barriers.md` — Pool Barrier and Enclosure Requirements
- `references/post-structural.md` — Fence Post Structural Requirements
- `references/retaining-walls.md` — Retaining Wall Requirements and Engineering Triggers

**Laguna Beach rules**

- `references/city-block-wall-detail.md` — Laguna Beach Block Wall — Standard CMU Detail

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
