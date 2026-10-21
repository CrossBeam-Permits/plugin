---
name: city-reference
description: "Laguna Beach, CA city reference: codes adopted, climatic and seismic design criteria, the fire, coastal, design review, hillside and historic layers, sprinkler retrofit triggers, permit processing tracks, permit expiration, construction hours, and division contacts. Use for general Laguna Beach permit questions that are not about one permit type, or when a permit skill points here."
metadata:
  version: "2.0"
  source: "City of Laguna Beach municipal code and Community Development publications"
  authority: "City of Laguna Beach"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — City Reference

Cross-cutting city facts that every permit skill in this plugin relies on. Permit-specific rules live in each permit skill.

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

Cross-cutting city information for all permit types. This document provides baseline data that any permit-type skill can reference when reviewing plans or permits in Laguna Beach.

---

## Jurisdiction Info

| Field | Value |
|-------|-------|
| **City** | City of Laguna Beach |
| **County** | Orange County, CA |
| **Municipal Code Source** | https://ecode360.com/LA4953 |
| **Permit Portal** | Tyler EnerGov CivicAccess — lagunabeachca-energovweb.tylerhost.net |
| **Building Department** | Community Development — Building Division |
| **City Website** | https://lagunabeachcity.net |
| **Phone** | (949) 497-0715 |
| **Code Adoption Contact** | the Building Official (CBO) — (949) 497-0719 |
| **Inspection Email** | lbinspectors@lagunabeachcity.net |
| **Address** | City Hall, 505 Forest Ave, Laguna Beach, CA 92651 |

---

## Construction Codes Adopted (Effective January 1, 2026)

Laguna Beach has adopted the **2025 edition** of all California Building Standards Codes:

| Code | Edition | Base Code |
|------|---------|-----------|
| California Building Code (CBC) | 2025 | 2024 IBC |
| California Residential Code (CRC) | 2025 | 2024 IRC |
| California Fire Code | 2025 | 2024 IFC |
| California Wildland-Urban Interface Code | 2025 | 2024 IWUIC |
| California Green Building Standards | 2025 | -- |
| California Existing Building Code | 2025 | 2024 IEBC |
| California Plumbing Code | 2025 | 2024 UPC |
| California Mechanical Code | 2025 | 2024 UMC |
| California Electrical Code | 2025 | 2023 NEC |
| California Energy Code | 2025 | 2024 IECC |

### Building-application code-cycle table

The California Building Standards Commission says the 2025 cycle applies to building-permit applications received on or after 2026-01-01, and the 2022 cycle to applications received on or before 2025-12-31. The date that counts is the date the City received the building application, not a date typed on the form or a Planning filing date.

