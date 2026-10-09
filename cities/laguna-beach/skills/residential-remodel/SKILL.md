---
name: residential-remodel
description: "Residential Remodel permits in Laguna Beach, CA. A whole-house or multi-room remodel, including bearing-wall work and new openings. Always a plan set. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against the Laguna Beach rules and the City submittal checklists, and prepares a portal-ready submission; (B) CITY REVIEWER — checks a submittal against the Laguna Beach rules and produces tight corrections output. California code compliance comes from the CrossBeam connector when it is connected. Use when the user mentions residential remodel in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Existing Building Code (Title 24 Part 10), 2025 California Residential Code (Title 24 Part 2.5), 2025 California Energy Code (Title 24 Part 6), 14 CCR Division 5.5 Coastal Commission Regulations, plus California Coastal Commission settled enforcement interpretation; LBMC Title 15 (Fire Prevention, Ord. 1726 12/18/2025), LBMC Title 25 (Zoning) Chapters 25.05 / 25.07 / 25.10 / 25.50 / 25.56 / 25.17, LBMC Title 14 Chapter 14.50 / 14.52 / 14.70 / 14.86, City of Laguna Beach Land Use Element (LCP), Major Remodel Quick Guide (Updated June 2026; standalone handout 23171 and SB 9 application Exhibit F), Building Plan Check Submittal Requirements (May 2026 republish, mod date 2026-04-30), Bluff Edge Determinations Quick Guide (Mar 2024), Zoning Plan-Check Project Submittal Requirements table, CCC F9a-11-2024 Notice (ADU coastal exemption rejection), LBMC Title 12 (Trees and Vegetation) Chapters 12.08 / 12.16 as amended by the 2026 efficiency ordinance (effective 2026-08-20)"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-08-15"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Residential Remodel Permit

Handles residential remodel permits in Laguna Beach end-to-end. Scope: A whole-house or multi-room remodel, including bearing-wall work and new openings. Always a plan set.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a residential remodel permit, or (B) a city reviewer checking a submitted one?"

- Mode A → walk **MODE A — Builder / Homeowner Intake** below
- Mode B → walk **MODE B — City Reviewer** below

Both modes share the same rules. This skill carries the Laguna Beach layer: the City rules, the City submittal checklists and the filing steps. California code compliance comes from the CrossBeam connector (see **California Code Compliance** below).

---

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

## Citywide Overlays

These apply to every permit in Laguna Beach before the rules below.

- **Wildfire — the whole city.** Treat every Laguna Beach parcel as inside a Fire Hazard Severity Zone / WUI area. Say so plainly: "assumed FHSZ based on citywide coverage; confirm the parcel on the City's adopted 2025 LRA map." Never tell an applicant a parcel is outside the zone without that map.
  Exterior work follows the California WUI Code (Title 24 Part 7; CBC Ch. 7A / CRC R337) as amended by LBMC Ch. 14.70, whose scope is set by LBMC §14.70.015. Class A roofing applies to any building in the City (LBMC §14.50.120, amending CBC §1505.1). Details: `../wildfire-wui/SKILL.md`.
- **Coastal zone — most of the city.** Check the parcel against the City's coastal zone map before naming a Planning route. Report a parcel that straddles the boundary as straddling. Coastal Development Permit analysis: `../coastal-development/SKILL.md`.

---

## MODE A — Builder / Homeowner Intake

### A1. Intake

Start by reading `../../references/homeowner-journey.md`; its opening exchange applies when this skill is selected directly. Read any files and answers the user already gave. For an idea-stage request with no files, briefly explain the help available and ask at most three opening questions: the address, the scope, and whether drawings exist.

Then establish, from evidence, the facts the **Laguna Beach Rules** below turn on: the Planning route, the coastal zone, overlays, and any triggers they name. Unknown answers stay unknown. Do not assume a route, an exemption, or compliance. Use the Laguna Beach rules and the City submittal checklists below as the coverage floor for what to ask, without interrogating. When preparing files or navigating intake, read `../../SKILL.md` for the canonical artifact and transaction workflow.

### A2. Pre-submission Compliance Check

Once you have enough information, walk the Laguna Beach rules and the City submittal checklists using the user's answers. When a plan set exists, run the plan-set check (`../plan-set-check/SKILL.md`). For California code compliance, follow **California Code Compliance** below. For every item:
- **FAIL** → tell the user the specific change needed before they submit
- **FLAG** → tell them what information or documentation they still need
- **PASS** → confirm and move on
- **NOT CHECKED** → a California code item with no CrossBeam result: say so, and recommend a CrossBeam check before filing

### A3. Submission Guide

When compliance is clean (or flag-only), produce a submission guide. Do not promise over-the-counter issuance unless the Laguna Beach rules below say the scope qualifies.

```
## Ready to Submit — Laguna Beach Residential Remodel Permit

**Planning route:** [from the Laguna Beach rules, or "none required"]
**Parallel applications:** [Coastal Development Permit, Design Review, or none]
**California code compliance:** [CrossBeam result, or "not checked: run a CrossBeam check before filing"]

### Required uploads
[Generated per skill — plans, product data sheets, calculations, waste management plan if applicable, Laguna Beach Fire clearance if overlay-triggered, etc.]

### Inspection sequence
[Generated per skill — standard inspection milestones]
```

### A4. Filing

Hand the confirmed facts and filing theory to this plugin's included `laguna-permit-preparer` skill. It fills only verified official forms, uses a visible browser when portal filing is supported, and stops at `portal_ready` with an exact handoff when browser control is unavailable. It never submits without a fresh final approval and a confirmation receipt.

---

## MODE B — City Reviewer

### Procedure

1. Accept the submitted material (form data, PDF, photos, or pasted text)
2. Extract the key facts: project type, scope, materials, dimensions, parcel address, contractor
3. Walk the Laguna Beach rules and the City submittal checklists, in order. Get California code compliance as **California Code Compliance** below says
4. Produce output in the format below — hard fails first, then flags, then local flags, then a compliant bundle, then inspection deferrals

### Output format

```
PLAN CHECK — {address} ({permit})

❌ CORRECTIONS REQUIRED (N)
   [plan-check severity=fail items that are not satisfied]

⚠️ VERIFY BEFORE ISSUANCE (N)
   [plan-check severity=flag items needing documentation or clarification]

ℹ️ LOCAL FLAGS (N) — city discretion
   [LBMC-specific items — parcel overlays, city-specific checks]

✓ {N} checks PASS (expand for detail)

➡ {N} checks deferred to inspection

⛔ NOT CHECKED — California code compliance [unless a CrossBeam result covers it]

—
Generated by CrossBeam Permits · crossbeam-permits.com
```

