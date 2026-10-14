---
name: swimming-pool
description: "Swimming Pool/Spa permits in Laguna Beach, CA. A new pool or spa, its barrier, and its equipment. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions swimming pool in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2) — Chapter 31, Section 3109, Section 1808.7.3; 2025 California Residential Code (Title 24, Part 2.5) — Appendix CI; 2025 California Mechanical Code (Title 24, Part 4) — Chapter 8; 2025 California Electrical Code (Title 24, Part 3) — Article 680; 2025 California Plumbing Code (Title 24, Part 5) — Chapters 7, 12; California Health & Safety Code 115920-115929"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-10-10"
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
| Design review | State silent | Ord. 1732 3-ft test: portable and in-ground pools/spas **no more than 3 ft** above adjacent legal ground elevation, and portable spas of **600 gallons or less**, take **Zone Clearance** (LBMC 25.05.040(B)(2)(t)); pools/spas **more than 3 ft** above that grade (except portable spas of 600 gallons or less) take **Design Review** (25.05.040(B)(1)(j)). The City intake matrix (built-in = DRB/PC, pre-fab spa = ADR) conflicts; the ordinance governs, confirm at pre-application |
| Pool/spa equipment | State mechanical/electrical | LBMC Section 7.25.130(C) six-part objective test (effective 2026-08-20): equipment meeting all six parts is approved without Design Review (Zone Clearance); equipment failing any part goes to Administrative Design Review per Section 25.05.040(B)(3)(a)(v). Under any route the installer signs the Section 7.25.130(A) noise acknowledgment and the equipment must meet the Section 7.25.040 limits |
| Pool/spa siting | State silent | LBMC 25.50.016: pool, spa and accessory equipment not in the required front yard, and at least 5 ft from any side or required rear property line (steep-lot front exception, see §1b) |
| Oceanfront bluff | State defers to local | LBMC Section 25.50.004(B)(4): pools and spas must be no closer than 25 ft to top of bluff |
| Geotech | State project-specific | City geotech handout requires soils report for new pools on ungraded lots, floodplain areas, coastal bluff top, and other hillside/hazard conditions |
| Coastal/CDP | State Coastal Act | SFR pools can be exempt under Section 25.07.008(A)(1), but exemption is lost for bluff/beach/wetland/ESA/highly scenic areas, certain appealable-area impacts, critical water supply areas, prior CDP conditions, or landform/vegetation alteration |
| WUI/VHFHSZ | State WUI/fire code | Use the parcel's fire hazard zone from `lookup_property` (much of Laguna is VHFHSZ, not all); fuel modification, defensible space, and site fire access can affect pool/spa site work |
| Floodplain | FEMA/CBC baseline | Residential floodplain permit application applies to development involving new construction, fill, improvement, or watercourse alteration in mapped flood areas |

---

### Decision Tree Router

| Scope | Laguna Route |
|---|---|
| Pool or spa (in-ground or portable) no more than 3 ft above adjacent legal grade, or a portable spa of no more than 600 gallons at any height | Zone Clearance (25.05.040(B)(2)(t)) plus building permit; check the stacking triggers in §1 |
| Pool or spa more than 3 ft above adjacent legal grade | Design Review (25.05.040(B)(1)(j)): DRB for single-/two-family, Planning Commission otherwise (25.05.040(F)(1)) |
| Height above adjacent legal grade unknown | Establish the height above legal grade from a survey; a section dimensioned to paving or finished grade does not establish it. Until then, give the route the stated scope supports, name the Design Review branch ("moves to Design Review if the survey shows more than 3 ft"), and ask for the survey |
| Any pool/spa | Siting check: not in the required front yard, 5 ft from side and rear lines (25.50.016, §1b) |
| Pool/spa on oceanfront or bluff lot | Bluff edge determination/geotech + 25-ft pool/spa bluff setback |
| Pool/spa in coastal zone | CDP exemption analysis; do not assume exemption |
| Pool/spa on ungraded lot, bluff, floodplain, steep hillside, liquefaction zone | Geotechnical report required or likely required |
| Pool/spa equipment only | Run the Section 7.25.130(C) six-part test (effective 2026-08-20). Pass all six → Zone Clearance, no Design Review. Fail any part → Administrative Design Review per Section 25.05.040(B)(3)(a)(v). Check CDP/WUI separately if exterior work |

