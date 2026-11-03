# Submit: Sign Permit — EnerGov type 197

The building permit for a sign. It is the **lightest application in the whole
Laguna Beach catalog**: one required attachment, no intake questions at all, and
a wizard you can finish in a sitting.

Note what this type is *not*. Planning runs its own **Sign Permit Review** as a
separate internal case type, so a sign that needs planning sign-off is a second
filing — see `planning-applications.md`, and `submit-commercial-permit.md` for
the building side of a storefront job. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/search, as of 2026-08-10]
If the sign needs its own branch circuit, that is electrical work; the Electrical
Permit's count sheet has a "Sign /Marquees: (One branch circuit)" field — see
`submit-electrical.md`. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/187/0/0, as of 2026-08-10]

**Apply:** https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/197/0/0 (portal account required)
**Catalog name, verbatim:** "Sign Permit" — category SIGN, module PERMITS.
**Catalog description, verbatim:** "This application is for a Sign Permit. \*PLEASE BE ADVISED THAT THE FINAL PERMIT ISSUANCE IS CONDUCTED IN PERSON AT THE BUILDING COUNTER."

Unless noted otherwise, everything below is the City's own configuration of this
application, read from the portal. The apply URL is login-gated in a browser;
the mirrored pull is the City source document (not included in this plugin).
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/197/0/0, as of 2026-08-10]

## Before you start

- **A signed permit application.** The only required attachment on this type is "Permit Application", described by the City simply as "Building Application". Sign it before you upload.
- **Plans are optional here.** The City's written instruction says "Project plans (if applicable)", and the Plans slot on this type is configured as optional. That is unusual — on Grading (214) and Residential (183) it is required.
- **A portal account.** See `how-to-submit.md` → "Before any of this".
- *Our note, not the City's:* the Planning Division publishes its own [Sign Permit application form](https://www.lagunabeachcity.net/home/showpublisheddocument/26375/639192070419070000), and the City publishes a [Sign Brochure](https://www.lagunabeachcity.net/home/showpublisheddocument/12310/637952216925200000). Neither is a portal requirement on this building-permit type; both are worth reading before you draw the sign. See `planning-applications.md` and `forms-index.md`. [source: https://www.lagunabeachcity.net/government/departments/community-development/planning-zoning/applications-handouts, as of 2026-08-09]

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/197/0/0, as of 2026-08-10]

## The wizard, step by step

**1 — Location.** "ATTENTION: This application is for a SignPermit only" (the
City's own text, missing the space). Click **+**, type the address of the primary
residence into the search field, select it once results populate; if it is not
found, click **Enter Manually**. Address is required.

**2 — Basic info.** Description is required, and the City asks for a "detailed
scope of work" — a "comprehensive explanation of the work you plan to do" that
**matches your plans**. Note the City's field warning, verbatim: "\*\* Square
Footage is for office use only. Do Not use." Square footage and valuation are
not required on this type.

**3 — Contacts.** Click **+** to search by person or business name, select the
result and click **Add**; if not found, **Enter Manually**. The City lists:
**Applicant** and **Owner** (required), plus **Contractor**, **Architect/Designer**,
and **Engineer**, each "(If applicable)".

**4 — More info.** Nothing to fill in. The step carries only the City's note that
"Helpful forms can be found on the City's website" —
[Building Applications & Forms](https://www.lagunabeachcity.net/government/departments/community-development/building-permits/applications-forms).

**5 — Attachments.** Signed application; project plans if applicable. See below.

**6 — Signature and submit.** An electronic signature is required.

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/197/0/0, as of 2026-08-10]

## The questions you will face (0 fields)

**None.** This type has no custom-field groups configured at all — no fixture
counts, no acknowledgements, no declarations. The More Info step exists but asks
nothing. Everything the City learns about the sign, it learns from your
description and your plans, which is a good argument for writing both carefully.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/197/0/0, as of 2026-08-10]

## Required attachments

One, PDF, one file:

