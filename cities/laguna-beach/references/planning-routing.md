# Planning routing

## Authority and method

Reason over the complete project evidence and hard site facts against the closed lists in
LBMC §25.05.040(B). Never choose a route from a keyword, filename, regex, or permit-type
enum. Unknown facts stay null and the route stays `undetermined`; do not invent a Design
Review tier merely to fill a form.

Before routing a pool or spa, establish all three of these facts:

1. its highest point above **adjacent legal ground elevation** (more than 3 feet, no more
   than 3 feet, or unknown), plus whether a portable spa exceeds 600 gallons;
2. whether the parcel/work is in the coastal zone and whether a CDP exemption exception
   applies; and
3. whether it is oceanfront or bluff-adjacent, including the surveyed/geotechnical top of
   bluff where the 25-foot setback could apply.

Route the pool/spa structure and its mechanical equipment independently. The equipment
test never downgrades the structure's route.

## One governing tier, additive applications

The governing design-review `tier` is singular. Use the highest list matched by any scope
component: Design Review Board / Planning Commission (`drb`) under (B)(1) outranks
Administrative Design Review (`admin_dr`) under (B)(3), which outranks Zone Clearance
(`zone_clearance`) under (B)(2). Name every matched component and set `mixed_scope: true`
when more than one list is implicated.

Both `drb` and `admin_dr` use the City's single Design Review Application. Add that form
only once even when a major remodel, pool, and equipment all implicate Design Review.
CDP, CUP, variance, and ADU/JADU applications are additional instruments, not substitute
tiers. A CDP is a **parallel package with its own completeness determination**; process it
concurrently where allowed, but do not fold its checklist into Design Review.

| Established fact | Governing result | Authority |
|---|---|---|
| Pool or spa more than 3 feet above adjacent legal grade, except a portable spa no more than 600 gallons | `drb`; one Design Review Application | LBMC §25.05.040(B)(1)(j) |
| Pool or spa no more than 3 feet above adjacent legal grade, or portable spa no more than 600 gallons | `zone_clearance`; Zone Clearance Application; online type 114 (verified public City configuration) | LBMC §25.05.040(B)(2)(t), §25.05.045, as enacted by Urgency Ord. 1732 and extended by Ord. 1733 |
| Development in an environmentally sensitive area, unless the licensed-professional determination and peer review establish no impact | `drb`, including an otherwise (B)(2)/(B)(3) item | LBMC §25.05.040(B)(1)(e), (B)(2) |
| Equipment passes all six objective requirements below | equipment is `zone_clearance`, without Design Review | LBMC §7.25.130(C); §25.05.040(B)(2)(v) |
| Equipment fails any one of the six requirements | equipment is `admin_dr` | LBMC §7.25.130(D); §25.05.040(B)(3)(a)(v) |

### Six-part equipment test (effective 2026-08-20)

Record each part separately as yes, no, or unknown. A blanket statement such as
"equipment complies" is not evidence. Passing means **all six are yes**; any no means
Administrative Design Review; any unknown leaves the equipment route undetermined.

1. Ground-mounted, or wall-mounted at ground level.
2. Outside the required front yard setback (Ord. 1731 struck "or side" from this test). The side
   yard is still closed to AC and pool equipment by LBMC §25.50.004(F)(2), so equipment in a
   required side yard fails yard conformance even when this test passes.
3. At least five feet from every property line.
4. Manufacturer specification sheet supplies the decibel rating; sound is limited to
   60 dB daytime / 50 dB nighttime at the property line; and two maintained sound-
   attenuation techniques are provided.
5. The City-provided sound form shows the property-line calculation under ARI Standard
   275 (1984, as amended). The form's published title is not confirmed—do not invent it.
6. A three-foot path of travel remains around every structure.

For equipment in or adjacent to residential areas, the installation contractor also signs
the §7.25.130(A) acknowledgment, before permit issuance, that the installation will meet
§7.25.040 noise limits.

## Coastal, bluff, geotechnical, and hazard branches

- Analyze the SFR pool exemption under LBMC §25.07.008(A)(1); never assume it. Check the
  beach/wetland/stream, mean-high-tide, within-50-feet-of-bluff, ESA, highly scenic,
  appeal-area, critical-water-supply, prior-CDP-condition, landform, and vegetation
  exceptions. A Zone Clearance route can still require a CDP.
