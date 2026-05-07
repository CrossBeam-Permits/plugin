---
title: "CEC Sections 210.8 and 210.12 — GFCI and AFCI Protection"
category: "Circuit Protection"
relevance: "Every rewire review"
key_code_sections: "CEC 210.8(A), 210.12(A)-(E)"
---

# CEC Sections 210.8 and 210.12 — GFCI and AFCI Protection

Source: 2025 California Electrical Code (Title 24, Part 3), Article 210.

---

## GFCI Protection — Section 210.8

A listed Class A GFCI shall provide protection. The GFCI must be installed in a **readily accessible location**.

### Dwelling Unit GFCI Locations — 210.8(A)

All 125V through 250V receptacles supplied by single-phase branch circuits rated 150V or less to ground in the following locations require GFCI protection:

| # | Location | Notes |
|---|----------|-------|
| 1 | **Bathrooms** | All receptacles |
| 2 | **Garages** | Including accessory buildings at/below grade, limited to storage/work areas |
| 3 | **Outdoors** | All outdoor receptacles |
| 4 | **Crawl spaces** | At or below grade level |
| 5 | **Basements** | All receptacles |
| 6 | **Kitchens** | All receptacles |
| 7 | **Food/beverage prep areas** | Areas with sinks and permanent provisions for food prep, beverage prep, or cooking |
| 8 | **Near sinks** | Within 6 feet (1.8m) from top inside edge of bowl |
| 9 | **Boathouses** | All receptacles |
| 10 | **Near bathtubs/showers** | Within 6 feet (1.8m) of outside edge |
| 11 | **Laundry areas** | All receptacles |
| 12 | **Indoor damp/wet locations** | All receptacles |

**Distance measurement**: Measured as the shortest path the power supply cord would follow without piercing a floor, wall, ceiling, or fixed barrier.

### GFCI Exceptions (210.8(A))

1. Receptacles not readily accessible, dedicated to snow-melting/deicing/pipeline heating
2. Receptacle supplying only a permanently installed premises security system
3. Listed weight-supporting ceiling receptacles for luminaires/fans (unless convenience receptacle is integral)
4. Factory-installed receptacles internally mounted to bathroom exhaust fan assemblies

### Additional GFCI Requirements

**Specific appliances — 210.8(D)**: GFCI required for branch circuit or outlet supplying (rated 150V or less, 60A or less):
- Dishwashers
- Electric ranges
- Wall-mounted ovens
- Counter-mounted cooking units
- Clothes dryers
- Microwave ovens
- Sump pumps

**Outdoor outlets — 210.8(F)**: For dwellings, all outdoor outlets (not just receptacles) including in garages at/below grade, accessory buildings, and boathouses.

> Exception: GFCI not required for listed HVAC equipment (expires September 1, 2026).

---

## AFCI Protection — Section 210.12

Arc-fault circuit-interrupter protection prevents fires caused by arcing faults in branch circuit wiring.

### Means of Protection — 210.12(A)

AFCI protection can be provided by:
1. **Listed combination-type AFCI** protecting entire branch circuit (most common)
2. Listed branch/feeder-type AFCI at origin + outlet branch-circuit-type at first outlet
3. Listed supplemental arc protection breaker at origin + outlet AFCI at first outlet (with conditions)
4. Listed outlet branch-circuit-type AFCI at first outlet + listed overcurrent device (with conditions)
5. Metal raceway/MC/AC cable with outlet AFCI at first outlet
6. Conduit encased in 2" concrete with outlet AFCI at first outlet

### Dwelling Unit AFCI Locations — 210.12(B)

All **120V, single-phase, 10-, 15-, and 20-ampere** branch circuits supplying outlets or devices in the following locations require AFCI:

| # | Room Type |
|---|-----------|
| 1 | Kitchens |
| 2 | Family rooms |
| 3 | Dining rooms |
| 4 | Living rooms |
| 5 | Parlors |
| 6 | Libraries |
| 7 | Dens |
| 8 | Bedrooms |
| 9 | Sunrooms |
| 10 | Recreation rooms |
| 11 | Closets |
| 12 | Hallways |
| 13 | Laundry areas |
| 14 | Similar areas |

> This is essentially **every habitable room** in a dwelling unit.

### AFCI Exceptions (210.12(B))

1. Individual branch circuit supplying a fire alarm system (installed in metal raceway/MC/AC cable)
2. Individual branch circuit supplying arc welding equipment (exception expired January 1, 2025)

### Wiring Modifications, Replacements, or Extensions — 210.12(E)

**This is the key section for rewire permits**: If branch-circuit wiring for any AFCI-required area is **modified, replaced, or extended**, the branch circuit must be AFCI-protected by:
1. Any of the means in 210.12(A)(1)-(6), OR
2. A listed outlet branch-circuit-type AFCI at the first receptacle outlet of the existing branch circuit

**Exception**: AFCI not required if the extension is ≤6 feet and doesn't include additional outlets/devices (not counting conductors inside enclosures).

> **For rewire**: Since a whole-house rewire replaces all branch-circuit wiring, **210.12(E) applies to every circuit in every AFCI-required location**. All circuits must have AFCI protection.

---

## GFCI + AFCI Overlap

Some locations require both GFCI and AFCI protection:

| Location | GFCI Required? | AFCI Required? | Solution |
|----------|---------------|----------------|----------|
| **Kitchens** | Yes (210.8(A)(6)) | Yes (210.12(B)(1)) | Dual-function AFCI/GFCI breaker |
| **Laundry areas** | Yes (210.8(A)(11)) | Yes (210.12(B)(13)) | Dual-function AFCI/GFCI breaker |
| **Bathrooms** | Yes (210.8(A)(1)) | No (not listed in 210.12(B)) | GFCI breaker or receptacle |
| **Bedrooms** | No | Yes (210.12(B)(8)) | AFCI breaker |
| **Living rooms** | No | Yes (210.12(B)(4)) | AFCI breaker |
| **Garages** | Yes (210.8(A)(2)) | No | GFCI breaker or receptacle |
| **Outdoors** | Yes (210.8(A)(3)) | No | GFCI breaker or receptacle |
| **Basements** | Yes (210.8(A)(5)) | No (unless finished/habitable) | GFCI breaker or receptacle |

**Dual-function breakers**: A single listed dual-function AFCI/GFCI breaker satisfies both requirements. This is the simplest solution for kitchens and laundry areas.
