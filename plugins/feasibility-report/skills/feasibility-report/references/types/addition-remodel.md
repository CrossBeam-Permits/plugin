# Profile: addition or remodel

Permit type ids to try: `residential-addition`, `residential-remodel`.

## Intake
- Added floor area, stories, rooms; what is demolished or altered; whether the work changes the footprint or roof.
- Existing house: year built, size, construction, sprinklers, known unpermitted work, whether it meets today's setbacks.
- Rough construction value if the person has one (do not invent one).

## Questions
| Topic | Where to look |
|---|---|
| Zone standards for the addition: setbacks, height, coverage, FAR, daylight planes | City zone chapter |
| Nonconforming structures: what can be added or rebuilt when the house does not meet today's standards, and the demolition or valuation threshold where it loses that status | City nonconforming chapter |
| Upgrades the work triggers in the existing house (sprinklers, smoke and CO alarms, energy, accessibility, structural) | Residential and existing building codes; city and fire amendments |
| Design review or a second-story review; historic status | City design and historic chapters; site-facts overlays |
| Parking added when bedrooms or area are added | City parking chapter |
| Fees, including whether impact fees apply to additions | `crossbeam_fees`; city fee schedule |

## Extra checks
- `crossbeam_permit_status` with the address: earlier permits (and whether the existing rooms were permitted), open cases.
- `crossbeam_rules` for the elements being added (stairs, egress windows, guards) when the person wants drawing-ready values.

## Cards
What can be added (fit table) · nonconforming status · upgrades the work triggers · design or historic review · parking · structure and foundation · fees.

## Intake checklist additions
Existing and proposed plans with areas; demolition plan; structural calcs; energy report for the new and altered space; smoke and CO alarm plan; survey if setbacks are tight.
