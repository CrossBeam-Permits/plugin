# Submit: Residential Permit — EnerGov type 183

The generic single-family building permit, and the catch-all for everything the
Laguna Beach catalog has no dedicated type for: **remodels, additions, reroofs,
decks, garages, fences and walls, pools, window and door replacement, demolition
of part of a structure, and the building permit that follows an ADU entitlement.**
There is no "remodel", "addition", or "reroof" type — they are all this one.

**Apply:** https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0 (portal account required)
**Catalog name, verbatim:** "Residential Permit" — category RESIDENTIAL, module PERMITS.

Unless noted otherwise, everything below is the City's own configuration of this
application, read from the portal. The apply URL is login-gated in a browser;
the mirrored pull is the City source document (not included in this plugin).
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0, as of 2026-08-10]

## Before you start

- **Does planning review come first?** Most Laguna remodels and additions touch design review, coastal, or zoning. That is a separate, earlier filing: **Residential Planning Entitlements (type 114)**, which spawns the `ZPC-`, `DR-`, and `CDP-` records. The portal offers no triage to tell you whether you need it — if the project changes the exterior, assume yes and confirm with Planning, (949) 497-0713. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/114/0/0, as of 2026-08-10]
- **For an ADU, file the ADU plan (type 182) first.** This permit is the second record, not the first. See `submit-adu.md`.
- **Download and sign the Building Permit Application** before you start: http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf — the City requires it signed before upload.
- **A/C in scope?** The **Mechanical Equipment Guide** is, in the City's capitals, "REQUIRED FOR ALL A/C PERMITS BY PLANNING": https://www.lagunabeachcity.net/home/showpublisheddocument/9959/638586590648770000
- **Reroof in scope?** The City requires a **Roof Material Color Swatch** (manufacturer product sheet) with the exact colour circled, so staff can check it against local guidelines.
- **A portal account.** See `how-to-submit.md` → "Before any of this".

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0, as of 2026-08-10]

## The wizard, step by step

**1 — Location.** "ATTENTION: This application is for a Residential Permit only."
Click **+**, type the address of the primary residence, select it from the
results; if it is not found, click **Enter Manually**. Address is required.

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

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0, as of 2026-08-10]

## The questions you will face (113 fields, 3 groups)

This is **not** a questionnaire about the project — it is the fixture count sheet
that drives the itemized MEP fees. Three groups, all optional, all numeric:

| Group | Fields | Examples |
|---|---|---|
| Electrical | 41 | outlets/switches, light fixtures, device boxes, panels and sub-panels by amperage band, services/meters/switchboards, generators/motors by HP band, temporary power poles, AC disconnect |
| Mechanical | 35 | F.A.U. above/below 100K BTU, air conditioner or heat pump by tonnage, air handling units by CFM, ducts/registers/returns, gas fireplace, hood or canopy, boilers by HP band |
| Plumbing | 37 | kitchen and bathroom sinks, shower/tub, toilet, water heater (standard, tankless, new vent), water service, backflow devices, gas piping per outlet, sewer connection, floor drains |

Count only what you are actually installing and leave the rest blank. The City
bills MEP as separate itemized fees, so these numbers become money.

⚠️ **The count sheets are not identical across types.** The stand-alone Plumbing
permit (188) has a **Clothes Washer** field that this form has nowhere, and the
stand-alone Mechanical permit (186) carries **AC Disconnect** in its Mechanical
group where this form has it only under Electrical. The Electrical permit (187)
also **labels the panel amperage bands differently** — "Up to 200 amps" there,
"Up to 600 amps" here, over the same underlying field. If the whole job is one
trade, file that trade's permit rather than this one, and if a panel lands near a
band edge, confirm the fee with the Building Division, (949) 497-0715.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0, as of 2026-08-10]
[source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]

