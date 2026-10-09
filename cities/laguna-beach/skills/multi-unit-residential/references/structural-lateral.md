---
title: "Seismic / Lateral System Requirements for Multi-Unit Residential"
category: structural
relevance: "Load when reviewing structural plans for lateral force-resisting system design, seismic design category determination, shear wall layout, diaphragm adequacy, load path completeness, or hold-down / anchor bolt detailing on wood-frame multi-unit residential buildings."
key_code_sections: "CBC 1604.4, 1604.5, 1604.8, 1604.9, 1605.1-1605.2, 1613.1-1613.3, 2302.1, 2305.1-2305.3, 2306.2-2306.3, 2307.1, 2308.2.1, 2308.10, ASCE 7-22 Ch 11-12, AWC SDPWS"
---

## Seismic / Lateral System Requirements for Multi-Unit Residential

### Seismic Design Category (SDC) Determination

The SDC governs nearly every lateral design decision: system selection, detailing requirements, analysis procedures, and inspection thresholds. It must be established at the start of design.

**Two permitted methods** (CBC 1613.2):
1. **Figure 1613.2(1)** — SDC from the structure risk category using USGS mapped values at default site conditions.
2. **ASCE 7 procedure** — Full site-specific determination using mapped spectral response acceleration parameters Ss and S1, site class, and risk category.

Where **Site Class DE, E, or F** soils are present (per geotechnical data or AHJ determination), the ASCE 7 procedure is **mandatory** — the simplified figure method is not permitted. (CBC 1613.2)

**ASCE 7 procedure summary** (ASCE 7-22, Ch 11):

| Step | Parameter | Description |
|------|-----------|-------------|
| 1 | Ss, S1 | Mapped MCER spectral response acceleration at short period and 1-second period (USGS web tool or ASCE 7 maps) |
| 2 | Site Class | A through F based on soil properties (default Site Class D when geotechnical data is absent per ASCE 7 11.4.3) |
| 3 | Fa, Fv | Site coefficients from ASCE 7 Tables 11.4-1 and 11.4-2 applied to Ss and S1 |
| 4 | SMS, SM1 | Site-adjusted spectral response: SMS = Fa x Ss, SM1 = Fv x S1 |
| 5 | SDS, SD1 | Design spectral response: SDS = 2/3 x SMS, SD1 = 2/3 x SM1 |
| 6 | Risk Category | From CBC Table 1604.5 (most multi-unit residential is Risk Category II) |
| 7 | SDC | From ASCE 7 Tables 11.6-1 and 11.6-2 based on SDS, SD1, and risk category — the more severe category governs |

**California-specific context for urban areas:**

Most of coastal and inland Southern California has mapped Ss values between 1.0 g and 2.5 g and S1 values between 0.4 g and 1.0 g. Combined with the typical default Site Class D (stiff soil), this places the vast majority of urban projects in **SDC D**. Sites near major faults (San Andreas, Newport-Inglewood, Elsinore) or on soft soils may reach **SDC E**. SDC E triggers more restrictive system limitations and detailing per ASCE 7 12.2.5.

Multi-unit residential buildings are typically Risk Category II per CBC Table 1604.5 (all buildings and structures except those listed in Risk Categories I, III, and IV). Buildings with occupant loads exceeding 5,000 would be Risk Category III. (CBC 1604.5)

### Why Conventional Light-Frame Construction Cannot Be Used for Multi-Story in SDC D

CBC Section 2308 (conventional light-frame construction) imposes strict limitations based on SDC:

| SDC | Allowable Stories per 2308.2.1 |
|-----|-------------------------------|
| A, B | 3 stories |
| C | 2 stories |
| **D, E** | **1 story** |

(CBC Table 2308.2.1)

This means that **any multi-story wood-frame building in SDC D or E cannot use the prescriptive conventional construction provisions of Section 2308** for its lateral system. It must be fully engineered per the allowable stress design path (Sections 2304, 2305, 2306) or the LRFD path (Sections 2304, 2305, 2307). (CBC 2302.1, 2308.2.1)

### Lateral Force-Resisting System Options for Wood-Frame Multi-Unit

**Engineered design is required** (CBC 2302.1 Items 1 or 2):
- **Allowable Stress Design (ASD)**: Sections 2304, 2305, 2306
- **Load and Resistance Factor Design (LRFD)**: Sections 2304, 2305, 2307

Both methods require compliance with **AWC SDPWS** (Special Design Provisions for Wind and Seismic) for shear wall and diaphragm design. (CBC 2305.1, 2306.3, 2307.1)

**Primary lateral system options for wood-frame (Type V-A) multi-unit:**