Summary verdict at the end: **APPROVE** | **CORRECTIONS REQUIRED** | **NEED ADDITIONAL INFO**

Without a CrossBeam result, the verdict covers the Laguna Beach rules and the City checklists only. Say so beside it, and never call the set compliant with the California codes.

Do not list inspection items as corrections. Do not enumerate every passing item unless the user asks. Respect the plan checker's time.

---

## Laguna Beach Rules

> Laguna Beach's local layer for this permit. It adds to or overrides California law, which comes from the CrossBeam connector. Paths are relative to this file.

This skill is the **city overlay** the parent state skill is told to invoke at every Laguna-Beach review. Its job is to (a) classify the project under Laguna's current closed-list planning routes, (b) determine major-remodel status using Laguna's dual coastal zone appealable / coastal zone non-appealable methodology, (c) run Laguna's deterministic 6th phantom-remodel signal on top of the parent's heuristic 5-signal detector, (d) layer in the city's two sprinkler retrofit triggers (Ch. 14.52.030 valuation and Title 15 §1103.5.4 scope), (e) layer in the bluff/CDP/VHFHSZ/view/tree/hillside overlays, and (f) flag the CCC F9a-11-2024 ADU-coastal-exemption pushback when relevant.

**What this covers (12 city-specific topics)**
1. Major-remodel operative authority chain — LCP Land Use Element → June 2026 Major Remodel Handout → LBMC §25.10.008(O) statutory backstop
2. Dual methodology — coastal zone appealable (foundation + walls + roof, removal AND reinforcement count) vs coastal zone non-appealable (exterior walls only, removal only); walls counted on each floor; each structure tested independently
3. Deterministic phantom-remodel rule from the May 2026 Building Plan Check Submittal Requirements — Laguna's codified 6th signal
4. Sprinkler retrofit — two independent triggers: Ch. 14.52.030 (valuation) and Title 15 §1103.5.4 (scope). Either fires.
5. Bluff overlay — §25.50.004(B)(4) 25-ft setback + §25.50.020 site-coverage shrinkage + anti-game buried-bluff rule + report stack
6. Nonconforming structures — Ch. 25.56 three-rule structure, plus the June 2026 handout rule: nonconforming status ends at a major remodel
7. Current project routing — §25.05.040 closed lists + §25.05.045 Zone Clearance, with ESA override
8. CDP for major remodel in coastal zone — Ch. 25.07 fires regardless of E-93-1 categorical exclusion
9. ADU coastal exemption pushback — CCC F9a-11-2024 (flag prominently)
10. Coastal Zone / Appealable Area / Bluff Overlay polygon integration pattern — point-in-polygon vs applicant fallback
11. VHFHSZ + WUI amendments — Ch. 14.70 affecting major remodels
12. View, Heritage Tree, Hillside overlays — when each triggers

**What this does NOT cover** (deferred to state skill or other city skills)
- CEBC trip-wire framework, scope classification, alteration levels, additions framework, energy code, Title 24 §150.2 — see the California Residential Remodel rules, which come from the CrossBeam connector (see "California Code Compliance" below)
- CDP procedure mechanics — invoked via `../coastal-development/references/california-baseline.md`
- ADU substantive rules — see the California ADU (Accessory Dwelling Unit) rules, which come from the CrossBeam connector (see "California Code Compliance" in `../adu/SKILL.md`) and `../adu/SKILL.md`
- Window/door, siding, reroof component checks — see the `window-replacement`, `siding-replacement`, `reroof` skills in this plugin
- Kitchen/bath component-level requirements — see the California Kitchen/Bath Remodel rules, which come from the CrossBeam connector (see "California Code Compliance" in `../kitchen-bath-remodel/SKILL.md`) and `../kitchen-bath-remodel/SKILL.md`

---

### How to Use This Skill

The parent (the California Residential Remodel rules, which come from the CrossBeam connector (see "California Code Compliance" below)) walks the project through state classification, the three trip-wires, and the heuristic 5-signal phantom detector. Then it invokes this skill. Walk the steps below in order:

1. **STEP A** — Run the **current project-route classifier** first. Route = Zone Clearance / Administrative Design Review / Design Review / `needs_source`, after the ESA override. The route drives notice timing, hearing requirements, and the approval authority.
2. **STEP B** — Run the **major-remodel determination** using the coastal zone appealable vs coastal zone non-appealable methodology, once for each structure (operative-but-interpretive — see hedge in §1 below).
3. **STEP C** — Run the **deterministic phantom-remodel signal** on top of the parent's 5-signal detector. This is Laguna's codified 6th signal. If it fires on coastal property, cite 11 Lagunita LLC v. CCC (2020) in the corrections-letter body.
4. **STEP D** — Apply **both sprinkler retrofit tests**: Ch. 14.52.030 (valuation) and Title 15 §1103.5.4 (scope). Either one firing requires the retrofit. Run both; never stop after one.
5. **STEP E** — If oceanfront / on the bluff, apply the **bluff overlay** (25-ft setback, anti-game fill rule, report stack).
6. **STEP F** — Apply **Ch. 25.56 nonconforming** rules where existing structure is nonconforming. Three rules; SFR vs multi-family distinctions matter. If Step B is YES, apply F.0 first: nonconforming status ends.
7. **STEP G** — If coastal zone, **CDP required** for any major remodel regardless of the E-93-1 categorical exclusion. If scope includes an ADU, flag the CCC F9a-11-2024 pushback.
8. **STEP H** — Apply **VHFHSZ + WUI** overlays from Ch. 14.70.
9. **STEP I** — Apply **View / Heritage Tree / Hillside** overlays where applicable.
10. **STEP J** — Assemble output. For every overlay test, return PASS / FAIL / FLAG / N/A with the verbatim city citation that drove the decision.

See this file for the reference file catalog.

---

### STEP A — Design Review Tier Classifier (run FIRST)

Cite current §25.05.040 as replaced by Urgency Ordinance No. 1732. The former rule that broadly subjected exterior work to Design Review, and the pre-ordinance Zoning Plan-Check project-tier table, do not control the current route.

Classify against the three closed lists:

| Route | Current list | Common remodel matches |
|---|---|---|
| **Design Review** before DRB/Planning Commission | §25.05.040(B)(1), 16 categories | Major remodel `(a)`; new building `(b)` unless an enacted ADU/Chapter 25.13 exception applies; improvement over 15 ft `(c)`; ESA development `(e)`; grading over 20 CY `(f)`; retaining wall over 5 ft `(g)`; pool/spa over 3 ft `(j)` |
| **Zone Clearance**; exempt from Design Review | §25.05.040(B)(2), 28 categories | Non-major demolition/alteration/addition `(a)`; improvement no more than 15 ft `(b)`; in-kind repair `(c)`; interior-only work `(d)`; qualifying reroof `(e)`; ADU `(h)`; grading no more than 20 CY `(i)`; retaining wall no more than 5 ft `(j)`; low deck/patio `(m)`; compliant primary dwelling under Chapter 25.13 `(z)` |
| **Administrative Design Review** | §25.05.040(B)(3), 17 categories | Elevated deck/patio `(iii)`; qualifying minor historic work `(iv)`; equipment failing §7.25.130(C) `(v)`; glare/light-colored reroof `(ix)`; roof geometry change `(x)`; detached fireplace `(xi)`; unshaded skylight `(xii)` |

