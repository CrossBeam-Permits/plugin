---
name: siding-replacement
description: "Siding Replacement permits in Laguna Beach, CA. Exterior wall covering replaced across a wall or elevation: siding, stucco, or shingle re-clad with its weather barrier and flashing. A small patch is general-building. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions siding replacement in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2 CBC, Part 2.5 CRC, Part 6 Energy, Part 7 WUI); LBMC Ch. 14.70 (WUI Code), Ch. 14.50 (Building Code amendments), Ch. 25.05 (Design Review), Title 15 (Fire Prevention)"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-07-22"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Siding Replacement Permit

Handles siding replacement permits in Laguna Beach end-to-end. Scope: Exterior wall covering replaced across a wall or elevation: siding, stucco, or shingle re-clad with its weather barrier and flashing. A small patch is general-building.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a siding replacement permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Siding Replacement Permit

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

This skill covers Laguna Beach's city-specific siding and exterior wall covering replacement requirements. **VHFHSZ fire-resistive exterior wall requirements and Design Review Board triggers make Laguna Beach siding replacement significantly more complex than typical CA cities.**

**How this skill relates to state code**: The `california-siding-replacement` skill covers CRC/CBC state requirements. This skill covers what Laguna Beach adds -- primarily the VHFHSZ fire-resistive exterior wall covering requirements, Design Review triggers, and coastal zone implications. **Load state code first**, then this skill.

---

### Decision Tree Router

| Project Type | Route |
|-------------|-------|
| **Like-for-like siding replacement** (same material, same appearance) | OTC may be eligible; Zone Clearance under §25.05.040(B)(2)(c), subject to overlays |
| **Siding material change** (e.g., wood to fiber cement) | Match current closed lists; ordinarily Zone Clearance as a non-major alteration/improvement ≤15 ft, unless another trigger applies |
| **Siding replacement as part of major remodel** | Full plan review, Design Review under §25.05.040(B)(1)(a) |

---

### VHFHSZ Fire-Resistive Exterior Wall Requirements

Laguna Beach is predominantly Very High Fire Hazard Severity Zone (citywide coverage: `../city-reference/SKILL.md`). Fire-resistive exterior wall covering requirements are CRITICAL for any siding replacement:

#### Laguna Beach WUI Amendments (Ch. 14.70)

##### Exterior Wall Coverings (Section 14.70.030, amending WUI Code 504.5.2)

Exterior wall covering, or wall assembly including insulation, must comply with ONE of:

1. **Noncombustible material** (stucco, metal, stone/masonry)
2. **Ignition-resistant building material** labeled for exterior use (fiber cement)
3. **Fire-retardant-treated wood** labeled for exterior use per CBC Section 2303.2
4. **Fire-retardant-treated wood shingles/shakes** qualified as "Class B" roof covering per CBC Section 1505.6 -- acceptable as wall covering when installed over solid sheathing

**PROHIBITED MATERIALS in VHFHSZ:**
- Vinyl siding -- combustible, does NOT comply
- Untreated wood siding -- combustible, does NOT comply
- Polypropylene siding -- combustible, does NOT comply

##### CBC Section 705.1 Amendment (Section 14.50.112)

Laguna Beach amends CBC 705.1 to require that **the most restrictive requirements of Section 705 AND Chapter 5 of the California Wildland-Urban Interface Code shall govern** for all buildings in Fire Hazard Zones. This means exterior wall coverings must satisfy both the CBC fire-separation requirements AND the WUI Code material restrictions simultaneously.

##### Minor Repair Exception (Section 14.70.015)

With the approval of the **building official**, minor repairs or replacement of exterior materials may be done with the **same materials as existing** on the building. This exception:
- Requires building official approval (not automatic)
- Only applies to minor repairs or replacement
- Only allows same-as-existing material
- Does NOT permit upgrading to a new non-compliant material
- A full re-clad of the entire building is NOT a "minor repair"

**Practical impact**: A homeowner patching a small damaged section of existing vinyl siding could potentially get building official approval under this exception. A full house re-side does not qualify.

---

### Current Design Review / Zone Clearance Route

Urgency Ordinance No. 1732 repealed the former broad exterior-work default, partial-facade exemption, and wildfire-resistant-material `(B)(2)(w)` exemption.

- In-kind replacement takes Zone Clearance under current §25.05.040(B)(2)(c).
- Other non-major siding alteration/addition and improvements no more than 15 ft ordinarily take Zone Clearance under (B)(2)(a)-(b), unless another closed-list trigger applies.
- A major remodel requires Design Review under (B)(1)(a); an improvement over 15 ft under (B)(1)(c); ESA work under (B)(1)(e) absent the enacted peer-reviewed professional determination.
- The Director retains the enacted referral authority.

