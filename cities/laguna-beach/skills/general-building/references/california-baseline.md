# California Baseline — Minor Building Work

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Minor Building Work — State Counter Check

This skill covers the minor residential work a city issues over the counter, where there is no
plan set to walk and no dedicated permit-type skill. It is the honest floor for the permits that
have no name: a 20 square foot drywall patch, two skylights, a 117 square foot shed, a walkway,
a stucco patch, a tub swapped in place, a sprinkler retrofit, a framing repair described in an
engineer's letter.

**What this covers**
- Whether the work actually needs a permit at all (CRC R105.2, CBC 105.2).
- The administrative check a counter tech runs: scope, valuation, licence, workers' comp,
  owner-builder, code cycle.
- The code sections that still apply to small alterations and repairs, by scope family.
- The escalation test: the words that mean this is not minor work.

**What this does NOT cover**
- Any permit type with its own skill. Route a roof covering to `california-reroof`, a window or
  door in an existing opening to `california-window-replacement`, a wall re-clad to
  `california-siding-replacement`, a kitchen or bath to `california-kitchen-bath-remodel`, a
  fence or freestanding wall to `california-fence` or `california-block-wall`, a soil-retaining
  wall to `california-retaining-wall`, a deck repair to `california-deck-patio-repair`, a
  cleanout to `california-cleanout`.
- Plan-check work of any size. If the submittal carries a drawing set a plan checker must walk,
  this is the wrong skill.
- City requirements. The city delta skill (for example `laguna-beach-general-building`) carries
  local exemption thresholds, sprinkler retrofit triggers, fire-zone rules, and coastal rules.

---

### How to Use This Skill

1. Run STEP 1. If any escalation trigger fires, stop and say the work needs a real review.
2. Run STEP 2 to name the scope family and load the one reference it points to.
3. Walk the STEP 3 checklist. Every item is a counter check; none of them needs a drawing.
4. Report each item PASS / FAIL / FLAG / N/A with the code section.

---

### Decision Tree Router

#### STEP 1 — Is this actually minor work?

Read the scope as the applicant wrote it, plus any photo, letter, or one-sheet sketch. Decide
from the words, not from the page count. Load `escalation-triggers.md` for the full list and the
judgment calls.

| The scope says | Verdict |
|---|---|
| Adds floor area, a story, or habitable space | NOT minor — plan review |
| Alters, removes, or underpins a bearing wall, beam, post, or footing | NOT minor — plan review |
| Cuts a new opening or enlarges an existing one in any wall | NOT minor — plan review |
| Moves earth, cuts, fills, or builds a wall that holds soil | NOT minor — grading or retaining-wall review |
| Changes occupancy, use, or the required means of egress | NOT minor — plan review |
| Repairs damage from fire, vehicle impact, water, or settlement beyond finish materials | NOT minor unless an engineer's letter defines the repair (see `minor-scope-families.md`) |
| Replaces finishes, fixtures, or small components in place, with no structural change | Minor — continue |

An application that carries a full drawing set is not minor work whatever the scope line says.

#### STEP 2 — Which scope family?

| The work is | Load |
|---|---|
| Interior finish: drywall patch, plaster, tile, paint, trim, cabinets in place | `minor-scope-families.md` |
| Exterior patch: a limited area of stucco or siding, not a wall or elevation | `minor-scope-families.md` |
| A skylight set in an existing roof opening | `minor-scope-families.md` |
| A shed or other small one-story detached accessory structure | `minor-scope-families.md` |
| Hardscape at grade: slab, walkway, patio paving, planters that retain no soil | `minor-scope-families.md` |
| A plumbing fixture replaced in place | `minor-scope-families.md` |
| A residential fire-sprinkler retrofit | `minor-scope-families.md` |
| A repair defined by an engineer's or architect's letter | `minor-scope-families.md` |
| Any question about whether a permit is required at all | `permit-thresholds-exemptions.md` |
| Any licence, valuation, workers' comp, or owner-builder question | `counter-administrative-check.md` |

