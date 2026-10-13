# Submit: Real Property Report — EnerGov type 192

**The odd one out in the catalog.** A Real Property Report (the City also calls
it a Real Property Disclosure, RPD) is what a seller or their agent orders before
a house changes hands — a City report on the property, not a permit and not a
plan review. It is the only one of the five PLANS types that does **not** shout
"THIS IS NOT A BUILDING PERMIT", because nobody would mistake it for one. It is
also the only type in the catalog with **zero attachment slots**, no required
contacts, and no plan review attached: you fill in a short form and wait.
It has its own tile on the portal home page.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/home, as of 2026-08-10]

**Apply:** https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/192/0/0 (portal account required)
**Catalog name, verbatim:** "Real Property Report" — category PLANNING ENTITLEMENTS, module PLANS.
**Catalog description, verbatim:** "Real Property Report Request."

Unless noted otherwise, everything below is the City's own configuration of this
application, read from the portal. The apply URL is login-gated in a browser;
the mirrored pull is the City source document (not included in this plugin).
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/192/0/0, as of 2026-08-10]

## Before you start

- **Order it early.** The City's own confirmation puts the estimated turnaround at **30 days**, and says requests for completion sooner **cannot be guaranteed**. On a 30-day escrow that is the whole clock.
- **Have the listing agent's details to hand** — name, **City of Laguna Beach business licence number**, phone, and email are all fields on the form.
- **Nothing to upload.** There are no attachment slots at all; do not go hunting for a checklist.
- **The City publishes a step-by-step RPD submittal guide** and a first-time registration guide: submittal guide https://www.lagunabeachcity.net/home/showpublisheddocument/22621/638858614092300000 , registration guide https://www.lagunabeachcity.net/home/showpublisheddocument/22619/638858590567600000 [source: https://www.lagunabeachcity.net/government/departments/community-development/planning-zoning/applications-handouts/real-property-reports, as of 2026-07-15]
- **A portal account.** See `how-to-submit.md` → "Before any of this".
- **The report carries more from 2026-08-20.** Three LBMC Title 12 amendments effective that date add tree and view items to the report's contents. See "What the report carries" below. Nothing on this form changes.

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/192/0/0, as of 2026-08-10]

## The wizard, step by step

**1 — Location.** "ATTENTION: This is a Real Property Report Application." Click
**+**, enter the address of the property, select it from the results; if not
found, **Enter Manually**. Address is required.

**2 — Basic info.** **Description is not required** on this type, and neither is
square footage or valuation — unlike every planning-entitlement type.

**3 — Contacts.** Click **+** to search by person or business name, then **Add**;
if not found, **Enter Manually**. The City's written instruction says "Required
Contact: Applicant" — but see "Contacts and licences" below, where the form's own
configuration disagrees.

**4 — More info.** The 11 fields below. The City's note, verbatim: "If you need
assistance completing this request please call the Planning Division at
(949) 497 - 0713."

**5 — Attachments.** The City's entire instruction on this step, verbatim:
**"FOR OFFICE USE ONLY. PLEASE ADVANCE TO THE NEXT PAGE."** There are no slots.

**6 — Signature and submit.** An electronic signature is required.

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/192/0/0, as of 2026-08-10]

## The questions you will face (11 fields, one group)

In the City's own order:

| # | Field | Required? |
|---|---|---|
| 1 | *Property Information* (heading) | — |
| 2 | Property type | **Required** |
| 3 | *Requester* (heading) | — |
| 4 | Requestor Email | optional |
| 5 | Additional Email | optional |
| 6 | Requestor Type | optional |
| 7 | *Listing Real Estate Agent* (heading) | — |
| 8 | Name | optional |
| 9 | Business License # — the City's tip: "City of Laguna Beach's Business License #" | optional |
| 10 | Phone | optional |
| 11 | Email | optional |

**Property type is the only required answer on the whole form.** Everything
else — including both email fields the City will use to reach you — is
technically optional in the configuration. Fill the emails in anyway: there is no
other channel on this form for the City to send the finished report to.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/192/0/0, as of 2026-08-10]

