# Laguna Beach — Removing or converting a dwelling unit (resident guide)

**Law as of:** 2026-10-10
**Authority:** Gov. Code 66300.5-66300.6 (Housing Crisis Act); Gov. Code
65590 (housing in the coastal zone); LBMC
25.07.006, 25.07.008(A)(2); LBMC 25.12.004, 25.14.004; CEQA (a CrossBeam reference that is not included in this plugin).
**Use for:** "Can I turn my duplex back into a single-family house?", "Can I demolish the second
unit?", "Can I tear down my apartment building and build one house?", "Can I convert an apartment
to an office?", merging two units, removing a second kitchen.

State law sets this floor; this file only says how it lands in Laguna. For the full state rules use
`../../multi-unit-residential/SKILL.md` and the state streamlining skill's SB 330 section.

## Step 1 — Facts that decide the answer

Ask for or find (permit history, the parcel lookup, the owner):
- How many legal units are on the site now, and the most there were in the last five years.
- Whether any unit is or was in the last five years rent-restricted, under rent control, rented to a
  lower-income household, or withdrawn from rent under the Ellis Act within the last ten years
  ("protected units", Gov. Code 66300.5(h)).
- Whether any unit is occupied by a low- or moderate-income household (coastal zone, 65590).
- Whether the lot is in the coastal zone.
- Whether the work is physical demolition, a merger of two units into one, or a change to a
  non-residential use.

A unit that was never permitted is a separate question (`unpermitted-work`).

## Step 2 — Housing Crisis Act (Gov. Code 66300.6)

- **No net loss of units.** An affected city "shall not approve a housing development project that
  will require the demolition of one or more residential dwelling units unless the project will
  create at least as many residential dwelling units as will be demolished" (66300.6(a)). A
  "housing development project" includes a project of residential units only (66300.5(e) via
  65905.5(b)(3) and 65589.5(h)(2)); on the words, one new house qualifies. So tearing down a duplex
  to build one house is barred by that rule unless the unit count is kept.
- **Protected units.** If the project demolishes protected units, or protected units were demolished
  on the site in the last five years, the project must replace them, include at least as many units
  as the most on the site in the last five years, give occupants six months' notice, and give
  lower-income occupants relocation benefits and a right of first refusal (66300.6(b)). For one
  house replacing one protected unit, "replace" means a unit of any size or income level
  (66300.5(i)(2)).
- **Affected city.** These rules bind cities HCD lists as "affected" (66300.5(a); 66300(d), list
  valid until January 1, 2030). Our sources do not hold HCD's list. Say: "These limits apply if
  Laguna Beach is on HCD's affected-city list; confirm with Planning."
- **Merging or converting without demolition** (removing a second kitchen, joining two units): the
  statute speaks of "demolition". Whether a merger counts is UNSETTLED; give both readings and
  confirm with Planning at pre-application.
- **Does an ADU or JADU count toward the unit total?** Not settled in our sources. UNSETTLED.
- A local rule that is more protective controls (66300.6(c)). We found no Laguna demolition or
  unit-replacement ordinance in the Title 25 corpus.

## Step 3 — Coastal zone housing (Gov. Code 65590)

- In the coastal zone, converting or demolishing units occupied by low- or moderate-income
  households needs replacement units (in the City, in or within three miles of the coastal zone,
  within three years) (65590(b)).
- **Small-building exemption:** the replacement rule does not apply to a residential structure with
  **fewer than three units**, or, where more than one structure is involved, to 10 or fewer units,
  unless the City finds replacement feasible (65590(b)(1)). A duplex usually falls here.
- **Conversion to a non-residential use** that is not coastal-dependent (for example apartment to
  office) "shall not be authorized unless the local government has first determined that a
  residential use is no longer feasible in that location" (65590(c)). This finding applies even to a
  small building.
- Laguna's LCP was certified after 1982, so the 65590(f) safe harbor for older LCPs does not apply.

## Step 4 — Coastal Development Permit

- A change in the density or intensity of use of land is "development" (25.07.006 "Development").
  Removing a unit changes density.
- A duplex or apartment building is not a single-family dwelling, so the (A)(1) exemption does not
  fit. The (A)(2) exemption for other structures does not cover "improvements to any structure which
  would result in a change in the intensity of use" (25.07.008(A)(2)(b)). Read with the definition,
  expect a CDP. The LBMC defines only "intensification" (more parking); whether a reduction is a
  "change in intensity" under (A)(2)(b) is UNSETTLED. Give both and confirm with Planning.
- The CDP is decided with any Design Review (25.07.012(D)); appealable in the appealable area.
  Details: `coastal-development-permits`.

## Step 5 — Zoning, Planning list and CEQA

- **Zoning:** a single-family house is a permitted use in R-2 and R-3 (25.12.004, 25.14.004).
  Check the zone of other lots with the parcel lookup.
- **Planning list:** run `planning-approvals` on the physical work. Interior-only work (removing a
  kitchen, opening a wall) is Zone Clearance (25.05.040(B)(2)(d)); demolition of a building or a
  major remodel follows the lists like any other project.
- **CEQA:** a discretionary approval (a CDP decided at a hearing, Design Review) is subject to CEQA.
  The City decides the exemption. Use a CrossBeam reference that is not included in this plugin for the state rules.
- **Building:** a demolition permit, or a building permit for the merger work; Fire if sprinklers or
  separations change.

## What to tell the resident

1. The unit count and occupancy facts decide the answer; ask for them.
2. Demolition that leaves fewer units: the Housing Crisis Act bars approval unless the units are
   replaced, if Laguna is an affected city (confirm). A merger without demolition is UNSETTLED.
3. Coastal zone: 65590 replacement rarely applies to a duplex, but a change to a non-residential use
   needs a "residential no longer feasible" finding.
4. Expect a CDP in the coastal zone (density change); UNSETTLED for a pure reduction.
5. Then the normal Planning list for the physical work.
