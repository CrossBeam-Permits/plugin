---
title: "Occupancy Classification & Change of Occupancy"
category: "Building — CBC Chapter 3"
relevance: "Loaded for every commercial TI. Determines whether the project is a same-occupancy alteration or a change of occupancy (which triggers CEBC Chapter 10)."
key_code_sections: "CBC 301-312, 508, Table 1004.5"
---

# Occupancy Classification & Change of Occupancy

The first question on every commercial TI review is: **is the new use in the same occupancy classification as the old use?** This reference walks through how to answer that, using CBC Chapter 3.

If you decide the occupancy changed, route to `structural-alterations.md` for the CEBC Ch. 10 cascade.

---

## 1. Occupancy Groups for Commercial TI

These are the occupancy groups you encounter in commercial TI (CBC 302.1 enumerates all groups; this skill excludes H, I, R, L, C, and E in detail — those route elsewhere).

| Group | Description | Common TI Uses |
|---|---|---|
| **A-1** (CBC 303.2) | Assembly with fixed seating for performing arts | Theaters, concert halls, TV studios with live audience |
| **A-2** (CBC 303.3) | Assembly intended for food/drink consumption | Restaurants, bars, banquet halls, cafeterias — **routes to california-restaurant-ti** |
| **A-3** (CBC 303.4) | Assembly: worship, recreation, amusement (non-A-1/A-2/A-4) | Yoga studios, dance studios, lecture halls, art galleries, museums, libraries, churches, bowling alleys, gyms without spectator seating, exhibit halls, community halls |
| **A-4** (CBC 303.5) | Assembly with spectator seating for indoor sports | Arenas, skating rinks, indoor swim with seating |
| **A-5** (CBC 303.6) | Outdoor assembly | Stadiums, grandstands, bleachers |
| **B** (CBC 304.1) | Business / professional / service | Offices, banks, professional services, barber/beauty, training/skill development (martial arts, gymnastics — see note), printing, post office, motor-vehicle showrooms, ambulatory care, outpatient clinics, animal hospitals, civic admin, food-processing commercial kitchens <=2,500 sf NOT associated with restaurants |
| **F-1** (CBC 306.2) | Moderate-hazard factory / industrial | Manufacturing, machine shops, woodworking, bakeries, dry cleaning plants, food processing > 2,500 sf, breweries, lithium-ion battery R&D |
| **F-2** (CBC 306.3) | Low-hazard factory / industrial | Ceramics, glass, masonry, foundries, metals (noncombustible products) |
| **M** (CBC 309.1) | Mercantile | Retail stores, department stores, drug stores, markets, motor-fuel dispensing, sales rooms, wholesale stores |
| **S-1** (CBC 311.2) | Moderate-hazard storage | Warehouses (most goods), furniture, tires, lumber, mini-storage, motor-vehicle repair garages within MAQ limits, dry boat storage indoor, lithium-ion battery storage |
| **S-2** (CBC 311.3) | Low-hazard storage | Storage of noncombustible products on wood pallets / in paper cartons, public parking garages |
| **U** (CBC 312.1) | Utility & miscellaneous accessory | Sheds, tanks, fences > 7 ft, communication equipment buildings < 1,500 sf, private garages |

### Small-Assembly Carve-Outs (CRITICAL for TI reviewers)

These let an assembly use stay in Group B:

- **CBC 303.1.1** — A building or tenant space used for assembly with **occupant load < 50** is classified as **Group B**.
- **CBC 303.1.2** — A room used for assembly that is **< 750 sf AND accessory** to another occupancy is classified as Group B or as part of that occupancy. (Both conditions must hold.)
- **CBC 303.1.4** — Religious educational rooms / auditoriums with **< 100 occupants** per room are part of the primary place-of-religious-worship occupancy.

### Accessory Storage Rule (CBC 311.1.1)

A room used for storage purposes that is **accessory to another occupancy** is classified as part of that occupancy (NOT separately as S-1/S-2). This matters when an office TI carves out a stockroom — it remains B.

