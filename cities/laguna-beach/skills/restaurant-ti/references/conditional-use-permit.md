# Laguna Beach — Conditional Use Permit for Restaurant TI

**Operative code:** zone use lists (25.18.004, 25.19.006, 25.20.006, 25.21.004, 25.25.006, Ch. 25.40); LBMC Sec. 25.05.030 (CUP procedure; decisions effective 14 calendar days after decision unless appealed, 25.05.030(I)(1) as amended by Ord. 1732); Ch. 25.52 (parking-relief CUPs).

---

## When CUP Is Required

The trigger is the **zone chapter's use list**, not Sec. 25.05.030 (which sets the CUP procedure and findings). Read the parcel's zone from site facts and quote the list. Corpus: the City source document (not included in this plugin) (codified through 2026-04-28).

| Zone | Restaurant without alcohol | CUP uses | Source |
|------|----------------------------|----------|--------|
| Local Business Professional (LBP) | CUP | Cafes, full-service and take-out restaurants, tea rooms; establishments serving alcohol (drive-in not permitted) | 25.18.004 |
| Commercial Neighborhood (C-N) | Permitted (full-service, with or without outdoor seating) | Restaurants serving alcohol; take-out restaurants (drive-in not permitted) | 25.19.002, 25.19.006 |
| Local Business (C-1) | Permitted (full-service, no alcohol, no dancing or entertainment; outdoor tables allowed with an indoor restaurant) | Restaurants serving alcohol and/or with entertainment; take-out; drive-in; on-sale alcohol establishments | 25.20.004, 25.20.006 |
| South Laguna Village (SLV) | Listed only as a CUP use | Cafe/restaurant, outdoor seating, alcohol and/or entertainment "only as authorized under the conditional use permit" | 25.25.006 |
| Commercial Hotel-Motel (CH-M) | Only incidental to a hotel | Cafes, restaurants, lounges with a primary hotel use | 25.21.004 |
| Downtown Specific Plan | See below | Ch. 25.40 use tables; full-service restaurants need special findings | Ch. 25.40 |

**Parking relief by CUP (Ch. 25.52):** joint use of spaces, shared parking, valet parking, off-site spaces for an intensification, and the 25.52.006(G) incentive reduction each need a CUP. Ord. 1732 § 46 (signed text p. 72) changed the 25.52.006(G) decision-maker from the City Council to the **Planning Commission** and deleted "upon recommendation by the approval authority".

**Not CUP triggers in our sources:** an intensification of use by itself (it triggers a CDP under 25.07.006 / 25.07.008(A)(2)(b) and the parking requirement under 25.52.004, not a CUP), and late hours (hours are set by CUP conditions where a CUP exists). If a source says otherwise, **confirm with Planning at pre-application**.

**Downtown Specific Plan carve-out.** The 2022 CCC-certified DSP update (Ch. 25.40) streamlined most downtown uses to by-right to lower barriers for retail/office uses. But the DSP **explicitly continues to require CUPs for bars, restaurants, and other "more intense uses."** Do not assume a downtown restaurant is by-right because the DSP simplified other categories.

---

## Process

| Item | Detail |
|------|--------|
| Hearing body | Planning Commission |
| Notice | 21 calendar days (Sec. 25.05.065) |
| Hearing | Per PC calendar |
| Appeal | To City Council within 14 calendar days (Sec. 25.05.070) |
| Concurrent processing | CUP processed alongside CDP, Design Review by same body when possible |
| Timeline | 12-20 weeks from complete application to PC action (longer if appeals) |

---

## Conditions of Approval (Sec. 25.05.030(G))

Planning Commission has wide discretion to attach conditions. Common restaurant-specific conditions:

| Condition type | Examples |
|----------------|----------|
| Hours of operation | Open/close times, last-call, kitchen-close |
| Noise | Receiver-side dBA limits, no amplified music after a fixed hour, indoor-only entertainment |
| Vibration | Equipment isolation requirements for bass speakers, RTUs |
| Odor | Hood exhaust filtration, charcoal pre-filters, grease-duct cleaning schedule |
| Signs | Illumination cutoff hours, color, character |
| Outdoor seating | Capacity cap, hours, heating equipment limits |
| Trash | Pickup hours (no early-morning trucks), enclosure standards |
| Alcohol | License type (Type 41 vs 47), no full bar after a fixed hour, no shots-only service |
| Security | Door staff at certain capacities, security plan, lighting |
| Parking | Valet plan, employee off-site parking, in-lieu fee |
| Duration & review | Initial 1-year operational review; CUP can be revoked or modified on complaint per Sec. 25.05.030(G) |

The "review on complaint" condition is standard and gives the city teeth to revisit the CUP if neighborhood issues arise.

---

## What CUP Does NOT Replace

A CUP is a use entitlement. It does NOT substitute for:

- **Coastal Development Permit** (Ch. 25.07) — needed independently for intensification of use
- **Planning route** (Sec. 25.05.040) — match current closed lists; exterior change alone is not a residual Design Review trigger
- **Building Permit** (Title 14) — needed for any construction work
- **OCHCA Plan Approval** — needed for any food facility
- **LBFD Plan Approval** — needed for any commercial cooking / sprinkler / alarm work
- **ABC License** — state alcohol license is separate, though Planning Commission action is often a condition precedent

---

## Documentation the Plan Set / Application Must Show

| Item | Required on |
|------|-------------|
| CUP application number | Title sheet |
| Use description | Cover sheet / project narrative |
| Hours of operation proposed | Cover sheet |
| Alcohol type / entertainment description if applicable | Project narrative |
| Capacity (occupant load, seat count) | Code summary, floor plan |
| Parking calculation showing prior-use vs proposed-use demand | Site plan |
| Compliance with all conditions of approval | Title sheet, after CUP issuance |

---

## Output Findings

- **PASS** — No CUP trigger present OR CUP issued and conditions reflected in plans.
- **FAIL** — The zone list makes the use a CUP use (e.g. alcohol, entertainment, take-out, drive-in, or any restaurant in LBP/SLV), or parking relief relies on a 25.52 CUP, and no CUP is on file.
- **FLAG** — Operational details (hours, alcohol type, entertainment) not specified in submittal; cannot determine CUP status.
- **N/A** — Confirmed non-alcohol, daytime-only, no entertainment, no drive-thru, no intensification (rare for new restaurants).
