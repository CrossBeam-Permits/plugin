# California Baseline — Siding Replacement

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Siding Replacement Permit Review

This skill covers **state-level** California requirements for residential exterior siding and wall covering replacement permits. The primary code path is the California Residential Code (CRC Chapter 7) for dwellings, with supplemental requirements from the CBC (Chapter 14), Energy Code (Part 6), and WUI Code (Part 7).

**What this covers:**
- Siding replacement (full removal and re-clad) and siding overlay
- Wall covering materials, minimum thicknesses, and standards
- Nailing schedules and fastener requirements by material type
- Weather-resistive barrier (WRB/housewrap) installation
- Flashing at windows, doors, penetrations, and wall intersections
- WUI fire-resistive exterior wall covering requirements
- Energy code wall insulation triggers when cavity is exposed
- Stucco (cement plaster) and EIFS systems
- Vapor retarder requirements
- Stone and masonry veneer on wood-frame walls
- Lead paint and asbestos abatement for pre-1978/pre-1981 homes
- Material compatibility (dissimilar metals, moisture)

**What this does NOT cover:**
- New construction wall framing design (see structural engineer)
- Interior wall finishes (drywall, plaster -- interior only)
- Window or door replacement (see separate fenestration skill)
- Solar PV or equipment mounted on walls
- Commercial curtain wall or storefront systems

---

### How to Use This Skill

1. Determine whether the project is **residential** (CRC) or **commercial** (CBC)
2. Walk through the Decision Tree Router below
3. For each checklist item, load the referenced file from `/` as needed
4. See `../SKILL.md` for the full reference file catalog

---

### Decision Tree Router

#### STEP 1 -- Determine Code Path

| Building Use | Code | Key Chapter |
|---|---|---|
| Single-family dwelling, duplex, townhouse <=3 stories | CRC | Chapter 7 (R703) |
| Commercial, light commercial, multifamily >3 stories | CBC | Chapter 14 (1402-1408) |

Both codes require weather-resistive barriers, flashing, and corrosion-resistant fasteners. The CRC provides prescriptive nailing schedules (Table R703.3(1)); the CBC adds fire propagation testing (NFPA 285) for taller buildings.

#### STEP 2 -- What Type of Review Is This?

| Review Type | Load These References |
|---|---|
| **Full permit review** (form data in, pass/fail out) | `wall-covering-materials.md`, `weather-barrier-flashing.md` + others as triggered |
| **Material/fastener question only** | `wall-covering-materials.md` |
| **WRB/flashing question** | `weather-barrier-flashing.md` |
| **WUI fire zone question** | `wui-exterior.md` |
| **Energy/insulation question** | `energy-wall-insulation.md` |
| **Stucco question** | `stucco-systems.md` |
| **Lead/asbestos question** | `lead-asbestos-abatement.md` |

#### STEP 3 -- Review Checklist