The ESA override can promote a Zone Clearance or ADR item to Design Review unless a licensed professional determines, subject to peer review, that it does not impact the ESA. The Director also retains the enacted referral authority, and a CDP may be independently required.

Except for elevated decks/patios and qualifying minor historic work, an ADR hearing may be waived only if no other entitlement is required and the 15-working-day mailed/published notice-and-comment procedure produces no timely hearing request. If a public hearing occurs, §25.05.065(D) sets the mailed-notice minimum and the same values independently govern applicable staking deadlines; the day counts are in `../city-reference/SKILL.md` §"Design Review / Zone Clearance".

Output the route, exact matched category, ESA analysis, referral possibility, CDP status, and hearing/waiver status. If no closed-list category can be matched, return `needs_source`. If Step B determines the work is a major remodel, use Design Review under §25.05.040(B)(1)(a).

Full content: `references/city-design-review-tiers.md`.

---

### STEP B — Major Remodel Determination (Dual Methodology)

**Source edition.** Apply the City's Major Remodel Interpretation Quick Guide, "Updated June 2026" [source: https://www.lagunabeachcity.net/home/showpublisheddocument/23171/639179723814800000, as of 2026-09-29]. The SB 9 application prints the same June 2026 text as Exhibit F [source: https://www.lagunabeachcity.net/home/showpublisheddocument/26958/639232726993730000, as of 2026-09-29]. The June 2026 edition replaces the August 2025 edition. Do not apply the August 2025 text.

> **OPERATIVE BUT INTERPRETIVE — read the handout's own hedge before applying.** The June 2026 Major Remodel Quick Guide (verbatim): *"Provided below are the calculation methods that City staff believes the CCC staff uses for their assessment of projects in determining whether a project is a major remodel. ... the language below is City staff's best attempt in interpreting CCC staff's analysis based on their previous appeal reports. As such, these calculation methods have not been approved by the CCC staff; and therefore, the City cannot guarantee that the CCC staff will apply the identical interpretation."* The handout further states: *"While a Municipal Code amendment is in process to achieve a long-term resolution, City staff now interprets 'major remodel' in a manner similar to that of the CCC staff for properties located in the appealable area of the coastal zone."* This skill applies the dual methodology as **operative city-staff interpretation**, not as statutory rule. A Municipal Code amendment is in process — re-check this skill when the amendment lands.

The handout's first paragraph states the consequence, verbatim: *"Whenever modifications to an existing building or structure constitute a major remodel, the building or structure shall be classified as new development subject to current zoning regulations and all requirements applicable to the construction of a new building or structure, including undergrounding requirements, required dedication of on- and off-site improvements, and payment of new development fees."*

#### B.0 Tool-Backed Calculation Path

Use the deterministic calculator before writing the narrative finding:

1. List each building or structure on the site (primary dwelling, detached garage, each detached accessory building or structure). Run Step B for each one independently (see B.4).
2. For each structure, extract or confirm Step B measurements from the demolition/existing-conditions sheets: exterior wall LF **on each floor**, load-bearing interior wall LF **on each floor**, foundation LF, roof SF, and cumulative addition square footage against that structure's January 13, 1993/reset baseline.
3. When sheet PNGs are available, run the vision extractor in a CrossBeam reference that is not included in this plugin; it uses `gemini-3-flash-preview`, returns counted segment geometry for an audit overlay, and calls the calculator.
4. When measurements are already provided by the applicant/reviewer, call `computeMajorRemodel(input)` from a CrossBeam reference that is not included in this plugin directly with the Laguna config for the area (`coastal-appealable` for the coastal zone appealable area, `non-coastal-appealable` for the coastal zone non-appealable area). Call it once for each structure.
5. The calculator takes one wall total per call. It does not split walls by floor. Its wall percentage is the whole-structure total. Compute the percentage on each floor yourself (B.2, B.3), then apply the three-way floor rule in B.2a.
6. Use the calculator result and intermediate values first, then write the review narrative with the authority chain below: LCP Land Use Element → June 2026 Major Remodel Handout (including the hedge) → LBMC §25.10.008(O).
7. If the calculator returns `NEEDS_MEASUREMENT`, or the plans do not give wall LF for each floor, do not pass the Step B check. Request the missing denominator or numerator needed for the applicable methodology.

#### B.1 Authority Chain (cite in this order)

1. **LCP Land Use Element** — statutory base. The LCP defines "major remodel" as *"alteration of or an addition to an existing building or structure that increases the square footage of the existing building or structure by 50% or more; or demolition, removal, replacement, and/or reconstruction of 50% or more of the existing structure."*
2. **June 2026 Major Remodel Handout** — operational application; what City staff applies in plan review (verbatim quote above).
3. **LBMC §25.10.008(O)** — single-sentence statutory backstop: *"A major remodel is a structural renovation and/or addition, which equals or exceeds fifty percent of the original gross floor area of the structure on the lot."* (Ord. 1475, 2007.) This is the **only** Municipal Code definition of major remodel in the codified LBMC. It is silent on dual methodology, on the cumulative baseline, and on the ADU carveout — those live in the LCP and the handout.

#### B.2 Coastal Zone Appealable Areas Methodology

Verbatim from the June 2026 Major Remodel Handout, "COASTAL ZONE APPEALABLE AREAS" section:

| Component | Formula | What Counts |
|-----------|---------|-------------|
| **Foundation** | (LF removed/reinforced) ÷ (LF existing) × 100 | *"For caissons, use the diameter to calculate linear feet and include any associated grade beams, taking care not to count the same linear footage twice where caissons and grade beams overlap."* |
| **Interior + Exterior Walls (each floor)** | *"(linear feet of walls to be removed/reinforced on each floor) ÷ (linear feet of existing walls on each floor) x 100"* | All exterior walls (load-bearing AND non-load-bearing). Interior walls — load-bearing only. **Both removal AND reinforcement count as demolition.** Drywall/stucco removal does NOT count. Window/door change-outs in same openings do NOT count. Filling in window/door openings does NOT count unless additional structural support is proposed. Compute one percentage for each floor. Combine the floors only by the three-way rule in B.2a. |
| **Roof** | (SF removed/reinforced including eaves) ÷ (SF existing) × 100 | Both removal AND reinforcement count as demolition. |

