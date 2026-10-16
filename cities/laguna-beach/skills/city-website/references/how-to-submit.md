# Laguna Beach — How to Submit: the channel map

A resident names a project. This file answers the only question that matters
next: **which of the four channels does it go through, and what is the exact
link.** Every fact is stamped with the surface it came from and the date that
surface was read. For what a single application type asks for once you are
inside it, load the matching `submit-<type>.md` guide.

## The four channels

| # | Channel | What it is | Entry point |
|---|---|---|---|
| A | **EnerGov online portal** | Tyler EnerGov CivicAccess self-service. 19 application types can be started online — 14 permits + 5 plans. | https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService |
| B | **SolarAPP+ → then EnerGov** | Residential rooftop PV only. Two steps, in order: SolarAPP+ approval first, then permit type 124 in the portal. | https://gosolarapp.org/ then `#/permit/apply/124/0/0` |
| C | **Appointment** | Book a Planner or Building Plan Reviewer. The route for anything the portal has no application type for — Zone Clearance above all. | https://lbwaitlist.cxmflow.com/OABS/Appointment/Index/2c052fc7-571f-4b76-9790-7e91f103c408 |
| D | **Counter / in person** | 505 Forest Ave. **Where nearly every building permit is actually issued**, even when it was applied for online. | See `../../city-reference/references/contacts-hours.md` for hours (⚠️ the City publishes two different sets) |

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/applicationassistant?sectionName=All&showTemplates=false, as of 2026-08-10]
[source: https://www.lagunabeachcity.net/government/departments/community-development, as of 2026-07-16]

## Router — what the resident says → where it goes

Ordered alphabetically by what the resident is likely to call it. "Type" is the
EnerGov case-type ID; the deep link is relative to
`https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService`.

| Resident says… | Channel | Type | Deep link | Guide |
|---|---|---|---|---|
| ADU / JADU / granny flat | A, **then A again** | 182 → 183 | `#/plan/apply/182/0/0` then `#/permit/apply/183/0/0` | `submit-adu.md` |
| Addition / remodel (single-family) | A | 183 | `#/permit/apply/183/0/0` | `submit-residential-permit.md` |
| Coastal Development Permit (CDP) | A | 114 or 116 | `#/plan/apply/114/0/0` | `submit-residential-planning-entitlements.md` |
| Commercial building work | A | 184 | `#/permit/apply/184/0/0` | `submit-commercial-permit.md` |
| Commercial tenant improvement | A | 184 | `#/permit/apply/184/0/0` | `submit-commercial-permit.md` |
| Demolition | A | 183 | `#/permit/apply/183/0/0`, a Demolition work class | `submit-residential-permit.md` |
| Design review | A | 114 or 116 | `#/plan/apply/114/0/0` | `submit-residential-planning-entitlements.md` |
| Driveway approach / sidewalk / trench in the street | A | 315 | `#/permit/apply/315/0/0` | `submit-right-of-way.md` |
| Electrical work / panel upgrade / EV charger circuit | A | 187 | `#/permit/apply/187/0/0` | `submit-electrical.md` |
| Fire sprinklers, commercial | A | 191 | `#/permit/apply/191/0/0` | `submit-fire-commercial.md` |
| Fire sprinklers, residential | A | 190 | `#/permit/apply/190/0/0` | `submit-fire-residential.md` |
| Grading / earth moving | A | 214 | `#/permit/apply/214/0/0` | `submit-grading.md` |
| Haul route / wide or overweight load on City streets / traffic control review | A | 394 | `#/permit/apply/394/0/0` | `submit-right-of-way.md` |
| HVAC / A/C / furnace | A | 186 | `#/permit/apply/186/0/0` | `submit-mechanical.md` |
| Mixed-use building work | A | 374 | `#/permit/apply/374/0/0` | `submit-mixed-use.md` |
| Multifamily (apartment/condo) building work | A | 322 | `#/permit/apply/322/0/0` | `submit-multifamily.md` |
| Neighbor's tree blocks my view | A | 301 | `#/plan/apply/301/0/0` | `submit-view-preservation.md` |
| Plumbing / repipe / sewer | A | 188 | `#/permit/apply/188/0/0` | `submit-plumbing.md` |
| Real Property Report (selling a house) | A | 192 | `#/plan/apply/192/0/0` | `submit-real-property-report.md` |
| Reroof | A | 183 | `#/permit/apply/183/0/0` | `submit-residential-permit.md` |
| Revision to an issued building permit | A | 183, 184 or 374 | that type's link, work class Revision | `submit-residential-permit.md`, `submit-commercial-permit.md`, `submit-mixed-use.md` |
| Sign | A | 197 | `#/permit/apply/197/0/0` | `submit-sign.md` |
| Solar (residential rooftop PV) | **B** | 124 | SolarAPP+ **first**, then `#/permit/apply/124/0/0` | `submit-solar.md` |
| Variance / Conditional Use Permit | A | 114 or 116 | `#/plan/apply/114/0/0` | `submit-residential-planning-entitlements.md` |
| Water heater | A | 188 | `#/permit/apply/188/0/0` | `submit-plumbing.md` |
| Zone Clearance | A | 114 | `#/plan/apply/114/0/0`, work class Zoning Plan Check | `submit-residential-planning-entitlements.md` |

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/applicationassistant?sectionName=All&showTemplates=false, as of 2026-08-10]
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/applicationassistant?sectionName=All&showTemplates=false, work classes read through the portal's public API, as of 2026-10-12]

