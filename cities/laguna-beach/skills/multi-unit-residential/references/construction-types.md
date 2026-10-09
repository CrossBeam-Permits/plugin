---
title: "Construction Types — Height, Area, and Stories Limits"
category: classification
relevance: "Load when determining whether a proposed multi-unit building is code-compliant for height, stories, and area based on its construction type and occupancy. Critical for early project feasibility."
key_code_sections: "CBC 602.1-602.5, Table 601, Table 504.3, Table 504.4, Table 506.2, 506.2.1, 506.3"
---

## Construction Types — Height, Area, and Stories Limits

### Construction Type Definitions

| Type | Description | Typical Multi-Unit Use |
|------|-------------|----------------------|
| **Type I-A/B** | Noncombustible throughout (steel/concrete) | High-rise apartments (7+ stories) |
| **Type II-A** | Noncombustible, 1-hr rated | Mid-rise apartments (4-5 stories) |
| **Type II-B** | Noncombustible, 0-hr rated | Low-rise apartments |
| **Type III-A** | Noncombustible exterior walls, combustible interior, 1-hr rated | Mixed-use podium buildings |
| **Type III-B** | Noncombustible exterior walls, combustible interior, 0-hr rated | Low-rise mixed-use |
| **Type IV-A/B/C/HT** | Mass timber (CLT) construction | Emerging for mid-rise residential |
| **Type V-A** | Any materials, 1-hr rated (wood frame) | **Most common for townhomes and low-rise apartments** |
| **Type V-B** | Any materials, 0-hr rated (wood frame) | Small residential projects |

(CBC 602.2–602.5)

### Table 601 — Fire-Resistance Rating Requirements (Hours)

Extracted for the construction types most relevant to multi-unit residential:

| Building Element | Type III-A | Type III-B | Type V-A | Type V-B |
|------------------|-----------|-----------|---------|---------|
| **Primary structural frame** | 1 | 0 | 1 | 0 |
| **Bearing walls — Exterior** | 2 | 2 | 1 | 0 |
| **Bearing walls — Interior** | 1 | 0 | 1 | 0 |
| **Nonbearing walls — Interior** | 0 | 0 | 0 | 0 |
| **Floor construction** | 1 | 0 | 1 | 0 |
| **Roof construction** | 1 | 0 | 1 | 0 |

(CBC Table 601)

**For the 35-unit townhome test case (Type V-A):** All structural frame, bearing walls, floors, and roofs require **1-hour fire-resistance rating**. This is the minimum for wood-frame construction with rated assemblies.

### Table 504.3 — Allowable Height in Feet (R-2 and R-3, Residential)

| Occupancy | Sprinkler Status | Type III-A | Type III-B | Type V-A | Type V-B |
|-----------|-----------------|-----------|-----------|---------|---------|
| **R-2** | NS (existing only) | 65 | 55 | 50 | 40 |
| **R-2** | S13R (NFPA 13R) | 60 | 55 | 50 | 40 |
| **R-2** | S (NFPA 13, no area incr.) | 85 | 75 | 70 | 60 |
| **R-2** | S (NFPA 13, with area incr.) | 65 | 55 | 60 | 40 |
| **R-3** | NS (existing only) | 65 | 55 | 50 | 40 |
| **R-3** | S13D (NFPA 13D) | 60 | 60 | 50 | 40 |
| **R-3** | S13R (NFPA 13R) | 60 | 55 | 60 | 60 |
| **R-3** | S (NFPA 13) | 65 | 55 | 70 | 60 |

(CBC Table 504.3)

**Notes:**
- NS values are only for evaluation of **existing** buildings per the California Existing Building Code (footnote d). New Group R occupancies are **required** to have sprinklers per CBC 903.2.8 (footnote h).
- S13R = NFPA 13R system (Section 903.3.1.2)
- S13D = NFPA 13D system (Section 903.3.1.3) — allowed for R-3 only, **not R-2**

### Table 504.4 — Allowable Number of Stories (R-2 and R-3, Residential)

| Occupancy | Sprinkler Status | Type III-A | Type III-B | Type V-A | Type V-B |
|-----------|-----------------|-----------|-----------|---------|---------|
| **R-2** | NS (existing only) | 4 | 4 | 3 | 2 |
| **R-2** | S13R | 4 | 4 | 4 | 3 |
| **R-2** | S (NFPA 13, no area incr.) | 5 | 5 | 4 | 3 |
| **R-2** | S (NFPA 13, with area incr.) | 4 | 4 | 4 | 2 |
| **R-3** | NS (existing only) | 4 | 4 | 3 | 3 |
| **R-3** | S13D | 4 | 4 | 3 | 3 |
| **R-3** | S13R | 4 | 4 | 4 | 4 |
| **R-3** | S (NFPA 13) | 5 | 5 | 4 | 4 |

