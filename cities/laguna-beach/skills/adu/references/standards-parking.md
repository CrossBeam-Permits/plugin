---
title: "Parking Requirements and Exemptions"
category: standards
relevance: "Load when parking requirements, exemptions, or replacement parking are relevant to the ADU proposal."
key_code_sections: "Gov. Code §§ 66314(d)(10), 66314(d)(11), 66322(a), 66334(a)"
---

## Parking Requirements and Exemptions

### Maximum Parking for ADUs

Parking requirements for ADUs **shall not exceed one parking space per unit or per bedroom, whichever is less**. (Gov. Code, § 66314, subd. (d)(10)(A).)

- Spaces may be provided as **tandem parking on a driveway**. (Gov. Code, § 66314, subd. (d)(10)(B).)
- **Guest parking** shall not be required for ADUs under any circumstances.
- ADUs with no bedrooms (efficiency units/studios) do not increase the bedroom count.

Local agencies may choose to eliminate or reduce parking requirements (e.g., zero or half a space per ADU) to reduce barriers to construction.

### Six Parking Exemption Categories

A local agency **shall not** impose parking standards on any of the following ADUs (Gov. Code, § 66322, subd. (a)):

1. ADUs within **one-half mile walking distance of public transit**.
2. ADUs within an **architecturally and historically significant historic district**.
3. ADUs that are **part of the proposed or existing primary residence or accessory structure** (i.e., converted ADUs).
4. When **on-street parking permits are required but not offered** to the ADU occupant.
5. When a **car share vehicle is located within one block** of the ADU.
6. When an ADU permit is submitted **with a permit for a new SF or MF dwelling** on the same lot, provided the ADU or parcel satisfies any other criteria in (1)-(5).

When the parcel facts is available, use `state_entitlements.adu_parking_waiver` and the top-level `transit` block to assert the transit parking exemption. If the resolver reports `transit.within_half_mile_major_stop` or `transit.within_half_mile_hq_corridor`, the parcel is near qualifying public transit for the v1 state-law assertion; cite `transit.nearest.distance_ft` and Gov. Code § 66322(a)(1). Do **not** ask the applicant to measure, use Google Maps, or check an MPO when `transit` is present. If the v1 provider does not assert the waiver, do not say the parcel is definitely ineligible — the broader all-public-transit stop test may still need local confirmation.

### 66323 Units — Always Exempt

Local agencies **may not** impose parking requirements on 66323 Units (state-mandated ADUs under Gov. Code § 66323). (Gov. Code, § 66323, subds. (a), (b).)

### JADUs — Always Exempt

Local agencies **may not** require parking as a condition of permitting a JADU, even when the JADU is converted from an attached garage. (Gov. Code, § 66334, subd. (a).)

### Replacement Parking Not Required

When a garage, carport, covered parking structure, or uncovered parking space is **demolished** in conjunction with ADU construction or **converted** to an ADU, the local agency **shall not require** those off-street parking spaces for the primary unit to be replaced. (Gov. Code, § 66314, subd. (d)(11).)

### Flexible Siting

Local agencies should be flexible when siting ADU parking. Off-street parking spaces **shall be permitted in setback areas** in locations determined by the local agency or through tandem parking, unless specific findings are made based on site or regional topographical or fire and life safety conditions. (Gov. Code, § 66314, subd. (d)(10)(B).)

### Cross-References
- See also: `unit-types-66323.md` — 66323 Units are exempt from parking
- See also: `unit-types-jadu.md` — JADUs are always exempt from parking
- See also: `standards-setbacks.md` — Parking spaces may be in setback areas
- See also: `permit-process.md` — Garage demolition permit issued with ADU application

### Key Code Sections
- Gov. Code § 66314, subd. (d)(10)(A) — Max one space per unit or bedroom
- Gov. Code § 66314, subd. (d)(10)(B) — Tandem parking and setback siting
- Gov. Code § 66314, subd. (d)(11) — No replacement parking for demolished garages
- Gov. Code § 66322, subd. (a) — Six parking exemption categories
- Gov. Code § 66323, subds. (a), (b) — 66323 Units exempt from parking
- Gov. Code § 66334, subd. (a) — JADUs exempt from parking
