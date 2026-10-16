# Submit: Commercial Permit — EnerGov type 184

The generic non-residential building permit, and the catch-all for commercial
work the Laguna Beach catalog has no dedicated type for: **tenant improvements,
commercial remodels and additions, shell work, reroofs on a commercial building,
and the MEP work bundled into any of them.** There is no "tenant improvement"
type — a commercial TI is this one. Mechanically it is the twin of the
Residential Permit (183): same wizard, same 39-slot file set, same 113-field MEP
count sheet.

**Apply:** https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/184/0/0 (portal account required)
**Catalog name, verbatim:** "Commercial Permit" — category COMMERCIAL, module PERMITS.
Its catalog description, verbatim: "This application is for a Commercial Building Permit."

Unless noted otherwise, everything below is the City's own configuration of this
application, read from the portal. The apply URL is login-gated in a browser;
the mirrored pull is the City source document (not included in this plugin).
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/184/0/0, as of 2026-08-10]

## Before you start

- **Does planning review come first?** Commercial projects that change the exterior, the use, or the signage generally need a planning entitlement first — that is a separate, earlier filing: **Commercial Planning Entitlements (type 116)**. The portal offers no triage to tell you whether you need it; confirm with Planning, (949) 497-0713. See `submit-commercial-planning-entitlements.md`. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/116/0/0, as of 2026-08-10]
- **Fire-protection work is a different type.** Commercial fire sprinklers file as **Fire Commercial Permit (191)** — see `submit-fire-commercial.md`.
- **Signs are a different type** — Sign Permit (197), `submit-sign.md`.
- **Download and sign the Building Permit Application** before you start: http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf — the City requires it signed before upload.
- **A/C in scope?** The **Mechanical Equipment Guide** is, in the City's capitals, "REQUIRED FOR ALL A/C PERMITS BY PLANNING": https://www.lagunabeachcity.net/home/showpublisheddocument/9959/638586590648770000
- **A portal account.** See `how-to-submit.md` → "Before any of this".

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/184/0/0, as of 2026-08-10]

## The wizard, step by step

**1 — Location.** "ATTENTION: This application is for a Commercial Permit only."
Click **+**, type the address into the search field, select it from the results;
if it is not found, click **Enter Manually**. Address is required. (The City's
instruction text says "the primary residence" here — boilerplate carried over
from the residential form; enter the commercial address.)

**2 — Basic info.** Description is required, and the City asks for a
"comprehensive explanation of the work you plan to do" that **matches your
plans** — a description that disagrees with the drawings is a correction waiting
to happen. Note the City's own field warning, verbatim: "\*\* Square Footage is
for office use only. Do Not use."

**3 — Contacts.** Click **+** to search by person or business name, then **Add**;
if not found, **Enter Manually**. The City lists: **Applicant** and **Owner**
(required), plus **Contractor**, **Architect/Designer**, and **Engineer** "if
applicable".

**4 — More info.** "Please enter the number of items each for Electrical,
Mechanical, and Plumbing if applicable." See the next section.

**5 — Attachments.** Signed application + plans. See "Required attachments".

**6 — Signature and submit.** An electronic signature is required.

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/184/0/0, as of 2026-08-10]

## The questions you will face (113 fields, 3 groups)

This is **not** a questionnaire about the project — it is the fixture count sheet
that drives the itemized MEP fees, identical to the one on type 183. Three
groups, all optional, all numeric:

| Group | Fields | Examples |
|---|---|---|
| Electrical | 41 | outlets/switches, light fixtures, device boxes, panels and sub-panels by amperage band, services/meters/switchboards, generators/motors by HP band, busway per 100', sign/marquee branch circuits, theatrical lighting |
| Mechanical | 34 | F.A.U. above/below 100K BTU, air conditioner or heat pump by tonnage, air handling units by CFM, VAV boxes, hood or canopy, commercial exhaust, refrigeration systems, boilers/compressors by HP band, fire/smoke dampers |
| Plumbing | 38 | kitchen and bathroom sinks, service sinks, toilet/water closet/urinal, floor sinks and drains, drinking fountains, grease interceptor/trap, water heater (standard, tankless, new vent), backflow devices, gas piping per outlet |

