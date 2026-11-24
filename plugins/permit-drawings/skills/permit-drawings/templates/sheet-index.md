# Sheet index template

Copy this into `logs/sheet-index.md` at stage 2 (`references/02-path.md` section 7), before the first measurement. It is the plan of the whole set: every sheet and the kit module it needs. Forms and their status stay in the Documents table of `logs/required-documents.md`. Update it in place when the scope changes, and record each change in `logs/decisions.md`.

The rows below are examples for a California remodel with a new beam. Replace them. A whole set drawn from scratch keeps a structural row and the energy and green rows (outside California, the energy and green documents the city lists) unless a source says the scope does not need them; then the row stays, with the status `not required (source)`.

Status values: `planned`, `drawn`, `by others (<who>)`, `by others: not engaged (<kind of preparer>)`, `not required (source)`. "Source" is the Documents table row, scope checklist row, packaging rule or code decision that asks for the sheet.

```markdown
# Sheet index

Permit type: <name and ID from logs/scope.md>
Sheet size and numbering: <from packaging_rules (source) / no rule: 24 x 36, A, S and T prefixes>

## Sheets
| # | Sheet | Title | Discipline | Shows | Source | Who prepares | Module | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | A-0 | Cover | architectural | project data, sheet index, open items, code checks | <RD row / packaging rule> | <you> | core | planned |
| 2 | A-1 | Site or plot plan | architectural | lot lines, setbacks, north arrow, work area | <RD row / checklist row> | <you> | core | planned |
| 3 | S-1 | Framing plan and members | structural | beam, posts, connections, preliminary calc for the engineer | <RD row / CD entry> | <you, with the engineer's calc by others (<who>)> | structural | planned |
| 4 | T-1 | Title 24 energy | energy | T-24 summary, CF1R worksheet | <RD row / CD entry> | <you; CF1R by the documentation author> | energy | planned |
| 5 | G-1 | CALGreen mandatory measures | green | measures that apply, with reasons | <RD row / CD entry> | <you> | energy | planned |

## Modules
- Needed: <energy, structural, 3d / none>
- Installed: <list, from python3 -m permitkit modules>
- Owner's answer on structural, energy and 3D sheets: <date, owner's words; see logs/decisions.md>
```