Walk each item in order. For every check, record PASS / FAIL / FLAG / N/A with the code section cited.

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 1 | **Scope: What Is Being Replaced?** | Identify existing siding material and proposed new material. Full removal vs. overlay. If overlay: verify compatibility and structural adequacy for added weight. Note year built -- triggers lead/asbestos checks. | CRC R703.1; CBC 1401.1 | `wall-covering-materials.md` |
| 2 | **Material Standards** | Verify proposed siding material meets applicable ASTM/ANSI standard. Must be certified and labeled by approved agency where required (vinyl per ASTM D3679, fiber cement per ASTM C1186, etc.). Check minimum thickness per Table R703.3(1) or CBC Table 1404.2. | CRC R703.3, Table R703.3(1); CBC 1403 | `wall-covering-materials.md` |
| 3 | **Fastener Schedule** | Verify nailing schedule per material type: fastener size, spacing, penetration depth. Fasteners must be corrosion-resistant (aluminum, galvanized, stainless, or rust-preventative coated). Aluminum siding requires aluminum nails only (no dissimilar metals). Min penetration 1-1/2" into framing for most materials. | CRC R703.3, R703.3.3, R703.3.4, Table R703.3(1) | `wall-covering-materials.md` |
| 4 | **Weather-Resistive Barrier** | Min one layer WRB (ASTM D226 Type 1 / #15 felt, or ASTM E2556 housewrap, or approved equivalent) over all exterior walls behind cladding. Horizontal application, upper over lower min 2" lap, 6" at joints. Continuous to top of walls. For stucco: two-layer or 60-minute WRB required. | CRC R703.2, R703.7.3; CBC 1403.2 | `weather-barrier-flashing.md` |
| 5 | **Flashing** | Corrosion-resistant flashing required at: windows/doors, chimneys, masonry/frame intersections, under copings/sills, above projecting trim, porch/deck/stair attachments, wall/roof intersections, built-in gutters. Self-adhered flashing per AAMA 711. Pan flashing at window/door sills where manufacturer instructions not provided. | CRC R703.4, R703.4.1; CBC 1404.4 | `weather-barrier-flashing.md` |
| 6 | **WUI Fire Zone** | If project is in a Wildland-Urban Interface area or Fire Hazard Severity Zone: exterior wall covering must be noncombustible, ignition-resistant building material, or fire-retardant-treated wood. Vinyl and untreated wood NOT permitted. Fiber cement, metal, and stucco are compliant. Paint/coatings NOT an approved method. 6" metal flashing at ground, deck, and roof intersections. | WUI Code 503.2, 504.5; CRC R337 | `wui-exterior.md` |
| 7 | **Energy Code -- Wall Insulation** | If siding replacement exposes wall cavity (sheathing removed): cavity insulation required -- R-15 in 2x4, R-21 in 2x6 framing. If siding replaced without cavity access: no insulation trigger. If adding continuous insulation (foam board): verify fastener schedule accommodates foam thickness. CF-1R/CF-2R documentation required if insulation installed. | Energy Code 150.2(b)1 | `energy-wall-insulation.md` |
| 8 | **Stucco-Specific** | If stucco: three-coat over metal lath (min 7/8" total), two-coat over masonry. Weep screed mandatory: min 4" above earth, 2" above paved. Lath: 7" OC along framing, 24" OC between. Curing: min 48 hrs between coats, 7 days before finish coat. EIFS with drainage required over wood/steel frame (min 90% drainage efficiency per ASTM E2273). | CRC R703.7; CBC 1407 | `stucco-systems.md` |
| 9 | **Vapor Retarder** | For most of Southern California (IECC Climate Zone 3): vapor retarder NOT required (Class III / latex paint is sufficient). For mountain/inland areas (IECC CZ 4-6): Class II or III vapor retarder required per Table R702.7(2). When adding continuous insulation: verify compatibility with vapor retarder class per Tables R702.7(3)-(5). | CRC R702.7; CBC 1404.3 | `energy-wall-insulation.md` |
| 10 | **Masonry/Stone Veneer** | If anchored stone or masonry veneer: limited to first story, max 5" thick (SDC A/B/C). Wood/steel frame backing required. Min 1" airspace between veneer and sheathing. Weepholes max 33" OC above flashing. Corrosion-resistant metal ties max 2.67 sq ft per tie. Lintels over openings -- noncombustible, min 4" bearing. | CRC R703.8; CBC 1404.7 | `wall-covering-materials.md` |
| 11 | **Wind Resistance** | Siding must resist wind loads per Tables R301.2.1(1) and (2). For most of California (110-115 mph, Exposure B): standard attachment per Table R703.3(1) is adequate. Where design wind pressure >30 psf or Table R703.3.2 limits exceeded: engineered design required. | CRC R703.1.2, R703.3.2 | `wall-covering-materials.md` |
| 12 | **Lead Paint (Pre-1978)** | If year built before 1978: lead paint presumed unless tested negative. EPA RRP Rule applies -- certified contractor required. Lead-safe work practices mandatory (containment, wet methods, HEPA). Cannot use open-flame burning, power sanding without HEPA, or dry scraping >2 sq ft. | 40 CFR 745; Cal/OSHA 1532.1 | `lead-asbestos-abatement.md` |
| 13 | **Asbestos (Pre-1981)** | If year built before 1981 or existing material is asbestos-cement (Transite): asbestos survey required before removal. SCAQMD Rule 1403 notification 10 working days before work (SoCal). C-22 licensed contractor for removal. Wet removal, intact panels, double-bagged disposal. | Cal/OSHA 1529; SCAQMD 1403 | `lead-asbestos-abatement.md` |
| 14 | **Ground Clearance** | Vinyl/polypropylene siding: min 6" above grade, 1/2" from adjacent surfaces. Stucco weep screed: min 4" above earth, 2" above paved. Wood siding: per manufacturer (typically 6-8" recommended). All materials: maintain clearance to prevent moisture wicking and pest entry. | CRC R703.3.1, R703.7.2.1 | `wall-covering-materials.md` |
| 15 | **Contractor Licensing** | C-35 (Lathing & Plastering) for stucco, B (General Building) for general siding, C-22 (Asbestos Abatement) where ACM present. EPA RRP firm certification for pre-1978 lead paint. Workers' compensation insurance required. | B&P Code 7028 | N/A |

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
- **N/A** -- Does not apply to this project (e.g., WUI checks when not in fire zone)

---

### Quick-Reference Tables

#### Siding Material Minimum Thickness

| Material | Min Thickness | Standard | Code Section |
|---|---|---|---|
| Vinyl siding | 0.035" | ASTM D3679 | CRC R703.11 |
| Fiber cement panel | 5/16" | ASTM C1186 Type A | CRC R703.10.1 |
| Fiber cement lap | 5/16" | ASTM C1186 Type A | CRC R703.10.2 |
| Hardboard panel | 7/16" | ANSI A135.5 | CRC R703.5 |
| Hardboard lap | 7/16" | ANSI A135.5 | CRC R703.5 |
| Wood bevel | 7/16" butt | -- | Table R703.3(1) |
| Wood structural panel | 3/8"-1/2" | ANSI/APA PRP-210 | CRC R703.5 |
| Aluminum | 0.019"-0.024" | AAMA 1402 | CBC 1403.5.1 |
| Steel | 29 gage | Approved type | Table R703.3(1) |
| Stucco (3-coat/metal lath) | 7/8" | ASTM C926 | CRC R703.7 |

#### WRB Requirements by Cladding Type

| Cladding | WRB Requirement | Code Section |
|---|---|---|
| Lap siding (wood, fiber cement, vinyl) | 1 layer: #15 felt or ASTM E2556 Type 1/2 | CRC R703.2 |
| Panel siding | 1 layer: #15 felt or ASTM E2556 Type 1/2 | CRC R703.2 |
| Stucco (dry climate) | 2 layers 10-min Grade D paper OR 1 layer 60-min Grade D + drainage | CRC R703.7.3.1 |
| Stucco (marine climate) | Per dry climate + min 3/16" drainage space | CRC R703.7.3.2 |
| EIFS with drainage | Per R703.2 or ASTM E2570, between EIFS and sheathing | CRC R703.9.2 |
| Masonry veneer | Per R703.2, continuous behind veneer | CRC R703.8 |

#### Flashing Required Locations

| Location | Requirement | Code Section |
|---|---|---|
| Windows and doors | Pan flashing at sill + head/side protection | CRC R703.4.1 |
| Chimney/masonry intersections | Projecting lips both sides | CRC R703.4 |
| Under copings, sills | Continuous | CRC R703.4 |
| Above projecting trim | Continuous | CRC R703.4 |
| Porch/deck/stair to wall | Required | CRC R703.4 |
| Wall/roof intersection | Required | CRC R703.4 |
| Built-in gutters | Required | CRC R703.4 |
| WUI zones (additional) | 6" metal flashing at ground/deck/roof | WUI 504.5.1 |

#### Insulation Trigger Summary

| Scenario | Insulation Required? | R-Value |
|---|---|---|
| Siding replaced, cavity NOT exposed | No | -- |
| Siding replaced, cavity IS exposed (2x4) | Yes | R-15 cavity |
| Siding replaced, cavity IS exposed (2x6) | Yes | R-21 cavity |
| Continuous insulation added over sheathing | Counts toward wall R-value | Per product |

#### WUI Siding Compliance

| Material | Compliant in WUI? | Why? |
|---|---|---|
| Fiber cement | Yes | Ignition-resistant |
| Metal (steel, aluminum) | Yes | Noncombustible |
| Stucco | Yes | Noncombustible |
| Stone/masonry | Yes | Noncombustible |
| Fire-retardant-treated wood | Yes | If labeled for exterior use |
| Untreated wood | **No** | Combustible |
| Vinyl | **No** | Combustible |
| Polypropylene | **No** | Combustible |

---

### Key Principles

1. **WRB is mandatory behind all cladding.** At least one layer of weather-resistive barrier (#15 felt or approved housewrap) must be installed over studs or sheathing on all exterior walls. Stucco requires two-layer or 60-minute WRB.
2. **Flashing protects the weak points.** Every window, door, penetration, and wall intersection must have corrosion-resistant flashing to redirect water outward. Missing or damaged flashing is the #1 cause of moisture intrusion in walls.
3. **WUI zones restrict materials.** In fire hazard areas, vinyl and untreated wood siding are prohibited. Fiber cement, metal, and stucco are the standard WUI-compliant options.
4. **Cavity exposure triggers insulation.** If siding replacement opens the wall cavity, insulation must be installed to current energy code: R-15 (2x4) or R-21 (2x6). No cavity access = no insulation trigger.
5. **Dissimilar metals cause corrosion.** Never mix aluminum and steel, or copper and galvanized fasteners. Use same-metal family or stainless steel.
6. **Stucco has special rules.** Three coats over metal lath, weep screed at base, curing times between coats, and stricter WRB requirements distinguish stucco from all other siding types.
7. **Pre-1978 = lead, pre-1981 = asbestos.** Year built determines hazardous material testing requirements. These are not optional -- they are federal and state law.
8. **Ground clearance prevents moisture damage.** All siding must maintain minimum clearance from grade to prevent wicking, splash-back, and pest access.
