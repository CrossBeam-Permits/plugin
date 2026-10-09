---
title: "Cross-Reference — When to Hand Off to california-restaurant-ti"
category: "Routing / boundary rules"
relevance: "Loaded when the submittal mentions cooking, food prep, A-2 dining, grease, walk-in coolers, or any food-facility content."
key_code_sections: "(Routing-only)"
---

# Boundary: `california-commercial-ti` vs `california-restaurant-ti`

Restaurant work is its own permit type with its own state skill (`california-restaurant-ti`). Commercial TI explicitly EXCLUDES restaurant scopes. This reference captures the boundary so the reviewer routes correctly.

When in doubt, hand the file to the restaurant skill — the restaurant skill is a superset (it pulls from the same CBC/CFC/CEC/Title 24 sources this skill uses, and adds CRFC + AB 671 + Type-I hood + grease interceptor).

---

## 1. Restaurant-Routing Triggers — STOP THIS SKILL, LOAD RESTAURANT SKILL

If ANY of these conditions appear in the project description, scope of work, equipment list, or floor plan, hand off:

| Trigger | Why It's Restaurant Scope |
|---|---|
| Commercial cooking equipment (fryer, grill, range, oven, broiler, charbroiler, salamander, wok, panini press with grease, griddle) | Requires CMC Type-I hood + UL 300 fire suppression + grease duct |
| Type-I or Type-II hood in scope | Per CMC §507-513 — separate review track |
| Grease interceptor / grease trap / grease arrestor | CPC §1014 — restaurant-specific |
| Food prep sink, 3-compartment warewashing sink | CRFC §114099, §114163 — health department review track |
| Walk-in cooler / walk-in freezer / dedicated cold-storage room with food | CRFC + CMC refrigeration code |
| A-2 occupancy classification (dining + drink consumption) per CBC 303.3 | Restaurants, bars, cafeterias, banquet halls, nightclubs |
| Bar / tavern with food service | A-2 |
| Coffee shop / café with prep beyond reheating | A-2 (depending on OL — see CBC 303.1.1 carve-out) |
| Tasting room with food | A-2 if OL >= 50; B if < 50 |
| Restaurant change of ownership permit | AB 671 fast-track pathway in restaurant skill |
| Food facility (per CRFC HSC §113789) | Health Dept jurisdiction — separate review |
| Outdoor dining / sidewalk dining | AB 592 — restaurant skill |
| Commissary kitchen / ghost kitchen / cloud kitchen | A-2 or B depending on retail aspect; restaurant skill |

### Small-Assembly Carve-Out (Edge Case)

Per CBC 303.1.1 / 303.1.2, a use that is *otherwise* A-2 but has OL < 50 OR is a room < 750 sf accessory to another occupancy can be classified Group B. This is a true edge case. Even when classification is B, if the kitchen has commercial cooking equipment producing grease-laden vapors, the CMC + CPC + CRFC obligations still attach — so the project still routes to `california-restaurant-ti`.

A retail bakery with no on-site cooking? Stays in this skill (B / M depending on retail mix).

A juice bar with blenders + sinks but no cooking? Generally B, no Type-I hood, no grease. Stays in this skill.

A coffee shop with espresso machines + reheating ovens (no grease)? Generally B, Type-II hood for steam if needed (no Type-I). Stays in this skill UNLESS food prep beyond reheating is added.

A salad / poke / smoothie place with no cooking + no grease? Stays in this skill.

---

## 2. What OVERLAPS Between Commercial TI and Restaurant TI

These sources are referenced by both skills. The restaurant skill is the authoritative source when restaurant work is in scope.

| Source | Commercial TI Use | Restaurant TI Use |
|---|---|---|
| CBC Ch. 3 (Occupancy) | A-3, B, F, M, S, U classifications | A-2 specifically, plus mixed-occupancy issues |
| CBC Ch. 5 (Heights & Areas) | All commercial occupancies | A-2 |
| CBC Ch. 9 (Fire Protection) | 903.2 sprinkler thresholds for all groups | 903.2.1.2 A-2 (lowest threshold) |
| CBC Ch. 10 (Egress) | All commercial occupancies | A-2 + assembly egress (1030) |
| CBC Ch. 11B (Accessibility) | 11B-202 / 11B-208 / 11B-213 / 11B-226 etc. | Same + dining-surface 5% accessible (11B-226) |
| CEBC Part 10 | All alteration levels + change of occupancy | Same |
| CFC | 903, 907, 904.12 (hood suppression) | Same + UL 300 detail |
| CMC | §403 ventilation, §504 outdoor air | Same + §507-513 Type-I/II hoods |
| CEC | Article 220 load calcs, etc. | Same + commercial-kitchen circuits |
| Title 24 Part 6 (Energy) | §141.0 (all alterations) | Same + commercial-kitchen energy + §141.0 sub-paths |
| Title 24 Part 11 (CALGreen) | Full Ch.5 if >= $200K | Same |

