---
name: sign
description: "Sign permits in Laguna Beach, CA. A wall, monument, blade, or awning sign, new or replaced, with its attachment and electrical. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions sign in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2 CBC Appendix H + Chapter 31; Part 3 CEC Article 600; Chapter 16 structural); LBMC Chapter 25.54 (Sign Regulations), Chapter 25.05 (Design Review)"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-10-10"
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
3. **Internally illuminated signs prohibited** -- 25.54.016(E) lists, verbatim: "Excepting marquees, internally illuminated signs;". Marquees are the only exception. Channel letters are not excepted: a front-lit channel letter with a translucent face is "directly lit from an interior light source contained within the sign structure through a transparent or translucent surface" (25.54.006 "Internally illuminated sign"), so it is prohibited. Allowed: indirect lighting ("spotlighting or backlighting", 25.54.006 "Indirectly lighted"; 25.54.010(C)(1)), which on our reading includes halo (reverse channel) letters with opaque faces
4. **Electronic/digital signs prohibited** -- EMCs and digital signs prohibited (except as interior building signs)
5. **Animated signs prohibited** (except interior building signs)
6. **Roof signs prohibited** in all use categories
7. **Pole signs prohibited**
8. **Backlit awning/canopy signs prohibited**
9. **Luminance limits** -- 25.54.010(C)(3) table by ambient light area: 1-70 candelas/sq ft (low), 71-100 (medium), 101-140 (high). No automatic-dimming mandate; the Director may order dimming of a sign found excessively bright
10. **Approval path** -- Director approves conforming signs (letters 14 in or less, within area cap, or per a master sign program); all others go to the Planning Commission (25.54.018(E), Ord. 1732)
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

If the sign type/use combination is "N", the sign is prohibited as designed ("not allowed under any circumstances", 25.54.010(A)). Do not stop at "redesign". Go to STEP 2A and give both options.

#### STEP 2 -- Check Prohibited Signs List

Cross-reference against Section 25.54.016 prohibited signs list:
- Animated signs (except interior)
- Internally illuminated signs, except marquees (25.54.016(E): "Excepting marquees, internally illuminated signs;"). Channel letters lit through a translucent face are internally illuminated and prohibited
- Electronic message centers / digital signs (except interior)
- Roof signs, pole signs, billboards, portable signs
- Back-lit awning/canopy signs
- Signs emitting sound, odor, or visible matter

#### STEP 2A -- Prohibited Type or Over a Table 2 Limit: Two Options

Give the applicant both options:

1. **Redesign to conform.** A conforming sign (for example a monument sign 6 ft or less with external or halo lighting) can be Director-approved under 25.54.018(E)(2).
2. **Sign permit plus a variance (LBMC 25.05.025).** City practice since Ord. 1732: a sign that needs a variance is taken in on the commercial zoning plan check (ZPCC) intake with the variance filed beside the sign permit; no decision on such a case has been published yet. The sign is not eligible for Director approval, so the Planning Commission decides it (25.54.018(E)(5)), and the Commission acts as the Board of Adjustment on a variance tied to a matter it is deciding (25.05.025(J)). Noticed public hearing (25.05.025(E)(1)). All four findings of 25.05.025(F) are required, starting with special circumstances of the property (size, shape, topography, location or surroundings).

Whether a variance can authorize a sign type the code calls "not allowed under any circumstances" (25.54.010(A), 25.54.016) is **UNSETTLED; confirm with Planning at pre-application**. The findings are hard to make for a prohibited type, so say redesign is the surer path. A variance from a Table 2 number (height, area) is the ordinary use of 25.05.025. The 25.54.018(G) "extraordinarily creative" bonus allows up to 25% more area or height at the Planning Commission without a variance, but it does not reach a prohibited type.

#### STEP 3 -- Check Design Standards

Use Table 2 (in reference file `references/city-sign-ordinance.md`) to verify:
- Maximum number of signs permitted
- Maximum sign area
- Maximum height
- Other specifications (setbacks, clearances, projections)
- Total site sign area (1 sq ft per foot of frontage, max 150 sq ft)

