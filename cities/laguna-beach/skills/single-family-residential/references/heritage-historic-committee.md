# Laguna Beach - Heritage Committee Review (Historic Resources)

Sources:

- LBMC **Ch. 25.45 HISTORIC PRESERVATION** — confirmed verbatim via scrape (the City source document (not included in this plugin), scraped 2026-05-12). Hosted at ecode360.com/42901400.
- City handout: `heritage-committee-review-submittal.pdf` (Heritage Committee submittal checklist, rev. 2/10/21)
- City handout: `historic-assessment-submittal.pdf` (companion document for the historic assessment report itself)
- Citywide reference: `../../city-reference/SKILL.md` (Heritage Committee row in permit decision matrix)

Use this reference when a new SFR replaces, alters, or demolishes a structure on the same lot that is, or may be, a historic resource (§25.45.004). Law as of 2026-10-10.

---

## Governing Section

Heritage Committee review is established under **LBMC Chapter 25.45 (Historic Preservation)** — section number confirmed via the 2026-05-12 scrape. The committee advises the City Council and the design review authority (DRB / Planning Commission / Director) on:

- Alterations to historic structures and properties on the city's Historic Register.
- Requests to add a structure to the Historic Register.
- Demolition applications for historic resources (§25.45.014).
- Historic-assessment reports submitted as part of plan check.

**Meeting schedule:** Heritage Committee usually meets the **3rd Monday of each month at 6:00 PM** in the City Council Chambers. Verify exact date and submittal deadline with city staff.

---

## When Heritage Review Is Triggered for a New SFR

The code trigger is whether the existing structure is a **historic resource**, not its age. §25.45.004 (as amended by Ord. 1732) defines a historic resource as a property or structure that "(1) is listed on the City's historic register, (2) is listed on the California Register of Historical Resources, (3) has been officially determined to be eligible for the California Register ... (4) is listed on the National Register of Historic Places, (5) has been officially determined to be eligible for the National Register ... or (6) the City is mandated by law to treat as a historic resource based on substantial evidence in light of the whole record." The absence of a recorded preservation agreement is not, on its own, conclusive evidence that a property is not on the City register.

A new SFR project triggers Heritage Committee review when it will demolish, relocate, or alter a historic resource on the lot:

1. **Demolition** follows §25.45.014: the department schedules the Heritage Committee within 30 days of a complete application; the design review authority acts after CEQA and the Committee's recommendation, at a public hearing; demolition "require[s] that the applicant obtain a Coastal Development Permit".
2. **Alteration** follows §25.45.010: Administrative Design Review under §25.05.040(B)(3) for qualifying minor work, or Design Review under §25.05.040(B)(1)(d) for major modifications; the Heritage Committee reviews and recommends first either way.

**Age alone.** No code section makes 50 years of age a trigger. Staff may still ask for a historic resource assessment for an older structure so they can decide item (6). UNSETTLED; confirm with Planning at pre-application.

If the existing structure is not a historic resource and staff do not ask for an assessment, this reference does not apply.

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

The new SFR review cannot short-circuit Heritage by demolishing a historic resource under a separate demolition permit before the Heritage path closes. Run Heritage **before** demo.

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
- Existing structure age: [years] (context only; not a code trigger)
- Historic resource status (§25.45.004): [Listed | Eligible | Not listed | Unknown]
- Heritage Committee review status: [Required - not yet scheduled | Pending | Cleared | N/A]
- Demolition waiting-period extension: [None | Up to 180 days | Expired]
```

Cite **LBMC Ch. 25.45** (or the current re-codified section) and reference the historic-assessment handout. Do not treat Heritage as a soft / advisory step — the design review authority's ability to extend the demolition waiting period up to 180 days is a hard schedule lever and must be flagged early in intake.

---

## Cross-References

- `../../city-reference/SKILL.md` — Heritage row in citywide permit decision matrix.
- `../../demolition/SKILL.md` — demo-permit-specific Heritage routing.
- `../SKILL.md` — Step 2 (Planning Route) calls this reference when a historic resource is on the lot.
