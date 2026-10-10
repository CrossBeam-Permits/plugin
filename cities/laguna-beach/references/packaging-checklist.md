# Packaging checklist

Run this checklist per portal record.

## Record integrity

- Address, scope, lane, process stage, prerequisites, and portal type are confirmed.
- No matching draft/open record remains unresolved.
- Planning application set contains each applicable form once.
- Building scopes, applications, descriptions, and valuations are separate.
- Every populated value has a source receipt or user confirmation.
- Form checksum and field-map version are current.

## Plan-set check (before packaging)

Run the `plan-set-check` skill (`skills/plan-set-check/SKILL.md`) on the final merged
plan set before you assemble any packet that carries plans.

- The check ran on the exact file you will upload. Record its SHA-256 next to
  `permit-work/output/plan-check/plan-set-check.json`. A changed sheet means a new check.
- The scope, plan-sheet matrix rows and checklists it used match the confirmed filing
  theory in `application-set.json`.
- Every **missing** item is fixed, or the user has decided to file anyway. Record that
  decision and show it in the pre-submit manifest.
- Every **unclear** item is resolved or listed for the City.
- The check is a completeness check only. Never describe it to the user as a code review
  or a City approval.

## PDFs

- Editable form verified logically; all updated widgets have appearances.
- Rendered preview inspected; no clipping, overlap, black glyphs, or stale values.
- User-controlled signature/declaration fields are reviewed and personally completed.
- Each uploaded application is the applicant-signed file whose SHA-256 matches `signed_sha256` in its signed verification (status `signed_verified`), and every signature crop was viewed (`scripts/verify-signed-form.py`).
- Merged PDFs open, have the expected page order/count, and preserve every source page.
- Final local filenames are unique, stable, descriptive, and hashed after assembly.

## Upload map

- Each filename maps to one exact City category in `submission-plan.json`.
- Required slots contain exactly the allowed file count/type.
- Type 114: one combined Application PDF, one Plans PDF; Reports/Technical Studies deliberate.
- Type 182: ADU/JADU Application and Plans; discipline plans deliberate.
- Type 183: signed Permit Application and Plans; triggered optional categories promoted to required locally.
- Types 186/187/188: signed Permit Application plus triggered discipline documents.
- Type 214: Permit Application, Plans, and triggered soils/grading/hydrology/WQMP/LID/survey categories.

## Pre-submit manifest

Show address, record/type, description, valuation, contacts, each file/category/hash, the plan-set check result (counts of present, missing and unclear, and any file-anyway decision), remaining declarations, duplicate/drift warnings, and the post-submit payment/issuance expectation. Submission is blocked if any warning is unresolved.
