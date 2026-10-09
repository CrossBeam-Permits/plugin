---
title: "Fire-Resistance Ratings — Table 601, Exterior Walls, Opening Protectives, and Assembly Determination"
category: fire-safety
relevance: "Load for any multi-unit project requiring fire-resistance-rated construction. Covers Table 601 ratings by construction type, exterior wall ratings by fire separation distance, opening limitations, fire door/window requirements, and how to determine assembly ratings."
key_code_sections: "CBC Table 601, Table 1505.1, 602.1, 703.2, 705.5, Table 705.5, Table 705.9, 716.1, Table 716.1(2), Table 716.1(3); CRC R902.1"
---

## Fire-Resistance Ratings — Table 601, Exterior Walls, Opening Protectives, and Assembly Determination

### Table 601 — Fire-Resistance Rating Requirements by Construction Type (Hours)

Extracted for the four construction types most relevant to multi-unit residential (R-2 apartments, R-3 townhomes):

| Building Element | Type III-A | Type III-B | Type V-A | Type V-B |
|------------------|-----------|-----------|---------|---------|
| **Primary structural frame** | 1 | 0 | 1 | 0 |
| **Bearing walls — Exterior** | 2 | 2 | 1 | 0 |
| **Bearing walls — Interior** | 1 | 0 | 1 | 0 |
| **Nonbearing walls — Interior** | 0 | 0 | 0 | 0 |
| **Floor construction and secondary members** | 1 | 0 | 1 | 0 |
| **Roof construction and secondary members** | 1 | 0 | 1 | 0 |

(CBC Table 601)

**Critical footnotes for residential:**
- **Footnote b (roof reduction):** For R-1, R-2, and R-2.1, fire protection of members *other than* the primary structural frame is not required where every part of the roof construction is **20 feet or more above any floor immediately below**. Fire-retardant-treated wood may be used for such unprotected members. (Table 601, footnote b.2)
- **Footnote e (exterior walls):** Bearing wall exterior ratings shown above are minimums from Table 601; the actual required rating may be **higher** based on fire separation distance per Table 705.5. Always check both tables and use the greater value. (Table 601, footnote e)
- **Footnote d (interior nonbearing):** The 0-hour rating for interior nonbearing walls/partitions is a default — other code sections (708 fire partitions, 707 fire barriers, 1020 corridor walls) may impose higher ratings.

**Practical impact by type:**
- **Type V-A** (most common wood-frame multi-unit): Every structural element, bearing wall, floor, and roof requires **1-hour** fire-resistance rating
- **Type V-B** (unprotected wood-frame): No fire-resistance ratings required by Table 601 alone, but exterior walls still require ratings based on fire separation distance (Table 705.5), and dwelling unit separations still require fire partitions (708)
- **Type III-A** (podium/mixed-use): Same as V-A for interior elements (1-hour), but exterior bearing walls jump to **2-hour**
- **Type III-B**: Exterior bearing walls require **2-hour** rating (noncombustible exterior is the Type III hallmark), but all interior elements are 0-hour

### Table 705.5 — Exterior Wall Fire-Resistance Ratings Based on Fire Separation Distance

For Group R (residential) occupancies, exterior walls require fire-resistance ratings based on both construction type and fire separation distance. Group R falls into the "A, B, E, F-2, I, R, S-2, U" column of Table 705.5.

**California amendment for Group R:** Exterior walls shall be rated for exposure to fire from **both sides** regardless of fire separation distance. This is stricter than the base IBC, which only requires both-sides rating at ≤10 feet. (CBC 705.5, CA amendment)

| Fire Separation Distance (X) | Construction Type | Required Rating (Group R) |
|------------------------------|-------------------|--------------------------|
| **X < 5 ft** | All | **1 hour** |
| **5 ≤ X < 10 ft** | IA, IVA | **1 hour** |
| **5 ≤ X < 10 ft** | Others (III-A, III-B, V-A, V-B, etc.) | **1 hour** |
| **10 ≤ X < 30 ft** | IIB, VB | **0 hours** |
| **10 ≤ X < 30 ft** | Others (III-A, III-B, V-A, etc.) | **1 hour** |
| **X ≥ 30 ft** | All | **0 hours** |

