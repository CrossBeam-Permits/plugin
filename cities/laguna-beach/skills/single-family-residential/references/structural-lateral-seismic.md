---
title: Structural Lateral and Seismic Systems
category: structural
relevance: >
  Covers the wall bracing, lateral force resistance, and seismic connection
  requirements that apply to California single-family residential construction
  based on the assigned seismic design category and building type. Plan
  reviewers must verify braced wall line layout, bracing method and length,
  cripple wall bracing, anchor bolt details with plate washers, and hold-down
  connections when those provisions apply.
key_code_sections:
  - CRC R602.10
  - CRC R602.10.1
  - CRC R602.10.2
  - CRC R602.10.3
  - CRC R602.10.4
  - CRC R602.10.5
  - CRC R602.10.10
  - CRC R602.11
  - CRC R602.9
  - CRC R403.1.6
  - CRC R403.1.6.1
  - CRC R301.2.2.1
  - CBC 1613.2
---

# Structural Lateral and Seismic Systems

Reference for California single-family residential permit review.
Source: 2025 California Residential Code (CRC), Title 24, Part 2.5;
2025 California Building Code (CBC), Title 24, Part 2.

---

## 1. Seismic Design Category Determination

### 1.1 CRC Prescriptive Method (CRC R301.2.2.1)

SDC assigned from Figure R301.2.2.1(1) based on default site class per
ASCE 7 Chapter 11.

### 1.2 CBC / Site-Specific Method (CRC R301.2.2.1.1 / CBC 1613.2)

Site-specific SDS may be determined per CBC Section 1613. SDC is then
assigned per Table R301.2.2.1.1:

| Calculated SDS | SDC |
|---|---|
| SDS <= 0.17g | A |
| 0.17g < SDS <= 0.33g | B |
| 0.33g < SDS <= 0.50g | C |
| 0.50g < SDS <= 0.67g | D0 |
| 0.67g < SDS <= 0.83g | D1 |
| 0.83g < SDS <= 1.25g | D2 |
| 1.25g < SDS | E |

Use the SDC assigned through the code-defined process; do not infer a category
from a statewide prevalence or fault-proximity assumption. SDC E triggers CBC
design unless reclassified to D2 per R301.2.2.1.2.

### 1.3 SDC E Reclassification (CRC R301.2.2.1.2)

SDC E buildings may use D2 prescriptive provisions if:
1. Detailed CBC evaluation shows site is actually SDC D; or
2. All of the following: all exterior shear wall lines or braced wall panels
   are in one vertical plane, no floor cantilevers extend past exterior walls,
   and the building is regular per R301.2.2.6.

---

## 2. Wall Bracing Overview (CRC R602.10)

Buildings shall be braced per Section R602.10 or, where applicable, Section
R602.12. Where any portion does not comply, that portion shall be designed and
constructed per R301.1.

---

## 3. Braced Wall Lines (CRC R602.10.1)

### 3.1 Definition and Layout

Braced wall lines are straight lines in the building plan along which
bracing is provided. The length of a braced wall line is the distance
between its ends (intersection with perpendicular braced wall line, angled
wall line, or exterior wall) (CRC R602.10.1.1).

### 3.2 Permitted Offsets (CRC R602.10.1.2)

Braced wall panels may be offset up to **4 feet** from the designated braced
wall line — applies to both exterior and interior walls. No more than
two-thirds of the required braced wall panel length may be located on one side
of the designated braced wall line.

### 3.3 Braced Wall Line Spacing (CRC R602.10.1.3)

| Application | Condition | Max Spacing | Exception |
|---|---|---|---|
| Wind bracing | Ultimate wind < 140 mph | 60 ft | None |
| Seismic — SDC A-C detached | — | Use wind | Use wind |
| Seismic — SDC A-B townhouse | — | Use wind | Use wind |
| Seismic — SDC C townhouse | — | 35 ft | Up to 50 ft with Table R602.10.3(4) adjustment |
| Seismic — SDC D0-D2 (1-2 story) | — | 25 ft | Up to 35 ft for single room <= 900 sf |
| Seismic — SDC D0-D2 | — | 25 ft | Up to 35 ft with Table R602.10.3(4) adjustment |

