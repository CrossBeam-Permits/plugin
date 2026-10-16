# Laguna Beach — Heritage Committee / Historic Resources for Commercial TI

**Authority:** LBMC **Chapter 25.45** (Historic Preservation), current **§25.05.040(B)(1)(d)** and **(B)(3)(a)(iv)**, and **§25.05.065(F)** (demolition newspaper notice). Ord. 1732 replaced the former interior-only historic exception with major/minor historic-action routes.

**Critical context:** The City's **1980-81 Historic Resources Inventory** identified **852 pre-1940 homes and commercial buildings**. Many Downtown, Forest Ave, North Laguna, and Heisler Park commercial properties are on the inventory. A property's age alone is not a trigger; status is (§25.45.004).

---

## 1. When Heritage Review Is Required

| Condition | Heritage trigger |
|-----------|------------------|
| Building is on the City's Historic Register | Heritage Committee review required for any alteration; DR for any change visible from public; Mills Act contract eligibility |
| Building is on the 1980-81 Historic Resources Inventory but NOT on Register | Heritage Committee review at DRB/PC discretion; historic assessment submittal may be required |
| Building is old but on no register, listing or inventory | **No age trigger.** Age alone does not make a property a historic resource (§25.45.004). Review only if Planning finds substantial evidence that it is a historic resource (§25.45.004 item (6), the CEQA standard); the Director may require an assessment (§25.45.010(C)) |
| Demolition of historic-register structure | Published newspaper notice required (§25.05.065(F)); up to 180-day waiting period |

Laguna keys historic review off the property's status, not its age: City register, California or National Register listing or official eligibility, or substantial evidence (§25.45.004 as amended by Ord. 1732). The 1981 inventory "is ineffective for the purposes of creating a presumption of historicity" (§25.45.002(H)), but an inventory rating (`historic.rating` in `lookup_property`) flags the property for a possible City-paid historic assessment (§25.45.010(C); `../../guide/references/historic-properties.md`). When status is unclear, FLAG for Planning; do not infer it from the year built.

---

## 2. Current major/minor historic-action route

Current §25.05.040(B)(2)(d) gives Zone Clearance to interior modifications that do not modify the exterior, but historic-resource actions are separately classified:

- Major modifications, alterations, or other actions pertaining to historic resources that do not qualify for ADR require Design Review under `(B)(1)(d)`.
- Qualifying minor alterations require ADR under `(B)(3)(a)(iv)` and cannot use the hearing waiver.
- Under amended §25.45.010, the Heritage Committee must review and recommend before the ADR matter is scheduled or before the major matter goes to DRB/Planning Commission.

Do not use former `(B)(2)(c)` or automatically equate every interior project in an old building with Planning Commission Design Review. Establish historic-resource status and classify the action.

---

## 3. Historic Assessment Submittal

When required, the historic assessment package consists of:

| Document | Doc ID | Purpose |
|----------|--------|---------|
| Historic Assessment Submittal | 5343 | Qualified historian's narrative + photo documentation + significance analysis |
| Historic Plan Review Submittal | 8904 | Plan-set markup showing what is being altered vs preserved |
| Heritage Committee Review Submittal | 5337 | Application form for Heritage Committee advisory review |

The historic assessment must be prepared by a qualified historian meeting the Secretary of the Interior's Professional Qualifications Standards (history, architectural history, or historic preservation).

---

## 4. Heritage Committee Role

The Heritage Committee:

- **Advises** the City Council, Planning Commission, and Design Review Board on:
  - Alterations to historic structures
  - Historic Register placement requests
  - Mills Act contract recommendations
- **Reviews** historic assessment submittals for completeness and accuracy
- **Recommends** conditions of approval that preserve historic character
- **Does NOT** have independent approval authority — its role is advisory to the discretionary body (Planning Commission for non-residential)

Heritage Committee meetings are typically held monthly. Application processing is typically 30–60 days for a recommendation, layered on top of the Planning Commission DR timeline.

---

## 5. Mills Act Contracts (Property Tax Reduction)

The Mills Act provides property tax reduction for owners of qualified historic properties who commit to maintenance and rehabilitation per the Secretary of the Interior's Standards. The Heritage Committee makes Mills Act contract recommendations to City Council.

For commercial TIs on historic-register properties, alignment of the TI scope with Mills Act standards (where applicable) may be a Planning Commission condition of approval. Use the Secretary of the Interior's Standards for Rehabilitation as the design baseline.

---

## 6. Demolition of Historic-Register Structures (§25.05.065(F))

Demolition of a structure on the City's Historic Register requires:

- **Published newspaper notice** in addition to standard mailed notice (§25.05.065(F))
- **Heritage Committee advisory review**
- Up to **180-day waiting period** (per Heritage program practice) during which the City and interested parties may attempt to negotiate preservation
- Planning Commission DR for the replacement structure

For commercial TI, demolition is rare — but partial demolition of historic-register facades, storefronts, or rooflines should be carefully evaluated against §25.05.065(F).

---

## 7. Architectural Treatment Standards

For TIs on historic structures, the Planning Commission typically conditions approval on Secretary of the Interior's Standards for Rehabilitation:

- Retain historic character-defining features (storefront systems, transom windows, cornices, signage bands, brick or stucco wall systems, original openings)
- Use compatible new materials (in-kind where possible)
- Avoid removal or alteration of historic features unless deteriorated beyond repair
- New work should be differentiated from the old but compatible in scale, color, material, and character
- New exterior signage scaled and placed to respect the original signage band

---

## 8. Required Findings Output

For each commercial TI heritage review, output:

```markdown
**Building age:** <year built / age in years>
**1980-81 Historic Resources Inventory status:** On inventory | Not on inventory | Verify with city records
**Historic Register status:** On register | Not on register
**Inventory rating (site facts):** <rating> | none
**Current historic-action route:** Major Design Review | Minor ADR | Interior Zone Clearance | needs_source
**Historic assessment submittal required:** YES (doc IDs 5343 / 8904 / 5337) | NO
**Heritage Committee review required:** YES (advisory to Planning Commission) | NO
**Demolition of historic-register structure in scope:** YES (newspaper notice + 180-day waiting period) | NO
**Mills Act contract status:** Active | Pending | None | N/A
**Compliance with Sec. of Interior's Standards for Rehabilitation:** PASS | FAIL | FLAG | N/A
```

Cite Ch. 25.45 for the Heritage Committee program, current §25.05.040(B)(1)(d)/(B)(3)(a)(iv) for routing, and §25.05.065(F) for demolition notice.
