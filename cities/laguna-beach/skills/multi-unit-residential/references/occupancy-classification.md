---
title: "Occupancy Classification — R-2 vs R-3, CRC vs CBC Applicability"
category: classification
relevance: "Load first for any multi-unit residential project. Determines which code (CRC vs CBC) governs the project and which fire/egress/accessibility requirements apply."
key_code_sections: "CBC 302.1, 310.3 (R-2), 310.4 (R-3), 508.1 (mixed occupancy); CRC R101.2 (scope)"
---

## Occupancy Classification — R-2 vs R-3, CRC vs CBC Applicability

### The Core Distinction: R-2 vs R-3

The California Building Code classifies residential occupancies based on the number of dwelling units and the nature of occupancy:

**Residential Group R-2** — Occupancies "containing sleeping units or **more than two dwelling units** where the occupants are primarily permanent in nature," including:
- Apartment houses
- Congregate living facilities (nontransient) with more than 16 occupants
- Boarding houses (nontransient)
- Dormitories
- Hotels/motels (nontransient)
- Live/work units

(CBC 310.3)

**Residential Group R-3** — Occupancies "where the occupants are primarily permanent in nature and not classified as Group R-1, R-2.1, R-2.2, R-3.1, R-4 or I," including:
- Buildings that **do not contain more than two dwelling units**
- Congregate residences (nontransient) with 16 or fewer occupants
- Lodging houses with five or fewer guest rooms

(CBC 310.4)

### When CRC vs CBC Applies

The California Residential Code (CRC) applies to:

> "The construction, alteration, movement, enlargement, replacement, repair, equipment, use and occupancy, location, removal and demolition of **detached one- and two-family dwellings and townhouses not more than three stories above grade plane** in height **with a separate means of egress** and their accessory structures not more than three stories above grade plane in height."

(CRC R101.2)

**Key criteria for CRC applicability:**
1. Detached one-/two-family dwelling OR townhouse
2. Not more than 3 stories above grade plane
3. Each unit has a **separate means of egress** (direct exterior exit)

### Townhouse vs Apartment — The Critical Boundary

| Feature | Townhouse (CRC — R-3) | Apartment (CBC — R-2) |
|---------|----------------------|----------------------|
| **Code** | California Residential Code | California Building Code |
| **Egress** | Each unit has separate, independent exterior exit | Common corridors, shared exits/stairs |
| **Max stories** | 3 above grade plane (CRC scope) | Per Table 504.4 by construction type |
| **Unit count** | Any number of townhouse units (each is independent) | More than 2 dwelling units in a building |
| **Party walls** | CRC R302.2 (1-hr sprinklered / 2-hr unsprinklered) | CBC 706 fire walls or 708 fire partitions |
| **Sprinklers** | CRC R309.1 (mandatory, NFPA 13D allowed) | CBC 903.2.8 (NFPA 13 or 13R, **not** 13D) |
| **Accessibility** | Not subject to Ch 11A covered multifamily | CBC Ch 11A applies (Type A/B units required) |

**For the 35-unit townhome test case (3-story, Type V-A, separate means of egress):**
- Each townhouse unit is classified **R-3** under the CRC
- The CRC governs fire separation (R302), egress (R318/R319), and sprinklers (R309)
- However, the CBC still governs **site-wide** requirements: fire access roads, hydrant spacing, accessible parking, and common area accessibility

### When a Townhouse Project Falls Under CBC Instead

A multi-unit project that looks like townhomes but has **any** of the following falls under CBC as R-2:
1. **Common corridors or shared exits** — units do not have independent exterior egress
2. **More than 3 stories** above grade plane — exceeds CRC scope
3. **Units stacked vertically** without independent egress at each level (apartment configuration)
4. **Mixed-use** with ground-floor commercial — triggers CBC 508

### Mixed Occupancy (CBC 508)

When a building contains more than one occupancy group, it must comply with CBC 508:

- **Nonseparated occupancies** (CBC 508.3): Each portion classified individually; the most restrictive provisions of Chapter 9 (fire protection) apply to the total nonseparated area. Allowable area calculated per the most restrictive occupancy. No separation required between nonseparated occupancies.

- **Separated occupancies** (CBC 508.4): Each portion classified individually with fire barrier separations per Table 508.4 between different occupancy groups.

Common mixed-occupancy scenarios for multi-unit residential:
- **R-2 over S-2** (apartments over parking garage) — requires 1-hr separation (Table 508.4)
- **R-2 with B** (apartments with ground-floor office) — requires 1-hr separation
- **R-2 with M** (apartments with ground-floor retail) — requires 1-hr separation
- **R-3 townhomes with U** (townhomes with accessory structures) — per CRC

(CBC 508.1, 508.3, 508.4)

### California-Specific Occupancy Groups

The CBC includes California amendments not found in the base IBC:

| Group | Description | Key Difference |
|-------|-------------|----------------|
| R-2.1 | 24-hour care facilities, 7+ clients (assisted living, group homes) | Supervised residential environment |
| R-2.2 | CDCR community facilities | State correctional |
| R-3.1 | Licensed 24-hour care, 6 or fewer clients | Within dwelling unit scale |
| R-4 | 7-16 ambulatory clients, supervised, 24-hour | Between R-3.1 and R-2.1 scale |

(CBC 310.3.1, 310.3.2, 310.4.1, 310.5)

### Cross-References
- See also: `construction-types.md` — Height/area limits by occupancy and construction type
- See also: `fire-separation.md` — Party wall requirements (CRC R302 vs CBC 706/708)
- See also: `fire-sprinkler.md` — Sprinkler system selection (13D vs 13R vs 13)
- See also: `accessibility-units.md` — When Chapter 11A applies (R-2 but not CRC townhomes)
- See also: `egress-exits.md` — Separate means of egress requirement for CRC applicability

### Key Code Sections
- CBC 302.1 — Occupancy classification framework
- CBC 310.1 — Residential Group R general definition
- CBC 310.3 — Residential Group R-2 (more than 2 dwelling units, permanent)
- CBC 310.4 — Residential Group R-3 (not more than 2 dwelling units, permanent)
- CBC 508.1 — Mixed occupancy general requirements
- CBC 508.3 — Nonseparated occupancies
- CBC 508.4 — Separated occupancies (fire barrier required per Table 508.4)
- CRC R101.2 — CRC scope: townhouses ≤3 stories with separate means of egress
