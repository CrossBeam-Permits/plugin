# Guided intake

Build one provenance-bearing fact table for Planning forms, Building forms, portal answers, routing, and attachment rules. Ask progressively; do not reproduce the City's entire application as chat questions.

## First exchange

Ask for:

1. Laguna Beach property address.
2. Plain-language description of all proposed work, including demolition, grading, pool/spa, ADU/JADU, utilities, reroof, and equipment.
3. Current stage: exploring, preparing Planning, Planning submitted, Planning approved/effective, preparing Building, correction/resubmittal, or permit issuance.
4. Available files: plans, surveys, title report, prior approvals, correction letters, calculations/studies, applications, and contractor materials.

Inventory first. Extract facts before asking the user to retype them.

## Fact contract

Every entry in `project-facts.json.facts` contains:

- stable canonical `id`;
- `value` or null;
- `source.kind`: `user_confirmed`, `plan`, `application`, `title_report`, `site_facts`, or `portal`;
- a receipt with file/page/sheet/field or user-answer timestamp;
- confidence from 0 to 1;
- whether applicant confirmation is required and, if so, its state;
- downstream consumers.

Use `site.address`, `project.description`, `project.stage`, `owner.*`, `applicant.*`, `contractor.*`, `designer.*`, `project.valuation.<record-id>`, and scoped plan facts such as `zoning.lot_area.existing`.

## Question batches

After extracting documents, present short batches in this order:

1. Identity and roles: owner, applicant, authorized agent, contact details.
2. Scope and process facts that change the filing route.
3. Separate Building record descriptions and valuations.
4. Contractor/designer/engineer details only where applicable.
5. Design-contingent requirements identified by the routing corpus.
6. Applicant-controlled assertions, declarations, and acknowledgements.

State why each answer is needed and which record it affects.

## Conflict protocol

If two sources disagree, store both candidates in the fact's `conflicts` array, stop the affected consumer, and ask the user to resolve it. Never silently prefer the value that makes the form complete. A plan/portal mismatch in address, scope, valuation, counts, or contact identity blocks the affected record.
