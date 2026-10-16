---
name: guide
description: "Laguna Beach project guide. For any project on any Laguna Beach parcel: does it need Planning, Building or both; which City application to file (Zone Clearance, Administrative Design Review, Design Review Board or Planning Commission, plus Coastal Development Permit, ADU, variance or use permit add-ons); in what order; and whether a drafted or filed packet matches that route. Use first for \"what do I need to file\", \"which Planning application\", \"does this need Design Review\", \"can I file with Building yet\", multi-part projects, and city topics (trees and views, historic, short-term lodging, home business, appeals)."
metadata:
  version: "2.0"
  source: "LBMC Title 25 corpus (codified through 2026-04-28) + Urgency Ord. 1732 (eff. 2026-07-22, extended by Ord. 1733); City Planning applications and review-level matrix (Aug. 2026); October 2026 Major Remodel Quick Guide"
  authority: "LBMC 25.05.040, 25.05.045 (Ord. 1732); LBMC Ch. 25.07 (certified LCP); City of Laguna Beach Planning Division"
  law_as_of: "2026-10-10"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Resident guide (router)

## City Info

| | |
|---|---|
| Permit system | Tyler EnerGov Civic Access |
| Permit portal | https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/home |
| Municipal code | https://ecode360.com/LA4953 |
| Fire agency | Laguna Beach Fire |
| Code edition | Title 14 Building & Housing · 2025 CBC/CRC |
| Code prefix | LBMC |

---

## How to answer (contract)

**Lead with the likely route.** The first lines of every project answer name the single most likely
route: what to file, with whom, and in what order. Build it the way a planner at the counter would:
from the facts given, the ordinance default for that kind of work, and the usual case where a fact
is missing. Then:
- **Alternatives get one line each, two at most**, and only when a fact could actually trigger them: "changes to
  X if Y" (for example "changes to Design Review if the new roof is over 15 ft").
- **Documents only for the first filing.** List what goes in with the application(s) filed first
  (usually the Planning application). A later filing (the building permit after Planning) is one
  numbered step with its link; give its documents when the resident asks. Never list documents for
  a branch you did not lead with.
- **Link every form you name.** Each filing step names the City's application form as a link to
  the City's current copy: the Planning application links are in the applications table of the
  `planning-applications` reference; the online filing links are in the `submit-*` guides. Never
  invent a link; with none in hand, link the City's applications and handouts page
  (https://www.lagunabeachcity.net/government/departments/community-development/planning-zoning/applications-handouts).
- **Short: aim for about 150 words; 250 at most, for any answer.** Bottom line; numbered steps with the forms
  linked; one line offering to list what to submit with the first form (the list comes when the
  resident asks); at most one "this changes if" line; one question. A list, when asked for, is a
  few words per item. No side notes, tables, citation column, overlay catalog or unasked code rules; detail comes when asked. City staff get full detail.
- **UNSETTLED only when it changes what the applicant files.** A fact or open question that routes
  the same either way (which of two parcels, which of two readings that land on the same
  application) gets no branch at all; settle it in a clause or leave it out.
- **Ask for a missing fact only when the route turns on it.** Otherwise answer on the usual case.
- **Too few facts to pick a branch** (for example "add a bedroom, what permits?" with no address or
  size): give the likely route in one or two lines, then at most one "changes to X if Y" line for
  the branch that would most change the filing, then the one question that moves the route most,
  usually the address (it settles zone, coastal, slope and historic at once); otherwise stories or
  height, size against the existing house, or how much exterior wall or roof comes off. Hold the
  document checklists until the branch is known.

The shape to aim for, on a fire station adding solar batteries: "This is administered by the
state; send it to Building as long as you're not doing any roof work." One route, one condition,
no tree of branches.

Method behind the lead lines:
1. Address given: call the parcel lookup, and the record check where the
   chat has it, in the same first round. If the address does not bind to a parcel, say so and
   confirm the parcel before using parcel facts; outside City limits, send the resident to the
   County. Name the facts you used. Existing approvals come first (`planning-approvals` Step 1a):
   never tell a resident to refile a project that already has an approval that has not lapsed. With
   no record lookup in the chat, ask the applicant to bring any existing or pending approvals for the
   address; do not assume one was checked.
2. Any "what do I need" question about a project, listed anywhere or not: pull `planning-approvals`
   and run its method on every piece. Never answer from a remembered example.
3. Work out every piece's approval and who decides (staff, Director, Design Review Board, Planning
   Commission), but write only what changes the filing: a piece that rides the lead application gets
   a clause in that step ("covers the house, garage, decks and walls"); a piece that needs its own
   application or a different body gets its own step.