(CBC Table 504.4)

**CBC 2025 PUBLISHING ERROR — Table 504.4 S13R Type V:** The published CBC 2025 transposes the R-1 and R-2 S13R values for Type V-A and V-B. The published table incorrectly shows R-2 S13R as V-A=3, V-B=2 (which are R-1's values) and R-1 S13R as V-A=4, V-B=3 (which are R-2's values). OSFM confirmed to UpCodes that this is a publishing error: *"The section of the table you referenced appears to be the result of a publishing error, as the Office of the State Fire Marshal (OSFM) did not propose this change as part of the triennial code update process. We will work to address and correct this item in the next available code update cycle."* The values above reflect the intended/correct values, consistent with CBC 2022 and the base IBC. If a plan checker cites the published CBC 2025 table showing R-2/VB/S13R = 2 stories, reference this OSFM statement.

**For the 35-unit townhome test case (R-3, Type V-A, 3 stories):**
- With S13D (NFPA 13D): 3 stories, 50 ft — **compliant at 3 stories**
- With S13R (NFPA 13R): 4 stories, 60 ft — compliant with margin
- With NFPA 13: 4 stories, 70 ft — compliant with margin

**Critical footnote for R-2, Type V-A (footnote o):** For R-2 buildings of Type V-A construction equipped with an NFPA 13 system, the sprinkler area increase (S1) is permitted in addition to the height/story increase, provided the height does not exceed **60 feet and 4 stories**.

### Table 506.2 — Allowable Area per Story (R-2 and R-3, Type V-A)

| Occupancy | NS | S1 (NFPA 13) | SM (no ht. incr.) |
|-----------|----|--------------|--------------------|
| **R-2** | 12,000 sf | 48,000 sf | 36,000 sf |
| **R-3** | UL | UL | UL |

(CBC Table 506.2)

**R-3 has unlimited area per story** — this is a significant advantage of the CRC/townhouse classification. R-2 buildings are area-limited and must calculate frontage increases per Section 506.3 and select the appropriate sprinkler column from Table 506.2.

### Area Increase Calculations (R-2 Only)

For R-2 buildings, the allowable area can be increased:

**Frontage increase (If)** — CBC 506.3:
Determined from Table 506.3.3 based on percentage of building perimeter fronting on a public way or open space (minimum 20 ft wide) and the open space distance. Maximum If = 75%.

**Sprinkler increase:** In the 2025 CBC, the sprinkler increase is built into Table 506.2 values directly. Select the appropriate column: S1 (single-story with NFPA 13), SM (multistory with NFPA 13), S13R, or S13D.

**Allowable area per story (single-occupancy)** — CBC 506.2.1 (Equation 5-1):
> Aa = At × (1 + If/100)

Where At = tabular allowable area factor (NS, S1, S13R, S13D, or SM as applicable) from Table 506.2, and If = frontage increase from Section 506.3.

### Fire Wall Separation Creates Separate Buildings

Each portion of a building separated by one or more **fire walls** complying with Section 706 is considered a **separate building** for purposes of height, area, and construction type. (CBC 503.1)

This is how large townhome developments achieve compliance: each group of townhomes separated by fire walls is treated as a separate building with its own area calculation.

### Cross-References
- See also: `occupancy-classification.md` — R-2 vs R-3 determination
- See also: `fire-resistance-ratings.md` — Detailed Table 601 and Table 705.5 requirements
- See also: `fire-sprinkler.md` — NFPA 13 vs 13R vs 13D applicability affects height/area
- See also: `fire-separation.md` — Fire walls (706) creating separate buildings

### Key Code Sections
- CBC 503.1 — Building height, stories, and area limitations; fire walls create separate buildings
- CBC 504.3, Table 504.3 — Allowable building height in feet by occupancy and construction type
- CBC 504.4, Table 504.4 — Allowable number of stories by occupancy and construction type
- CBC 506.2, Table 506.2 — Allowable area factor by occupancy and construction type
- CBC 506.2.1 — Allowable area per story for single-occupancy buildings (Equation 5-1)
- CBC 506.3 — Frontage increase determination (Table 506.3.3)
- CBC Table 601 — Fire-resistance rating requirements for building elements by construction type
- CBC 602.2–602.5 — Construction type definitions (Types I through V)
- CBC 903.2.8 — New Group R occupancies required to have sprinkler protection
