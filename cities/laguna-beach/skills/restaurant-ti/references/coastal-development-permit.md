# Laguna Beach — Coastal Development Permit for Restaurant TI

**Operative code:** LBMC Chapter 25.07 (Coastal Development Permits).
Key sections: Sec. 25.07.006 (definitions), Sec. 25.07.008 (exemptions), Sec. 25.07.009 (de minimis waiver), Sec. 25.07.013 (administrative CDP w/ public-hearing waiver), Sec. 25.07.016 (appeals).

---

## Threshold: Is It "Development"?

Sec. 25.07.006 defines "development" extremely broadly. For restaurant TI purposes the relevant prongs are:

1. **Alteration of structure size** — any addition, exterior change, or structural alteration.
2. **Change in intensity of use** — the operative trigger for retail-to-restaurant conversions even where there is no exterior work.
3. **Improvements that change intensity of use** — even interior-only work that adds seating, kitchen capacity, or alcohol service.

**"Intensification of use" rule: a parking test under the parcel's governing plan.** Sec. 25.07.006: "Intensification of use" means "a change in the use of a lot or premises which, based upon the provisions of the underlying zone, requires more off-street parking than did the immediately preceding legal use". So compute required parking for the prior legal use and for the new use with the ratio of the plan that governs the parcel, and compare:
- **Outside a specific plan with its own ratio (Ch. 25.52 applies):** food service is 1 space per 100 sf of gross floor area including outdoor seating, or 1 per 3 seats, whichever is greater; general retail is 1 per 250 sf (25.52.012). Retail-to-restaurant there usually requires more parking, so it usually is intensification.
- **Downtown Specific Plan:** non-residential uses, "office, retail, food service", share one minimum of 3 spaces per 1,000 sf of gross floor area (DSP 2022, Ch. 5 "Parking", incorporated by 25.40; our copy is an extract of the certified plan). Retail to food service at the same floor area requires no more parking, so it is not intensification by parking. Added floor area, outdoor seating that adds gross floor area, or a use the DSP sends back to Ch. 25.52 (places of assembly, cultural uses, visitor accommodations) can still change the count; run the numbers.
- **Other specific plans and zones:** use that plan's ratio first, Ch. 25.52 where the plan defers to it.
When the count does not go up, the change of use is not intensification, and the (A)(2)(b) carve-back does not apply on that ground.

---

## Exemption Carve-Backs (Sec. 25.07.008)

Sec. 25.07.008(A)(2) exempts certain non-SFR improvements from CDP, BUT carves back in:

- **Any change in intensity of use**, tested by required parking as above (outside the DSP most retail-to-restaurant TIs intensify; inside the DSP a same-size retail-to-food change does not)
- **Improvements in highly scenic areas, ESHA, or first-public-road areas** (PCH-fronting and downtown-fronting parcels — most of where restaurants actually exist in Laguna)

Practical effect: run the parking test first. Where required parking goes up, expect a CDP. Where it does not and no other carve-back applies, the TI is an exempt improvement to an existing structure; Planning makes the determination (25.07.012(B)).

---

## CDP Categories (in order of escalation)

| Category | When | Process | Notice | Appeal |
|----------|------|---------|--------|--------|
| **Exempt** | Sec. 25.07.008(A) qualifies AND no carve-back applies | Staff letter | None | None |
| **De minimis waiver (Sec. 25.07.009)** | Not appealable development, no local hearing required, no potential adverse effect on coastal resources, no violation | Director, written waiver; reported to City Council before it takes effect (25.07.009(F)) | Mailed and posted at least 10 calendar days before the decision (25.07.009(E)) | Not available in the appealable area |
| **Administrative CDP w/ public-hearing waiver (Sec. 25.07.013)** | Minor development; no other discretionary approval needed; no objection during waiver period | Director | Public-hearing waiver notice | If no one asks for a hearing within the period, no hearing; otherwise a Director hearing |
| **Non-appealable CDP** | Outside appealable area; standard discretionary review | The body that decides the project's other permit (see below) | Mailed at least 10 days before the hearing (25.07.014(C)) | To City Council; not to CCC |
| **Appealable CDP** | Within appealable area (~300 ft of sea / first public road, between sea and first road, tide/submerged lands, parcels designated appealable in city's LCP) | The body that decides the project's other permit (see below); at least one public hearing (25.07.012(E)) | Mailed within 10 days of accepting the application or at least 10 days before the hearing (25.07.014(B)) | **10-working-day CCC appeal window after local action; effective date delayed until window closes** |

**Who decides the CDP (25.07.012(D)).** The CDP "shall be reviewed in conjunction with whatever other permits are required for the project in the underlying zone; all such permits shall be processed concurrently and the approving body for the coastal development permit shall be the same as that for the permit required by the underlying zoning district or other city regulation." So: with a CUP or Design Review at the Planning Commission (Downtown, nonresidential, 25.05.040(F)(1); every CUP, 25.05.030(E)), the Planning Commission; with only a Director-level permit (an AUP or ADR), the Director; when only a CDP is needed, the Director at a public hearing ((D)(1)). Never name the Planning Commission for every CDP. The CDP is the last entitlement to become effective in the appealable area because of the CCC appeal window.

---

## Appealable Area Test

The parcel is in an appealable area if any of:

- Within 300 ft of the inland extent of any beach or of the mean high tide line where there is no beach
- Within 300 ft of the top of the seaward face of any coastal bluff
- Between the sea and the first public road paralleling the sea
- On tide/submerged lands, beaches, public trust lands
- Designated appealable in the city's certified Local Coastal Program (LCP)

Do not assume appealability from the street name. Use the parcel's appeals-area result from `lookup_property` (site facts). Appealability varies parcel by parcel on S. Coast Highway, Forest Avenue and Ocean Avenue. If site facts return no appeals-area result, say so and ask Planning to confirm; do not guess.

---

## Documentation the Plan Set Must Show

| Item | Required on |
|------|-------------|
| CDP application number | Title sheet, after Planning intake |
| Parcel coastal-zone classification | Sheet G-1 General Notes |
| Appealable / non-appealable status | Sheet G-1 General Notes |
| Use comparison: prior legal use vs proposed restaurant (intensification analysis) | Site plan / cover sheet |
| Parking calculation showing prior vs proposed demand | Site plan |
| CCC appeal window note (if appealable) | Title sheet |

---

## CCC Appeal Window

After local final action on an appealable CDP, the **California Coastal Commission** has **10 working days** to receive an appeal. The CDP — and any concurrent building permit conditioned on the CDP — does NOT become effective until that window closes without an appeal being filed (or until any filed appeal is resolved). Plan the construction-start date accordingly.

---

## Output Findings

- **PASS** — CDP exemption affirmatively documented OR CDP issued and CCC appeal window closed.
- **FAIL** — Restaurant TI scope clearly trips CDP and no application is on file.
- **FLAG** — Cannot determine appealable status from submitted information; need parcel-specific overlay analysis.
- **N/A** — Parcel is verifiably outside the Coastal Zone (rare — confirm with planning).
