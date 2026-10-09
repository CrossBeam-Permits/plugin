# California Baseline — Window/Door Replacement

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Window & Door Replacement Permit Review

This skill covers **state-level** California requirements for residential and light commercial window and door replacement permits. It routes between the California Residential Code (CRC) for dwellings and the California Building Code (CBC) for commercial/light commercial buildings.

**What this covers:**
- Like-for-like window replacement (same size opening)
- Window upgrades (new size, style, or configuration)
- Enlarged or new window/door openings (structural modifications)
- Energy Code compliance (U-factor, SHGC by climate zone)
- Safety glazing (tempered glass in hazardous locations)
- Emergency egress requirements (bedroom windows)
- Window fall protection
- Fire-rated glazing (windows in fire-rated walls)
- WUI exterior glazing requirements
- Flashing and weatherproofing
- Lead paint and asbestos considerations for pre-1978 homes
- Sliding glass doors, patio doors, and exterior door replacement

**What this does NOT cover:**
- Storefront/curtain wall systems (see structural engineer)
- Skylights as standalone permit (partial coverage for skylight glazing)
- Commercial high-rise glazing engineering
- Interior window/pass-through openings between rooms
- Window film application (no permit typically required)

---

### How to Use This Skill

1. Determine whether the project is **residential** (CRC) or **commercial** (CBC)
2. Walk through the Decision Tree Router below
3. For each checklist item, load the referenced file from `/` as needed
4. See `../SKILL.md` for the full reference file catalog

---

### Decision Tree Router

#### STEP 1 -- Determine Code Path

| Building Use | Code | Key Sections |
|---|---|---|
| Single-family dwelling, duplex, townhouse <=3 stories | CRC | R609, R324, R319, R321, R302, R325 |
| Commercial, light commercial, multifamily >3 stories | CBC | Chapter 24, Section 716, Section 1031 |

Both codes share the same energy code requirements (Title 24 Part 6). The CRC is generally simpler; the CBC adds wind design and structural requirements for larger buildings.

#### STEP 2 -- What Type of Replacement Is This?

| Replacement Type | Load These References |
|---|---|
| **Like-for-like replacement** (same size, same opening) | `fenestration-energy.md` (energy compliance is still required) |
| **Different size in same rough opening** | `fenestration-energy.md`, `egress-requirements.md` (verify egress is maintained), `safety-glazing.md` |
| **Enlarged or new opening** (structural modification) | `structural-openings.md`, `fenestration-energy.md`, `egress-requirements.md`, `safety-glazing.md` |
| **Window in fire-rated wall** | `fire-rated-glazing.md`, `safety-glazing.md` |
| **WUI area replacement** | `wui-exterior-glazing.md`, `fenestration-energy.md` |
| **Energy question only** | `fenestration-energy.md` |
| **Safety glazing question only** | `safety-glazing.md` |
| **Egress question only** | `egress-requirements.md` |
| **Full permit review** (all checks) | All reference files as triggered |

#### STEP 3 -- Review Checklist

