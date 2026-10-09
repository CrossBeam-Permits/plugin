---
title: Structural Design Criteria
category: structural
relevance: >
  Establishes the fundamental load and environmental design parameters that
  govern every structural element in a single-family dwelling — seismic design
  category, wind speed, snow load, live/dead loads, and deflection limits.
  Plan reviewers must verify these criteria are addressed before evaluating
  any specific framing, foundation, or lateral system detail.
key_code_sections:
  - CRC R301.1
  - CRC R301.2
  - CRC R301.2.1
  - CRC R301.2.2
  - CRC R301.2.2.1
  - CRC R301.3
  - CRC R301.4
  - CRC R301.5
  - CRC R301.6
  - CRC R301.7
  - CBC 1613.1
  - CBC 1613.2
---

# Structural Design Criteria

Reference for California single-family residential permit review.
Source: 2025 California Residential Code (CRC), Title 24, Part 2.5;
2025 California Building Code (CBC), Title 24, Part 2.

---

## 1. Design Criteria Overview

All buildings and structures shall be constructed to safely support all
loads — dead, live, roof, flood, snow, wind, and seismic — and provide a
complete load path from point of origin through load-resisting elements to
the foundation (CRC R301.1).

**[CA] California amendment**: Existing buildings housing protective social
care facilities established prior to 1972 are subject to the California Fire
Code and California Existing Building Code (CRC R301.1).

### Alternative Provisions (CRC R301.1.1)

The following standards are permitted as alternatives, subject to code
limitations:

1. AWC Wood Frame Construction Manual (WFCM)
2. AISI S230 — Cold-Formed Steel Prescriptive Method
3. ICC 400 — Log Structures

### Nonconventional Structural Elements (CRC R301.1.3)

Where structural elements exceed the prescriptive limits of Section R301 or
otherwise do not conform, design them in accordance with accepted engineering
practice and maintain compatibility with the conventional system. Engineered
design in accordance with the California Building Code is permitted for a
building or portion within CRC scope.

**[CA] California-specific triggers**:
- Where a structure deviates from substantial compliance with conventional
  wood-frame requirements, the building official shall require approval and
  stamping by a CA-licensed architect or engineer for the irregular or
  nonconforming portion (CRC R301.1.3.1).
- Wood-frame dwellings over two stories and a basement require stamped
  plans (CRC R301.1.3.2).
- Floor, wall, and roof-ceiling structural elements in dwellings designed of
  cold-formed steel, concrete, masonry, or structural insulated panels and
  prescribed by the CRC require stamped plans (CRC R301.1.3.3).

---

## 2. Climatic and Geographic Design Criteria

Each jurisdiction fills in Table R301.2 with locally applicable values for
the parameters below (CRC R301.2).

When the plans do not print SDC or ultimate design wind speed, read
the parcel facts `design_parameters` and use those parcel-resolved inputs under
the current 2025 CRC/CBC paths. State the source and Site Class assumption
(`assumed_default_D` means no geotechnical report was available). Under
R602.10.3, use Tables R602.10.3(1) and (2) for SDC A/B and detached dwellings in
SDC C. For townhouses in SDC C and all buildings in SDC D0-D2, use the greater
bracing amount from Table (1) or (3), with the applicable adjustment factors in
Table (2) or (4), respectively. Only FLAG the missing jurisdiction value when
the relevant design parameter is absent/null. Plan-stated jurisdiction values
and a project geotechnical report control over the parcel snapshot/default.

### 2.1 Wind Design (CRC R301.2.1)

Ultimate design wind speeds are taken from Figure R301.2(2) (3-second gust,
Exposure C, 33 ft above ground, ~700-year MRI). Exposure category is
determined on a site-specific basis (CRC R301.2.1.4).

Determine the project wind speed from the locally completed Table R301.2 and
the applicable map. Examine mountainous terrain, gorges, ocean promontories,
and other special wind regions for site-specific wind conditions.

A continuous uplift load path from roof to foundation is required
(CRC R301.2.1).

### 2.2 Seismic Design Categories (CRC R301.2.2)

Buildings are assigned a Seismic Design Category (SDC) from Figure
R301.2.2.1(1) — based on default site class per ASCE 7, Chapter 11
(CRC R301.2.2.1).

**Alternate SDC determination** (CRC R301.2.2.1.1): The SDC may be
determined using CBC Section 1613. The site-specific SDS value sets the SDC
per the following table:

| Calculated SDS | Seismic Design Category |
|---|---|
| SDS <= 0.17g | A |
| 0.17g < SDS <= 0.33g | B |
| 0.33g < SDS <= 0.50g | C |
| 0.50g < SDS <= 0.67g | D0 |
| 0.67g < SDS <= 0.83g | D1 |
| 0.83g < SDS <= 1.25g | D2 |
| 1.25g < SDS | E |