Sources: [CBSC Information Bulletin 25-01](https://www.dgs.ca.gov/-/media/Divisions/BSC/06-News/Information-Bulletins/2025/BSC-Bulletin-25-01-FINAL.pdf),
[CBSC code history](https://www.dgs.ca.gov/en/BSC/About/History-of-the-California-Building-Standards-Code---Title-24).

## Climatic and Geographic Design Criteria

| Parameter | Value |
|-----------|-------|
| **Seismic Design Category** | **D** (high seismic) |
| **Basic Wind Speed** | **95 mph** |
| **Topographic Effect** | **No** |
| **Special Wind Region** | **No** |
| **Windborne-Debris Zone** | **No** |
| **Ground Snow Load** | Zero |
| **Climate Zone (Title 24 Energy)** | **Zone 6** (Southern CA Coast) |
| **Fire Hazard Severity Zone** | **Parcel-specific** — use the adopted 2025 LRA map; see the adopted-map baseline below |
| **Wildland-Urban Interface** | Yes — Ch. 14.70 adopted with extensive local amendments |
| **Coastal Zone** | **Most of city** — California Coastal Act applies |
| **Flood Zone** | Portions in FEMA flood zones — NFIP participation |
| **Sprinklers Required (new construction)** | **Yes — ALL 1&2-family dwellings + attached garages** (Ch. 14.52.030 local amendment of CRC R309.2) |
| **Sprinkler Retrofit Trigger (existing 1&2-family)** | **Two independent triggers — either one fires.** Ch. 14.52.030 (valuation: cumulative additions/alterations/repairs in any 3-year period > 50% of pre-work valuation) **and** Title 15 §1103.5.4 (scope: alteration of 50% of the building OR an added story; whether 50% exterior work alone fires it is UNSETTLED, see the sprinkler reference). CBC-track Group R and non-residential occupancies must also be checked under §14.50.104/§903.6. |
| **Mean Annual Temperature** | ~60 degrees F |
| **Frost Line Depth** | None |
| **Termite Damage** | Very Heavy |

The City's 2026 jurisdictional data sheet records adopted **CRC Appendices BH and CI**
and **CBC Appendices G, H, I and J**.

---

## Critical Laguna Beach Layers (What Makes This City Different)

### 1. Very High Fire Hazard Severity Zone (VHFHSZ)
- **Adopted-map baseline (parcel-specific):** CrossBeam's 2026-08-18 parcel-intersection audit found **7,393 of 11,302 addressed parcels** in the Very High tier of the 2025 LRA map. The City states that Council adopted that recommended map on 2025-06-24 ([City FHSZ map and adoption page](https://www.lagunabeachcity.net/government/departments/fire/fire-prevention/new-lra-fhsz-maps-for-public-comments)). Determine each site from that adopted map; never infer VHFHSZ from a citywide percentage or a legacy City viewer.
- **Mandatory residential sprinklers (new construction)** on ALL 1&2-family dwellings AND attached garages (Ch. 14.52.030, amending CRC R309.2). Garage within 10 feet counts as "attached."
- **Sprinkler retrofit (existing buildings)** has **two independent triggers on a one- or two-family dwelling, and either one requires the retrofit**: (1) **Ch. 14.52.030** — valuation: cumulative additions, alterations and repairs in any three-year period exceed 50% of the pre-work valuation of the dwelling and attached garage; (2) **Title 15 §1103.5.4** — scope: alteration of 50% or more of the building, or the addition of one or more stories (whether work on 50% or more of the exterior fires it on its own is UNSETTLED; confirm with Building and Fire at pre-application), with one carve-out for "work that consists only of the installation of fire-resistant siding." See §"Sprinkler Retrofit Triggers" below and `../residential-remodel/references/city-sprinkler-retrofit.md`.
- Sprinkler systems must be per NFPA 13D with flow switch activating exterior alarm + interconnected interior smoke detectors (Ch. 14.52.031)
- NFPA 13D systems with a separate control valve require central/proprietary/remote-station supervision. The blanket **24-hour UL-certified central-station** mandate in Title 15 §15.01.070 applies to NFPA 13R systems, not every NFPA 13D system.
- Wildland-Urban Interface Code (Ch. 14.70) has extensive local amendments:
  - **Class A roof required** for ALL roofs and re-roofs (§14.70.020)
  - Exterior wall coverings must be noncombustible or ignition-resistant (§14.70.030)
  - Vinyl windows require welded corners + metal reinforcing (§14.70.035)
  - **No plastic skylights** — glass only (§14.70.040)
  - Vent openings max 144 sq in (§14.70.025)
  - Defensible space per the **2019 LBFD Landscape/Fuel Modification Standards and Maintenance Program** (L/FMSMP) (§14.70.060)
  - Fuel modification plans required for new construction/major remodels (§14.70.070)

### 2. Coastal Zone
- Most of the city falls within the California Coastal Zone
- **Coastal Development Permit (CDP)** required for development in the Coastal Zone unless the work is exempt or excluded under Ch. 25.07
- Separate application from the building permit. Zone Clearance, Administrative Design Review and Design Review never replace it (LBMC 25.05.040(A)(2)(e), 25.05.045(C)(4))
- May require California Coastal Commission review/appeal
- Bluff edge determinations required for coastal bluff properties

### 3. Design Review / Zone Clearance — current Ord. 1732 routing

Urgency Ordinance No. 1732 replaced the former exterior-work default with three closed lists: 16 Design Review categories, 28 Zone Clearance categories, and 17 Administrative Design Review categories. Do not infer discretionary review merely because work is exterior.

- Design Review hearings route by project type under §25.05.040(F)(1): the **Design Review Board** hears single-family and two-family developments (with their right-of-way work); the **Planning Commission** hears everything else, including three or more units, all Downtown Specific Plan projects, non-residential projects, public works, and projects where the Commission is the primary authority (such as a CUP). **The Design Review Board meets the 2nd and 4th Thursday of the month at 5:00 p.m. in the City Council Chambers, with a few exceptions.** [source: City of Laguna Beach, "How are building permits processed," as of 2026-06-18 — `../city-website/references/planning-applications.md`] This is the single home for the DRB meeting schedule.
- Zone Clearance is issued by the Community Development Department under new §25.05.045.
- Administrative Design Review is decided by the Director/designee; most categories may use the conditional 15-working-day notice/comment hearing-waiver procedure.
- Development in an ESA—including slopes of 30% or greater—cannot use Zone Clearance/ADR absent the enacted peer-reviewed professional determination.
- A CDP may still be separately required.
- Appeals are filed within 14 calendar days. **This is the canonical citywide summary for the notice day-counts:** §25.05.065(D) sets mailed hearing notice at 21 days minimum for Design Review and 14 days minimum for Administrative Design Review; applicable staking independently uses the same respective periods. §25.05.065(E) requires posting in three public places including the site at least 10 calendar days before hearing. Operational routing references may repeat a deadline where the check depends on it; they must cite the current section rather than invent a shared footer value.

Use `../residential-remodel/references/city-design-review-tiers.md` for the current routing matrix.

### 4. Hillside / Geology
- Many properties on hillsides require **geotechnical reports**
- Specific geology report requirements per city standards
- Slope stability, soil bearing capacity, foundation recommendations

### 5. Historic Resources
- A **historic resource** is defined by LBMC 25.45.004 (as amended by Ord. 1732): City register, California or National Register listing or official eligibility, or CEQA substantial evidence. Age alone does not make a property historic, and the older inventory creates no presumption (25.45.002(H)).
- Work on a historic resource goes to Administrative Design Review (minor, 25.05.040(B)(3)(a)(iv)) or Design Review (major, (B)(1)(d)), with a **Heritage Committee** recommendation first (25.45.010)
- The Director may require a historic resource assessment (25.45.010(C)); an inventory rating in site facts flags it
- Heritage Register placement process (25.45.006). Resident guide: `../guide/references/historic-properties.md`

---

## Permit Exemptions (CBC §105.2 as amended)

The following work does NOT require a building permit:
- Walls and fences ≤72" high (UNLESS within 3' of property line or public ROW)
- Retaining walls ≤48" from footing to top (UNLESS supporting surcharge, impounding flammable liquids, or within 3' of property line/ROW)
- Painting, papering, tiling, carpeting, cabinets, counter tops, similar finish work
- Window awnings on R-3/U occupancy (≤30" projection, no additional support)
- Temporary on-grade removable storage structures to SFR (≤120 sf, <12' above grade)
- Non-fixed movable fixtures/cases/racks/counters/partitions ≤5'9"
- Minor electrical repairs, lamp replacement, connection of portable equipment
- Portable gas heating appliances, minor gas parts replacement
- Portable mechanical appliances, ventilating equipment for single dwelling

---

## Sprinkler Retrofit Triggers — classify the building, then run every applicable trigger

Laguna Beach amended both the Residential Code (Ord. 1725) and the Fire Code (Ord. 1726) on
12/18/2025. An existing **one- or two-family dwelling** therefore has **two independent retrofit
triggers**. One measures money, the other measures scope. **Either one firing requires the full
retrofit.** CBC-track Group R buildings also run §14.50.104/§903.6(1),(5); occupancies other
than Group R or U use the conditional §903.6(2) test. Classify the building first, then run every
trigger that applies to it.

| # | Trigger | Basis | Applies to | Test | Ordinance |
|---|---------|-------|-----------|------|-----------|
| 1 | **LBMC Ch. 14.52.030** (amends CRC R309.2) | **Valuation** | One- and two-family dwellings + garage attached (within 10 ft) | Cumulative value of additions, alterations and repairs in **any three-year period** exceeds **50% of the valuation before the work** | Ord. 1725, 12/18/2025 |
| 1a | **LBMC Ch. 14.52.026** (amends CRC R309.1) | **Valuation** | Townhouses + attached garage; each townhouse is a separate building | Same 50% / three-year test | Ord. 1725, 12/18/2025 |
| 2 | **LBMC Title 15 §1103.5.4** (adds CFC Ch. 11 §1103.5.4) | **Scope** | ALL existing Group R fire areas | Alteration of 50% or more of the building, OR addition of one or more stories. Exterior work of 50% or more as a standalone prong is UNSETTLED (two readings) | Ord. 1726, 12/18/2025 |
| 3 | **LBMC §14.50.104** (amends CBC §903.6) | **CBC retrofit tests** | CBC-track Group R; other-than-R/U occupancies; additions to already-sprinklered buildings; large additions | Group R: ≥50% valuation, plus a separate substantial-renovation test. Other-than-R/U: post-work building must require sprinklers **and** valuation must reach ≥50%. The section also has addition-specific triggers. Cumulative valuation uses any three-year period. | Ord. 1725, 12/18/2025 |

**Triggers 1 and 2 are different tests that share the number 50.** Trigger 1 compares dollars.
Trigger 2 compares physical scope. A project can fire one and not the other. Run both on every
existing one- or two-family dwelling. Do not merge them, and do not confuse either with the LCP
**major-remodel** 50% rule in `../residential-remodel/references/city-major-remodel-methodology.md`
— that rule sets Design Review and CDP tier, not sprinklers.

Single residential reference:
`../residential-remodel/references/city-sprinkler-retrofit.md`.

### Trigger 1 — Ch. 14.52.030 (valuation, one- and two-family)

Verbatim from the City source document (not included in this plugin) §14.52.030
(Ord. 1725, 12/18/2025):

> **R309.2 One- and two-family dwellings automatic sprinkler systems.** An automatic residential
> fire sprinkler system shall be installed in one- and two-family dwellings and garages attached
> to one- and two-family dwellings. A garage is considered attached for the purposes of this
> subsection if it is within ten feet of the one- or two-family dwelling. If the cumulative value
> of additions, alterations and repairs done to a one- or two-family dwelling and attached garage
> in any three-year period exceeds fifty percent of the valuation of the one- or two-family
> dwelling and attached garage prior to the additions, alterations, and repairs, the entire one-
> or two-family dwelling and attached garage must be sprinklered throughout. The valuation used
> for the existing building and for the additions, alterations, and repairs is the valuation
> established in the City's resolution for computation of building permit fees. For the purposes
> of this subsection, firewalls, fire barriers, or fire partitions shall not define separate
> buildings or fire areas.

The same section mandates sprinklers in **new** one- and two-family dwellings and attached
garages. Both duties live in one section: new construction, and the valuation retrofit.
Valuation comes from the City's building-permit fee resolution, not from an appraisal or a
contract price. Ch. 14.52.026 states the identical rule for townhouses.

### Trigger 2 — Title 15 §1103.5.4 (scope, all Group R)

Verbatim from the City source document (not included in this plugin) §15.01.040
(Ord. 1726, 12/18/2025):

> **Section 1103.5.4 Group R.** An automatic sprinkler system installed in accordance with
> Section 903.3 shall be provided throughout all existing Group R fire areas when work requiring
> a building permit that involves alteration of 50 percent or more of a building, which includes
> or involves work on 50 percent or more of the building's exterior, or which involves the
> addition of one or more stories.
>
> **Exception:** Work that consists only of the installation of fire-resistant siding.

Two prongs fire the retrofit on any reading:

1. Alteration of 50% or more of the building — the major-remodel methodology in
   `../residential-remodel/references/city-major-remodel-methodology.md` is the operational test; OR
2. Addition of one or more stories (whether a new basement or lower level counts is UNSETTLED; see the reference).

Whether work on 50% or more of the building's exterior fires the retrofit **by itself** is
**UNSETTLED**. The "which includes or involves" clause can be read as part of the 50%-alteration
prong or as its own prong. The City has not ruled. When exterior work alone decides the answer,
give both readings and say "confirm with Building and Fire at pre-application". The two readings
are in `../residential-remodel/references/city-sprinkler-retrofit.md` (Trigger B).

The exception is narrow. It covers work that consists **only** of installing fire-resistant
siding. Add any other scope and the exception is gone.

### Trigger 3 — LBMC §14.50.104 (CBC §903.6, CBC-track buildings)

Do not describe §14.50.104 as non-residential-only: its first and fifth clauses expressly apply
to **Group R**. For a CBC-track Group R building (including 3+ unit multi-family), sprinklers are
required when additions, alterations or repairs reach at least 50% of the pre-work building
valuation, or when the Building Official finds a substantial renovation whose installation
complexity would be similar to a new building. The cumulative valuation is measured over any
three-year period.

For an occupancy **other than Group R or Group U**, the 50% valuation threshold is not enough by
itself. The completed building must also be one that §903.2 would require to be sprinklered.
Section 903.6 separately covers any addition to an already-sprinklered building and an addition
that is at least 33% of existing area and greater than 1,000 square feet within two years.

This is combined with Laguna's tightened **§903.2 thresholds**, which mandate sprinklers in
Group A, B, E, F-1, M, S-1, and S-2 occupancies whenever the building exceeds **2 stories** OR
**5,000 sf** of fire area — these thresholds apply to both new construction and any
change-of-occupancy/major-alteration that crosses them.

A mixed-use building (R over commercial) can fire the Fire Code scope trigger and one or more
CBC §903.6 triggers at once. Apply the exact clause for each occupancy and scope; do not reduce
§903.6 to an unconditional 50%-valuation rule.

---

## Permit Processing Tracks

**This section is the single home for OTC hours and OTC eligibility.** Every Laguna permit-type
skill cites it by OTC item number. No permit-type skill restates the hours or the list.

[source: the City source document (not included in this plugin) — City of Laguna Beach, "Building Plan Review Services," edition 06/08/2026, 2026 California Codes cycle]

### 1. Over-the-Counter (OTC) Plan Review
- **Turnaround:** Same day (30-min appointment or walk-in). An OTC review does not guarantee a same-day permit.
- **OTC walk-in, no appointment:** Monday-Thursday 7:30am-2:00pm, **last check-in 12:45pm**. Subject to plan-reviewer availability; wait times can be lengthy.
- **OTC by appointment:** Monday-Thursday 7:30am-11:00am. Half-hour slots, 30-minute maximum, first-come first-served. Book at `https://www.lagunabeachcity.net/government/departments/community-development/building-permits/appointment-for-counter-plan-review`
- **Both tracks cover** first review, rechecks and revisions. An applicant who employs a design professional must have that design professional present.
- **Scope limit:** projects that are not complex and are small in scope-of-work — reviewable in approximately 30 minutes.

**Qualified projects for OTC — the City's 11 numbered items. Cite by number.**

1. Residential kitchen and bathroom remodels with minor structural modifications.
2. Residential decks, balconies and patio cover repairs with minor structural modifications (no extension or replacement).
3. Window and door replacement with minor structural modifications.
4. Construction revisions to approved plans and structural calculations. Two new sets of plans and calculations (if applicable); all revised items clouded with a delta number.
5. Exterior siding replacement.
6. Residential electrical meter upgrade or change-out in same location, clearance and access, up to 200A (utility company approval required).
7. Re-roof with same material or lighter.
8. Residential HVAC change-outs in same location, clearances, access and type.
9. Minor plumbing, electrical or mechanical repairs or replacements.
10. Wood or metal fences, with a completed Survey Waiver form if the fence is within 3' of a property line. Certification is required if no Survey Waiver form was submitted at permit issuance.
11. **Commercial signs without structural alterations.**

**Disqualifiers — a project on the list still goes to full review if it requires any of:**
other City department review and approval; approval by an outside agency (County Health, Caltrans, etc.); geotechnical report review; extensive structural design and modifications; change of construction type; or change of use/occupancy to a more restrictive occupancy.

**OTC submittal:** completed permit application with the correct address, plus two sets of 24"x36" plans showing an accurate site plan, the complete scope of work, and a floor plan locating existing and proposed work. Two sets of stamped and signed engineered plans and calculations, and two sets of Title 24 energy forms, if applicable.

### 2. Standard Plan Review (Full)
Multi-step process with 4 phases:
1. **Zoning Plan Check** — Planning Division reviews for zoning compliance (setbacks, height, parking, open space, lot coverage)
2. **Planning route** — Match the current §25.05.040 closed lists: Design Review, Zone Clearance, or Administrative Design Review. Do not use exterior work as a default trigger.
3. **State Agency Review** — If PCH or Laguna Canyon Road work, Caltrans permit needed
4. **Building Plan Check** — for new single-family construction and additions of 500 sf or
   more, 4 sets of 24"x36" construction drawings; for additions under 500 sf and interior
   remodels, 2 sets. Minor permits may use 11"x17" sheets. Supporting calculations and
   reports follow the current Building Division checklist.

**Projects that go to full plan review** [same source]:

- **Residential:** new single-family residences; additions; major remodels; accessory dwelling units; site improvements; decks and guardrails; patio covers; retaining walls; pools and spa; **elevator**; solar; **roof trusses (for deferred submittal)**; **Alternative Materials, Design & Methods (AM&M) request**.
- **Non-residential:** new building/structure; tenant improvements with interior and exterior modification and alterations; mixed use; **AM&M request**; **Unreasonable Hardship request to disabled access requirements**.

Zoning/Planning approval, including the 14-day Design Review appeal period where one applies, is required for every full plan review submittal.

### 3. Expedited Permit — Solar Only
- Small residential rooftop solar energy systems (per Ch. 14.84)
- Building permit issued within **3 business days** if meets standard plan/checklist
- Only **1 inspection** required, scheduled within 2 business days

### 4. EV Charger Permit
- Streamlined per Ch. 14.85
- Code compliance checklists available for residential, non-residential, and multi-family

---

## Permit Expiration (§14.50.024)

- Building permits **expire after 1 year** if work has not commenced
- **180-day extensions** available upon request

### Building plan-check applications (CBC/CRC 105.3.2)

- Laguna adopts CBC/CRC 105.3.2 without amendment (LBMC 14.50.010; 14.52.014 adds CRC R101.4). An
  application is **deemed abandoned 180 days after filing**, unless the applicant is pursuing it
  in good faith or the permit has been issued. The building official may extend it in writing for
  justifiable cause: up to 90 days at a time under the CBC, 180 days under the CRC.
- This clock runs from filing, not from a corrections letter. The City's Building correction
  letters state no response deadline.

---

## Permit Decision Matrix

Each row names a trigger and the permit or review it adds. Apply a row only when the project's facts meet its trigger.

| Trigger | Required Permit/Review | Chapter |
|---------|----------------------|---------|
| Any construction/alteration | Building Permit | Ch. 14.50 |
| Work on a §25.05.040(B) closed list | **Zone Clearance**, **Administrative Design Review**, or **Design Review** (DRB for single-/two-family, Planning Commission otherwise — §25.05.040(F)(1)). Exterior work alone is not a trigger. | §25.05.040, §25.05.045 (Ord. 1732) |
| Property in Coastal Zone | **Coastal Development Permit**, unless the work is exempt (§25.07.008, e.g. most single-family improvements) or categorically excluded (§25.07.010) | Ch. 25.07 |
| Property in VHFHSZ (most of city) | WUI compliance review | Ch. 14.70 |
| 1&2-family dwelling (new construction) | **Sprinkler system** required | Ch. 14.52.030 (CRC R309.2 amendment) |
| Existing 1&2-family dwelling — 3-year cumulative valuation >50% of pre-work valuation, OR alteration ≥50% OR added story (exterior work ≥50% alone: UNSETTLED) | **Full sprinkler retrofit** required (either trigger fires it) | Ch. 14.52.030 **and** Title 15 §1103.5.4 |
| Hillside property, steep lot, CGS landslide/liquefaction zone | **Geotechnical report**, with City peer review where the Building Division's list requires it; slopes of 30%+ are also an ESA for Planning (§25.08.010, Ord. 1732) | Building Division geotechnical handout (2026-06-17); `../guide/references/grading-drainage.md` |
| Historic resource (register, state/national listing, or CEQA evidence; inventory rating flags a possible assessment) | **Heritage Committee** recommendation before ADR or Design Review | Ch. 25.45 (Ord. 1732) |
| Near PCH or Laguna Canyon Rd | **Caltrans** encroachment permit | State |
| In FEMA flood zone | **Floodplain Development Permit** | Ch. 25.38 |
| Demolition | **Demolition Notification** | City form |
| Walls/fences within 3' of property line | **Survey waiver** or survey required | City policy |

---

## Zoning Overview

Laguna Beach has unique zoning with character-preservation focus. Key zones:

### Residential Zones
- **R-1** — Single-family residential (most of the city)
- **R-2** — Two-family residential
- **R-3** — Multi-family residential

### Commercial Zones (LBMC 25.02.006)
- **LBP** — Local Business-Professional (Ch. 25.18)
- **C-N** — Commercial-Neighborhood (Ch. 25.19)
- **C-1** — Local Business (Ch. 25.20)
- **CH-M** — Commercial Hotel-Motel (Ch. 25.21)
- **SLV** — South Laguna Village Commercial (Ch. 25.25)
- **Downtown Specific Plan** (Ch. 25.40) — downtown is zoned by DSP districts, e.g. CBD-1 Resident Serving, CBD-2 Downtown Commercial, CBD-Office, CBD-Central Bluffs, CBD-Arts District, CBD Visitor Commercial (named in LBMC 25.16.050 and 25.23.030(A))

### Special Overlay Districts
- **Three Arch Bay** — Private community with additional development application process
- **Coastal Zone** — California Coastal Act overlay
- **VHFHSZ** — Fire hazard overlay

---

## ADU/JADU (Ch. 25.17)

- ADU/JADU permitted in residential zones per state law + local regulations
- ADUs take **Zone Clearance**, not Design Review, "only as set forth in Chapter 25.17" (§25.05.040(B)(2)(h), Ord. 1732); state ADU law keeps qualifying ADUs ministerial — `load_skills("adu")`
- Coastal Development Permit may also be required
- ADU process flowchart and FAQ available as city handouts
- More complex than flat-terrain cities due to hillside, coastal, fire, and design review overlays

---

## Construction Hours (LBMC §7.25.080 and Building Division staging procedures)

| Activity / day | Permitted Hours |
|-----|----------------|
| **Construction, Monday-Friday** | 7:30 AM - 6:00 PM |
| **Grading, Monday-Friday** | 8:00 AM - 4:00 PM |
| **Hauling, Monday-Friday** | 9:00 AM - 3:00 PM |
| **Saturday and Sunday** | **PROHIBITED** |
| **Federal Holidays** | **PROHIBITED** |

Verbatim from §7.25.080(A)–(B): noise-generating construction is permitted on weekdays only, **7:30 a.m. – 6:00 p.m.**; on weekend days OR federal holidays, "No person ... shall operate any tool, equipment or machine in a manner which produces loud noise."

**Exceptions** (§7.25.080(D)):
- Emergency construction authorized by the director of community development or building official
- Public works by/for a public agency (subject to specific findings)
- Construction that demonstrably complies with the noise limits in §7.25.040
- Sawdust Festival / Art-A-Fair / Laguna Art Museum — extended hours per ordinance

This is materially more restrictive than most CA cities, which typically allow a Saturday window. **No general Saturday window exists in Laguna Beach.** Verify any project schedule against §7.25.080 before approval.

---

## Fire Service

- **LBFD** (Laguna Beach Fire Department) provides fire services — Laguna Beach has its own municipal fire department, NOT OCFA
- 2025 California Fire Code adopted
- Title 15 contains fire prevention regulations with local amendments
- VHFHSZ defensible space requirements enforced

---

## Contact Information

Phone, address, portal and code links are in the jurisdiction table at the top of this file —
they are not repeated here. Division phones, emails, staff and every published hours variant live
in `references/contacts-hours.md`. OTC hours are in §"Permit Processing Tracks" above.

---

## References

Load these on demand. Paths are relative to this file.

**Laguna Beach rules**

- `references/contacts-hours.md` — Laguna Beach Community Development — Contacts, Hours & Locations
- `references/city-zoning-standards.md` — Laguna Beach — City Zoning Standards (Cross-Cutting Reference)

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
