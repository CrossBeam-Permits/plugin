# After filing

Filing is the start of the City's process, not the end. Keep the same record, the same receipt file, and the same distinctions: **submitted**, **received** (fee paid where the City requires it), **complete**, **approved**, and **issued** are different milestones. Never call a record more than the portal or a City document shows.

The receipt lives in `permit-work/output/receipts/<record-id>/submission-receipt.json` (schema `schemas/submission-receipt.schema.json`, version 1.1.0) with a readable `SUBMISSION-RECEIPT.md` beside it. Every step below adds to that one receipt.

## 1. Capture the receipt at the confirmation

Right after the terminal confirmation (`online-submission.md` P7), record:

- the record or application number exactly as shown, or `null` if none is shown;
- the confirmation text, word for word;
- the timestamp in UTC, plus the local time the user saw;
- the visible account identity label (not the email if the label is enough);
- the record type, work class, and filing behavior from the submission plan;
- every uploaded file: name, portal category, SHA-256;
- a page-state receipt path (screenshot or saved text) with credentials, payment fields, and other people's contact details kept out.

The City's configured messages say a permit technician (Building) or planner (Planning) will screen the submittal and contact the applicant in 2-3 business days for payment (`submitSuccessMessage` in `assets/portal-maps/v2-portal-map.json`). Write that as `expected_city_response`. If the portal showed anything else, record what it showed.

A saved draft is not a submission. Use `status: "saved_draft"` and say so.

## 2. Fee invoice

- **Review First** classes: after the completeness screen, staff contact the applicant for payment (City success messages). The invoice appears on the record's Fees tab, which only a contact on the record can see (`portal-account.md`), or arrives by email.
- **Pay First** classes (the 183 Revision class; the 187 panel class up to 400 A): the portal asks for fees during filing.
- **Zone Clearance:** the official form says an application is deemed received only after submission **and** payment of the Zoning Plan Check fee (`planning-routing.md`). A submitted, unpaid Zone Clearance is not received.

When an invoice appears, add it to `invoices` exactly as shown: source (portal, email, letter, counter), invoice number, each fee line, total, due date. Unknown values stay `null`. Set `payment_state` to `pending_invoice`. Do not quote fees from memory or estimate them.

**Paying needs a separate, explicit approval.** Show the record, invoice number, fee lines, total, and payment method, then ask: `Pay <total> for <record> now?` Approval to submit, or an earlier "take care of it", does not cover payment. The user enters card or bank details themselves; never store, read back, or log them. After payment, add a `payments` entry (approval time, paid time, amount, portal receipt number) and set `payment_state` to `paid` only when the portal or a City receipt shows it paid.

## 3. Status checks

When the user asks for a status check, or a check-back they scheduled comes due:

1. The user signs in. Open the record from the dashboard, not by searching for a new one.
2. Read the status, the current workflow step, and any review results shown. Public record pages show the summary and workflow steps; fees, reviews, and attachments need a contact on the record.
3. Add a `status_checks` entry with what the page says, word for word where it matters.
4. Tell the user the observed status and the next action in one or two sentences. Do not infer approval from silence or elapsed time.

If the host can schedule follow-ups, use it at the frequency the user asked for. If it cannot, say that automatic monitoring is not active.

## 4. Corrections letters

1. Find the letter on the record (Reviews or Attachments tab, or the City's email). Download it in the user's browser. The user does any sign-in.
2. Save it under `permit-work/input/city/`, hash it, and add a `city_documents` entry with `kind: "corrections_letter"`.
3. Read the whole letter. Build the item-by-item response in `homeowner-journey.md` style: each comment, the sheet or document that answers it, and who must do the work. Flag items that need the designer, engineer, or another professional. Do not invent technical answers.
4. Track what is still open in `permit-work/state/next-actions.md`.

## 5. Resubmittal

- Resubmit to the **existing record**. Never start a new application to answer corrections.
- Use the response and revised-document categories the map lists for the record's work class (for example `Building Plan Check Response`, `Planning Plan Check Response`, `Plan Check Responses`, `Revised Permit Application`, `Revised Structural Calculations`). The revised plan set is still one merged PDF.
- How the portal starts a resubmittal on an existing Building record has not been observed. If no resubmit or upload action is visible on the record, stop and ask the City; do not use the Revision work class instead.
- The Revision work class is only for revising details of work already approved and permitted (`building-routing.md`). It is Pay First.
- The same gates apply: duplicate check, upload verification, the user's own signature, and a fresh `Submit these applications now: ...?` before the click. Add a `resubmittals` entry with the confirmation text and files.

## 6. Issuance in person

The catalog descriptions for types 183, 186, 187, 188 and 214 say: "PLEASE BE ADVISED THAT THE FINAL PERMIT ISSUANCE IS CONDUCTED IN PERSON AT THE BUILDING COUNTER" (v2 map, `catalogDescription`). Planning types 114 and 182 carry "THIS IS NOT A BUILDING PERMIT".

When the City says a permit is ready to issue:

- Record `issuance.status: "ready_for_issuance"` with the date and the City's words.
- Prepare a counter handoff: record number, work class, what to bring. The City issues to an owner-builder or a City-licensed contractor, and businesses working in the city need a Laguna Beach business licence (`portal-account.md` source 1, line 169). Owner-builder status and licences are applicant declarations; never fill them in.
- The Building counter is at City Hall, 505 Forest Avenue. The City publishes more than one set of counter hours; tell the user to check the City's current hours before going. Appointment booking is its own approval (`online-submission.md` P8).
- Mark `issued` only when the user has the issued permit or the portal shows it issued, and add the permit document to `city_documents` if they share it.

## Sources

- City success messages, catalog descriptions, Revision instructions, and upload categories: City public portal API read 2026-10-09, pinned in `assets/portal-maps/portal-snapshot.json` and `v2-portal-map.json`.
- Fees/Reviews/Attachments visible only to a contact on the record; public summary and workflow steps; counter address; owner-builder or City-licensed contractor and business licence at issuance; more than one published set of hours: CrossBeam private `skills/cities/laguna-beach/website/references/how-to-submit.md` lines 16, 129, 169, 176 and `data/cities/laguna-beach/portal/ui-walk/login-wall.md` (captured 2026-08-10).
- Zone Clearance deemed-received condition: `references/planning-routing.md`, "Channel correction verified 2026-09-08".