---

### Laguna-Specific Checks

#### 1. Design Review Routing

Urgency Ordinance No. 1732 (effective 2026-07-22) routes the pool or spa **structure** by its height above the adjacent, legal ground elevation. The City's intake matrix (zoning plan-check table) still prints built-in pool/spa = DRB/Planning Commission and pre-fab spa = Administrative Design Review. The ordinance governs; give the ordinance route, name the matrix conflict, and say "confirm with Planning at pre-application". Source: a CrossBeam reference that is not included in this plugin and `dr-tier-b2-zone-clearance.md`.

- **Zone Clearance — LBMC 25.05.040(B)(2)(t):** "Portable and in-ground swimming pools and spas no more than 3 feet above adjacent, legal ground elevation, and portable spas that do not exceed 600 gallons."
- **Design Review — LBMC 25.05.040(B)(1)(j):** "Portable and in-ground swimming pools and spas more than 3 feet above adjacent, legal ground elevation, except for portable spas that do not exceed 600 gallons." The DRB hears single-family and two-family projects; the Planning Commission hears all others (25.05.040(F)(1)).
- **Water features** are Zone Clearance (25.05.040(B)(2)(u)).

A pool that passes the 3-ft test can still land in Design Review or Administrative Design Review through another item on the closed lists. Check each one:

- environmentally sensitive area, including slopes of 30% or more, without a peer-reviewed no-impact finding → Design Review (25.05.040(B)(1)(e), (B)(2));
- grading of more than 20 cubic yards outside the building footprint → Design Review (25.05.040(B)(1)(f)). The item excepts 22.10.010(e), and Ord. 1732 § 54 added 22.10.010(e)(6): "Backfill for a swimming pool if authorized by a valid building permit" needs no grading permit, so pool backfill under the pool building permit does not count. Other site grading still counts. 22.10.010(e)(2) also exempts "An excavation for a swimming pool if authorized by a valid building permit or valid swimming pool permit", so on the plain text the pool dig does not count either. No City record rules on it directly: confirm with Planning at pre-application;
- retaining walls more than 5 ft in exposed height → Design Review (25.05.040(B)(1)(g));
- pool decks, slabs, terraces or patios more than 3 ft above adjacent legal grade → Administrative Design Review, always with a hearing (25.05.040(B)(3)(a)(iii), (B)(3)(b));
- a pool that is part of a new building or major remodel rides with that Design Review (25.05.040(B)(1)(a)-(b));
- the Director may refer a Zone Clearance project to the DRB or Planning Commission (25.05.040(A)(2)(d)).

A Coastal Development Permit may still be required (25.05.040(A)(2)(e); see §4). Ord. 1732 is local law not yet certified by the Coastal Commission; in the Coastal Zone, confirm the route with Planning at pre-application.

When a pool does go to Design Review, the reviewer applies the 11 criteria in 25.05.040(H) (for example environmental context, landscaping, privacy, view equity). The former pool-specific criterion (geology, equipment noise, compatible fencing) was not carried into Ord. 1732. Equipment noise is handled by the LBMC 7.25.040 limits and the §1a test below.

Route the pool or spa **structure** and the pool/spa **equipment** separately. The six-part test below governs equipment only. It does not change the 3-ft structure routing above.

#### 1a. Pool/Spa Equipment — LBMC Section 7.25.130(C) Six-Part Test (effective 2026-08-20)

**Authority:** LBMC Section 7.25.130, "Heating, venting, and air conditioning (HVAC) and pool/spa equipment—special provisions", as amended by Ord. 1731, the 2026 Efficiency Ordinance (adopted 2026-07-21, **effective 2026-08-20**), now codified on eCode360. Source: the codified text, mirrored in the City source document (not included in this plugin).

Pool/spa equipment in any zone that meets **all six** requirements is reviewed and approved **without Design Review**:

1. Equipment is ground-mounted, or wall-mounted at ground level.
2. Equipment is not within the required front yard setback. Ord. 1731 struck "or side", so a side yard setback does not fail this part.
3. Equipment maintains a five-foot clearance from all property lines.
4. Manufacturer's specification sheet is provided with the application and includes the decibel rating. Maximum 60 dB day / 50 dB night, measured at the property line. **Two sound attenuation techniques shall be utilized** (code examples: physical enclosures such as fencing with insulation, internal sound compression blanket, shock absorption base), used and maintained per manufacturer's specifications for the life of the equipment.
5. A city-provided form is completed detailing how the project meets the maximum sound levels measured at the property line, computed per ARI Standard 275, "Standard Application of Sound Rated Outdoor Unitary Equipment" (1984, as amended). The form's name is not yet confirmed — do not invent one.
6. Equipment does not obstruct a 3-foot path of travel around any structure.