## Required attachments

**None. This type has zero attachment slots** — required or optional. The
attachments step exists but is, in the City's words, "FOR OFFICE USE ONLY."
eReviews is switched off on this type, so there is no electronic plan review
attached to it either.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/192/0/0, as of 2026-08-10]

## Optional attachment slots worth knowing

**None.** Nothing can be uploaded on this application.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/192/0/0, as of 2026-08-10]

## Contacts and licences

- **No contact type is marked required** in this form's configuration. **Applicant** is an optional slot; there are no other contact slots.
- ⚠️ **The City contradicts itself here.** The Contacts step's written instruction reads "Required Contact: Applicant", while the underlying configuration marks Applicant optional. Add yourself as Applicant regardless — it costs nothing and satisfies both readings.
- No contractor licence is validated on this type. The **business licence number** the form asks for is the *listing real estate agent's* City of Laguna Beach business licence, not a contractor licence. Business licences: https://www.lagunabeachcity.net/government/departments/administrative-services/finance-division/business-licenses

[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/192/0/0, as of 2026-08-10]

## After you submit

The City's confirmation message, verbatim:

> Thank you for your Real Property Report Request. The estimated turnaround for
> completion of Real Property Reports is 30 days and that requests for completion
> prior to 30 days cannot be guaranteed.

That is the whole promise: **30 days, and no rush option**. Unlike every other
type in the catalog, there is no "2 - 3 business days" contact-for-payment step
described here, and no in-person-issuance warning. If you need to chase it, the
help line the City puts on this form is Planning Division (949) 497-0713.
[source: https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/192/0/0, as of 2026-08-10]

## What the report carries — three LBMC Title 12 amendments effective 2026-08-20

This file documents the portal request. What the finished report **contains** is
set elsewhere in the code. The 2026 efficiency ordinance adds three items,
**effective 2026-08-20**:

- **Heritage trees.** Notice of the existence of a heritage tree is included in the property file and **in the real property report issued by the city when property is sold** (LBMC 12.08.030(b), as amended). Note the code's wording here: it names the city-issued report, not Chapter 14.76.
- **Record of views.** A record of views is maintained in the property address files and **noted in any real property report required by Chapter 14.76** (LBMC 12.16.040(b), as amended).
- **View decisions.** Decisions by city staff and the View Restoration Committee on view restoration and view preservation **are set forth in any real property report required by Chapter 14.76** (LBMC 12.16.100, as amended). Those decisions also run with the land, bind heirs, successors and assigns, and are recorded in the official records of the County of Orange to the extent permitted.

Sellers and listing agents: order the report on the same 30-day clock, and expect
tree and view obligations to appear in it that earlier reports did not carry. See
`submit-view-preservation.md` and `planning-applications.md` → "Views, trees, and
hedges" for the underlying programmes.

[source: Laguna Beach efficiency ordinance amending LBMC Chapters 7.25, 12.08, 12.16 and 17.50 — introduced 2026-06-23, adopted 2026-07-21, effective 2026-08-20 lines 105, 123, 143. Title 12 and Chapter 14.76 are not in the scraped municipal-code corpus, and eCode360 had not republished Title 12 as of 2026-08-14, so the ordinance is the authority.]

## Next step

> **Next step:** order the report in the City's permit portal —
> [Real Property Report (type 192)](https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/plan/apply/192/0/0),
> and start it at least a month before you need it — the City estimates
> **30 days** and will not guarantee faster. Have the listing agent's name,
> Laguna Beach business licence number, phone, and email ready; there is nothing
> to upload. From **2026-08-20** the report also carries notice of any heritage
> tree, any record of views, and any view restoration or preservation decision
> (LBMC 12.08.030(b), 12.16.040(b), 12.16.100, as amended). The City's
> [step-by-step RPD submittal guide](https://www.lagunabeachcity.net/home/showpublisheddocument/22621/638858614092300000)
> walks the same screens.
> You'll need a portal account — [registration guide](https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000).
> Questions: Planning Division (949) 497-0713.
