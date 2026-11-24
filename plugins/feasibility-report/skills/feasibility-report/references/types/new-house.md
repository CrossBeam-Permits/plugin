# Profile: new house

Permit type ids to try: `single-family-residential`.

## Intake
- Size, stories, bedrooms, garage; whether an existing house is demolished; vacant lot or teardown.
- Slope, retaining walls and how much earth moves; access and driveway; trees.
- Utilities: sewer or septic, water or well, electric service; gas or all-electric.

## Questions
| Topic | Where to look |
|---|---|
| Zone standards: setbacks, height, stories, lot coverage, FAR, open space, landscaping | City zone chapter |
| Design review, neighborhood compatibility, view or privacy rules, and whether review is ministerial or has a hearing | City design review chapter |
| Hillside, grading and drainage limits; when a grading permit or soils report is needed | City grading chapter; building code; site-facts slope and soils |
| Wildfire building rules and defensible space in a fire hazard zone | State and city wildfire building code chapters; site-facts fire zone |
| Flood, coastal, liquefaction or fault zone requirements | Site facts; city floodplain and coastal chapters; state law |
| Demolition of an existing house (permit, historic review, housing replacement rules) | City code; state housing law |
| Fire department access, hydrant distance, sprinklers | Fire code and city amendments |
| Energy (solar, all-electric reach codes), green building | Energy code; CALGreen in California; city reach code |
| Impact, school and utility connection fees | `crossbeam_fees`; city fee schedule |
| Parking and garage rules | City parking chapter |

## Extra checks
- `crossbeam_permit_status` with the address: prior permits, open cases, an approval to revise.
- `crossbeam_get_review_requirements` for each lane (building, planning).

## Cards
Zone standards and the fit table · design review path · grading, slope and drainage · hazard zones (fire, flood, seismic, coastal) · demolition · fire access and sprinklers · energy and green building · utilities · fees.

## Intake checklist additions
Survey and topography; soils report; grading and drainage plan; architectural set; structural calcs; energy report; fire department sheet; landscape plan if required; demolition permit; utility will-serve letters where needed.