(Table R301.2.2.1.1)

Determine the project's SDC under R301.2.2.1 or CBC 1613; do not infer it from
a statewide geographic generalization.

**SDC E reclassification** (CRC R301.2.2.1.2): Buildings in SDC E may be
reclassified to D2 if either:
1. A detailed evaluation per CBC shows the site is actually SDC D; or
2. All exterior shear wall lines or braced wall panels are in one plane
   vertically from the foundation to the uppermost story, floors do not
   cantilever past exterior walls, and the building is regular per R301.2.2.6.

Otherwise, SDC E buildings must be designed per the CBC (not prescriptive
CRC).

### 2.3 Seismic Provisions Applicability (CRC R301.2.2)

| Building Type | SDC Where Seismic Provisions Apply |
|---|---|
| Townhouses (3+ units) | C, D0, D1, D2 |
| Detached 1-2 family | D0, D1, D2 |

### 2.4 Weights of Materials (CRC R301.2.2.2)

Average dead loads for prescriptive seismic design shall not exceed:

| Assembly | Maximum Dead Load |
|---|---|
| Roof + ceiling (horizontal projection) | 15 psf (25 psf with bracing adjustment) |
| Floor assemblies | 10 psf |
| Exterior light-frame wood walls | 15 psf |
| Exterior light-frame CFS walls | 14 psf |
| Interior light-frame wood walls | 10 psf |
| Interior light-frame CFS walls | 5 psf |
| 8-inch masonry walls | 80 psf |
| 6-inch concrete walls | 85 psf |
| SIP walls | 10 psf |

### 2.5 Irregular Buildings (CRC R301.2.2.6)

Buildings in SDC C through D2 with any of the following irregularities must
have the irregular portions engineered:

1. Shear wall / braced wall offsets out of plane, except for qualifying
   wood-light-frame cantilevers or setbacks satisfying all five Item 1 framing
   conditions
2. Floor or roof not laterally supported on all edges, except a floor portion
   supporting no shear wall, braced wall panel above, or roof may extend up to
   6 ft beyond a shear wall or braced wall line
3. A braced wall panel end over an opening below that extends more than 1 ft
   past the opening edge, subject to the Item 3 wood-light-frame header
   exception for qualifying openings up to 8 ft
4. Floor / roof opening > lesser of 12 ft or 50% of least dimension
5. Floor level vertical offset, except framing directly supported by continuous
   perimeter foundations or wood-light-frame floors lapped or tied per R502.6.1
6. No bracing in two perpendicular directions
7. A story above grade partially or completely braced by R602 wood or R603
   cold-formed-steel wall framing that includes masonry or concrete, except
   code-compliant fireplaces, chimneys, and masonry veneer
8. Hillside construction (slope > 1:5, cripple wall > 7 ft, < 50% enclosed
   living space below lowest floor), except where the lowest framed floor is
   supported directly on concrete or masonry walls for the full length of each
   side other than the downhill side

### 2.6 Height Limitations (CRC R301.2.2.7)

- Wood-frame: 3 stories above grade plane or the applicable limit in Table
  R602.10.3(3), whichever governs. SDC D2 over 2 stories requires engineered
  wind and seismic design.
- SIP: 2 stories above grade plane max.
- Story height for wood walls: 11 ft 7 in max. The 13-ft-7-in exception permits
  studs under R602.3.1 Exception 2 or 3 or an engineered wall-member design,
  with R602.10 bracing and lateral support at the top and bottom plates (CRC
  R301.3).

### 2.7 Snow Loads (CRC R301.2.3)

Ground snow loads from Figure R301.2(3) or CBC Section 1608. Prescriptive
provisions apply where ASD ground snow load pg(asd) <= 70 psf.

### 2.8 Seismic Restraint of Equipment (CRC R301.2.2.10)

In SDC D0-D2 (and townhouses in SDC C), fixed appliances and equipment shall
be supported, braced, or anchored under the manufacturer's recommendations or
R301.2.2.10.1. No seismic support is required for suspended ducts, conduit,
sprinkler, or plumbing systems; qualifying low-profile floor/roof equipment;
suspended equipment weighing 50 lb or less; or equipment weighing 400 lb or
less with its bottom no more than 4 ft above the adjacent floor. When
R301.2.2.10.1 is used, the supports, bracing, and anchorage must resist a
horizontal force equal to one-third the operating weight in any direction.

---

## 3. Story Height (CRC R301.3)

