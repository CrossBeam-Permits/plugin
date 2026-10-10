---
name: swimming-pool
description: "Swimming Pool/Spa permits in Laguna Beach, CA. A new pool or spa, its barrier, and its equipment. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions swimming pool in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2) — Chapter 31, Section 3109, Section 1808.7.3; 2025 California Residential Code (Title 24, Part 2.5) — Appendix CI; 2025 California Mechanical Code (Title 24, Part 4) — Chapter 8; 2025 California Electrical Code (Title 24, Part 3) — Article 680; 2025 California Plumbing Code (Title 24, Part 5) — Chapters 7, 12; California Health & Safety Code 115920-115929"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-08-24"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Swimming Pool/Spa Permit

Handles swimming pool/spa permits in Laguna Beach end-to-end. Scope: A new pool or spa, its barrier, and its equipment.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a swimming pool/spa permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Swimming Pool/Spa Permit

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
| Design review | State silent | Current §25.05.040 (Ord. 1732) routes the pool/spa structure by height: more than 3 ft above adjacent legal ground elevation → Design Review under (B)(1)(j); no more than 3 ft, or a portable spa of no more than 600 gallons → Zone Clearance under (B)(2)(t) and §25.05.045 |
| Pool/spa equipment | State mechanical/electrical | LBMC Section 7.25.130(C) six-part objective test (effective 2026-08-20): equipment meeting all six parts is approved without Design Review (Zone Clearance); equipment failing any part goes to Administrative Design Review per Section 25.05.040(B)(3)(a)(v). Ord. 1732 removed the pool/spa design criteria from §25.05.040(H); equipment noise is judged by the §7.25.130(C) test |
| Oceanfront bluff | State defers to local | LBMC Section 25.50.004(B)(4): pools and spas must be no closer than 25 ft to top of bluff |
| Geotech | State project-specific | City geotech handout requires soils report for new pools on ungraded lots, floodplain areas, coastal bluff top, and other hillside/hazard conditions |
| Coastal/CDP | State Coastal Act | SFR pools can be exempt under Section 25.07.008(A)(1), but exemption is lost for bluff/beach/wetland/ESA/highly scenic areas, certain appealable-area impacts, critical water supply areas, prior CDP conditions, or landform/vegetation alteration |
| WUI/VHFHSZ | State WUI/fire code | Most of Laguna is VHFHSZ; fuel modification, defensible space, and site fire access can affect pool/spa site work |
| Floodplain | FEMA/CBC baseline | Residential floodplain permit application applies to development involving new construction, fill, improvement, or watercourse alteration in mapped flood areas |

---

### Decision Tree Router

| Scope | Laguna Route |
|---|---|
| Pool or spa structure more than 3 ft above adjacent legal ground elevation | Design Review Board / Planning Commission under §25.05.040(B)(1)(j), using the one Design Review Application, plus building permit |
| Pool or spa no more than 3 ft above adjacent legal ground elevation, or a portable spa of no more than 600 gallons | Zone Clearance under §25.05.040(B)(2)(t) and §25.05.045, plus building permit |
| Height above adjacent legal grade unknown | Route undetermined. Establish the height from the plans before naming a route |
| Pool/spa on oceanfront or bluff lot | Bluff edge determination/geotech + 25-ft pool/spa bluff setback |
| Pool/spa in coastal zone | CDP exemption analysis; do not assume exemption |
| Pool/spa on ungraded lot, bluff, floodplain, steep hillside, liquefaction zone | Geotechnical report required or likely required |
| Pool/spa equipment only | Run the Section 7.25.130(C) six-part test (effective 2026-08-20). Pass all six → Zone Clearance, no Design Review. Fail any part → Administrative Design Review per Section 25.05.040(B)(3)(a)(v). Check CDP/WUI separately if exterior work |

---

### Laguna-Specific Checks

#### 1. Design Review Routing

Use the city zoning plan-check table and LBMC Section 25.05.040:

