# Submit: Mixed Use Permit — EnerGov type 374

The building permit for **buildings that combine residential and non-residential
use** — the mixed-use sibling of the Residential (183), Commercial (184), and
Multifamily (322) permits. Same wizard, same 39-slot file set, same 113-field MEP
count sheet; what differs is the category and the contact configuration (see
"Contacts and licences", the one real trap here).

**Apply:** https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/374/0/0 (portal account required)
**Catalog name, verbatim:** "Mixed Use Permit" — category MIXED USE, module PERMITS.
Its catalog description, verbatim: "This application is for a Mixed Use Building Permit."

Unless noted otherwise, everything below is the City's own configuration of this
application, read from the portal. The apply URL is login-gated in a browser;
the mirrored pull is the City source document (not included in this plugin).
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/374/0/0, as of 2026-08-10]

## Before you start

- **Does planning review come first?** Mixed-use work that changes the exterior, the use mix, or the unit count generally needs a planning entitlement first — a separate, earlier filing. The portal offers no triage to tell you whether you need it; confirm with Planning, (949) 497-0713, and see `submit-commercial-planning-entitlements.md`. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/116/0/0, as of 2026-08-10]
- **Purely residential building?** Use **Multifamily Permit (322)** — `submit-multifamily.md`. **Purely commercial?** Use **Commercial Permit (184)** — `submit-commercial-permit.md`. This type is for the building that is both. Fire sprinklers are their own type, 190 or 191 — `submit-fire-residential.md`, `submit-fire-commercial.md`.
- **Download and sign the Building Permit Application** before you start: http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf — the City requires it signed before upload.
- **A/C in scope?** The **Mechanical Equipment Guide** is, in the City's capitals, "REQUIRED FOR ALL A/C PERMITS BY PLANNING": https://www.lagunabeachcity.net/home/showpublisheddocument/9959/638586590648770000 You also need **a portal account** — see `how-to-submit.md` → "Before any of this".

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/374/0/0, as of 2026-08-10]

## The wizard, step by step

**1 — Location.** "ATTENTION: This application is for a Mixed Use Permit only."
Click **+**, type the address into the search field, select it from the results;
if it is not found, click **Enter Manually**. Address is required. (The City's
instruction text says "the primary residence" here — boilerplate carried over
from the residential form; enter the building's address.)

**2 — Basic info.** Description is required, and the City asks for a
"comprehensive explanation of the work you plan to do" that **matches your
plans**. On a mixed-use building, say which portions the work touches. Note the
City's own field warning, verbatim: "\*\* Square Footage is for office use only.
Do Not use."

**3 — Contacts.** Click **+** to search by person or business name, then **Add**;
if not found, **Enter Manually**. The City's written instruction lists
**Applicant** and **Owner** under "Required Contacts", plus **Contractor**,
**Architect/Designer**, and **Engineer** "if applicable" — but the form itself
does not enforce any of it. See "Contacts and licences".

**4 — More info.** "Please enter the number of items each for Electrical,
Mechanical, and Plumbing if applicable." See the next section.

**5 — Attachments.** Signed application + plans. See "Required attachments".

**6 — Signature and submit.** An electronic signature is required.

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/374/0/0, as of 2026-08-10]

## The questions you will face (113 fields, 3 groups)

This is **not** a questionnaire about the project — it is the fixture count sheet
that drives the itemized MEP fees, identical to the one on types 183, 184, and
322. Three groups, all optional, all numeric:

| Group | Fields | Examples |
|---|---|---|
| Electrical | 41 | outlets/switches, light fixtures, device boxes, panels and sub-panels by amperage band, services/meters/switchboards, generators/motors by HP band, sign/marquee branch circuits, pedestal meters |
| Mechanical | 34 | F.A.U. above/below 100K BTU, air conditioner or heat pump by tonnage, air handling units by CFM, VAV boxes, hood or canopy, residential and commercial exhaust systems, boilers/compressors by HP band, fire/smoke dampers |
| Plumbing | 38 | kitchen and bathroom sinks, shower/tub, toilet/water closet/urinal, floor sinks and drains, grease interceptor/trap, water heater (standard, tankless, new vent), backflow devices, gas piping per outlet |

The list is one flat sheet — it does not separate the residential portion from
the commercial one, so count everything in scope together, only what you are
actually installing, and leave the rest blank. The City bills MEP as separate
itemized fees, so these numbers become money.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/374/0/0, as of 2026-08-10]
[source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]

The City added a separate online work class to this type in September 2026:
**"Revision"** (template "Building Permit - Revision", portal filing behavior
"Pay First"). It is not on the portal's apply menu. Its intake sheet has a
"Revison" group (the City's spelling) with a required **Revision Number** field
and an optional **Additional Valuation** field, followed by the Mechanical and
Plumbing count sheets. The City changed it in early October 2026: the
Electrical count sheet was removed from the revision intake, a project
**address is now required**, and the portal's permit search list now shows it as
"Mixed Use Revision Permit". As of 2026-10-05 no other building permit type
(Residential 183, Commercial 184, Multifamily 322) had this work class. To
revise an issued mixed-use permit, or if you cannot find the revision path in
the portal, call the Building Division, (949) 497-0715.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService (permit application intake questions and setup), as of 2026-10-05]

