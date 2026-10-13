# Submit: Multifamily Permit — EnerGov type 322

The building permit for **apartment and condominium buildings** — the multifamily
sibling of the Residential (183) and Commercial (184) permits. Same wizard, same
39-slot file set, same 113-field MEP count sheet; what differs is the category,
and the contact configuration (see "Contacts and licences", which is the one real
trap on this type).

**Apply:** https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/322/0/0 (portal account required)
**Catalog name, verbatim:** "Multifamily Permit" — category MULTIFAMILY, module PERMITS.
Its catalog description, verbatim: "This application is for a Multifamily Building Permit."

Unless noted otherwise, everything below is the City's own configuration of this
application, read from the portal. The apply URL is login-gated in a browser;
the mirrored pull is the City source document (not included in this plugin).
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/322/0/0, as of 2026-08-10]

## Before you start

- **Does planning review come first?** Multifamily work that changes the exterior, the unit count, or the site generally needs a planning entitlement first — a separate, earlier filing. The portal offers no triage to tell you whether you need it; confirm with Planning, (949) 497-0713, and see `submit-residential-planning-entitlements.md`. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/114/0/0, as of 2026-08-10]
- **Ground-floor commercial in the building?** That makes it mixed use — file **Mixed Use Permit (374)** instead, `submit-mixed-use.md`.
- **Fire sprinklers are a separate type** — 190 or 191 depending on how the City classes the building; see `submit-fire-residential.md` and `submit-fire-commercial.md`.
- **Download and sign the Building Permit Application** before you start: http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf — the City requires it signed before upload.
- **A/C in scope?** The **Mechanical Equipment Guide** is, in the City's capitals, "REQUIRED FOR ALL A/C PERMITS BY PLANNING": https://www.lagunabeachcity.net/home/showpublisheddocument/9959/638586590648770000
- **A portal account.** See `how-to-submit.md` → "Before any of this".

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/322/0/0, as of 2026-08-10]

## The wizard, step by step

**1 — Location.** "ATTENTION: This application is for a Multifamily Permit only."
Click **+**, type the address of the primary residence into the search field,
select it from the results; if it is not found, click **Enter Manually**.
Address is required.

**2 — Basic info.** Description is required, and the City asks for a
"comprehensive explanation of the work you plan to do" that **matches your
plans** — a description that disagrees with the drawings is a correction waiting
to happen. Note the City's own field warning, verbatim: "\*\* Square Footage is
for office use only. Do Not use."

**3 — Contacts.** Click **+** to search by person or business name, then **Add**;
if not found, **Enter Manually**. The City's written instruction lists
**Applicant** and **Owner** under "Required Contacts", plus **Contractor**,
**Architect/Designer**, and **Engineer** "if applicable" — but the form itself
does not enforce any of it. See "Contacts and licences".

**4 — More info.** "Please enter the number of items each for Electrical,
Mechanical, and Plumbing if applicable." See the next section.

**5 — Attachments.** Signed application + plans. See "Required attachments".

**6 — Signature and submit.** An electronic signature is required.

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/322/0/0, as of 2026-08-10]

## The questions you will face (113 fields, 3 groups)

This is **not** a questionnaire about the project — it is the fixture count sheet
that drives the itemized MEP fees, identical to the one on types 183 and 184.
Three groups, all optional, all numeric:

| Group | Fields | Examples |
|---|---|---|
| Electrical | 41 | outlets/switches, light fixtures, device boxes, panels and sub-panels by amperage band, services/meters/switchboards, generators/motors by HP band, temporary power poles, pedestal meters, pole-mounted light fixtures |
| Mechanical | 34 | F.A.U. above/below 100K BTU, air conditioner or heat pump by tonnage, air handling units by CFM, ducts/registers/returns, wall/suspended heaters, gas fireplace, boilers/compressors by HP band, fire/smoke dampers |
| Plumbing | 38 | kitchen and bathroom sinks, shower/tub, toilet/water closet/urinal, water heater (standard, tankless, new vent), water service, backflow devices, gas piping per outlet, building sewer, floor drains |

