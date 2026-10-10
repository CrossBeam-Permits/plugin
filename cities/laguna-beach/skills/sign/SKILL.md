---
name: sign
description: "Sign permits in Laguna Beach, CA. A wall, monument, blade, or awning sign, new or replaced, with its attachment and electrical. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions sign in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2 CBC Appendix H + Chapter 31; Part 3 CEC Article 600; Chapter 16 structural); LBMC Chapter 25.54 (Sign Regulations), Chapter 25.05 (Design Review)"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2025"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Sign Permit

Handles sign permits in Laguna Beach end-to-end. Scope: A wall, monument, blade, or awning sign, new or replaced, with its attachment and electrical.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a sign permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Sign Permit

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

This skill covers Laguna Beach's city-specific sign regulations. **Laguna Beach has one of the most restrictive and detailed sign ordinances in Orange County**, driven by the city's artistic village character and coastal location.

**How this skill relates to state code**: The `california-sign` skill covers CBC Appendix H structural requirements and CEC Article 600 electrical requirements. This skill covers what Laguna Beach adds -- primarily the zoning-level sign regulations (types, sizes, illumination, aesthetics, prohibited signs). **Load state code first**, then this skill.

---

### What Laguna Beach Adds Beyond State Code

1. **Comprehensive sign type/use matrix** -- Table 1 controls which sign types are allowed by use category (residential, commercial, industrial, institutional, recreational)
2. **Strict sign area/height/number limits** -- Table 2 with specific limits per sign type; total site max 1 sq ft per foot of frontage, 150 sq ft cap
3. **Internally illuminated signs prohibited** -- No cabinet/box signs (only individual channel letters, halo illumination, external illumination, and marquees allowed)
4. **Electronic/digital signs prohibited** -- EMCs and digital signs prohibited (except as interior building signs)
5. **Animated signs prohibited** (except interior building signs)
6. **Roof signs prohibited** in all use categories
7. **Pole signs prohibited**
8. **Backlit awning/canopy signs prohibited**
9. **Luminance limits** -- Daytime max 5,000 nit; nighttime max 300 nit; automatic dimming required
10. **Design review** -- Signs subject to Design Review Board or Planning Commission review per Section 25.05.040
11. **Sign programs** -- Multi-tenant buildings require coordinated master sign programs
12. **Downtown area** -- More restrictive limits (wall signs 15 sq ft max; temporary signs 5 sq ft max; window signs 5 sq ft max)
13. **Franchise/standardized signs prohibited** -- Except logos constituting less than 20% of sign area
14. **Luminous tube (neon) signs** -- Only interior locations 4+ ft from window, 3 sq ft max, single color, no animation
15. **Arts organizations** -- Special sign program provisions for designated arts organizations

---

### Decision Tree Router

#### STEP 1 -- Determine Sign Type and Use Category

Use Table 1 (in reference file `references/city-sign-ordinance.md`) to determine:
- What type of sign (wall, projecting, freestanding, etc.)
- What use category (residential, commercial, industrial, institutional, recreational)
- Whether the sign is Allowed (A), Permit Required (P), or Not Allowed (N)

If the sign type/use combination is "N" -- STOP. The sign is prohibited.

#### STEP 2 -- Check Prohibited Signs List

Cross-reference against Section 25.54.016 prohibited signs list:
- Animated signs (except interior)
- Internally illuminated signs (except marquees and individual channel letters)
- Electronic message centers / digital signs (except interior)
- Roof signs, pole signs, billboards, portable signs
- Back-lit awning/canopy signs
- Signs emitting sound, odor, or visible matter

#### STEP 3 -- Check Design Standards

Use Table 2 (in reference file `references/city-sign-ordinance.md`) to verify:
- Maximum number of signs permitted
- Maximum sign area
- Maximum height
- Other specifications (setbacks, clearances, projections)
- Total site sign area (1 sq ft per foot of frontage, max 150 sq ft)

#### STEP 4 -- Check Illumination

If illuminated:
- Only external, halo, or individual channel letter illumination allowed
- No internally illuminated cabinet/box signs (except marquees)
- No backlit awnings
- Luminance limits: 5,000 nit day / 300 nit night
- Automatic dimming required
- No glare, flash, blink, or fluctuation
- No exposed incandescent bulbs