| Framing Type | Max Story Height | Max Stud Clear Height |
|---|---|---|
| Wood wall framing | 11 ft 7 in | Per Table R602.3(5) |
| Wood (with exception) | 13 ft 7 in | 12 ft (studs per R602.3.1 Exception 2 or 3, or engineered wall-member design; R602.10 bracing; lateral support at top and bottom plates) |
| Cold-formed steel | 11 ft 7 in | 10 ft |
| Masonry | 13 ft 7 in | 12 ft (+ 8 ft for gable ends) |
| ICF | 11 ft 7 in | 10 ft |
| SIP | 11 ft 7 in | 10 ft |

---

## 4. Dead Load (CRC R301.4)

Actual weights of materials and construction shall be used. Consider dead
load of fixed service equipment.

---

## 5. Live Load (CRC R301.5)

| Use | Uniform Load (psf) | Concentrated Load (lb) |
|---|---|---|
| Uninhabitable attics without storage | 10 | -- |
| Uninhabitable attics with limited storage | 20 | -- |
| Habitable attics / attics with fixed stairs | 30 | -- |
| Balconies (exterior) and decks | 60 | -- |
| Fire escapes | 40 | -- |
| Guards | -- | 200 |
| Handrail | -- | 200 |
| Passenger vehicle garages | 50 | 2,000 |
| Areas other than sleeping | 40 | -- |
| Sleeping areas | 30 | -- |
| Stairs | 40 | 300 |

(Table R301.5)

---

## 6. Roof Load (CRC R301.6)

Design for the greater of roof live load (Table R301.6) or ground snow load
(Table R301.2).

| Roof Slope | Tributary Area 0-200 sf | 201-600 sf | Over 600 sf |
|---|---|---|---|
| Flat or < 4:12 | 20 psf | 16 psf | 12 psf |
| 4:12 to < 12:12 | 16 psf | 14 psf | 12 psf |
| 12:12 and greater | 12 psf | 12 psf | 12 psf |

(Table R301.6)

---

## 7. Deflection Limits (CRC R301.7)

| Structural Member | Allowable Deflection |
|---|---|
| Rafters > 3:12 slope, no attached ceiling | L/180 |
| Interior walls and partitions | H/180 |
| Floors | L/360 |
| Ceilings with brittle finishes (plaster, stucco) | L/360 |
| Ceilings with flexible finishes (gypsum board) | L/240 |
| All other members (excl. guards/handrails) | L/240 |
| Exterior walls — wind — plaster/stucco finish | H/360 |
| Exterior walls — wind — other brittle finish | H/240 |
| Exterior walls — wind — flexible finish | H/120 |
| Lintels supporting masonry veneer | L/600 |

(Table R301.7)

Notes:
- Wind load for deflection may be taken as 0.7x the ASD component and
  cladding loads from Table R301.2.1(1).
- Cantilever members: L = 2x cantilever length.
- Exterior walls with interior gypsum board: limit H/180.

---

## 8. CBC Seismic Design Category Determination (CBC 1613)

For structures not using the CRC prescriptive maps, SDC is determined per
CBC 1613.2 using one of:

1. Figure 1613.2(1) based on Risk Category (default site conditions); or
2. ASCE 7 Chapter 11 (site-specific).

Where Site Class DE, E, or F soils are present, ASCE 7 must be used
(CBC 1613.2).

**[CA] Scope exception** (CBC 1613.1): Detached one- and two-family
dwellings in SDC A, B, or C are exempt from CBC seismic analysis. The seismic
force-resisting system of a wood-frame building conforming to CBC Section 2308
is not required to be analyzed as specified in CBC 1613.1.

---

## Key Code Sections

- **CRC R301.1** — Design criteria application, load path
- **CRC R301.1.3** — Nonconventional structural elements
- **CRC R301.2** — Climatic and geographic design criteria (Table R301.2)
- **CRC R301.2.1** — Wind design criteria, exposure categories
- **CRC R301.2.2** — Seismic provisions, applicability by SDC
- **CRC R301.2.2.1** — SDC determination (Figure R301.2.2.1(1))
- **CRC R301.2.2.1.1** — Alternate SDC via SDS (Table R301.2.2.1.1)
- **CRC R301.2.2.2** — Dead load limits for prescriptive seismic design
- **CRC R301.2.2.6** — Irregular building definitions
- **CRC R301.2.2.7** — Height limitations by SDC
- **CRC R301.3** — Story height limits by framing type
- **CRC R301.4** — Dead load
- **CRC R301.5** — Live load (Table R301.5)
- **CRC R301.6** — Roof load (Table R301.6)
- **CRC R301.7** — Deflection limits (Table R301.7)
- **CBC 1613.1** — Earthquake loads scope
- **CBC 1613.2** — SDC determination methods

## Cross-References

- **foundations.md** — Foundation design driven by loads established here
- **structural-lateral-seismic.md** — Wall bracing amounts keyed to SDC and
  wind speed from this file's criteria