Count only what you are actually installing and leave the rest blank. The City
bills MEP as separate itemized fees, so these numbers become money.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/184/0/0, as of 2026-08-10]
[source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]

The City added a separate online work class to this type in October 2026:
**"Revision"** (template "Building Permit - Revision", portal filing behavior
"Pay First"). It is not on the portal's apply menu, and the portal's permit
search list shows it as "Commercial Revision Permit". A project **address is
required**, and no contact is. Two PDFs are required, one file each:
**Revised Plans** and **Original Plans Approved/Stamped by City**. Its intake sheet opens with a
"Revision Info" group — a required **Revision Number** field and an optional
**Additional Valuation** field — followed by the same 113-item Electrical,
Mechanical, and Plumbing count sheet as above. The portal does not say whether to
count the whole job again or only what the revision adds — ask the Building
Division. To revise an issued commercial permit, or if you cannot find the
revision path in the portal, call the Building Division, (949) 497-0715.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService (permit application intake questions and setup), as of 2026-10-12]

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
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/184/0/0, as of 2026-08-10]

## Optional attachment slots worth knowing

37 more categories exist on this type — the same set as 183. The ones that carry
a real Laguna requirement or commonly decide whether a submittal is complete:

- **Mechanical Equipment Guide** — "REQUIRED FOR ALL A/C PERMITS BY PLANNING". Optional slot, mandatory content.
- **Structural Calculations**, **Soils Report or Geotechnical Report**, **Survey** — the standard trio on additions, new structures, and anything on a slope.
- **Energy Calculations** (and the addendum) — Title 24 compliance.
- **Specification Sheets**, **ESR Sheet**, **Installation Manual**, **Fabrication or Shop Drawings** — the product-substantiation slots a commercial reviewer asks for most.
- **WQMP**, **WQ LID Checklist**, **WELO Calculations/Report**, **Hydrology Report** — water quality and landscape efficiency; expected on larger projects.
- **Fuel Modification or Fire Study** — Laguna is a very-high fire hazard severity zone city.
- **Asbestos Report** and **Asbestos Clearance Certification** — on demolition or older-structure work.
- **Roof Material Color Swatch** — the City's own note: "REQUIRED FOR REROOF PERMITS. Please circle or otherwise clearly indicate the exact color you are using." On a commercial reroof, treat it as required.
- **Plan Check Responses** and the per-division response slots (Building, Fire, Planning, Public Works, Water Quality) — where you upload your answers to a correction letter on a resubmittal.
- **Plans: Reference Only Digitized Paper (NO REVIEW)** — exactly what it says; do not put review plans here.

Most accept PDF only; the response slots also take .doc/.docx/.jpg/.jpeg, and
Miscellaneous takes images. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/184/0/0, as of 2026-08-10]

## Contacts and licences

- Required: **Applicant, Owner**. Optional: Architect, Contractor, Designer, Engineer.
- **Contractor entries are licence-validated** by the portal.
- Permits issue only to an owner-builder or a **City-licensed** contractor, and every business working in the city needs a Laguna Beach business licence. [source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/184/0/0, as of 2026-08-10]

## After you submit

The City's confirmation message, verbatim:

> Thank you for your Commercial Permit application. A permit technician will
> review your application to ensure all required information has been submitted,
> and contact you in 2 - 3 business days for payment.

So submitting does not start plan check — a technician screens it for
completeness first, then invoices. **And the permit itself is not issued online.**
This type carries the City's warning, verbatim: "\*PLEASE BE ADVISED THAT THE
FINAL PERMIT ISSUANCE IS CONDUCTED IN PERSON AT THE BUILDING COUNTER." Plan on a
counter trip to 505 Forest Ave at the end.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/184/0/0, as of 2026-08-10]

## Next step

> **Next step:** file a Commercial Permit in the City's permit portal —
> [Commercial Permit (type 184)](https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/184/0/0).
> Have the signed [Building Permit Application](http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf) and your plans ready as PDFs.
> You'll need a portal account first — [registration guide](https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000).
> Questions: Building Division (949) 497-0715.