#### STEP 5 -- Determine Approval Path

| Sign Category | Approval Authority | Notes |
|--------------|-------------------|-------|
| Signs within an approved sign program | Director (administrative) | Exempt from design review |
| Simple commercial signs meeting all standards | Director (administrative) / OTC | Same-day OTC review available |
| Master sign programs | Planning Commission | Multi-tenant coordinated signage |
| Advertising signs | Planning Commission | |
| Freestanding signs | Planning Commission | Max 1 per site |
| Wall signs of unique design | Planning Commission | |
| Blade/projecting signs | Planning Commission | |
| Tract/area identity signs | Planning Commission | |
| Sign independently matching a current Design Review category (for example, an improvement over 15 ft) | DRB or Planning Commission, as applicable | Current §25.05.040(B)(1) |
| Other sign whose only claimed DR basis is Ch. 25.54's stale `(B)(1)(d)` cross-reference | Planning confirmation / `needs_source` | Ord. 1732 reassigned `(B)(1)(d)` to historic-resource work |
| Temporary signs | Director | Max 30 days + 30-day extension |

#### STEP 6 -- Check Additional Overlays

| Overlay | Check |
|---------|-------|
| **Coastal Zone** | Most of city -- CDP may be required for new freestanding signs or significant structural sign work |
| **Downtown Specific Plan** | More restrictive limits: wall signs 15 sq ft; temporary 5 sq ft; window 5 sq ft |
| **VHFHSZ** | Materials must comply with WUI code if sign is part of exterior construction |

#### STEP 7 -- State Code Review

After completing city checks, run the state `california-sign` skill for:
- Structural requirements (wind, seismic, attachment per CBC Appendix H)
- Electrical requirements (CEC Article 600 for illuminated signs)
- Material/fire requirements
- Contractor licensing (C-45 for sign installation)

---

### Quick-Reference: Laguna Beach vs. State Code

| Topic | State Code (CBC/CEC) | Laguna Beach (Ch. 25.54) |
|-------|---------------------|--------------------------|
| Sign types allowed | All types (with structural/safety rules) | Restricted by use category (Table 1); roof/pole/billboard prohibited |
| Max sign area | No state zoning limit | 1 sq ft per ft of frontage, max 150 sq ft total |
| Freestanding height | 35-100 ft (by material) | **6 ft max** |
| Wall sign area | No state zoning limit | 75 sq ft max (15 sq ft in downtown) |
| Internal illumination | Allowed (with electrical code compliance) | **Prohibited** (except individual channel letters and marquees) |
| Electronic/digital signs | Allowed (with electrical code compliance) | **Prohibited** (except interior building signs) |
| Roof signs | Allowed (with structural requirements) | **Prohibited** |
| Pole signs | Allowed (as ground/freestanding) | **Prohibited** |
| Animated signs | Allowed (with fail-safe device) | **Prohibited** (except interior) |
| Franchise/standardized signs | No state restriction | **Prohibited** (logos max 20% of sign area) |
| Design review | Not required by state | Required for most signs |
| Luminance | No state standard | 5,000 nit day / 300 nit night; auto-dimming |
| Neon/luminous tube | Allowed per CEC Article 600 | Interior only, 4+ ft from window, 3 sq ft max, single color |

---

### Key Laguna Beach Sign Facts