(Table R602.10.1.3)

### 3.4 Angled Walls (CRC R602.10.1.4)

Wall may angle out of plane for max diagonal length of 8 ft. Greater than
8 ft = separate braced wall line.

---

## 4. Braced Wall Panels (CRC R602.10.2)

Braced wall panels are full-height wall sections without vertical or
horizontal offsets, constructed with one of the methods in Section R602.10.4.

### 4.1 Location Requirements (CRC R602.10.2.2)

- Nearest edge within **10 feet** of each end of braced wall line.
- Distance between adjacent panel edges: **20 feet max**.

**SDC D0-D2 additional requirement** (CRC R602.10.2.2.1):
Braced wall panels shall be located at each end of the braced wall line.

Exceptions in SDC D0-D2:
- Methods WSP, BV-WSP, and continuous sheathing methods may begin up to 10 ft
  from the end under Exception 1. The 24-inch panel-on-each-side corner path is
  limited to WSP, CS-WSP, CS-G, and CS-PF; the alternative 1,800-lb hold-down
  path applies to the Exception 1 methods, including BV-WSP.
- Methods PFH, ABW, BV-WSP with hold-down: may begin up to 10 ft from end.

### 4.2 Minimum Number (CRC R602.10.2.3)

- Braced wall line <= 16 ft: 2 panels of any length, or 1 panel >= 48 in.
- Braced wall line > 16 ft: minimum 2 panels.

---

## 5. Required Length of Bracing (CRC R602.10.3)

When the plans omit SDC or ultimate design wind speed, read the parcel-resolved
values from the parcel facts `design_parameters` and compute the required
length below. This data path is an operational review workflow, not a code-law
requirement. State the data source and use the site condition supplied by the
project documents or the default stated by the controlling current source; do
not hard-code Site Class D from this reference. Only flag a missing
jurisdiction input when the relevant design parameter is absent or null; a
plan-stated or geotechnical-report-derived value controls.

### 5.1 Which Tables to Use

| SDC | Building Type | Bracing Table | Adjustment Table |
|---|---|---|---|
| A, B | All | R602.10.3(1) (wind) | R602.10.3(2) |
| C | Detached | R602.10.3(1) (wind) | R602.10.3(2) |
| C | Townhouse | Greater of R602.10.3(1) or R602.10.3(3) | R602.10.3(2) or R602.10.3(4) |
| D0, D1, D2 | All | Greater of R602.10.3(1) or R602.10.3(3) | R602.10.3(2) or R602.10.3(4) |

### 5.2 Seismic Bracing Table Summary (Table R602.10.3(3))

Basis: 10 ft wall height, 10 psf floor DL, 15 psf roof/ceiling DL, braced
wall line spacing <= 25 ft.

**SDC D0 — minimum total bracing length (feet) per braced wall line:**

| Story | BWL Length | Methods WSP, ABW, PFH | Methods CS-WSP, CS-G, CS-PF |
|---|---|---|---|
| 1-story | 25 ft | 4.5 | 3.8 |
| 2-story, 2nd floor | 25 ft | 4.5 | 3.8 |
| 2-story, 1st floor | 25 ft | 9.5 | 8.0 |

**SDC D1:**

| Story | BWL Length | Methods WSP, ABW, PFH | Methods CS-WSP, CS-G, CS-PF |
|---|---|---|---|
| 1-story | 25 ft | 5.0 | 4.3 |
| 2-story, 2nd floor | 25 ft | 5.0 | 4.3 |
| 2-story, 1st floor | 25 ft | 11.3 | 9.6 |

**SDC D2:**

