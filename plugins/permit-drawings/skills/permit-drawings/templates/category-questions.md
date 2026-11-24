# Category questions template

Use this at stage 2 (`references/02-path.md` section 3). It holds five questions. Each question covers one category of what a plan reviewer expects for a scope. Copy the questions, replace each `<...>` placeholder, and ask them with `crossbeam_ask`. Put the five in one numbered question, or ask each in its own conversation.

Scope checklist rows replace a question only when they name the category's individual items. A row that names only the category does not. `references/02-path.md` section 3, step 4 says when to ask each question.

These answers are not law. They say what the reviewer will look for. Record each item with the level of its source (`references/02-path.md` section 3, step 5).

## The questions

Context to give with every question:

- Jurisdiction and state: `<jurisdiction>, <state>`
- Code basis: `<code family, edition, effective date from logs/code-decisions.md>`
- Permit type: `<name and ID from logs/scope.md, or "no ID">`
- Scope statement: `<the paragraph from logs/scope.md>`
- Building: `<building type, storeys, year built if a document gives it>`
- Who prepares the plans: `<the owner / a builder / a designer>`

(a) Documents. "For this scope in `<jurisdiction>`, which documents must go with the plans? Include forms, calculations, reports, product data, checklists, owner declarations, recorded documents and any form for another agency, such as the fire authority. For each one, say who may prepare it, whether it needs approved software or a licensed preparer, and where the official blank form is published. Cite the source for each."

(b) Cover-sheet project data. "Which project data must the cover sheet show for this scope in `<jurisdiction>`? Include the building data (occupancy group, construction type, building height and number of stories, year built), areas, the codes and local code to list, design criteria, site designations and hazards, and any count the reviewer checks. Cite the source for each."

(c) General notes. "Which general notes must the sheets carry for this scope in `<jurisdiction>`? Include construction notes, environmental and health notes, and notes the city adds by local rule. For each one, give the section and the edition, and quote the text that requires it."

(d) Site plan. "What must the site plan or plot plan show for this scope in `<jurisdiction>`? Include lot lines and dimensions, distances from each building to the lot lines, other structures, utilities and any other item the reviewer checks. Cite the source for each."

(e) Plan sheets. "For this scope, which plan sheets does the plan reviewer expect: floor plan, electrical plan, mechanical plan, plumbing plan, framing plan, sections, details, others? What must each one show?" Give the existing devices recorded at stage 3 (`references/03-measure.md` section 7) when you have them.

## Where each answer goes

| Question | Record in | Section |
|---|---|---|
| (a) Documents | `logs/required-documents.md` | Documents |
| (b) Cover-sheet project data | `logs/required-documents.md` | Sheet content plan |
| (c) General notes | `logs/required-documents.md` | Sheet content plan |
| (d) Site plan | `logs/required-documents.md` | Sheet content plan |
| (e) Plan sheets | `logs/required-documents.md` | Documents, one row per sheet |

Record each question and answer as an entry in `logs/code-decisions.md`, with its conversation ID and the level of each item. Each row in `logs/required-documents.md` names that entry.

For every value an item needs (a lot dimension, a year built, an area), find it in the documents first (`references/02-path.md` section 5). Ask the owner only for a value no document holds.