- **Structure more than 3 feet above adjacent legal ground elevation:** Design Review Board / Planning Commission under LBMC §25.05.040(B)(1)(j), using the one Design Review Application.
- **Structure no more than 3 feet, or a portable spa of no more than 600 gallons:** Zone Clearance under §25.05.040(B)(2)(t) and §25.05.045. The current official Zone Clearance form requires online submission; read `../../references/planning-routing.md` for the portal route. Do not promise an appointment-only process.
- **Height unknown:** the route is undetermined. Do not assume Design Review or Zone Clearance.
- **Environmentally sensitive area:** an otherwise lower-tier item goes to Design Review under (B)(1) unless a licensed professional determines, subject to peer review, that it does not impact the ESA.
- The former swimming pool, spa, and water-feature design criteria are not current §25.05.040(H) criteria under Ord. 1732. Equipment noise is handled by the §7.25.130(C) test below; geology is handled by the geotechnical triggers in check 3.

Route the pool or spa **structure** and the pool/spa **equipment** separately. The six-part test below governs equipment only. It does not change the structure route above.

#### 1a. Pool/Spa Equipment — LBMC Section 7.25.130(C) Six-Part Test (effective 2026-08-20)

**Authority:** LBMC Section 7.25.130, "Heating, venting, and air conditioning (HVAC) and pool/spa equipment—special provisions", as amended by the 2026 Efficiency Ordinance (adopted 2026-07-21, **effective 2026-08-20**). Source: the City source document (not included in this plugin) line 45.

Pool/spa equipment in or adjacent to residential areas that meets **all six** requirements is reviewed and approved **without Design Review**:

1. Equipment is ground-mounted, or wall-mounted at ground level.
2. Equipment is not within the required front or side yard setbacks.
3. Equipment maintains a five-foot clearance from all property lines.
4. Manufacturer's specification sheet is provided with the application and includes the decibel rating. Maximum 60 dB day / 50 dB night, measured at the property line. **Two sound attenuation techniques shall be utilized** (code examples: physical enclosures such as fencing with insulation, internal sound compression blanket, shock absorption base), used and maintained per manufacturer's specifications for the life of the equipment.
5. A city-provided form is completed detailing how the project meets the maximum sound levels measured at the property line, computed per ARI Standard 275, "Standard Application of Sound Rated Outdoor Unitary Equipment" (1984, as amended). The form's name is not yet confirmed — do not invent one.
6. Equipment does not obstruct a 3-foot path of travel around any structure.

Equipment that fails any part is reviewed per Section 25.05.040 Design Review (Section 7.25.130(D)), and appears on the Administrative Design Review list at Section 25.05.040(B)(3)(a)(v).

**Zone Clearance is the exempt-from-design-review path — the two framings agree.** Section 25.05.040(B)(2)(v) lists mechanical equipment meeting Section 7.25.130(c) under "Exempt from Design Review (Zone Clearance)" (urgency DR Efficiency Ordinance, effective 2026-07-22). Passing the six-part test means Zone Clearance under Section 25.05.045 plus the building permit — no hearing, no notice period.

Exception: Section 25.05.040(B)(2) bars the Zone Clearance process for listed projects in an environmentally sensitive area, unless a licensed professional determines, subject to peer review, that the development does not impact the ESA. Those go to Design Review under Section 25.05.040(B)(1).

Section 7.25.130(A) applies to pool/spa equipment permits regardless of routing: the installation contractor must sign an acknowledgment that the installation will meet the Section 7.25.040 noise limits before the permit is issued.

#### 2. Oceanfront Bluff Setback

LBMC Section 25.50.004(B)(4) states pools and spas shall be no closer than **25 ft to the top of bluff**. Require the bluff edge to be established by survey/geotech when the parcel is oceanfront or bluff-adjacent.

Do not use the 10-ft deck/patio projection rule for pools or spas. The code separately states the 25-ft pool/spa setback.

#### 3. Geotechnical Report

Laguna's geotechnical handout requires a soils report for new swimming pools when:

- Built on ungraded lots.
- Built in a floodplain area.
- Built on a coastal bluff top.

The same handout also flags steep hillside, liquefaction zone, soil/structure failure history, non-conventional foundations, and Building Official discretion.

#### 4. Coastal Development Permit