| Story | BWL Length | Methods WSP, ABW, PFH | Methods CS-WSP, CS-G, CS-PF |
|---|---|---|---|
| 1-story | 25 ft | 6.3 | 5.4 |
| 2-story, 2nd floor | 25 ft | 6.3 | 5.4 |
| 2-story, 1st floor | 25 ft | 13.8 | 11.7 |
| Cripple wall below 1-2 story | 25 ft | 18.8 | 16.0 |
| 3-story | Any | NP | NP |

(Interpolated from Table R602.10.3(3) at 25 ft BWL length)

Note: D2 three-story dwellings require engineered design.

### 5.3 Seismic Adjustment Factors (Table R602.10.3(4))

The rows below are a nonexhaustive excerpt, not a substitute for the live
table. Use all applicable live-table rows and footnotes for each calculation,
including the separate SDC C townhouse, stone or masonry veneer, limited-
veneer, and diaphragm-ratio conditions.

| Item | Condition | Factor |
|---|---|---|
| Wall height | <= 10 ft | 1.0 |
| Wall height | > 10 ft, <= 12 ft | 1.2 |
| BWL spacing, SDC D0-D2 | > 25 ft, <= 30 ft | 1.2 |
| BWL spacing, SDC D0-D2 | > 30 ft, <= 35 ft | 1.4 |
| Wall dead load | < 8 psf | 0.85 |
| Wall dead load | 8-15 psf | 1.0 |
| Roof/ceiling DL, multi-story | <= 15 psf | 1.0 |
| Roof/ceiling DL, multi-story | > 15, <= 25 psf | 1.1 |
| Roof/ceiling DL, 1-story or top | > 15, <= 25 psf | 1.2 |
| Interior gypsum omitted | — | 1.5 |
| Horizontal blocking omitted | Methods WSP, PBS, CS-WSP | 2.0 |

Total required length = table value x product of all applicable factors.

---

## 6. Bracing Methods (CRC R602.10.4)

### 6.1 Intermittent Bracing Methods

| Code | Method | Min. Thickness | Key Connection |
|---|---|---|---|
| LIB | Let-in bracing | 1x4 wood or metal strap, 45-60 deg | Wood: 2-8d common nails or 3-8d listed nails per stud and plates; metal strap: per manufacturer |
| DWB | Diagonal wood boards | 3/4" (1" nominal) | 2-8d nails per stud |
| WSP | Wood structural panels | 3/8" | 6" edges, 12" field |
| SFB | Structural fiberboard | 1/2" or 25/32" | 3" edges, 6" field |
| GB | Gypsum board | 1/2" | 7" edges, 7" field |
| PBS | Particleboard sheathing | 3/8" or 1/2" | 3" edges, 6" field |
| PCP | Portland cement plaster | Per R703.6 | 6" o.c. all framing |
| HPS | Hardboard panel siding | 7/16" | 4" edges, 8" field |
| ABW | Alternate braced wall | 3/8" WSP | Hold-down required |
| PFH | Portal frame w/ hold-downs | 3/8" WSP | Per R602.10.6.2 |
| PFG | Portal frame at garage | 7/16" WSP | Per R602.10.6.3 |
| BV-WSP | WSP with masonry veneer | 7/16" | 4" edges, 12" field, 4" at end posts |

### 6.2 Continuous Sheathing Methods

| Code | Method | Min. Thickness | Key Connection |
|---|---|---|---|
| CS-WSP | Continuously sheathed WSP | 3/8" | 6" edges, 12" field |
| CS-G | CS-WSP adjacent to garage | 3/8" | Per CS-WSP |
| CS-PF | Continuously sheathed portal frame | 7/16" | Per R602.10.6.4 |
| CS-SFB | Continuously sheathed fiberboard | 1/2" or 25/32" | 3" edges, 6" field |

(Table R602.10.4)