The City added a separate online work class to this type in October 2026:
**"Revision"** (portal filing behavior "Pay First"). It is not on the portal's
apply menu, and the portal's permit search list shows it as "Residential
Revision Permit". A project **address is required**, and no contact is. Two PDFs are required, one file each: **Revised Plans** and **Original Plans Approved/Stamped by City**. Its intake sheet opens with a "Revision Info" group — a required
**Revision Number** field and an optional **Additional Valuation** field —
followed by the same 113-item Electrical, Mechanical, and Plumbing count sheet as
above. The portal does not say whether to count the whole job again or only what
the revision adds — ask the Building Division. To revise an issued residential
permit, or if you cannot find the revision path in the portal, call the Building
Division, (949) 497-0715.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService (permit application intake questions and setup), as of 2026-10-12]

## Required attachments

Two, both PDF, one file each:

| Attachment | The City's description |
|---|---|
| Permit Application | Building Application — the signed [Building Permit Application PDF](http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf) |
| Plans | Project Plans for Reviews |

The City's written instruction, condensed: submit all required documents to
avoid delays — an incomplete application draws a correction request *before* the
plans are reviewed at all — and **sign applications before uploading**.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0, as of 2026-08-10]

## Optional attachment slots worth knowing

37 more categories exist on this type. The ones that carry a real Laguna
requirement or commonly decide whether a submittal is complete:

- **Roof Material Color Swatch** — the City's own note: "REQUIRED FOR REROOF PERMITS. Please circle or otherwise clearly indicate the exact color you are using." Filed as optional, described as required. On a reroof, treat it as required.
- **Mechanical Equipment Guide** — "REQUIRED FOR ALL A/C PERMITS BY PLANNING". Same pattern: optional slot, mandatory content.
- **Soils Report or Geotechnical Report**, **Structural Calculations**, **Survey** — the standard trio on additions, new structures, and anything on a slope.
- **Energy Calculations** (and the addendum) — Title 24 compliance.
- **WQMP**, **WQ LID Checklist**, **WELO Calculations/Report**, **Hydrology Report** — water quality and landscape efficiency; expected on larger projects.
- **Fuel Modification or Fire Study** — Laguna is a very-high fire hazard severity zone city.
- **Asbestos Report** and **Asbestos Clearance Certification** — on demolition or older-structure work.
- **Plan Check Responses** and the per-division response slots (Building, Fire, Planning, Public Works, Water Quality) — where you upload your answers to a correction letter on a resubmittal.
- **Plans: Reference Only Digitized Paper (NO REVIEW)** — exactly what it says; do not put review plans here.

Most accept PDF only; the response slots also take .doc/.docx/.jpg/.jpeg, and
Miscellaneous takes images. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0, as of 2026-08-10]

## Contacts and licences

- Required: **Applicant, Owner**. Optional: Architect, Contractor, Designer, Engineer.
- **Contractor entries are licence-validated** by the portal.
- Permits issue only to an owner-builder or a **City-licensed** contractor, and every business working in the city needs a Laguna Beach business licence. [source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0, as of 2026-08-10]

## After you submit

The City's confirmation message, verbatim:

> Thank you for your Residential Permit application. A permit technician will
> review your application to ensure all required information has been submitted,
> and contact you in 2 - 3 business days for payment.

So submitting does not start plan check — a technician screens it for
completeness first, then invoices. **And the permit itself is not issued online.**
This type carries the City's warning, verbatim: "\*PLEASE BE ADVISED THAT THE
FINAL PERMIT ISSUANCE IS CONDUCTED IN PERSON AT THE BUILDING COUNTER." Plan on a
counter trip to 505 Forest Ave at the end. Fees are due at first plan-check
submittal **and** again at issuance.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0, as of 2026-08-10]
[source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]

## Next step

> **Next step:** file a Residential Permit in the City's permit portal —
> [Residential Permit (type 183)](https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0).
> Have the signed [Building Permit Application](http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf) and your plans ready as PDFs.
> You'll need a portal account first — [registration guide](https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000).
> Questions: Building Division (949) 497-0715.
