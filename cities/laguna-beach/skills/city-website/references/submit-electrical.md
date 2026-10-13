# Submit: Electrical Permit — EnerGov type 187

The stand-alone electrical permit, and the catch-all for electrical work the
catalog has no other home for: **EV-charger circuits, panel and sub-panel
upgrades, service/meter/switchboard changes, generators and motors, low-voltage
systems, temporary construction power, sign circuits, site and street
lighting.** Use it when electrical work is the whole job. If it is part of a
larger remodel or addition, it rides along on the **Residential Permit (183)**
instead — see `submit-residential-permit.md`.

**It is also the fallback for solar-adjacent electrical.** SolarAPP+ (type 124)
covers residential rooftop PV only; the City's own form lists **ground-mounted
PV, service upgrades outside SolarAPP+ scope, main panel upgrades, and new
service meter installations** (plus generators and a reroof done with the solar
job) as needing separate permits. The electrical half of that list files here.
See `submit-solar.md`.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/124/0/0, as of 2026-08-10]

**Apply:** https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/187/0/0 (portal account required)
**Catalog name, verbatim:** "Electrical Permit" — category MECHANICAL, ELECTRICAL, AND PLUMBING, module PERMITS.
**Catalog description, verbatim:** "This application is for a Electrical Building Permit. \*PLEASE BE ADVISED THAT THE FINAL PERMIT ISSUANCE IS CONDUCTED IN PERSON AT THE BUILDING COUNTER."

Unless noted otherwise, everything below is the City's own configuration of this
application, read from the portal. The apply URL is login-gated in a browser;
the mirrored pull is the City source document (not included in this plugin).
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/187/0/0, as of 2026-08-10]

## Before you start

- **A signed permit application.** The only required attachment on this type is "Permit Application", described by the City simply as "Building Application". Sign it before you upload.
- **EV charger?** The City publishes four EV documents on its forms page — *Electric Vehicle Charger Installation Guidelines* and three *Electric Vehicle Charging (Code Compliance Checklist)* variants (general, non-residential, multi-family). None is a portal requirement on this type; they are the City's guidance for getting the design right. [source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits/applications-forms, as of 2026-08-10]
- **A portal account.** See `how-to-submit.md` → "Before any of this".
- *Our note, not the City's:* the City publishes **two** paper forms that could answer to "Building Application" — the *Building Application* and an *Electrical, Mechanical, and Plumbing Permit Application* — and the portal does not say which one this slot wants. If in doubt, call the Building Division, (949) 497-0715. [source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits/applications-forms, as of 2026-08-10]

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/187/0/0, as of 2026-08-10]

## The wizard, step by step

**1 — Location.** "ATTENTION: This application is for an Electrical Permit only."
Click **+**, type the address of the primary residence into the search field,
select it once results populate; if it is not found, click **Enter Manually**.
Address is required.

**2 — Basic info.** Description is required, and the City asks for a "detailed
scope of work" — a "comprehensive explanation of the work you plan to do" that
**matches your plans**. Note the City's field warning, verbatim: "\*\* Square
Footage is for office use only. Do Not use." Square footage and valuation are
not required on this type.

**3 — Contacts.** Click **+** to search by person or business name, select the
result and click **Add**; if not found, **Enter Manually**. The City lists:
**Applicant** and **Owner** (required), plus **Contractor** "(If applicable)".

**4 — More info.** "Please enter the number of items each for Electrical," plus
a pointer to the City's [applications and forms page](https://www.lagunabeachcity.net/government/departments/community-development/building-permits/applications-forms).

**5 — Attachments.** Signed application; project plans if applicable. See below.

**6 — Signature and submit.** An electronic signature is required.

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/187/0/0, as of 2026-08-10]

## The questions you will face (41 fields, 1 group)

This is **not** a questionnaire about the project — it is the device count sheet
that drives the itemized electrical fees. One group, all optional, all numeric,
in the City's order:

| Group | Fields | Examples |
|---|---|---|
| Electrical | 41 | outlets/switches each, light fixtures each, circuit/conduit/outlet assemblies, device boxes, time clock, low-voltage systems, AC disconnect, range and cooking unit, appliances (residential self-contained, commercial up to 1hp, not listed), washer and dryer, misc conduit/apparatus/conductors, underground service conduit per 100′, busway per 100′, alarms/fire sprinklers/misc electrical, temporary power pole, sub pole, construction lighting and distribution, panels/sub-panels by amperage band, services/meters/switchboards by amperage band, generators/motors by size band, sign or marquee branch circuit, theatrical lighting, special-event generators and lighting, street light pole, pedestal meter, pole/platform-mounted fixture, misc not listed |

