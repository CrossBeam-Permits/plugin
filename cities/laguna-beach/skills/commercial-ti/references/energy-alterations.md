---
title: "Energy Alterations — Title 24 Part 6 §141.0"
category: "Energy — Title 24 Part 6 (California Energy Code)"
relevance: "Loaded when any envelope, lighting, HVAC, service-water-heating, sign, or electrical-power-distribution work is in scope."
key_code_sections: "Title 24 Part 6 §141.0(b), §141.1"
---

# Energy Alterations — Commercial TI

Title 24 Part 6 §141.0 is the comprehensive nonresidential-alterations rule. It is the single most-frequently-missed section in commercial TI reviews — applicants often submit minimal energy compliance documentation, but §141.0 has nearly two dozen sub-triggers that drive specific requirements.

This reference enumerates each trigger. Reviewers verify each one against drawings/specs.

The overall framework (§141.0(a)/(b)/(c)/(d)):
- **(a)** Additions — meet Sections 110.0-120.7, 120.9-130.5, and 140.2-140.9 by either prescriptive or performance approach.
- **(b)** Alterations — meet §141.0(b)1 mandatory, then either §141.0(b)2 prescriptive OR §141.0(b)3 performance.
- **(c)** Repairs — must not increase pre-existing energy consumption.
- **(d)** Alternate — meet Title 24 Part 6 for the entire building.

Most commercial TI work falls under (b).

**Healthcare exception (§141.0 NOTE):** Alterations to healthcare facilities are exempt from §141.0. (Healthcare TI = HCAI / OSHPD jurisdiction, out of scope for this skill.)

---

## 1. Mandatory Requirements for Altered Components (§141.0(b)1)

These apply to ALL alteration projects — both prescriptive and performance paths — when the listed component is altered.

### Roof / Ceiling Insulation (§141.0(b)1A)

When the opaque portion of a roof/ceiling separating conditioned from unconditioned spaces or ambient air is altered → must meet §141.0(b)2Bii insulation requirements.

### Wall Insulation (§141.0(b)1B)

When opaque wall area separating conditioned from unconditioned is altered:

| Wall Type | Insulation OR U-factor (area-weighted avg) |
|---|---|
| Metal building | R-13 between framing OR U-0.113 |
| Metal framed | R-13 between framing OR U-0.217 |
| Wood framed and others | R-11 between framing OR U-0.110 |
| Spandrel panels / glass curtain walls | R-4 OR U-0.280 |

Exception: light and heavy mass walls.

### Floor Insulation (§141.0(b)1C)

For altered raised floors separating conditioned/unconditioned:

| Floor Type | Insulation OR U-factor |
|---|---|
| Raised framed floors | R-11 between framing OR U-0.071 |
| Raised mass floors in hotel/motel guest rooms | R-6 OR U-0.111 |
| Raised mass floors in other occupancies | No minimum |

### Fan Energy Index (§141.0(b)1D)

New fan systems serving an existing building meet §120.10.

### Exterior Windows (§141.0(b)1E)

| Threshold | Requirement |
|---|---|
| **Replaced vertical fenestration > 150 sf** of building's total | Max U-factor 0.58 |
| **Added vertical fenestration > 50 sf** | Per §120.7(d) (high-performance fenestration) |
| Added vertical fenestration <= 50 sf | No requirement |

---

## 2. Prescriptive Approach — Altered Components (§141.0(b)2)

### Fenestration Detailed (§141.0(b)2A)

For replaced vertical fenestration > 150 sf — must meet Table 141.0-A (U-factor and RSHGC by climate zone):

| Climate Zone | U-Factor | RSHGC |
|---|---|---|
| 1, 4, 6 | 0.47 / 0.47 / 0.47 | 0.41 / 0.31 / 0.31 |
| 2 | 0.47 | 0.31 |
| 3, 5 | 0.58 | 0.41 |
| 7-15 | 0.47 | 0.31 |
| 16 | 0.47 | 0.41 |

Added vertical fenestration > 50 sf → per Tables 140.3-B/C/D.

### Cool Roof / Roof Insulation (§141.0(b)2B)

For roof replacement, recovery, or recoating:

- **Always** comply with §110.8(i).
- When roof altered > 50% of roof area OR > 2,000 sf (whichever is less):
  - Roofing products meet §140.3(a)1A (aged solar reflectance + thermal emittance / SRI).
  - Insulation per Table 141.0-C: CZ 1-5, 9-16 → R-23 OR U-0.037 (with R-10 above deck); CZ 6-8 → R-17 OR U-0.047 (with R-10 above deck).

