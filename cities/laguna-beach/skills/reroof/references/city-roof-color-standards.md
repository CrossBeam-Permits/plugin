# Laguna Beach — Roof Color, Finish, and Pre-Issuance Approval

Source: City of Laguna Beach Community Development / Building Division handout **"REROOFING"** (includes the
**COLOR GUIDE** at the end of the packet), received from the City **2026-08-12**. Raw source of record:
the City source document (not included in this plugin)
(verbatim pandoc conversion; the City's photo examples are extracted to the sibling `reroofing-guide/media/` dir).

Provenance date for everything in this file: **2026-08-12**. Contact for color questions: Building Division
the Building Division; design-review questions go to the Planning Division. Phone numbers: `../../city-reference/references/contacts-hours.md`.

**This is a city delta.** The state reroof skill (`california-baseline.md`) has no roof-color standard —
California regulates roof *fire class* and *solar reflectance*, not hue. Laguna Beach restricts roof color and
finish citywide, and requires City approval of materials and colors **before the permit is issued**.

---

## The rule in the City's words

> **Approval:** Materials and colors must be approved prior to permit issuance

> **Do:** Choose dark brown, dark gray or black for flat roofs
>
> **Do:** Apply a matte finish coating to metal roofs to prevent glare
>
> **Don't:** Choose banned light colors like white, tan, or light gray

The City's own standard project-description template repeats the rule as a line the applicant is expected to
copy onto the application:

> Tear off and reroof with GAF Timberline composition shingles ESR-1475 (Color: Charcoal Gray): 2811 SF.
> (1) layer of synthetic underlayment. \*No light or white colors in Laguna Beach\* CO/Smoke Detectors
> Required\* Sheathing Inspection Required \* Class A Fire Rated Materials Required

> ***Note: Additional requirements may apply to historic properties***

---

## Color and finish standards by roof material

| Roof material | Not acceptable | Acceptable | City's stated basis |
|---|---|---|---|
| **Any roof (general)** | Light-colored roofs — white, tan, light gray; standing-seam metal with no matte finish; reflective roof materials | Colors that are neither light nor close to white | COLOR GUIDE, "Avoid" list |
| **Shingle** | Light hues or hues closely resembling white | "hues that are neither light nor closely resemble white" | COLOR GUIDE, Shingle Roof Material |
| **Metal** | Reflective / glare-producing finish (untreated standing seam) | Acceptable **with condition**: matte finish coating applied to eliminate reflective glare | COLOR GUIDE, Metal Roof Material |
| **Membrane / flat (TPO, EPDM, PVC)** | White, light tan, light grey | Dark brown, dark grey, or black | COLOR GUIDE, Roof Membrane/Flat roof material |

The COLOR GUIDE is photographic, not a numbered swatch list — there is **no published LRV, SRI, or color-number
threshold**. Judging a proposed color is a reasoning step against the City's stated categories and photo
examples, not a lookup. When a submitted color sits near the line (medium gray, weathered wood, light bronze),
**FLAG for the Building Division's color approval** rather than passing or failing it outright.

### The City's photo examples (raw corpus paths)

Base dir: the City source document (not included in this plugin)

| Image | What the City is showing |
|---|---|
| `image3.png`, `image4.png`, `image5.png` | "Avoid" — light colored roofs, unmatted standing-seam metal, reflective materials |
| `image6.png` | Shingle — **acceptable** colors |
| `image7.png` | Shingle — **not acceptable** colors |
| `image8.png`, `image9.png` | Metal — acceptable **with** matte finish condition |
| `image10.png`, `image11.png`, `image12.png` | Membrane/flat — **not acceptable** (white, light tan, light grey) |
| `image13.png`, `image14.png`, `image15.png` | Membrane/flat — **acceptable** (dark brown, dark grey, black) |

---

## Approval happens before permit issuance

Materials and colors must be approved **prior to permit issuance**, which makes the color submittal a gate on
issuance, not a field/inspection item. The City's "3 Steps to Apply" names what the applicant brings:

> **Gather Materials:** Collect your completed application, site plan, roof specifications, material details
> and color samples

A reroof application that names a product but no color — or a color with no sample/swatch — is **incomplete
for issuance**, even when every state-code check passes. Say that plainly rather than passing the application.

**Historic properties:** the handout warns that "Additional requirements may apply to historic properties"
without stating them. Do not invent the extra review. The historic-resource trigger (register, state or national listing, or the 1981 inventory rating; not age, LBMC 25.45.004) lives in
`../../city-reference/SKILL.md` §5 (Historic Resources) and
`../../single-family-residential/references/heritage-historic-committee.md` (LBMC Ch. 25.45) — point there,
and treat a Register-listed or inventory-rated property as a FLAG for Planning, not a Building-side determination. A building's age alone is not a trigger.

---

## Conflict to watch: dark flat roofs vs. the state cool-roof standard

Laguna Beach is **Title 24 Climate Zone 6** (`../../city-reference/SKILL.md`, Climatic and Geographic Design Criteria). The
state low-slope cool-roof rule reaches **houses**, not only commercial buildings:

- **Single-family house (including a flat-roofed house or a flat roof section):** Energy Code §150.2(b)1Iiia,
  the residential alterations section. When more than 50 percent of the roof is replaced, new low-slope roofing
  in CZ 6 needs an aged solar reflectance of **0.63** and thermal emittance of **0.75**, or **SRI 75**.
- **Multifamily:** §180.2(b)1A, same values. **Nonresidential / hotel-motel:** §141.0(b)2B.

Exceptions to §150.2(b)1Iiia: the Table 150.2-E insulation trade-off; roof area under building-integrated PV or
solar thermal panels; roofs weighing at least 25 lb/ft². Full text and tables:
`cool-roof-energy.md`.

The City's rule for flat roofs (dark brown, dark gray or black; white, light tan and light gray "not acceptable")
points the other way. A local color standard cannot waive Title 24 Part 6. **Both can be met:**

1. **Insulation trade-off (Table 150.2-E, CZ 6–7 column).** With at least **R-10 continuous insulation at the
   roof deck**, there is no reflectance requirement, so a dark membrane complies. Lower reflectance steps:
   0.60 with R-2, 0.55 with R-4, 0.50 with R-6, 0.45 with R-8. This is the usual answer for a dark flat roof on
   a house. Check that the added insulation keeps flashing heights at walls, parapets and rooftop equipment.
2. **A dark product that meets the number.** Some dark-colored "cool" membranes and coatings may reach SRI 75 or
   0.63 aged reflectance; verify the CRRC-rated values. Few dark products reach 0.63, so expect path 1.
3. **Other exceptions:** roof area under BIPV panels, or a roof of at least 25 lb/ft².
4. **Performance (CF1R) compliance** for the alteration is a fourth route.

A reroof replacing 50 percent or less of the roof does not trigger §150.2(b)1I at all.

**Review rule:** do not FAIL a dark flat roof on color, and do not FAIL it on reflectance alone. Ask which
Title 24 path the applicant uses and check the CF2R/plans for it (insulation R-value at the roof deck, or the
product's CRRC aged values). Whether the City would accept a light-colored but not white cool membrane on a house
where the applicant refuses the trade-off is **UNSETTLED; confirm with Planning at pre-application**.

Steep-slope reroofs in CZ 6 have no state cool-roof requirement (§150.2(b)1Ii lists CZ 4 and 8-15 only), so the
ordinary pitched Laguna house reroof carries no such tension.