A structure IS a major remodel if **any** of:
1. Demolition or reinforcement of 50%+ of the **exterior walls** (apply B.2a) OR 50%+ of the **combined roof/walls/foundation** of the structure.

#### B.2a How Floors Combine — Three-Way Rule

The June 2026 handout computes walls "on each floor". It does not state how the floor results combine. For each structure, compute the **floor percentages** (one for each floor) and the **whole-structure total**: (wall LF removed or reinforced on all floors of that structure) ÷ (existing wall LF on all floors of that structure) × 100. Then:

1. Every floor percentage is under 50% → the wall test is **not met**.
2. At least one floor percentage is 50% or more AND the whole-structure total is 50% or more → the wall test is **met**. Both readings agree.
3. At least one floor percentage is 50% or more BUT the whole-structure total is under 50% → **do not decide**. Return **FLAG** (not FAIL, not PASS). State that the June 2026 handout computes walls per floor but does not state how floors combine, and that the City must confirm. Show both numbers.

Use the same rule for the interior + exterior wall formula in the appealable area. For the combined roof/walls/foundation test, compute the combined result with the wall figures both ways. If one reading gives 50% or more and the other gives under 50%, return FLAG and show both results.
2. *"Addition(s) to an existing structure that individually, or when combined with prior additions, results in greater than a 50% expansion of the existing structure."*

#### B.3 Coastal Zone Non-Appealable Areas Methodology

Verbatim from the handout, "COASTAL ZONE NON-APPEALABLE AREAS" section: *"City staff will use a less expansive calculation method as these areas are not subject to CCC review."*

| Component | Formula | What Counts |
|-----------|---------|-------------|
| **Exterior Walls only (each floor)** | *"(linear feet of walls to be removed on each floor) ÷ (linear feet of existing walls on each floor) x 100"* | All exterior walls (load-bearing AND non-load-bearing). **Only removal counts** (NOT reinforcement). Drywall/stucco removal does NOT count. Window/door change-outs in same openings do NOT count. Filling in window/door openings does NOT count unless additional structural support is proposed. Compute one percentage for each floor. Combine the floors only by the three-way rule in B.2a. |

A structure IS a major remodel if any of:
1. *"Demolition of 50% or more of the exterior walls occurs"* (apply the three-way floor rule in B.2a).
2. Addition(s) to the existing structure that, individually or cumulative with prior additions, result in **>50% expansion** of the existing structure.

#### B.4 Each Structure Separately; Cumulative Baseline — January 13, 1993

Verbatim from the handout: *"For sites with more than one structure (whether primary dwelling unit or detached accessory buildings or structures, or similar) the above calculation methods shall be applied to each such building or structure independently."*

- Run B.2 or B.3 for each building or structure on its own. Use only that structure's foundation, walls, roof, and floor area.
- Do not add a garage or a detached structure to the primary dwelling's totals.
- Report YES / NO / FLAG for each structure.

Verbatim from the handout (appealable-area section): *"'Existing structure' for the purposes of this section means a structure that legally existed on the site on January 13, 1993. The construction of a new structure or major remodel of an existing structure after January 13, 1993 establishes a new baseline for purposes of calculating cumulative additions over time."* The non-appealable section reads "up to January 13, 1993". The date is the same.

- The baseline belongs to each structure. It is not a site-wide total.
- **NOT a rolling 3-year window.** Earlier Laguna research drafts cited a "3-year rolling cumulative" framing — that does not appear in the handout, the LCP, or LBMC §25.10.008(O). Use Jan 13, 1993.
- **Reset events:** construction of a new structure OR a post-1993 major remodel of an existing structure. The reset applies to that structure.

#### B.5 Carveouts

- **ADUs are exempt.** Verbatim: *"The construction and remodeling of accessory dwelling units are exempt from major remodel calculations."* This is the **only** carveout.
- **No 1,500 sf SFR exception.** That number appears in §25.56.008(C) but governs **parking** for nonconforming SFRs, NOT major-remodel calculation. Earlier research drafts misattributed; do not cite.

#### B.6 Practical Cushion (city advisory)

Verbatim from the handout: *"Although not required, City staff advises applicants to provide a cushion that accounts for unplanned demolition that may sometimes occur during the construction phase of the project — there have been instances where a project was proposed to remain under the 50% demolition threshold, but exceeded 50% due to unforeseen circumstances during construction."*

Treat any structure, or any floor of a structure, landing within ~5% of the 50% threshold under either methodology as **FLAG — applicant should provide cushion analysis or be prepared for major-remodel reclassification mid-construction.**

#### B.7 Nonconforming Status Ends at a Major Remodel

Verbatim from the handout: *"Any legal, non-conforming structure shall be brought into compliance when the threshold for a major remodel is met. When a principal structure undergoes a major remodel, all associated accessory structures and improvements shall be subject to the current zoning regulations and all other applicable requirements, and shall lose their legal, nonconforming status."*

- A structure that meets the threshold must be brought into compliance with current zoning.
- When the principal structure is YES, list every associated accessory structure and improvement that is legal nonconforming. Each one loses that status, even with no work of its own. Require the plans to show how each one complies. See Step F.

Full content: `references/city-major-remodel-methodology.md`.

---

### STEP C — Deterministic Phantom-Remodel Rule (Laguna's Codified 6th Signal)

The parent skill runs a heuristic 5-signal phantom detector with a 2-of-5 / 3-of-5 decision rule. Inside Laguna, the city has **codified** an additional deterministic signal in the May 2026 republish of the Building Plan Check Submittal Requirements (file mod date 2026-04-30), verbatim:

> *"Existing walls with structural upgrades/modifications affecting the foundation or the lateral support (shear) are considered new walls. Existing walls with the drywall removed are considered part of the area of renovation."*

How to apply (deterministic, not heuristic):
1. From the demolition plan + structural plans, identify every wall annotated as "existing to remain" but that EITHER (a) carries new continuous footings, new shear panels, new hold-downs, or any other structural upgrade affecting foundation or lateral support, OR (b) shows drywall removal/replacement.
2. Convert those walls' linear footage into the **renovation/new** column of the Step B calculation.
3. Re-run the Step B coastal zone appealable or coastal zone non-appealable methodology with those walls counted as renovation, on each floor of the affected structure. Compare to 50%.

When this rule re-classifies a project from "remodel" to "major remodel" on **coastal property**, cite **11 Lagunita LLC v. CCC (2020)** in the corrections-letter body alongside the verbatim §1103.5.4 fire-retrofit consequence (if it also fires) and the LCP/handout authority chain. 11 Lagunita is the operative California precedent: a Laguna oceanfront SFR owner pulled "remodel" permits on what was operationally a teardown; CCC reclassified as new construction; $1M penalty + cease-and-desist + seawall removal.

