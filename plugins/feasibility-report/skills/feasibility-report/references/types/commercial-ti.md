# Profile: commercial tenant improvement or change of use

Permit type ids to try: `commercial-ti`, `restaurant-ti`, `commercial-new`.

## Intake
- The tenant's use, in plain words (what happens in the space, hours, seats, employees), the previous use, and the suite's floor area.
- Work scope: walls, ceilings, mechanical, electrical, plumbing, storefront, signs, outdoor seating; food preparation and cooking type; hazardous materials.
- Building facts: year built, construction type, sprinklers, fire alarm, stories, restrooms, accessible entrance and parking.

## Questions
| Topic | Where to look |
|---|---|
| Is the use allowed in the zone, by right or with a use permit; any distance or concentration rules | City use table and zone chapter |
| Parking for the new use versus the old one, and any credits for existing spaces | City parking chapter |
| Occupancy classification, and whether the change of use is a change of occupancy | Building code occupancy chapter; existing building code |
| Accessibility: path of travel, restrooms, entrance, parking, and the cost threshold for upgrades | Building code accessibility chapter (11B in California) |
| Fire sprinklers, fire alarm, exits and occupant load | Building and fire codes; city fire amendments |
| Food uses: health department plan review, grease interceptor, hood and duct | County health department; plumbing and mechanical codes; sewer agency |
| Energy for lighting and mechanical alterations | Energy code |
| Signs, outdoor seating, business license | City sign and outdoor dining rules; business license |
| Fees, including impact or sewer capacity fees on a change of use | `crossbeam_fees`; city and sewer agency schedules |

## Extra checks
- `crossbeam_permit_status` with the address (and suite): the space's earlier permits and its last approved use.
- `crossbeam_get_review_requirements` with `commercial-ti` or `restaurant-ti` for each lane.
- `crossbeam_contractor_license` if the person names a contractor.

## Cards
Use allowed (fit to the zone) · parking · occupancy and change of occupancy · accessibility upgrades · fire and life safety · food and health (only for food uses) · energy · signs and outdoor space · fees · review path and timeline (Planning, Building, Fire, Health).

## Intake checklist additions
Floor plan with occupant load and exits; accessibility plan and path-of-travel analysis; mechanical, electrical and plumbing sheets; energy compliance forms; health department approval for food uses; fire sprinkler and alarm submittals; sign permit.