### B vs A-3 Decision Tree for Common TI Conversions

```
Is the activity dance / yoga / martial arts / gymnastics / fitness?
│
├─ Per CBC 304.1, "training and skill development not in a school or academic program
│  (including tutoring centers, martial arts studios, gymnastics and similar uses
│  regardless of the ages served, and where not classified as a Group A occupancy)"
│  is Group B.
│
├─ Check the carve-outs:
│  ├─ OL < 50? → B per 303.1.1
│  ├─ Room < 750 sf AND accessory? → B per 303.1.2
│  └─ Neither → A-3
│
└─ When ambiguous, the building official decides per 302.1 (occupancy "it most nearly resembles").
```

---

## 2. Mixed Occupancies (CBC 508)

When a tenant space contains more than one occupancy, the reviewer must decide among three approaches (CBC 508.2):

1. **Accessory occupancies** (CBC 508.2) — Occupancies < 10% of building area on the story and not over MAQ for H — classified with the main occupancy.
2. **Non-separated occupancies** (CBC 508.3) — All occupancies share construction-type / height-and-area limits of the most restrictive. No fire-rated separation, but the entire space inherits the most restrictive systems requirements.
3. **Separated occupancies** (CBC 508.4) — Each occupancy is enclosed by fire-rated separation per Table 508.4. Each can independently meet its own height/area / systems limits.

**Most common TI mixed-occupancy scenarios:**

| Combo | Typical Treatment |
|---|---|
| B office + S-1 storage in same suite | Accessory (storage < 10%) — usually no rated separation needed |
| B office + A-3 (training room > 50 OL, > 750 sf) | Separated — 1-hr B-to-A-3 separation per Table 508.4 (NS column) |
| M retail + S-1 stockroom > 10% | Either non-separated (most common in retail) or separated |
| B office + F-1 light manufacturing | Almost always separated (1-2 hr depending on construction type & sprinkler status) |

**Table 508.4 abbreviated** (S = sprinklered, NS = not sprinklered; values are hours of fire-resistance):

| From\To | A, E | B | F-1 | M | S-1 | S-2/U |
|---|---|---|---|---|---|---|
| A, E | -- | 1 (S) / 2 (NS) | 1 (S) / 2 (NS) | 1 (S) / 2 (NS) | 1 (S) / 2 (NS) | 1 (S) / 2 (NS) |
| B | -- | -- | 1 (S) / 2 (NS) | 1 (S) / 2 (NS) | 1 (S) / 2 (NS) | 1 (S) / 2 (NS) |
| F-1 | -- | -- | -- | 1 (S) / 2 (NS) | 1 (S) / 2 (NS) | 1 (S) / 2 (NS) |
| M | -- | -- | -- | -- | 1 (S) / 2 (NS) | 1 (S) / 2 (NS) |
| S-1 | -- | -- | -- | -- | -- | 1 (S) / 2 (NS) |

(Full table includes H, I, R, U — see CBC.)

---

## 3. Identifying a Change of Occupancy

A change of occupancy triggers CEBC Ch. 10. It occurs when ANY of the following apply (CEBC 202; CBC 202):

1. The occupancy classification changes (e.g., M → B, B → A-3, S-1 → F-1).
2. There is a change of *use* within the same classification that crosses a different fire-protection-system threshold in CBC Ch. 9 (e.g., M storage that increases combined fire area from 11,000 sf to 13,000 sf, crossing the 12,000-sf sprinkler line in 903.2.7).
3. A change creates a higher Risk Category (e.g., normal office → essential facility — rare in TI).

### Same-Occupancy "Change of Use" That Still Triggers Chapter 10

The most-missed scenario: **a same-occupancy use change that crosses a CBC 903.2 threshold.** CEBC 1001.1 / 1011.1 both invoke Chapter 10 protections whenever "there is a different fire protection system threshold requirement in Chapter 9 of the current California Building Code than exists in the current building or space" — even within the same group.