This is **deterministic** because the rule itself converts a wall to "renovation" by definition, no judgment call required. It supplements (does not replace) the parent's heuristic 5-signal detector — both run.

Full content: `references/city-deterministic-phantom-rule.md`.

---

### STEP D — Sprinkler Retrofit (Ch. 14.52.030 AND Title 15 §1103.5.4)

The parent skill correctly identifies that California has **no state-level SFR sprinkler retrofit trigger** (CRC §R309.2 Exception 1 exempts existing un-sprinklered SFRs from retrofit on additions/alterations, and R313 in the 2025 CA CRC is "ceiling height," not sprinklers). **Laguna fills that silence twice.** An existing one- or two-family dwelling has two independent triggers, adopted the same day for the 2026 code cycle. **Either one firing requires the full retrofit. Run both.**

#### Trigger A — LBMC Ch. 14.52.030 (valuation), Ord. 1725, 12/18/2025

Verbatim (the City source document (not included in this plugin) §14.52.030, amending CRC R309.2):

> **R309.2 One- and two-family dwellings automatic sprinkler systems.** ... If the cumulative value of additions, alterations and repairs done to a one- or two-family dwelling and attached garage in any three-year period exceeds fifty percent of the valuation of the one- or two-family dwelling and attached garage prior to the additions, alterations, and repairs, the entire one- or two-family dwelling and attached garage must be sprinklered throughout. The valuation used for the existing building and for the additions, alterations, and repairs is the valuation established in the City's resolution for computation of building permit fees.

One section carries two duties: it mandates sprinklers in **new** one- and two-family dwellings and attached garages, **and** it imposes this valuation retrofit on existing ones. A garage within 10 feet is "attached." Ch. 14.52.026 states the same rule for townhouses.

#### Trigger B — LBMC Title 15 §1103.5.4 (scope), Ord. 1726, 12/18/2025

Verbatim (Fire Code Chapter 11 amendment):

> **Section 1103.5.4 Group R.** An automatic sprinkler system installed in accordance with Section 903.3 shall be provided throughout all existing Group R fire areas when work requiring a building permit that involves alteration of 50 percent or more of a building, which includes or involves work on 50 percent or more of the building's exterior, or which involves the addition of one or more stories.
>
> **Exception:** Work that consists only of the installation of fire-resistant siding.

Any one of these prongs independently fires Trigger B:

1. **Alteration of 50% or more of the building** — use the Step B major-remodel methodology as the operational test.
2. **Work on 50% or more of the building's exterior** — independent of major-remodel determination; e.g., a reroof + reside + fenestration replacement project that hits 50%+ of exterior cladding/roof can fire prong 2 alone.
3. **Addition of one or more stories** — geometric, not %-based.

The fire-resistant-siding exception belongs to Trigger B only. It does not exempt a project from Trigger A.

#### Do not confuse the three 50% rules

Trigger A measures **dollars**. Trigger B measures **physical scope**. The LCP **major-remodel** 50% rule (Step B) measures demolition extent from the January 13, 1993 baseline and decides Design Review and CDP tier — **not** sprinklers. They share a number and nothing else.

When either trigger fires on a CRC-track dwelling, the system must comply with NFPA 13D plus the city's NFPA-13D amendments (sprinklers in attached garages and detached garages within 30 ft, attic protection, exterior overhangs ≥48", exterior alarm, and interior alarm devices). A separate NFPA 13D control valve requires alarm-service supervision. The blanket 24-hour UL central-station rule and ≥75 dBA sleeping-area rule are NFPA 13R amendments for low-rise multi-family, not universal NFPA 13D requirements. The CRC prescriptive design method is deleted (Ch. 14.52.032) — NFPA 13D engineering is mandatory.

Full content: `references/city-sprinkler-retrofit.md` — the single residential retrofit reference for the city.

---

### STEP E — Bluff Overlay (§25.50.004(B)(4) + §25.50.020)

Applies to oceanfront and oceanfront-bluff property only. There is **no standalone "Bluff Overlay" chapter** in the LBMC — the load-bearing rule is at §25.50.004(B)(4) (Building Setbacks on or Adjacent to the Pacific Ocean and Beaches) and §25.50.020 (Oceanfront lots).

#### E.1 25-Foot Bluff-Top Setback (§25.50.004(B)(4)) — verbatim

> *"In addition to (1), (2) and (3) above, no new building, additions to existing buildings, or structures or improvements shall encroach beyond the applicable building stringline or shall be closer than twenty-five feet to the top of an oceanfront bluff; the more restrictive shall apply. Greater setback may be required by the city engineer or building official in order to protect the public health, safety or welfare. Pools and spas shall be no closer than twenty-five feet to the top of bluff. Public accessways shall be exempt from this provision."*

- Oceanfront bluff = "an oceanfront landform having a slope of forty-five degrees or greater from horizontal whose top is ten or more feet above mean sea level" (§25.50.004(B)(4)(a)).
- "More restrictive applies" — if the building stringline is more restrictive than 25 ft, use stringline. The DRB may modify only when the stringline is **significantly more restrictive than** 25 ft AND unique conditions limit development.
- Pre-existing rule. Section history: Ord. 811 (1974); Ord. 832 (1975); Ord. 1187 (1989); Ord. 1223 (1991); Ord. 1354 (1999); Ord. 1416 (2002). **Ord. 1688 is NOT in this section's history.** Ord. 1688 (7/11/2023) amended Ch. 25.07 CDP procedures (§§25.07.008 and 25.07.012), not bluff setbacks. Do not attribute the 25-ft bluff setback to Ord. 1688.
- Building projection setback — balconies, patios, decks, including patio deck covers > 30 inches above finished grade may project a maximum of 5 feet beyond the applicable building setback or to the applicable deck stringline, whichever is least restrictive, **but in no case shall such projections be closer than ten feet to the top of an oceanfront bluff**. Decks/patios ≤30 inches above finished grade — no closer than 10 feet to top of oceanfront bluff.

#### E.2 Site-Coverage Shrinkage on Oceanfront Lots (§25.50.020)

Verbatim §25.50.020(B): *"Building Site Coverage (%) = 35 + (8,000 − A) × 9 / 4,000  Where A = lot area as calculated using the building setback lines described in Section 25.50.004(B)(1), (2) and (3) or the oceanfront bluff whichever is more restrictive."*

This is the second-largest financial trigger after the 25-ft setback itself: lot-area for site-coverage uses the **more restrictive of the elevation-line setback OR the bluff edge**. Practical effect — a project that survives the 25-ft setback may still fail site-coverage because the developable area shrinks.