#### STEP 3 — Walk the counter checklist

| # | Check | What to verify | Code section | Reference |
|---|---|---|---|---|
| 1 | **Scope is minor** | The described work fits a STEP 2 family and trips no STEP 1 trigger. Scope drives everything downstream, so a misread here is a FAIL, not a flag. | CRC R105.2, R105.2.2 | `escalation-triggers.md` |
| 2 | **Permit is actually required** | Work below the exemption thresholds needs no permit; say so rather than reviewing it. City thresholds are commonly lower than the state's. | CRC R105.2; CBC 105.2 | `permit-thresholds-exemptions.md` |
| 3 | **Scope is described, not just labelled** | Location, quantity, and materials are on the application. "Repair as needed" is not a scope. | City intake practice | `counter-administrative-check.md` |
| 4 | **Valuation is stated and plausible** | A dollar value is on the form and matches the described quantity. Valuation sets the fee and, in many cities, a cumulative sprinkler or upgrade trigger. | City fee schedule; city cumulative-valuation triggers | `counter-administrative-check.md` |
| 5 | **Contractor licence** | An active CSLB licence in a classification that covers the work, or a valid owner-builder declaration on an owner-occupied dwelling where the owner performs the work. | B&P §7028, §7044 | `counter-administrative-check.md` |
| 6 | **Workers' compensation** | A certificate on file, or the signed exemption declaration on the application. | CSLB licensing requirement | `counter-administrative-check.md` |
| 7 | **Code cycle** | Review against the edition in force for the application's received date, not today's edition. | CBSC cycle table | `counter-administrative-check.md` |
| 8 | **Family requirements** | The one or two state rules that still reach this scope (energy, safety glazing, water-conserving fixtures, sprinkler standard, hazmat). | see family | `minor-scope-families.md` |
| 9 | **Hazardous materials** | Pre-1978 paint disturbance (EPA RRP) or pre-1981 asbestos-suspect material: certification and work practices. FLAG for documentation; this is an EPA/Cal-OSHA overlay, not a building-department pass/fail. | 40 CFR 745; Cal/OSHA Title 8 §§1529, 1532.1 | `counter-administrative-check.md` |
| 10 | **City overlay** | Fire hazard zone, coastal zone, historic status, and local exemption amendments reach even minor work. Always invoke the city skill. | city code | city delta skill |

#### STEP 4 — Output

For each item: **PASS** (met, cite the section), **FAIL** (not met, cite the section and say
what is wrong), **FLAG** (cannot tell from what was submitted, say exactly what is missing), or
**N/A** (does not apply, say why).

When STEP 1 escalates, the output is one finding: this work is not minor, name the trigger and
the words in the scope that fired it, and say what review it needs instead.

---

### Quick Reference

#### The state permit-exemption thresholds most often reached here

| Work | Permit required? | Section |
|---|---|---|
| One-story detached accessory structure used as a tool or storage shed, floor area at or below 120 sq ft | No | CBC 105.2 |
| Fence not over 7 ft high | No | CRC R105.2 |
| Retaining wall not over 4 ft, footing to top, no surcharge | No | CRC R105.2 |
| Deck at or below 200 sq ft, not more than 30 in above grade, not attached, not serving a required exit door | No | CRC R105.2 |
| Any repair that cuts structural members, removes load-bearing supports, or changes means of egress | Yes | CRC R105.2.2 |

Cities amend these thresholds downward and the local number governs. Never clear a project on
the state threshold without checking the city delta.

#### What this skill never does

- It never approves work it cannot see. A scope line that hides a structural change is a FAIL on
  item 1, not a PASS on the rest.
- It never substitutes a nearest-neighbour permit type. If a named type fits, use that type's
  skill instead of this one.
- It never invents a code citation. When no state rule reaches a minor scope, say so.