Example: a B-occupancy tenant goes from 80 to 110 occupants (still B); not a change of occupancy classification, but does NOT cross 903.2.2 thresholds because B doesn't have a load-based sprinkler trigger — so this is just a Level 2/3 alteration. Versus M going from 11,000 sf single fire area to 13,000 sf — same Group M but crossing 903.2.7 — Chapter 10 applies.

### Hazard Category Tables (CEBC 1011)

When the occupancy IS changing, the direction matters:

**Means-of-egress hazard categories (CEBC Table 1011.5):**

| Category | Groups | Direction |
|---|---|---|
| 1 (highest) | H | Not allowed |
| 2 | I-2, I-3, I-4 | Restricted |
| 3 | A, E, M, R-1, R-2, R-4 | -- |
| 4 | B, F-1, R-3, R-4, S-1 | -- |
| 5 (lowest) | F-2, S-2, U | -- |

**Heights & areas hazard categories (CEBC Table 1011.6):**

| Category | Groups |
|---|---|
| 1 (highest) | H |
| 2 | A-1, A-2, A-3, A-4, I, R-1, R-2, R-4 Cond. 2 |
| 3 | E, F-1, S-1, M |
| 4 (lowest) | B, F-2, S-2, A-5, R-3, R-4 Cond. 1, U |

**Exterior-wall fire-resistance hazard categories (CEBC Table 1011.7):**

| Category | Groups |
|---|---|
| 1 (highest) | H |
| 2 | F-1, M, S-1 |
| 3 | A, B, E, I, R |
| 4 (lowest) | F-2, S-2, U |

**Direction rule:** Change to HIGHER hazard category (lower number) → must comply with current CBC for the new occupancy. Change to EQUAL/LOWER hazard → existing elements deemed acceptable (CEBC 1011.5.2, 1011.6.2, 1011.7.2).

### Common TI Change-of-Occupancy Outcomes

| Change | M-of-Egress (T1011.5) | Height/Area (T1011.6) | Ext Walls (T1011.7) | Net |
|---|---|---|---|---|
| B → A-3 (yoga, OL>=50) | 4 → 3 (HIGHER) | 4 → 2 (HIGHER) | 3 → 3 (equal) | Egress + height/area triggers |
| M → B (retail to office) | 3 → 4 (LOWER) | 3 → 4 (LOWER) | 2 → 3 (LOWER) | Existing accepted |
| B → M (office to retail) | 4 → 3 (HIGHER) | 4 → 3 (HIGHER) | 3 → 2 (HIGHER) | Egress + height/area + ext walls |
| S-1 → B (warehouse to office) | 4 → 4 (EQUAL) | 3 → 4 (LOWER) | 2 → 3 (LOWER) | Existing largely accepted, but check seismic per CEBC 1006.3 |
| M → A-2 (restaurant) | 3 → 3 (EQUAL) | 3 → 2 (HIGHER) | 2 → 3 (LOWER) | **Routes to california-restaurant-ti** |
| F-1 → B | 4 → 4 (EQUAL) | 3 → 4 (LOWER) | 2 → 3 (LOWER) | Existing accepted, seismic check |
| B → F-1 | 4 → 4 (EQUAL) | 4 → 3 (HIGHER) | 3 → 2 (HIGHER) | Height/area + ext walls |
| B → I-2 (24-hr medical) | 4 → 2 (HIGHER) | 4 → 2 (HIGHER) | 3 → 3 (EQUAL) | OUT OF SCOPE — OSHPD likely |

---

## 4. Occupant Load (CBC 1004) — Frequently Used for Group Assignment

Calculating occupant load (OL) is necessary to apply CBC 303.1.1 (A vs B carve-out) and to verify sprinkler/alarm thresholds. Use Table 1004.5 for areas without fixed seating; the most-relevant factors for commercial TI are in `california-baseline.md`'s quick-reference.