#### E.3 Anti-Game Buried-Bluff Rule

Verbatim from the city's Bluff Edge Determinations Quick Guide (Mar 2024): *"In areas where fill has been placed near or over the bluff edge, the original bluff edge, even if buried beneath fill, shall be taken to be the bluff edge."* This blocks the gaming pattern where fill is graded over the bluff to push the "bluff edge" seaward. Always require the bluff-edge survey to verify against historical site conditions, not just current topography.

#### E.4 Required Reports for Oceanfront/Bluff-Top Major Remodels

From the Bluff Edge Determinations Quick Guide:
- **Slope-stability analysis** with factor of safety ≥1.5 static and ≥1.2 pseudostatic (k=0.15, or determined through analysis by the geotechnical engineer) for the economic life of the structure. F.S. should be identified for oceanfront and bluff-top lots on a plan or cross section.
- **Sea-level rise** scenarios per the 2018 SLR Guidance, including the medium-high risk-aversion scenario of approximately 6.6 ft.
- **Wave uprush and impact** report considering a seasonally eroded beach combined with 75-year erosion, high-tide conditions, combined with 75-year SLR, storm waves from a 100-year event or a storm comparable to the 1982/83 El Niño.
- Identification of **geologic hazards** affecting the project site and necessary mitigation measures.

Full content: `references/city-bluff-overlay.md`.

---

### STEP F — Nonconforming Structures (Ch. 25.56) — Three Rules, Not One

#### F.0 Major Remodel Ends Nonconforming Status (June 2026 handout)