(CBC Table 705.5)

**Key footnotes:**
- **Footnote a:** Load-bearing exterior walls must *also* comply with Table 601. Use the **greater** of the two ratings. For example, Type III-A bearing exterior wall at FSD < 5 ft: Table 601 says 2-hour, Table 705.5 says 1-hour — use **2-hour**.
- **Footnote i (R-3 exception):** For a Group R-3 building of Type II-B or V-B construction, exterior wall fire-resistance rating is not required where FSD is 5 feet or greater, or where sprinklered throughout per 903.3 and FSD is 3 feet or greater.

**Continuity of exterior wall rating** (CBC 705.6): The fire-resistance rating shall extend from the top of the foundation or floor/ceiling assembly below to the underside of the floor sheathing, roof sheathing, deck or slab above.

### Table 705.9 — Maximum Area of Exterior Wall Openings by Fire Separation Distance

| Fire Separation Distance (ft) | Unprotected, No Sprinkler | Unprotected, Sprinklered | Protected |
|-------------------------------|--------------------------|-------------------------|-----------|
| **0 to < 3** | Not Permitted | Not Permitted | Not Permitted |
| **3 to < 5** | Not Permitted | 15% | 15% |
| **5 to < 10** | 10% | 25% | 25% |
| **10 to < 15** | 15% | 45% | 45% |
| **15 to < 20** | 25% | 75% | 75% |
| **20 to < 25** | 45% | No Limit | No Limit |
| **25 to < 30** | 70% | No Limit | No Limit |
| **30 or greater** | No Limit | No Limit | No Limit |

(CBC Table 705.9)

**Values are percentages of the exterior wall area, per story.** Sprinklered = NFPA 13 system per 903.3.1.1.

**Practical impact for multi-unit residential:**
- Since new R-2 and R-3 buildings require sprinklers (CBC 903.2.8), most projects use the "Unprotected, Sprinklered" column
- At FSD < 3 ft: **no openings at all** — common issue for zero-lot-line townhomes
- At FSD 3-5 ft: maximum **15%** of wall area in openings
- At FSD ≥ 20 ft: **unlimited** openings (sprinklered)
- Where both protected and unprotected openings exist in the same wall story, the mixed opening formula (Equation 7-2) applies: Ap/ap + Au/au ≤ 1 (CBC 705.9.4)

**Vertical separation of openings** (CBC 705.9.5): Openings in exterior walls in adjacent stories must be separated vertically by not less than **3 feet** using 1-hour spandrel panels (rated both sides) or 30-inch flame barriers, where openings are within 5 feet of each other horizontally.

Exceptions: Not required for buildings 3 stories or less above grade, or buildings with NFPA 13 or 13R sprinkler systems.

### Opening Protectives — Fire Doors and Fire Windows (CBC 716)

When openings in fire-rated walls require protection, the opening protective (fire door, fire window, fire shutter) must have a fire protection rating per Tables 716.1(2) and 716.1(3). The fire protection rating of the opening protective is always **less than** the fire-resistance rating of the wall.

#### Fire Door Ratings — Table 716.1(2) (Relevant Extracts)

| Wall Assembly Type | Wall Rating | Min. Fire Door Rating |
|-------------------|-------------|----------------------|
| **Fire walls / fire barriers > 1 hour** | 2 hours | 1-1/2 hours |
| **Fire walls / fire barriers > 1 hour** | 1-1/2 hours | 1-1/2 hours |
| **Fire barriers = 1 hour** (shaft enclosures, exit stairways, exit passageways) | 1 hour | 1 hour |
| **Other fire barriers** | 1 hour | 3/4 hour (45 min) |
| **Fire partitions — Corridor walls** | 1 hour | 1/3 hour (20 min) |
| **Fire partitions — Corridor walls** | 1/2 hour | 1/3 hour (20 min) |
| **Other fire partitions** (dwelling unit separations) | 1 hour | 3/4 hour (45 min) |
| **Other fire partitions** | 1/2 hour | 1/3 hour (20 min) |
| **Exterior walls** | 3 hours | 1-1/2 hours |
| **Exterior walls** | 2 hours | 1-1/2 hours |
| **Exterior walls** | 1 hour | 3/4 hour (45 min) |