Walk each item in order. For every check, record PASS / FAIL / FLAG / N/A with the code section cited.

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 1 | **Scope: Replacement Type** | Determine if this is like-for-like replacement (same size opening), resizing within existing rough opening, enlarging an existing opening, or creating a new opening. Like-for-like and same-rough-opening replacements are simpler. Enlarging or creating new openings triggers structural review (headers, lintels) and may trigger additional energy, egress, and fire-separation checks. | CRC R609.1; CBC 2401.1 | `structural-openings.md` |
| 2 | **Energy Code: U-Factor** | Replacement fenestration must meet U-factor requirements. Prescriptive: max U-factor 0.27 in CZ 1-5, 11-14, 16; max 0.30 in CZ 6-10, 15. Exception for replacements <=75 SF: U-factor <=0.40 in CZ 1-16. Glass replaced in existing sash/frame is considered a "repair" and exempt from energy requirements if performance equals or exceeds original. | Energy Code 150.2(b)1B, Table 150.1-A | `fenestration-energy.md` |
| 3 | **Energy Code: SHGC** | Replacement fenestration must meet Solar Heat Gain Coefficient requirements. Max SHGC 0.23 in CZ 2, 4, 6-14; max 0.20 in CZ 15; no requirement in CZ 1, 3, 5, 16. Exception for replacements <=75 SF: SHGC <=0.35 in CZ 2, 4, 6-14; SHGC <=0.23 in CZ 15. | Energy Code 150.2(b)1B, 150.1(c)3A, Table 150.1-A | `fenestration-energy.md` |
| 4 | **NFRC Label Verification** | All replacement windows and doors must bear an NFRC (National Fenestration Rating Council) label showing U-factor and SHGC ratings. Verify the label values meet or exceed the requirements for the project's climate zone. Products must be tested per AAMA/WDMA/CSA 101/I.S.2/A440. | CRC R609.3; Energy Code 110.6 | `fenestration-energy.md` |
| 5 | **Egress: Bedroom Windows** | Every sleeping room must have at least one emergency escape and rescue opening. Minimum net clear opening: 5.7 SF (5.0 SF at grade floor). Min height: 24". Min width: 20". Max sill height: 44" above floor. Replacement windows in existing egress openings must be the manufacturer's largest standard size that fits the existing frame or rough opening (CRC R319.5). Cannot reduce egress below existing if window serves a sleeping room. | CRC R319.1-R319.5; CBC 1031.2-1031.3 | `egress-requirements.md` |
| 6 | **Safety Glazing: Hazardous Locations** | Safety glazing (tempered, laminated, or approved safety glass) is required in hazardous locations: (a) all glazing in doors, (b) glazing within 24" of a door edge and below 60" from floor, (c) glazing in windows where pane >9 SF AND bottom edge <18" from floor AND top edge >36" from floor AND walking surface within 36", (d) glazing adjacent to tubs/showers/pools where bottom edge <60" from standing surface, (e) glazing adjacent to stairs where bottom edge <36" above walking surface, (f) glazing in guards/railings. Must be marked per CPSC 16 CFR 1201 or ANSI Z97.1. | CRC R324.1-R324.4; CBC 2406 | `safety-glazing.md` |
| 7 | **Window Fall Protection** | In dwelling units, operable windows with bottom of clear opening <24" above finished floor AND >72" above exterior grade must either: (a) limit opening so 4" sphere cannot pass, or (b) have window opening control device per ASTM F2090. If window also serves as egress, the control device must allow full opening and not reduce net clear area below egress minimums. | CRC R321.2; CBC 1015 | `egress-requirements.md` |
| 8 | **Structural: Headers for New/Enlarged Openings** | If the opening is being enlarged or is new, a properly sized header is required in bearing walls. Header size depends on span, number of stories supported, and species/grade of lumber. Jack studs required per Table R602.7(1) and R602.7(2). Non-bearing walls: no load-bearing header required; flat 2x4 permitted for openings up to 8 ft. If opening exceeds prescriptive table limits, engineered design required. | CRC R602.7, Tables R602.7(1)-(3); CBC 2308.6 | `structural-openings.md` |
| 9 | **Fire Separation: Openings Near Property Lines** | No openings (windows/doors) are permitted in exterior walls with fire separation distance <3 ft from property line. At 3 ft: openings limited to 25% of wall area. At >=5 ft: unlimited openings. Replacement windows in existing openings at <3 ft fire separation distance may be a pre-existing nonconformity -- FLAG for building official review. | CRC R302.1, Table R302.1(1); CBC 705 | `fire-rated-glazing.md` |
| 10 | **Fire-Rated Glazing** | Windows in fire-rated walls must use fire-rated glazing assemblies. Fire window assemblies rated per Table 716.1(3). 1-hour exterior wall: min 3/4-hour fire window assembly marked OH-45 or W-60. Replacement in a fire-rated wall must maintain the wall's fire-resistance rating. | CBC 716.1, Table 716.1(3); CRC R302.1 | `fire-rated-glazing.md` |
| 11 | **WUI Exterior Glazing** | In Wildland-Urban Interface (WUI) areas, exterior windows must be: (a) multi-pane with at least one tempered pane, (b) glass block, (c) fire-protection-rated glazing >=20 min per NFPA 257 or UL 9, or (d) glazing meeting SFM Standard 12-7A-2. Dual-pane with one tempered pane is the most common compliant option. Single-pane windows are NOT compliant in WUI zones. | WUI Code 504.8; CRC R337 | `wui-exterior-glazing.md` |
| 12 | **Flashing and Weatherproofing** | Window and door openings must be flashed per CRC R703.4. Flashing must integrate with the weather-resistive barrier (WRB). Pan flashing at sill, side flashing lapped over pan, head flashing lapped by WRB above. Manufacturer's installation instructions must be followed. Sealant alone is not acceptable flashing. | CRC R703.4, R609.1; CBC 1404.4 | `safety-glazing.md` |
| 13 | **Wind Resistance** | Windows must be rated for the design wind loads per ASCE 7. Most of California: 110-115 mph ultimate design wind speed. Products tested per AAMA/WDMA/CSA 101/I.S.2/A440. Performance grade on NFRC/AAMA label must meet or exceed required design pressure. | CRC R609.2, R301.2.1; CBC 1609 | `fenestration-energy.md` |
| 14 | **Natural Light and Ventilation** | Habitable rooms require glazing area >=8% of floor area for natural light. Openable area >=4% of floor area for ventilation. Bathrooms require 3 SF glazing (half openable) unless mechanical ventilation provided. Replacement windows must maintain compliance or have existing exception (artificial light/mech vent). | CRC R325.1-R325.2 | `egress-requirements.md` |
| 15 | **Lead Paint / Asbestos** | For homes built before 1978, window replacement may disturb lead-based paint. Contractor must be EPA RRP (Renovation, Repair, Painting) certified. Lead-safe work practices required per EPA 40 CFR 745. Glazing compounds in pre-1978 windows may contain asbestos -- test before demolition if suspected. Not a building code requirement per se, but a federal/state regulatory requirement that affects permitting. | EPA 40 CFR 745; Cal/OSHA Title 8 | N/A |
| 16 | **Anchoring and Installation** | Windows must be anchored per manufacturer's instructions. Through-frame, frame-clip, or through-flange methods per CRC R609.7. Masonry/concrete substrates: anchors embedded directly or through wood buck >=1.5" thick. Mullions tested per AAMA 450 or engineered. | CRC R609.7-R609.8 | `structural-openings.md` |
| 17 | **Product Testing and Labeling** | Windows must bear label from approved testing agency showing manufacturer, performance grade, and compliance with AAMA/WDMA/CSA 101/I.S.2/A440. Safety glazing must be permanently marked (acid-etched, sandblasted, ceramic-fired, laser-etched, or embossed). Removable labels not acceptable for tempered glass (except spandrel). | CRC R609.3, R324.1; CBC 2403, 2406 | `safety-glazing.md` |
| 18 | **Contractor Licensing** | C-17 (Glazing) or B (General Building) contractor license required for window installation. D-64 (Non-Electrical Sign) for storefront glazing. Workers' compensation insurance required. For lead paint disturbance on pre-1978 homes: EPA RRP certification required. | B&P Code 7028 | N/A |

