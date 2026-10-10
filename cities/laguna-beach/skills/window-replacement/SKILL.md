---
name: window-replacement
description: "Window/Door Replacement permits in Laguna Beach, CA. Windows and doors replaced in their existing openings, retrofit or full-frame. NOT a new or enlarged opening, which needs a header and a real review. Skylights are general-building. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions window replacement in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2 CBC, Part 2.5 CRC, Part 6 Energy, Part 7 WUI); Building Division OTC policies, Ch. 14.70 Wildland-Urban Interface Code, Ch. 14.52 Residential Code amendments, Title 25 Zoning (Design Review & Coastal Development)"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-10-10"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Window/Door Replacement Permit

Handles window/door replacement permits in Laguna Beach end-to-end. Scope: Windows and doors replaced in their existing openings, retrofit or full-frame. NOT a new or enlarged opening, which needs a header and a real review. Skylights are general-building.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a window/door replacement permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Window/Door Replacement Permit

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

This skill covers Laguna Beach's city-specific window and door replacement requirements. **On parcels in a fire hazard severity zone (check the parcel in `lookup_property`), the WUI glazing rules and the vinyl window amendments make Laguna Beach window replacements more complex than typical CA cities.**

**How this skill relates to state code**: The `california-window-replacement` skill covers CBC/CRC/Energy Code/WUI state requirements. This skill covers what Laguna Beach adds -- primarily the vinyl window WUI amendment, skylight restrictions, design review rules, coastal zone analysis, and OTC processing. **Load state code first**, then this skill.

---

### Decision Tree Router

| Project Type | Route |
|-------------|-------|
| **Like-for-like replacement** (same opening, same material type) | OTC eligible |
| **Like-for-like but vinyl frames** | OTC eligible -- verify welded corners + metal reinforcing (Ch. 14.70.035) |
| **Different size in same rough opening** | OTC eligible ("minor structural mods") |
| **New or enlarged opening** | Full plan review -- structural + possible Design Review |
| **New or relocated window** (different wall location) | Match current closed lists; ordinarily Zone Clearance as a non-major alteration no more than 15 ft, unless another trigger applies |
| **Skylights** | Operable automatic night shade → Zone Clearance `(B)(2)(s)`; without one → ADR `(B)(3)(a)(xii)`; must also be glass in VHFHSZ |
| **Part of major remodel** | Full plan review + Design Review `(B)(1)(a)` |

---

### VHFHSZ Glazing Requirements

Use the parcel's actual fire hazard severity zone from `lookup_property` (site facts). Do not assume it from a citywide share; many Laguna parcels are Very High, but not all (`../city-reference/SKILL.md`). Where the parcel is in a WUI area (LBMC 14.70.010, 101.2), the state WUI Code (Section 504.8) requires multi-pane glazing with at least one tempered pane, and Laguna Beach adds the following local amendments:

#### Vinyl Window Amendment (Ch. 14.70.035 -- Section 504.8.3)

**City-specific requirement beyond state code:**

> Glazing frames made of vinyl materials shall have welded corners and metal reinforcing in the interlock area.

This means:
- **Vinyl-framed windows** in VHFHSZ areas must have welded (not mechanical) corner joints
- **Metal reinforcing** is required in the interlock area (the interlocking rail where the sash meets the frame on sliding/hung windows)
- This applies to ALL vinyl windows in the VHFHSZ, not just replacement -- but is especially relevant for replacement since contractors may spec standard vinyl windows that lack these features
- **Aluminum, fiberglass, and wood-clad windows** are NOT subject to this amendment (it only applies to vinyl frames)

**Review check:** When the application specifies vinyl windows, verify the product spec sheet shows welded corners and metal-reinforced interlocks. FLAG if specs are not provided or if the product uses mechanical corner fasteners instead of welded joints.

#### Skylight and Sloped Glazing Restriction (Ch. 14.70.040 -- Section 504.8.4)

**City-specific requirement beyond state code:**

> Skylights and sloped glazing must comply with Section 504.8 and must be of glass. Plastic skylights and plastic sloped glazing are not allowed.

This means:
- **No acrylic or polycarbonate skylights** anywhere in the VHFHSZ
- Replacement skylights must be glass (tempered or laminated per state code)
- This is more restrictive than state code, which allows plastic skylights in some configurations

#### WUI Minor Repair Exception (Ch. 14.70.015 -- Section 101.2 Exception)