**Posting requirement (CBC 1004.9):** Any room used for assembly, classroom, dining, drinking, or similar purposes with OL >= 50 must have its occupant load posted near the main exit.

**Net vs Gross:**
- **Net** floor area = actual occupiable space (excludes circulation, structural elements, wall thickness, accessory areas not directly used by occupants).
- **Gross** floor area = entire floor area within exterior walls / fire separations (includes circulation and accessory storage).

---

## Plan Check Review Checklist — Occupancy Classification

Default applicability: `ALL`

| ID | Tag | Item | Pass Criteria | Code Section | Likely sheets |
|---|---|---|---|---|---|
| OC-1 | ALL | Existing occupancy on record | Cited from prior C of O, building card, or pre-existing permit. FLAG where the existing occupancy is inferred rather than documented. | CEBC 1001.2 | Cover, code data |
| OC-2 | ALL | Proposed occupancy classification | Each use area identified, with a CBC 303-312 citation matching the use description. FAIL where a missing code-data block prevents review. | CBC 302.1, 303-312 | Cover, floor plans |
| OC-3 | ALL | Occupant load calculated | Table 1004.5 factor applied to floor area of each function space; sum reported on cover sheet. FAIL where absent and egress / plumbing / assembly thresholds depend on it. | CBC 1004.5 | Code data |
| OC-4 | ASSEMBLY-50+ | A-occupancy carve-outs checked | If OL < 50 and use is assembly-like, B classification confirmed; if room < 750 sf and accessory, B confirmed. FLAG where an assembly-like use lacks the math. | CBC 303.1.1, 303.1.2 | Floor, code data |
| OC-5 | ALL | Mixed-occupancy approach declared | Accessory / non-separated / separated identified on plans. FAIL where multiple occupancies have no declared approach. | CBC 508.2-508.4 | Code data |
| OC-6 | ALL | Separated-occupancy ratings shown | Where 508.4 used, fire barriers + ratings shown per Table 508.4. FAIL where the separated approach is declared but ratings are absent. | CBC 508.4; CBC 707 | Life safety, floor |
| OC-7 | CHANGE-OF-OCCUPANCY | Change-of-occupancy flag | Plans clearly state whether project is or is not a change of occupancy; if yes, route through CEBC Ch.10. FLAG on a declared-vs-derived mismatch. | CEBC 1001.1, 1011.1 | Cover, code data |
| OC-8 | ALL | Restaurant trigger check | If any food prep / cooking / A-2 dining → submittal routes to california-restaurant-ti. FLAG where the food/cooking boundary needs routing. | (Routing rule) | Cover, floor |
| OC-9 | ASSEMBLY-50+ | Occupant-load posting note | Where OL >= 50 in an assembly/classroom/dining space, posting requirement noted. FLAG where the threshold is likely met and the note is absent. | CBC 1004.9 | Code data |
| OC-10 | ALL | Hazardous-materials inventory | If any chemicals/storage that could push into Group H, HMIS submitted. | CBC 307, CFC 5001 — OUT OF SCOPE here | Cover, storage |
| OCC-11 | CITY-DELTA | Tenant use-to-zone symbol gate | The proposed tenant use is permitted in the parcel's zone. Proceed where the use matrix reads permitted (P / Pc / Pc*); FAIL or FLAG where a conditional or blank symbol leaves an entitlement gate unresolved. **Never infer the matrix from state law** — read the city zoning rules; where the city input is absent, that is a `verify` naming the missing use-matrix determination. | City zoning rules (city overlay) | Site facts, zoning |
| OCC-12 | CITY-DELTA | Parking demand delta for change of use | Where the use changes, the parking demand delta is computed against the CITY's parking table. PASS where there is no delta or the math is provided; FLAG where a new use may increase demand and no math is shown, or where the city parking table is unavailable. | City zoning / parking table (city overlay) | Cover, site, zoning |
