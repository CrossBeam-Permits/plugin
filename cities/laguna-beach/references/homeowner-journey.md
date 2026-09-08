# Homeowner journey: from “we want a pool” to the City's next action

Own the work across exchanges. Give a short progress update in plain language, perform
the next available preparation step, and ask only for facts that cannot be extracted.
Do not turn the application into a long questionnaire or stop at a generic checklist.

For a first-time idea with no files, keep the first reply to a short explanation of the
help available and at most three brief questions about the address, proposed scope, and
available files/review history. Mention drafting inputs in one sentence. Do not front-load
the ordinance tables, equipment tests, schemas, approval gates, or two batches of intake.
Investigate the technical routing facts after obtaining the address and available evidence.

## Start with the project, plans, and review history

Ask for the address, scope, and any existing plans/review correspondence. Establish pool
height above adjacent legal grade (not water depth), spa type/capacity, equipment location,
and coastal/bluff conditions through the cited Planning routing reference. Unknown site
facts remain unknown; do not ask a homeowner to certify a technical determination.

Ask: “Do you have drawings yet, and has the City or a private plan reviewer reviewed
this version?” Read any answer and attached reports before asking more questions.

Record review facts under `review.*`: reviewer, review kind, date, report file, plan
revision/sheet index, record number, unresolved corrections, and approval/effective date.
Keep private pre-check, City completeness screening, Planning approval, Building plan
check, and issued permit distinct. A CrossBeam pre-check does not establish City approval
or waive City review. Do not call a private pre-check mandatory without a current City
source requiring it. If requested, use the host's available CrossBeam connection or
verified public interface; do not invent a review tool or claim a review ran.

For each prerequisite in `application-set.json`, use the ID of a sourced Boolean fact,
for example `planning.approval_effective`. The model determines its value from the cited
evidence; the compiler only checks that it is usable and true. An application set may be
confirmed while a future Building record remains `prerequisite_pending`. Preparation can
continue locally; that record must not be described as portal ready.

## Prepare drawings when requested

Inventory the required sheets from the current official application and the relevant
scope skill. Create a sheet register in `permit-work/state/drawing-register.md` recording
each sheet, source inputs, revision, author/reviewer, missing inputs, and readiness.

Offer to draft a cover sheet, project description, source-based site layout, schedules,
equipment notes, or a corrections index when the available drafting/file tools support
them. Generate editable source and a rendered PDF, and inspect the output. Label sheets
with unresolved technical inputs “DRAFT — NOT FOR CONSTRUCTION OR SUBMITTAL.”

For a pool, identify evidence needed for property boundaries/easements, legal grades,
setbacks, pool/spa dimensions, grading/drainage, structure, equipment, utilities, and
barriers. Use measured/surveyed inputs for scale and dimensions. Do not manufacture a
survey, structural design, geotechnical conclusion, professional seal, or signature.
Ask the responsible professional for missing technical work and make a precise handoff
listing the needed sheet/calculation. Preserve the original approved plans; changing a
design requires checking whether the approval still covers it.

A conceptual drawing is useful progress. It is not evidence that a required plan sheet
is complete. Exclude unfinished sheets from upload packets until the required inputs and
review are resolved. If drafting tools are unavailable, deliver the sheet brief and say
which drawings still need production.

## Build and review the complete packet

Read the current official application checklist, scope skill, and any City conditions.
For each required item record source/locator, applicability reasoning, supporting file
and revision, status, and unresolved issue in `permit-work/state/readiness.md`. Distinguish
missing documents from documents present but incomplete. Portal “optional” does not waive
an applicable City requirement. Include the pool/equipment, soils, grading, drainage,
barrier, and energy/electrical details actually triggered by the evidence.

Fill the current official forms from the fact table; render and inspect each used page.
Present remaining applicant declarations/signatures in one review handoff. A populated
field count is a form-mapping test, not a completeness determination.

## File and continue the existing case

Use the real route and `online-submission.md`. If the current City source page, application
PDF, and portal disagree about the channel, record all three receipts and get the exact
City route clarified before creating a record. Do not guess a portal type to keep moving.

After filing, save the confirmation and actual record number. Record invoice state,
requested response, deadlines from the City notice, and the next responsible person in
`permit-work/state/next-actions.md`. Do not infer a statutory deadline from a generic
estimate or call an invoice “paid” without payment evidence.

When asked to check back, use the host's scheduling tools if available; otherwise explain
that automatic monitoring is not active. Follow the requested notification frequency.
For corrections, read the complete letter, create an item-by-item response with revised
sheet/page references, flag items requiring the designer, and resubmit to the existing
record. Apply the same signature, payment, and final-submit boundaries on resubmittal.

Finish with the observed City status. “Submitted,” “complete,” “approved,” and “issued”
are different milestones. If issuance requires the counter, prepare the exact handoff.

## Demonstration standard

A synthetic demonstration runs locally and displays “DEMONSTRATION — NOT SUBMITTED.”
Never create a City record, signature, payment, or fake receipt for it. A real filmed
submission needs a consenting applicant, their actual complete packet, an authorized
account, personal signature entry, and record-specific final approval. Hide private
contact details and credentials from the recording. End a filing video on the actual
receipt; do not describe it as an issued permit unless issuance is verified.
