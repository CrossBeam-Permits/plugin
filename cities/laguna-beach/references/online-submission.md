# Online submission gates

EnerGov filing is a resumable external transaction. Use visible labels and current page state, not screen coordinates or one brittle selector chain. Persist only non-secret state in `browser-state.json`.

## P0 - Browser and account

- Require a user-visible browser-control surface. Open only the official domain `lagunabeachca-energovweb.tylerhost.net` from the deep link in the submission plan.
- Let the user sign in and complete SSO/MFA/passkeys. Never request, store, inspect, or replay credentials or session material.
- Confirm the visible account identity label with the user before starting records.
- If browser control is unavailable, stop at a `portal_ready` packet and copy/paste answer sheet. Do not claim submission.

## P1 - Duplicate and draft check

- Inspect the user's dashboard/search for drafts or open applications at the same address and portal type.
- Compare description/scope. Resume an unambiguous match.
- Show a possible duplicate and ask which record to use when scope is ambiguous.
- Never start another record because a prior browser turn timed out.

## P2 - Exact type

- Navigate with the deep link in `submission-plan.json`.
- Verify the visible catalog label, module, and category against `assets/portal-maps/v1-portal-map.json`.
- Stop if the type is removed, renamed, disabled, or moved.

## P3 - Wizard

At Location, Basic Info, Contacts, More Info, Attachments, and Signature/Submit:

1. Read the visible required fields and instructions.
2. Compare them to the pinned portal map.
3. Populate only submission-plan/project-fact values.
4. Re-read the effective value after entry.
5. Record the step/checkpoint locally.

Stop on a new field, changed wording, new validation, unsupported address, licence failure, or unanswered field. Do not guess. On MEP types, every entered count needs a source; no blanket zero-filling.

## P4 - Upload and verify

Authenticated type 114 verification (2026-09-09) found:

- Follow the full catalog URL `#/plan/apply/114/0/0`; the shortened `#/plan/apply/114` redirected home.
- Before opening a chooser, verify each absolute local path exists, is nonempty, and matches its packet hash. The browser bridge can produce a zero-byte file from a missing path. Reject any zero-byte attachment card.
- Selecting files creates cards; Next triggers the actual Saving Files transfer. Wait until it completes and the Signature step appears before reporting upload success.
- Tyler explicitly reports that attachments cannot be saved in a draft. On resumption, inspect and reattach the exact files; a saved project draft does not prove file persistence.
- Signature consent and an electronic signature are required before Review and Submit. A demonstration authorized only through uploads stops here without signing.


- Upload each exact local file to its mapped City category.
- Re-read category, filename, completion state, and file count.
- Where preview/download is exposed, verify the first and last page or hash/download receipt so an older same-named file is not mistaken for the current one.
- Enforce one-file slots. Do not silently replace a file.

## P5 - Pre-submit review

Show one compact manifest containing:

- every record about to be submitted;
- address, exact type, scope/description, and Building valuation;
- contacts and roles;
- uploaded filename/category/hash list;
- declarations and signature still required;
- payment, appointment, or later in-person issuance expectation;
- any unresolved warning.

Block submission for source/portal drift, duplicate ambiguity, scope mismatch, missing required upload, unconfirmed applicant-controlled fact, missing Building valuation, or failed upload verification.

## P6 - Signature and final approval

The user personally enters the V1 electronic signature/attestation. After the final manifest and signature, ask immediately before clicking Submit: `Submit these applications now: <record labels>?` Earlier preparation approval is not enough.

## P7 - Submit once and capture

- After explicit approval, click Submit once.
- Wait for the terminal confirmation.
- On timeout/ambiguous response, inspect dashboard/search before any retry.
- Capture status, record/application number if shown, exact type/scope, timestamp, visible account identity label, uploaded names/hashes, confirmation text, screenshot/page-state path where available, payment state, expected response, and in-person/appointment follow-up.
- Write schema-valid `submission-receipt.json` and human-readable `SUBMISSION-RECEIPT.md`.

Types 114, 182, 183, 186, 187, 188, and 214 generally enter a 2-3 business-day completeness screen followed by staff contact for payment. Most Building permits still require later in-person issuance.

## P8 - Payment and follow-up

Payment is a new transaction. Show invoice amount, record, fee description, and payment method; get separate approval; let the user enter credentials; capture a separate receipt. V1 may stop after successful application confirmation and record the invoice follow-up.

Appointment booking is also a transaction. Show the exact office/service/date/time and get explicit approval before booking.