#### STEP 4 -- Check Illumination

If illuminated:
- "Where not otherwise restricted, signs may be indirectly lighted" (25.54.010(C)(1)): external lighting (spotlighting) or backlighting. Halo (reverse channel) letters with opaque faces read as backlighting (our reading; confirm with Planning)
- No internally illuminated sign of any kind, cabinet or channel letter, except a marquee (25.54.016(E))
- No backlit awnings
- Luminance: the 25.54.010(C)(3) table, in candelas per square foot by ambient light area: 1 to 70 for LOW areas (most residential areas and the beaches); 71 to 100 for MEDIUM areas (isolated signs, or next to low areas); 101 to 140 for HIGH areas (downtown, highly lighted streets or parking areas, high sign competition). Measured with a light meter. No automatic dimming is required, but "the director of community development may order the dimming of any sign illumination determined to be excessively bright" (25.54.010(C)(3))
- Front lighting fixtures mount from the top of the sign structure (25.54.010(C)(3))
- No high intensity discharge sources (mercury vapor, metal halide, high pressure sodium) (25.54.010(C)(1)); shield the source to light only the sign (25.54.010(C)(2))
- Lighting that depicts action makes it an animated sign, prohibited except as an interior building sign (25.54.006 "Animated sign"; 25.54.016(A))

#### STEP 5 -- Determine Approval Path

Sign permits are decided under LBMC 25.54.018 as amended by Ord. 1732 §§ 47-48 (signed text pp. 74-75), not under the §25.05.040 Design Review lists. The approval authority is the Director of Community Development for signs eligible under 25.54.018(E), otherwise the Planning Commission (25.54.006 "Approval authority").

| Sign | Approval authority | Source |
|------|-------------------|--------|
| Sign in compliance with an approved master sign program | Director (administrative) | 25.54.018(E)(1) |
| Sign that meets all Ch. 25.54 design standards (25.54.010, Tables 1 and 2), keeps total site signage within the maximum, and has letter or font height **14 in or less** | Director (administrative) | 25.54.018(E)(2) (Ord. 1732 § 48 raised the limit from 8 in) |
| Temporary sign complying with 25.54.020 (not City Council special-event signs) | Director | 25.54.018(E)(3) |
| **Replacement** of a sign previously authorized by a sign permit, meeting all current design standards | Director | 25.54.018(E)(4) (added by Ord. 1732) |
| Luminous tube (neon) sign | Planning Commission (never administrative) | 25.54.018(E) |
| Any sign not eligible above (e.g. letters over 14 in, over the site area cap, not meeting a standard) | **Planning Commission** | 25.54.018(E)(5) |
| Sign of a prohibited type, or over a Table 2 limit, kept as designed | Planning Commission sign permit plus a variance, Commission as Board of Adjustment (STEP 2A) | 25.54.018(E)(5); 25.05.025(J) |
| Master sign program (new office/shopping center construction or substantial facade work with four or more businesses) | Planning Commission | 25.54.010(D) as amended |
| **Amending** an approved master sign program (changing its common standards: letter size, sign size, types, placement, lighting, number of signs), or a sign that departs from it | Planning Commission, as a master sign program application ("For new and amended Master Sign Programs, include all existing signs", City Sign Permit application). Ch. 25.54 has no separate amendment rule: the Commission sets the program's conditions (25.54.010(D)), only a sign "in compliance with an approved master sign program" is administrative ((E)(1)), and the 25.05.060 change rule does not list sign permits. A sign that departs from the program can still be administrative if it meets every (E)(2) test on its own; otherwise the Commission. Check the program's approval resolution for a delegated minor-change clause; for an arts or cultural organization's program the Commission may authorize Director approval of changes (25.54.026(C)). Ch. 25.54 does not use "planned sign program"; a program by any name that sets common standards for a multi-business site is read as a master sign program. One business's own "sign program" (the drawings every sign permit files, 25.54.018(A)) changes by a new sign permit routed by (E) | 25.54.010(D); 25.54.018(A), (E)(1), (E)(5); 25.54.026(C) |
| Up to 25% more sign area or height for an "extraordinarily creative" design | Planning Commission only | 25.54.018(G) as amended |
| Arts and cultural organizations' signs, facade changes, sign programs | Planning Commission | 25.54.026 as amended ("such as" the six named organizations; no longer a closed list) |