(CBC Table 716.1(2))

**For multi-unit residential:**
- **Dwelling unit entry doors** (in 1-hour fire partitions): **45-minute** (3/4-hour) fire door required
- **Corridor doors** (in 1-hour corridor walls): **20-minute** (1/3-hour) fire door required — tested per NFPA 252 or UL 10C, without hose stream test (CBC 716.2.2.1)
- **Exit stairway doors** (in 1-hour fire barriers): **1-hour** fire door with 450 deg F temperature rise at 30 minutes (CBC 716.2.2.3). Exception: temperature rise not required in buildings with NFPA 13 or 13R sprinklers.

**Door vision panels:** Fire-protection-rated glazing in doors is limited to **100 sq in** in fire barriers rated > 1 hour. In 20-minute corridor doors, fire-protection-rated glazing is permitted at the maximum size tested (CBC Table 716.1(2), CBC 716.2.5.3).

**Self-closing / latching:** All fire doors must be self-closing or automatic-closing and latching (CBC 716.2.6.1, 716.2.6.2). Exception: fire doors in common walls separating dwelling units in R-1 are permitted without automatic or self-closing devices (716.2.6.1, Exception 1).

#### Fire Window Ratings — Table 716.1(3) (Relevant Extracts)

| Wall Assembly Type | Wall Rating | Min. Fire Window Rating | Glazing Marking |
|-------------------|-------------|------------------------|-----------------|
| **Fire partitions** | 1 hour | 3/4 hour (45 min) | OH-45 or W-60 |
| **Fire partitions** | 1/2 hour | 1/3 hour (20 min) | OH-20 or W-30 |
| **Exterior walls** | > 1 hour | 1-1/2 hours | OH-90 or W-XXX |
| **Exterior walls** | 1 hour | 3/4 hour (45 min) | OH-45 or W-60 |
| **Exterior walls** | 1/2 hour | 1/3 hour (20 min) | OH-20 or W-30 |
| **Fire walls** | All | Not Permitted | W-XXX (fire-resistance-rated only) |
| **Fire barriers > 1 hour** | > 1 hour | Not Permitted | W-XXX (fire-resistance-rated only) |

(CBC Table 716.1(3))

**Area limitation for interior fire windows:** Total glazing area in fire-protection-rated window assemblies shall not exceed **25% of the area of a common wall** with any room (CBC 716.3.2.1.2).

**Exterior wall openings requiring protection** (per 705.3, 705.9, 705.9.5, or 705.9.6) must have a fire protection rating of not less than **3/4 hour** (CBC 716.3.4).

### Determining Fire-Resistance Ratings of Assemblies (CBC 703.2)

The fire-resistance rating of a building element, component, or assembly is determined by one of the following methods — **without** incorporating automatic sprinklers or fire suppression (CBC 703.2):

#### Method 1: Tested Assemblies (703.2.1)
Fire-resistance rating determined by testing per **ASTM E119 or UL 263**. This is the gold standard. Tested assemblies are documented by:
- UL Fire Resistance Directory (most commonly referenced)
- Gypsum Association Fire Resistance Design Manual (GA-600)
- Manufacturer proprietary test reports

Key rules for tested assemblies:
- **Nonsymmetrical walls** must be tested from both sides; the rating is the shorter duration, unless the least fire-resistant side was tested and accepted by the building official (CBC 703.2.1.1)
- **Supplemental features** (items not tested as part of the assembly) must not reduce the required rating (CBC 703.2.1.4)
- Combustible aggregates are permitted in gypsum and Portland cement concrete mixtures (CBC 703.2.1.2)

