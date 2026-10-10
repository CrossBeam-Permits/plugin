# V1 form coverage

Coverage is a closed list. A route not listed as supported below is not permission to
adapt another form. Name the uncovered application, preserve the known filing theory,
and stop that record as `unsupported_form` / `needs_source` with the City's Applications
& Handouts page as the handoff.

Every form has a `status` in `assets/form-manifest.json`. Fill only `pinned` forms.
`needs_source` means the City links a revision this plugin has not pinned and mapped.

## Supported and SHA-pinned

Planning:

- Coastal Development Permit Application
- Conditional Use Permit Application
- Design Review Application (both DRB and Administrative Design Review)
- Floodplain Development Permit Application for Residential Development
- Variance Application
- Zone Clearance Application

Building:

- Building Permit Application with the Stormwater Quality Certification (2 pages, 96
  fields; field map 3.0.0). This is the form the portal's type 183 and type 214
  attachment instructions link. Use it for every Building record that asks for the
  "Permit Application". See "Building application revision" below.
- Electrical, Mechanical, and Plumbing Permit Application.

Other Planning forms must still be checked against the current linked revision before use.

## Needs source: ADU & JADU Application

The 2026-09-08 source-page audit found the City now links ADU document **27032**:
https://www.lagunabeachcity.net/home/showpublisheddocument/27032/639238583151930000

The manifest pins obsolete document **26710**. On 2026-10-09 the new link returned HTTP
403 (AkamaiGHost) to a script and to headless Chromium, so it could not be inspected.
`adu-application` is `needs_source`; `fill-form.py` refuses its map. Download the new
revision in the applicant's visible browser (see `form-source-policy.md`), then pin and
remap it. Never fill document 26710, even when its old URL still serves a valid PDF.

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

## Eleven uncovered Planning application types

These are out of scope for V1 form filling and packet assembly:

1. Artist Occupancy Permit Application
2. Historic Register Placement Application
3. Lot Line Adjustment Application
4. Reasonable Accommodation Application
5. Revocable Encroachment Permit Application
6. SB 9 Application
7. SB 330 Application
8. Sign Permit Application
9. Temporary Use Permit Application
10. Tentative Parcel and Tract Map Application
11. Wireless Facility Permit Application

The five most requested are queued in the manifest's `pending_sources`. Each needs a
source receipt, an exact semantic field map, and a round-trip eval before it is supported.
On 2026-10-09 every one returned HTTP 403 (AkamaiGHost) to a script and to headless
Chromium, so none was added. Last known links, from the 2026-08-14 link inventory:

| Application | Last seen revision | Status | Last known URL |
|---|---|---|---|
| SB 9 Application | Updated August 2026 (file marked DRAFT) | needs_source, 403 | https://www.lagunabeachcity.net/home/showpublisheddocument/26708/639216201110030000 |
| Sign Permit Application | Updated July 2026 | needs_source, 403 | https://www.lagunabeachcity.net/home/showpublisheddocument/26375/639192070419070000 |
| Temporary Use Permit Application | Updated July 2026 | needs_source, 403 | https://www.lagunabeachcity.net/home/showpublisheddocument/26473/639198118552870000 |
| Revocable Encroachment Permit Application | Updated July 2026 | needs_source, 403 | https://www.lagunabeachcity.net/home/showpublisheddocument/26469/639198116032630000 |
| Lot Line Adjustment Application | Updated July 2026 | needs_source, 403 | https://www.lagunabeachcity.net/home/showpublisheddocument/26467/639198115671300000 |

The links can change between revisions. Confirm each on the source page before pinning.

Short-Term Lodging / Administrative Use Permit is also outside the residential V1 lane.
If the City exposes PC Concept Review or SB 684 as a separate current application, those
are likewise unsupported until each has an official source receipt, semantic field map,
and behavior eval. Never silently substitute Design Review, CUP, or Zone Clearance.

Source page: https://www.lagunabeachcity.net/government/departments/community-development/planning-zoning/applications-handouts (visible-browser verification required; direct and headless fetches return HTTP 403).
