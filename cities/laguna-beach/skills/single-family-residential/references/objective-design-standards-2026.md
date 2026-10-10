# Laguna Beach - 2026 Objective Design Standards pathway

**Authority:** *Objective Design Standards - Single-Family and Two-Family Residential*, City
document 26790, published 2026-08-10. Source ledger:
the City source document (not included in this plugin).

Use this reference with `objective-primary-dwelling-ch25-13.md` whenever an applicant asks about
or elects the ministerial Chapter 25.13 path. Chapter 25.13 is the development/eligibility gate;
this reference and exactly one Form Group file are the design-conformance gate. Both must pass.

## Scope gate

- Applies to single-family and two-family developments, including SB 9.
- Excludes 3+ primary units, mixed use, ADUs/JADUs, and non-residential development. Do not attach
  these standards to an ADU merely because it is submitted with a covered primary dwelling.
- A major remodel remains ineligible under LBMC 25.13.030(C).
- A compliant project skips discretionary Design Review but may still require a CDP under Chapter
  25.07. Treat those as independent decisions.
- In a VHFHSZ/fire-code conflict, apply the more restrictive requirement. Areas subject to Zone 0
  are exempt from the Chapter 2 landscaping standards.

## Applicant-selected Form Group

The applicant must select one Form Group and comply with every standard in that group; groups may
not be mixed. The City document states no parcel, neighborhood, zoning, or context rule that limits
the choice. Therefore do not infer a group from architectural appearance or surroundings. If the
application/checklist does not name one, return `unknown` and request the applicant's selection.

Load exactly one matching reference after this file:

| Selection | Style guide | Load |
|---|---|---|
| A | Arts and Crafts, Shingle, and Bungalow | `objective-design-form-group-a-2026.md` |
| B | Southern California Spanish Revival and Mediterranean | `objective-design-form-group-b-2026.md` |
| C | Tudor, English Cottage, French Cottage, Norman, and Storybook | `objective-design-form-group-c-2026.md` |
| D | Ranch, Minimal Traditional, Mid-20th-Century, and Contemporary | `objective-design-form-group-d-2026.md` |

Every covered project must also pass all 13 General Design Standards below. The applicant must
include the completed Chapter 2 checklist and the selected Chapter 3 checklist in the submittal
package and identify the project sheet for each standard.

## Decision contract

- `eligible`: Chapter 25.13 passes, every applicable General and selected-group standard passes,
  the applicant selected the path at filing, and no unresolved design row remains.
- `not_eligible`: any development or design standard fails. Preserve the document's three outcomes:
  revise/resubmit, seek discretionary DRB/Planning Commission review, or withdraw.
- `indeterminate`: a Form Group, checklist, plan locator, or material fact needed for a standard is
  absent. Do not treat missing evidence as a pass.

Always report CDP separately and separately route other structures/site improvements proposed with
the dwelling. Private CC&R/HOA requirements also remain separate.

## General Design Standards

Section anchors: `2.1 Site`, `2.2 Landscaping`, and `2.3 Massing and Privacy`.

### 2.1.1 (PDF p. 22)

Publicly visible gate or door. At least one project entry, either a gate or front door, shall be directly visible from the public right of way.

### 2.1.2 (PDF p. 22)

On-site pedestrian pathway. All project entries, either a gate or front door, shall be served by a continuous pathway at least three feet wide extending from the public right-of-way.

### 2.1.3 (PDF p. 22)

Garage access. Where an alley provides access to a residential lot, the garage shall be accessed from the alley.

### 2.1.4 (PDF p. 23)

Exterior lighting. Exterior lighting shall utilize the following criteria:
• Each exterior lighting fixture shall not emit more than 1,000 lumens and shall be fully shielded, with all light directed downward.
• Notwithstanding the requirements of standard 2.1.4.a, the following light fixtures with visible light sources are allowed.
• A maximum of two light fixtures with visible light sources not exceeding 750 lumens and placed a maximum of seven feet above the adjacent finished surface shall be allowed on the total of all exterior walls that are oriented in the same direction.
• Bistro, festoon, or string lighting where no individual lamp emits more than 50 lumens and the lumen density of the string is no greater than 25 lumens per foot.
• Directional light fixtures used for facade illumination which are shielded and aimed to hit their target.
• Security lighting that exceeds the lumen levels and light source visibility otherwise allowed by this Section shall be by fully shielded fixtures, activated by motion detection, and automatically turn off no more than five minutes after activity is no longer detected.
• No lighting or lighting fixture shall be more than 10 feet above grade.
• No more than two exterior light fixtures with visible light sources are permitted for each wall or building elevation, with a maximum of eight total fixtures allowed on a lot or parcel.

### 2.2.1 (PDF p. 24)

Invasive species. Invasive species identified by the California Invasive Plant Council are prohibited.

### 2.2.2 (PDF p. 24)

Shrub and perennial groundcover. Provide shrub and/or perennial groundcover in required landscape areas, with no more than 35 percent comprising the same species.

### 2.2.3 (PDF p. 24)

Inorganic groundcover. A maximum of 20 percent of all required frontages adjoining public streets and front yard setbacks, excluding driveways, sidewalks, and walkways, may be covered with gravel, cobble, or decomposed granite.

### 2.3.1 (PDF p. 25)

Building wall, maximum length. A straight and continuous building wall shall not exceed 30 feet in length without a horizontal offset in plan view that establishes, top to bottom of the wall, a minimum 18-inch offset for sites with less than 50 feet of street frontage and a minimum three-foot offset for sites with 50 feet or greater street frontage.

### 2.3.2 (PDF p. 25)

Skylights. With the exception of flat glass skylights with automatic night shades that constitute no more than five percent of the total roof area, all skylights, including dome skylights, are prohibited.

### 2.3.3 (PDF p. 25)

Architectural continuity, detached garages and accessory structures.
Detached garages and accessory structures shall be architecturally treated and meet the form group standards of the primary structure by implementing at least two of the following components:
a. Consistent use of roof forms and if sloped, roof materials and colors.
b. Consistent use of facade materials.
c. Consistent use of exterior wall colors.

### 2.3.4 (PDF p. 25)

Solar roofs and panels. All solar roofs and panels shall be matte or non-reflective.

### 2.3.5 (PDF p. 26)

Privacy. Windows and doors that have more than two square feet of glazing are located less than 12 feet from a side lot line and adjacent to a single-family use shall comply with at least one of the following standards:
a. All window sills are located at least five feet above the ground plane as measured directly below the window.
b. Opaque glazing utilizing specialty glass, glass block, or permanently affixed film is used at all openings less than five feet above grade.
c. All windows and doors are positioned such that the vertical plane of the opening when projected horizontally shall be no closer than six feet to any glazed opening in such adjacent building.

### 2.3.6 (PDF p. 26)

Side yard facing patios and terraces. All ground-level patios and terraces utilizing the side yard setback and adjacent to a single-family use shall be a minimum 12 feet in depth as measured from the side yard boundary line along the entire length of the patio or terrace.
