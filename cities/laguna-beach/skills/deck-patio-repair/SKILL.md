---
name: deck-patio-repair
description: "Deck/Patio permits in Laguna Beach, CA. Repair or in-kind rebuild of an existing deck, balcony, stair, or guardrail. NOT a new or enlarged deck, which is a residential addition. NOT flatwork at grade (a slab, walkway, or patio paving), which is general-building. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions deck patio repair in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2.5 CRC, Part 2 CBC, Part 11 CALGreen); Building Division OTC policies, Ch. 14.70 WUI Code, Ch. 14.50/14.52 building/residential code amendments, Title 25 zoning/design review, Ch. 25.07 coastal development"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-10-10"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Deck/Patio Permit

Handles deck/patio permits in Laguna Beach end-to-end. Scope: Repair or in-kind rebuild of an existing deck, balcony, stair, or guardrail. NOT a new or enlarged deck, which is a residential addition. NOT flatwork at grade (a slab, walkway, or patio paving), which is general-building.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a deck/patio permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Deck/Patio Permit

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

This skill covers Laguna Beach's city-specific deck, patio, and balcony requirements. **VHFHSZ fire-resistive material requirements, design review for elevated decks, coastal zone CDP requirements, and stainless steel fastener mandates make Laguna Beach deck permits more complex than typical CA cities.**

**How this skill relates to state code**: The `california-deck-patio-repair` skill covers CRC/CBC state requirements (R507 structural, guards, handrails, stairs, ledger connections, waterproofing). This skill covers what Laguna Beach adds. **Load state code first**, then this skill.

---

### Decision Tree Router

| Project Type | Route |
|-------------|-------|
| **Deck/balcony/patio cover repair** (no extension, no replacement) | OTC eligible |
| **Deck replacement or new deck construction** | Building permit (no deck exemption in LBMC 14.50.022) + Planning route below |
| **New elevated deck >3 ft above grade, or a replacement that changes size, height or location** | Administrative Design Review, §25.05.040(B)(3)(a)(iii) |
| **Like-for-like replacement or repair of an existing elevated deck** (same size, height and location; resurfacing; new railing) | Zone Clearance, in-kind (B)(2)(c) and railings (B)(2)(r); City practice ZPC-2026-1362 (deck replaced like for like), ZPC-2026-1825 (second-floor deck repair with new guard, counter) |
| **Deck on top of a structure** (roof deck, deck over a room, garage, carport or ADU) | City Planning intake treats it as establishing Design Review; the ordinance item alone gives ADR (iii). See below |
| **Deck/slab/terrace/patio ≤3 ft above adjacent legal grade** | Zone Clearance under §25.05.040(B)(2)(m) |
| **Deck wrapping with fire-resistant materials** | Match the current closed lists; the former categorical `(B)(2)(w)` exemption was repealed |
| **Deck as part of major remodel** | Full plan review + Design Review under §25.05.040(B)(1)(a) |

---

### OTC-Eligible Deck Work

Deck, balcony, and patio cover **repairs** qualify for over-the-counter review when:
- Repair only — no extension or replacement of the deck
- No structural expansion beyond existing footprint
- Not part of a project triggering major remodel

**OTC-eligible per the city reference OTC item 2** — residential decks, balconies and patio cover repairs with minor structural modifications, no extension or replacement. Hours and the full OTC list: `../city-reference/SKILL.md` §"Permit Processing Tracks".

Deck **replacement** (tear-off and rebuild) or **new construction** does NOT qualify for OTC and requires standard plan review.

---

### Design Review Requirements for Decks

#### Exempt from Design Review — Zone Clearance

Per Section 25.05.040(B)(2):

| Improvement | Condition | Code |
|------------|-----------|------|
| **Decks, slabs, terraces, or patios ≤3 ft above adjacent legal grade** | Zone Clearance | 25.05.040(B)(2)(m) |
| **Railings** | Zone Clearance | 25.05.040(B)(2)(r) |