## Channel A — the 19 types you can start online

Ordered by module, then by case-type ID. All Apply links require a portal
account; the catalog itself is readable logged out.

### PERMITS (module 2) — 14 types

| Type | Name in the catalog | Category | Deep link |
|---|---|---|---|
| 124 | SolarAPP+ Permit (MUST USE SolarAPP+ FIRST BEFORE PROCEEDING) | SOLAR | `#/permit/apply/124/0/0` |
| 183 | Residential Permit | RESIDENTIAL | `#/permit/apply/183/0/0` |
| 184 | Commercial Permit | COMMERCIAL | `#/permit/apply/184/0/0` |
| 186 | Mechanical Permit | MECHANICAL, ELECTRICAL, AND PLUMBING | `#/permit/apply/186/0/0` |
| 187 | Electrical Permit | MECHANICAL, ELECTRICAL, AND PLUMBING | `#/permit/apply/187/0/0` |
| 188 | Plumbing Permit | MECHANICAL, ELECTRICAL, AND PLUMBING | `#/permit/apply/188/0/0` |
| 190 | Fire Residential Permit | RESIDENTIAL | `#/permit/apply/190/0/0` |
| 191 | Fire Commercial Permit | COMMERCIAL | `#/permit/apply/191/0/0` |
| 197 | Sign Permit | SIGN | `#/permit/apply/197/0/0` |
| 214 | Grading Permit | GRADING | `#/permit/apply/214/0/0` |
| 315 | Right-of-Way Permits | RIGHT-OF-WAY | `#/permit/apply/315/0/0` |
| 322 | Multifamily Permit | MULTIFAMILY | `#/permit/apply/322/0/0` |
| 374 | Mixed Use Permit | MIXED USE | `#/permit/apply/374/0/0` |
| 394 | Transportation Permits | RIGHT-OF-WAY | `#/permit/apply/394/0/0` |

### PLANS (module 3) — 5 types, all under PLANNING ENTITLEMENTS

| Type | Name in the catalog | Deep link |
|---|---|---|
| 114 | Residential Planning Entitlements | `#/plan/apply/114/0/0` |
| 116 | Commercial Planning Entitlements | `#/plan/apply/116/0/0` |
| 182 | Accessory Dwelling Units (ADUs) and Junior Accessory Dwelling Units (JADUs) | `#/plan/apply/182/0/0` |
| 192 | Real Property Report | `#/plan/apply/192/0/0` |
| 301 | View Preservation | `#/plan/apply/301/0/0` |

- Four of the five PLANS types shout **"ATTENTION: THIS IS NOT A BUILDING PERMIT"** in their own catalog description — 114, 116, 182, and 301. A plan record is zoning/entitlement review; it does not authorize construction. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/applicationassistant?sectionName=All&moduleId=3&categoryName=PLANNING%20ENTITLEMENTS&showTemplates=false, as of 2026-08-10]

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/applicationassistant?sectionName=All&showTemplates=false, as of 2026-08-10]

## Channel B — residential rooftop solar is two steps, in this order

1. **SolarAPP+ approval first.** SolarAPP+ is the automated plan-review platform; the installing contractor must be a registered SolarAPP+ user. Start at https://gosolarapp.org/ — the City's own contractor how-to link is https://help.solar-app.org/article/15-permit-application (it now redirects to `help.gosolarapp.org`). [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/124/0/0, as of 2026-08-10]
2. **Then file type 124 in the portal.** The type is literally named "SolarAPP+ Permit (MUST USE SolarAPP+ FIRST BEFORE PROCEEDING)", and its first wizard step reads "DO NOT PROCEED WITHOUT SolarAPP+ APPROVAL FIRST". You upload the approved SolarAPP+ checklist and the SolarAPP+ specification sheets. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/124/0/0, as of 2026-08-10]

