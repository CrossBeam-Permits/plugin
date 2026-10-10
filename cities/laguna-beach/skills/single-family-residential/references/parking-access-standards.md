# Laguna Beach - SFR Parking and Access Standards

Sources:

- LBMC Chapter 25.52 SFR extract: the City source document (not included in this plugin)
- LBMC Chapter 25.53 SFR extract: the City source document (not included in this plugin)
- LBMC Section 25.10.008 side/front/rear yard limits: the City source document (not included in this plugin)

---

## Required SFR Parking

Section 25.52.012(G) requires:

| Dwelling size | Required parking |
|---------------|------------------|
| <3,600 sf gross floor area | 2 covered spaces |
| >=3,600 sf gross floor area | 2 covered spaces + 1 additional uncovered space |

For a dwelling at or above 3,600 sf GFA, the additional uncovered space may be replaced by an in-lieu fee, parking reduction, or parking alternative only when supported by a parking demand study and approved through the applicable city process.

---

## Plot Plan Requirements

Section 25.52.006 requires the building permit plot plan to show:

- Parking spaces and access.
- Dimensions of spaces and access aisles.
- Traffic circulation pattern.
- Adjacent and directly across on-street parking.

Reject or flag any new SFR plan set that lists parking counts but does not dimension the parking/access layout.

---

## Tandem and Additional Covered Parking

Tandem parking under Section 25.52.008(D) is allowed for required residential spaces only if:

1. No more than 2 required spaces are placed behind each other;
2. The spaces serve the same dwelling unit;
3. All required parking spaces are independently accessible; and
4. DRB/Planning Commission approval is granted under Section 25.52.012(G).

Section 25.52.012(G) also requires DRB/Planning Commission review for additional covered parking. The city evaluates neighborhood consistency, residential design guideline consistency, and impacts to neighboring properties and the public right-of-way.

---

## Yard Limits Affecting Parking

R-1 front yards may not be used for regular/constant vehicle parking.

R-1 side yards may not be used for regular/constant vehicle parking except for the required additional parking space when approved under the parking chapter.

For rear-yard garages entered from an alley, maintain 25 ft from the opposite side of the alley and at least 5 ft from the rear lot line.

---

## Chapter 25.53 Access

Section 25.53.004 requires usable vehicular right-of-way access to required parking facilities.

Section 25.53.006 requires new development to provide street and access improvements, including curbs, gutters, sidewalks, and paving, as determined by the city engineer.

For already-developed property, Chapter 25.53 applies when additions or alterations, individually or cumulatively, exceed 50% of existing allowable population density or intensity of use. When that threshold fires, the access/street-improvement rules apply as if the property were vacant.

---

## Output Template

```markdown
## Parking and Access - LBMC Ch. 25.52 / 25.53
**Gross floor area:** [sf]
**Required parking:** [2 covered | 2 covered + 1 uncovered]
**Provided parking:** [counts and dimensions]
**Tandem/additional covered parking:** YES | NO
**Parking study/alternative needed:** YES | NO
**Access from usable vehicular ROW:** PASS | FAIL | FLAG
**Street/frontage improvements:** Required | Not required | City Engineer determination needed
**Result:** PASS | FAIL | FLAG
```