- **OTC eligible**: Yes -- simple commercial signs meeting all standards
- **Roof signs**: Prohibited
- **Pole signs**: Prohibited
- **Internally illuminated cabinet signs**: Prohibited (individual channel letters OK)
- **Digital/EMC signs**: Prohibited (except interior)
- **Max total sign area**: 1 sq ft per ft of frontage, 150 sq ft cap
- **Max freestanding height**: 6 ft
- **Max freestanding area**: 50 sq ft total, 25 sq ft per face
- **Downtown area**: More restrictive (wall 15 sq ft, temporary 5 sq ft, window 5 sq ft)
- **Neon signs**: Interior only, 4+ ft from window, 3 sq ft max
- **Franchise signs**: Prohibited (logos allowed if <20% of sign area)
- **Temporary signs**: Max 30 days + 30-day extension, 60 days/year total
- **Planning route**: match the current §25.05.040 closed lists; do not use Ch. 25.54's stale `(B)(1)(d)` cross-reference as a current sign trigger
- **Sign programs**: Required for multi-tenant buildings (Planning Commission approval)
- **Arts organizations**: Special provisions for 6 designated organizations

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Sign Type Classification** | ❌ **fail** | Classify the sign as wall, projecting, ground/monument, pole, roof, marquee, channel letter, awning, digital/electronic, or portable/temporary. The type determines which CBC Appendix H sections apply and material/height requirements. | H102.1 |
| 2 | **Permit Exemption Check** | ⚠️ **flag** | Verify whether the sign requires a permit. Exempt: painted nonilluminated signs, temporary sale/rent signs, transportation authority signs, projecting signs <=2.5 sq ft, and changing moveable parts of an approved changeable sign. | H101.2 |
| 3 | **Location Restrictions** | ❌ **fail** | Sign must not obstruct exit signs, fire escapes, means of egress doors/windows, or required ventilation openings. Must not be attached to a fire escape. Must not prevent free passage on a roof. Must not confuse or interfere with traffic signs/signals. | H101.1, H103.1 |
| 4 | **Material Compliance** | ❌ **fail** | Verify materials comply with sign type requirements. Wall signs >40 sq ft: noncombustible. Projecting, roof, marquee signs: entirely noncombustible (with exceptions for letters/trim per H107.1 and internally illuminated facings per H106.1.1). Plastics: must pass ASTM D635 (<=2.5 in/min burn rate). Electric sign plastic faces: max 200 sq ft each. | H107, H110.1, H111.1, H112.1, H113.1 |
| 5 | **Height and Projection Limits** | ❌ **fail** | Verify sign does not exceed height limits for its type. Ground signs: 35 ft (combustible) / 100 ft (noncombustible). Roof signs: 24 ft (solid), 75/40 ft (open by construction type), 50/35 ft (closed). Projecting signs: must not exceed roof/cornice height (limited exception for 18" perpendicular signs). Marquee signs: max 6 ft above, 1 ft below, 8 ft total vertical. | H109.1, H110.3-H110.5, H112.4, H113.3-H113.4 |
| 6 | **Clearance Requirements** | ❌ **fail** | Ground signs: min 3 ft bottom clearance above grade. Roof signs: min 6 ft between roof and lowest sign part, min 5 ft between supports. Vehicle areas: min 14 ft above grade (CEC 600.9). Pedestrian clearances: per local code (state code sets vehicle height only). | H109.2, H110.1, CEC 600.9(A) |
| 7 | **Structural — Wind Load Design** | ❌ **fail** | Signs must be designed for wind loads per CBC Chapter 16 / ASCE 7. Verify wind speed for project location (typically 110-115 mph V for Risk Category II in CA). Freestanding signs: ASCE 7 Section 29.3. Attached signs: components and cladding per Chapter 30. Construction documents must show loads, stresses, and anchors. | H105.3, CBC 1609, ASCE 7 Ch 29 |
| 8 | **Structural — Seismic Design** | ⚠️ **flag** | Signs designed for wind are generally deemed adequate for seismic (H105.4), but ASCE 7 Chapter 13 (nonstructural components) and Chapter 15 (nonbuilding structures) may apply. In Seismic Design Categories D-F (most of CA), verify seismic analysis for large or heavy signs. | H105.4, CBC 1613, ASCE 7 Ch 13/15 |
| 9 | **Structural — Attachment** | ❌ **fail** | Attachment to masonry/concrete/steel: metal anchors, bolts, or expansion screws of sufficient size. Wall signs: min 3/8" diameter, min 5" embedment. No wood block anchorage (except on wood buildings). Projecting signs: no nails/staples, min 3/8" supports, min 5/8" lag screws, turnbuckles required. No anchorage to unbraced parapets. | H105.6, H111.2, H112.1-H112.3 |
| 10 | **Structural — Foundation (Freestanding)** | ❌ **fail** | For ground/pole signs: verify foundation design per CBC Chapter 18. Must resist overturning from wind and seismic. Wood in ground contact must be pressure treated. Soil bearing analysis required for large signs. | H109.3, CBC Ch 18 |
| 11 | **Electrical — Branch Circuit** | ❌ **fail** | Each commercial occupancy must have a dedicated 20A branch circuit at each pedestrian entrance for signs. Neon signs: max 30A branch circuit. All other signs: max 20A. Sign loads are continuous loads (125% sizing). | CEC 600.5 |
| 12 | **Electrical — Disconnect** | ❌ **fail** | Each sign must have an externally operable switch or circuit breaker opening all ungrounded conductors, controlling no other load. Must be accessible. Located at point of entry to sign, within sight of sign, within sight of controller, or at marked remote location. Switch must be rated for inductive loads or 2x transformer/power supply current. | CEC 600.6 |
| 13 | **Electrical — Grounding & Bonding** | ❌ **fail** | All metal equipment must be grounded via equipment grounding conductor. All metal parts bonded together and to transformer/power supply EGC. Metal building parts shall NOT be used for bonding. Bonding conductors: copper min 14 AWG or copper-clad aluminum min 12 AWG. | CEC 600.7 |
| 14 | **Electrical — Listing & Labeling** | ❌ **fail** | Electric signs must be listed and labeled (UL 48), with installation instructions, and installed per listing. Field-installed skeleton tubing exempt from listing if installed per CEC. Markings: manufacturer name, input voltage, current rating, visible after installation. | CEC 600.3, 600.4 |
| 15 | **Electrical — Enclosure** | ❌ **fail** | Live parts (other than lamps/neon tubing) must be enclosed. Enclosures: metal or listed. Min metal thickness: copper/aluminum 0.020", steel 0.016". Metal parts protected from corrosion. | CEC 600.8 |
| 16 | **Electrical — GFCI** | ❌ **fail** | Portable/mobile signs in wet or damp locations: listed GFCI protection required, integral to attachment plug or within 12" of it. Cords: hard-service type with EGC. | CEC 600.10(C)(2) |
| 17 | **Electrical — Transformers/Power Supplies** | ❌ **fail** | Must be listed, accessible, securely fastened. Neon transformers: secondary-circuit ground-fault protection required (with exceptions). Max secondary voltage 15,000V. Max secondary current 300 mA. Working space: min 3 ft x 3 ft x 3 ft. Secondary outputs NOT in parallel or series. | CEC 600.21-600.24 |
| 18 | **Combustible Material Proximity** | ❌ **fail** | Sign must not subject adjacent combustible materials to temperatures >194 deg F. Min 2" spacing between wood/combustibles and incandescent/HID lamps. Internally illuminated signs: 2" min clearance from wiring to facing. Illumination by electrical means only — no open flames. | CEC 600.9(C), H106.1, H106.1.1 |
| 19 | **Wet Location Compliance** | ❌ **fail** | Exterior signs (wet location): weatherproof or listed watertight. Drain holes: 1/4" to 1/2", at every low point, no obstructions. Transformers/power supplies: weatherproof or outdoor type protected in sign body. | CEC 600.9(D), 600.21(C) |
| 20 | **Animated/Moving Devices** | ❌ **fail** | Signs with moving sections/ornaments: fail-safe device required to prevent release. Must support full dead weight. Max center-of-gravity shift: 15 inches. Fail-safe independent of operating mechanism. | H108.1 |
| 21 | **Sign Identification** | ⚠️ **flag** | Outdoor advertising display signs requiring permits must be marked with erector/maintainer name and permit number (or approved ID) on front. | H104.1 |
| 22 | **Construction Documents** | ⚠️ **flag** | Plans must show dimensions, materials, construction details, loads, stresses, and anchors. For illuminated signs: electrical plan showing branch circuit, disconnect location, transformer/power supply, and wiring methods. | H105.2, CEC 600.5(D) |
| 23 | **Contractor Licensing** | ❌ **fail** | C-45 (Electrical Sign) license required for installing, altering, or repairing all types of signs. C-10 (Electrical) for electrical wiring to sign. B (General Building) may perform structural work. | B&P Code 7028 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/sign-electrical.md` — Sign Electrical Requirements
- `references/sign-materials-fire.md` — Sign Material and Fire Resistance Requirements
- `references/sign-structural.md` — Sign Structural Requirements
- `references/sign-types-clearances.md` — Sign Types, Classifications, and Clearances

**Laguna Beach rules**

- `references/city-sign-ordinance.md` — Laguna Beach Sign Regulations (LBMC Chapter 25.54)

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