Count only what you are actually installing across the whole scope, and leave the
rest blank. The City bills MEP as separate itemized fees, so these numbers become
money — on a multi-unit job they add up fast.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/322/0/0, as of 2026-08-10]
[source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]

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
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/322/0/0, as of 2026-08-10]

## Optional attachment slots worth knowing

37 more categories exist on this type — the same set as 183 and 184. The ones
that carry a real Laguna requirement or commonly decide whether a submittal is
complete:

- **Mechanical Equipment Guide** — "REQUIRED FOR ALL A/C PERMITS BY PLANNING". Optional slot, mandatory content.
- **Structural Calculations**, **Soils Report or Geotechnical Report**, **Survey** — the standard trio on additions, new structures, and anything on a slope.
- **Energy Calculations** (and the addendum) — Title 24 compliance.
- **WQMP**, **WQ LID Checklist**, **WELO Calculations/Report**, **Hydrology Report** — water quality and landscape efficiency; expected on projects at multifamily scale.
- **Grading Plans** and **Address Assignment Request** — the latter matters when new units need addresses.
- **Fuel Modification or Fire Study** — Laguna is a very-high fire hazard severity zone city.
- **Asbestos Report** and **Asbestos Clearance Certification** — on demolition or older-building work.
- **Roof Material Color Swatch** — the City's own note: "REQUIRED FOR REROOF PERMITS. Please circle or otherwise clearly indicate the exact color you are using." On a reroof, treat it as required.
- **Plan Check Responses** and the per-division response slots (Building, Fire, Planning, Public Works, Water Quality) — where you upload your answers to a correction letter on a resubmittal.
- **Plans: Reference Only Digitized Paper (NO REVIEW)** — exactly what it says; do not put review plans here.

Most accept PDF only; the response slots also take .doc/.docx/.jpg/.jpeg, and
Miscellaneous takes images. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/322/0/0, as of 2026-08-10]

## Contacts and licences

**This type has no required contacts.** All 22 contact types on it are optional
— including Applicant and Owner. That is a real difference from the Residential
(183) and Commercial (184) permits, which both require Applicant and Owner. The
City's own on-screen instruction still says "Required Contacts: Applicant,
Owner", so **the portal does not enforce a required contact on this type; still
list Applicant and Owner.** There is a second reason beyond the instruction: on
the public side you must be logged in *and* listed as a contact on a record to
see its Fees, Reviews, Attachments, Contacts, or Meetings tabs.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/search, as of 2026-08-10]

- Optional (all 22): Agent, Applicant, Architect, Architect - Prior, Claimant, Contractor, Contractor – Prior, Customer/Resident, Designer, Designer - Prior, Engineer, Engineer - Prior, Geotechnical, Other, Owner, Owner - Prior, Owner/Builder, Site Contact, Special Inspector, Subcontractor, Tenant, Vegetation Owner. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/322/0/0, as of 2026-09-14]
- **Contractor and Subcontractor entries are licence-validated** by the portal.
- Permits issue only to an owner-builder or a **City-licensed** contractor, and every business working in the city needs a Laguna Beach business licence. [source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/322/0/0, as of 2026-08-10]

## After you submit

The City's confirmation message, verbatim:

> Thank you for your Multi-Family Permit application. A permit technician will
> review your application to ensure all required information has been submitted,
> and contact you in 2 - 3 business days for payment.

So submitting does not start plan check — a technician screens it for
completeness first, then invoices. **And the permit itself is not issued online.**
This type carries the City's warning, verbatim: "\*PLEASE BE ADVISED THAT THE
FINAL PERMIT ISSUANCE IS CONDUCTED IN PERSON AT THE BUILDING COUNTER." Plan on a
counter trip to 505 Forest Ave at the end.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/322/0/0, as of 2026-08-10]

## Next step

> **Next step:** file a Multifamily Permit in the City's permit portal —
> [Multifamily Permit (type 322)](https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/322/0/0).
> Have the signed [Building Permit Application](http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf) and your plans ready as PDFs.
> You'll need a portal account first — [registration guide](https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000).
> Questions: Building Division (949) 497-0715.