---

## 3. What DOES NOT Overlap — Restaurant-Only Sources

These are NOT covered by `california-commercial-ti`:

| Source | Topic |
|---|---|
| **California Retail Food Code (CRFC)** — HSC Division 104 Part 7 | Health Department construction: floors, walls, ceilings, lighting, ventilation, vermin exclusion, fixture spacing, sinks |
| **AB 671** — Gov. Code 66345-66345.4 | Restaurant TI fast-track / QPC pathway / 20-day deemed-approval |
| **AB 592** — HSC 114266(d), 114067, BPC 25750.5 | Outdoor dining, open-front operations |
| **CMC §507-513** | Type-I and Type-II kitchen hoods, exhaust rates, makeup air |
| **CPC §1014** | Grease interceptor sizing |
| **CPC §422 (food service fixture counts)** | A-2 occupancy plumbing fixture ratios |
| **NFPA 17A, NFPA 96** | Hood fire suppression (UL 300 wet chemical) |
| **CFC 904.12** | Commercial cooking fire suppression |
| **Department of Public Health (CDPH) regulations** | Operator certifications, food handler cards, etc. |

If submittal documents reference any of these, the project IS a restaurant project. Hand off to `california-restaurant-ti`.

---

## 4. Handoff Procedure

When restaurant-routing triggers are detected:

1. **Note the trigger** in the review summary (one line: "Project includes [specific scope]; routing to california-restaurant-ti").
2. **STOP all further work** in this skill.
3. **Re-invoke the agent** with the restaurant skill loaded as the primary state skill.
4. Restaurant skill takes over Step 1 (classify submission type) through Step 3 (output).

**Do NOT** attempt partial review in this skill, then "add" restaurant items. The decision tree in the restaurant skill is structured around AB 671 dual-track review (Building + Health) and the two cannot be mixed cleanly with this skill's structure.

---

## 5. Adjacent Scope — Same Site, Different Permits

A common situation: a property is being repositioned to add restaurant + retail + office in adjacent tenants. The owner may file:

- One restaurant TI permit (→ `california-restaurant-ti`)
- One commercial TI permit for office (→ `california-commercial-ti`)
- One commercial TI permit for retail (→ `california-commercial-ti`)

Each permit is reviewed in isolation by the matching skill. Mixed-occupancy separations between tenants are reviewed under whichever permit the demising wall belongs to, with reference to CBC 508.4.

---

## 6. Quick Decision Flowchart

```
Project scope description received
│
├── Mentions cooking equipment / hood / grease / food prep / A-2 / restaurant?
│   ├── YES → STOP. Hand off to california-restaurant-ti.
│   └── NO  → Continue in california-commercial-ti.
│
├── Cooking-adjacent but no grease (espresso bar, juice bar, sandwich shop with no cooking)?
│   ├── Verify NO commercial cooking equipment / NO Type-I hood / NO grease interceptor.
│   ├── If verified clean → Stay in california-commercial-ti.
│   └── If any doubt → Hand off to california-restaurant-ti.
│
└── Pure commercial (office, retail, warehouse, light industrial, fitness without food)?
    └── Stay in california-commercial-ti.
```

---

## Plan Check Review Checklist — Restaurant Routing

| # | Item | Pass Criteria | Action |
|---|---|---|---|
| RR-1 | Cooking equipment present? | Equipment list reviewed for fryers / ranges / grills / ovens / charbroilers / griddles / woks | If yes → route to restaurant skill |
| RR-2 | Type-I hood in scope? | Mechanical drawings reviewed for hood schedule | If yes → route to restaurant skill |
| RR-3 | Grease-producing food prep? | Floor plan reviewed for cooking / prep zones | If yes → route to restaurant skill |
| RR-4 | A-2 occupancy declared? | Cover sheet occupancy classification | If A-2 → route to restaurant skill |
| RR-5 | Grease interceptor / grease trap in plumbing scope? | Plumbing isometric reviewed | If yes → route to restaurant skill |
| RR-6 | Walk-in cooler / freezer | Floor plan + mech drawings | If yes for food storage → route to restaurant skill |
| RR-7 | Boundary edge case (espresso / juice / sandwich w/o cooking) | All triggers verified absent | If clean → stay in commercial-ti; document in review |