- Type 124 is one of the few permit types with **no** in-person-issuance warning, and its submit confirmation reads "Your permit has been issued!" — an instant-issuance path. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/124/0/0, as of 2026-08-10]
- Anything outside SolarAPP+'s envelope — ground-mount PV, non-residential solar, generators, service or main-panel upgrades, new service meters, and a reroof done as part of the solar job — needs a **separate permit** and is not covered by type 124. The City lists those exclusions on the form itself. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/124/0/0, as of 2026-08-10]
- **Symbium is not a Laguna Beach channel.** Nothing in the catalog, on lagunabeachcity.net, or on Symbium's own site connects Symbium to Laguna Beach; `symbium.com/permits/ca/laguna-beach` returns 404. Laguna Niguel and Laguna Hills run public SolarAPP+ programs and are the likely source of the confusion. [source: https://symbium.com/instantpermitting/solar/california/sb379, as of 2026-08-10]
- The local ordinance layer is unchanged: LBMC Ch. 14.84 (expedited small residential rooftop solar) still governs the *rules*. Channel ≠ rules. [source: https://ecode360.com/42894680, as of 2026-08-10]

Full details: `submit-solar.md`.

## Channel C — appointment with a Planner or Plan Reviewer

Book at https://lbwaitlist.cxmflow.com/OABS/Appointment/Index/2c052fc7-571f-4b76-9790-7e91f103c408 [source: https://www.lagunabeachcity.net/government/departments/community-development, as of 2026-07-16]

- **Zone Clearance is filed online, not here.** It has no application type of its own; it is the Zoning Plan Check work class of Residential Planning Entitlements (114). The City's planning-entitlement forms say "If no discretionary planning entitlement is required but zoning review is still necessary, submit a Zone Clearance Application." An appointment is still available but is not required. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/applicationassistant?sectionName=All&showTemplates=false, work classes read through the portal's public API, as of 2026-10-09]
- Over-the-counter building plan review is **Monday–Thursday 7:30–11:00 a.m. by appointment**, half-hour slots, 30-minute maximum. **Walk-in without an appointment is Monday–Thursday 7:30 a.m. – 2:00 p.m., last check-in 12:45 p.m.** Both cover first review, rechecks and revisions. Full detail and the ⚠️ about the City's stale appointment page: `../../city-reference/references/contacts-hours.md`. [source: Building Plan Review Services handout, edition 06/08/2026 — the City source document (not included in this plugin)]

### ⚠️ Discretionary planning: online type vs. "book an appointment" — the City says both

The City gives two different answers for how a discretionary planning
application (design review, CDP, variance, CUP) is filed, and both were live on
2026-08-10:

- **Reading 1 — file it online.** *Residential Planning Entitlements* (114) and *Commercial Planning Entitlements* (116) are live, applyable online types. Design Review, Coastal Development Permit, Variance, and Conditional Use Permit have no application type of their own; they are filed through 114/116, and the City then opens the `DR-`, `CDP-`, `ZPC-` child records itself under one `PR-` project. Public record search shows exactly that pattern. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/applicationassistant?sectionName=All&moduleId=3&categoryName=PLANNING%20ENTITLEMENTS&showTemplates=false, as of 2026-08-10]
- **Reading 2 — book an appointment.** The ADU form's first step reads: "Projects that don't involve an ADU and/or a JADU should schedule an appointment for submittal at the following link: Book an Appointment." Taken at face value that routes every non-ADU planning submittal to the appointment booker. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/182/0/0, as of 2026-08-10]

**How to answer:** give the online type (114 or 116) as the filing route, and add
that the City also directs planning submittals to a booked appointment — so
booking one is never wrong and is the safe move for anything discretionary. Do
not assert that discretionary planning cannot be filed online; two live types
say otherwise. Confirm with Planning, (949) 497-0713.

## Channel D — the counter, and the caveat that catches everyone