#### Administrative Design Review Required

Per Section 25.05.040(B)(3)(a)(iii):

- **Elevated decks MORE THAN 3 ft above adjacent existing grade** require an administrative design review hearing before the Director of Community Development
- This category cannot use the Administrative Design Review hearing waiver
- The Director may refer it to the Design Review Board or Planning Commission (25.05.040(A)(2)(d))

#### Design Review Required (public hearing)

Per Section 25.05.040(B)(1). The Design Review Board hears it on a single-family or two-family lot; the Planning Commission hears it on other lots and anywhere in the Downtown Specific Plan area (25.05.040(F)(1)(i)-(ii)):

- The deck work is part of a major remodel, (B)(1)(a)
- The work is development in an ESA (which expressly includes slopes of 30% or greater), absent the enacted peer-reviewed professional determination, (B)(1)(e)
- A deck on top of enclosed space (a roof deck, or a deck over a room or garage), including an ADU roof deck, **can** move here. Headline ADR (iii), the ordinance item, then give the two facts that could make it Design Review: City Planning intake treats a deck on top of a structure as establishing Design Review (Planning intake ruling, September 2026; no post-Ord. 1732 decision has tested it, a CrossBeam reference that is not included in this plugin section 3), and a roof guard read as a "rooftop appurtenance" with its top more than 15 ft up is (B)(1)(c) (a CrossBeam reference that is not included in this plugin Step 4f). Confirm at pre-application. An open raised deck with nothing enclosed under it is ADR (iii) at any height, never Design Review on this ground; a pool, a ground-level lounge deck or a patio cover alone does not trigger the intake rule.

The deck item (iii) governs the deck itself over the 15-ft catch-all (B)(1)(c) (specific over general, a CrossBeam reference that is not included in this plugin Step 4d). New floor area, a new story or a raised roof built with the deck is a separate piece that can still meet (B)(1)(c). An open deck more than 15 ft up is still ADR (iii); only a deck on top of enclosed space raises the Design Review question above (Step 4f).

The Director may also refer any Zone Clearance or ADR deck to the board (25.05.040(A)(2)(d)).

#### ADU-Attached Decks (Special Rules)

Per Chapter 25.17 as replaced by Urgency Ord. 1713, LBMC 25.17.020(c)(5) (Coastal Act/LCP requirements for coastal-zone ADUs; text at the City source document (not included in this plugin)):
- Covered porches, decks, patios and other outdoor living space attached to an ADU must meet the same height and setbacks as the ADU. **ADU that needs a CDP:** the certified LCP also binds it ("the ADU or JADU must comply with the requirements of the City's certified LCP", 25.17.010(d)(1)(B), Ord. 1713), so outdoor living space is also "limited to 20% maximum floor area of the ADU" (certified 25.17.040(E)(5)(c)). An ADU with no CDP has no 20% cap (Ord. 1713 dropped it).
- **Roof decks are prohibited**: "a deck above the uppermost story of a building, with no access from interior living space at the same floor level."
- The deck's own Planning route still follows the closed lists above (for example ADR if more than 3 ft above grade). For the ADU itself load `adu`.

---

### VHFHSZ Fire-Resistive Deck Requirements

Laguna Beach is predominantly Very High Fire Hazard Severity Zone (citywide coverage: `../city-reference/SKILL.md`). The WUI code applies to exterior construction including decks.

#### WUI Scope for Deck Work (Ch. 14.70)

Per Section 14.70.015, the WUI code applies to exterior materials/systems/assemblies for:
- New buildings
- Additions
- Alterations
- **Repairs**

**Exception**: With building official approval, minor repairs or replacement of exterior materials may use same materials as existing (Section 14.70.015 exception).

#### State WUI Deck Material Requirements (IWUIC 504.7.3)

In VHFHSZ, the walking surface of decks, porches, balconies, and stairs must use one of:

1. Material tested per ASTM E2632 and ASTM E2726 meeting fire performance requirements
2. Ignition-resistant building material per Section 503.2.4
3. Material meeting SFM Standard 12-7A-4 and Section 503.2.4
4. Fire-retardant-treated wood labeled for exterior use per CBC Section 2303.2
5. Noncombustible material
6. Material meeting SFM Standard 12-7A-4A (with noncombustible/ignition-resistant attached wall covering)
7. Material meeting ASTM E2632 performance (with noncombustible/ignition-resistant attached wall covering)

**CRITICAL**: Standard pressure-treated lumber (e.g., ACQ-treated Douglas Fir) does NOT automatically qualify. Decking must be ignition-resistant, fire-retardant-treated, or noncombustible, OR pass the ASTM E2632/E2726 fire tests.

#### Deck-to-Wall Flashing (IWUIC 504.7.3.1)

A minimum **6-inch metal flashing**, applied vertically on the exterior wall, is required at ALL deck-to-wall intersections. This is in addition to the CRC R507.9.1.5 ledger flashing requirements.

#### Laguna Beach WUI Amendments Affecting Decks

| Requirement | Code Section | Impact on Decks |
|------------|-------------|-----------------|
| **Exterior wall coverings** | 14.70.030 (504.5.2) | Walls adjacent to decks must be noncombustible or ignition-resistant |
| **Underfloor vent size** | 14.70.025 (504.10.4) | Vent openings into underfloor spaces (under elevated decks) max 144 sq in |
| **Minor repair exception** | 14.70.015 | Same material OK for minor repairs with building official approval |

#### Balcony Provisions for Non-Residential / Multi-Story (Ch. 14.50)

Per Section 14.50.116 (amending CBC 705.2.3.1):
- Balconies/projections of combustible construction must be fire-resistance rated per Table 601 or Type IV construction
- **Exception 1**: On Type I/II buildings <=3 stories, fire-retardant-treated wood permitted for balconies, porches, decks, and exterior stairways (not used as required exits)
- **Exception 2**: On Type III/IV/V buildings, Type V construction permitted but must comply with WUI Chapter 5 (Section 504)
- **Exception 3**: Where sprinkler protection extends to balcony areas, aggregate length limit is removed

---

### Coastal Zone Requirements

Most of Laguna Beach is in the California Coastal Zone. A Coastal Development Permit (CDP) may be required for deck work.

#### CDP Exemptions for Deck Work

Per Section 25.07.008(A):

**ESA means habitat here, not slope.** Chapter 25.07 has its own definition, and it governs the CDP questions: "For the purposes of this chapter, the following definitions shall apply: ... 'Environmentally sensitive area' means any area in which plant or animal life or their habitats are either rare or especially valuable because of their special nature or role in an ecosystem and which could be easily disturbed or degraded by human activities and development" (§25.07.006). The "slopes of 30% or greater" wording is in the Ord. 1732 Title 25 definition (§25.08.010) that drives Design Review (B)(1)(e). It is not in §25.07.006. A 30% slope alone does not make a site an ESA for the CDP exemptions. Use the ESA term below only when the parcel has habitat facts (Coastal ESA map, Biological Resource Values "Very High", a stream, or a biological assessment). A steep site still needs the full screen for its other facts (bluff edge, landform alteration).

**Deck repairs/maintenance**: EXEMPT from CDP (§25.07.008(A)(3)) unless the work is a listed exception. For a deck the main ones are:
- An addition to, enlargement, or expansion of the deck
- Shoreline protective works
- Repair or maintenance in a habitat ESA, on a sand area, within 50 ft of a coastal bluff edge or of a habitat ESA, or within 20 ft of coastal waters or streams, where it involves placing or removing solid materials or using mechanized equipment or outdoor storage of construction materials (§25.07.008(A)(3)(d))