WUI fire-resistant material compliance remains mandatory, but it is no longer its own categorical Design Review exemption. Do not cite former `(B)(2)(d)` or `(B)(2)(w)`.

---

### OTC Eligibility

**Exterior siding replacement is OTC-eligible per the city reference OTC item 5.** Hours, the full 11-item OTC list, and the disqualifiers live in `../city-reference/SKILL.md` §"Permit Processing Tracks".

**However**, OTC eligibility for the building permit does NOT exempt the project from:
- Design Review (if triggered per above)
- Coastal Development Permit (if in Coastal Zone)
- WUI material compliance (Ch. 14.70)

A siding replacement can be OTC for the building permit while still requiring a separate DRB hearing or CDP.

---

### Coastal Zone Implications

Most of Laguna Beach falls within the California Coastal Zone:
- **Coastal Development Permit (CDP)** may be required per Chapter 25.07
- Siding replacement that constitutes "development" under the Coastal Act requires a CDP unless exempt under Section 25.07.008
- Like-for-like replacement or minor repair is generally exempt from CDP
- Material changes that alter the exterior appearance may trigger CDP review
- May be subject to California Coastal Commission appeal

---

### Sprinkler Retrofit Trigger Interaction

**Two triggers, either one fires.** Full rule: `../residential-remodel/references/city-sprinkler-retrofit.md` — the single residential retrofit reference. Do not restate it here.

- **Title 15 §1103.5.4** (scope, Ord. 1726) — alteration of ≥50% of the building, OR work on ≥50% of the exterior, OR an added story.
- **Ch. 14.52.030** (valuation, Ord. 1725) — cumulative additions, alterations and repairs in any three-year period exceeding 50% of the pre-work valuation of the dwelling + attached garage.

#### Siding-specific note — the fire-resistant-siding exception is narrow

> **Exception:** Work that consists only of the installation of fire-resistant siding.

Installing fire-resistant siding (fiber cement, stucco, metal) as a standalone project does not fire **§1103.5.4**, even when it covers the whole exterior. Two limits on that:

1. **"Consists only of."** Add windows, roofing or interior work and the exception is gone, and the combined exterior scope can reach the §1103.5.4 50%-exterior prong.
2. **The exception does not reach Ch. 14.52.030.** A full re-side is high-value work. Its valuation counts toward the 50% / three-year cumulative total, so a fire-resistant re-side can still fire the retrofit through Ch. 14.52.030. Always check the three-year permit history.

**Do not substitute CBC §903.6 / LBMC §14.50.104 for Ch. 14.52.030 on a CRC-track house.** Section 903.6 is not non-residential-only—it expressly covers CBC-track Group R—but Ch. 14.52.030 is the specific valuation rule for a one- or two-family dwelling.

---

### Major Remodel Interaction

If the siding replacement is part of a larger project that constitutes a **major remodel** (50% or more of original gross floor area in additions/alterations):
- Full plan review required (not OTC)
- Full DRB hearing required
- Fuel modification plan may be required (Ch. 14.70, Section 613)
- Fire Safety Standards Review required for a major remodel (Section 25.05.040(C)(4); Fire Department or Building Division, as applicable)
- New construction standards apply throughout

---

### Laguna Beach Siding Replacement Review Checklist -- City Overlay

Walk these items AFTER completing the state-level checklist. For every check, record PASS / FAIL / FLAG / N/A with the code section cited.

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| LB-1 | **VHFHSZ Status** | Confirm the property is in VHFHSZ. If yes, all WUI exterior wall requirements apply. | Ch. 14.70 | `references/city-wui-exterior-walls.md` |
| LB-2 | **Wall Covering Material Compliance** | Proposed siding material must be noncombustible, ignition-resistant (labeled for exterior use), or FRT wood. Vinyl, untreated wood, and polypropylene are PROHIBITED. Verify labeling for ignition-resistant materials. | §14.70.030 (504.5.2) | `references/city-wui-exterior-walls.md` |
| LB-3 | **Minor Repair Exception** | If small area repair with same-as-existing material: building official approval may allow non-compliant material. Full re-clad does NOT qualify. | §14.70.015 (101.2 Exception) | `references/city-wui-exterior-walls.md` |
| LB-4 | **CBC 705.1 Dual Compliance** | Exterior wall coverings must satisfy BOTH CBC Section 705 AND WUI Chapter 5 -- most restrictive governs. | §14.50.112 (705.1) | `references/city-wui-exterior-walls.md` |
| LB-5 | **Planning route** | In-kind → Zone Clearance `(B)(2)(c)`; other non-major work ≤15 ft ordinarily → Zone Clearance `(B)(2)(a)-(b)`; apply major-remodel, height, ESA, and Director-referral checks. | §25.05.040(B)(1)(a), (c), (e); (B)(2)(a)-(c) | `references/city-wui-exterior-walls.md` |
| LB-6 | **Coastal Development Permit** | If property is in Coastal Zone: determine if siding work constitutes "development" requiring CDP. Like-for-like replacement generally exempt; material changes may trigger. | Ch. 25.07 | N/A |
| LB-7 | **Sprinkler Retrofit -- Fire-Resistant Siding Exception** | Installation of fire-resistant siding alone does NOT trigger sprinkler retrofit per §1103.5.4 exception. But verify cumulative 3-year valuation under §903.6. | Title 15 §1103.5.4; CBC §903.6 | `references/city-fire-amendments.md` |
| LB-8 | **Major Remodel Check** | If the overall project is a major remodel: Design Review applies and §25.56.011 classifies it as a new building. | §25.05.040(B)(1)(a); §25.56.011 | N/A |

