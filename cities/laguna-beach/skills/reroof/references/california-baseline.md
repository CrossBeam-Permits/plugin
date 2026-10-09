# California Baseline — Reroof

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Reroof Permit Review

This skill covers **state-level** California requirements for residential and commercial reroof permits. It routes between the California Residential Code (CRC Chapter 9) for dwellings and the California Building Code (CBC Chapter 15) for commercial/light commercial buildings.

**What this covers:**
- Roof replacement (full tear-off) and roof recover (overlay)
- Fire classification requirements (Class A/B/C)
- Material-slope compatibility for all covering types
- Sheathing inspection and replacement
- Underlayment, flashing, and drainage
- Tile weight and structural adequacy
- Cool roof energy code compliance
- Attic ventilation calculations
- Insulation and radiant barrier requirements
- Smoke and carbon monoxide alarm verification
- Gas vent terminations and roof penetrations
- Construction waste diversion (CALGreen)

**What this does NOT cover:**
- New construction roof framing design (see structural engineer)
- Solar PV installation on roofs (see california-solar-pv skill)
- Roof-mounted equipment (HVAC, antennas)
- Historical/landmark building exemptions

---

### How to Use This Skill

1. Determine whether the project is **residential** (CRC) or **commercial** (CBC)
2. Walk through the Decision Tree Router below
3. For each checklist item, load the referenced file from `/` as needed
4. See `../SKILL.md` for the full reference file catalog

---

### Decision Tree Router

#### STEP 0 — Wildfire / WUI Pre-Check

For Laguna Beach the wildfire overlay is set citywide: use the `wildfire: 'all'` row below, and the `wildfire-wui` skill in this plugin for the Chapter 7A / WUI Code details.

| Overlay status                  | What to do                                                                                                                                                                                                                |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Not loaded (no FHSZ in city)    | Skip WUI / Chapter 7A. Apply only the statewide Class A/B/C floor in check #2 of the standard reroof tree.                                                                                                                |
| Loaded — `wildfire: 'partial'`  | City has some FHSZ parcels but not the whole jurisdiction. Run check #2 with **Class A as a conditional requirement** — surface it as "If parcel is in VHFHSZ, Class A roof covering is mandatory" and point applicants to the CalFire FHSZ viewer (osfm.fire.ca.gov). Do not fail on WUI grounds without parcel confirmation. |
| Loaded — `wildfire: 'all'`      | Entire or substantial majority of the city is FHSZ. Apply **Class A roof covering** unconditionally as the baseline, prefaced with a brief "assumed FHSZ based on city coverage; confirm via osfm.fire.ca.gov" disclaimer. Also surface Chapter 7A vent and edge-detail requirements from the overlay. |

Reroof is the WUI-adjacent permit type with the most concrete delta — Class A vs Class C roof covering. When the overlay is loaded, follow `../../wildfire-wui/SKILL.md` Step 3 for roof assemblies and pull `../../wildfire-wui/references/roof-eaves-vents.md` for the specific Chapter 7A requirements that apply to a reroof scope (covering class, valleys, eave/soffit treatment, ember-resistant vents on the replaced roof plane).

#### STEP 1 — Determine Code Path

| Building Use | Code | Key Chapter |
|---|---|---|
| Single-family dwelling, duplex, townhouse <=3 stories | CRC | Chapter 9 (R902-R908) |
| Commercial, light commercial, multifamily >3 stories | CBC | Chapter 15 (1503-1512) |

Both codes share the same material standards (ASTM) and California amendments. The CRC is generally simpler; the CBC adds structural and wind design requirements.

#### STEP 2 — What Type of Review Is This?

| Review Type | Load These References |
|---|---|
| **Full permit review** (form data in, pass/fail out) | `reroof-overlay-rules.md`, `roof-covering-fire-class.md`, `roof-materials-slope.md`, `cool-roof-energy.md` + others as triggered |
| **Material/slope question only** | `roof-materials-slope.md` |
| **Cool roof / energy question** | `cool-roof-energy.md`, `insulation-energy.md` |
| **Overlay vs tear-off question** | `reroof-overlay-rules.md` |
| **Ventilation calculation question** | `attic-ventilation.md` |
| **Tile weight/structural question** | `tile-structural.md` |

#### STEP 3 — Review Checklist