**SDC D0-D2 restrictions**:
- Methods PFG and CS-SFB are **not permitted**.
- Adhesive attachment (including GB) is **not permitted** in SDC C-D2.
- Methods PFH, PFG, and ABW limited to single story or first of two stories.

### 6.3 Mixing Methods (CRC R602.10.4.1)

- Story to story: intermittent bracing and continuous-sheathing methods may be
  mixed, subject to each method's other restrictions.
- Wall line to wall line within a story: permitted (intermittent + CS only
  in SDC A-C with wind <= 130 mph).
- Along a wall line, intermittent methods may be mixed only in SDC A and B and
  detached SDC C buildings.
- Mixing CS-WSP, CS-G, and CS-PF, or combining ABW, PFH, and PFG, follows the
  distinct method and calculation limits in R602.10.4.1; do not substitute a
  blanket highest-value rule.
- Mixing interior intermittent bracing with exterior continuous sheathing is
  limited to SDC A and B and detached one- and two-family dwellings in SDC C,
  and must also comply with R602.10.7.

### 6.4 Interior Finish (CRC R602.10.4.3)

The baseline is 1/2" gypsum board on the opposite side, fastened per Table
R602.3(1) or R702.3.5; an equivalent interior finish is permitted. The
opposite-side finish is not required for Methods GB, BV-WSP, ABW, PFH, PFG,
and CS-PF unless R302.6 requires it. For other methods, interior finish may be
omitted with the applicable bracing-length adjustment, except that it may not
be omitted for Method LIB. Interior finish shall not be glued in SDC D0-D2.

---

## 7. Minimum Panel Length (CRC R602.10.5)