#### Output Format

For each city-overlay check, produce:

```
## LB-[#]. [Check Name]
**Result:** PASS | FAIL | FLAG | N/A
**Code:** [Section number]
**Finding:** [1-2 sentence explanation]
```

---

### Key Laguna Beach Siding Replacement Facts

- **OTC eligible**: Yes -- exterior siding replacement is a listed OTC project type
- **VHFHSZ**: vinyl and untreated wood siding PROHIBITED
- **WUI code**: Ch. 14.70 Section 14.70.030 -- noncombustible or ignition-resistant required
- **Minor repair exception**: Same-material minor repairs OK with building official approval
- **Planning route**: classify under the current closed lists; WUI upgrading is not itself a categorical exemption
- **Coastal Zone**: Most of city -- CDP may be required for material changes
- **Sprinkler exception**: Fire-resistant siding installation alone does NOT fire the Title 15 §1103.5.4 scope trigger. It is NOT exempt from the Ch. 14.52.030 valuation trigger — re-side valuation counts toward the 50% / 3-year cumulative total. See `../residential-remodel/references/city-sprinkler-retrofit.md`
- **CBC 705.1**: Most restrictive of CBC 705 or WUI Chapter 5 governs

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Scope: What Is Being Replaced?** | ❌ **fail** | Identify existing siding material and proposed new material. Full removal vs. overlay. If overlay: verify compatibility and structural adequacy for added weight. Note year built -- triggers lead/asbestos checks. | CRC R703.1; CBC 1401.1 |
| 2 | **Material Standards** | ❌ **fail** | Verify proposed siding material meets applicable ASTM/ANSI standard. Must be certified and labeled by approved agency where required (vinyl per ASTM D3679, fiber cement per ASTM C1186, etc.). Check minimum thickness per Table R703.3(1) or CBC Table 1404.2. | CRC R703.3, Table R703.3(1); CBC 1403 |
| 3 | **Fastener Schedule** | ❌ **fail** | Verify nailing schedule per material type: fastener size, spacing, penetration depth. Fasteners must be corrosion-resistant (aluminum, galvanized, stainless, or rust-preventative coated). Aluminum siding requires aluminum nails only (no dissimilar metals). Min penetration 1-1/2" into framing for most materials. | CRC R703.3, R703.3.3, R703.3.4, Table R703.3(1) |
| 4 | **Weather-Resistive Barrier** | ❌ **fail** | Min one layer WRB (ASTM D226 Type 1 / #15 felt, or ASTM E2556 housewrap, or approved equivalent) over all exterior walls behind cladding. Horizontal application, upper over lower min 2" lap, 6" at joints. Continuous to top of walls. For stucco: two-layer or 60-minute WRB required. | CRC R703.2, R703.7.3; CBC 1403.2 |
| 5 | **Flashing** | ❌ **fail** | Corrosion-resistant flashing required at: windows/doors, chimneys, masonry/frame intersections, under copings/sills, above projecting trim, porch/deck/stair attachments, wall/roof intersections, built-in gutters. Self-adhered flashing per AAMA 711. Pan flashing at window/door sills where manufacturer instructions not provided. | CRC R703.4, R703.4.1; CBC 1404.4 |
| 6 | **WUI Fire Zone** | ❌ **fail** | If project is in a Wildland-Urban Interface area or Fire Hazard Severity Zone: exterior wall covering must be noncombustible, ignition-resistant building material, or fire-retardant-treated wood. Vinyl and untreated wood NOT permitted. Fiber cement, metal, and stucco are compliant. Paint/coatings NOT an approved method. 6" metal flashing at ground, deck, and roof intersections. | WUI Code 503.2, 504.5; CRC R337 |
| 7 | **Energy Code -- Wall Insulation** | ❌ **fail** | If siding replacement exposes wall cavity (sheathing removed): cavity insulation required -- R-15 in 2x4, R-21 in 2x6 framing. If siding replaced without cavity access: no insulation trigger. If adding continuous insulation (foam board): verify fastener schedule accommodates foam thickness. CF-1R/CF-2R documentation required if insulation installed. | Energy Code 150.2(b)1 |
| 8 | **Stucco-Specific** | ❌ **fail** | If stucco: three-coat over metal lath (min 7/8" total), two-coat over masonry. Weep screed mandatory: min 4" above earth, 2" above paved. Lath: 7" OC along framing, 24" OC between. Curing: min 48 hrs between coats, 7 days before finish coat. EIFS with drainage required over wood/steel frame (min 90% drainage efficiency per ASTM E2273). | CRC R703.7; CBC 1407 |
| 9 | **Vapor Retarder** | ⚠️ **flag** | For most of Southern California (IECC Climate Zone 3): vapor retarder NOT required (Class III / latex paint is sufficient). For mountain/inland areas (IECC CZ 4-6): Class II or III vapor retarder required per Table R702.7(2). When adding continuous insulation: verify compatibility with vapor retarder class per Tables R702.7(3)-(5). | CRC R702.7; CBC 1404.3 |
| 10 | **Masonry/Stone Veneer** | ❌ **fail** | If anchored stone or masonry veneer: limited to first story, max 5" thick (SDC A/B/C). Wood/steel frame backing required. Min 1" airspace between veneer and sheathing. Weepholes max 33" OC above flashing. Corrosion-resistant metal ties max 2.67 sq ft per tie. Lintels over openings -- noncombustible, min 4" bearing. | CRC R703.8; CBC 1404.7 |
| 11 | **Wind Resistance** | ⚠️ **flag** | Siding must resist wind loads per Tables R301.2.1(1) and (2). For most of California (110-115 mph, Exposure B): standard attachment per Table R703.3(1) is adequate. Where design wind pressure >30 psf or Table R703.3.2 limits exceeded: engineered design required. | CRC R703.1.2, R703.3.2 |
| 12 | **Lead Paint (Pre-1978)** | ⚠️ **flag** | If year built before 1978: lead paint presumed unless tested negative. EPA RRP Rule applies -- certified contractor required. Lead-safe work practices mandatory (containment, wet methods, HEPA). Cannot use open-flame burning, power sanding without HEPA, or dry scraping >2 sq ft. | 40 CFR 745; Cal/OSHA 1532.1 |
| 13 | **Asbestos (Pre-1981)** | ⚠️ **flag** | If year built before 1981 or existing material is asbestos-cement (Transite): asbestos survey required before removal. SCAQMD Rule 1403 notification 10 working days before work (SoCal). C-22 licensed contractor for removal. Wet removal, intact panels, double-bagged disposal. | Cal/OSHA 1529; SCAQMD 1403 |
| 15 | **Contractor Licensing** | ❌ **fail** | C-35 (Lathing & Plastering) for stucco, B (General Building) for general siding, C-22 (Asbestos Abatement) where ACM present. EPA RRP firm certification for pre-1978 lead paint. Workers' compensation insurance required. | B&P Code 7028 |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 14 | **Ground Clearance** | Vinyl/polypropylene siding: min 6" above grade, 1/2" from adjacent surfaces. Stucco weep screed: min 4" above earth, 2" above paved. Wood siding: per manufacturer (typically 6-8" recommended). All materials: maintain clearance to prevent moisture wicking and pest entry. | CRC R703.3.1, R703.7.2.1 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/energy-wall-insulation.md` — Energy Code Wall Insulation Requirements
- `references/lead-asbestos-abatement.md` — Lead Paint and Asbestos Abatement Requirements
- `references/stucco-systems.md` — Stucco (Exterior Plaster) and EIFS Requirements
- `references/wall-covering-materials.md` — Wall Covering Materials and Installation
- `references/weather-barrier-flashing.md` — Weather-Resistive Barrier and Flashing Requirements
- `references/wui-exterior.md` — WUI Fire-Resistive Exterior Wall Requirements

**Laguna Beach rules**

- `references/city-fire-amendments.md` — Laguna Beach Fire Code Amendments (Title 15)
- `references/city-wui-exterior-walls.md` — Laguna Beach WUI Code -- Fire-Resistive Exterior Wall Covering Requirements

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