> With the approval of the building official, minor repairs or replacement of exterior materials may be done with the same materials as exists on the building.

This exception allows the building official to approve a window replacement with the same materials as the existing window, even if those materials do not fully comply with current WUI code. This is a discretionary exception -- not automatic. FLAG when an applicant appears to be relying on this exception (e.g., replacing single-pane with single-pane in VHFHSZ).

---

### OTC Eligibility

Window and door replacement is eligible for over-the-counter plan review:

- **Qualified:** Window/door replacement in same openings or with minor structural mods
- **OTC item:** the city reference OTC item 3 (window and door replacement with minor structural modifications) — hours and the full list live in `../city-reference/SKILL.md`
- **Not OTC:** New openings requiring structural headers, or work that is part of a major remodel
- **Where to file:** City practice is to take simple permits such as a like-for-like window replacement at the Building counter, not through the online portal (R26-1837; a CrossBeam reference that is not included in this plugin). Tell the applicant to bring it to the counter after Planning's Zone Clearance. Which other simple permits are counter-only is still an open City question.

---

### Design Review

Urgency Ordinance No. 1732 repealed the former window-specific exemption and neighbor-consent ADR split.

- In-kind replacement routes to Zone Clearance under current §25.05.040(B)(2)(c).
- A non-major alteration/addition and an improvement no more than 15 ft ordinarily route to Zone Clearance under (B)(2)(a)-(b), unless another closed-list trigger or the ESA override applies.
- Do not require neighbor consent as a statutory prerequisite or cite the repealed `(B)(2)(k)`, `(B)(2)(b)(iii)`, or `(B)(3)(a)(xi)(3)` provisions.
- A skylight with an operable automatic night shade takes Zone Clearance under (B)(2)(s); without such a shade it takes ADR under (B)(3)(a)(xii).
- **Historic resource:** replacing or modifying doors and windows is a minor alteration that takes Administrative Design Review under (B)(3)(a)(iv), after review against the Secretary of the Interior's Standards; the hearing cannot be waived for this item. Larger historic changes are Design Review under (B)(1)(d).
- **Planning first:** Zone Clearance is required before Building issues the permit (§25.05.045(B)(3)), including for OTC change-outs.
- **ESA** (includes slopes of 30% or greater): (B)(2) and (B)(3) are unavailable unless a licensed professional finds, subject to peer review, no impact; otherwise Design Review under (B)(1)(e).
- The Director may refer a Zone Clearance or ADR window project up to the board (§25.05.040(A)(2)(d)).

#### Design Review Trigger

If the overall project constitutes a major remodel, Design Review is required under §25.05.040(B)(1)(a). An improvement over 15 ft independently requires Design Review under (B)(1)(c). The Design Review Board hears it for a single-family home or duplex; the Planning Commission hears it for 3+ units, nonresidential buildings, and anything in the Downtown Specific Plan area (§25.05.040(F)(1)(i)-(ii)).

---

### Coastal Zone

Most of Laguna Beach is in the Coastal Zone. Window replacement in single-family dwellings is generally **exempt** from Coastal Development Permit (CDP) requirements under Section 25.07.008(A)(1) as an "improvement to a single-family dwelling."

#### When CDP IS Required

A CDP may be required even for window replacement if the property is:

1. **On a beach, in a wetland or stream, seaward of mean high tide, within 50 feet of a coastal bluff edge, in an environmentally sensitive area, or in a highly scenic area** (Section 25.07.008(A)(1)(b))
2. **Between the sea and the first public road** (or within 300 feet of the beach/mean high tide) AND the window work is part of a project causing an aggregate increase of 10% or more of internal floor area, or an increase in height of more than 10% (Section 25.07.008(A)(1)(c)) -- unlikely for window-only work
3. **Subject to a prior CDP condition** that requires future improvements to get a CDP (Section 25.07.008(A)(1)(f))

**For standalone window replacement (no floor area or height change), CDP is typically NOT required** even in the Coastal Zone -- but FLAG if the property is within 50 feet of a bluff edge or in an environmentally sensitive area.

#### Multi-unit, commercial and mixed-use buildings