| System | ASCE 7 Table 12.2-1 Designation | R | Omega-0 | Cd | Height Limit SDC D |
|--------|--------------------------------|---|---------|----|--------------------|
| Wood structural panel shear walls | A.15: Light-frame (wood) walls sheathed with wood structural panels | 6.5 | 3 | 4 | 65 ft |
| Wood structural panel shear walls (designed per ASCE 7 14.5) | A.16: Light-frame (wood) walls with shear panels of all other materials | 2 | 2.5 | 2 | 35 ft |
| Steel-strap braced wall (if used) | Varies by system | Varies | Varies | Varies | Varies |

**For multi-unit residential, wood structural panel (plywood or OSB) shear walls are the standard system.** These provide R = 6.5 for SDC D with a 65-ft height limit, which accommodates 3- to 4-story wood-frame buildings. (ASCE 7 Table 12.2-1)

**Key requirements for wood structural panel shear walls in SDC D, E, or F** (CBC 2306.3, Table 2306.3(1) footnote g):
- Where shear design values exceed **350 plf**, all framing members receiving edge fastening from abutting panels must be not less than a single 3-inch nominal member or two 2-inch nominal members fastened together
- Wood structural panel joint and sill plate nailing must be **staggered** at all panel edges
- Sill plate size and anchorage per AWC SDPWS requirements

### Load Combinations

Structures must be designed for the most critical load combination per ASCE 7 Section 2.3 (strength design) or Section 2.4 (ASD), or the CBC alternative ASD combinations of Section 1605.2. (CBC 1605.1)

**Strength design (LRFD) — ASCE 7 Section 2.3 key seismic combinations:**
- 1.2D + 1.0E + L + 0.2S
- 0.9D + 1.0E

Where E includes both horizontal seismic effect (Eh = rho x QE) and vertical seismic effect (Ev = 0.2 SDS x D). The redundancy factor rho = 1.0 or 1.3 per ASCE 7 12.3.4.

**Allowable stress design (ASD) — ASCE 7 Section 2.4 key seismic combinations:**
- D + 0.7E
- D + 0.75L + 0.75(0.7E)
- 0.6D + 0.7E

**Alternative ASD combinations (CBC 1605.2):**
Equations 16-1 through 16-6 (referenced by number in code; equation text not reproduced in scraped source due to formatting). These permit increased allowable stresses where allowed by the material chapter. When using these alternatives, the vertical seismic effect Ev in Equation 12.4-4 of ASCE 7 is permitted to be taken as zero. (CBC 1605.2)

**Overstrength combinations (ASCE 7 Section 2.4.5)** are required where specified by ASCE 7 Chapters 12, 13, and 15 — typically for collectors, diaphragm-to-shear-wall connections, and elements not part of the seismic force-resisting system but carrying seismic forces. (CBC 1605.2)

### Continuous Load Path — Roof to Foundation

Every structure must provide a **complete load path** capable of transferring loads from their point of origin to the load-resisting elements. (CBC 1604.4)

**Load path for lateral forces in a wood-frame multi-unit:**

1. **Roof diaphragm** collects lateral inertia forces and distributes them to shear walls below
2. **Shear walls at each story** resist in-plane shear and transfer forces down to the story below
3. **Diaphragms at each floor level** collect and redistribute forces between upper and lower shear walls
4. **Hold-downs and tie-downs** at shear wall ends resist overturning (tension)
5. **Anchor bolts** at sill plates transfer shear from wood framing into the foundation
6. **Foundation** transfers forces into the ground

**Anchorage requirements** (CBC 1604.8):
- Roof-to-wall, wall-to-floor, wall-to-foundation anchorage must resist **uplift and sliding** from prescribed loads (CBC 1604.8.1)
- Structural walls providing vertical load-bearing or lateral shear resistance must be anchored to the roof and all floors that provide lateral support or are supported by the wall (CBC 1604.8.2)
- Connections must resist horizontal forces from prescribed loads, including earthquake out-of-plane loads per ASCE 7 12.11 for SDC B through F (CBC 1604.8.2)

### Diaphragm Requirements for Multi-Story Wood Frame

Wood structural panel diaphragms must be designed per **AWC SDPWS**. (CBC 2305.1)

**Key design considerations:**

**Diaphragm flexibility classification** — Lateral force distribution depends on whether the diaphragm is flexible, rigid, or semi-rigid. Where a diaphragm cannot be idealized as flexible or rigid per ASCE 7 or AWC SDPWS, the structure must use either: (CBC 1604.4)
1. Envelope analysis using both flexible and rigid assumptions, designing for the worse case, or
2. Semi-rigid diaphragm analysis

**Blocked vs. unblocked** — Blocked diaphragms (all panel edges backed by framing or blocking) achieve significantly higher shear capacities. Multi-story buildings in SDC D typically require blocked diaphragms at all levels. Allowable shear values range from approximately 160 to 450 plf for standard stapled panel diaphragms, and up to 1,795 plf for high-load blocked diaphragms with multiple rows of fasteners. (CBC Tables 2306.2(1) and 2306.2(2))

