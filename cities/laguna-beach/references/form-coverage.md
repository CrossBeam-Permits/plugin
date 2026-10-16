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
- Conditional Use Permit Application (document 26463, re-pinned 2026-10-10)
- Design Review Application (both DRB and Administrative Design Review)
- Floodplain Development Permit Application for Residential Development
- General Plan Amendment Application (document 27396)
- Lot Line Adjustment Application
- Planning Commission Concept Review Application (document 26904)
- Revocable Encroachment Permit Application
- SB 9 Application (fields only in its exhibits; see below)
- SB 684 / Starter Home Revitalization Act Application (document 26902; fields only in
  its exhibits; see below)
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
| Conditional Use Permit Application | 26463/639252307038230000 | 47 | 178 / 208 | 2.0.0 | Re-pinned later the same day (see below). The City replaced the file under the same document id; the July file (53 pages, 194 fields) is in `retired_forms`. |
| Planning Commission Concept Review Application | 26904/639227554954730000 | 2 | 45 / 45 | 1.0.0 | New on the page (not in the 2026-08-14 inventory). |
| SB 684 / Starter Home Revitalization Act Application | 26902/639227554030430000 | 133 | 206 / 229 | 1.0.0 | New on the page. Link text "Start Home Revitalization Act (SB684)". |
| General Plan Amendment Application | 27396/639263715770130000 | 17 | 37 / 36 | 1.0.0 | New on the page ("September 2026"). |

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
- **Conditional Use Permit**: project location, the three contact blocks (the applicant
  and representative rows share field names, so they are exact widget targets), the
  project description (page 2), and the Project Summary Tables (page 25). The new file
  prints the City's earlier fee amounts in submittal requirement 1: they match the
  February 2026 schedule (for example Zoning Plan Check $945 / $4,743, Minor CUP $4,931), not
  the adopted FY26/27 schedule ($1,390 / $6,975 / $7,250, MFS pp. 29 and 31) that
  `requirements/fees/fee-schedule.json` and the fee estimate use. Quote fees from the fee
  estimate, never from the printed form, and tell the applicant the City confirms the
  amount at invoicing. The new file also replaces the fillable deposit
  agreement in Exhibit A with a deposit table and the City's deposit procedure (the
  agreement now comes with the first incomplete letter), and adds the owner signature to
  the Exhibit I affidavit. `requirements/planning/conditional-use-permit.md` lists the
  same deliverables (unchanged in this edition) and notes the Exhibit A change. Fees
  still come from the fee estimate.
- **Planning Commission Concept Review**: location, APN, current use, building square
  footage, parking spaces, lot area, and the owner and applicant name, phone, address, and
  email (one address line each, so `owner.full_address` / `applicant.full_address`). The
  submittal checklist boxes, the header DATE, and the City's Concept Review Number stay
  review-only.
- **SB 684 / SHRA**: only the Project Summary Tables (page 41). As with SB 9, the City
  built the application sections without fields: the Project Information table (page 1)
  and the bundled CDP application form (page 77) are `manual_sections`. Appendix A
  (pages 15-25) is the City's reference checklist, "not part of the application". The
  package's checklists cite the wrong exhibit letter for the CDP form (see `planning-routing.md`).
- **General Plan Amendment**: project location, the three contact blocks, and the
  proposed amendment (page 3). The Application Type boxes (Initiation of Amendment /
  General Plan Amendment) are not fields, so they are a `manual_sections` entry.

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
- Retired from this plugin's manifest is not the same as refused by the City. The counter
  has accepted the one-page form. When an applicant already filled it, list "the current form
  adds a signed stormwater certification page" under Tidy-ups, not the fix list, unless a City
  note says the counter now returns the one-page form. New filings use the two-page form.

## Uncovered Planning application types

These are out of scope for V1 form filling and packet assembly:

1. Artist Occupancy Permit Application
2. Historic Register Placement Application
3. Reasonable Accommodation Application
4. SB 330 Application
5. Tentative Parcel and Tract Map Application
6. Wireless Facility Permit Application

Each needs a source receipt, an exact semantic field map, and a round-trip eval before
it is supported. `pending_sources` in the manifest is empty: the five forms queued there
on 2026-10-09 are pinned above, and the three applications new on the 2026-10-10 page
(Planning Commission Concept Review, SB 684, General Plan Amendment) are pinned too.
Each pinned form's filing route is in `planning-routing.md`, "Filing routes for the other
pinned Planning forms".

Short-Term Lodging / Administrative Use Permit is also outside the residential V1 lane;
its link serves a City account login page, not a PDF. Never silently substitute Design
Review, CUP, or Zone Clearance.

Source page: https://www.lagunabeachcity.net/government/departments/community-development/planning-zoning/applications-handouts (direct script fetches return HTTP 403; applicants download in a visible browser).