The single-family exemption (A)(1) does not apply. **Default: exempt.** Two exemptions fit window and door replacement on an apartment, condominium, commercial or mixed-use building:
- §25.07.008(A)(2): "Improvements to an existing structure (including attached fixtures and landscaping) other than single-family dwellings or public works facilities are exempt unless classified under one of the following": (a) development described in (A)(1) through (6) or in a stream or lake; (b) a "change in the intensity of use"; (c) a condominium, stock cooperative or similar conversion; (d) significant landform alteration near a bluff or stream, in a highly scenic area or an ESA.
- §25.07.008(A)(3): "Repair and maintenance activities that do not result in an addition to, or enlargement or expansion of, the object of such repair and maintenance activities" are exempt; its exceptions are shoreline works and work on sand, bluffs, ESAs or near coastal waters.

So give the exemption as the answer, and test only the exceptions: items 1-3 under "When CDP IS Required" above, which reach these buildings through (A)(2)(a); a change in use intensity; a conversion. If none applies, the CDP step is the City's exemption record, not an administrative CDP. City practice: coastal-zone exterior projects routinely file a CDP exemption record. One older multi-unit window and door job took an administrative CDP (CDP-2023-1175, before Ord. 1732); give it only as a reason to confirm with Planning, not as the default.

#### De Minimis Waiver (Section 25.07.009)

If a CDP is technically required, the Director of Community Development may issue a **de minimis waiver** for window replacement if the development has no adverse effect on coastal resources and is not in an appeal area. This avoids the full CDP hearing process.

---

### Sprinkler Retrofit

**Two triggers, either one fires.** See `../residential-remodel/references/city-sprinkler-retrofit.md` — the single residential retrofit reference. Do not restate the rule here.

- **Ch. 14.52.030** (valuation, Ord. 1725) — cumulative additions, alterations and repairs in any three-year period exceeding 50% of the pre-work valuation of the dwelling + attached garage.
- **Title 15 §1103.5.4** (scope, Ord. 1726) — alteration of ≥50% of the building, OR an added story. Whether work on ≥50% of the exterior fires it by itself is UNSETTLED (two readings in the reference; confirm with Building and Fire at pre-application).

**Window-specific notes.**
- Window replacement alone is unlikely to fire either trigger. Cumulative history is what fires Ch. 14.52.030: if the owner permitted a kitchen remodel, bathroom remodel or re-roof in the past three years, the combined valuation may cross 50%. **Always ask whether other permitted work exists in the three-year window.** If the cumulative valuation approaches 50%, FLAG for sprinkler review.
- If the exterior prong is tested, window and door openings count toward the exterior tally even on same-opening change-outs, because the cladding around them is disturbed. Window work combined with a reside or reroof can reach 50% of the exterior. That prong is UNSETTLED: when it alone decides the answer, give both readings and do not say sprinklers are required.
- Do **not** substitute §14.50.104 / CBC §903.6 for Ch. 14.52.030 on a CRC-track house. Section 903.6 expressly covers CBC-track Group R, but Ch. 14.52.030 is the specific valuation rule here.

---

### Key Laguna Beach Window Replacement Facts

