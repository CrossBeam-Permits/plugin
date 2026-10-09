# Laguna Beach - Heritage Committee Review (50+ Year Structures)

Sources:

- LBMC **Ch. 25.45 HISTORIC PRESERVATION** — confirmed verbatim via scrape (the City source document (not included in this plugin), scraped 2026-05-12). Hosted at ecode360.com/42901400.
- City handout: `heritage-committee-review-submittal.pdf` (Heritage Committee submittal checklist, rev. 2/10/21)
- City handout: `historic-assessment-submittal.pdf` (companion document for the historic assessment report itself)
- Citywide reference: `../../city-reference/SKILL.md` (Heritage Committee row in permit decision matrix)

Use this reference when a new SFR replaces, alters, or demolishes a structure 50 years or older on the same lot. The trigger is the **age of the existing structure**, not the construction value of the new SFR.

---

## Governing Section

Heritage Committee review is established under **LBMC Chapter 25.45 (Historic Preservation)** — section number confirmed via the 2026-05-12 scrape. The committee advises the City Council and the design review authority (DRB / Planning Commission / Director) on:

- Alterations to historic structures and properties on the city's Historic Register.
- Requests to add a structure to the Historic Register.
- Demolition applications for structures 50 years or older.
- Historic-assessment reports submitted as part of plan check.

**Meeting schedule:** Heritage Committee usually meets the **3rd Monday of each month at 6:00 PM** in the City Council Chambers. Verify exact date and submittal deadline with city staff.

---

## When Heritage Review Is Triggered for a New SFR

A new SFR project triggers Heritage Committee review when:

1. **An existing structure 50 years or older is on the lot** and the new SFR will demolish, relocate, or substantially alter it; OR
2. **The lot is already on the city's Historic Register** (alteration of any contributing structure or character-defining feature is in scope); OR
3. **The Historical Assessment** submitted with the permit identifies the existing structure as historically or architecturally significant (regardless of age).

If none of those apply (i.e., the existing structure is under 50 years old and the lot is not Register-listed), Heritage Committee review is not required and this reference does not apply.

---

## Process and Timing

The Heritage Committee review path runs in parallel with, and BEFORE, the demolition permit and the DRB hearing:

1. **Historic Assessment submittal.** Applicant submits a historical assessment report (per the city `historic-assessment-submittal.pdf` handout) describing the existing structure's age, architectural style, integrity, and significance.
2. **Heritage Committee review of demolition application** — committee reviews **within 30 days** of a complete demolition application.
3. **Committee recommendation** — committee makes one of:
   - No objection to demolition (proceed to DRB / building permit).
   - Recommendation for Historic Register placement (advisory to Council).
   - **Recommendation for an extended demolition waiting period** to allow relocation of the structure.
4. **DR authority demolition waiting-period extension** — the design review authority **may extend the demolition waiting period up to 180 days** if relocation of the structure is deemed imminent or feasible.
5. **DRB hearing on the new SFR** — runs in parallel; DRB cannot issue final design approval for the replacement SFR until the Heritage Committee path has cleared (or the 180-day waiting period has run).
6. **Demolition permit** — only issued after the Heritage Committee has acted and any extended waiting period has expired.
7. **Building permit for new SFR** — issued after demolition permit and after DRB approval.

The new SFR review cannot short-circuit Heritage by demolishing the 50+ year structure under a separate demolition permit before the Heritage path closes. Run Heritage **before** demo.

---

## Submittal Add-Ons When Heritage Is Triggered

Per `heritage-committee-review-submittal.pdf` (rev. 2/10/21), the Heritage Committee submittal is **8 collated copies** of:

1. **Application for placement on the Historic Register** (if not already listed).
2. **Historic Assessment OR SOIS Report** — typically prepared by a qualified historian or architectural historian meeting Secretary of the Interior's Professional Qualification Standards (SOIS).
3. **Letter of explanation** with owner / applicant name and contact info.
4. **Color photographs** on 8.5x11 paper — front, back, both sides (max 4 photos per page).
5. **Site plan + floor plans + exterior elevations** at 11x17 (the committee specifically restricts to 11x17 — not 24x36) for any proposed improvements / additions.
6. **Staking suggested** for additions and exterior alterations — the committee often continues the item to a future meeting if staking is absent.
7. **Historic photos / publications** where available.
8. **Renderings, color & material samples** for additions.

These are in addition to the standard `submittal-requirements.md` package.

**Critical scheduling note:** 8 copies + 3rd-Monday meeting + likely-continuance-if-not-staked combination means Heritage routing can add 30–60 days minimum to a new-SFR schedule when triggered. Flag Heritage requirements at intake, not late in plan review.

---

## Output Format Addition

When Heritage review is triggered, add a row to the city overlay output:

```markdown
**Heritage / Historic:** PASS | FAIL | FLAG | N/A
- Existing structure age: [years]
- Historic Register status: [Listed | Eligible | Not listed | Unknown]
- Heritage Committee review status: [Required - not yet scheduled | Pending | Cleared | N/A]
- Demolition waiting-period extension: [None | Up to 180 days | Expired]
```

Cite **LBMC Ch. 25.45** (or the current re-codified section) and reference the historic-assessment handout. Do not treat Heritage as a soft / advisory step — the design review authority's ability to extend the demolition waiting period up to 180 days is a hard schedule lever and must be flagged early in intake.

---

## Cross-References

- `../../city-reference/SKILL.md` — Heritage row in citywide permit decision matrix.
- `../../demolition/SKILL.md` — demo-permit-specific Heritage routing.
- `../SKILL.md` — Step 2 (Planning Route) calls this reference when a 50+ year structure is on the lot.