| Method | 8 ft wall | 10 ft wall | 12 ft wall |
|---|---|---|---|
| WSP, SFB, PBS, etc. | 48" | 48" | 58" |
| GB | 48" | 48" | 58" |
| LIB | 55" | 69" | NP |
| ABW (SDC D0-D2) | 32" | 34" | NP |
| CS-WSP (adj opening <= 64") | 24" | 30" | 36" |

(Table R602.10.5)

---

## 8. Hold-Down and Tie-Down Connections

### 8.1 Method ABW Hold-Down Forces (CRC R602.10.6.1)

| SDC / Wind | Story | 8 ft wall | 10 ft wall |
|---|---|---|---|
| SDC A-C, < 140 mph | One story | 1,800 lb | 1,800 lb |
| SDC A-C, < 140 mph | First of two | 3,000 lb | 3,000 lb |
| SDC D0-D2, < 140 mph | One story | 1,800 lb | 1,800 lb |
| SDC D0-D2, < 140 mph | First of two | 3,000 lb | 3,000 lb |

(Table R602.10.6.1)

Walls > 10 ft in SDC D0-D2: Not Permitted for ABW.

### 8.2 Method PFH — Portal Frame with Hold-Downs (CRC R602.10.6.2)

Constructed per Figure R602.10.6.2. Header shall not extend over more than
one opening.

### 8.3 Method BV-WSP Hold-Down Forces (CRC R602.10.6.5.4)

Use Table R602.10.6.5.4 only for the qualifying Method BV-WSP path under
R602.10.6.5.2 and R602.10.6.5.4 where veneer exceeds the first story. The
table separates forces for nonaligned panels from cumulative forces at aligned
panels. First-story-only veneer and limited veneer follow their separate
R602.10.6.5 rules; do not apply this table as a general force schedule to every
veneered dwelling.

### 8.4 Wind Bracing Adjustment with Hold-Downs (Table R602.10.3(2))

Optional 800-lb hold-down at end of each braced wall panel (top story only)
reduces required bracing length by factor of 0.80 only for Methods DWB, WSP,
SFB, PBS, PCP, and HPS.

---

## 9. Cripple Wall Bracing (CRC R602.9, R602.10.10)

### 9.1 General Cripple Wall Requirements (CRC R602.9)

- Framed with studs not smaller than studding above.
- Exceeding 4 ft height: studs sized for additional story.
- Exterior cripple wall height < 14 inches: continuously sheathed with WSP on
  one side, or solid blocking.
- Supported on continuous foundations.

### 9.2 Cripple Wall Bracing (CRC R602.10.10)

- Braced with same method as wall above, per Tables R602.10.3(1) and
  R602.10.3(3).
- Required bracing length multiplied by **1.15** factor.
- Where gypsum board omitted from inside of cripple wall: additional
  adjustment factor per Tables R602.10.3(2) and R602.10.3(4) applied on top
  of the 1.15.

### 9.3 SDC D0, D1 and Townhouses SDC C (CRC R602.10.10.1)

- Bracing limited to **Methods WSP and CS-WSP only**.
- Distance between adjacent panel edges: **14 ft max**.
- Where interior braced wall lines lack continuous foundation: adjacent
  cripple walls braced with WSP or CS-WSP, length multiplied by **1.5**.
  If insufficient length: reduce panel edge fasteners to 4" o.c. and
  multiply by 0.7. If still insufficient: engineered design required.

### 9.4 SDC D2 (CRC R602.10.10.2)

Cripple walls braced per Tables R602.10.3(3) and R602.10.3(4). Three-story
buildings: cripple walls not permitted.

### 9.5 Redesignation (CRC R602.10.10.3)

Where all cripple wall segments <= 48 inches: may be redesignated as
first-story wall (stories above re-counted as second/third). Where any
segment > 48 inches: entire cripple wall counts as additional story.

---

## 10. Connection to Foundation (CRC R602.11, R403.1.6)

### 10.1 Wall Anchorage — General

Baseline anchor-bolt provisions are 1/2" diameter, 6 ft o.c. maximum,
extending 7 inches into concrete, centered in the middle third of the plate
width, with at least two bolts per plate section. Approved anchors or straps
providing equivalent anchorage are permitted. An end bolt must be no more than
12 inches and no less than seven bolt diameters from the plate end. Apply the
two short-offset-wall exceptions in the live section where relevant (CRC
R403.1.6).

### 10.2 Wall Anchorage in SDC D0-D2 and SDC C Townhouses (CRC R602.11.1)

**Plate washers** required: 0.229" x 3" x 3" minimum between sill plate
and nut on all braced wall line anchor bolts. Diagonal slotting of plate
washer permitted (3/16" wider than bolt, slot <= 1-3/4" long) with standard
cut washer between plate washer and nut. This applies to wood light-frame
structures in SDC D0-D2 and wood light-frame townhouses in SDC C; approved
anchor straps are excepted from the plate-washer rule.

### 10.3 Braced Wall Panel Connections — SDC D0-D2 (CRC R602.10.8.1)

- Braced wall panels fastened to foundations per R602.11.1.
- Top plate lap splices: face-nailed with not less than **8-16d nails** on
  each side of splice.

### 10.4 Stepped Foundations in SDC D0-D2 (CRC R602.11.2)

Where braced wall line height varies > 4 ft along its length:

1. Where lowest floor rests on sill bolted to foundation >= 8 ft long: line
   is considered braced. Double plate of cripple wall spliced by extending
   upper top plate >= 4 ft along foundation. Anchor bolts within 1 ft and
   3 ft of foundation step.
2. Where cripple walls occur: bracing per R602.10.10 applies.
3. Where only bottom of foundation is stepped: R403.1.6 and R602.11.1
   apply.

---

## 11. Diaphragm Nailing

### 11.1 Roof Sheathing (Table R602.3(1))

Wood structural panel roof sheathing to framing:
- 3/8" - 1/2": 8d common or RSRS-01 nails, 6" at edges and intermediate
  supports (4" in the Footnote f edge/ridge zones where its wind and framing-
  specific-gravity conditions apply).
- 19/32" - 3/4": 8d common nails, 6" edges.

### 11.2 Floor Sheathing (Table R602.3(1))

Wood structural panel subfloor to framing:
- 3/8" - 1/2": 6d common, 6" edges, 12" intermediate.
- 19/32" - 3/4": 8d common, 6" edges, 12" intermediate.

### 11.3 Wall Sheathing — Braced Wall Panels

Per Table R602.10.4 and Table R602.3(3) for exterior WSP sheathing. Edge
nailing at braced wall panels is critical for lateral resistance.

---

## 12. California-Specific Seismic Amendments Summary [CA]

The following provisions reflect California amendments that go beyond the
base IRC:

1. **Licensed professional required** for wood-frame > 2 stories, any
   non-conventional framing, cold-formed steel, concrete, masonry, or SIP
   structural elements (CRC R301.1.3.1 through R301.1.3.3).

2. **Soil testing in SDC C+**: when soil testing is performed at an SDC C-or-
   greater site, the geotechnical report must include site class and SDS
   determination per CBC 1613 (CRC R401.4).

3. **SDC E buildings** must be designed per CBC unless reclassified to D2
   (CRC R301.2.2.1.2).

4. **Foundation elevation on graded sites** [CA]: top of exterior foundation
   >= 12" + 2% above the street gutter at the point of discharge or an
   approved drainage-device inlet. The building official may approve an
   alternate elevation where drainage away from the building is demonstrated
   (CRC R403.1.7.3).

5. **Expansive soils**: foundations and slabs are designed per CBC 1808.6,
   except that the building official may approve slab-on-ground or other
   systems that performed adequately in similar soil conditions (CRC
   R403.1.8).

6. **Capillary break** required with vapor retarder per CALGreen
   (CRC R506.3.3.1).

---

## Key Code Sections

- **CRC R301.2.2** — Seismic provisions applicability
- **CRC R301.2.2.1** — SDC determination (Figure R301.2.2.1(1))
- **CRC R301.2.2.1.1** — Alternate SDC via SDS (Table R301.2.2.1.1)
- **CRC R301.2.2.6** — Irregular building definitions
- **CRC R602.9** — Cripple wall general requirements
- **CRC R602.10** — Wall bracing scope
- **CRC R602.10.1** — Braced wall lines (layout, spacing)
- **CRC R602.10.1.3** — BWL spacing table
- **CRC R602.10.2** — Braced wall panel location and count
- **CRC R602.10.3** — Required bracing length (Tables R602.10.3(1)-(4))
- **CRC R602.10.4** — Bracing methods (Table R602.10.4)
- **CRC R602.10.5** — Minimum panel length (Table R602.10.5)
- **CRC R602.10.6.1** — ABW hold-down forces
- **CRC R602.10.6.2** — PFH portal frame with hold-downs
- **CRC R602.10.6.5** — Bracing with masonry veneer in SDC D0-D2
- **CRC R602.10.10** — Cripple wall bracing (1.15 factor)
- **CRC R602.10.10.1** — Cripple walls SDC D0-D1 and SDC C townhouses (WSP/CS-WSP only, 14 ft max)
- **CRC R602.11** — Wall anchorage
- **CRC R602.11.1** — Plate washers for wood light-frame D0-D2 structures
  and wood light-frame SDC C townhouses
- **CRC R602.11.2** — Stepped foundations in SDC D0-D2
- **CRC R403.1.6** — Anchor bolts (1/2", 6 ft o.c.)
- **CRC R403.1.6.1** — Enhanced anchorage for wood light-frame D0-D2
  structures and wood light-frame SDC C townhouses
- **CBC 1613.2** — SDC determination methods

## Cross-References

- **structural-design-criteria.md** — SDC determination, load criteria, and
  height limitations that govern which bracing provisions apply
- **foundations.md** — Foundation anchorage details, footing reinforcement
  in SDC D0-D2, continuous footing requirements for interior braced walls
