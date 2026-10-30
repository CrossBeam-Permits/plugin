# Submit: Fire Residential Permit — EnerGov type 190

The fire-protection permit on the residential side of the catalog — the type
`how-to-submit.md` routes **residential fire sprinklers** to. It is the shortest
application in the catalog: address, description, contacts, two files, sign.

**Apply:** https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/190/0/0 (portal account required)
**Catalog name, verbatim:** "Fire Residential Permit" — category RESIDENTIAL, module PERMITS.
Its catalog description, verbatim: "This application is for a Fire Residential Permit."

The City does not publish a scope list for this type — that one sentence is the
whole description. If your scope is anything other than residential fire
protection, check the router in `how-to-submit.md` before you file; general
residential work is a **Residential Permit (183)**, `submit-residential-permit.md`.

Unless noted otherwise, everything below is the City's own configuration of this
application, read from the portal. The apply URL is login-gated in a browser;
the mirrored pull is the City source document (not included in this plugin).
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/190/0/0, as of 2026-08-10]

## Before you start

- **Download and sign the Building Permit Application** before you start: http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf — this type asks for the same signed form as every other building permit, and the City requires it signed before upload.
- **Have the plans as a single PDF.** The Plans slot takes one file.
- **Commercial building?** File **Fire Commercial Permit (191)** instead — see `submit-fire-commercial.md`.
- **A portal account.** See `how-to-submit.md` → "Before any of this".

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/190/0/0, as of 2026-08-10]

## The wizard, step by step

Five steps, not six — this type has **no More info step**.

**1 — Location.** "ATTENTION: This application is for a Fire Residential Permit
only." Click **+**, type the address of the primary residence into the search
field, select it from the results; if it is not found, click **Enter Manually**.
Address is required.

**2 — Basic info.** Description is required, and the City asks for a
"comprehensive explanation of the work you plan to do" that **matches your
plans**. Note the City's own field warning, verbatim: "\*\* Square Footage is
for office use only. Do Not use."

**3 — Contacts.** Click **+** to search by person or business name, then **Add**;
if not found, **Enter Manually**. The City lists: **Applicant** and **Owner**
(required), plus **Contractor**, **Architect/Designer**, and **Engineer** "if
applicable".

**4 — Attachments.** Signed application + plans. See "Required attachments".

**5 — Signature and submit.** An electronic signature is required.

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/190/0/0, as of 2026-08-10]

## The questions you will face

**None.** This type carries **zero** intake questions — there is no More info
step and no fixture count sheet. The wizard goes straight from Contacts to
Attachments. That is a real difference from the Residential (183) and Commercial
(184) permits, which each ask 113 MEP count fields.

Practically: nothing in this form captures your device counts, so **the
description and the plans are the only place the scope gets stated.** Write the
description accordingly.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/190/0/0, as of 2026-08-10]

## Required attachments

Two, both PDF, one file each:

| Attachment | The City's description |
|---|---|
| Permit Application | Building Application — the signed [Building Permit Application PDF](http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf) |
| Plans | Project Plans for Reviews |

The City's written instruction on this step, condensed: submit all required
documents to avoid delays — an incomplete application draws a correction request
*before* the plans are reviewed at all — applicants must submit the Building
Permit application and project plans, and **sign applications before uploading**.
Additional applications and forms are on the [City's forms page](https://www.lagunabeachcity.net/government/departments/community-development/building-permits/applications-forms).

Note the difference from type 183: this type's attachment instruction **does not**
carry the Mechanical Equipment Guide line. The guide's upload slot still exists
below (see next section) — the City just does not call it out here.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/190/0/0, as of 2026-08-10]

## Optional attachment slots worth knowing

39 more categories exist on this type — the City gave it the **same 41-slot file
set as the Residential and Commercial permits**, so several slots are plainly
inherited boilerplate rather than fire-specific asks. The ones most likely to
matter here:

- **Specification Sheets**, **ESR Sheet**, **Installation Manual** — product listings and data sheets for the equipment being installed.
- **Fabrication or Shop Drawings** — where shop drawings go.
- **Fuel Modification or Fire Study** — Laguna is a very-high fire hazard severity zone city.
- **Hydraulic/structural backup:** **Structural Calculations** (and the addendum), **Revised Structural Calculations**.
- **Fire Plan Check Response** and the general **Plan Check Responses** slot — where you upload your answers to a correction letter on a resubmittal. Per-division response slots also exist for Building, Planning, Public Works, and Water Quality.
- **Revision Form** and **Revised Permit Application** — for changes after submittal. The Revision Form slot's description is now a link to the Building Division's Applications & Forms page, https://www.lagunabeachcity.net/government/departments/community-development/building-permits/applications-forms, which is where the portal points you for the form. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/190/0/0, attachment setup read through the portal's public API, as of 2026-10-26]
- **Health Approval** and **Hydrant Flow Report** — two slots the City added between 2026-10-19 and 2026-10-26. Both are optional, and the portal describes each only by its name. Two City rules use the same names. A project with a fire sprinkler system needs an LBFD Hydrant Flow Report from a water-purveyor flow test no more than 6 months old (LBMC Title 15 §15.01.070, amending NFPA 13 §28.1.3). A project with a food operation or another Environmental Health-regulated use needs Orange County Environmental Health approval (the City's 2026 building issuance-requirements checklist). The portal does not tie either slot to those rules, so ask the Building Division, (949) 497-0715, before telling an applicant a slot is required. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/190/0/0, attachment setup read through the portal's public API, as of 2026-10-26]
- **Miscellaneous** — the catch-all; it is the only slot that also takes images.
- Inherited-boilerplate slots you can ignore unless they genuinely apply: **Roof Material Color Swatch**, **Mechanical Equipment Guide**, **WQMP**, **WELO Calculations/Report**, **Grading Plans**, **Survey**, **Energy Calculations**, **Asbestos Report**.

Most accept PDF only; the response slots also take .doc/.docx/.jpg/.jpeg, and
Miscellaneous takes .tif/.tiff/.jpeg/.jpg/.png.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/190/0/0, as of 2026-08-10]

## Contacts and licences

- Required: **Applicant, Owner**. Optional: Architect, Contractor, Designer, Engineer.
- **Contractor entries are licence-validated** by the portal.
- Permits issue only to an owner-builder or a **City-licensed** contractor, and every business working in the city needs a Laguna Beach business licence. [source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/190/0/0, as of 2026-08-10]

## After you submit

The City's confirmation message on this type is, verbatim:

> Thank you for your Commercial Permit application. A permit technician will
> review your application to ensure all required information has been submitted,
> and contact you in 2 - 3 business days for payment.

**Yes, it says "Commercial Permit" on a residential type.** That is the City's
own copy-paste in the portal configuration, not a sign that you filed the wrong
application. The substance is what matters: submitting does not start plan check
— a technician screens it for completeness first, then invoices.

**And the permit itself is not issued online.** This type carries the City's
warning, verbatim: "\*PLEASE BE ADVISED THAT THE FINAL PERMIT ISSUANCE IS
CONDUCTED IN PERSON AT THE BUILDING COUNTER." Plan on a counter trip to
505 Forest Ave at the end.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/190/0/0, as of 2026-08-10]

## Next step

> **Next step:** file a Fire Residential Permit in the City's permit portal —
> [Fire Residential Permit (type 190)](https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/190/0/0).
> Have the signed [Building Permit Application](http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf) and your plans ready as PDFs.
> You'll need a portal account first — [registration guide](https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000).
> Questions: Building Division (949) 497-0715.
