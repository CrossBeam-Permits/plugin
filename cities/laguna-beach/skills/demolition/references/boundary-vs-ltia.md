---
title: "Skill Boundary -- california-demolition vs. california-ltia-demolition"
category: "Routing & Scope"
relevance: "Every demolition review where scope is ambiguous"
key_code_sections: "CEBC 701.2 (existing-building conformance); CEBC Chapter 6 §§602–604 (Level 1/2/3 classification); CEBC Chapters 7–9 (requirements by alteration level); CBC 3301.1 (Chapter 33 scope); CBC 3303 (demolition section)"
---

# Skill Boundary -- Demolition vs. LTIA Demolition

CrossBeam has **two** California demolition state skills:

| Skill | Scope |
|---|---|
| `california-demolition` (this skill) | **FULL-STRUCTURE demolition** -- whole-building teardown, structural elements, exterior envelope, roof system, foundation, slab |
| `california-ltia-demolition` | **INTERIOR non-structural demolition** -- LTIA (Limited Tenant Improvement Area) gut-outs of tenant spaces in malls, shopping centers, high-rises -- drywall, finishes, fixtures only |

When project scope is unambiguous, use the matching skill. When it sits on the boundary, walk through the trigger questions below and -- when still in doubt -- default to **full demolition** (this skill), because its checklist is the superset.

---

## The Five Trigger Questions

Answer **YES to any one** = use this skill (full demolition). All five answered **NO** = use LTIA.

| # | Question | YES = Full Demolition (this skill) |
|---|---|---|
| 1 | Is any **load-bearing wall, column, beam, or shear wall** being removed, relocated, or substantially modified? | YES |
| 2 | Is any portion of the **exterior building envelope** (exterior walls, roof, exterior windows that change wall opening size, exterior doors that change wall opening size) being removed? | YES |
| 3 | Is the **roof structure** (joists, rafters, trusses, sheathing -- as opposed to roofing material only) being removed? | YES |
| 4 | Is the **slab or foundation** being removed or substantially modified? | YES |
| 5 | Is the entire structure (or a complete building / accessory building on the parcel) being removed? | YES |

If all five are **NO**, the project is interior non-structural and routes to LTIA.

---

## CEBC Alteration Levels (Background)

The California Existing Building Code (Title 24, Part 10) Chapter 6 classifies
work as Level 1, Level 2 or Level 3 in §§602, 603 and 604. The substantive
requirements for those levels are in Chapters 7, 8 and 9, respectively:

- **Level 1** -- removal/replacement of equivalent materials and equipment (e.g., recovering, repainting). No reconfiguration of space.
- **Level 2** -- reconfiguration of space, addition or elimination of doors/windows, reconfiguration of partition walls (non-structural), addition or elimination of plumbing fixtures.
- **Level 3** -- Level 2 work that exceeds 50% of the aggregate building floor area.

LTIA-style interior demolition typically falls under Level 1 (finish removal) or Level 2 (non-structural partition reconfiguration). Anything that triggers Level 3 -- or any work touching structural elements regardless of level -- belongs to full demolition.

---

## Project-Type Examples

### Always FULL DEMOLITION (this skill)

- Whole single-family home teardown to slab (or below slab)
- Whole single-family home teardown with slab/foundation removal
- Detached garage demolition to slab
- Commercial shell demolition
- Multi-tenant strip-center demolition
- Apartment building demolition
- ADU teardown / replacement (where existing ADU is being removed)
- Removal of any load-bearing wall (even if exterior envelope remains)
- Roof structure removal (e.g., for vertical addition where existing roof is demolished)
- Foundation removal / replacement
- Carport or detached structure demolition where any structural framing is removed

### Always LTIA (other skill)

- Tenant gut-out in a mall: drywall, ceilings, floors, fixtures only, no structural
- Office demolition for new tenant: partitions, ceilings, finishes, no structural
- Restaurant interior strip-out before new TI build-out
- Removal of non-load-bearing partition walls within an existing residence (no structure touched)
- Kitchen / bathroom demolition where only fixtures and non-bearing walls are removed (typically handled under a remodel permit, with demo as a phase)

### Ambiguous -- Walk Through the Trigger Questions

| Project | Resolution |
|---|---|
| "We're demolishing the interior of a residence in preparation for a major remodel that will keep two exterior walls" | LTIA if truly no structural / envelope touched; FULL if any wall removed. Almost always FULL because at least one structural element is touched in a major remodel. |
| "We're removing the carport but leaving the house" | FULL (the carport is a complete structure, Trigger #5). |
| "We're removing one bearing wall to open up the kitchen" | FULL (Trigger #1). |
| "We're stripping a commercial shell to studs, then re-skinning" | FULL (Trigger #2 -- envelope is being removed). |
| "We're demolishing only the roof to add a second story" | FULL (Trigger #3). |
| "We're replacing the foundation under an existing house" | FULL (Trigger #4). |
| "We're doing a 'soft demo' -- finishes only, no structure" | LTIA. |
| "We're removing all the non-bearing partitions in a tenant space" | LTIA. |

---

## Edge Case -- "Selective Demolition" / "Demo Phase of Remodel"

Many California cities issue a single combined permit (often labeled "Demolition / Remodel" or "Selective Demolition") that covers both the demo phase and the new construction. For CrossBeam review purposes:

- If the demo phase touches any of the five triggers above -- run THIS skill's checklist for the demo portion, then run the appropriate construction skill (residential-addition, single-family-residential, restaurant-ti, etc.) for the construction portion.
- If the demo phase is interior non-structural only -- run LTIA's checklist for the demo portion.

---

## When in Doubt -- Default to Full Demolition

This skill's checklist is the superset. Running the full-demolition checklist on a project that turns out to be LTIA produces a few extra FLAGs (asbestos survey for an interior gut-out is a real requirement anyway; utility-disconnect items will be N/A). Running the LTIA checklist on a project that turns out to be full demolition **misses critical items** (pedestrian protection, site safety plan, adjacent-property notice, utility disconnects, AQMD survey at building-shell level, lead-paint workflow).

**One-line rule:** Err on the side of this skill.

---

## Citation Hand-off

When routing a borderline project to LTIA, document the decision:

> Project scoped as interior non-structural per the five-trigger test (CEBC 701.2 boundary; no load-bearing, envelope, roof structure, slab/foundation, or whole-structure removal). Routed to `california-ltia-demolition`.

When routing a borderline project to this skill from LTIA:

> Project scoped as full-structure demolition per Trigger #[N] -- [load-bearing wall / envelope / roof / foundation / whole structure] is being removed. CEBC 701.2 conformance and CBC Chapter 33 safeguards apply. Routed to `california-demolition`.