#### Method 2: Analytical Methods (703.2.2)
Fire resistance may be determined by analytical methods based on the fire exposure and acceptance criteria of ASTM E119 or UL 263:
1. Fire-resistance designs documented in **approved sources** (e.g., GA-600)
2. **Prescriptive designs** per CBC Section 721
3. **Calculations** per CBC Section 722
4. **Engineering analysis** based on comparison with tested assemblies
5. Fire-resistance designs **certified by an approved agency**

#### Method 3: Alternate Methods (703.2.3)
Where neither testing nor analytical methods apply, an alternative protection method per CBC 104.2.3 may be used with building official approval.

### Common Assemblies for Multi-Unit Residential

These are the most frequently specified assemblies in multi-unit wood-frame construction:

#### 1-Hour Wood Frame Wall (Bearing or Nonbearing)
- 2x4 or 2x6 wood studs at 16" o.c.
- **5/8" Type X gypsum board** on each side
- Yields 1-hour fire-resistance rating (UL U305, U301 series, or GA WP 3510 and similar)
- Used for: interior bearing walls (Type V-A), dwelling unit separations (fire partitions), corridor walls

#### 2-Hour Wood Frame Wall
- 2x4 or 2x6 wood studs at 16" o.c.
- **Two layers of 5/8" Type X gypsum board** on each side (or one layer each side with specific stud configurations per tested assembly)
- Yields 2-hour fire-resistance rating
- Used for: exterior bearing walls (Type III-A/B), fire barriers where 2-hour is required, occupancy separations

#### 1-Hour Floor/Ceiling Assembly
- Wood I-joists or dimensional lumber at 16" or 24" o.c.
- **5/8" Type X gypsum board** on the ceiling side
- Subfloor of 3/4" plywood or OSB on top
- May require specific insulation and resilient channel per the tested assembly
- Yields 1-hour fire-resistance rating (UL L500/L501 series, or GA FC 5610 and similar)
- Used for: floor construction (Type V-A and III-A), horizontal dwelling unit separations
- Must also meet **STC 50 and IIC 50** sound ratings for dwelling unit separations (CBC 1206)

#### 1-Hour Roof/Ceiling Assembly
- Wood trusses or rafters
- **5/8" Type X gypsum board** on the ceiling side
- Roof sheathing above
- Yields 1-hour fire-resistance rating
- Used for: roof construction (Type V-A and III-A)

**Important:** Always verify the specific assembly design number (UL, GA, or manufacturer listing) and ensure all components match the tested assembly exactly. Substitutions — even seemingly minor ones like changing fastener spacing or insulation type — can invalidate the rating.

### Parapets on Exterior Walls (CBC 705.12)

Parapets are required on exterior walls of buildings, with the following relevant exceptions:

1. Wall is **not required to be fire-resistance rated** per Table 705.5 (FSD-based)
2. Building area ≤ 1,000 sq ft per floor
3. Walls terminating at roofs of ≥ 2-hour construction or entirely noncombustible
4. **1-hour exterior walls** terminating at underside of roof sheathing where roof framing parallel to wall is 1-hour rated for 4 feet (Groups R and U) and no roof openings within 5 feet, with minimum Class B roof covering
5. **Groups R-2 and R-3 specific:** Wall may terminate at underside of roof sheathing in Types III, IV, and V where entire building has Class C roof covering and either noncombustible/FRTW sheathing for 4 feet OR 5/8" Type X gypsum board beneath the roof deck for 4 feet

(CBC 705.12, Exceptions 4 and 5)

Where required, parapets must be **not less than 30 inches** above the roof/wall intersection, with the same fire-resistance rating as the supporting wall, and noncombustible faces for the uppermost 18 inches (CBC 705.12.1).

### Table 1505.1 — Minimum Roof Covering Fire Classification by Construction Type

Roof coverings are tested per **ASTM E108 or UL 790** and classified as Class A (highest), B, or C (minimum).