Equipment that fails any part is reviewed per Section 25.05.040 Design Review (Section 7.25.130(D)), and appears on the Administrative Design Review list at Section 25.05.040(B)(3)(a)(v).

Before 2026-08-20 the test had five parts, applied only in or adjacent to residential areas, and part 2 also excluded the required side yard setbacks.

The side yard is still a zoning check: pool equipment may not be in a required side yard (Section 25.50.004(F)(2); in R-1, Section 25.10.008(E)(3)(a)(2)). Equipment there is a yard-conformance failure. It does not fail part 2 and does not change the design review route.

**Zone Clearance is the exempt-from-design-review path — the two framings agree.** Section 25.05.040(B)(2)(v) lists mechanical equipment meeting Section 7.25.130(c) under "Exempt from Design Review (Zone Clearance)" (urgency DR Efficiency Ordinance, effective 2026-07-22). Passing the six-part test means Zone Clearance under Section 25.05.045 plus the building permit — no hearing, no notice period.

Exception: Section 25.05.040(B)(2) bars the Zone Clearance process for listed projects in an environmentally sensitive area, unless a licensed professional determines, subject to peer review, that the development does not impact the ESA. Those go to Design Review under Section 25.05.040(B)(1).

Section 7.25.130(A) applies to pool/spa equipment permits regardless of routing: the installation contractor must sign an acknowledgment that the installation will meet the Section 7.25.040 noise limits before the permit is issued.

#### 1b. Pool/Spa Siting — LBMC 25.50.016

Verbatim (codified text; Ord. 1732 did not amend 25.50.016, it amended only 25.50.012(B)(6) in this chapter): "A swimming pool or spa and its accessory equipment shall not be located in the required front yard, nor closer than five feet from any side or required rear property line, except that on lots having a slope of twenty-five percent or greater over the rear one-half of such lots, the swimming pool or spa itself may be permitted to within ten feet of the front property line."

- Measure from the plan: the pool or spa water's edge and the equipment pad to each side and rear property line (5 ft minimum), and confirm neither sits in the zone's required front yard.
- The front-yard exception covers only the pool or spa itself, not the equipment, and only where the rear half of the lot slopes 25% or more; it then allows the pool or spa to within 10 ft of the front property line. Ask for the slope calculation on the rear half.
- The equipment also has to meet 7.25.130(C) parts 2 and 3 (§1a).
- A siting that does not meet 25.50.016 does not conform as designed. Report it as a correction (move the pool or equipment) and name the variance route (25.05.025) as the alternative; Design Review cannot waive it.

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
| LB-POOL-1 | Design review route | Pool/spa structure routed by the Ord. 1732 3-ft test: no more than 3 ft above adjacent legal grade (or portable spa of 600 gallons or less) → Zone Clearance per 25.05.040(B)(2)(t); more than 3 ft → Design Review per 25.05.040(B)(1)(j); stacking triggers (ESA, grading over 20 cy, retaining wall over 5 ft, deck over 3 ft) checked separately; pool/spa equipment routed by the Section 7.25.130(C) six-part test (effective 2026-08-20) — pass all six → Zone Clearance with no Design Review, fail any part → Administrative Design Review per Section 25.05.040(B)(3)(a)(v) |
| LB-POOL-2 | Equipment six-part test and design criteria | All six Section 7.25.130(C) parts checked by name, including the two sound attenuation techniques (part 4) and the 3-ft path of travel (part 6); contractor noise acknowledgment per Section 7.25.130(A) on file. Equipment that fails any part is routed to Administrative Design Review; geology is checked under the geotechnical triggers (check 3) |
| LB-POOL-2a | Pool/spa siting | Pool, spa and equipment outside the required front yard and at least 5 ft from side and required rear property lines; front exception (pool/spa only, to within 10 ft of the front line) only with 25%+ slope over the rear half of the lot (25.50.016) |
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
