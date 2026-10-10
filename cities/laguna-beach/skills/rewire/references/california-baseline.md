# California Baseline — Rewire

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Rewire — State Regulatory Decision Engine

This skill contains California state-level whole-house rewire rules extracted from the 2025 California Electrical Code (CEC) and California Residential Code (CRC), Title 24 Parts 3 and 2.5. It covers residential rewiring — replacing existing branch circuit wiring throughout a dwelling.

**What this covers**: State electrical and residential code — the requirements that apply everywhere in California. Every city must enforce at least these standards.

**What this does NOT cover**: City-specific ordinances, local fee schedules, or project-specific engineering. Use the city-level rewire skill (e.g., `buena-park-rewire`) for those.

### How to Use This Skill

When reviewing a rewire permit or answering a rewire code question, follow the decision tree below. Each step tells you which reference files to load. Most reviews require 2 reference files.

---

### Decision Tree Router

#### STEP 1: What Type of Review Is This?

| Review Type | Load These References |
|-------------|----------------------|
| **Full permit review** (form data in → pass/fail out) | `gfci-afci-210.md`, `outlet-spacing-210.md`, `smoke-co-detectors.md` |
| **GFCI/AFCI question only** | `gfci-afci-210.md` |
| **Outlet spacing / receptacle layout** | `outlet-spacing-210.md` |
| **Smoke/CO detector question** | `smoke-co-detectors.md` |
| **Service capacity / load calc** | See `california-ev-charger` skill → `load-calc-220.md` (same 220.83(A) method) |
| **Wire sizing question** | See `california-ev-charger` skill → `wire-sizing-310.md` (same Table 310.16) |
| **General rewire code question** | `gfci-afci-210.md`, `outlet-spacing-210.md` |

#### STEP 2: Walk the Review Checklist

For a full permit review, check each item in order:

| # | Check | What to Verify | Code Section | Reference File |
|---|-------|---------------|--------------|----------------|
| 1 | **Service capacity adequate?** | If full rewire: verify panel can handle all circuits; load calc per 220.83(A) | CEC 220.83(A) | EV charger skill `load-calc-220.md` |
| 2 | **Outlet spacing correct?** | Habitable rooms: no point >6' from receptacle; kitchen countertop: no point >24" from receptacle | CEC 210.52 | `outlet-spacing-210.md` |
| 3 | **GFCI protection?** | Required in: bathrooms, kitchens, garages, outdoors, laundry, crawl spaces, basements, near sinks/tubs | CEC 210.8(A) | `gfci-afci-210.md` |
| 4 | **AFCI protection?** | Required in: kitchens, bedrooms, family/living/dining rooms, hallways, closets, laundry, rec rooms | CEC 210.12(B) | `gfci-afci-210.md` |
| 5 | **Dedicated circuits?** | Kitchen: 2× 20A small-appliance; bathroom: 20A; laundry: 20A; garage: 20A | CEC 210.11(C) | `outlet-spacing-210.md` |
| 6 | **Wire type and sizing?** | NM cable (Romex) for residential; #14 for 15A, #12 for 20A; conduit where exposed | CEC 334, Table 310.16 | EV charger skill `wire-sizing-310.md` |
| 7 | **Smoke/CO detectors?** | Rewire triggers requirement to bring smoke/CO up to current code if wall/ceiling finishes are removed | CRC R310, R311 | `smoke-co-detectors.md` |
| 8 | **Contractor licensing?** | Licensed C-10 Electrical Contractor required (CA B&P Code §7028). Owner-builder exemption per B&P §7044 only for owner-occupied residential where owner personally performs the work. Verify active CSLB license and workers' comp insurance. | CA B&P §7028, §7044 | N/A — statutory requirement |

#### STEP 3: Output the Review Result

For each checklist item, output one of:
- **PASS** — requirement met, cite code section
- **FAIL** — requirement not met, cite code section and explain what's wrong
- **FLAG** — cannot determine from submitted data, explain what additional info is needed
- **N/A** — does not apply to this installation

---

### Quick-Reference Tables

#### GFCI Required Locations — Dwelling Units (CEC 210.8(A))