- **Ask whether the building has a sign program before saying it has none.** A center or building with four or more businesses may have an approved master sign program (25.54.010(D)), and the Director route under (E)(1) and every new sign there depend on it. `permit_status` and `lookup_property` do not reliably show one. Ask the resident or the property manager, and say Planning can confirm. Only say "no program" when the resident or a record says so; otherwise give both branches (with a program: must comply or amend; without: the (E)(2) tests).
- The Director may refer any administrative sign to the Planning Commission (25.54.018(E)).
- **Appeals:** under §25.05.070 as replaced by Ord. 1732 (on the City form within 14 calendar days). The former 10-business-day sign appeal was deleted (25.54.018(F)).
- **Design Review lists:** Ord. 1732's §25.05.040 has no sign item and no Sign Quality criterion. A sign is not Design Review unless the sign structure independently matches a (B)(1) item (for example any improvement over 15 ft, (B)(1)(c), or work on a historic resource, (B)(1)(d)/(B)(3)(a)(iv)), or the Director refers it. Where a source still says signs need "design review", say the current route is the 25.54 sign permit and **confirm with Planning**.
- **Downtown Specific Plan:** signs there are reviewed against the DSP urban design guidelines (25.54.018(D)(5)).

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
| Internal illumination | Allowed (with electrical code compliance) | **Prohibited** except marquees (25.54.016(E)); channel letters lit through a translucent face included |
| Electronic/digital signs | Allowed (with electrical code compliance) | **Prohibited** (except interior building signs) |
| Roof signs | Allowed (with structural requirements) | **Prohibited** |
| Pole signs | Allowed (as ground/freestanding) | **Prohibited** |
| Animated signs | Allowed (with fail-safe device) | **Prohibited** (except interior) |
| Franchise/standardized signs | No state restriction | **Prohibited** (logos max 20% of sign area) |
| Local approval | Not required by state | Sign permit: Director for conforming signs, Planning Commission otherwise (25.54.018(E)) |
| Luminance | No state standard | 1-140 candelas/sq ft by ambient light area (25.54.010(C)(3)); no auto-dimming mandate; Director may order dimming |
| Neon/luminous tube | Allowed per CEC Article 600 | Interior only, 4+ ft from window, 3 sq ft max, single color |

---

### Key Laguna Beach Sign Facts

- **OTC eligible**: Yes -- simple commercial signs meeting all standards
- **Roof signs**: Prohibited
- **Pole signs**: Prohibited (25.54.016(K)); a variance request is possible but UNSETTLED (STEP 2A)
- **Internally illuminated signs**: Prohibited, cabinet or channel letter, except marquees (25.54.016(E))
- **Digital/EMC signs**: Prohibited (except interior)
- **Max total sign area**: 1 sq ft per ft of frontage, 150 sq ft cap
- **Max freestanding height**: 6 ft
- **Max freestanding area**: 50 sq ft total, 25 sq ft per face
- **Downtown area**: More restrictive (wall 15 sq ft, temporary 5 sq ft, window 5 sq ft)
- **Neon signs**: Interior only, 4+ ft from window, 3 sq ft max
- **Franchise signs**: Prohibited (logos allowed if <20% of sign area)
- **Temporary signs**: Max 30 days + 30-day extension, 60 days/year total
- **Approval**: Director if 25.54.018(E) eligible (letters 14 in or less, meets standards and area cap, master-program sign, temporary, or replacement of a permitted sign); otherwise Planning Commission. Appeals per §25.05.070 (14 calendar days)
- **Sign programs**: Required for multi-tenant buildings (Planning Commission approval)
- **Arts and cultural organizations**: Planning Commission sign/facade discretion (25.54.026, "such as" the six named organizations)

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