#### STEP 4 -- Output Format

For each checklist item, produce:

```
## [#]. [Check Name]
**Result:** PASS | FAIL | FLAG | N/A
**Code:** [Section number]
**Finding:** [1-2 sentence explanation of what was verified or what failed]
```

- **PASS** -- Requirement met per submitted information
- **FAIL** -- Requirement not met; cite code section and explain the deficiency
- **FLAG** -- Cannot determine from submitted data; explain what additional info is needed
- **N/A** -- Does not apply to this project (e.g., WUI checks when not in WUI zone)

---

### Quick-Reference Tables

#### Fenestration U-Factor by Climate Zone (Prescriptive -- New Construction / Added Fenestration)

| Climate Zone | Max U-Factor | Max SHGC |
|---|---|---|
| CZ 1 | 0.27 | NR |
| CZ 2 | 0.27 | 0.23 |
| CZ 3 | 0.27 | NR |
| CZ 4 | 0.27 | 0.23 |
| CZ 5 | 0.27 | NR |
| CZ 6 | 0.30 | 0.23 |
| CZ 7 | 0.30 | 0.23 |
| CZ 8 | 0.30 | 0.23 |
| CZ 9 | 0.30 | 0.23 |
| CZ 10 | 0.30 | 0.23 |
| CZ 11 | 0.27 | 0.23 |
| CZ 12 | 0.27 | 0.23 |
| CZ 13 | 0.27 | 0.23 |
| CZ 14 | 0.27 | 0.23 |
| CZ 15 | 0.30 | 0.20 |
| CZ 16 | 0.27 | NR |

#### Replacement Fenestration Exception (<=75 SF, Energy Code 150.2(b)1B Exception 1)