**Diaphragm deflection** — Must be calculated per AWC SDPWS. For blocked wood structural panel diaphragms with staples, Equation 23-1 provides the deflection calculation considering bending, shear, fastener slip, and chord splice slip. (CBC 2305.2)

**Chord members** — Continuous boundary members (chords) at diaphragm edges resist the flexural couple from diaphragm bending. Chord splices must be designed for the induced forces, and splice slip contributes to diaphragm deflection.

**Collectors (drag struts)** — Transfer diaphragm shear to shear walls that do not extend the full length of the diaphragm. Collectors in SDC C through F must be designed for the overstrength seismic load (omega-0 factor) per ASCE 7 12.10.2.1.

### Shear Wall Deflection

Shear wall deflection must be calculated per AWC SDPWS. For blocked wood structural panel walls with staples, Equation 23-2 accounts for bending, shear, fastener slip, and anchorage elongation. (CBC 2305.3)

**Story drift limits** — ASCE 7 Table 12.12-1 sets allowable story drift. For Risk Category I and II structures, the limit is 0.025 times the story height (hsx). Story drift is calculated as the difference in deflection at the top and bottom of a story, amplified by the deflection amplification factor Cd.

### Shear Wall Allowable Values (Wood Structural Panel, Staples)

For wood structural panel shear walls fastened with staples to Douglas Fir-Larch or Southern Pine framing (CBC Table 2306.3(1)):

| Panel Grade | Thickness | Staple Spacing at Edges | Allowable Shear (plf) |
|-------------|-----------|------------------------|----------------------|
| Structural I | 3/8" | 6" | 155 |
| Structural I | 3/8" | 4" | 235 |
| Structural I | 3/8" | 3" | 315 |
| Structural I | 3/8" | 2" | 400 |
| Structural I | 15/32" | 6" | 185 |
| Structural I | 15/32" | 4" | 280 |
| Structural I | 15/32" | 3" | 375 |
| Structural I | 15/32" | 2" | 475 |
| Sheathing (non-Struct I) | 3/8" | 6" | 140 |
| Sheathing (non-Struct I) | 3/8" | 2" | 360 |
| Sheathing (non-Struct I) | 15/32" | 6" | 170 |
| Sheathing (non-Struct I) | 15/32" | 2" | 430 |

(CBC Table 2306.3(1))

These values are for **seismic loading**. For **wind design**, values may be increased by 40%. (CBC 2306.3)

For normal or permanent load duration, multiply by 0.63 or 0.56, respectively. (CBC Table 2306.3(1) footnote i)

### Seismic Detailing — Wind Does Not Override

Even where wind load effects are greater than seismic load effects, the lateral force-resisting system must still meet seismic detailing requirements and limitations prescribed by ASCE 7 Chapters 11, 12, 13, 15, 17, and 18. (CBC 1604.9)

This means a wood-frame building in SDC D must use properly detailed and engineered shear walls even if wind loads control the design forces.

### Sill Plate Anchorage Requirements in SDC D and E

**SDC D** (CBC 2308.7.1.1): Sill plates along braced wall lines must be anchored with minimum 1/2-inch diameter anchor bolts with **steel plate washers** not less than 0.229 inch by 3 inches by 3 inches. Plate washers may have diagonally slotted holes (max 3/16" larger than bolt, max 1-3/4" slot length) if a standard cut washer is placed between the plate washer and nut.

**SDC E** (CBC 2308.7.1.2): Same as SDC D but with minimum **5/8-inch** diameter anchor bolts and the same steel plate washer requirements.

For engineered shear walls (non-prescriptive), AWC SDPWS provides additional anchorage requirements, including specific sill plate sizes and anchor bolt spacing as a function of unit shear.

### Torsion and Irregularities

Where required by ASCE 7, provisions must be made for increased forces from torsion due to eccentricity between the center of application of lateral forces and the center of rigidity of the lateral system. (CBC 1604.4)

ASCE 7 12.3.2 defines horizontal structural irregularities (torsional, re-entrant corner, diaphragm discontinuity, out-of-plane offset, nonparallel systems) and vertical irregularities (soft story, weight, geometric, in-plane discontinuity, weak story). Multi-unit residential buildings with irregular floor plans, offset shear walls between stories, or large corridor openings in diaphragms must be checked for these irregularities, as they trigger additional analysis requirements and prohibitions in SDC D and above.

### 35-Unit Townhome Test Case — Buena Park, CA

