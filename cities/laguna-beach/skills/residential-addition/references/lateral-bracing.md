---
title: "Lateral Bracing Requirements"
category: "Structural"
relevance: "Every addition with walls — shear walls, hold-downs, and braced wall panel requirements"
key_code_sections: "CRC R602.10, R602.10.3, R602.10.6, R602.10.8, Table R602.10.3(1)"
---

# Lateral Bracing Requirements

Source: 2025 California Residential Code (Title 24, Part 2.5), Chapter 6, Section R602.10.

---

## Overview

Lateral bracing resists horizontal forces (wind and seismic) and transfers them to the foundation. In California, seismic design governs in most locations. Every addition must have adequate bracing on all braced wall lines.

---

## Braced Wall Lines (CRC R602.10.1)

### Definition
Braced wall lines are straight lines through the building plan that designate the location of lateral force resistance. They must be:
- Located at or near each end of the building in each direction
- Spaced max 35 ft apart (measured perpendicular to the braced wall line)
- Offset max 4 ft from the edge of the building

### For Additions
- New braced wall lines must align with or tie into existing braced wall lines where practical
- Where the addition creates a new exterior wall line, it becomes a braced wall line
- Interior braced wall lines may be required if the building width (perpendicular to any exterior braced wall line) exceeds 35 ft

---

## Braced Wall Panel Methods (CRC R602.10.4)

The CRC provides multiple methods for bracing. The most common for residential additions:

| Method | Code | Description | Min Panel Length |
|---|---|---|---|
| **WSP** | R602.10.4.1 | Wood structural panels (plywood/OSB) — min 3/8" thick, nailed 6" OC edges / 12" OC field | 48" |
| **LIB** | R602.10.4.2 | Let-in bracing — 1x4 diagonal at 45-60 degrees | Full story height |
| **DWB** | R602.10.4.3 | Gypsum board (1/2") — screws 4" OC edges / 7" OC field | 96" |
| **SFB** | R602.10.4.4 | Structural fiberboard sheathing — min 1/2" thick | 48" |
| **PBS** | R602.10.4.5 | Portal frame at garage openings — min 24" wide WSP each side | 24" |
| **PFH** | R602.10.4.6 | Portal frame with hold-downs — engineered connection | 16" |
| **CS-WSP** | R602.10.4.7 | Continuous wood structural panel sheathing — entire exterior wall | 48" |
| **CS-G** | R602.10.4.8 | Continuous gypsum board sheathing | 48" |
| **CS-SFB** | R602.10.4.9 | Continuous structural fiberboard sheathing | 48" |

### Wood Structural Panel (WSP) — Most Common Method

**Panel Requirements:**
- Min 3/8" wood structural panel (plywood or OSB)
- Min 48" wide (or 2 adjoining panels min 24" wide each)
- Full height of wall (sole plate to top plate)

**Nailing Schedule:**
- Panel edges: 6" OC with 8d common (2-1/2" x 0.131") nails
- Intermediate supports: 12" OC
- Alternative: 6d common (2" x 0.113") at 4" OC edges for increased capacity

**Continuous Sheathing (CS-WSP):**
- When WSP covers all exterior wall surfaces (not just panels), minimum bracing amounts are reduced
- Corners: WSP must wrap min 24" around corners on each side
- Window/door openings: narrower panels allowed when sheathing is continuous

---

## Minimum Bracing Amounts (CRC R602.10.3, Table R602.10.3(1))

When the plans omit SDC or ultimate design wind speed, read the parcel-resolved
values from the parcel facts `design_parameters` and COMPUTE the required
length from Tables R602.10.3(1)/(2)/(3). State the source and Site Class
assumption (default D unless a geotechnical report is in the set). Only FLAG the
missing jurisdiction input when the relevant design parameter is absent/null; a
plan-stated or geotech-derived value controls over the default.

The required total length of braced wall panels on each braced wall line depends on:
1. **Seismic Design Category** (most of CA is SDC D)
2. **Number of stories**
3. **Bracing method**
4. **Wall height**
5. **Building dimensions**

### Typical Minimum Bracing for SDC D (Table R602.10.3(1))

For a one-story building, 8 ft wall height, using WSP method:

| Braced Wall Line Spacing | SDC D0 | SDC D1 | SDC D2 |
|---|---|---|---|
| 10 ft | 4'-0" | 5'-4" | 6'-4" |
| 20 ft | 5'-4" | 8'-0" | 10'-8" |
| 30 ft | 6'-8" | 10'-0" | 13'-4" |
| 35 ft | 7'-0" | 10'-0" | 14'-0" |

