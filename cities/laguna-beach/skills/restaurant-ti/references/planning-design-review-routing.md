# Laguna Beach — Current Restaurant TI Planning Route

**Law as of:** 2026-07-22

**Authority:** LBMC §§25.05.040 and 25.05.045 as replaced/added by Urgency Ordinance No. 1732

## Closed-list rule

Exterior work is no longer a categorical Design Review trigger. Match every component to Ord. 1732's closed lists and screen CDP/CUP separately.

| Common restaurant scope | Current route |
|---|---|
| Interior modification with no exterior modification | Zone Clearance, §25.05.040(B)(2)(d) |
| Other non-major alteration/addition and improvement no more than 15 ft | Ordinarily Zone Clearance, (B)(2)(a)-(b), absent another trigger |
| New building | Design Review, (B)(1)(b) |
| Improvement over 15 ft | Design Review, (B)(1)(c) |
| Commercial parking/loading area | Design Review, (B)(1)(l) |
| New/widened vehicular access described by the ordinance | Design Review, (B)(1)(k) |
| Trash storage/enclosure | Design Review, (B)(1)(n), except qualifying screened side-yard Zone Clearance `(B)(2)(q)` or front-yard ADR `(B)(3)(a)(xv)` |
| Mechanical equipment passing §7.25.130(C) | Zone Clearance, (B)(2)(v) |
| Mechanical equipment failing §7.25.130(C) | Administrative Design Review, (B)(3)(a)(v) |

Storefronts, awnings, exterior paint, lights, visible furniture, hood terminations, and signs are not named categorical triggers in the replacement lists. Classify their actual physical improvement, height, location, and combined project scope. If no category matches, return `needs_source` instead of reviving the former exterior-work default.

Chapter 25.54 retains a broken cross-reference to former `(B)(1)(d)` for signs; current `(B)(1)(d)` governs historic resources. Apply Chapter 25.54's independent sign standards, but obtain Planning's route when no current §25.05.040 category independently applies.

## Authority, ESA, and timing

- When Design Review is triggered for a non-residential project, the Planning Commission is the hearing authority under §25.05.040(F).
- Zone Clearance is issued by the Community Development Department.
- ADR is decided by the Director/designee; except for elevated decks and minor historic work, its hearing may be waived only through the 15-working-day notice/comment procedure when no other entitlement is required.
- ESA development routes to Design Review absent the enacted peer-reviewed professional determination.
- Design Review/ADR mailed hearing notice is at least 21/14 calendar days, respectively; applicable staking uses the same respective minimums. Hearing posting under §25.05.065(E) is at least 10 calendar days.
- Appeals are filed within 14 calendar days.

## Current criteria

When Design Review applies, use the 11 current §25.05.040(H) criteria: Access; Design Articulation; Environmental Context; General Plan Compliance; Historic Preservation; Landscaping; Lighting and Glare; Neighborhood Compatibility; Pedestrian Orientation; Privacy; and View Equity.

## Output

Return `Design Review`, `Zone Clearance`, `Administrative Design Review`, or `needs_source`, with the exact current category, ESA analysis, hearing/waiver status, and separate CDP/CUP results.