## Required attachments

Two, both PDF, one file each:

| Attachment | The City's description |
|---|---|
| Permit Application | Building Application — the signed [Building Permit Application PDF](http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf) |
| Plans | Project Plans for Reviews |

The City's written instruction, condensed: submit all required documents to
avoid delays — an incomplete application draws a correction request *before* the
plans are reviewed at all — and **sign applications before uploading**. The same
step repeats the Mechanical Equipment Guide line for A/C work.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/374/0/0, as of 2026-08-10]

## Optional attachment slots worth knowing

37 more categories exist on this type — the same set as 183, 184, and 322. The
ones that carry a real Laguna requirement or commonly decide whether a submittal
is complete:

- **Mechanical Equipment Guide** — "REQUIRED FOR ALL A/C PERMITS BY PLANNING". Optional slot, mandatory content.
- **Structural Calculations**, **Soils Report or Geotechnical Report**, **Survey** — the standard trio on additions, new structures, and anything on a slope. **Energy Calculations** (and the addendum) cover Title 24.
- **Specification Sheets**, **ESR Sheet**, **Installation Manual**, **Fabrication or Shop Drawings** — product substantiation, asked for often on the commercial portion.
- **WQMP**, **WQ LID Checklist**, **WELO Calculations/Report**, **Hydrology Report** — water quality and landscape efficiency; expected on projects at this scale.
- **Grading Plans**; **Address Assignment Request** when new units or suites need addresses; **Fuel Modification or Fire Study** (Laguna is a very-high fire hazard severity zone city); **Asbestos Report** and **Asbestos Clearance Certification** on demolition or older-building work.
- **Roof Material Color Swatch** — the City's own note: "REQUIRED FOR REROOF PERMITS. Please circle or otherwise clearly indicate the exact color you are using." On a reroof, treat it as required.
- **Plan Check Responses** and the per-division response slots (Building, Fire, Planning, Public Works, Water Quality) — where you upload your answers to a correction letter on a resubmittal.
- **Plans: Reference Only Digitized Paper (NO REVIEW)** — exactly what it says; do not put review plans here. Most slots accept PDF only; the response slots also take .doc/.docx/.jpg/.jpeg, and Miscellaneous takes images.

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/374/0/0, as of 2026-08-10]

## Contacts and licences

**This type has no required contacts.** All 22 contact types on it are optional,
including Applicant and Owner — a real difference from the Residential (183) and
Commercial (184) permits, which both require Applicant and Owner. The City's own
on-screen instruction still says "Required Contacts: Applicant, Owner", so **the
portal does not enforce a required contact on this type; still list Applicant and
Owner.** A second reason to: on the public side you must be logged in *and*
listed as a contact on a record to see its Fees, Reviews, Attachments, Contacts,
or Meetings tabs. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/search, as of 2026-08-10]

- Optional (all 22): Agent, Applicant, Architect, Architect - Prior, Claimant, Contractor, Contractor – Prior, Customer/Resident, Designer, Designer - Prior, Engineer, Engineer - Prior, Geotechnical, Other, Owner, Owner - Prior, Owner/Builder, Site Contact, Special Inspector, Subcontractor, Tenant, Vegetation Owner. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/374/0/0, as of 2026-09-14]
- **Contractor and Subcontractor entries are licence-validated** by the portal.
- Permits issue only to an owner-builder or a **City-licensed** contractor, and every business working in the city needs a Laguna Beach business licence. [source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/374/0/0, as of 2026-08-10]

## After you submit

The City's confirmation message on this type is, verbatim:

> Thank you for your Commercial Permit application. A permit technician will
> review your application to ensure all required information has been submitted,
> and contact you in 2 - 3 business days for payment.

**Yes, it says "Commercial Permit" on the Mixed Use type** — the City's own
copy-paste in the portal configuration, not a sign that you filed the wrong
application (the Multifamily type (322) says "Multi-Family Permit" in the same
slot). The substance is what matters: submitting does not start plan check — a
technician screens it for completeness first, then invoices.

**And the permit itself is not issued online.** This type carries the City's
warning, verbatim: "\*PLEASE BE ADVISED THAT THE FINAL PERMIT ISSUANCE IS
CONDUCTED IN PERSON AT THE BUILDING COUNTER." Plan on a counter trip to 505
Forest Ave at the end.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/374/0/0, as of 2026-08-10]

## Next step

> **Next step:** file a Mixed Use Permit in the City's permit portal —
> [Mixed Use Permit (type 374)](https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/374/0/0).
> Have the signed [Building Permit Application](http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf) and your plans ready as PDFs.
> You'll need a portal account first — [registration guide](https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000).
> Questions: Building Division (949) 497-0715.