Exceptions:
- Roof recovers with new R-10 above deck — full Table 141.0-C insulation not required.
- Existing rooftop equipment that won't be disconnected & lifted — added insulation is greater of R-10 OR maximum thickness that keeps base flashing per manufacturer.
- Tapered insulation at drains may use lesser R-values if average meets table.
- Recoat — no insulation requirement.
- BIPV / building-integrated solar thermal panel area — exempt.
- Roof construction >= 25 lb/sf — exempt from reflectance/emittance/SRI.

### Space Conditioning (§141.0(b)2C)

New or replacement space-conditioning systems / components (other than ducts) must meet §140.4. Plus:

**Additional fan power allowance** (Table 141.0-D — add to §140.4-A/B values):

| System Type | <=5,000 CFM | 5,001-10,000 CFM | > 10,000 CFM |
|---|---|---|---|
| Multi-zone VAV — supply | 0.135 | 0.114 | 0.105 |
| Multi-zone VAV — supply w/ adapter curb | 0.033 | 0.033 | 0.043 |
| Other — supply | 0.139 | 0.120 | 0.107 |
| Multi-zone VAV — exhaust/return | 0.070 | 0.061 | 0.054 |
| Multi-zone VAV — exhaust/return w/ adapter curb | 0.016 | 0.017 | 0.022 |
| Other — exhaust/return | 0.070 | 0.062 | 0.055 |

**Packaged single-zone DX < 65,000 Btu/h (Table 141.0-E-1)** — varies by climate zone and building type (retail/grocery, school, office/financial, library); typically requires SZHP (single-zone heat pump + economizer) or SZAC1 (variable-speed fan + economizer / dual-fuel HP).

Exception: §141.0(b)2Cii doesn't apply if alteration exceeds existing main service panel/transformer capacity (requires PE-stamped electrical load calc per CEC Article 220).

Exception 2 to (b)2C: doesn't apply to replacement of equivalent / lower-capacity electric resistance space heaters when natural gas not available.

### Altered Duct Systems (§141.0(b)2D)

New or replacement ducts meet §120.4(a)-(f) and ONE of:

- **§141.0(b)2D.i** — Entirely new / complete-replacement duct systems leakage-tested per §120.4(g). Applies when reused parts <= 25% of new system.
- **§141.0(b)2D.ii** — Extension to existing system: combined leakage <= 15% of nominal air-handler airflow, verified per Reference Nonresidential Appendix NA7.5.3. Applies when:
  1. Not a healthcare facility,
  2. Constant-volume single-zone,
  3. Serves < 5,000 sf conditioned floor area,
  4. Outdoor / unconditioned duct surface > 25% of total duct surface.
- **§141.0(b)2D.iii** — Otherwise: meet CMC §603.9.2 duct leakage testing.

Exception 2: Existing asbestos-insulated/sealed ducts exempt.

### Altered Space-Conditioning Systems (§141.0(b)2E)

When SC system altered by installation/replacement of equipment (air handler, outdoor condensing unit, cooling/heating coil):

- **§141.0(b)2E.i** — Existing thermostat must comply with §110.12 demand-responsive requirements; if not, replace with compliant DR thermostat. All NEW units must have DR thermostat.
- **§141.0(b)2E.ii** — Connected duct system sealed per §141.0(b)2D.ii.

### Lighting Systems Installed for First Time (§141.0(b)2F)

Spaces with lighting installed for first time meet §110.9, §130.0, §130.1, §130.2, §130.4, §140.3(c), §140.6, §140.7.

### Daylighting Skylight Trigger Exception (§141.0(b)2G)

If §130.1(d) is triggered by adding skylights to existing building and lighting not recircuited, daylighting control need not meet multilevel requirements.

### Internally / Externally Illuminated Signs (§141.0(b)2H, §141.0(b)2M)

- New signs: per §110.9, §130.3, §140.8.
- Altered signs that increase connected lighting load, replace > 50% of ballasts, OR relocate: per §140.8.
- Exception: replacement of lamps, sign face, or ballasts (no rewiring; not at relocation) is not an alteration.

### Indoor Lighting Alterations — THE BIG TRIGGER (§141.0(b)2I)

If alteration touches **>= 10% of luminaires** serving an enclosed space, MUST meet ONE of three paths:

- **Path i** — Comply with §140.6 lighting power requirements + Table 141.0-F lighting controls (full set).
- **Path ii** — 80% of §140.6 lighting power + Table 141.0-F lighting controls (full set minus multi-level, minus daylighting, minus DR).
- **Path iii** — One-for-one luminaire alteration in a building/tenant space <= 5,000 sf, total wattage of altered luminaires >= 40% lower than pre-alteration, + Table 141.0-F lighting controls (full set minus multi-level, minus daylighting, minus DR).

Alterations cannot prevent operation of existing unaltered controls or remove §130.1 functions.

**Exceptions:**
1. Portable / movable-partition luminaires; lighting excluded per §140.6(a)3.
2. Any enclosed space with only one luminaire.
3. Alteration that would disturb asbestos (unless paired with asbestos abatement).
4. Acceptance testing per §130.4 not required when controls added to <= 20 luminaires.
5. Alteration limited to adding controls OR replacing lamps/ballasts/drivers only.
6. One-for-one luminaire alteration of up to 50 luminaires per complete floor / complete tenant space per annum.

Table 141.0-F summary (the controls actually required):

| Control | Path (i) | Path (ii) or (iii) |
|---|---|---|
| Manual area controls §130.1(a)1 | Required | Required |
| Manual area controls §130.1(a)2 | Required | Required |
| Control separation §130.1(a)3 | Only for new/completely-replaced circuits | Only for new/completely-replaced circuits |
| Multi-level §130.1(b) | Required | NOT required |
| Auto shut-off §130.1(c)1-6, 8 | All Required | All Required (except 130.1(c)6D in path ii/iii) |
| Daylighting §130.1(d) | Required | NOT required |
| DR controls §110.12(a), (c) | Required | NOT required |

### Outdoor Lighting Alterations (§141.0(b)2L)

For lighting applications in Tables 140.7-A or 140.7-B:

- Alterations that increase connected lighting load: added/altered luminaires meet §130.2(c) and §140.7.
- Alterations not increasing load, with >= 10% existing luminaires replaced in general hardscape or specific application:
  - Parking lots / sales lots with luminaire <= 24 ft above ground: §130.2(c)1 AND §130.2(c)3.
  - Else: §130.2(c)1 + EITHER §130.2(c)2 OR motion sensors reducing power >= 40%.
- Alterations not increasing load, with >= 50% existing luminaires replaced: above + §140.7 power allowances.
- Exception: fewer than 5 luminaires replaced — no requirements.

Acceptance testing not required for <= 20 luminaires.

### Service Water Heating (§141.0(b)2N)

Service water-heating systems meet §140.5(a)2 and (b), excluding solar water heating requirements.

### Building Shell First-Time Interior Walls/Ceilings (§141.0(b)2O)

When interior walls/ceilings installed for the first time, meet §140.3(c).

### Electrical Power Distribution (§141.0(b)2P)

| Trigger | Requirement |
|---|---|
| New / replacement service equipment | §130.5(a) electrical metering |
| Entirely new / complete-replacement electrical power distribution | §130.5(b) circuit separation for energy monitoring |
| Altered feeders + branch circuits (both modified) | §130.5(c) voltage drop |
| Entirely new / complete-replacement | §130.5(d) and (e) circuit controls + controlled receptacles |

Exception to (b)2Piii: voltage drop permitted by CEC §647.4, §695.6, §695.7.

### Wall Air Leakage (§141.0(b)2Q)

When >= 25% of an existing envelope wall area is altered, comply with §140.3(a)9. If tested per NA5.1 and leakage > 0.4 CFM/sf at 75 Pa, visual inspection + diagnostic per NA5.7, seal all observed leaks where possible without destruction.

Exception: healthcare facilities.

### Exterior Doors (§141.0(b)2R)

Alterations adding exterior door area meet U-factor requirements of §140.3(a)7.

---

## 3. Performance Approach (§141.0(b)3)

Allows tradeoffs across components. The altered envelope + SC + lighting + water-heating + new equipment meet §110.0-110.9, §120.0-120.6, §120.9-130.5.

Standard design for an altered component is the *higher* efficiency of (existing conditions) or (§141.0(b)2 requirements).

Window-film exception (§141.0(b)3A Exception 1): Applied window films comply with U-factor, RSHGC, VT per Table 141.0-E-2.

Use case: where prescriptive §141.0(b)2 would force expensive equipment swaps, performance approach can trade reduced lighting power against under-performing envelope.

---

## 4. Repairs (§141.0(c))

> Repairs shall not increase the pre-existing energy consumption of the repaired component, system or equipment.

Repairs are NOT alterations. Glass replaced in an existing sash, sash replaced in existing frame — repairs per definition in §141.0(b)2A Note.

---