- **Location**: Buena Park, Orange County, CA — typical mapped values Ss approximately 1.5g, S1 approximately 0.6g
- **Default Site Class**: D (stiff soil, absent geotechnical investigation)
- **Risk Category**: II (standard residential)
- **Seismic Design Category**: **D** (based on SDS and SD1 with Risk Category II)
- **Construction Type**: Type V-A wood frame, 1-hour rated assemblies
- **Conventional construction (2308)**: **Not permitted** for multi-story in SDC D — limited to 1 story
- **Required design method**: Engineered per CBC 2302.1 Item 1 (ASD) or Item 2 (LRFD)
- **Lateral system**: Wood structural panel shear walls (R = 6.5, Cd = 4, Omega-0 = 3)
- **Height limit**: 65 ft per ASCE 7 Table 12.2-1 for this system in SDC D — adequate for 3-story townhomes
- **Plan review must verify**:
  - Geotechnical report with site class determination (or default Site Class D assumed)
  - Seismic design parameters (Ss, S1, SDS, SD1, SDC) shown on structural drawings
  - Complete load path from roof diaphragm through all shear walls to foundation
  - Shear wall schedule with panel grade, thickness, nailing/stapling pattern, hold-downs, and anchor bolts
  - Diaphragm schedule with nailing/stapling pattern and chord/collector design
  - Story drift calculations within ASCE 7 limits (0.025 hsx for Risk Category II)
  - Hold-down schedule with manufacturer, model, and allowable capacity
  - Anchor bolt size, spacing, and plate washer details per SDC D requirements
  - Redundancy factor (rho) determination
  - Irregularity check and any triggered additional requirements

### Reference Standards

| Standard | Title | Relevance |
|----------|-------|-----------|
| **ASCE 7-22** | Minimum Design Loads and Associated Criteria for Buildings and Other Structures | Primary reference for seismic force determination, load combinations, system selection, drift limits, and irregularity checks |
| **AWC SDPWS** | Special Design Provisions for Wind and Seismic | Required standard for design of wood shear walls and diaphragms — provides unit shear capacities, deflection equations, and detailing rules |
| **ANSI/AWC NDS** | National Design Specification for Wood Construction | Governs wood member design, connection design, load duration factors, and species-specific properties |
| **AWC WFCM** | Wood Frame Construction Manual | Permitted for Risk Category I and II buildings within its scope limitations (CBC 2309.1) — generally not used for multi-unit in SDC D due to complexity |

### Cross-References
- See also: `construction-types.md` — Type V-A height, area, and story limits
- See also: `fire-resistance-ratings.md` — 1-hour rated assemblies for Type V-A structural elements
- See also: `occupancy-classification.md` — Risk Category II determination for R-2/R-3 occupancies

### Key Code Sections
- CBC 1604.4 — Structural analysis: complete load path, diaphragm rigidity, torsion
- CBC 1604.5 — Risk category assignment (Table 1604.5)
- CBC 1604.8 — Anchorage requirements: roof-to-wall, wall-to-foundation, uplift and sliding
- CBC 1604.9 — Seismic detailing required even when wind controls
- CBC 1605.1 — Load combinations: strength design (ASCE 7 Section 2.3), ASD (ASCE 7 Section 2.4), alternative ASD (Section 1605.2)
- CBC 1605.2 — Alternative allowable stress design load combinations
- CBC 1613.1 — Earthquake loads scope: design per ASCE 7 Chapters 11, 12, 13, 15, 17, 18
- CBC 1613.2 — Seismic design category determination: Figure 1613.2(1) or ASCE 7 method
- CBC 1613.3 — Simplified design procedure (ASCE 7 alternate method)
- CBC 2302.1 — Wood design methods: ASD (Item 1), LRFD (Item 2), conventional (Item 3)
- CBC 2305.1 — Wood lateral systems: design per AWC SDPWS
- CBC 2305.2 — Diaphragm deflection calculation (Equation 23-1)
- CBC 2305.3 — Shear wall deflection calculation (Equation 23-2)
- CBC 2306.2 — Diaphragm allowable shear values (Tables 2306.2(1) and 2306.2(2))
- CBC 2306.3 — Shear wall allowable shear values (Tables 2306.3(1), 2306.3(2), 2306.3(3))
- CBC 2307.1 — LRFD design per ANSI/AWC NDS and AWC SDPWS
- CBC 2308.2.1 — Conventional construction story limits by SDC (Table 2308.2.1)
- CBC 2308.7.1.1 — Sill plate anchorage in SDC D (plate washers required)
- CBC 2308.7.1.2 — Sill plate anchorage in SDC E (5/8" bolts required)
- CBC 2308.10 — Wall bracing requirements and methods (Table 2308.10.1)
- ASCE 7-22 Ch 11 — Seismic design criteria, SDC determination
- ASCE 7-22 Ch 12 — Seismic design requirements for building structures
- ASCE 7-22 Table 12.2-1 — Design coefficients for seismic force-resisting systems (R, Omega-0, Cd, height limits)
- ASCE 7-22 Table 12.12-1 — Allowable story drift
- AWC SDPWS — Wood shear wall and diaphragm design provisions