- **11 of the 14 online permit types still require in-person issuance.** Their catalog descriptions carry, verbatim: "\*PLEASE BE ADVISED THAT THE FINAL PERMIT ISSUANCE IS CONDUCTED IN PERSON AT THE BUILDING COUNTER." That covers 183, 184, 186, 187, 188, 190, 191, 197, 214, 322, and 374 — the only exceptions are 124 (SolarAPP+), 315 (Right-of-Way), and 394 (Transportation, added October 2026). **"Apply online" is real but partial**: the applicant still ends up at 505 Forest Ave to pick up the permit. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/applicationassistant?sectionName=All&showTemplates=false, as of 2026-08-10] [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/applicationassistant?sectionName=All&showTemplates=false, as of 2026-10-12]
- None of the five PLANS types carries the warning — a plan record is reviewed and invoiced, not issued over a counter.
- **Demolition** and **Zone Clearance** have no application type of their own, but both are filed online as work classes: standalone demolition under 183 (Demolition; Demolition - Single Family Residence; Demolition - ADU/JADU; Demolition - Duplex, all Review First), and Zone Clearance under 114 (Zoning Plan Check). An earlier read (2026-08-10) looked only at application types and called both counter matters. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/applicationassistant?sectionName=All&showTemplates=false, work classes read through the portal's public API, as of 2026-10-09]
- **A revision to an issued building permit** is a work class too, not an application type: **Revision** (portal filing behavior "Pay First") under Residential (183), Commercial (184), and Mixed Use (374). Multifamily (322) has none. The intake asks for the revision number, any added valuation, and the MEP count sheet; each type's guide has the detail. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/applicationassistant?sectionName=All&showTemplates=false, work classes read through the portal's public API, as of 2026-10-12]

## Sharp edges — the four things that actually trip people up

1. **ADU is a PLAN, and it needs a SECOND filing.** Type 182 is a planning
   entitlement, not a building permit — its own card says so in capitals. A
   resident who files only 182 gets zoning clearance and no authority to build.
   The building permit is a separate Residential Permit (183) filed afterward.
   Always answer an ADU question as two records, in order: **182 → 183**.
   [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/182/0/0, as of 2026-08-10]

2. **Applying online does not mean getting the permit online.** See Channel D.
   Set the expectation up front, or the resident plans their project around a
   permit that is sitting at the counter waiting for them.

3. **Reroof and water heater have no type of their own** — the two highest-volume
   simple residential permits in any city. A reroof is a **Residential Permit
   (183)**; internally the City runs it under a "Reroof" work class, and its
   file set includes a **Roof Material Color Swatch** that the City marks
   "REQUIRED FOR REROOF PERMITS" (circle the exact color, so staff can check it
   against local guidelines). A water heater is a **Plumbing Permit (188)**; a
   heat-pump water heater needing a new circuit realistically also needs an
   Electrical Permit (187). The portal offers no triage for either.
   [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0, as of 2026-08-10]

4. **Registration is Tyler Identity, and it is email-first.** `#/registration`
   redirects to Tyler's hosted SSO, not a City login. You can sign in with
   Google, Apple, Microsoft, or Facebook, **or** create an email/password
   account. The City's own guide warns: if your social login uses a personal
   email and you use a business email for the portal, **the accounts will not
   link**. Pick one email and stay on it. Registration then takes an emailed
   verification code, the remaining asterisked fields, and Submit.
   [source: https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000, as of 2026-08-10]

## Before any of this: you need an account

- All of it is walled: applying, paying invoices, tracking status, requesting inspections, and the dashboard. The catalog and public record search are the only things readable logged out. [source: https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000, as of 2026-08-10]
- Registration guide (PDF): https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000 [source: https://www.lagunabeachcity.net/government/departments/community-development, as of 2026-07-16]
- Nothing at signup asks for a contractor licence, business licence, or proof of ownership. Those attach later, at permit issuance — the City requires an owner-builder or a **City-licensed** contractor, and every business working in the city needs a Laguna Beach business licence. [source: https://www.lagunabeachcity.net/government/departments/community-development/building-permits, as of 2026-07-08]

## What no public surface will tell a resident

- **There is no per-type document checklist visible before login.** EnerGov holds a written submittal checklist for all 19 types; the Application Assistant shows only a one-line description. The `submit-<type>.md` guides in this pack exist to close exactly that gap. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/applicationassistant?sectionName=All&showTemplates=false, as of 2026-08-10]
- **No fee estimator is surfaced anywhere.** Only two of the 19 types even have fee estimation enabled in the back end (197 Sign, 214 Grading), and no estimator entry point is rendered in the portal. Fees are quoted by staff after review. For a current amount, call
the fee estimate; do not quote figures from `fees.md`. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/home, as of 2026-08-10]
- **You cannot see your own fees or plan-check comments from the public side.** On a record page the Fees, Reviews, Attachments, Contacts, and Meetings tabs return "You must be a contact on this record to see this information" — you must log in *and* be listed as a contact on that record. [source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/search, as of 2026-08-10]

## Answer shape

Any "how do I get a permit for X" answer ends with a **Next step** line naming
the channel and giving the link as a labelled markdown link — never a bare URL:

> **Next step:** file a Residential Permit in the City's permit portal —
> [Residential Permit (type 183)](https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0).
> You'll need a portal account first — [registration guide](https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000).