- Pools and spas must be at least 25 feet from the top of an oceanfront bluff under
  LBMC §25.50.004(B)(4). Establish that edge by survey/geotechnical evidence when relevant.
- Require the City geotechnical report branch for a new pool on an ungraded lot, in a
  floodplain, or on a coastal bluff top. Also flag steep hillside, liquefaction, prior
  soil/structure failure, unconventional foundations, and Building Official discretion.
- Screen floodplain development and fuel-modification/WUI impacts independently; neither
  is a reason to guess the Design Review tier.

## Filing set and channel

| Filing | Channel |
|---|---|
| Zone Clearance | Type 114 `Residential Planning Entitlements`, PLANS module; one `Application` PDF and one `Plans` PDF; verified through current City type/work-class instructions |
| Design Review / Administrative Design Review | Type 114 `Residential Planning Entitlements`, one `Application` PDF and one `Plans` PDF |
| Coastal Development Permit | Add to the type 114 Application PDF and preserve its separate checklist/completeness result |
| Conditional Use Permit or Variance | Add the confirmed form to the one type 114 Application PDF |
| ADU/JADU | Planning type 182; Building type 183 only after Planning approval is effective |
| Residential floodplain development | Add the pinned floodplain application when the mapped floodplain/development facts trigger it |

After Planning approval, create **one Building Permit Application per distinct Building
scope, each with its own valuation**. A remodel, ADU, and pool may share a Planning Design
Review form but may not ride on one Building application.

If commercial Planning is implicated, declare the V1 residential checklist unsupported
and obtain an authoritative commercial checklist. Never adapt the residential list.
Read `form-coverage.md` before promising form preparation for any other application type.

## Filing routes for the other pinned Planning forms (sourced 2026-10-10)

Every form below says, on its first page, that new applications go through the Public
Permit Portal, online or on a City computer at City Hall, with a hard-copy submittal only
as an accommodation requested from Community Development at (949) 497-0713. None of them
names a portal record type, and the portal has no record type for any of them. Route each
from the evidence below. Choosing which form applies is a judgment over the project facts;
never pick it from a keyword or a filename.

What the portal itself says (public GETs of the EnerGov SelfService API, 2026-10-10; the
type 114 entries match `assets/portal-maps/v2-portal-map.json`):

- **Type 114, Residential Planning Entitlements, Zoning Plan Check work class.** Its
  attachment instruction: "Development applications submitted to the Planning Division
  must identify the specific entitlement or approval requested. Please complete and submit
  the applicable forms for each requested entitlement or approval." Required uploads:
  one `Application` PDF and one `Plans` PDF; optional `Miscellaneous`, `Reports`,
  `Technical Studies`. It has no slot named for any form below, so every applicable form
  goes into the one `Application` PDF.
