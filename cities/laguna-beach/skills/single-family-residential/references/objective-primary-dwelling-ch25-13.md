# Laguna Beach — Optional Chapter 25.13 Primary-Dwelling Path

**Law as of:** 2026-08-10
**Authority:** LBMC Chapter 25.13, added by Urgency Ordinance No. 1732; City document 26790, *Objective Design Standards for Single-Family and Two-Family Residential Development*
**Official signed ordinance:** https://ecode360.com/LA4953/laws/LF2759074.pdf

Chapter 25.13 is an optional alternative to discretionary Design Review for a new primary dwelling unit in a single-family residential zone. A qualifying project takes Zone Clearance under §25.05.040(B)(2)(z) and §25.05.045. This is an exemption from discretionary Design Review only: a Coastal Development Permit and other permits may still be required.

## Eligibility gate

Return `eligible` only if all are true:

- the proposal is a new primary dwelling unit in a single-family residential zone;
- it is not a major remodel;
- the primary dwelling and every component subject to the chapter meet the objective development standards;
- the proposal meets all 13 General Design Standards and every applicable standard in exactly one applicant-selected Form Group from the adopted 2026 Objective Design Standards; and
- any other simultaneously proposed structure is separately routed if it does not qualify under the chapter.

A major remodel cannot use Chapter 25.13 even though §25.56.011 classifies it as a new building.

## Computable development standards

- One story and no more than 15 ft high.
- Primary dwelling: no more than 1,500 sf gross floor area.
- Second primary dwelling where otherwise lawful: no more than 800 sf.
- Garage: no more than 400 sf and two parking spaces.
- Front, side, and rear setbacks: 20% greater than the underlying-zone minimums.
- No setback redistribution and no reduced setback under §25.50.004(E).
- Lot FAR follows the 12-row Table A in the enacted chapter, from 0.60 for the smallest band through 0.17 for lots of 10,000 sf or more.
- Landscaping maintained-height caps: no more than 15 ft within buildable area; no more than 6 ft in rear/side yards; no more than 4 ft in front yard, or no more than 3 ft on a corner lot.
- Exterior lighting fully shielded and aimed downward.
- Roof decks prohibited.
- The state-law floor remains available for a compliant ADU (850 sf studio/one-bedroom or 1,000 sf two-bedroom) and a 500 sf JADU.

Use the complete current-law table and enacted details in:
the City source document (not included in this plugin).

## Adopted objective design standards

The ordinance's objective **development** standards are only the first gate. The City published the adopted objective **design** standards as document 26790 in August 2026. Load:

1. `objective-design-standards-2026.md` for applicability, the 13 General Design Standards, and the pathway decision contract.
2. Exactly one applicant-selected file: `objective-design-form-group-a-2026.md`, `objective-design-form-group-b-2026.md`, `objective-design-form-group-c-2026.md`, or `objective-design-form-group-d-2026.md`.

The applicant may choose A, B, C, or D, but may not mix groups. The source does not constrain that choice by zone, neighborhood, or context, so never infer it. An unstated choice or a missing plan locator makes final eligibility `indeterminate`, not pass.

The completed Chapter 2 and selected Chapter 3 checklists belong in the application package. Treat an omitted checklist as nonblocking staff verification until the City confirms its intake effect in a CrossBeam reference that is not included in this plugin.

If every development and design standard passes, the project may take Zone Clearance without Design Review. If a standard fails, preserve the source's three choices: revise/resubmit, seek discretionary DRB/Planning Commission review, or withdraw. A CDP may still be required, and other simultaneous structures remain separately routed. In a VHFHSZ/fire-code conflict, the more restrictive standard governs; Zone 0 areas are exempt from Chapter 2 landscaping standards.

The signed ordinance repeats section number `25.13.040` for Administration, Objective Development Standards, and Objective Design Standards. Preserve that enacted numbering anomaly in legal references; do not silently renumber it.

## Output

```text
Chapter 25.13 election: requested | not requested | unknown
Zone eligibility: pass | fail | unknown
Major remodel: no (required) | yes (ineligible) | unknown
Height/story: pass | fail | unknown
Floor-area/garage: pass | fail | unknown
Setbacks: pass | fail | unknown
Table A FAR: pass | fail | unknown
Landscape/light/roof-deck standards: pass | fail | unknown
Objective-design Form Group: A | B | C | D | unknown
General Design Standards (13): pass | fail | unknown (one row per rule)
Selected Form Group standards: pass | fail | unknown (one row per rule)
Objective-design checklist: present | missing—staff verification | unknown
Other simultaneous structures: separately routed | none | unknown
CDP: required | exempt | Planning determination needed
Final route: Zone Clearance | Design Review | indeterminate
If not eligible: revise/resubmit | discretionary DRB/Planning Commission | withdraw | applicant decision pending
```