Check this first. If Step B classifies a structure as a major remodel, the June 2026 Major Remodel Quick Guide governs its nonconformities [source: https://www.lagunabeachcity.net/home/showpublisheddocument/23171/639179723814800000, as of 2026-09-29]. Verbatim: *"Any legal, non-conforming structure shall be brought into compliance when the threshold for a major remodel is met. When a principal structure undergoes a major remodel, all associated accessory structures and improvements shall be subject to the current zoning regulations and all other applicable requirements, and shall lose their legal, nonconforming status."*

- The major-remodel structure must comply with current zoning. Its existing nonconformities do not carry forward.
- When the principal structure is a major remodel, each associated accessory structure and improvement loses its legal, nonconforming status. Require the plans to bring each one into compliance.
- The Ch. 25.56 rules below still apply to a project that is **not** a major remodel.

Below the major-remodel threshold, Ch. 25.56 does **not** have a blanket "loss of nonconforming protection at 50%" rule. It has three distinct rules:

#### F.1 §25.56.008(A) — Any Expansion Triggers Full Title 25 Conformance for the Expansion Portion (operative for SFR remodels)

Verbatim §25.56.008: *"A legal nonconforming structure may be enlarged or expanded if: (A) The enlargement or expansion complies in every respect with all applicable provisions of this Title 25 Laguna Beach Municipal Code; ..."* — i.e., no % threshold, but the **expansion portion must fully conform** to current Title 25 (setbacks, height, coverage, parking, etc.). Existing nonconformities on the unmodified portion are not blanket-extinguished, unless the structure is a major remodel (F.0).

§25.56.008(C) parking exception: existing single-family dwellings with a nonconforming number of required parking spaces may be enlarged without complying with the required number of spaces **if** the total gross floor area of the residential structure (including the proposed enlargement or addition) does not exceed **1,500 sq ft** AND at least one parking space is provided on the property. (This is the rule that the 1,500 sf number actually governs — it is **not** a major-remodel exemption.)

#### F.2 §25.56.014 — 50% Damage Restoration: MULTI-FAMILY ONLY

Verbatim §25.56.014: *"Notwithstanding the extent of damage, any legal nonconforming building, structure or improvement which has been damaged by fire, flood, wind, earthquake or other disasters may be repaired, restored, replaced or reconstructed up to the original size, placement and density within five years of such damage or destruction, notwithstanding any other provision of this title; provided, however, that no multiple-family dwelling which has been so damaged to the extent of more than fifty percent of the value of such building, structure or improvement immediately prior to such calamity shall be repaired, restored, replaced or reconstructed unless the provisions of Chapter 25.52 are complied with in full; ..."*

- **Applies to multi-family only**, not SFR. SFRs damaged by fire/flood/wind/earthquake may be reconstructed up to original size/placement/density within 5 years regardless of damage extent.
- For multi-family >50% damaged → full Ch. 25.52 (parking) compliance triggered.
- Shore protective devices: separate rule — restoration only if consistent with prevailing zoning + general plan policy.

#### F.3 §25.56.020(C) — 50% Density/Intensity Triggers Ch. 25.53 Access Standards

Verbatim §25.56.020(C): *"If additions or alterations exceed fifty percent of the existing population density or intensity of use, the provisions of Chapter 25.53 (Access and Improvement Requirements) shall apply..."* — i.e., the 50% trigger here is for **access standards**, not blanket loss of nonconforming protection. Improvement requirements may be limited per the section's qualifications.

#### F.4 §25.56.009 — Removal of Nonconforming Portion During Modification

Verbatim §25.56.009: *"If any part of a nonconforming portion of the structure is substantially removed or modified in such a way that it compromises the structural integrity of the building, that portion must be rebuilt in conformance with zoning regulations."* — i.e., if a nonconforming wall is removed mid-construction (or its structural integrity is compromised), the rebuilt portion must conform.

Full content: `references/city-nonconforming.md`.

---

### STEP G — Coastal Development Permit (Ch. 25.07)

Ch. 25.07 governs CDP procedure. The state skill (`../coastal-development/references/california-baseline.md`) covers the substantive CDP analysis. This step layers in two Laguna-specific notes:

#### G.1 Major Remodel in Coastal Zone Always Requires CDP

A "major remodel" — as determined by the Step B methodology — is **development** under §25.07.006(D) and is not within the §25.07.008 single-family-dwelling improvement exemption (the exemption applies only to "improvements ... [that] are normally associated with a single-family dwelling," and explicitly excludes any improvement to a structure between the sea and the first public roadway that "would constitute or result in ... an increase of ten percent or more of an internal floor area" or "an increase in height of more than ten percent" — let alone a 50% major remodel). A major remodel in the coastal zone therefore always requires a CDP regardless of any E-93-1 categorical exclusion.

#### G.2 ADU Coastal Exemption Pushback — CCC F9a-11-2024

The California Coastal Commission's F9a-11-2024 Notice of Pending Action / decision rejected Laguna's E-93-1 ADU categorical exemption as applied to ADUs in the coastal zone. **ADUs in Laguna's coastal zone still need a CDP.** When a residential remodel scope includes an ADU (attached/detached/JADU/conversion), flag prominently:

- ADU ≠ exempt from CDP merely because the city's E-93-1 categorical exclusion claims it
- The ADU likely still needs a CDP processed under Ch. 25.07
- This is independent of whether the rest of the remodel triggers a CDP

#### G.3 Categorical Exclusion (E-93-1) — Scope Limited

§25.07.010 provides that "Development included in any categorical exclusion area adopted pursuant to the California Coastal Act is exempt from the regulations contained in this chapter except for the notice requirements contained within California Code of Regulations Section 13248." E-93-1 is Laguna's categorical exclusion. Its scope is narrower than Laguna staff historically assumed; CCC F9a-11-2024 narrowed it further for ADUs. For major remodels and bluff/oceanfront work, do not assume E-93-1 covers the project — apply the §25.07.008 analysis instead.

Full content: `references/city-cdp-coastal-zone.md`.

---

### STEP H — VHFHSZ + WUI (Ch. 14.70 + CFC §304/§324)

Laguna is predominantly VHFHSZ (citywide coverage: `../city-reference/SKILL.md`). Major remodels and new construction in the VHFHSZ + Fuel Modification designation must comply with **both** Ch. 14.70 (the city's WUI Code amendments) **and** CFC §304/§324 (the city's Fire Code amendments per Title 15 §15.01.030):

| Topic | Section | Requirement |
|-------|---------|-------------|
| Class A roof | §14.70.020 | Class A roof required for all new roofs and re-roofs |
| Exterior wall coverings | §14.70.030 | Noncombustible or ignition-resistant |
| Vinyl windows | §14.70.035 | Welded corners + metal reinforcing |
| Skylights | §14.70.040 | Glass only; no plastic skylights |
| Vent openings | §14.70.025 | Maximum 144 sq in |
| Defensible space | §14.70.060 + CFC §304.1.3.2 | August 2021 Defensible Space Guideline for existing structures in VHFHSZ |
| Fuel modification plans | §14.70.070 + CFC §324 | Required for new construction or major remodel in city Fuel Modification designation; preliminary fuel-mod plans concurrent with tentative-map submittal; final fuel-mod plans approved prior to building permit issuance |
| §25.05.040(C)(4) Fire Safety Standards Review | §25.05.040(C)(4) | Before Design Review deliberation on new construction and major remodels, the Fire Department or Building Division, as applicable, reviews and approves or conditionally approves the application, including fuel-modification programs. The former 50%-alteration Fire-Department-only trigger is not current. |

Cross-reference: `../wildfire-wui/SKILL.md` (state skill) for the underlying CRC Ch. 7A and CBC Ch. 7A frameworks.

Full content: `references/city-vhfhsz-wui.md`.

---

### STEP I — View, Heritage Tree, Hillside Overlays

#### I.1 View (Ch. 12.16)

Ch. 12.16 (View Restoration) is **vegetation-only**. Building view impacts are NOT enforced via Ch. 12.16; when Design Review applies, they are evaluated under current §25.05.040(H)(11) "View Equity." When a remodel proposes vegetation that will impact a neighboring view, route through Ch. 12.16. When a current Design Review category applies to building mass changes that may affect views, evaluate View Equity in that proceeding.

**Prior view decisions bind this owner — §12.16.100, amended effective 2026-08-20.** Decisions by city staff and the View Restoration Committee on view restoration and view preservation **run with the land** and bind the claimant, the vegetation owner, and their heirs, successors and assigns. To the extent permitted they are recorded in Orange County official records and are set forth in any real property report required by **Ch. 14.76**. If a record of views or a view restoration order already exists for the subject property or an adjacent one, the current owner inherits it — a remodel landscape plan cannot quietly undo it. Check the property file and the real property report; the record of views is noted there under §12.16.040(b), as amended effective 2026-08-20. [source: the City source document (not included in this plugin) lines 123, 143]

#### I.2 Heritage Tree (Ch. 12.06 + 12.08)

A Tree Removal Permit (TRP) is required when project scope encroaches on the drip-line or critical root zone of any heritage tree. Heritage tree **removal** requires City Council approval (not DRB, not Director). When a remodel scope includes grading, foundation, or hardscape within ~10 ft of any tree on city's heritage tree register, flag for TRP analysis.

**Development benefits now require a written agreement — §12.08.030(b), amended effective 2026-08-20.** Heritage tree owners remain eligible for benefits related to potential development improvements on the property. The amendment conditions the grant of any such benefit on a **written agreement between the city and the property owner** ensuring continued preservation and maintenance of the heritage tree(s) on the subject property, and that agreement must include a provision binding **subsequent** heritage tree owners to continue preservation and maintenance. If a remodel claims a heritage-tree development benefit, FLAG the written agreement as a required step before the benefit is granted — do not treat the designation alone as sufficient. Notice of the heritage tree also appears in the property file and in the real property report the city issues on sale. [source: the City source document (not included in this plugin) line 105]

#### I.3 Hillside (R/HP zone, Ch. 25.15) + Title 22 (Grading)

- Grading over 20 cubic yards outside the building footprint requires Design Review under current §25.05.040(B)(1)(f), subject to §22.10.010(e); separately determine the grading permit
- Geotechnical report required for hillside, coastal, and vacant lots (city handout "When a soils report is required" — $5,000 deposit for peer review per Building Plan Check Submittal Requirements)
- Cut/fill restrictions, slope stability, and view-equity overlay all interact

Full content: state skill the California Residential Remodel rules, which come from the CrossBeam connector (see "California Code Compliance" below) does not duplicate this; see Laguna `references/city-vhfhsz-wui.md` and the Geotech section in the Building Plan Check Submittal Requirements for cross-references.

---

### Output Format

For each city overlay test that fires, return:

```
## [Overlay] -- [Name]
**Result:** PASS | FAIL | FLAG | N/A | DISPATCHED
**Code:** [Section number — verbatim, e.g., "LBMC Title 15 §1103.5.4"]
**Finding:** [What was verified or what failed; 1–3 sentences]
**Citation:** [Verbatim quote of the operative threshold]
**Action required:** [What the applicant must do]
```

Aggregate at the end of the city overlay:
- **Planning route:** Zone Clearance / Administrative Design Review / Design Review / `needs_source` (from Step A; a Step B major-remodel finding matches §25.05.040(B)(1)(a))
- **Major Remodel:** YES / NO / FLAG for each structure on the site (with methodology applied, the wall percentage for each floor, and the whole-structure wall total)
- **Nonconforming status ended (June 2026 handout):** list each structure and improvement that loses legal, nonconforming status, or N/A
- **CDP Required:** YES / NO (with reasons)
- **Sprinkler Retrofit Required:** YES / NO — state which trigger fired: Ch. 14.52.030 (valuation) and/or Title 15 §1103.5.4 (with which prong). If the documents do not state a valuation, report Trigger A as undetermined and request it.
- **Bluff Overlay:** APPLICABLE / N/A
- **VHFHSZ + WUI:** APPLICABLE / N/A
- **CCC F9a-11-2024 ADU Pushback Flag:** YES / NO
- **Phantom-Remodel Re-classification (deterministic):** TRIGGERED / NOT TRIGGERED (with which walls converted)

---

### Key Principles

1. **Layer, don't duplicate.** State law lives in the parent skill. This skill only adds Laguna-specific overlays.
2. **Route first.** Always run Step A's current closed-list classifier first — it determines the procedural envelope (notice timing, hearing requirement, and authority) that everything else hangs off of.
3. **Major remodel is operative-but-interpretive.** The dual-methodology section is the city staff's interpretation of CCC staff's analysis, not statutory rule. Mirror the handout's own hedge in any output that quotes the methodology. A Municipal Code amendment is in process — re-check.
4. **Sprinkler retrofit has two triggers and either one fires it.** Ch. 14.52.030 is the valuation test (50% cumulative in any three-year period). Title 15 §1103.5.4 is the scope test (50% building / 50% exterior / added story). Both are current, both were adopted 12/18/2025. Run both on every existing one- or two-family dwelling and name the one that fired. Never report the retrofit as governed by only one of them.
5. **Cumulative baseline is January 13, 1993, not a rolling 3-year window.** The baseline belongs to each structure. It resets only on construction of a new structure or a post-1993 major remodel of that structure.
6. **ADU is the only major-remodel carveout. No 1,500 sf SFR exception exists.** 1,500 sf is a parking rule (§25.56.008(C)).
7. **Bluff = §25.50.004(B)(4) + §25.50.020.** Pre-existing rule (Ord. 811 1974 → Ord. 1416 2002), NOT Ord. 1688.
8. **Ord. 1688 (7/11/2023) amended §25.07 CDP procedures, not bluff setbacks.**
9. **Ch. 25.56 has three rules, not one.** Below the major-remodel threshold, there is no blanket loss of nonconforming protection at 50%. §25.56.014 50%-damage rule applies to **multi-family only**. At a major remodel, the June 2026 handout ends nonconforming status for the structure and, for a principal structure, for its accessory structures and improvements.
10. **CDP required for major remodel in coastal zone regardless of E-93-1.** ADUs still need CDP per CCC F9a-11-2024.
11. **Deterministic phantom rule supplements, not replaces, the parent's heuristic.** Both run.
12. **Cite verbatim. Trace every load-bearing threshold to a specific on-disk source file in the City source document (not included in this plugin).**

---

## City Submittal Checklists

The City's own lists of what a submittal must contain. They ship in this plugin; paths are relative to this file.

- `../../requirements/README.md` — the index: which checklist covers which scope
- `../../requirements/plan-sheets/plan-sheet-matrix.md` — which plan sheets the project needs and what each sheet must show
- `../../requirements/building/` — the Building Division submittal checklists
- `../../requirements/planning/application-index.md` — which Planning application to file
- `../../requirements/issuance/issuance-checklist.md` — what is due after approval, before the permit issues

Choose the checklists from the project scope the evidence shows, not from the permit name. When a plan set exists, run `../plan-set-check/SKILL.md` on it. These are completeness checks. They do not check the design against the code.

---

## California Code Compliance

This plugin does not carry the California code checklist for Residential Remodel plan sets: the building, residential, structural, fire and life-safety, energy, green-building, plumbing, mechanical, electrical and accessibility requirements. That check comes from CrossBeam.

**When the CrossBeam connector is connected** (the host has tools whose names start with `crossbeam_`):

1. Call `crossbeam_get_review_requirements` with `city: "laguna-beach"` and `permit_type: "residential-remodel"`. It returns the review lanes, the required documents and the packaging rules, with citations. Read it beside the City checklists above. Where they differ, tell the user and cite both. Coverage `none` means CrossBeam has no data, not that nothing is required.
2. Ask code questions with `crossbeam_ask`. Send the city (Laguna Beach, CA), the permit type and the project facts you have, and follow up with its `conversation_id`. A code section the answer cites that is not in its citations is unverified.
3. To check a plan set against the code, use a CrossBeam check. For a set drawn with CrossBeam's permit-drawings skill, call `crossbeam_get_skill` with `skill_id: "permit-drawings"` and follow `../../references/plan-sheets.md` section 2; permit-drawings runs the check. For a set drawn by someone else, the user uploads it for a CrossBeam check in the CrossBeam app, because the connector does not upload plans; then read the results with `crossbeam_list_projects`, `crossbeam_get_project_summary` and `crossbeam_get_findings`. A CrossBeam check is paid. Start one only with the user's approval.

CrossBeam cites the current 2025 California Building Standards Code (Title 24, effective 2026-01-01). Use its citations over code sections you remember. Apply the Laguna Beach rules above on top of them.

**When the connector is not connected**, or a tool is missing or needs sign-in:

- Do not check the design against the California codes from memory, and never report a California code item as passing.
- Do the Laguna Beach rules and the City checklists in full, then list California code compliance as **not checked**.
- Say it plainly, once: "This plugin checks the Laguna Beach rules and the City's submittal checklists for Residential Remodel permits. It cannot check the plans against the California building codes. For that, connect CrossBeam (crossbeam-permits.com) and run a CrossBeam check before you file."
- Then carry on with intake, the City checklists and filing.

---

## References

Load these on demand. Paths are relative to this file.

- `../../requirements/README.md` — the City submittal checklists, plan-sheet matrix and issuance checklist
- `../plan-set-check/SKILL.md` — checks a plan set against the City checklists
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**Laguna Beach rules**

- `references/city-bluff-overlay.md` — Laguna Beach — Bluff Overlay (§25.50.004(B)(4) + §25.50.020)
- `references/city-cdp-coastal-zone.md` — Laguna Beach — Coastal Development Permit (Ch. 25.07)
- `references/city-design-review-tiers.md` — Laguna Beach — Current Design Review Routing (Ord. 1732)
- `references/city-deterministic-phantom-rule.md` — Laguna Beach — Deterministic Phantom-Remodel Rule (Codified 6th Signal)
- `references/city-major-remodel-methodology.md` — Laguna Beach — Major Remodel Methodology (Operative-but-Interpretive)
- `references/city-nonconforming.md` — Laguna Beach — Nonconforming Structures (Ch. 25.56)
- `references/city-sprinkler-retrofit.md` — Laguna Beach — Residential Sprinkler Retrofit (TWO triggers)
- `references/city-vhfhsz-wui.md` — Laguna Beach — VHFHSZ + WUI (Ch. 14.70 + CFC §304/§324)

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
