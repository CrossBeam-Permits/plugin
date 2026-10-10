# Laguna Beach - Planning, Design Review, Coastal, and Bluff Routing for New SFR

Sources:

- LBMC Sections 25.05.040 and 25.05.045, as replaced/added by Ord. 1732: the City source document (not included in this plugin)
- LBMC Chapter 25.13: the City source document (not included in this plugin)
- Objective Design Standards, City document 26790: the City source document (not included in this plugin)
- LBMC Chapter 25.07, Coastal Development Permits: the City source document (not included in this plugin)
- LBMC Section 25.50.004 and 25.50.020: the City source document (not included in this plugin)
- Bluff Edge Determinations Quick Guide: the City source document (not included in this plugin)

---

## New SFR Planning Route

Default: a new building requires Design Review under current §25.05.040(B)(1)(b). For one-family residential projects, Section 25.05.040(F) supplies the hearing authority.

Optional alternative: a qualifying new primary dwelling may elect Chapter 25.13 and take Zone Clearance under §25.05.040(B)(2)(z). Run `objective-primary-dwelling-ch25-13.md`, then the 2026 objective-design overview and exactly one applicant-selected Form Group reference. The Chapter 25.13 development gate and every applicable design standard must pass. A major remodel is ineligible, other simultaneous structures may be separately reviewed, and a CDP may remain required.

Required outputs:

- Route: Design Review, Chapter 25.13 Zone Clearance, or `indeterminate`.
- Form Group selection and separate general/selected-group design-conformance findings.
- Staking: required for DRB hearings; stakes/ribbons must represent the full proposed structure, including decks and eaves.
- Appeal/effective date: DR decision effective after 14 calendar days unless appealed.
- Expiration: DR approval lapses after 2 years if not used/commenced; extensions are available through the code process.

Use the shared full reference at `../../residential-remodel/references/city-design-review-tiers.md` when notice, staking, hearing-count, or appeal details matter.

---

## Design Review Criteria

Section 25.05.040(H) has 11 criteria: Access; Design Articulation; Environmental Context; General Plan Compliance; Historic Preservation; Landscaping; Lighting and Glare; Neighborhood Compatibility; Pedestrian Orientation; Privacy; and View Equity.

For a new SFR, do not stop at numeric height/setback compliance. Return a separate DR finding for compatibility, privacy, view equity, massing, and neighborhood context when the plans create issues.

---

## Fire Safety Standards Review

Current §25.05.040(C)(4) requires Fire Department or Building Division review, as applicable, before deliberation on a Design Review application for new construction and major remodels, including proposed fuel-modification programs. Do not use the former 50%-alteration Fire-Department-only trigger.

---

## Coastal Development Permit Route

Section 25.07.004 requires a CDP for all proposed development within the coastal zone unless exempt under Section 25.07.008 or 25.07.010.

For a new SFR:

- Treat the work as new "development" under Section 25.07.006.
- Do not use the routine "improvements to single-family dwellings" exemption in Section 25.07.008(A)(1) because new SFD construction is not an improvement to an existing SFD.
- Determine whether the parcel is in the appealable area.
- If appealable, apply the 10-working-day Coastal Commission appeal window after CCC receipt of final local action.

Use `../../residential-remodel/references/city-cdp-coastal-zone.md` for detailed CDP procedure and appealable-area logic.

---

## Appealable Area Checks

Section 25.07.006 appealable areas include:

- All area between the sea and the first public road paralleling the sea.
- All area within 300 ft of the inland extent of any beach or mean high tide line where there is no beach.
- All area within 100 ft of any wetland, estuary, or stream.
- All area within 300 ft of the top of the seaward face of any coastal bluff.

Use polygon data if available; otherwise flag the applicant's coastal/appealable-area assertion for Planning confirmation.

---

## Bluff / Oceanfront Route

If the parcel is oceanfront or oceanfront-bluff:

1. Apply Section 25.50.004(B)(4): more restrictive of applicable stringline or 25 ft from top of oceanfront bluff.
2. Apply the 25 ft minimum to pools and spas.
3. Apply 10 ft minimum to deck/patio/balcony projections, including projections 30 in or less above grade.
4. Recalculate Section 25.50.020 site coverage using the reduced oceanfront lot area.
5. Require the Bluff Edge Determinations report stack when the project is new development, major remodel, or an addition on oceanfront/oceanfront bluff property.

Use `../../residential-remodel/references/city-bluff-overlay.md` for the full bluff-edge and report analysis.