**SFR deck improvements**: EXEMPT from CDP unless:
- Located on a beach, in a wetland/stream, seaward of mean high tide, within 50 ft of coastal bluff edge, in a habitat ESA (§25.07.006; not slope alone), or in highly scenic area — per 25.07.008(A)(1)(b)
- In the coastal appealable area (between sea and first public road, or within 300 ft of beach/mean high tide) AND the improvement results in >=10% floor area increase or >=10% height increase — per 25.07.008(A)(1)(c)
- A new detached structure (new freestanding deck could qualify) — per 25.07.008(A)(1)(c)(3)

#### CDP Required

A CDP IS required when:
- Building a new freestanding deck in the coastal appealable area
- Deck addition increases floor area by >=10% in the coastal appealable area
- Any deck work within 50 ft of a coastal bluff edge
- Deck improvements in a habitat ESA (§25.07.006 definition; a 30% slope alone does not count), and repair/maintenance there that meets §25.07.008(A)(3)(d)

---

### Major Remodel Interaction

Deck work itself is NOT directly measured in the major remodel 50% calculation (which measures foundation LF, wall LF, and roof SF). However:

#### Sprinkler Retrofit Trigger

**Two triggers, either one fires.** See `../residential-remodel/references/city-sprinkler-retrofit.md` — the single residential retrofit reference. Do not restate the rule here.

- **Ch. 14.52.030** (valuation) — cumulative additions, alterations and repairs in any three-year period exceeding 50% of the pre-work valuation.
- **Title 15 §1103.5.4** (scope) — alteration of ≥50% of the building, OR an added story. Whether work on ≥50% of the exterior fires it by itself is UNSETTLED (two readings in the reference; confirm with Building and Fire at pre-application).

**Deck-specific note.** Deck replacements can be high-value work, and deck valuation counts toward the Ch. 14.52.030 three-year cumulative total. A deck also sits on the building exterior, so a large deck rebuild combined with other exterior scope can feed the §1103.5.4 exterior tally. That prong is UNSETTLED; if it alone decides the answer, give both readings. Check both triggers.

#### Major Remodel (Area-Based)

- Whether the whole project is a major remodel is decided by the October 2026 Major Remodel Quick Guide method in `../residential-remodel/references/city-major-remodel-methodology.md` (exterior walls / structural elements removed or reinforced, and additions over 50% since January 13, 1993). Do not restate it here.
- A major remodel is Design Review under 25.05.040(B)(1)(a) (Design Review Board for a house or duplex), with Fire Safety Standards Review (25.05.040(C)(4)), and is treated as a new building for current zoning standards (25.56.011)

---

### Stainless Steel Fasteners

Per CRC Table R507.2.3 note b: "Fasteners and connectors exposed to salt water or located within 300 feet of a salt water shoreline shall be stainless steel."

The rule turns on distance to the salt-water shoreline. Oceanfront and near-shore lots are within 300 ft; most hillside and canyon lots are not. Measure or ask; do not assume either way. Outside 300 ft, the table's other options (hot-dip galvanized and the like) apply.

**This affects**: nails, screws, bolts (including nuts and washers), metal connectors, joist hangers, post bases, ledger hardware, and guard post connectors.

---

### Hillside / Geotechnical Considerations

Many Laguna Beach properties are on hillsides with challenging geology:

- **Steep slopes (≥30%)**: Included in the Ord. 1732 Title 25 ESA definition (§25.08.010); apply §25.05.040(B)(1)(e) unless a licensed professional determines, subject to peer review, that the work does not impact the ESA. This is a Design Review rule only. It does not defeat a CDP exemption: Ch. 25.07 defines ESA by habitat (§25.07.006)
- **Deck foundations on hillsides**: May require geotechnical report for soil bearing capacity, slope stability, and foundation recommendations
- **Elevated deck posts**: Posts on hillside properties may have significant height — verify against CRC R507.4 post height limits (max 14 ft for 4x4 under 40 psf)
- **Lateral loads on hillside decks**: Additional engineering may be required for decks cantilevered from hillside structures