| Attachment | The City's description |
|---|---|
| Permit Application | Building Application |

The City's written instruction on this step names something different from the
required slot: "Applicants must submit the following: Project plans (if
applicable)" — plans, hedged, and no mention of the application. Read together:
the application is the hard requirement, the plans are the expected-but-optional
addition. The rest of the instruction, condensed: submit all required documents
to avoid delays — an incomplete application draws a correction request *before*
the plans are reviewed at all.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/197/0/0, as of 2026-08-10]

## Optional attachment slots worth knowing

Eight more categories exist on this type, all PDF unless noted, unlimited files
unless noted:

- **Plans** — "Project Plans for Reviews", one file. Optional on this type, but the City's instruction asks for it "if applicable" and a sign is a drawing-driven review. Volunteer it: elevation, dimensions, mounting, and the sign in context on the façade.
- **Specification Sheets** — "Project Specification Sheets". Materials, illumination, and cabinet details.
- **Plan Check Responses** (.doc/.docx/.pdf/.jpg/.jpeg) — where you upload your answers to a correction letter on a resubmittal.
- **Revision Form** — for a change after the permit exists. The slot's description is now a link to the Building Division's Applications & Forms page, https://www.lagunabeachcity.net/government/departments/community-development/building-permits/applications-forms, which is where the portal points you for the form. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/197/0/0, attachment setup read through the portal's public API, as of 2026-10-26]
- **Energy Calculations** and **Energy Calculation Addendum** — Title 24; relevant only if the scope triggers it.
- **Mechanical Equipment Guide** — the slot is inherited from the City's standard file set; its "REQUIRED FOR ALL A/C PERMITS BY PLANNING" instruction is written only on the Mechanical Permit (186) and has nothing to do with a sign.
- **Miscellaneous** (.pdf/.tif/.tiff/.jpeg/.jpg/.png) — photos of the existing façade go well here.

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/197/0/0, as of 2026-08-10]

## Contacts and licences

- Required: **Applicant, Owner**. Optional: Architect, Contractor, Designer, Engineer — a shorter list than the MEP types carry (no Agent, Owner/Builder, Subcontractor, or Tenant slots).
- **Contractor entries are licence-validated** by the portal.
- Permits issue only to an owner-builder or a **City-licensed** contractor, and every business working in the city needs a Laguna Beach business licence. [source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/197/0/0, as of 2026-08-10]

## After you submit

The City's confirmation message, verbatim:

> Thank you for your Sign Permit application. A permit technician will review
> your application to ensure all required information has been submitted, and
> contact you in 2 - 3 business days for payment.

So submitting does not start plan check — a technician screens it for
completeness first, then invoices. **And the permit itself is not issued
online.** This type carries the City's warning, verbatim: "\*PLEASE BE ADVISED
THAT THE FINAL PERMIT ISSUANCE IS CONDUCTED IN PERSON AT THE BUILDING COUNTER."
Plan on a counter trip to 505 Forest Ave at the end.

**On fees:** this is one of only two types in the entire catalog with **fee
estimation enabled in the back end** — the other is Grading (214). Do not
promise a resident an estimator: **no fee estimator is surfaced anywhere in the
portal.** It is back-end configuration, not a feature you can use. Fees are
quoted by staff after review. For a current amount, call the fee estimate; do
not quote figures from `fees.md`.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/197/0/0, as of 2026-08-10]
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/home, as of 2026-08-10]

## Next step

> **Next step:** file a Sign Permit in the City's permit portal —
> [Sign Permit (type 197)](https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/197/0/0).
> The signed application is the only required upload; add your sign drawings under the optional **Plans** slot anyway.
> Forms live on the [Building Applications & Forms page](https://www.lagunabeachcity.net/government/departments/community-development/building-permits/applications-forms).
> You'll need a portal account first — [registration guide](https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000).
> Questions: Building Division (949) 497-0715; sign design questions, Planning (949) 497-0713.
