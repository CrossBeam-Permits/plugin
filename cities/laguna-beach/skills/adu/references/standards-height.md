---
title: "Height Limits by ADU Type"
category: standards
relevance: "Load when height limits or number of stories are relevant to the ADU proposal. Distinguishes detached vs. attached limits and transit/multistory bonuses."
key_code_sections: "Gov. Code §§ 66321(b)(4), 66314(d)(8)"
---

## Height Limits by ADU Type

### Does State Law Set a Height Limit?

State ADU Law does not contain a height limit itself, but it sets **minimum heights that local agencies must allow**. A local agency may impose height limits by adopting a compliant ADU ordinance, but may not go below the state-mandated minimums. (Gov. Code, § 66321, subd. (b)(4).)

### Detached ADU Height Limits

A local agency may not impose a height limit less than:

| Scenario | Minimum Height | Code Section |
|---|---|---|
| **Base** — lot with proposed or existing SF or MF dwelling | **16 feet** | § 66321(b)(4)(A) |
| **Near transit** — within half-mile of major transit stop or high-quality transit corridor | **18 feet** (includes +2 ft for roof pitch matching primary dwelling) | § 66321(b)(4)(B) |
| **Multistory primary** — lot with existing or proposed multifamily, multistory dwelling | **18 feet** | § 66321(b)(4)(C) |

### Attached ADU Height Limits

**25 feet** or the height limitation that applies to the primary dwelling in the local zoning ordinance, **whichever is lower**. (Gov. Code, § 66321, subd. (b)(4)(D).)

### Number of Stories

There is **no limit on the number of stories** in State ADU Law. A local agency must allow at least **two stories**. An attached ADU may be built to the height of the zoning for the primary dwelling or up to 25 feet, whichever is lower. (Gov. Code, § 66321, subd. (b)(4)(D).)

If a detached two-story ADU can be built within the allowed height while remaining compliant with building code, a local agency **cannot deny the application** — even if underlying zoning restricts the primary dwelling to one story. (Gov. Code, §§ 66321, subd. (b)(4)(D); 66314, subd. (d)(8).)

### 66323 Unit Height Limits

For 66323 Units (state-mandated ADUs under § 66323(a)(2) and (a)(4)), the same height limits apply: **16, 18, or 20 feet** for detached units depending on the conditions above. No additional local height standards may be imposed beyond what § 66323 specifically authorizes. (Gov. Code, § 66323, subds. (a), (b).)

### Determining Transit Proximity

When the parcel facts is available, use the parcel-resolved `transit` block:

- If `state_entitlements.adu.height_floor_ft` is **18**, assert the 18-foot detached ADU state height floor and cite the resolved `transit.nearest.distance_ft` / `hqta_type`.
- If `transit.within_half_mile_major_stop` or `transit.within_half_mile_hq_corridor` is true, assert the § 66321(b)(4)(B) transit height unlock from that site fact.
- Do **not** ask the applicant to measure, use Google Maps, or check an MPO when the resolver supplied `transit`. The v1 method is a radial proxy for the ADU walking-distance test; if the distance is close to 0.5 mile, note that the local agency may confirm walking distance.

If no `transit` site fact is available, treat transit proximity as unresolved rather than assuming a citywide yes/no answer. (Gov. Code, § 66321, subd. (b)(4)(B).)

### Cross-References
- See also: `unit-types-66323.md` — 66323 categories and which height limits apply
- See also: `unit-types-adu-general.md` — Attached vs. detached ADU definitions
- See also: `standards-setbacks.md` — Setback rules that interact with height
- See also: `standards-design.md` — Objective standards including height as an example

### Key Code Sections
- Gov. Code § 66321, subd. (b)(4)(A) — 16-foot base height for detached ADUs
- Gov. Code § 66321, subd. (b)(4)(B) — 18-foot height near transit (includes +2 ft roof pitch)
- Gov. Code § 66321, subd. (b)(4)(C) — 18-foot height on multistory multifamily lots
- Gov. Code § 66321, subd. (b)(4)(D) — 25-foot attached ADU limit; two-story minimum; two-story override
- Gov. Code § 66314, subd. (d)(8) — Cannot deny two-story ADU if within height allowance
