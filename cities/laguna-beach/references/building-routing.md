# Building routing

## Record separation rule

Create one Building record, Building/MEP application, scope description, valuation, attachment bundle, and receipt per distinct scope. Shared plans may be uploaded to more than one record, but records must not share a blended valuation.

## Record type and work class

Every online Building filing has two parts: the portal **record type** (the catalog entry, such as 183 Residential Permit) and the **work class** inside it (such as Reroof, Pool, Demolition, or Revision). The work class decides which More Info questions, uploads, and contacts the City asks for, and whether fees come before or after staff review. The pinned map `assets/portal-maps/v2-portal-map.json` lists every online work class for each type, read from the City's public portal on the date in its `source.pulled_at`.

## Supported V1 routes

| Reasoned scope | Portal type | Work classes the City offers online (v2 map) | Required base uploads | Key boundary |
|---|---:|---|---|---|
| Residential new dwelling, addition, alteration, remodel, ADU after Planning, pool, reroof, deck/patio, fence/wall, hardscape, garage, shoring, slope repair, window/door, and similar residential building work | 183 Residential Permit | 32 classes, including New Single Family Residence, Addition, Alteration, Remodel, ADU - Attached/Detached, Pool, Reroof, and the default Residential class | Signed Building Application (`Permit Application`; 2 pages, with the Stormwater Quality Certification); an already-filled older one-page form is accepted, and its missing stormwater page is a Tidy-up + one merged `Plans` PDF; `permittee.type` confirmed | Reroof also needs the exact color swatch (`Roof Material Color Swatch`); issuance later in person |
| Standalone demolition | 183 Residential Permit | Demolition; Demolition - Single Family Residence; Demolition - ADU/JADU; Demolition - Duplex. All are online, Review First | `Permit Application` + `Plans` | Its own record and valuation; never ride on the new-building record |
| Revision of an issued, approved permit | 183 Residential Permit | Revision (**Pay First**) | `Original Plans Approved/Stamped by City` + `Revised Plans` | Not for plan-check corrections or added scope; see below |
| Mechanical work | 186 Mechanical Permit | Mechanical | Signed Building or MEP application | A/C requires Mechanical Equipment Guide despite optional portal flag |
| Panel/service/electrical work | 187 Electrical Permit | Electrical; Residential Electrical Service Panel up to 400 AMP (**Pay First**) | Signed Building or MEP application; the panel class asks for its own uploads | Contractor/licence/utility facts must be confirmed; portal item counts |
| In-kind same-location/same-type/size/rating water heater and other plumbing work | 188 Plumbing Permit | Plumbing | Signed Building or MEP application | Tankless conversion, relocation, capacity/fuel change is not the simple in-kind route |
| Grading | 214 Grading Permit | Grading (default); 0 - 20 Cubic Yards; Over 20 Cubic Yards | Signed Building Application (2 pages, with the Stormwater Quality Certification); an already-filled older one-page form is accepted, and its missing stormwater page is a Tidy-up + Plans | Add soils/geotech, grading plans, hydrology, WQMP/LID, survey as triggered |

Run `python3 scripts/list-work-classes.py --type <id>` for the full, current list with each class's questions, uploads, contacts, and the City's own instruction text.

Most 183 classes share one 165-question layout (Reroof, Pool, Addition, Alteration and others). ADU - Attached, ADU - Detached and New Single Family Residence share a 124-question layout. The default Residential class has 113. Populate counts only from plan evidence or user confirmation; zero is a value and must also be sourced. Types 186/187/188 have their discipline-specific count groups.

## Choosing the work class

Choose by reasoning, never by matching words between the scope and a class label.

