# Building routing

## Record separation rule

Create one Building record, Building/MEP application, scope description, valuation, attachment bundle, and receipt per distinct scope. Shared plans may be uploaded to more than one record, but records must not share a blended valuation.

## Supported V1 routes

| Reasoned scope | Portal type | Required base form/attachments | Key boundary |
|---|---:|---|---|
| Residential new dwelling, addition, ADU after Planning, structural alteration, reroof, pool/related residential building work | 183 Residential Permit | Signed Building Application + Plans | Reroof also needs exact color-swatch attachment; issuance later in person |
| Mechanical work | 186 Mechanical Permit | Signed Building or MEP application | A/C requires Mechanical Equipment Guide despite optional portal flag |
| Panel/service/electrical work | 187 Electrical Permit | Signed Building or MEP application | Contractor/licence/utility facts must be confirmed; portal item counts |
| In-kind same-location/same-type/size/rating water heater and other plumbing work | 188 Plumbing Permit | Signed Building or MEP application | Tankless conversion, relocation, capacity/fuel change is not the simple in-kind route |
| Grading | 214 Grading Permit | Signed Building Application + Plans | Add soils/geotech, grading plans, hydrology, WQMP/LID, survey as triggered |

Type 183 has 113 MEP count fields. Populate counts only from plan evidence or user confirmation; zero is a value and must also be sourced. Types 186/187/188 have their discipline-specific count groups.

## Non-online and unsupported boundaries

- Standalone demolition has no V1 online type. Prepare its own application/valuation and current counter or appointment handoff.
- A panel upgrade above 400A or serving more than two meters is outside the e-permit route and outside V1 source coverage.
- Commercial Planning is unsupported. Commercial reroof may be reasoned from the source corpus but is outside this residential-first V1 transaction set.
- Never collapse new dwelling, demolition, grading, pool, ADU, or MEP scopes into one Residential record merely because they share plans.

## Requirements source

The source repository's `skills/cities/laguna-beach/submittal-requirements/ROUTING.md`, `scope-map.yaml`, and Building reference corpus remain the authoritative scope-to-requirements layer. This skill compiles the transaction boundary, not a parallel semantic classifier. Where a project falls outside the declared source coverage, say so and get City guidance.