- **Type 116, Commercial Planning Entitlements, Zoning Plan Check - Commercial work
  class.** Same instruction, plus optional slots named for these forms: `Temporary Uses`
  ("Provide a full description of the temporary activities ..."), `Revocable Encroachment
  Permit Application` ("Required when a project proposes private encroachments into an
  otherwise unimproved, unused public right-of-way ..."), `Lot Line Adjustment`, `Sign
  Plans`, `Planning Commission Concept Review Application` ("Required if a concept review
  hearing is recommended by Planning staff."), and `Tentative Map`. Type 116 is outside
  portal map v2 and commercial Planning is unsupported in V1: name the route and hand off.
- **Type 197, Sign Permit (PERMITS module, Building).** Work classes Blade,
  Miscellaneous, Monument, Sign, and Wall. The required upload is `Permit Application`,
  described as "Building Application"; the instruction links the Building Applications &
  Forms page; a permit technician screens it; final issuance is in person at the Building
  counter. Type 197 is outside portal map v2.

| Form (manifest id) | Route | `channel` | Source |
|---|---|---|---|
| Temporary Use Permit (`temporary-use-permit-application`) | Residential site: type 114, Zoning Plan Check, the TUP form in the `Application` PDF. Commercial site: type 116 with the activity description in `Temporary Uses` (unsupported in V1). File at least 30 days before a use of 5 days or less (Director), 90 days before a longer one (Planning Commission). A temporary use that needs a CDP files a separate CDP application. | `online` (114) | TUP form p. 1 and footnote 1; type 114 and 116 instructions and slots |
| Revocable Encroachment Permit (`revocable-encroachment-permit-application`) | Type 114, Zoning Plan Check, in the `Application` PDF with the Design Review Application when that is also required ("Submit concurrent, if required"). The REP fee is charged in addition to the Zoning Plan Check fee. Commercial site: type 116, `Revocable Encroachment Permit Application` slot. After approval and the 14-day appeal period, the notarized license agreement (pp. 8-9) is recorded. This is a Planning approval, not the Public Works Right-of-Way Permit (type 315); the form does not say whether construction in the right-of-way also needs a type 315 permit, so ask Public Works. | `online` (114) | REP form pp. 1, 4-5; type 114 and 116 instructions and slots |
| Lot Line Adjustment (`lot-line-adjustment-application`) | Type 114, Zoning Plan Check, in the `Application` PDF; the LLA fee is charged in addition to the Zoning Plan Check fee. Commercial parcels: type 116, `Lot Line Adjustment` slot. A CDP or other entitlement is a separate application. | `online` (114) | LLA form pp. 1, 3; type 114 and 116 instructions and slots |
| SB 9 (`sb-9-application`) | Type 114, Zoning Plan Check, in the `Application` PDF; the SB 9 fee is charged in addition to the Zoning Plan Check fee. The application is not complete without the approved, final CDP, so the CDP is its own earlier type 114 filing. | `online` (114) | SB 9 form pp. 1, 5, 7, 10, 14 and footnote 1; type 114 instruction |
| Sign Permit, Planning (`sign-permit-application`) | Two filings. (1) The Planning Sign Permit Application, screened by a planner: type 116 for a commercial site, with drawings in `Sign Plans` (unsupported in V1); type 114 for a residential site. (2) "Except for window decal signs, new signs generally require a building permit prior to installation": the Building Sign Permit, type 197, with the Building Division's permit application, never the Planning form. A new business also needs a City business license (LBMC Chapter 5.08). | `unverified` (116 and 197 are not in the portal map) | Sign Permit form pp. 1-2; type 116 and 197 setup and instructions |
| Planning Commission Concept Review (`planning-commission-concept-review-application`) | Only after consulting Planning staff, and only when staff recommend a concept review hearing. Commercial: type 116, `Planning Commission Concept Review Application` slot. Residential: type 114, in the `Application` PDF. Needs a 300-foot mailed neighborhood notification and the concept review fee. | `online` (114) | Concept Review form p. 1, section I and III; type 116 slot description; type 114 instruction |
| SB 684 / SHRA (`sb-684-application`) | The housing development part is "an application for Zoning Plan Check (Ministerial Design Review)"; the subdivision part pays the Zoning Plan Check fee in addition to the map deposit. File both on type 114, Zoning Plan Check, in the `Application` PDF; the portal has no SHRA or tentative map record type (type 116 has a `Tentative Map` slot, but it is the commercial type). Each part needs a legally approved, final CDP first. | `online` (114) | SB 684 package pp. 2-3, 5, 8, 13; type 114 instruction |
| General Plan Amendment (`general-plan-amendment-application`) | Two stages. First a request to initiate (Application Type "Initiation of Amendment", the initiation deposit, a narrative and exhibits); the City Council decides at a noticed hearing, and without initiation the City will not accept the application. Then the amendment application, within two years. The form says to file through the Public Permit Portal; it does not say which record type, and neither type 114 nor 116 names legislative amendments. Ask Planning, (949) 497-0713, which record takes the request before filing. | `unverified` | GPA form pp. 1-4 |

The SB 684 package labels its own exhibits inconsistently: its checklists say to sign
"Exhibit H" (the affidavit is Exhibit I, page 67) and call the CDP form "Exhibit I" (the
bundled CDP package starts on page 76). Use the page, not the letter.

## Sources

- [LBMC §25.05.040, Design Review](https://ecode360.com/42898558)
- [Urgency Ordinance 1732, including new LBMC §25.05.045](https://ecode360.com/LA4953/laws/LF2759074.pdf), effective immediately 2026-07-21
- [Ordinance 1733, extending Urgency Ordinance 1732](https://ecode360.com/LA4953/laws/LF2782335.pdf), adopted 2026-08-04
- [Ordinance 1731, six-part LBMC §7.25.130 test](https://ecode360.com/LA4953/laws/LF2759073.pdf), effective 2026-08-20
- [LBMC §25.07.008, coastal-development exemptions](https://ecode360.com/42898824)
- [LBMC §25.50.004, oceanfront development standards](https://ecode360.com/42901675)
- [City Applications & Handouts](https://www.lagunabeachcity.net/government/departments/community-development/planning-zoning/applications-handouts), verified 2026-08-22; application links re-read 2026-10-10
- Current form source receipts: `assets/form-manifest.json`
- Current portal source receipt: `assets/portal-maps/v2-portal-map.json` (built from `assets/portal-maps/portal-snapshot.json`, read 2026-10-09)
- Types 114, 116, 197 and 315, read 2026-10-10 with `scripts/pull-portal-catalog.py --menu-ids 114,116,197,315` (23 unauthenticated GETs: `energov/plans/setup/{typeId}`, `energov/permits/setup/{typeId}`, `casetype/instructions/{typeId}/{workClassId}`). The type 114 Zoning Plan Check instructions hash is unchanged from portal map v2 (`44b043e0...`).
- Form pages cited in the routes table: the pinned PDFs in `assets/form-manifest.json` (each entry's `url`)

## Channel correction verified 2026-09-08

The [official Zone Clearance application](https://www.lagunabeachcity.net/home/showpublisheddocument/26718/639216211418770000), page 1, requires new applications through the Public Permit Portal and ties receipt to submission plus the Zoning Plan Check fee. Its footnote offers a City computer or a requested hard-copy accommodation. The current [Applications & Handouts page](https://www.lagunabeachcity.net/government/departments/community-development/planning-zoning/applications-handouts) also directs applications online. Earlier plugin guidance and evals incorrectly treated this as appointment-only.

The current public portal configuration resolves the entry: **type 114, Residential
Planning Entitlements, PLANS module**, type ID `d1c3da85-1287-4578-9312-bdc56e2ae963`
and work-class ID `6c1ac741-1447-403d-a218-ac5715c6d9a9`. The City's instructions
keyed to that exact pair explicitly direct a Zone Clearance Application where no
discretionary entitlement is required. See `assets/portal-maps/zone-clearance-2026-09-08/mapping.json`
for the reviewed mapping and adjacent raw API responses/hash receipts. This supersedes
the earlier same-day unverified-entry finding; no City account was needed to obtain it.

Represent a supported residential Zone Clearance record with `channel: "online"` and
the confirmed type 114 portal mapping. Its work class is **Zoning Plan Check**, the class
the type 114 catalog entry opens (v2 map, read 2026-10-09). The same plan type's ADU class
has its own catalog entry, 182; never file an ADU under 114. Record the work class in
`work-class-selection.json` like any other online record. Its readiness/status still depends on the user's
filing theory, required facts and documents, and prerequisite checks. Never turn a
confirmed route into a claim that the packet is complete or submitted.

The public configuration requires a location, description, square footage, signature,
Applicant and Owner contacts, and one PDF each in Application and Plans. Valuation is
optional. Contractor/Engineer/Architect contacts are conditional; the Contractor contact
validates a license when supplied. The mapped online custom-field layout has no question
groups. Attach further materials required by the actual applicable forms; portal-required
upload categories alone are not the complete project checklist.

The configured success message says a planner will screen the submittal and contact
the applicant for payment. The official form's deemed-received condition still requires
both submission and the Zoning Plan Check fee. Record payment state separately from the
submission receipt; do not describe a submitted/unpaid application as received, complete,
approved, or issued. Actual authenticated UI and live submission have not been tested.
Before a real filing, perform the usual visible portal drift and record checks.

When explaining this route to the user, call for the current Zone Clearance application
and supporting packet. Briefly attribute type 114 to the City’s type/work-class instructions
and say these are verified public configuration requirements; the authenticated screens
and actual filing have not been exercised. This keeps the evidence limit visible without
turning the answer into a technical checklist.

For Zone Clearance preparation, read `zone-clearance-packet.md` before deciding the
Application and Plans PDFs are complete. It identifies non-widget signatures, the
physical PDF page numbering, and the pool-specific document matrix discrepancy.