Walk each item in order. For every check, record PASS / FAIL / FLAG / N/A with the code section cited.

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| 1 | **Scope: Tear-off or Overlay?** | If overlay: existing roof must have <=1 layer already (max 2 total). Cannot overlay over slate, clay, cement, or asbestos-cement tile. Cannot overlay if existing is water-soaked or deteriorated. If tear-off: all layers removed to deck. | CBC 1512.2, 1512.3; CRC R908.3 | `reroof-overlay-rules.md` |
| 2 | **Fire Classification** | All new roofing in California must be fire-retardant rated at minimum Class C (CBC 1505.1.2). If >50% of roof replaced in one year, entire roof must be minimum Class C. In Very High Fire Hazard Severity Zones (VHFHSZ), Class A is mandatory regardless of construction type. Materials must bear testing agency labels (ASTM E108 or UL 790). Minimum per construction type: Type IA/IB/IIA/IV/VA = Class B; Type IIB/IIIB/VB = Class C (Table 1505.1). | CBC 1505.1, 1505.1.2, Table 1505.1; CRC R902.1, R902.1.2 | `roof-covering-fire-class.md` |
| 3 | **Wind Speed Zone** | Determine wind speed zone for project location (typically 110-115 mph for most of California per ASCE 7-22/CBC 1609). Wind speed zone affects underlayment requirements and wind-resistance labeling. Verify roofing material wind resistance labeling per ASTM D7158 or ASTM D3161 (CRC R905.2.4/CBC 1504.2). | CBC 1609, 1504.2; CRC R905.2.4 | `roof-materials-slope.md` |
| 4 | **Material-Slope Compatibility** | Verify selected material is allowed at the stated roof slope. Each material has a minimum slope. Low slopes require additional underlayment. | CBC 1507.2-1507.13; CRC R905.2-R905.8 | `roof-materials-slope.md` |
| 5 | **Tile Weight / Structural** | If clay or concrete tile: verify weight (psf) is provided. If weight exceeds original roofing by >3 psf or original framing was not designed for tile, structural analysis may be required. Permit valid for materials <=6 lbs/SF on standard plans. | CBC 1607.13; CRC R301.1 | `tile-structural.md` |
| 6 | **ICC-ESR Product Approval** | If tile: ICC-ES evaluation report number should be provided. This verifies the product meets code. Note the number -- validation is city staff's responsibility. | CBC 1507.3; CRC R905.3 | `tile-structural.md` |
| 7 | **Sheathing** | On tear-off: all missing, rotten, termite-eaten, or damaged sheathing must be replaced. Min thickness 1/2". Nailing: 6" OC at perimeter, 12" OC in field. Gaps in spaced sheathing <=1/4" or per manufacturer. Shingles shall be fastened only to solidly sheathed decks. | CRC R803.1, R803.2, R905.2.1 | `sheathing-requirements.md` |
| 8 | **Underlayment** | Required under all roof coverings. Type depends on wind zone and material. Low-slope (2:12-4:12) requires double underlayment for shingles. Fastening: 12" grid between side laps, 6" at side/end laps. Drip edge: over underlayment at eaves, under underlayment at rakes. | CBC 1507.1.1; CRC R905.1.1, Table R905.1.1(2), Table R905.1.1(3) | `roof-materials-slope.md` |
| 9 | **Flashing** | Required at wall/roof intersections, slope changes, penetrations. Metal >=0.019" (26 gage galvanized). Step flashing: min 4" legs, 2" offset from shingle edge. Sub-flashing required behind step flashing at dormers. Counter-flashing at chimney/masonry. Soffit flashing at chimney cricket. Kickout flashing at eave/sidewall intersections. Crickets for penetrations >30" wide. Valley lining installed BEFORE roofing material. Drip edge fastener spacing 12" OC. Prime metal flashing before applying bituminous materials. Rusted/damaged flashings must be replaced. | CBC 1503.2, 1503.5, 1512.5; CRC R903.2, R905.2.8, R905.2.8.3 | `roof-materials-slope.md` |
| 10 | **Roof Drainage** | Drains at low points unless designed to drain over edges. Overflow drains or scuppers required where parapets trap water (inlet 2" above low point). Scuppers: 3x drain size, min 4" opening height. Drainage must not discharge onto adjacent property. | CRC R903.4, R903.4.1; CBC 1503.4 | `roof-drainage.md` |
| 11 | **Cool Roof Compliance** | Low-slope (<=2:12): SRI >=75. Steep-slope (>2:12): SRI >=16. Commercial low-slope: aged reflectance >=0.63, emittance >=0.75. Residential steep-slope: aged reflectance >=0.20, emittance >=0.75. Heavy roofs >=25 lb/ft2 exempt. BIPV/solar thermal exempt. | Energy Code 150.2(b)1I | `cool-roof-energy.md` |
| 12 | **Attic Ventilation** | Vented attics: cross ventilation required. NFA = area/150 (unbalanced) or area/300 (balanced with 40-50% upper vents + vapor barrier). 1" min clearance between insulation and sheathing at vents. Vaulted ceilings: each bay ventilated individually. | CRC R806.1, R806.2, R806.3 | `attic-ventilation.md` |
| 13 | **Insulation & Radiant Barrier** | Reroof may trigger insulation upgrade to min R-22 (residential). Radiant barrier required in CZ 2-15 when vented attic with 1" air gap. Commercial low-slope: R-14 continuous insulation in CZ 1-2, 4, 8-16. | Energy Code 150.0(A), 150.1(C)1-2 | `insulation-energy.md`, `sheathing-requirements.md` |
| 14 | **Smoke & CO Alarms** | Verified at final inspection. Working alarms required in each bedroom, outside sleeping areas, each story. CO alarms required where fuel-fired appliances or attached garage. Detectors >10 years old must be replaced. For reroof-only: hardwired/interconnected upgrade NOT required (exterior work exception). | CRC R310, R311 | `smoke-co-alarms.md` |
| 15 | **Gas Vent Terminations** | Gas vents must extend through roof flashing/jack and terminate with a listed cap. Type B/L: min 5 ft above draft hood. Height above roof follows the applicable termination conditions. Min 3 ft above a forced-air inlet within 10 ft. Single-wall clearance uses the applicable CMC Table 802.7.3.3 or CPC Table 509.7.3.4(1) row; Type B follows its listing/manufacturer. Pipe boots are coordinated with the reroof scope. | CMC 802.6.1, 802.6.2, Table 802.7.3.3; CPC 509.6.1, Table 509.7.3.4(1) | `gas-vent-terminations.md` |
| 16 | **Waste Diversion** | Tear-off projects: 65% minimum nonhazardous waste diversion from landfill (CALGreen 5.408). Waste management plan required. | CALGreen 5.408 | `waste-diversion.md` |
| 17 | **Contractor Licensing** | C-39 (Roofing) or B (General Building) license required. C-43 (Sheet Metal) for metal roofing. Workers' compensation insurance required. | B&P Code 7028 | N/A |

#### STEP 4 — Output Format

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
- **N/A** -- Does not apply to this project (e.g., tile checks when material is asphalt)

---

### Quick-Reference Tables

#### Minimum Slope by Material

| Material | Min Slope | Code Section | Notes |
|---|---|---|---|
| Asphalt shingles | 2:12 | CRC R905.2.2 | Double underlayment 2:12-4:12 |
| Clay/concrete tile | 2.5:12 | CRC R905.3 | Double underlayment 2.5:12-4:12 |
| Metal panels (standing seam) | 0.25:12 | CRC R905.10.2 | Lowest slope allowed |
| Metal panels (lapped w/ sealant) | 0.5:12 | CRC R905.10.2 | -- |
| Metal panels (lapped no sealant) | 3:12 | CRC R905.10.2 | -- |
| Metal shingles | Per mfr | CRC R905.4 | Per manufacturer specs |
| Wood shingles | 3:12 | CRC R905.7 | -- |
| Wood shakes | 3:12 | CRC R905.8 | Interlayment required |
| Slate | 4:12 | CRC R905.6 | Head lap varies by slope |
| Roll roofing (mineral-surfaced) | 1:12 | CRC R905.5 | -- |
| Modified bitumen | 0.25:12 | CBC 1507.11 | -- |
| Built-up (asphalt) | 0.25:12 | CBC 1507.10 | Coal-tar: 0.125:12 |
| Single-ply (EPDM, TPO, PVC) | 0.25:12 | CBC 1507.12 | -- |
| Sprayed polyurethane foam | 0.25:12 | CBC 1507.13 | Protective coating 2-72 hrs |
| Liquid applied | 0.25:12 | CBC 1507.15 | -- |
| PV shingles / BIPV panels | 2:12 | CRC R905.15 | Must be Class A, UL 7103 |

#### Cool Roof Thresholds (California Energy Code)

| Roof Type | Climate Zones | Min Aged Solar Reflectance | Min Thermal Emittance | OR Min SRI |
|---|---|---|---|---|
| Residential steep-slope (>2:12) | CZ 4, 8-15 | 0.20 | 0.75 | 16 |
| Commercial low-slope (<=2:12) | CZ 4, 6-15 | 0.63 | 0.75 | 75 |

#### Attic Ventilation Quick-Reference

| Calculation Type | Ratio | When to Use |
|---|---|---|
| **Unbalanced** | Area / 150 | Default -- when balanced conditions are NOT met |
| **Balanced** | Area / 300 | When 40-50% of vents are upper (within 3 ft of ridge), balance at eaves, AND vapor barrier installed |

To convert SF of NFA to square inches: **NFA (SF) x 144 = NFA (sq in)**

#### Overlay Rules Summary

| Condition | Allowed? |
|---|---|
| 1 existing layer, good condition | Overlay permitted |
| 2 existing layers | Must tear off -- overlay prohibited |
| Existing slate/clay/cement/asbestos tile | Must tear off -- overlay prohibited |
| Water-soaked or deteriorated deck | Must tear off -- overlay prohibited |

#### Fastener Requirements by Material

| Material | Min Fasteners | Fastener Spec | Code Section |
|---|---|---|---|
| Asphalt shingles (strip) | 4 per strip shingle | 12-gage, 3/8" head, 3/4" penetration | CRC R905.2.5, R905.2.6 |
| Asphalt shingles (individual) | 2 per shingle | Same as above | CRC R905.2.6 |
| Clay/concrete tile (perimeter) | 1-2 per tile | 11-gage, 5/16" head, 3/4" penetration | CRC R905.3.6, R905.3.7 |
| Clay/concrete tile (field, battens, <5:12) | Not required | -- | CRC R905.3.7 |
| Lightweight tile (<9 lb/SF) | 1 per tile (all slopes) | Same as tile spec | CRC R905.3.7 |
| Metal panels | Per manufacturer | Galvanically compatible | CRC R905.10 |

#### Gas Vent Height Above Roof (CMC Table 802.6.1)

For vents 12" or less in diameter, 8+ ft from a vertical wall:

| Roof Slope | Min Height (ft) |
|---|---|
| Flat to 6:12 | 1.0 |
| Over 6:12 to 7:12 | 1.25 |
| Over 7:12 to 8:12 | 1.5 |
| Over 8:12 to 9:12 | 2.0 |
| Over 9:12 to 10:12 | 2.5 |
| Over 10:12 to 11:12 | 3.25 |
| Over 11:12 to 12:12 | 4.0 |

For vents >12" diameter or <8 ft from a wall: min **2 ft** above highest point within 10 ft horizontal.

---

### Key Principles

1. **California = fire-rated territory.** All new roof coverings must be fire-retardant rated at minimum Class C (CBC 1505.1.2/CRC R902.1.2). If more than 50% of the roof is replaced in one year, the entire roof must be minimum Class C. In Very High Fire Hazard Severity Zones (VHFHSZ), Class A is mandatory regardless of construction type.
2. **Two-layer maximum.** You cannot overlay a third layer. If two layers already exist, full tear-off is required (CBC 1512.3, CRC R908.3).
3. **Slope dictates material.** Every roofing material has a minimum slope requirement. Asphalt shingles below 2:12 is a code violation. Tile below 2.5:12 is a code violation.
4. **Tile means structural check.** Concrete and clay tile weigh 8-15 psf -- significantly more than composition shingles (~2 psf). Switching to tile from a lighter material may require structural analysis.
5. **Cool roof is California-specific.** The Energy Code requires minimum solar reflectance values that vary by climate zone and roof slope. This applies on reroof, not just new construction. Low-slope: SRI >=75. Steep-slope: SRI >=16.
6. **Ventilation must be calculated.** Every reroof with attic space must show ventilation NFA -- either 1/150 (unbalanced) or 1/300 (balanced). Cross ventilation is mandatory.
7. **Sheathing is a critical inspection point.** On tear-off, damaged sheathing must be replaced. Min 1/2" thickness. Spaced sheathing may need conversion to solid if changing from shakes to shingles.
8. **Smoke and CO alarms verified at final.** Working alarms must be present in all required locations. For reroof-only projects, hardwired interconnection is not required (exterior work exception).