4. Then the documents: call the City checklists for the first filing's lane, in the same
   round as other lookups, for the form and its link. Offer the filing's document list in one line;
   give it from that result when the resident asks. Never pad the document list from a permit skill.
5. Cite the rule that decides the route (LBMC section, Ord. 1732, state code, or "City practice since
   Ord. 1732") in parentheses; the resident can ask for the rest.
6. The City has not ruled and the answer changes the filing: say UNSETTLED, lead with the reading
   the code text and City practice favor (weighed by the `city-practice` method), give the other as
   one "changes to" line, and say "confirm with Planning at pre-application". Never guess a
   threshold.
7. A deciding fact is unknown (height, slope, coastal status, historic status, deck height): lead
   with the usual case, give the other branch as one "changes to X if Y" line, and ask for the
   fact (one question per answer: the one that moves the route most).
8. Plain, short sentences.

## How many references to pull

Pull `planning-approvals` for every project question. Then pull one reference for each overlay the
facts or pieces trigger (coastal, fire, grading or geology, historic, trees and views, right-of-way,
unpermitted work, unit removal, disaster rebuild, temporary use), plus
`process-timeline-appeals` when there are two or more pieces or the resident asks about steps. A
single small piece may need two files; a multi-part project on a constrained lot may need six or
more. Pull what the pieces need, not everything.
A reference's "What to tell the resident" list covers a question about that topic alone. In a
project answer, an overlay that changes the filing gets a clause in the step it changes or one
"changes to X if Y" line; the rest of that list waits until the resident asks.

## Router — by kind of question

Pull with the reference file `references/<name>.md`. These are the guide's topics, all of them:
`planning-approvals`, `city-practice`, `design-review-lists`, `review-bodies`,
`coastal-development-permits`, `process-timeline-appeals`, `discretionary-permits`,
`building-permit-exemptions`, `grading-drainage`, `fire-hazard-and-wui`, `historic-properties`,
`trees-views-hedges`, `noise-lighting-equipment`, `short-term-lodging`, `home-business`,
`right-of-way-utilities`, `unpermitted-work`, `unit-removal`, `disaster-rebuild`, `temporary-uses`,
`before-you-file` (a drafted or filed packet: right application? Planning before Building?),
`common-corrections` (a drafted plan set: what Laguna's plan check most often corrects, by permit
type, and how to check the City's numeric standards on the drawings).
They are reference topics, not permit skills: never pass them to the permit skills. City website pages
(`planning-applications`, `forms-index`, `fees`, `submit-right-of-way`, `code-enforcement`) are also
reference topics.

| Kind of question | Pull | Also |
|---|---|---|
| What approvals does my project need? (any project, any mix, including ones no file names) | `planning-approvals` | the parcel lookup; one permit skill per piece |
| What exactly does a list item say? Is X on a list? Does Ord. 1732 apply in the coastal zone? | `design-review-lists` | |
| A close call the lists do not settle; how far to rely on how the City has routed similar work | `city-practice` (the method for weighing practice) | after `planning-approvals` |
| Who decides? DRB or Planning Commission? Heritage Committee? Coastal Commission? | `review-bodies` | |
| Do I need a CDP? Coastal zone, appealable area, exclusion area, highly scenic? Three Arch Bay or Irvine Cove filing, beach event, emergency CDP, changing a CDP | `coastal-development-permits` | `../coastal-development/SKILL.md` for plan detail |
| How do I apply? How long? Several applications at once? Staking, notice, hearing, appeals, approval life | `process-timeline-appeals` | the fee estimate for any dollar amount |
| Do I need a permit at all? | `building-permit-exemptions` | |
| Moving dirt, steep lot, soils report, landslide or liquefaction zone, drainage, water quality (WQESA) | `grading-drainage` | |
| Fire zone, fuel modification, wildfire materials, accessory structures in the fire zone | `fire-hazard-and-wui` | |
| Historic house, ratings, Heritage Committee, Mills Act | `historic-properties` | |
| Trees, views, hedges, landscaping height | `trees-views-hedges` | |
| Equipment noise, outdoor lighting, construction hours | `noise-lighting-equipment` | |
| What will plan check correct on my plans? Checking height, setbacks, coverage, the 50% major remodel test, equipment or WUI on the drawings | `common-corrections` (a plan-check preview, never an intake defect) | `before-you-file` first for the intake side |
| Variance, CUP, AUP, TUP, changing an approved plan, lot line, SB 9, right-of-way encroachment | `discretionary-permits` | SB 9 state law: `../single-family-residential/SKILL.md` |
| Work in the street, sidewalk or parkway; utility boxes, poles, undergrounding; cell antennas in the right-of-way; Coast Highway or Laguna Canyon Road (Caltrans); address outside City limits (Emerald Bay) | `right-of-way-utilities` | `discretionary-permits` for the encroachment permit |
| Unpermitted work: legalizing it, code enforcement case, stop-work order, as-built plans | `unpermitted-work` | `planning-approvals` for the pieces |
| Removing or merging a dwelling unit: duplex to house, demolishing units, apartment to office | `unit-removal` | a CrossBeam reference that is not included in this plugin for discretionary approvals |
| Rebuilding after a fire, landslide or other disaster | `disaster-rebuild` | `fire-hazard-and-wui` |
| Temporary uses: events, live music or other occasional activity at a business, containers, construction trailers, temporary structures, street closures | `temporary-uses` | |
| Housing on a church, school or other faith-based or nonprofit college site; SB 4 (Gov. Code 65913.16) | `../multi-unit-residential/SKILL.md` (state-preemption, SB 4) | `planning-approvals`; `coastal-development-permits` |
| Solar or batteries on any building | `planning-approvals` Step 4a-bis (Building only, Gov. Code 65850.5) | `../solar/SKILL.md` |
| Short-term rental | `short-term-lodging` | |
| Home business | `home-business` | |
| Anything else, or a project or situation no row fits | `planning-approvals` (run the method) | say what is UNSETTLED |

## Permit skills (for plan and submittal detail, after the Planning answer)

Permit skill folders (`../<kind>/SKILL.md`): `adu`, `residential-remodel`, `residential-addition`, `single-family-residential`,
`multi-unit-residential`, `kitchen-bath-remodel`, `window-replacement`, `reroof`, `siding-replacement`,
`solar`, `ev-charger`, `hvac`, `deck-patio-repair`, `patio-cover`, `swimming-pool`, `pool-demolition`,
`fence`, `block-wall`, `retaining-wall`, `sign`, `commercial-ti`, `restaurant-ti`, `ltia-demolition`,
`coastal-development`. A piece with no permit skill (for example a detached accessory building) is
answered from the guide alone; never force-fit a permit type.

## Facts that change the answer (details in `planning-approvals` Step 1)

- **Coastal zone, appealable area, Commission area:** CDP unless exempt; major remodel method;
  Ord. 1732 certification question (UNSETTLED).
- **ESA (25.08.010, Ord. 1732): habitat, streams, slopes of 30% or more:** lower-list pieces go to
  Design Review (B)(1)(e) absent a peer-reviewed no-impact finding. Slope from the parcel lookup is
  a screen; a survey decides.
- **Height over 15 ft** (25.08 "Height, building"): Design Review (B)(1)(c) for new roof, floor area
  or story over 15 ft; a specific item (equipment, deck, railing, reroof) governs its own subject.
- **Design Review of new construction or a major remodel, any zone:** Fire Safety Standards Review
  before the hearing (25.05.040(C)(4)). Only the fuel modification program or AM&M request is
  tied to the fire zone: VHFHSZ or FM parcel when Fire finds it necessary; on FM land a final fuel
  modification plan before the building permit (14.70.070).
- **Solar and paired storage on any building:** Building only, no Planning list (Gov. Code
  65850.5(b); `planning-approvals` Step 4a-bis). On an existing building it is a CDP-exempt
  improvement unless a listed exception applies (25.07.008(A)(1)-(2)); cost never makes it a CDP
  (`coastal-development-permits`).
- **Historic resource:** Heritage Committee, then ADR for the minor alterations ADR item (iv) lists,
  or Design Review for major work; in-kind replacement of doors, windows, roofing or siding is still
  ADR (iv). In-kind replacement of things (iv) does not list (equipment, repair that alters nothing)
  is Zone Clearance with a historic staff check (`historic-properties` section 2).
- **CGS landslide or liquefaction zone, WQESA:** geotechnical review; Public Works water quality.
  Neither changes the Planning list.
- **Zone and use:** house or duplex goes to the DRB; 3+ units, Downtown or commercial to the
  Planning Commission.

## What this guide does not do

- It does not restate California law (ADU, SB 9, building code, WUI); it points to the state skill.
- It does not quote fees; call the fee estimate.
- It does not predict a Director referral to a hearing.

---

## Tools in this plugin

The plugin root is `../..` from this file. These are what the rest of this skill means by:

- **the parcel lookup**: run `python3 <plugin-root>/scripts/parcel-facts/parcel_facts.py --address "<street address>"`. It reads the City's public map layers and prints the zone, specific plan, coastal and appealable areas, historic rating, habitat, oceanfront, fuel modification and other overlays. If the host cannot run it, or a layer fails, ask the applicant for those facts (a survey and the title report hold most of them), and say which facts are unconfirmed.
- **the record check**: ask the applicant for any existing or pending approvals for the address (Planning case numbers, resolutions, Planning-stamped plans). The City's online permit portal (https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/home) lists records for an address. Never assume a record check was done.
- **the municipal code**: the Laguna Beach Municipal Code at https://ecode360.com/LA4953.
- **the City checklists**: `<plugin-root>/requirements/` (index: `requirements/README.md`). Planning applications are in `requirements/planning/` (`application-index.md` names each one and its trigger), Building in `requirements/building/`, required plan sheets in `requirements/plan-sheets/`.
- **the fee estimate**: `node <plugin-root>/scripts/estimate-fees.mjs` (`requirements/fees/README.md`).
- **reference topics**: a bare topic name such as `planning-approvals` is a file in this skill's `references/` folder; City website topics (`planning-applications`, `forms-index`, `fees`, `submit-*`, `code-enforcement`) are in `../city-website/references/`.
- **permit skills**: the sibling folders of this skill (`../adu/`, `../swimming-pool/`, and the rest).
- To check a drafted plan set, use the `plan-set-check` skill; to fill and file the City forms, the `laguna-permit-preparer` skill.

---

## References

Load these on demand. Paths are relative to this file.

**Laguna Beach rules**

- `references/before-you-file.md` — Laguna Beach — Before you file: does the packet match the route?
- `references/building-permit-exemptions.md` — Laguna Beach — Work that needs no building permit, and work that still needs Planning
- `references/city-practice.md` — Laguna Beach — Weighing City practice against the code (method)
- `references/coastal-development-permits.md` — Laguna Beach — Coastal Development Permits (resident guide)
- `references/common-corrections.md` — Laguna Beach — Common plan-check corrections: check the drawings before the City does
- `references/design-review-lists.md` — Laguna Beach — the three Design Review lists (Ord. 1732)
- `references/disaster-rebuild.md` — Laguna Beach — Rebuilding after a fire, landslide or other disaster (resident guide)
- `references/discretionary-permits.md` — Laguna Beach — Variances, use permits, and other Planning permits
- `references/fire-hazard-and-wui.md` — Laguna Beach — Fire hazard zone, fuel modification and wildfire building rules (resident guide)
- `references/grading-drainage.md` — Laguna Beach — Grading, drainage, hillsides and soils reports (resident guide)
- `references/historic-properties.md` — Laguna Beach — Historic properties (resident guide)
- `references/home-business.md` — Laguna Beach — Running a business from home (resident guide)
- `references/noise-lighting-equipment.md` — Laguna Beach — Construction hours, equipment noise and outdoor lighting (resident guide)
- `references/planning-approvals.md` — Laguna Beach — Does my project need Planning approval, and which? (the method)
- `references/process-timeline-appeals.md` — Laguna Beach — Planning process, timelines, and appeals
- `references/review-bodies.md` — Laguna Beach — Who decides (review bodies)
- `references/right-of-way-utilities.md` — Laguna Beach — Work in the street, utilities, wireless, Caltrans and sites outside City limits (resident guide)
- `references/short-term-lodging.md` — Laguna Beach — Short-term lodging (resident guide)
- `references/temporary-uses.md` — Laguna Beach — Temporary uses, events, containers and temporary structures (resident guide)
- `references/trees-views-hedges.md` — Laguna Beach — Trees, views and hedges (resident guide)
- `references/unit-removal.md` — Laguna Beach — Removing or converting a dwelling unit (resident guide)
- `references/unpermitted-work.md` — Laguna Beach — Legalizing unpermitted work, code cases and stop-work orders (resident guide)

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