1. Read every online class for the type with `scripts/list-work-classes.py`. Note what each asks for: its questions, uploads, filing behavior, and the City's instruction text.
2. From the confirmed project facts, decide which class the City would expect for this one record: what is built, removed, or changed; new or existing; the dwelling type; and whether the record revises an already-issued permit.
3. If two classes still fit (for example Remodel and Alteration, or Addition and Alteration), say so, show the user the difference you can see in the map, and ask the user or the Building Division. Do not guess.
4. Write `permit-work/state/work-class-selection.json` (schema `schemas/work-class-selection.schema.json`): the class ID and label, your reasoning, the fact IDs it rests on, and the classes you ruled out and why. Show it with the filing theory. Set `status: confirmed` and `confirmed_at` only after the user confirms.
5. Build the submission plan with `--work-class-selection`. The plan builder never picks a class. It blocks the record when no class is confirmed, and it hard-stops when the chosen class, its layout, or its upload rules are not in the pinned map. A hard stop means: run the portal freshness check, rebuild and review the map, and only then continue.

A class that has its own catalog entry is filed there, not under the parent type. Example: the SolarAPP+ class of the Residential type is catalog entry 124, which V1 does not support.

## Filing behavior

The map records the City's filing behavior for each class (`filingBehavior`):

- **Review First:** staff screen the submittal, then contact the applicant for payment, generally in 2-3 business days (the City's configured success message).
- **Pay First:** the portal asks for fees as part of filing. Payment is still its own transaction with its own approval; see `online-submission.md` P8 and `after-filing.md`.
- **Simple:** the portal may invoice or issue at once. V1 maps none for filing.

## Revision is Pay First and narrow

The City's Revision class instructions say it is "STRICTLY FOR A SUB-PERMIT TO REVISE DETAILS OF PREVIOUSLY APPROVED AND PERMITTED WORK"; added scope needs a separate application; the description must state the revision number; changed sheets must be clouded with a delta; and inspections stay on the original permit record (City instructions keyed to type 183 / class Revision, in `assets/portal-maps/portal-snapshot.json`). Its More Info layout requires `RevisionNumber`. Use it only when an issued permit exists and the evidence shows a revision of that approved work. Answer plan-check corrections on the existing record instead (`after-filing.md`).

## Non-online and unsupported boundaries

- A panel upgrade above 400A or serving more than two meters is outside the e-permit route and outside V1 source coverage. The Pay First panel class covers a residential service panel up to 400 A only.
- The panel class's contact set marks Contractor and Owner/Builder required; the City's instructions ask for "Contractor or Owner-Builder". V1 has no canonical owner-builder identity mapping, so the plan builder blocks that class until one exists. Do not invent a declaration.
- Commercial Planning is unsupported. Commercial reroof may be reasoned from the source corpus but is outside this residential-first V1 transaction set.
- Never collapse new dwelling, demolition, grading, pool, ADU, or MEP scopes into one Residential record merely because they share plans.

## Requirements source

This reference compiles the **transaction boundary** — which portal type and work class, which record separation, which base form. It is not a scope-to-requirements classifier and does not enumerate every Building submittal item.

The authoritative scope-to-requirements layer for the Building lane is the City checklists in `requirements/building/` (see `requirements/README.md`) and the plan-sheet matrix in `requirements/plan-sheets/`, checked with `skills/plan-set-check/SKILL.md`. The simple per-scope skills under `skills/` (`reroof`, `panel-upgrade` and the rest) add Laguna's local rules for those jobs. Read those for what a submittal must contain; read this file for how the filing is structured.

Where a project falls outside both the scope skills and the routes above, say so plainly, name the uncovered scope, and get City guidance. Do not adapt a neighbouring route to close the gap.

## Sources

- Online work classes, layouts, uploads, contacts and instruction text: City public portal API read 2026-10-09 with GET requests only; pinned in `assets/portal-maps/portal-snapshot.json` and compiled to `assets/portal-maps/v2-portal-map.json` by `scripts/build-portal-map.py`.
- Catalog statement that final permit issuance is in person at the Building counter: catalog descriptions for 183, 186, 187, 188 and 214 in the same snapshot.