---

### Submittal Requirements for Deck Projects

Per city zoning plan check standards, a deck addition requires:
- Application forms
- Title sheet
- Survey
- Site plan
- Roof plan
- Elevations
- Cross sections
- Floor area calculations
- Open space calculations

Additional submittals depending on scope:
- Structural calculations (if elevated deck, hillside, or engineer-designed)
- Geotechnical report (if hillside property)
- WUI compliance documentation (materials certification for VHFHSZ)
- CDP application (if in coastal zone and not exempt)
- Design review application (if elevated deck >3 ft)

---

### Key Laguna Beach Deck Facts

- **OTC eligible**: Deck/balcony/patio cover REPAIRS only (no extension/replacement)
- **Zone Clearance (no hearing)**: Decks/patios 3 ft or less above adjacent legal grade (B)(2)(m), railings (B)(2)(r), in-kind repair (B)(2)(c). WUI deck wrapping has no categorical exemption any more; route it by these lists
- **Administrative Design Review**: Decks more than 3 ft above adjacent legal grade, (B)(3)(a)(iii); hearing cannot be waived
- **Building permit**: Laguna's exemption list (LBMC 14.50.022, applied to homes by 14.52.014 / CRC R101.4) has no deck or platform exemption. Treat any new or replacement deck as needing a permit; see a CrossBeam reference that is not included in this plugin
- **Fire-resistive decking**: Required in VHFHSZ per IWUIC 504.7.3
- **Stainless steel fasteners**: Required within 300 ft of a salt-water shoreline or where exposed to salt water (CRC Table R507.2.3 note b); check the lot's distance
- **CDP**: Required in coastal zone unless exempt (repairs/maintenance with no expansion are generally exempt). Slope alone does not remove the exemption
- **Sprinkler trigger**: Two triggers — Ch. 14.52.030 (deck valuation counts toward the 50% / 3-year cumulative total) and Title 15 §1103.5.4 (scope). Either fires. See `../residential-remodel/references/city-sprinkler-retrofit.md`
- **Underfloor vents**: Max 144 sq in per opening under elevated decks (Ch. 14.70.025)
- **Hillside lots (slope 30% or more)**: ESA, so Design Review under (B)(1)(e) unless a peer-reviewed licensed professional finds no impact; potential geotech report
- **ADU decks**: Same height and setbacks as the ADU; roof decks prohibited (Urgency Ord. 1713)

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Permit Exemption** | ❌ **fail** | Verify project does not qualify for exemption per CRC R105.2. If exempt, no further review needed. If deck exceeds 200 sq ft, is more than 30" above grade, is attached to dwelling, or serves an egress door, permit IS required. | CRC R105.2 |
| 2 | **Footings & Foundations** | ❌ **fail** | Footings required for all decks except: (a) joists directly on grade over entire length, or (b) freestanding decks <=200 sq ft with joists on precast pier blocks at grade, walking surface <=20" above grade. Min footing depth 12" below undisturbed ground. Footing size per Table R507.3.1 based on tributary area and soil bearing capacity. Frost protection required for decks attached to frost-protected structures. | CRC R507.3, R507.3.1, R507.3.2, R507.3.3 |
| 3 | **Posts** | ❌ **fail** | Post size per Table R507.4 based on species, tributary area, and height. Max post height 14 ft for single-level decks. Post-to-footing connection: approved connectors or min 12" embedment in soil or concrete pier. 4x4 posts supporting guard loads shall NOT be notched at guard connection. | CRC R507.4, R507.4.1, R507.10.2 |
| 4 | **Beams** | ❌ **fail** | Beam spans per Tables R507.5(1) through R507.5(4) based on joist span, live load, and species. Beam plies fastened with two rows of 10d nails at 16" OC. Beam bearing: min 1-1/2" on wood/metal, min 3" on concrete/masonry. Beam cantilever limited to 1/4 of adjacent beam span. Post-to-beam connection per Figures R507.5.2(1) and R507.5.2(2). | CRC R507.5, R507.5.1, R507.5.2 |
| 5 | **Joists** | ❌ **fail** | Joist spans per Table R507.6 based on species, size, spacing, and load. Max cantilever per Table R507.6. Joist bearing: min 1-1/2" on wood/metal, min 3" on concrete/masonry. Lateral restraint at joist ends required (hangers, blocking, or rim joist). Rim joist to joist: min three 10d nails or three No. 10 x 3" screws. | CRC R507.6, R507.6.1, R507.6.2 |
| 6 | **Decking** | ❌ **fail** | Max joist spacing per Table R507.7 based on decking thickness and orientation. 1-1/4" wood perpendicular: 16" max (multi-span). 2" wood perpendicular: 24" max. Diagonal decking reduces max spans. Each board attached with min two 8d deformed shank nails or two No. 8 screws per support. Plastic composite decking per R507.2.2 with labeling, flame spread <=200, and decay resistance. | CRC R507.7, R507.2.2 |
| 7 | **Ledger Connection** | ❌ **fail** | Ledger min 2x8 nominal, No. 2 grade or better, pressure-treated or naturally durable. Lag screw or bolt spacing per Table R507.9.1.3(1). Lag screws: 1/2" diameter, pre-drilled 1/2" through ledger, 5/16"-3/8" through band joist. Band joist: min 2" nominal solid-sawn SPF or better, or min 1" engineered rim board. Bolt placement per Table R507.9.1.3(2): top edge 2", bottom edge 3/4", ends 2", row spacing 1-5/8" to 5". Ledger shall NOT bear on stone or masonry veneer. Ledger shall NOT support concentrated loads from beams. | CRC R507.9, R507.9.1, Table R507.9.1.3(1), Table R507.9.1.3(2) |
| 9 | **Lateral Load Connection** | ❌ **fail** | Lateral loads must transfer to ground or supporting structure. Hold-down tension devices: min 2 per deck within 24" of each end, each with ASD capacity >= 1,500 lb (per Figure R507.9.2(1)). Alternate: min 4 devices, each >= 750 lb ASD capacity (per Figure R507.9.2(2)). Attachment NOT permitted by toenails or nails subject to withdrawal (CRC R318.5). | CRC R507.9.2, R507.8, R318.5 |
| 10 | **Guards (Guardrails)** | ❌ **fail** | Required where walking surface is >30" above grade (measured within 36" horizontally of open edge). Height: min 42" measured vertically from walking surface. On open stair sides: min 34" from nosing line, or 34"-38" if top rail serves as handrail. Baluster spacing: no opening allows passage of 4" sphere. Stair triangle exception: 6" sphere at triangular opening formed by riser, tread, and bottom rail. Floor framing supporting guards per R502.11. | CRC R321.1.1, R321.1.2, R321.1.3, R507.10, R502.11 |
| 11 | **Handrails** | ❌ **fail** | Required on at least one side of stairs with 4 or more risers. Height: 34"-38" measured from nosing line. Grip size Type I: circular 1-1/4" to 2" OD, or non-circular perimeter 4" to 6-1/4" with max cross-section 2-1/4". Type II: perimeter >6-1/4" with graspable finger recess. Continuous for full flight length. Returned to wall, guard, or walking surface. Wall clearance: min 1-1/2". Max projection into stair: 4-1/2". Plastic composite handrails per R507.2.2. | CRC R320.1-R320.7, R318.7.8 |
| 12 | **Stairs** | ❌ **fail** | Riser height: max 7-3/4". Tread depth: min 10". Rise/run uniformity: max 3/8" variation within a flight. Stair width: min 36" clear above handrail, min 31-1/2" at/below one handrail, min 27" between two handrails. Headroom: min 6'-8". Max vertical rise per flight: 12'-7". Nosing: 3/4" to 1-1/4" projection. Open risers >30" above grade: no 4" sphere passage. Landing at top and bottom: min 36" depth in direction of travel. Bottom landing for exterior stairs to grade with <=3 risers: min 36" wide (if not serving egress door). Walking surface slope: max 2%. | CRC R318.7.1-R318.7.7 |
| 13 | **Decay Protection** | ❌ **fail** | All wood structural members exposed to weather without adequate roof/eave protection must be naturally durable or pressure-treated (CRC R304.1 Item 8). Ground contact wood: pressure-treated per AWPA U1 for ground contact use (R304.1.2). Field-cut ends treated per AWPA M4 (R304.1.1). Quality mark required showing treating plant, preservative type, retention, end use, standard, and inspection agency (R304.2). Sawn lumber for joists/beams/posts: No. 2 grade or better (R507.2.1). | CRC R304.1, R304.1.1, R304.1.2, R304.2, R507.2.1 |
| 14 | **Fasteners & Connectors** | ❌ **fail** | All metal fasteners for decks per Table R507.2.3 and R304.3. Nails: hot-dipped galvanized per ASTM A153 Class D, or stainless steel, silicon bronze, copper. Bolts: hot-dipped galvanized per ASTM A153 Class C/D, or mechanically galvanized per ASTM B695 Class 55, or stainless steel. Metal connectors: ASTM A653 type G185 zinc-coated or post hot-dipped per ASTM A123. Within 300 ft of salt water: stainless steel required. Through-bolt holes drilled 1/32" to 1/16" larger than bolt diameter. | CRC R507.2.3, R304.3, Table R507.2.3 |
| 15 | **Waterproofing (Elevated Decks)** | ❌ **fail** | Where decks are over habitable space: wood structural members supporting moisture-permeable floors exposed to weather must be protected or separated by impervious moisture barrier with positive drainage (R304.1 Item 6). Enclosed framing in exterior balconies exposed to rain/snow: net-free ventilation area >= 1/150 of each separate space (R304.1.3). Flashing: corrosion-resistant metal >= 0.019" or approved non-metallic, compatible with substrate (R507.2.4). | CRC R304.1, R304.1.3, R507.2.4 |
| 16 | **Attachment to Structure** | ❌ **fail** | Exterior decks, balconies, stairs, and landings must be positively anchored to primary structure for vertical AND lateral forces, or designed as self-supporting. Attachment NOT by toenails or nails subject to withdrawal. Where positive connection cannot be verified during inspection, deck must be self-supporting. Cantilevered framing connections must resist uplift from full live load on cantilever. | CRC R318.5, R507.8 |
| 17 | **Contractor Licensing** | ❌ **fail** | C-5 (Framing and Rough Carpentry), B (General Building), or A (General Engineering for larger projects) license required. Workers' compensation insurance required. | B&P Code 7028 |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 8 | **Ledger Flashing** | Flashing installed above ledger, extending min 2" vertically above ledger. Horizontal extension: min 4" beyond ledger face OR to ledger face plus 1/4" down. Water-resistive barrier lapped over vertical leg by min 2". Existing walls without WRB: install WRB behind ledger and flashing with self-adhered counterflashing. Exterior wall coverings terminated above deck surface. Flashing not required if ledger spaced 1/4" from wall for drainage/ventilation. | CRC R507.9.1.5, R507.9.1.6, R507.9.1.7, R507.9.1.8 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/deck-structural.md` — Deck Structural Requirements
- `references/guards-handrails.md` — Guards and Handrails
- `references/ledger-connections.md` — Ledger Connections
- `references/stairs-requirements.md` — Stair Requirements
- `references/waterproofing-drainage.md` — Waterproofing and Drainage

**Laguna Beach rules**

- `references/city-design-review-decks.md` — Laguna Beach — Current Deck and Patio Planning Route
- `references/city-wui-decking.md` — Laguna Beach WUI Code — Fire-Resistive Deck & Exterior Construction Requirements

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
