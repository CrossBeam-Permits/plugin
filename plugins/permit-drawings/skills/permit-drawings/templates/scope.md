# Scope template

Copy this into `logs/scope.md` at stage 1 (`references/01-scope.md`). This file is a table you update in place. Record each change in `logs/decisions.md`.

```markdown
# Scope

## Jurisdiction
- Address: <full address> — source: <message / document>
- Permitting agency: <city or county>, <state> — source: <CrossBeam answer, conversation ID>
- CrossBeam covers this jurisdiction: <yes / no>

## Scope statement
<One paragraph, plain construction words. Name the floor. Name each change. End with what is not in scope.>
Owner confirmed: <date, the owner's words>

## Facts
| Fact | Value | Source | Read back to owner |
|---|---|---|---|
| Room use, each room in the work area (the owner's words) | | | |
| Bedroom count after the work | | | |
| Floor (storey) of each item of work | | | |
| Bearing or non-bearing, each changed wall | | | |
| Who builds (owner-builder or named contractor) | | | |
| Property owner's name, as the property record shows it | | | |
| Earlier permits the work touches | <list / none / unknown: confirm with the city> | | |

A fact the owner cannot answer yet: write "open: Q-xxx" as its value. `logs/questions.md` names the work it blocks.

## Elements
| Element | (E) / (N) / demo | Each end stops against | Source |
|---|---|---|---|

## Permit type
- Type: <name> — ID: <ID from crossbeam_get_review_requirements, or "no ID"> — source: <conversation ID>
- Other permits for this scope: <list, or "none stated">
```