| Location | GFCI Required? |
|----------|---------------|
| Bathrooms | Yes |
| Garages (at/below grade) | Yes |
| Outdoors | Yes |
| Crawl spaces (at/below grade) | Yes |
| Basements | Yes |
| Kitchens | Yes |
| Near sinks (within 6') | Yes |
| Laundry areas | Yes |
| Near bathtubs/showers (within 6') | Yes |
| Indoor damp/wet locations | Yes |

#### AFCI Required Rooms — Dwelling Units (CEC 210.12(B))

All 120V, single-phase, 10/15/20A branch circuits in:

| Room Type | AFCI Required? |
|-----------|---------------|
| Kitchens | Yes |
| Family rooms | Yes |
| Dining rooms | Yes |
| Living rooms / Parlors | Yes |
| Bedrooms | Yes |
| Libraries / Dens / Sunrooms | Yes |
| Recreation rooms | Yes |
| Closets | Yes |
| Hallways | Yes |
| Laundry areas | Yes |

> Essentially all habitable rooms in a dwelling unit require AFCI protection.

#### Dedicated Branch Circuits (CEC 210.11(C))

| Circuit | Rating | Serves |
|---------|--------|--------|
| Small-appliance (×2 minimum) | 20A | Kitchen/dining/pantry receptacles |
| Laundry | 20A | Laundry receptacle only |
| Bathroom | 20A | Bathroom receptacle(s) only |
| Garage | 20A | Garage receptacles |

#### Wire Sizing Quick Reference

| Circuit Rating | Min. Wire Size | Typical Use |
|---------------|---------------|-------------|
| 15A | #14 AWG | General lighting, bedrooms |
| 20A | #12 AWG | Kitchen, bathroom, laundry, garage |
| 30A | #10 AWG | Dryer, water heater |
| 40A | #8 AWG | Range/oven |
| 50A | #6 AWG | Range, subpanel |

---

### Key Principles

1. **Rewire triggers outlet spacing compliance**: Per the Buena Park form helpText and general code practice, if existing outlet spacing does not meet current CEC 210.52 requirements during a rewire, new outlets must be added to achieve compliance.

2. **AFCI coverage is nearly universal**: For dwelling units, AFCI protection is required for practically every habitable room (210.12(B)). The only residential locations NOT requiring AFCI are bathrooms (if on a dedicated circuit), outdoors, garages, and unfinished basements.

3. **GFCI and AFCI can overlap**: Some locations (kitchens, laundry) require both GFCI and AFCI. Dual-function AFCI/GFCI breakers satisfy both requirements.

4. **Smoke/CO upgrade depends on scope**: A rewire that removes wall or ceiling finishes triggers full smoke alarm compliance (hardwired, interconnected, all locations per R310.3). A rewire that doesn't disturb finishes has more limited requirements.

5. **Cross-reference with panel upgrade**: If the rewire increases circuit count beyond panel capacity, a panel upgrade is also needed. The load calculation uses the same CEC 220.83(A) method as the EV charger and panel upgrade skills.

6. **Aluminum wiring prohibition on branch circuits**: Aluminum conductors are not acceptable for new 15A and 20A branch circuit wiring in residential dwelling units. CEC 334.104 and Table 310.16 effectively prohibit aluminum for small branch circuits — #14 and #12 AWG aluminum are not rated for 15A/20A circuits (aluminum #12 is rated only 15A at 75C, insufficient for 20A circuits, and #14 aluminum is not manufactured in NM cable). All new residential branch circuit wiring must be copper NM cable (Romex). If existing aluminum branch wiring is discovered, it must be remediated per manufacturer-approved connectors (e.g., AlumiConn, COPALUM) or replaced with copper. Flag any proposal to install new aluminum branch circuit wiring as a FAIL.

---

### Knob-and-Tube (K&T) Wiring — Coexistence & Remediation

When a rewire permit discovers existing knob-and-tube wiring that is NOT being replaced as part of the project scope, apply the following decision tree:

#### K&T Decision Tree

| # | Check | Rule | Code Section | Action |
|---|-------|------|-------------|--------|
| K1 | **K&T in insulated spaces?** | CEC 394.12 prohibits K&T wiring where it passes through or is surrounded by thermal insulation (blown-in, batt, or loose-fill). If attic, wall, or floor cavities containing K&T have insulation present, the K&T in those spaces must be replaced or the insulation removed. | CEC 394.12 | **FAIL** if insulation contacts K&T. Determine insulation status before permit issuance. If unknown, require attic/wall inspection. |
| K2 | **AFCI protection for retained K&T?** | K&T circuits that are retained (not replaced) do not have equipment grounding conductors, so standard AFCI breakers may not function correctly. AFCI-at-panel (combination type, CEC 210.12(A)) is the recognized interim protection method for retained K&T branch circuits. | CEC 210.12(A), 210.12(E) | **FLAG** — require AFCI breaker at panel for each retained K&T circuit. Note: AFCI effectiveness on K&T is reduced but is the best available protection. |
| K3 | **GFCI remediation for ungrounded K&T outlets?** | K&T outlets lack an equipment grounding conductor. CEC 406.4(D)(2) permits GFCI protection as an alternative to grounding for replacement receptacles on ungrounded circuits. Three-prong receptacles on K&T circuits must be GFCI-protected and labeled "No Equipment Ground." | CEC 406.4(D)(2) | **FLAG** — all retained K&T receptacles must be GFCI-protected (breaker or receptacle) and labeled per 406.4(D)(2). |
| K4 | **AHJ policy on K&T retention?** | Some California jurisdictions have local policies requiring complete K&T removal when a comprehensive rewire permit is open. Others allow partial retention if K1–K3 are satisfied. AHJ policy is not codified statewide — confirm with the local building department before finalizing scope. | Local policy (varies) | **FLAG** — confirm AHJ policy on K&T retention during rewire. Document the policy determination in the permit file. |
| K5 | **Insurance advisory** | Many homeowners' insurance carriers will not insure or will surcharge dwellings with active K&T wiring. While not a code requirement, advise the applicant to confirm insurance coverage for the retained K&T configuration. | N/A (advisory) | **ADVISORY** — recommend applicant verify insurance coverage for retained K&T. |

#### K&T Quick-Reference

- **CEC 394.12**: K&T wiring shall NOT be used where conductors are in contact with thermal insulation. This is the single most common trigger for mandatory K&T replacement.
- **CEC 406.4(D)(2)**: GFCI protection is the recognized remediation for ungrounded (2-wire) circuits — applies to K&T. Label "GFCI Protected / No Equipment Ground."
- **CEC 210.12(E)**: When branch circuit wiring is modified or replaced, AFCI protection is required. For retained K&T circuits, AFCI-at-panel is the practical path.
- **Scope boundary**: If the rewire scope excludes K&T circuits, clearly delineate on plans which circuits are being replaced and which are retained. Each retained K&T circuit must be individually assessed for K1–K5.
