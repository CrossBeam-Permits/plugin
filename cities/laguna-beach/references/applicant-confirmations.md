# Applicant confirmations

## Never infer or silently enter

- signatures, initials, signer capacity, attestations, or sworn declarations;
- owner-builder status or authorization to act for an owner/contractor;
- valuation;
- contractor licence/class, Laguna business-licence status, or utility authorization;
- ownership, title, legal entity, authorized representative, or tenant assertions;
- a discretionary entitlement not established by the route analysis;
- appointment, final submission, or payment authorization.

## Four distinct action boundaries

1. **Filing theory:** user confirms the proposed application/record set before forms or portal drafts.
2. **Signature:** user personally enters V1 signatures/attestations after reviewing the final document/page. This includes signing the application PDF before it is uploaded.
3. **Final transaction:** immediately before Submit, name every record and ask explicit permission to submit now.
4. **Appointment/payment:** show exact appointment date/time/type or invoice amount/record/method, then get separate approval.

A prior request to “apply,” “fill it out,” or “take care of the permit” authorizes preparation, not these consequential actions.

## Owner-builder or licensed contractor

Laguna Beach issues a Building permit only to an owner-builder or a City-licensed contractor, and every business working in the city needs a Laguna Beach business license. [source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]. The Building Permit Application prints the same rule: all contractors, including subcontractors, need a City business license under LBMC 5.08.200.

Ask the applicant one direct question for every Building record: "Will this permit be pulled by the property owner as an owner-builder, or by a licensed contractor?" Record the answer as the fact `permittee.type` with value `owner_builder` or `licensed_contractor`, source `user_confirmed`, and a confirmed confirmation. The schema rejects any other source.

- Never derive it from a contractor name on plans, a title block, a letterhead, a portal contact, an email domain, or who is talking to you. Those are evidence to mention when you ask, not an answer.
- `fill-form.py` blocks the Building application until `permittee.type` is confirmed.
- On a `licensed_contractor` permit, the contractor block fills from confirmed contractor facts. Also ask for the contractor's Laguna business license: record `contractor.laguna_business_license.status` (`active`, `applied`, or `none`) and, when given, `contractor.laguna_business_license.number`. Subcontractors need one too. A `none` or unknown status does not block filing, but say plainly that the City will not issue the permit until the license exists.
- On an `owner_builder` permit, the contractor block stays blank. The City rejects an application that names both an owner-builder and a contractor. The owner-builder uploads the City's Property Owner's Package, government ID, and ownership documents; an agent filing for the owner needs the owner's authorization inside that package. [source: City e-permit and reroof guides, received 2026-08-12, quoted in `requirements/building/express-permits.md` rows `laguna_owner_builder_package`, `laguna_owner_builder_agent_authorization`, and `laguna_owner_builder_applicant_consistency`]
- Some permits do not issue to an owner-builder. Residential solar issues only to a licensed contractor [`requirements/building/solar.md` row `laguna_solar_no_owner_builder`]. Raise this before filing; it is an issuance condition, not an intake defect.
- If the answer changes, re-fill the form. Never edit a signed copy.

Portal note: the type 183 (Residential) and type 214 (Grading) portal forms list contact roles Applicant and Owner (required) plus Architect, Contractor, Designer, and Engineer. Neither has an Owner/Builder role. [source: EnerGov `energov/permits/setup` for both types, public GET, 2026-10-09]. The declaration therefore lives in the signed application and the attachments. How to enter the owner-builder on the portal screens belongs to `online-submission.md`.

## Signing the application before upload

The portal asks applicants to sign applications before uploading them. The applicant signs; the agent prepares and checks.

- After fill, verify, and render, show the applicant every page and name each signature line from the map's `signature_blocks`. The Building application has two: the page 1 SIGNATURE and DATE, and the Stormwater Quality Certification "Signed:" and "Date:" on page 2.
- Confirm who signs the stormwater certification. It is "the applicant authorizing construction activities". Record the certifier's name, address, phone, and email as confirmed facts; never assume the certifier is the owner.
- The applicant signs with a pen and scans, or uses their own e-signature tool. Never apply, draw, type, or paste a signature or initials, even when asked to, and never store a signature image.
- Run `scripts/verify-signed-form.py` on the signed file, look at the rendered pages and signature crops, and record the signed file's SHA-256 for the packet. See `form-source-policy.md`.

## Confirmation receipt

For a user answer, record timestamp, exact affected fact/action, and a short paraphrase in local state. Do not record passwords, MFA codes, payment data, or a signature image. If authorization is ambiguous, stop and ask.
