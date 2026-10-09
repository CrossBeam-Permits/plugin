---
title: "Egress & Means of Egress — CBC Chapter 10 for Commercial TI"
category: "Egress — CBC Chapter 10; CEBC 1011.4-1011.7 for change of occupancy"
relevance: "Loaded for ANY commercial TI that reconfigures walls, doors, corridors, or occupant load. A TI that moves a single demising wall can change exit count, common path, and dead-end geometry."
key_code_sections: "CBC 1004.9, 1006, 1007, 1008, 1010, 1013, 1017, 1020.5; CEBC 1011.4-1011.7"
---

# Egress & Means of Egress — Commercial TI

Egress is the check a tenant improvement most often breaks without anyone noticing: the scope reads as "new partitions and finishes," but moving partitions changes exit access travel distance, common path of egress travel, dead-end corridor length, and sometimes the required number of exits. None of those are visible on a finish schedule.

Two framings drive the review:

1. **CBC Chapter 10 governs the geometry** — how many exits, how far apart, how far to reach one, how wide the door, what hardware.
2. **CEBC 1011.4-1011.7 governs what a CHANGE OF OCCUPANCY does to that geometry** — a use moving to a higher hazard category can require egress that complied perfectly under the prior use to be brought up.

---

## 1. Exit count and arrangement

**Number of exits (CBC 1006).** Required exits are determined per space and per story from occupant load, not per tenant suite. A TI that raises occupant load past a threshold can require a second exit that the existing suite does not have — this is the single most expensive egress finding to discover late.

**Exit separation / remoteness (CBC 1007).** Where two or more exits are required, they must be placed a minimum distance apart (measured as a fraction of the diagonal, halved where the building is fully sprinklered). Two doors at the same end of a suite do not satisfy this even if the count is right.

**Common path of egress travel (CBC 1006.2.1).** The distance an occupant must travel before reaching a point where two separate paths become available. Limits vary by occupancy and sprinkler status. On open-plan office TIs this is the check most often undimensioned.

**Exit access travel distance (CBC 1017).** Total distance to an exit. Sprinklered buildings get longer allowances.

**Dead-end corridors (CBC 1020.5).** Corridor length past the last exit access point. A new corridor stub created by a demising wall is the usual cause.

---

## 2. Doors and hardware

**Egress doors (CBC 1010).** Width, swing direction, maneuvering clearance, landing, and operating force. Doors serving an occupant load at or above the code threshold must swing in the direction of egress travel.

**Panic and fire exit hardware (CBC 1010.2.9).** Required on doors serving qualifying occupancies and occupant loads (notably Group A and E above the threshold, and rooms containing certain electrical equipment). The door schedule is where this is proven or missed.

---

## 3. Lighting and marking

**Exit signs and means-of-egress illumination (CBC 1008, 1013).** Required continuously along the means of egress, including emergency power.

> **Scope overlap — read this.** The same requirement appears as **FL-12** in `fire-life-safety.md`, because plan checkers conventionally review egress illumination under the fire/life-safety umbrella. **They are ONE check. Emit ONE finding.** Whichever discipline agent reaches it first owns it; the other marks it covered.

---

## 4. Assembly-specific

**Occupant-load posting and assembly thresholds (CBC 1004.9, 1006).** Assembly, classroom, and dining spaces at or above the posting threshold carry a posting requirement plus the egress and hardware consequences of the assembly load.

---

## 5. Change of occupancy (CEBC 1011.4-1011.7)

Where the use changes, the egress evaluation runs against the **hazard category direction** — the same higher/equal/lower determination that drives ST-6 in `structural-alterations.md`. A move to a higher hazard category triggers the Chapter 10 provisions for the new use within the work area; an equal or lower move can leave existing egress in place. Plans must state the direction, not just the new use.

---

## Plan Check Review Checklist — Egress

Default applicability: `ALL`

| ID | Tag | Item | Pass Criteria | Code Section | Likely sheets |
|---|---|---|---|---|---|
| EG-1 | ALL | Exit count by occupant load and common path | Exit count calculated per space and per story. FAIL where a required second exit is omitted. | CBC 1006 | Code data, floor |
| EG-2 | ALL | Exit access travel distance | Distances shown and within limits for the occupancy and sprinkler status. FLAG if not dimensioned but likely compliant. | CBC 1017 | Life safety plan |
| EG-3 | ALL | Common path of egress travel | Common path dimensioned. FLAG if not shown. | CBC 1006.2.1 | Life safety plan |
| EG-4 | ALL | Dead-end corridor limits | Dead ends dimensioned or demonstrably absent. FLAG if corridor geometry is unclear. | CBC 1020.5 | Floor |
| EG-5 | ALL | Exit separation / remoteness | Two exits remotely located where required. FAIL where separation is visibly insufficient. | CBC 1007 | Life safety plan |
| EG-6 | ALL | Door swing, width, and maneuvering at egress doors | Schedule and plan show compliant egress doors. FLAG if the door schedule is incomplete. | CBC 1010 | Door schedule, floor |
| EG-7 | ALL | Panic / fire exit hardware | Required hardware shown for qualifying rooms and loads. FLAG if the occupant-load threshold is unclear. | CBC 1010.2.9 | Door schedule |
| EG-8 | ALL | Exit signs and egress illumination | Shown throughout the means of egress. FAIL if missing where required. **Same check as FL-12 in `fire-life-safety.md` — one finding, not two.** | CBC 1008, 1013 | Electrical, life safety |
| EG-9 | ASSEMBLY-50+ | Assembly occupant-load thresholds | Posting, exits, and hardware consequences of the assembly load considered. FAIL if omitted. | CBC 1004.9, 1006 | Code data |
| EG-10 | CHANGE-OF-OCCUPANCY | Egress changes under CEBC | Hazard direction and the egress compliance path shown. FLAG if the CEBC path is absent. | CEBC 1011.4-1011.7 | Code data |
