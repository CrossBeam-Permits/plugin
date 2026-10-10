# V1 form coverage

Coverage is a closed list. A route not listed as supported below is not permission to
adapt another form. Name the uncovered application, preserve the known filing theory,
and stop that record as `unsupported_form` / `needs_source` with the City's Applications
& Handouts page as the handoff.

Every form has a `status` in `assets/form-manifest.json`. Fill only `pinned` forms.
`needs_source` means the City links a revision this plugin has not pinned and mapped.

## Supported and SHA-pinned

Planning:

- ADU & JADU Application (document 27032; see "Planning forms pinned 2026-10-10")
- Coastal Development Permit Application
- Conditional Use Permit Application
- Design Review Application (both DRB and Administrative Design Review)
- Floodplain Development Permit Application for Residential Development
- Lot Line Adjustment Application
- Revocable Encroachment Permit Application
- SB 9 Application (fields only in its exhibits; see below)
- Sign Permit Application (no fillable fields; see below)
- Temporary Use Permit Application
- Variance Application
- Zone Clearance Application

Building:

- Building Permit Application with the Stormwater Quality Certification (2 pages, 96
  fields; field map 3.0.0). This is the form the portal's type 183 and type 214
  attachment instructions link. Use it for every Building record that asks for the
  "Permit Application". See "Building application revision" below.
- Electrical, Mechanical, and Plumbing Permit Application.

Other Planning forms must still be checked against the current linked revision before use.

## Planning forms pinned 2026-10-10

On 2026-10-10 a headless browser loaded the Applications & Handouts page, read its
document links, and fetched each PDF from inside the loaded page. Each manifest entry
carries the receipt: link text, document id and ticks, HTTP Last-Modified, PDF dates,
SHA-256, page and field counts. A direct script download still returns HTTP 403
(AkamaiGHost); applicants download in their own visible browser
(`form-source-policy.md`) and `check-source-freshness.py` verifies the file.

| Form | City link (document/ticks) | Pages | Fields / widgets | Map | What changed since the 2026-08-14 inventory |
|---|---|---|---|---|---|
| ADU & JADU Application | 27032/639238583151930000 | 43 | 231 / 258 | 2.0.0 | New document replacing 26710. Same field tree; the ADU and JADU application and deposit fee rose from $945 to $1,390. |
| SB 9 Application | 26958/639232726993730000 | 105 | 200 / 226 | 1.0.0 | New document replacing the DRAFT 26708. Now bundles a CDP application package. |
| Sign Permit Application | 26375/639192070419070000 | 36 | 0 / 0 | 1.0.0 (no mappings) | Unchanged. |
| Temporary Use Permit Application | 26473/639198118552870000 | 10 | 31 / 31 | 1.0.0 | Unchanged. |
| Revocable Encroachment Permit Application | 26469/639198116032630000 | 17 | 23 / 39 | 1.0.0 | Unchanged. |
| Lot Line Adjustment Application | 26467/639198115671300000 | 12 | 67 / 67 | 1.0.0 | Unchanged. |

What each map fills:

- **ADU & JADU**: application type boxes, project location, the three contact blocks,
  the five-line project description, the rent-reporting estimate (page 9), and the
  Project Summary Tables (page 34). Never fill document 26710; it is in `retired_forms`.
- **SB 9**: only the Project Summary Tables (page 29). The City built the application
  sections without form fields: the Lot Split sections I-III (pages 2-5), the Two-Unit
  sections I-III (pages 8-10), the Exhibit H affidavit name line (page 38), and the
  bundled CDP application form (page 49). The map lists them as `manual_sections`;
  `fill-form.py` prints them and copies them into `review-and-sign.json`. The applicant
  completes them by hand. The SB 9 application is not complete without a copy of the
  approved, final CDP, so the CDP is its own earlier filing.
- **Sign Permit**: the City PDF has no form fields. `fill-form.py` refuses its map and
  names the pages to complete by hand (application form page 3, Exhibits A-C). Verify the
  file with `check-source-freshness.py` and give the applicant the values to transcribe.
- **Temporary Use Permit**: event location, the three contact blocks, the six-line event
  description, and the owner name in the Exhibit A affidavit.
- **Revocable Encroachment Permit**: project location, the three contact blocks (the City
  reused one field name across blocks, so these are exact widget targets), the six-line
  description, and the affidavit owner name. Pages 8-9 are the recordable license
  agreement the applicant completes after DRB approval; they stay review-only.
- **Lot Line Adjustment**: the four parcel blocks (address, APN, owner and owner
  contacts), the affidavit owner name, and the Owners / Existing APNs / Proposed Parcel
  table on Exhibits C, D, and E. The City assigns the LLA number.

Every signature, signature date, and City-use field stays review-only. Deposit
agreements, notice addresses, and the water quality form stay review-only, as on the
other Planning packages.

## Building application revision (2026-10-09)

- Type 183 and type 214 attachment instructions say: "Applicants must submit the
  following: Building Permit application (link to form) Project plans Please be sure to
  sign applications before uploading into the permit portal." The link is
  `http://gis.lagunabeachcity.net/MapsLinks/PublicGIS/BuildingPermitApplication.pdf`.
  [source: EnerGov `casetype/instructions` for types 183 and 214, public GET, 2026-10-09]
- That `http://` link returned HTTP 404. The same path over `https://` returns the pinned
  2-page form (PDF modified 2024-09-27). Fetch it over https; it is not behind Akamai.
- Page 1 is the application. Page 2 is the Stormwater Quality Certification, signed by
  "the applicant authorizing construction activities" (LBMC Title 16).
- The one-page form (document 216) is retired from the manifest. It has no stormwater
  certification. The City's Building Applications & Forms page linked it on 2026-08-22;
  that page returned HTTP 403 on 2026-10-09, so whether it still links document 216 is
  unverified. The two-page form's page 1 has every block of the old form except the
  MultiFamily box. If the City asks for the old form by name, ask the Building Division,
  (949) 497-0715, which form it wants; do not keep two Building maps.

## Uncovered Planning application types

These are out of scope for V1 form filling and packet assembly:

1. Artist Occupancy Permit Application
2. Historic Register Placement Application
3. Reasonable Accommodation Application
4. SB 330 Application
5. Tentative Parcel and Tract Map Application
6. Wireless Facility Permit Application
7. Planning Commission Concept Review (document 26904 on the 2026-10-10 page)
8. Start Home Revitalization Act (SB 684) (document 26902 on the 2026-10-10 page)
9. General Plan Amendment (document 27396 on the 2026-10-10 page)

Each needs a source receipt, an exact semantic field map, and a round-trip eval before
it is supported. `pending_sources` in the manifest is empty: the five forms queued there
on 2026-10-09 are pinned above.

Short-Term Lodging / Administrative Use Permit is also outside the residential V1 lane;
its link serves a City account login page, not a PDF. Never silently substitute Design
Review, CUP, or Zone Clearance.

Source page: https://www.lagunabeachcity.net/government/departments/community-development/planning-zoning/applications-handouts (direct script fetches return HTTP 403; applicants download in a visible browser).