For two-story buildings: first floor bracing amounts increase significantly (multiply by approximately 1.5-2x).

### Adjustment Factors
- **Wall height >10 ft:** multiply bracing length by wall height / 10
- **Gypsum board only (DWB):** multiply by 2.0 (less effective than WSP)
- **Continuous sheathing (CS-WSP):** multiply by 0.65 (more effective)

---

## Hold-Down Connectors (CRC R602.10.6)

### When Required
Hold-down connectors (also called tie-downs) are required:
- At ends of braced wall panels in SDC D0, D1, and D2
- At portal frame braced wall panels (PBS and PFH methods)
- Where overturning forces exceed the dead-load resistance of the panel

### Installation
- Connect panel end stud to foundation or to framing below
- Manufacturer's specifications for anchor bolt size, edge distance, and embedment
- Common types: Simpson HTT, HDU, HD series
- Allowable loads per manufacturer's evaluation report (ICC-ES ESR)

### Foundation Connection
- Hold-down bolts: typically 5/8" or 3/4" anchor bolt, min 7" embedment
- Edge distance: per manufacturer (typically 1-3/4" to 3-1/2" from concrete edge)
- Hold-down strap: alternative for connecting upper floor panels to lower floor panels

---

## Braced Wall Panel Location Rules (CRC R602.10.3.2)

### Placement
- Each end of each braced wall line must have a braced wall panel starting within 10 ft of the end
- Where only one braced wall panel is required: locate within center 2/3 of the braced wall line length
- Braced wall panels must be distributed along the braced wall line

### Openings
- Openings in braced wall lines reduce the available bracing length
- Large garage openings may require portal frame (PBS/PFH) method
- Windows/doors: headers must transfer lateral loads to adjacent panels

---

## Connection Between Stories (CRC R602.10.8)

### Floor Diaphragm Connections
At each floor level and at the top of the foundation wall:
- A continuous load path must transfer lateral forces from braced wall panels above to braced wall panels below
- Blocking between joists at braced wall lines
- Nailing of blocking to plates: per Table R602.3(1)

### Rim Joist/Band Joist
- Rim joist to sill or top plate: 8d box at 4" OC toe nail (or 8d common at 6" OC)
- Band joist to joist: 3-16d common end nail

---

## Tying New Bracing to Existing Structure

### Critical Considerations for Additions
1. **Identify existing braced wall lines** in the existing structure where the addition connects
2. **Continuous load path:** New bracing must connect to existing diaphragm and foundation
3. **Blocking at connection:** Install blocking between existing joists/rafters at the intersection with the new addition
4. **Sheathing continuity:** Where new WSP meets existing wall, overlap or properly nail to existing framing
5. **Foundation connection:** New hold-downs must be installed at the connection point if the existing foundation doesn't have them

### Common Issues
- Existing structure may not have adequate bracing by current standards — this is not required to be upgraded unless the existing structure is being altered
- New addition bracing is designed for the new addition's loads, not the entire building
- If the addition changes the building's seismic weight significantly (e.g., second-story addition), engineering analysis may be required for the combined structure

---

## Seismic Design Categories in California

Most of California falls in SDC D0, D1, or D2. The SDC is determined from:
- Site class (soil type)
- Short-period spectral response acceleration (SDS) per ASCE 7-22

| SDC | Typical California Locations |
|---|---|
| SDC C | Very limited areas far from active faults |
| SDC D0 | Some coastal and valley areas with good soils |
| SDC D1 | Most of suburban Southern California |
| SDC D2 | Near-fault zones, soft soils near active faults |

For SDC D1 and D2, bracing requirements are significantly higher than SDC C, and hold-down connectors are always required at braced wall panel ends.

---

## When Engineering Is Required for Bracing

Engineered shear wall design (per CBC/ASCE 7) is required when:
1. Braced wall lines exceed 35 ft spacing
2. Irregular building configurations (L-shaped, T-shaped with large offsets)
3. Large openings that cannot be addressed with prescriptive portal frames
4. Buildings with soft stories (e.g., garage below, living space above)
5. Structures in SDC D2 with conditions exceeding Table R602.10.3(1)
6. Multi-story additions where dead load calculations are needed for hold-down sizing