- **OTC eligible:** Yes -- same/similar openings, minor structural mods
- **Fenestration energy:** state rule, not a city delta; apply it from the state skill. Laguna is Climate Zone 6 (ZIPs 92651, 92652). Replacement windows: U-factor 0.30 and SHGC 0.23 (Energy Code 150.2(b)1B, Table 150.1-A), or, for up to 75 sq ft of replaced vertical fenestration, U-factor 0.40 and SHGC 0.35 (Exception 1). Added window area uses Table 150.1-A (150.2(b)1A)
- **Fire hazard zone:** parcel-specific. Use the parcel's fire hazard severity zone from `lookup_property`; WUI glazing (state WUI 504.8, dual-pane with a tempered pane) and the city amendments apply where the parcel is in a WUI area
- **Vinyl windows:** Must have welded corners + metal reinforcing in interlock area (Ch. 14.70.035)
- **Skylights:** Glass only -- no plastic (Ch. 14.70.040)
- **Planning route:** in-kind replacements take Zone Clearance; other non-major work ordinarily takes Zone Clearance; the former neighbor-consent ADR split was repealed
- **Coastal Zone:** Generally exempt from CDP for window replacement; FLAG if near bluff edge or ESA
- **Sprinkler trigger:** For a CRC-track house, run Ch. 14.52.030 (50% cumulative valuation over any 3-year period) and Title 15 §1103.5.4 (scope). Do not mislabel §14.50.104 as non-residential-only; its Group R clauses apply to CBC-track residential buildings. See `../residential-remodel/references/city-sprinkler-retrofit.md`
- **WUI minor repair exception:** Building official may approve same-material replacement (Ch. 14.70.015)

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Scope: Replacement Type** | ❌ **fail** | Determine if this is like-for-like replacement (same size opening), resizing within existing rough opening, enlarging an existing opening, or creating a new opening. Like-for-like and same-rough-opening replacements are simpler. Enlarging or creating new openings triggers structural review (headers, lintels) and may trigger additional energy, egress, and fire-separation checks. | CRC R609.1; CBC 2401.1 |
| 2 | **Energy Code: U-Factor** | ❌ **fail** | Replacement fenestration must meet U-factor requirements. Prescriptive: max U-factor 0.27 in CZ 1-5, 11-14, 16; max 0.30 in CZ 6-10, 15. Exception for replacements <=75 SF: U-factor <=0.40 in CZ 1-16. Glass replaced in existing sash/frame is considered a "repair" and exempt from energy requirements if performance equals or exceeds original. | Energy Code 150.2(b)1B, Table 150.1-A |
| 3 | **Energy Code: SHGC** | ❌ **fail** | Replacement fenestration must meet Solar Heat Gain Coefficient requirements. Max SHGC 0.23 in CZ 2, 4, 6-14; max 0.20 in CZ 15; no requirement in CZ 1, 3, 5, 16. Exception for replacements <=75 SF: SHGC <=0.35 in CZ 2, 4, 6-14; SHGC <=0.23 in CZ 15. | Energy Code 150.2(b)1B, 150.1(c)3A, Table 150.1-A |
| 5 | **Egress: Bedroom Windows** | ❌ **fail** | Every sleeping room must have at least one emergency escape and rescue opening. Minimum net clear opening: 5.7 SF (5.0 SF at grade floor). Min height: 24". Min width: 20". Max sill height: 44" above floor. Replacement windows in existing egress openings must be the manufacturer's largest standard size that fits the existing frame or rough opening (CRC R319.5). Cannot reduce egress below existing if window serves a sleeping room. | CRC R319.1-R319.5; CBC 1031.2-1031.3 |
| 6 | **Safety Glazing: Hazardous Locations** | ❌ **fail** | Safety glazing (tempered, laminated, or approved safety glass) is required in hazardous locations: (a) all glazing in doors, (b) glazing within 24" of a door edge and below 60" from floor, (c) glazing in windows where pane >9 SF AND bottom edge <18" from floor AND top edge >36" from floor AND walking surface within 36", (d) glazing adjacent to tubs/showers/pools where bottom edge <60" from standing surface, (e) glazing adjacent to stairs where bottom edge <36" above walking surface, (f) glazing in guards/railings. Must be marked per CPSC 16 CFR 1201 or ANSI Z97.1. | CRC R324.1-R324.4; CBC 2406 |
| 7 | **Window Fall Protection** | ❌ **fail** | In dwelling units, operable windows with bottom of clear opening <24" above finished floor AND >72" above exterior grade must either: (a) limit opening so 4" sphere cannot pass, or (b) have window opening control device per ASTM F2090. If window also serves as egress, the control device must allow full opening and not reduce net clear area below egress minimums. | CRC R321.2; CBC 1015 |
| 8 | **Structural: Headers for New/Enlarged Openings** | ❌ **fail** | If the opening is being enlarged or is new, a properly sized header is required in bearing walls. Header size depends on span, number of stories supported, and species/grade of lumber. Jack studs required per Table R602.7(1) and R602.7(2). Non-bearing walls: no load-bearing header required; flat 2x4 permitted for openings up to 8 ft. If opening exceeds prescriptive table limits, engineered design required. | CRC R602.7, Tables R602.7(1)-(3); CBC 2308.6 |
| 9 | **Fire Separation: Openings Near Property Lines** | ❌ **fail** | No openings (windows/doors) are permitted in exterior walls with fire separation distance <3 ft from property line. At 3 ft: openings limited to 25% of wall area. At >=5 ft: unlimited openings. Replacement windows in existing openings at <3 ft fire separation distance may be a pre-existing nonconformity -- FLAG for building official review. | CRC R302.1, Table R302.1(1); CBC 705 |
| 10 | **Fire-Rated Glazing** | ❌ **fail** | Windows in fire-rated walls must use fire-rated glazing assemblies. Fire window assemblies rated per Table 716.1(3). 1-hour exterior wall: min 3/4-hour fire window assembly marked OH-45 or W-60. Replacement in a fire-rated wall must maintain the wall's fire-resistance rating. | CBC 716.1, Table 716.1(3); CRC R302.1 |
| 11 | **WUI Exterior Glazing** | ❌ **fail** | In Wildland-Urban Interface (WUI) areas, exterior windows must be: (a) multi-pane with at least one tempered pane, (b) glass block, (c) fire-protection-rated glazing >=20 min per NFPA 257 or UL 9, or (d) glazing meeting SFM Standard 12-7A-2. Dual-pane with one tempered pane is the most common compliant option. Single-pane windows are NOT compliant in WUI zones. | WUI Code 504.8; CRC R337 |
| 13 | **Wind Resistance** | ⚠️ **flag** | Windows must be rated for the design wind loads per ASCE 7. Most of California: 110-115 mph ultimate design wind speed. Products tested per AAMA/WDMA/CSA 101/I.S.2/A440. Performance grade on NFRC/AAMA label must meet or exceed required design pressure. | CRC R609.2, R301.2.1; CBC 1609 |
| 14 | **Natural Light and Ventilation** | ❌ **fail** | Habitable rooms require glazing area >=8% of floor area for natural light. Openable area >=4% of floor area for ventilation. Bathrooms require 3 SF glazing (half openable) unless mechanical ventilation provided. Replacement windows must maintain compliance or have existing exception (artificial light/mech vent). | CRC R325.1-R325.2 |
| 15 | **Lead Paint / Asbestos** | ⚠️ **flag** | For homes built before 1978, window replacement may disturb lead-based paint. Contractor must be EPA RRP (Renovation, Repair, Painting) certified. Lead-safe work practices required per EPA 40 CFR 745. Glazing compounds in pre-1978 windows may contain asbestos -- test before demolition if suspected. Not a building code requirement per se, but a federal/state regulatory requirement that affects permitting. | EPA 40 CFR 745; Cal/OSHA Title 8 |
| 18 | **Contractor Licensing** | ❌ **fail** | C-17 (Glazing) or B (General Building) contractor license required for window installation. D-64 (Non-Electrical Sign) for storefront glazing. Workers' compensation insurance required. For lead paint disturbance on pre-1978 homes: EPA RRP certification required. | B&P Code 7028 |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 4 | **NFRC Label Verification** | All replacement windows and doors must bear an NFRC (National Fenestration Rating Council) label showing U-factor and SHGC ratings. Verify the label values meet or exceed the requirements for the project's climate zone. Products must be tested per AAMA/WDMA/CSA 101/I.S.2/A440. | CRC R609.3; Energy Code 110.6 |
| 12 | **Flashing and Weatherproofing** | Window and door openings must be flashed per CRC R703.4. Flashing must integrate with the weather-resistive barrier (WRB). Pan flashing at sill, side flashing lapped over pan, head flashing lapped by WRB above. Manufacturer's installation instructions must be followed. Sealant alone is not acceptable flashing. | CRC R703.4, R609.1; CBC 1404.4 |
| 16 | **Anchoring and Installation** | Windows must be anchored per manufacturer's instructions. Through-frame, frame-clip, or through-flange methods per CRC R609.7. Masonry/concrete substrates: anchors embedded directly or through wood buck >=1.5" thick. Mullions tested per AAMA 450 or engineered. | CRC R609.7-R609.8 |
| 17 | **Product Testing and Labeling** | Windows must bear label from approved testing agency showing manufacturer, performance grade, and compliance with AAMA/WDMA/CSA 101/I.S.2/A440. Safety glazing must be permanently marked (acid-etched, sandblasted, ceramic-fired, laser-etched, or embossed). Removable labels not acceptable for tempered glass (except spandrel). | CRC R609.3, R324.1; CBC 2403, 2406 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/egress-requirements.md` — Emergency Egress and Window Requirements
- `references/fenestration-energy.md` — Fenestration Energy Code Requirements
- `references/fire-rated-glazing.md` — Fire-Rated Glazing and Fire Separation Requirements
- `references/safety-glazing.md` — Safety Glazing Requirements
- `references/structural-openings.md` — Structural Requirements for Window/Door Openings
- `references/wui-exterior-glazing.md` — WUI Exterior Glazing Requirements

**Laguna Beach rules**

- `references/city-design-review-windows.md` — Laguna Beach — Current Window/Door Planning Route
- `references/city-wui-glazing.md` — Laguna Beach WUI Glazing Amendments

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
