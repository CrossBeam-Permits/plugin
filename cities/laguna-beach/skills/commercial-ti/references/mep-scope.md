---
title: "MEP Scope & Completeness — CMC / CPC / CEC for Commercial TI"
category: "Mechanical, Plumbing, Electrical — Title 24 Parts 3, 4, 5 as they land on a TI"
relevance: "Loaded for ANY commercial TI touching HVAC, ventilation, fixtures, waste, lighting, or power. Most MEP findings on a TI are COMPLETENESS findings — the discipline package is absent, not wrong."
key_code_sections: "CMC Ch. 4; CPC fixture tables; CEC load calculations; CEBC 1009.1; Energy Code §141.0(b)2N"
---

# MEP Scope & Completeness — Commercial TI

The dominant MEP failure mode on a tenant improvement is not a bad calculation — it is a **missing discipline package**. The architectural set shows new restrooms, a new break room, and a reconfigured open office, and there are no M, P, or E sheets at all. That is one completeness finding per absent discipline, not a cascade of per-fixture corrections.

> **Discipline-absence rule.** When an ENTIRE discipline is missing, emit exactly ONE finding — "No [discipline] plans included — provide [discipline] plans for review" — carrying no code citation, and do NOT generate per-item findings against the missing discipline. This is the shared `absent-discipline.md` rule; it governs MEP-1, MEP-2, and MEP-3 below.

---

## 1. Which package is required when

| Scope trigger | Package required |
|---|---|
| HVAC equipment added, replaced, relocated; ductwork reconfigured; ventilation rates changed | Mechanical (CMC) |
| Fixtures added/relocated/removed; waste or vent lines altered; service water heating touched | Plumbing (CPC) |
| Luminaires altered; panels, feeders, or branch circuits altered; new equipment loads | Electrical (CEC) |

A TI whose scope narrative says "no MEP work" but whose floor plan shows a new restroom is an internal contradiction — reconcile it before accepting the absence.

---

## 2. Mechanical (CMC)

**Outside air / ventilation (CMC Ch. 4).** Ventilation rates are a function of occupancy and floor area. When a TI changes use or occupant density — an office becoming a fitness studio, a warehouse becoming assembly — the required outside air changes even if the air handler does not.

**Restroom exhaust (CMC Ch. 4).** Exhaust rates and duct routing shown for altered restrooms.

**Enclosed parking / garage CO ventilation.** Enclosed parking within the work area requires mechanical ventilation with CO monitoring and control.

---

## 3. Plumbing (CPC)

**Fixture count (CEBC 1009.1 + CPC fixture tables).** Where a change of occupancy raises occupant load past the CEBC 1009.1 threshold, the required fixture count is recalculated. This is the same subject as ST-14 in `structural-alterations.md` — **one finding, not two**; ST-14 owns it when the review is running the change-of-occupancy path, MEP-4 owns it otherwise.

**Service water heating (Energy Code §141.0(b)2N + CPC).** A replaced or added water heater is both a plumbing and an energy-compliance item; see EN-15 in `energy-alterations.md`.

**Grease / food-service plumbing.** A grease interceptor, floor sink, or food-prep waste line appearing in the plumbing scope is a **restaurant-TI routing signal**, not a commercial-TI check — route per OC-8.

---

## 4. Electrical (CEC)

**Load calculation.** New equipment, new lighting, and new receptacle loads must be supported by a load calculation against the existing service. A TI adding a server room or a commercial kitchen to a suite is the common case where the existing service is inadequate and nobody checked.

**Panel and feeder schedules.** Where panels, feeders, or branch circuits are altered, schedules are the evidence.

---

## Plan Check Review Checklist — MEP

Default applicability: `ALL`

| ID | Tag | Item | Pass Criteria | Code Section | Likely sheets |
|---|---|---|---|---|---|
| MEP-1 | ALL | Mechanical plan submitted when HVAC/ventilation altered | Mechanical sheets exist, or no mechanical scope. FAIL (uncited, completeness) where altered HVAC/ventilation has no mechanical package. | *(documents/completeness — CMC scope)* | M sheets |
| MEP-2 | ALL | Plumbing plan submitted when fixtures/waste altered | Plumbing sheets exist, or no plumbing scope. FAIL (uncited, completeness) where fixture/waste scope has no plumbing package. | *(documents/completeness — CPC scope)* | P sheets |
| MEP-3 | ALL | Electrical plan and panel/load schedules submitted | Electrical package exists, or no electrical scope. FAIL (uncited, completeness) where lighting/power work has no electrical package. | *(documents/completeness — CEC scope)* | E sheets |
| MEP-4 | CHANGE-OF-OCCUPANCY | Plumbing fixture count recalculated | Fixture-count math provided where load or use changes. FAIL if absent. **Same subject as ST-14 — one finding.** | CEBC 1009.1; CPC fixture tables | Plumbing, code data |
| MEP-5 | ALL | Garage / enclosed parking CO ventilation | Garage ventilation and controls shown, or N/A. FAIL where an enclosed garage scope lacks ventilation. | CMC Ch. 4 (garage exhaust) | Mechanical |
| MEP-6 | ALL | Outside air / ventilation schedule | Occupancy ventilation rates scheduled. FLAG where equipment exists but rates are absent. | CMC Ch. 4 | Mechanical |
| MEP-7 | ALL | Restroom exhaust | Exhaust rates and duct routing shown. FLAG where a restroom is altered and exhaust is unclear. | CMC Ch. 4 | Mechanical |
| MEP-8 | ALL | Electrical service / load impact | Load calculation supports the new loads. FLAG where new equipment or lighting lacks load analysis. | CEC load calculation | Electrical |
| MEP-9 | ALL | Service water heating altered | New/replaced SWH documented. FLAG where plumbing scope implies an SWH change. See EN-15. | Energy Code §141.0(b)2N; CPC | Plumbing, energy |
| MEP-10 | ALL | Grease / food plumbing boundary | Absent or demonstrably out of scope. Routing FLAG where a grease interceptor or food prep appears — route to california-restaurant-ti per OC-8. | (Routing rule) | Plumbing |
