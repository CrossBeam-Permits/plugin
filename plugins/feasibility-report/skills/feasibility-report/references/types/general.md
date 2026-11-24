# Profile: general (any other permit)

Use it for a pool, retaining wall, deck, patio cover, fence or wall, sign, solar or battery, demolition, grading, industrial work, or any project no other profile fits. Find the permit type id from the list `crossbeam_get_review_requirements` returns for a bad id.

## Intake
- What is built or removed, its size and location on the lot, and anything it touches (property line, slope, existing structure, utilities).

## Questions
| Topic | Where to look |
|---|---|
| Is a permit needed at all, and which (building, planning, grading, encroachment, fire) | `crossbeam_get_review_requirements`; city code; `crossbeam_ask` |
| Location limits: setbacks, height, coverage, easements | City zone chapter; title report |
| The building code sections for the thing being built (pool barriers, guards, retaining-wall height, solar access) | `crossbeam_rules` with the elements; `crossbeam_lookup_code` |
| Hazard zones that add requirements | Site facts |
| Fees | `crossbeam_fees` |

## Extra checks
- `crossbeam_permit_status` with the address.

## Cards
Is a permit needed · where it can go (fit table) · the code for what is built · hazard zones · fees · review path.

## Intake checklist additions
What `crossbeam_get_review_requirements` lists for the permit type; otherwise a site plan, construction details, and engineering where the code calls for it.