LBMC Section 25.07.008(A)(1) normally treats swimming pools as SFR-associated improvements that may be exempt, but check the exception list before clearing:

- Beach, wetland/stream, seaward of mean high tide, within 50 ft of coastal bluff edge, ESA, or highly scenic area.
- Appeal area 10% floor/height triggers or detached-structure trigger where applicable.
- Critical short water supply areas and major water-using development such as swimming pools.
- Prior CDP condition requiring future CDP.
- Significant landform alteration or vegetation removal.

#### 5. WUI / Fire Access / Fuel Modification

Pool projects can affect defensible space, vegetation, fuel modification, and fire access. Apply Laguna Ch. 14.70 and the city reference when:

- Pool is part of new construction or major remodel in fuel modification area.
- Grading/landscape work changes defensible space.
- Pool equipment or enclosures affect side-yard/fire access.
- Equipment sheds or accessory structures use exterior materials in WUI areas.

---

### Review Checklist - Laguna Swimming Pool/Spa

| ID | Check | Pass Criteria |
|---|---|---|
| LB-POOL-1 | Design review route | Pool/spa structure routed by height above adjacent legal grade — more than 3 ft → Design Review under (B)(1)(j); no more than 3 ft, or a portable spa of no more than 600 gallons → Zone Clearance under (B)(2)(t); pool/spa equipment routed by the Section 7.25.130(C) six-part test (effective 2026-08-20) — pass all six → Zone Clearance with no Design Review, fail any part → Administrative Design Review per Section 25.05.040(B)(3)(a)(v) |
| LB-POOL-2 | Equipment six-part test and design criteria | All six Section 7.25.130(C) parts checked by name, including the two sound attenuation techniques (part 4) and the 3-ft path of travel (part 6); contractor noise acknowledgment per Section 7.25.130(A) on file. Equipment that fails any part is routed to Administrative Design Review; geology is checked under the geotechnical triggers (check 3) |
| LB-POOL-3 | Bluff setback | Oceanfront/bluff pools and spas at least 25 ft from top of bluff with bluff edge established |
| LB-POOL-4 | Geotech report | Required city geotech triggers checked and report included where required |
| LB-POOL-5 | Coastal/CDP | Section 25.07.008 SFR pool exemption and exceptions documented |
| LB-POOL-6 | Floodplain | Floodplain permit application screened when in FEMA/floodway areas or involving fill/excavation |
| LB-POOL-7 | WUI/fire access | Fuel modification, defensible space, fire access, and WUI accessory-material impacts checked |
| LB-POOL-8 | State pool safety | Barrier, drowning prevention, bonding, GFCI, plumbing, suction outlet, slope setback, and structural checks completed by state skill |

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Site plan complete?** | ⚠️ **flag** | Property lines, all structures with dimensions and setbacks, proposed pool location, easements, driveways, fencing locations with heights, utility locations, north arrow, scale | CBC 107.2 |
| 2 | **Pool/spa plan details?** | ⚠️ **flag** | Structural details, dimensions, material specifications, cross-sections showing existing slopes and retaining walls to 5 ft beyond property lines | CBC 3109, 107.2 |
| 3 | **Structural calculations?** | ❌ **fail** | Required if non-standard plan. Standard plans (where approved by jurisdiction) may be exempt. | CBC 1901, 3109 |
| 4 | **Slope setback adequate?** | ❌ **fail** | Pool-to-slope setback = half the building footing setback distance. Pool wall within 7 ft horizontal of slope top must support water without soil support. Soil report required if pool is within 15 ft of slope top or 8 ft of slope toe (slope steeper than 1:3). | CBC 1808.7.3 |
| 5 | **Concrete/shotcrete specs?** | ❌ **fail** | Min f'c = 4,500 psi 28-day, Type V cement (sulfate-resistant), max w/c ratio = 0.45 per ACI 318. Special inspection required for gunite/shotcrete per CBC 1705.3, 1908. | CBC Ch. 19, ACI 318 |
| 6 | **Soil report provided (if required)?** | ❌ **fail** | Required when pool is near slopes (see item 4). Geotechnical memo confirming excavation suitability required before steel inspection. | CBC 1803.2 |
| 7 | **Barrier/enclosure compliant?** | ❌ **fail** | Min 60" high, max 2" ground clearance, no 4" sphere passage, no climbable features, gates self-closing/self-latching with latch at min 60" above ground, gates swing away from pool | HS Code 115923, CRC App. CI |
| 8 | **Drowning prevention features (2-of-7)?** | ❌ **fail** | Two different qualifying features from seven options. Certain combinations prohibited (e.g., exit alarm + door latch on same door, pool cover + pool alarm). | HS Code 115922 |
| 9 | **Safety glazing near pool?** | ❌ **fail** | Required for glazing within 60" above standing surface and within 60" horizontal of water's edge | CRC R324.4.5 |
| 10 | **Equipotential bonding grid?** | ❌ **fail** | Pool shell rebar bonded, perimeter surfaces bonded within 3 ft of pool edge, all metallic components bonded. Bonding to perimeter at min 4 points uniformly spaced. Conductor: min #8 AWG solid copper. | CEC 680.26 |
| 11 | **GFCI protection adequate?** | ❌ **fail** | All 125V receptacles within 20 ft of pool edge GFCI-protected. Receptacle required 6-20 ft from pool edge. No receptacles within 6 ft. | CEC 680.22 |
| 12 | **Underwater lighting compliant?** | ❌ **fail** | Wet-niche fixtures: GFCI-protected, max 150V, forming shell grounded to equipment grounding conductor. Low-voltage (15V or less) listed LED fixtures permitted. | CEC 680.23 |
| 13 | **Pool pump/motor wiring?** | ❌ **fail** | Disconnect within sight and min 5 ft from pool edge. Motors GFCI-protected per 680.21(C). Wiring methods suitable for corrosive environments. No aluminum conduit. | CEC 680.21, 680.13, 680.14 |
| 14 | **Pool heater compliant?** | ❌ **fail** | Gas: fuel piping under the applicable CPC route; venting under the appliance listing/manufacturer instructions and applicable CMC Chapter 8 route; Energy Code 110.4 certification. Electric: proper circuit sizing and disconnect. Cover required if an outdoor heat pump or gas heater triggers Energy Code 110.4. | CPC Ch. 12; CMC Ch. 8; CEC 680.9 |
| 15 | **Suction outlets anti-entrapment?** | ❌ **fail** | Min 2 suction outlets per pump, hydraulically balanced, min 3 ft apart. Anti-entrapment grates per ANSI/APSP-16, removable only with tools. | HS Code 115928 |
| 16 | **Drain system adequate?** | ❌ **fail** | Two return drains required -- one at bottom, one at side 2" within bottom, min 4 ft apart, with anti-vortex covers. | HS Code 115928, CPC |
| 17 | **Plumbing/filtration per code?** | ❌ **fail** | Water supply with backflow prevention, filtration system, water heater piping per CPC. All drains/grates/skimmer covers approved before installation. | CPC Ch. 7, 12 |
| 18 | **Drainage/grading adequate?** | ⚠️ **flag** | Deck and surrounding grade slope minimum 2% away from structures. Pool drainage does not increase runoff to neighboring properties. | CBC 1804.4 |
| 19 | **Erosion/sediment control?** | ⚠️ **flag** | Erosion and sediment control plan required. BMP measures during construction. NPDES compliance for dewatering. | CBC 3304.1.5 |
| 20 | **Equipment listing?** | ❌ **fail** | All pool equipment (pump, filter, heater, lighting, GFCI devices) listed and installed per manufacturer instructions. | CEC 110.3(B), CBC 3109 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/barriers-enclosures.md` — Pool Barrier, Enclosure, and Drowning Prevention Requirements
- `references/electrical-bonding-680.md` — CEC Article 680 — Swimming Pool Electrical Requirements
- `references/plumbing-filtration.md` — Pool Plumbing, Filtration, and Anti-Entrapment Requirements
- `references/structural-drainage.md` — Structural Design, Slope Setbacks, and Drainage for Swimming Pools

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