Count only what you are actually installing and leave the rest blank. The City
bills electrical work as separate itemized fees, so these numbers become money.

⚠️ **The panel bands are internally inconsistent.** On this type the City labels
them "Panel/Sub Panel: Up to 200 amps" and "Over 200 - 1,000 amps", but the
underlying field names are `NUM_PanelUpto600amps` and `NUM_Panel600to1000amps` —
and the same fields are labelled "Up to 600 amps" / "600-1,000 amps" on the
Residential Permit (183). If your panel is between 200 A and 600 A, ask the
Building Division which band the City is billing, (949) 497-0715.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/187/0/0, as of 2026-08-10]
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0, as of 2026-08-10]

The City also configures a separate online work class on this type:
**"Residential Electrical Service Panel up to 400 AMP"** (portal filing behavior
"Pay First"). It is not on the portal's apply menu. Its intake sheet is headed
"200 Amps or Less" and "Between 200 Amps & 400 Amps". Until August 2026 the
second header read "Between 200 Amps & 1,000 Amps"; the City tightened it to
match the 400-amp work-class name. For a service panel over 400 A, this express
path does not apply — use the standard Electrical application above, or call the
Building Division, (949) 497-0715.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService (permit application intake questions), as of 2026-08-31]

## Required attachments

One, PDF, one file:

| Attachment | The City's description |
|---|---|
| Permit Application | Building Application |

The City's written instruction on this step reads differently from the
configuration: it says "Applicants must submit the following: Project plans (if
applicable)" — but **Plans is an optional slot on this type and Permit
Application is the only required one.** The condensed rest of the instruction:
submit all required documents to avoid delays — an incomplete application draws
a correction request *before* the plans are reviewed at all.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/187/0/0, as of 2026-08-10]

## Optional attachment slots worth knowing

Eight more categories exist on this type, all PDF unless noted, unlimited files
unless noted:

- **Plans** — "Project Plans for Reviews", one file. The City's written instruction asks for project plans "if applicable"; this is where they go. On a panel upgrade or a new service, a single-line diagram and a site plan belong here.
- **Specification Sheets** — "Project Specification Sheets". Charger, panel, and generator cut sheets.
- **Energy Calculations** and **Energy Calculation Addendum** — Title 24 compliance; expected when the scope triggers it.
- **Plan Check Responses** (.doc/.docx/.pdf/.jpg/.jpeg) — where you upload your answers to a correction letter on a resubmittal.
- **Revision Form** — for a change after the permit exists.
- **Mechanical Equipment Guide** — the slot exists on this type too, but the "REQUIRED FOR ALL A/C PERMITS BY PLANNING" instruction is written only on the Mechanical Permit (186). See `submit-mechanical.md`.
- **Miscellaneous** (.pdf/.tif/.tiff/.jpeg/.jpg/.png) — everything else.

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/187/0/0, as of 2026-08-10]

## Contacts and licences

- Required: **Applicant, Owner**. Optional: Agent, Architect, Contractor, Contractor – Prior, Designer, Engineer, Other, Owner - Prior, Owner/Builder, Subcontractor, Tenant.
- **Contractor and Subcontractor entries are licence-validated** by the portal.
- Permits issue only to an owner-builder or a **City-licensed** contractor, and every business working in the city needs a Laguna Beach business licence. [source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/187/0/0, as of 2026-08-10]

## After you submit

The City's confirmation message, verbatim:

> Thank you for your Electrical Permit application. A permit technician will
> review your application to ensure all required information has been submitted,
> and contact you in 2 - 3 business days for payment.

So submitting does not start plan check — a technician screens it for
completeness first, then invoices. **And the permit itself is not issued
online.** This type carries the City's warning, verbatim: "\*PLEASE BE ADVISED
THAT THE FINAL PERMIT ISSUANCE IS CONDUCTED IN PERSON AT THE BUILDING COUNTER."
Plan on a counter trip to 505 Forest Ave at the end.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/187/0/0, as of 2026-08-10]

## Next step

> **Next step:** file an Electrical Permit in the City's permit portal —
> [Electrical Permit (type 187)](https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/187/0/0).
> Rooftop solar itself goes through [SolarAPP+ first](https://gosolarapp.org/) and then [type 124](https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/124/0/0) — ground-mount PV, service upgrades, main panel upgrades, and new service meters come back here.
> Forms live on the [Building Applications & Forms page](https://www.lagunabeachcity.net/government/departments/community-development/building-permits/applications-forms).
> You'll need a portal account first — [registration guide](https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000).
> Questions: Building Division (949) 497-0715.
