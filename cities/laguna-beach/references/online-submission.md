# Online submission gates

EnerGov filing is a resumable external transaction. Use visible labels and current page state, not screen coordinates or one brittle selector chain. Persist only non-secret state in `browser-state.json`.

## Driving the browser on any host

Gates P0-P8 are the same on every host. Use whatever user-visible browser control the host offers: a browser extension the agent drives, desktop computer use, an in-app browser, or a Playwright or other browser MCP server. None of these is required. Do not tell the user to install a particular one.

- Before P0, find out what the host can do in the user's browser: read the page, type, click, and attach a local file. Record these as capability flags in `browser-state.json`. Do not record tool names, tokens, or screenshots of private data.
- Work in small steps: read the page (text, accessibility tree, or a screenshot), act on one control, then read the result again. Do this every time on consequential controls.
- When the host can drive the page but cannot attach files (it blocks uploads or the native file dialog), stop at that upload card. Tell the applicant the exact card name, the exact local file name and folder, and the first 12 characters of its SHA-256. Ask them to click the card and pick the file in the dialog themselves. Then read the card again: the file name must match and the size must be nonzero. Never pick a different file to get past the card. (A fresh 2026-09-08 rehearsal hit exactly this: the browser bridge denied file upload; `docs/plans/PLAN-laguna-concierge-0908.md`, "DEMO-R3".)
- When the host has no user-visible browser control at all, stop at a `portal_ready` packet: the exact deep link, the work class to pick, a copy/paste answer sheet, and the files in upload order. Do not claim submission.
- The user signs in, completes any verification code or MFA, and enters payment details. See `portal-account.md`.

## One merged PDF per Plans card

The pinned map's upload rules come from the City's portal configuration (`NumberOfFilesAllowed`, `AllowedFileTypes`). On every mapped record type and work class, the `Plans`, `Application`, `Permit Application`, `ADU or JADU Application`, and Revision `Revised Plans` cards each take **one PDF file**. So the whole plan set goes up as one merged PDF per Plans card, and the signed application as one PDF per Application card. Merge with `scripts/assemble-packet.py` before hashing. The plan builder blocks a record that puts two files or a non-PDF file on a one-file card. Other cards (reports, technical studies, plan check responses) may take more files; follow the map.

## P0 - Browser and account

- Require a user-visible browser-control surface. Open only the official domain `lagunabeachca-energovweb.tylerhost.net` from the deep link in the submission plan.
- Let the user sign in and complete SSO/MFA/passkeys. Never request, store, inspect, or replay credentials or session material. If the user has no account yet, follow `portal-account.md`.
- Confirm the visible account identity label with the user before starting records.
- If browser control is unavailable, stop at a `portal_ready` packet and copy/paste answer sheet. Do not claim submission.

## P1 - Duplicate and draft check

- Inspect the user's dashboard/search for drafts or open applications at the same address and portal type.
- Compare description/scope. Resume an unambiguous match.
- Show a possible duplicate and ask which record to use when scope is ambiguous.
- Never start another record because a prior browser turn timed out.

## P2 - Exact type and work class

- Navigate with the deep link in `submission-plan.json`. Use the full catalog URL ending `/0/0`; the shortened `#/plan/apply/114` redirected home in the 2026-09-09 test.
- Verify the visible catalog label, module, and category against `assets/portal-maps/v2-portal-map.json`.
- The submission plan names the work class the user confirmed. Where the wizard shows a work class choice, select that class by its visible label and read the selection back. Then check that the More Info step shows the planned layout's question groups.
- How the Building wizard presents the work class has not been observed; only type 114 has been driven signed in. If the wizard does not offer the planned class, or fixes a different one, stop that record. Do not choose the nearest-sounding class.
- Stop if the type or work class is removed, renamed, disabled, or moved.

## P3 - Wizard

At Location, Basic Info, Contacts, More Info, Attachments, and Signature/Submit:

1. Read the visible required fields and instructions.
2. Compare them to the pinned portal map for the planned work class.
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
- If the host cannot attach files, use the applicant-picks-the-file step above. It is the same gate: the card must show the planned file before you continue.

## P5 - Pre-submit review

Show one compact manifest containing:

- every record about to be submitted;
- address, exact type, work class, scope/description, and Building valuation;
- contacts and roles;
- uploaded filename/category/hash list;
- declarations and signature still required;
- payment, appointment, or later in-person issuance expectation, including whether the work class is Pay First;
- any unresolved warning.

Block submission for source/portal drift, duplicate ambiguity, scope mismatch, missing required upload, unconfirmed applicant-controlled fact, missing Building valuation, unconfirmed work class, or failed upload verification.

## P6 - Signature and final approval

The user personally enters the V1 electronic signature/attestation. After the final manifest and signature, ask immediately before clicking Submit: `Submit these applications now: <record labels>?` Earlier preparation approval is not enough.

## P7 - Submit once and capture

- After explicit approval, click Submit once.
- Wait for the terminal confirmation.
- On timeout/ambiguous response, inspect dashboard/search before any retry.
- Capture status, record/application number if shown, exact type/work class/scope, timestamp, visible account identity label, uploaded names/hashes, confirmation text, screenshot/page-state path where available, payment state, expected response, and in-person/appointment follow-up.
- Write schema-valid `submission-receipt.json` and human-readable `SUBMISSION-RECEIPT.md`. Then continue with `after-filing.md`.

Types 114, 182, 183, 186, 187, 188, and 214 generally enter a 2-3 business-day completeness screen followed by staff contact for payment. Most Building permits still require later in-person issuance.

## P8 - Payment and follow-up

Payment is a new transaction. Show invoice amount, record, fee description, and payment method; get separate approval; let the user enter credentials; capture a separate receipt. V1 may stop after successful application confirmation and record the invoice follow-up.

A Pay First work class (for example the 183 Revision class, or the 187 panel class up to 400 A) asks for fees as part of filing. The same rule applies there: stop at the fee step, show the amount and fee lines, and get a separate approval before the user pays. Submit approval does not cover payment.

Appointment booking is also a transaction. Show the exact office/service/date/time and get explicit approval before booking.