| Climate Zone | Max U-Factor | Max SHGC |
|---|---|---|
| CZ 1-16 | 0.40 | 0.35 (CZ 2, 4, 6-15) |
| CZ 1, 3, 5, 16 | 0.40 | NR |
| CZ 15 | 0.40 | 0.23 |

#### Emergency Egress Window Minimums

| Requirement | New Construction | Replacement (R319.5) |
|---|---|---|
| Net clear opening area | 5.7 SF (5.0 SF at grade) | Manufacturer's largest standard size fitting existing frame/rough opening |
| Min clear height | 24" | Same operating style or equal/greater opening area |
| Min clear width | 20" | Same operating style or equal/greater opening area |
| Max sill height above floor | 44" | Not required to meet if replacement complies with R319.5 |

#### Safety Glazing -- Hazardous Locations Summary

| Location | Condition | Code Section |
|---|---|---|
| Doors (all glazing) | Fixed and operable panels in swinging, sliding, bifold doors | R324.4.1 |
| Adjacent to doors | Within 24" of door edge, bottom edge <60" above floor | R324.4.2 |
| Windows (large panes) | Pane >9 SF, bottom <18" from floor, top >36" from floor, walking surface within 36" | R324.4.3 |
| Guards and railings | All glazing regardless of size or height | R324.4.4 |
| Wet areas (tubs/showers/pools) | Bottom edge <60" above standing surface | R324.4.5 |
| Adjacent to stairs/ramps | Bottom edge <36" above walking surface of stair/ramp | R324.4.6 |
| Bottom stair landing | Within 60" arc of bottom tread, <36" above landing | R324.4.7 |

#### Fire Separation Distance -- Openings in Exterior Walls (CRC)

| Fire Separation Distance | Openings Allowed | Fire Rating Required |
|---|---|---|
| < 3 feet | Not allowed | N/A |
| 3 feet | 25% maximum of wall area | 0 hours |
| >= 5 feet | Unlimited | 0 hours |

#### Header Sizing Quick Reference (Exterior Bearing Wall, 30 psf snow, 24' building width)

| Header Size | Max Span (Roof + Ceiling) | Jack Studs Required |
|---|---|---|
| 2-2x6 | 4'-7" | 1 |
| 2-2x8 | 5'-9" | 1 |
| 2-2x10 | 6'-10" | 2 |
| 2-2x12 | 8'-1" | 2 |
| 3-2x10 | 8'-7" | 1 |
| 3-2x12 | 10'-1" | 2 |

---

### Key Principles

1. **Even like-for-like triggers energy code.** Replacement windows must meet current energy code U-factor and SHGC requirements -- the exception for <=75 SF replacements provides relaxed values (U-0.40, SHGC 0.35 — except CZ15 where SHGC exception cap is 0.23) but does not eliminate the requirement entirely. Glass replaced in existing sash/frame is a "repair" and exempt only if performance equals or exceeds original.
2. **Egress cannot be reduced.** If a window serves as a required emergency escape opening (bedroom), the replacement must maintain compliant egress dimensions. CRC R319.5 provides a practical exception: the replacement must be the manufacturer's largest standard size that fits the existing frame or rough opening.
3. **Safety glazing is location-based, not size-based.** The requirement to use tempered or safety glass depends on where the window is installed (near doors, tubs, stairs, low to floor), not just its size. All seven hazardous location categories in R324.4 must be checked.
4. **Enlarging openings = structural review.** Any opening wider or taller than the existing triggers header sizing per Tables R602.7(1) and R602.7(2) in bearing walls. Non-bearing walls allow a flat 2x4 header for up to 8 ft spans.
5. **WUI zones require dual-pane with tempered.** Single-pane windows are not code-compliant in WUI areas. The most common compliant option is a dual-pane IGU with at least one pane of tempered glass.
6. **Fire separation controls everything near property lines.** No new openings within 3 ft of a property line. At 3 ft, openings are limited to 25% of wall area. Replacement in existing openings at noncompliant locations should be flagged for building official review.
7. **Flashing is not optional.** Window openings must be flashed and integrated with the weather-resistive barrier. Caulk/sealant alone is not acceptable. Pan flashing, side flashing, and head flashing are all required per manufacturer instructions.
8. **Lead paint is a federal requirement.** For pre-1978 homes, EPA RRP certification is required for the contractor. This is not a building code item but is enforced at the permit counter in many jurisdictions.