## 5. Covered Processes (§141.1)

For TIs that include processes / lab equipment:

| Trigger | Reference |
|---|---|
| Lab/process facility exhaust additions or alterations | §141.1(a) → §140.9(c) |
| Computer rooms — newly installed cooling + UPS | §141.1(b) → §120.6(j), §140.9(a)2, §140.9(a)4 + economizer requirements |
| Controlled-environment horticulture (indoor growing / greenhouse / horticultural lighting) | §141.1(c) → §120.6(h) |
| Process piping (heating / cooling) | §141.1(d) → §120.3 |

---

## Plan Check Review Checklist — Energy

Default applicability: `ALL`

| ID | Tag | Item | Pass Criteria | Code Section | Likely sheets |
|---|---|---|---|---|---|
| EN-1 | ALL | Compliance path declared | Prescriptive (§141.0(b)2) OR performance (§141.0(b)3) on cover sheet. FAIL if an energy scope declares no path. | §141.0(b) | Energy forms |
| EN-2 | ALL | Title 24 Forms submitted | Required Cx forms (NRCC-LTI for lighting alterations, NRCC-MCH for mechanical, etc.). FAIL if missing for a lighting/HVAC/envelope scope. | §10-103 | Energy forms |
| EN-3 | NEW-WORK | Altered envelope walls insulated | Per §141.0(b)1B table. FLAG if wall scope is unclear. | §141.0(b)1B | Architectural/energy |
| EN-4 | NEW-WORK | Altered roof — cool-roof / insulation | Per §141.0(b)2B if > 50% of roof OR > 2,000 sf. FLAG if roof work is unclear. | §141.0(b)2B | Roof, energy |
| EN-5 | NEW-WORK | Replaced fenestration > 150 sf | Max U-factor 0.58; Table 141.0-A if prescriptive. FLAG if quantity is unclear. | §141.0(b)1E, §141.0(b)2A | Window schedule |
| EN-6 | NEW-WORK | Added fenestration > 50 sf | §120.7(d) high-performance. | §141.0(b)1E | Window schedule |
| EN-7 | ALL | HVAC altered | §140.4 applicable subsections; Table 141.0-E-1 packaged-unit type. FLAG if HVAC scope is unclear. | §141.0(b)2C | Mechanical/energy |
| EN-8 | ALL | Demand-responsive thermostat | All altered + new SC units. FLAG if the equipment schedule is incomplete. | §141.0(b)2E.i, §110.12 | Mechanical/energy |
| EN-9 | ALL | Duct system leakage tested | Per (b)2D.i / (b)2D.ii / (b)2D.iii as applicable. FLAG if duct scope is unclear. | §141.0(b)2D | Mechanical |
| EN-10 | ALL | Indoor lighting alteration check | If >= 10% luminaires altered: one of three paths (§141.0(b)2I); Table 141.0-F controls. FAIL if a lighting alteration lacks forms. | §141.0(b)2I | Lighting/energy |
| EN-11 | ALL | Acceptance test (lighting) | NA7.6 acceptance test certificate filed by certified ATT. FLAG if omitted where required. | §130.4 | Energy forms |
| EN-12 | SITE | Outdoor lighting alterations | §141.0(b)2L compliance if applicable; N/A otherwise. | §141.0(b)2L | Site/electrical |
| EN-13 | NEW-WORK | Wall air leakage | If >= 25% wall altered: §140.3(a)9 + NA5.1 testing if applicable. FLAG if wall area is unknown. | §141.0(b)2Q | Architectural |
| EN-14 | ALL | Electrical power distribution | If service equipment / feeders + branches altered: §130.5(a)-(e). | §141.0(b)2P | Electrical/energy |
| EN-15 | ALL | Service water heating | If altered: §140.5(a)2 and (b); N/A otherwise. | §141.0(b)2N | Plumbing/energy |
| EN-16 | SITE | Sign alterations | If load increase OR > 50% ballasts replaced OR relocation: §140.8; N/A otherwise. | §141.0(b)2M | Sign/electrical |
| EN-17 | SITE | Sign / illuminated sign permits | Stamped Cx forms provided where a sign scope exists. | §141.0(b)2H | Sign/energy |
| EN-18 | ALL | Climate zone identified | Project address mapped to CEC Climate Zone (1-16). FLAG if absent — the energy tables depend on it. | §100.1 | Energy forms/site facts |
| EN-19 | ALL | Process loads identified | If lab / computer room / horticulture / process piping → §141.1; confirm absent otherwise. | §141.1 | Mechanical/electrical |
