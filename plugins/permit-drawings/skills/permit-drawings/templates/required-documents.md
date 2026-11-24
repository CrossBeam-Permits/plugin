# Required-documents template

Copy this into `logs/required-documents.md` at stage 2 (`references/02-path.md` section 3). This file is a table you update in place. Record each change in `logs/decisions.md`.

Status values: `references/02-path.md` section 3, step 6 defines every status of the Documents table. When `logs/setup.md` names a city plugin, the city's own application forms and portal answers take `by city plugin (<plugin>)`.

Row 1 is an example. The "Preparer statement" row takes only `done`, `not required (source)` or `unknown: confirm with the city`. Omit the row when CrossBeam or the city already says no statement is needed (`references/02-path.md` section 2, step 6).

The "Level" column holds the level of the source that put the row on the list (`references/02-path.md` section 3, step 5).

```markdown
# Required documents

## Documents
| # | Document | Required by (source, date) | Level | Who prepares | Status | File |
|---|---|---|---|---|---|---|
| 1 | Preparer statement on the sheets | <quoted CrossBeam citation / city's written instruction (source, date) / "no citation"> | <quoted / primary-read / unquoted / city instruction> | <who prepares the plans> | <done / not required (source) / unknown: confirm with the city> | project.json preparer.statement |

## Sheet content plan
Items the cover sheet, the general notes and the site plan must show (category questions (b), (c) and (d), or scope checklist rows).

| # | Category | Item | Required by (CD entry or checklist row) | Level | Value source | Sheet and note | Status |
|---|---|---|---|---|---|---|---|

Category: cover data / general note / site plan. Value source: the document, site fact or `project.json` key that gives the value, or "open: Q-xxx". Status: `planned`, `drawn`, `open (<what is missing>)`, `not required (source)`.

## Scope checklist rows
Source: <crossbeam_get_scope_checklist, date / crossbeam_ask, conversation ID / coverage: none>

| Row | Requirement | Where the reviewer looks | Layer | Sheet and note that answers it |
|---|---|---|---|---|

## Facts sent to the checklist
| Fact id | Value with units | Source |
|---|---|---|
```