| Construction Type | IA | IB | IIA | IIB | IIIA | IIIB | IV | VA | VB |
|---|---|---|---|---|---|---|---|---|---|
| **State minimum** | B | B | B | C | B | C | B | B | C |

(CBC Table 1505.1; CRC R902.1)

**Key points:**
- Class A = effective against severe fire exposure (concrete/clay tile, metal, fiberglass-reinforced asphalt, slate)
- Class B = effective against moderate fire exposure (some treated wood shakes)
- Class C = effective against light fire exposure (some roll roofing, treated wood shingles)
- In **VHFHSZ areas**, Class A is mandatory regardless of construction type (state code)
- **Many California cities override this table to require Class A for ALL construction types** — always check city amendments to CBC 1505.1 / CRC R902.1

**Exception:** Nonclassified roofing is permitted on Group U (utility) buildings with ≥6 feet fire-separation distance from adjacent structures.

**What to check on plans:** Look for roof covering fire class on (1) roof plan notes, (2) elevation keynotes specifying roofing material, (3) general notes referencing ASTM E108/UL 790, and (4) architectural detail sheets showing roofing assemblies. On multi-building projects, check each building type independently — inconsistencies between building types are a common drafting error.

### Cross-References
- See also: `fire-separation.md` — Party walls, dwelling unit separation, fire partitions, sound transmission
- See also: `construction-types.md` — Height, area, stories limits by construction type
- See also: `fire-sprinkler.md` — Sprinkler requirements affect opening area (Table 705.9) and party wall ratings
- See also: `egress-corridors.md` — Corridor wall ratings and door requirements (CBC 1020)
- See also: `occupancy-classification.md` — R-2 vs R-3 determines applicable columns in Table 705.5

### Key Code Sections
- CBC Table 601 — Fire-resistance rating requirements for building elements by construction type (hours)
- CBC 602.1 — General classification and requirement that elements comply with Tables 601 and 705.5
- CBC 602.3 — Type III construction definition (noncombustible exterior, FRTW permitted in 2-hr or less)
- CBC 602.5 — Type V construction definition (any material)
- CBC 703.2 — Fire-resistance determination methods (tested, analytical, alternate)
- CBC 703.2.1 — Tested assemblies (ASTM E119 / UL 263)
- CBC 703.2.1.1 — Nonsymmetrical walls tested from both sides
- CBC 703.2.2 — Analytical methods (approved sources, Section 721 prescriptive, Section 722 calculations)
- CBC 705.5 — Exterior wall fire-resistance ratings (CA amendment: both-sides exposure for Group R)
- CBC Table 705.5 — Exterior wall rating by fire separation distance and occupancy group
- CBC 705.6 — Continuity of exterior wall fire-resistance rating (foundation to sheathing above)
- CBC 705.8 — Unexposed surface temperature and equivalent opening factor (Equation 7-1)
- CBC Table 705.9 — Maximum exterior wall opening area by FSD and protection degree
- CBC 705.9.1 — Allowable area of openings (unlimited unprotected permitted in certain conditions)
- CBC 705.9.4 — Mixed openings formula (Equation 7-2: Ap/ap + Au/au ≤ 1)
- CBC 705.9.5 — Vertical separation of openings (3-ft spandrel or 30-in flame barrier)
- CBC 705.12 — Parapet requirements and exceptions (30-inch minimum height)
- CBC 716.1 — Opening protectives general requirements (NFPA 80 installation)
- CBC Table 716.1(2) — Fire door/shutter assembly ratings and glazing markings by wall type
- CBC Table 716.1(3) — Fire window assembly ratings and glazing markings by wall type
- CBC 716.2.2.1 — Corridor door assemblies (20-minute rating, smoke and draft control)
- CBC 716.2.2.3 — Exit stairway doors (450 deg F temperature rise at 30 min)
- CBC 716.2.6.1 — Self-closing / automatic-closing fire doors
- CBC 716.3.2.1.2 — Fire window area limitation (25% of common wall area)
- CBC 716.3.4 — Exterior wall opening protectives (minimum 3/4-hour rating)
