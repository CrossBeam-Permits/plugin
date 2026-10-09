---
name: reroof
description: "Reroof permits in Laguna Beach, CA. Roof covering replaced or overlaid on an existing roof, whole or partial, including the partial reroof under a solar array. NOT new roof framing. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions reroof in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Building Code (Title 24, Part 2 CBC, Part 2.5 CRC, Part 4 CMC, Part 5 CPC, Part 6 Energy, Part 11 CALGreen); LBMC Ch. 14.70 (WUI Code), Ch. 14.50 (Building Code amendments), Ch. 25.05 (Design Review), Ch. 7.19 (C&D waste), Title 15 (Fire Prevention); City Building Division REROOFING handout (2026-08-12)"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "2026-08-15"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Reroof Permit

Handles reroof permits in Laguna Beach end-to-end. Scope: Roof covering replaced or overlaid on an existing roof, whole or partial, including the partial reroof under a solar array. NOT new roof framing.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a reroof permit, or (B) a city reviewer checking a submitted one?"

- Mode A → walk **MODE A — Builder / Homeowner Intake** below
- Mode B → walk **MODE B — City Reviewer** below

Both modes share the same rules. The Laguna Beach rules come first; the California checklist applies wherever Laguna does not override it.

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

Then establish, from evidence, the facts the **Laguna Beach Rules** below turn on: the Planning route, the coastal zone, overlays, and any triggers they name. Unknown answers stay unknown. Do not assume a route, an exemption, or compliance. Use the checklists below as the coverage floor for what to ask, without interrogating. When preparing files or navigating intake, read `../../SKILL.md` for the canonical artifact and transaction workflow.

### A2. Pre-submission Compliance Check

Once you have enough information, walk the Laguna Beach rules and then the California checklist using the user's answers. For every item:
- **FAIL** → tell the user the specific change needed before they submit
- **FLAG** → tell them what information or documentation they still need
- **PASS** → confirm and move on

### A3. Submission Guide

When compliance is clean (or flag-only), produce a submission guide. Do not promise over-the-counter issuance unless the Laguna Beach rules below say the scope qualifies.

```
## Ready to Submit — Laguna Beach Reroof Permit

**Planning route:** [from the Laguna Beach rules, or "none required"]
**Parallel applications:** [Coastal Development Permit, Design Review, or none]

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
3. Walk the Laguna Beach rules, then the California checklist, in order
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

—
Generated by CrossBeam Permits · crossbeam-permits.com
```

Summary verdict at the end: **APPROVE** | **CORRECTIONS REQUIRED** | **NEED ADDITIONAL INFO**

Do not list inspection items as corrections. Do not enumerate every passing item unless the user asks. Respect the plan checker's time.

---

## Laguna Beach Rules

> Laguna Beach's local layer for this permit. It adds to or overrides the California checklist below. Paths are relative to this file.

**Base skill:** `references/california-baseline.md`
**This skill contains ONLY items where Laguna Beach differs from state code.**
**All state checklist items apply unless explicitly overridden below.**

**VHFHSZ fire requirements and a citywide roof color standard make Laguna Beach re-roofs more complex than typical CA cities.**

City source of record for the substantive rules below: the Building Division's **REROOFING** handout (with its
COLOR GUIDE), received from the City **2026-08-12** —
the City source document (not included in this plugin).

---

### Decision Tree Router

| Project Type | Route |
|-------------|-------|
| **Re-roof**, no dimension/SF/pitch change, not white/light, no glare | OTC may be eligible; design-review **exempt with Zone Clearance** per current §25.05.040(B)(2)(e) → `references/city-roof-color-standards.md` for the separate color gate |
| **Re-roof** resulting in a white/light roof or possible glare | **Administrative Design Review** under §25.05.040(B)(3)(a)(ix) |
| **Re-roof** changing dimensions, square footage, or roof pitch | **Administrative Design Review** under §25.05.040(B)(3)(a)(x), unless a Design Review trigger independently applies |
| **Overlay (recover)** proposed over existing **wood shake** | City prohibits — tear-off required → "Overlay Limits" below |
| **Re-roof** on a historic / Register-listed / 50+-year structure | FLAG for Planning — `../city-reference/SKILL.md` §5, `../single-family-residential/references/heritage-historic-committee.md` |
| **Re-roof** as part of major remodel | Full plan review |

---

### OTC-Eligible Re-Roofs

Re-roofing qualifies for over-the-counter review if:
- Same material or lighter weight material
- No structural modifications
- Not part of a project triggering major remodel

**OTC-eligible per the city reference OTC item 7** — re-roof with same material or lighter. Hours and the full OTC list: `../city-reference/SKILL.md` §"Permit Processing Tracks".

**Process note (volatile — City handout, as of 6/23/26):** applications may be submitted as (2) sets in person
or (1) digital set online, but ***"As of 6/23/26, all reroof permits are issued in person at the counter"***.
Submittal channel and issuance channel are different things here; re-verify this row with the City before
relying on it, process rows go stale faster than code rows.

---

### Roof Color and Finish — Citywide Standard (City delta)

Laguna Beach restricts roof **color and finish** citywide, and **materials and colors must be approved prior to
permit issuance**. There is no state analogue — California regulates fire class and solar reflectance, not hue.

Headline rules (full standard, per-material table, the City's photo examples, and the cool-roof conflict:
**`references/city-roof-color-standards.md`**):

- **No light colors** — white, tan, light gray are banned; no highly reflective roof materials.
- **Flat roofs** (TPO/EPDM/PVC membrane): dark brown, dark gray, or black.
- **Metal roofs**: acceptable **with condition** — matte finish coating to eliminate reflective glare.
- **Color samples are a submittal item and an issuance gate** — an application naming a product but no color, or
  a color with no sample, is incomplete for issuance even when every state-code check passes.
- Judging a borderline color is a reasoning step against the City's stated categories and photo examples —
  there is no published LRV/SRI threshold. Borderline → FLAG for Building Division color approval.

---

### Design Review — current Ord. 1732 routing (City delta)

The re-roof design-review exemption is **conditional**, not automatic. Both branches must be carried.

Section 25.05.040 was replaced after the Building handout was issued. Current subsection (B)(2)(e) routes a reroof to **Zone Clearance** when it does not result in a white or light-colored roof, makes no change to dimensions, square footage, or roof pitch, and will not result in glare, as determined by the Community Development Director.

Current Administrative Design Review categories separately cover:

- white/light-colored roofs and possible glare, (B)(3)(a)(ix); and
- changes to roof dimensions, square footage, or pitch, (B)(3)(a)(x).

Do not use the pre-ordinance `(B)(2)(f)` test or treat a material change alone as a categorical ADR trigger. Class A and the City color policy remain separate Building/WUI requirements. Planning decides the Zone Clearance/ADR branch; historic-resource procedures may also apply.

---

### Overlay Limits — one genuine city delta (City delta)

The state floor already governs layer counts and prohibited substrates (`references/reroof-overlay-rules.md`,
CBC 1512.3 / CRC R908.3): max one existing layer (two total), and **no overlay over slate, clay, cement, or
asbestos-cement tile**. The City handout restates those — nothing to encode.

**The delta is wood shake.** The handout says:

> **Don't:** Apply overlays on wood shake, slate, clay, cement or asbestos tile

State code **permits** recover over existing wood shakes (metal panel, metal shingle, or concrete/clay tile)
when the combustible concealed space is covered with gypsum board, mineral fiber, glass fiber, or other approved
noncombustible material (CBC 1512.3.1). **Laguna Beach's Building Division prohibits it outright — tear-off is
required over wood shake.** The state skill's own note to "FLAG overlay over wood shakes for inspector review"
resolves against the applicant in Laguna.

**Provenance caveat (be precise about this in findings):** this ban is stated in the City's 2026-08-12 handout.
It is **not** traced to an adopted ordinance — LBMC Ch. 14.50 (Building Code amendments), Ch. 14.52 (Residential
Code) and Ch. 14.70 (WUI) contain no amendment to CBC 1512 / CRC R908 (checked 2026-08-12). Cite the handout as
the City's stated policy, not a code section, and frame the applicant's path as a building-official
alternate-means discussion rather than a code argument they can win on CBC 1512.3.1.

---

### Product Evaluation Report (City delta)

> ***Note: A third party verified evaluation report number from an approved testing agency is required
> (Example: ICC, PRI, UL product IQ, QAI, IAPMO, etc.)***

The state floor asks for an ICC-ES report number for **tile** (state check #6). Laguna requires a third-party
evaluation report number for the roofing product **regardless of material** — the City's own description
template carries one inline ("GAF Timberline composition shingles **ESR-1475**"). An application with no
evaluation report number is incomplete.

---

### Waste Management Plan + Security Deposit (City delta)

> **Do:** Submit a Waste Management Plan and separate security deposit (check or cash) for tear-off reroofs,
> per Municipal Code 7.19 (exempt if no tear-off)

State CALGreen §5.408 requires 65% diversion and a waste management plan on tear-off. Laguna adds a **separate
refundable security deposit (check or cash) under LBMC Ch. 7.19**. **Overlay/recover scopes with no tear-off are
exempt** from both the plan and the deposit. Solid Waste Division: (949) 464-6677 / Recycle@LagunaBeachCity.net.

---

### VHFHSZ Fire-Resistive Roofing Requirements

Laguna Beach is predominantly Very High Fire Hazard Severity Zone (citywide coverage: `../city-reference/SKILL.md`). Fire-resistive roofing requirements are CRITICAL:

#### Laguna Beach Amendments (Ch. 14.50 Building Code, Ch. 14.70 WUI Code)
- **Class A roofing required citywide** — this is ordinance-backed, not just handout policy. **LBMC §14.50.120**
  amends CBC §1505.1 verbatim: "A Class A roof assembly or roof covering is the minimum class of roofing that
  can be applied on **any building in the City** for either new roofing or reroofing. Roofing and reroofing must
  also comply with Section 504.2 of the California Wildland-Urban Interface Code." So Class A does **not** depend
  on a parcel-level FHSZ lookup, and the handout's "Use Class 'A' fire-rated assemblies for all reroofs"
  (2026-08-12) is the Division restating its own code.
  - **Exception (§14.50.120, exc. 2):** with the approval of the building official, **reroofing of small portions
    of a roof** may be done with the same material as exists on the roof. Mirrors the §14.70.015 minor-repair
    exception — building official approval is required, it is not automatic, and a whole-roof scope never qualifies.
- **Ch. 14.70 §14.70.020 (WUI 504.2)** independently requires Class A on all roofs/re-roofs (ASTM E108/UL 790)
- **Roof vents**: Maximum 144 sq in opening size
- **No plastic skylights** — glass only
- **Noncombustible exterior wall covering** required (ignition-resistant materials)
- **Welded vinyl windows** required (welded corners + metal reinforcing)

Note: Other fire-resistive roofing details (ember-resistant vents, eave/soffit construction, valley flashings, gutters) come from state Chapter 7A via the `california-reroof` skill — they are NOT Laguna Beach city amendments.

#### Major Remodel vs. Sprinkler Retrofit — different tests, same number
**Major remodel** (area-based): In the coastal zone appealable area, roof area removed/reinforced counts in the combined roof/walls/foundation test. If the combined roof/walls/foundation of the structure reaches 50% or more, it constitutes a major remodel. This triggers new construction standards and full plan review (not OTC).

**Sprinkler retrofit** — classify the Group R building before selecting its valuation section (`../city-reference/SKILL.md`, "Sprinkler Retrofit Triggers"; full rule in `../residential-remodel/references/city-sprinkler-retrofit.md`):
- **LBMC Ch. 14.52.030** (valuation, Ord. 1725 12/18/2025) — cumulative additions, alterations and repairs to a one- or
  two-family dwelling and attached garage in any three-year period exceeding 50% of the pre-work valuation. **A re-roof
  valuation counts toward that total**, so a re-roof stacked on recent permits can fire the retrofit by itself.
- **LBMC Title 15 §1103.5.4** (scope, Ord. 1726 12/18/2025) — alteration of ≥50% of the building, OR work on ≥50% of the
  exterior, OR an added story. A re-roof alone does not usually fire it, but roof area counts toward the exterior prong.
- **CBC-track Group R (including 3+ unit multi-family): LBMC §14.50.104/CBC §903.6(1),(5)** — run its
  50%-valuation and Building Official substantial-renovation tests in addition to Title 15 §1103.5.4.
- **Other-than-R/U occupancies: LBMC §14.50.104/CBC §903.6(2)** — both the post-work
  sprinklers-required condition and the 50%-valuation condition must be met. Section 903.6 also has
  addition-specific triggers; do not reduce it to an unconditional 50% rule.

Both triggers, when they fire, require full WUI compliance and full plan review (not OTC).

---

### Major Remodel Interaction

Source: City Major Remodel Interpretation Quick Guide, Updated June 2026 [source: https://www.lagunabeachcity.net/home/showpublisheddocument/23171/639179723814800000, as of 2026-09-29].

In the **coastal zone appealable area**, roof replacement is part of the major remodel calculation:
- Formula: (SF of roof removed/reinforced, including eaves) / (SF of existing roof) x 100
- The handout's trigger is "Demolition or reinforcement of 50% or more of the exterior walls OR combined roof/walls/foundation of the structure." The roof counts in the combined test. Roof work alone is not a separate trigger.
- Run the test for each building or structure on the site independently. A reroof of a detached garage is measured against the garage, not the house.

In the **coastal zone non-appealable area**, roof is NOT part of the calculation (only exterior walls count, on each floor).

---

### Coastal Zone — cross-lane pointer

The City's reroof handout routes coastal parcels before anything else:

> **Coastal Appealable Area:** file a **CDP Exemption** and wait out a 10 working day appeal
>
> **Deferred Certification Zone:** This is under the direct jurisdiction of the State. Complete and submit all
> **Appendix B forms** and send the required application fees directly to the California Coastal Commission

Zone confirmation is the City's GIS viewer (`gis.lagunabeachcity.net`), and a parcel that **straddles** a zone
boundary must be said as straddling, never point-sampled to one side. Do not adjudicate coastal status inside
the reroof review — surface the routing and point to `../coastal-development/SKILL.md` and `../city-reference/SKILL.md` §2.

---

### Laguna Beach Re-Roof Review Checklist — City Overlay

Walk these AFTER the state-level checklist. Record PASS / FAIL / FLAG / N/A with the section cited.

| # | Check | What to Verify | Code Section | Reference File |
|---|---|---|---|---|
| LB-1 | **Class A citywide** | Roof assembly is Class A per ASTM E108/UL 790. Required on **any building in the City**, new roofing or reroofing — not gated on a parcel FHSZ lookup. Small-portion same-material reroof is the only exception, and it needs building-official approval. | §14.50.120 (amending CBC 1505.1); §14.70.020 (WUI 504.2) | `references/city-wui-roofing.md` |
| LB-2 | **Roof color** | Not white, tan, or light gray, and not a highly reflective material. Flat/membrane roofs: dark brown, dark gray, or black. Borderline hue → FLAG for Building Division approval, do not guess. | City reroof handout, COLOR GUIDE (2026-08-12) | `references/city-roof-color-standards.md` |
| LB-3 | **Metal roof finish** | Metal roofs acceptable only with a matte finish coating applied to eliminate reflective glare. Unmatted standing seam → FAIL. | City reroof handout, COLOR GUIDE (2026-08-12) | `references/city-roof-color-standards.md` |
| LB-4 | **Color approved before issuance** | Material details and a color sample/swatch are in the submittal. Missing color or missing sample = incomplete for issuance regardless of code compliance. | City reroof handout, "Approval" (2026-08-12) | `references/city-roof-color-standards.md` |
| LB-5 | **Overlay over wood shake** | If existing covering is wood shake and an overlay/recover is proposed → tear-off required; report it as failing the City's stated policy, not a code section (no LBMC amendment to CBC 1512 exists). State would allow it with noncombustible separation per CBC 1512.3.1 — say so, and route the applicant to the building official. | City reroof handout, "Rules & Color Restrictions" (2026-08-12) | "Overlay Limits" above; `references/reroof-overlay-rules.md` |
| LB-6 | **Planning route** | Zone Clearance when current `(B)(2)(e)` conditions are met; ADR for a white/light or possibly glaring roof `(B)(3)(a)(ix)` or a dimension/SF/pitch change `(B)(3)(a)(x)`. Apply any independent ESA/Design Review trigger. | §25.05.040(B)(2)(e), (B)(3)(a)(ix)-(x) | `../residential-remodel/references/city-design-review-tiers.md` |
| LB-7 | **Historic / 50+ year structure** | Register-listed, historic, or 50+-year structure → FLAG for Planning/Heritage; the handout warns of additional requirements without stating them. | LBMC Ch. 25.45 | `../single-family-residential/references/heritage-historic-committee.md`; `../city-reference/SKILL.md` §5 |
| LB-8 | **Evaluation report number** | Third-party evaluation report number from an approved agency (ICC, PRI, UL Product iQ, QAI, IAPMO) provided for the roofing product — all materials, not just tile. | City reroof handout (2026-08-12) | N/A |
| LB-9 | **Waste plan + deposit** | Tear-off: Waste Management Plan **and** separate security deposit (check or cash) per LBMC Ch. 7.19. No tear-off (overlay) → exempt. State CALGreen 65% diversion still applies to tear-off. | LBMC Ch. 7.19; CALGreen 5.408 | N/A |
| LB-10 | **Coastal routing** | Coastal Appealable Area → CDP Exemption + 10-working-day appeal window. Deferred Certification Zone → Appendix B forms + fees direct to the Coastal Commission. Straddling parcels must be reported as straddling. | Ch. 25.07 | `../coastal-development/SKILL.md` |
| LB-11 | **Sprinkler retrofit** | Classify occupancy first. CRC-track house/townhouse → Ch. 14.52.026/.030 valuation plus Title 15 §1103.5.4 scope. CBC-track Group R → §14.50.104/§903.6(1),(5) plus Title 15 §1103.5.4. Other-than-R/U → apply the conditional §903.6(2) test and addition triggers. | Ch. 14.52.026/.030; Title 15 §1103.5.4; §14.50.104/§903.6 | `../residential-remodel/references/city-sprinkler-retrofit.md`; `references/city-fire-amendments.md` |
| LB-12 | **Major remodel** | Coastal zone appealable area: roof area removed/reinforced ÷ existing roof area counts in the combined roof/walls/foundation test for that structure; combined 50% or more → major remodel, full plan review. Coastal zone non-appealable area: roof does not count. | §25.05.040 | `../residential-addition/references/city-major-remodel.md` |

#### Output Format

```
## LB-[#]. [Check Name]
**Result:** PASS | FAIL | FLAG | N/A
**Code:** [Section number]
**Finding:** [1-2 sentence explanation]
```

---

### Key Laguna Beach Re-Roof Facts

- **OTC eligible**: Yes — same/lighter material, no structural mods. Permits **issued in person at the counter** as of 6/23/26 (verify — volatile).
- **Fire rating**: Class A on **any building in the City**, new or reroof, per §14.50.120 (CBC 1505.1 as amended) + §14.70.020 — ordinance-backed, not FHSZ-gated. Small-portion same-material reroof needs building-official approval.
- **Roof color**: no white/tan/light gray or reflective materials; flat roofs dark brown/dark gray/black; metal needs a matte finish. Colors approved **before permit issuance**.
- **Overlay**: no overlay over **wood shake** (City policy, stricter than state — no LBMC amendment found), slate, clay, cement, or asbestos tile; max one overlay on asphalt/wood shingle (state floor)
- **WUI code**: Ch. 14.70 — extensive fire-resistive requirements
- **Planning route**: qualifying reroof → Zone Clearance under §25.05.040(B)(2)(e); white/light or glare → ADR `(B)(3)(a)(ix)`; dimensions/SF/pitch change → ADR `(B)(3)(a)(x)`
- **Historic**: additional requirements may apply — FLAG for Planning (Ch. 25.45)
- **Evaluation report**: third-party report number required for all roofing products
- **Waste**: Waste Management Plan + separate security deposit per LBMC 7.19 on tear-off; exempt if no tear-off
- **Major remodel**: Roof replacement counted in the combined roof/walls/foundation test in the coastal zone appealable area
- **Sprinklers**: CRC-track houses/townhouses use Ch. 14.52.026/.030 valuation plus Title 15 §1103.5.4 scope. CBC-track Group R also uses §14.50.104/§903.6(1),(5). Other-than-R/U uses the conditional §903.6(2) test; addition triggers are separate.
- **Contact**: division phones and the counter address live in `../city-reference/references/contacts-hours.md`. Solid Waste / C&D is a separate line, (949) 464-6677

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Scope: Tear-off or Overlay?** | ❌ **fail** | If overlay: existing roof must have <=1 layer already (max 2 total). Cannot overlay over slate, clay, cement, or asbestos-cement tile. Cannot overlay if existing is water-soaked or deteriorated. If tear-off: all layers removed to deck. | CBC 1512.2, 1512.3; CRC R908.3 |
| 2 | **Fire Classification** | ❌ **fail** | All new roofing in California must be fire-retardant rated at minimum Class C (CBC 1505.1.2). If >50% of roof replaced in one year, entire roof must be minimum Class C. In Very High Fire Hazard Severity Zones (VHFHSZ), Class A is mandatory regardless of construction type. Materials must bear testing agency labels (ASTM E108 or UL 790). Minimum per construction type: Type IA/IB/IIA/IV/VA = Class B; Type IIB/IIIB/VB = Class C (Table 1505.1). | CBC 1505.1, 1505.1.2, Table 1505.1; CRC R902.1, R902.1.2 |
| 3 | **Wind Speed Zone** | ⚠️ **flag** | Determine wind speed zone for project location (typically 110-115 mph for most of California per ASCE 7-22/CBC 1609). Wind speed zone affects underlayment requirements and wind-resistance labeling. Verify roofing material wind resistance labeling per ASTM D7158 or ASTM D3161 (CRC R905.2.4/CBC 1504.2). | CBC 1609, 1504.2; CRC R905.2.4 |
| 4 | **Material-Slope Compatibility** | ❌ **fail** | Verify selected material is allowed at the stated roof slope. Each material has a minimum slope. Low slopes require additional underlayment. | CBC 1507.2-1507.13; CRC R905.2-R905.8 |
| 5 | **Tile Weight / Structural** | ⚠️ **flag** | If clay or concrete tile: verify weight (psf) is provided. If weight exceeds original roofing by >3 psf or original framing was not designed for tile, structural analysis may be required. Permit valid for materials <=6 lbs/SF on standard plans. | CBC 1607.13; CRC R301.1 |
| 6 | **ICC-ESR Product Approval** | ⚠️ **flag** | If tile: ICC-ES evaluation report number should be provided. This verifies the product meets code. Note the number -- validation is city staff's responsibility. | CBC 1507.3; CRC R905.3 |
| 11 | **Cool Roof Compliance** | ❌ **fail** | Low-slope (<=2:12): SRI >=75. Steep-slope (>2:12): SRI >=16. Commercial low-slope: aged reflectance >=0.63, emittance >=0.75. Residential steep-slope: aged reflectance >=0.20, emittance >=0.75. Heavy roofs >=25 lb/ft2 exempt. BIPV/solar thermal exempt. | Energy Code 150.2(b)1I |
| 16 | **Waste Diversion** | ❌ **fail** | Tear-off projects: 65% minimum nonhazardous waste diversion from landfill (CALGreen 5.408). Waste management plan required. | CALGreen 5.408 |
| 17 | **Contractor Licensing** | ❌ **fail** | C-39 (Roofing) or B (General Building) license required. C-43 (Sheet Metal) for metal roofing. Workers' compensation insurance required. | B&P Code 7028 |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 7 | **Sheathing** | On tear-off: all missing, rotten, termite-eaten, or damaged sheathing must be replaced. Min thickness 1/2". Nailing: 6" OC at perimeter, 12" OC in field. Gaps in spaced sheathing <=1/4" or per manufacturer. Shingles shall be fastened only to solidly sheathed decks. | CRC R803.1, R803.2, R905.2.1 |
| 8 | **Underlayment** | Required under all roof coverings. Type depends on wind zone and material. Low-slope (2:12-4:12) requires double underlayment for shingles. Fastening: 12" grid between side laps, 6" at side/end laps. Drip edge: over underlayment at eaves, under underlayment at rakes. | CBC 1507.1.1; CRC R905.1.1, Table R905.1.1(2), Table R905.1.1(3) |
| 9 | **Flashing** | Required at wall/roof intersections, slope changes, penetrations. Metal >=0.019" (26 gage galvanized). Step flashing: min 4" legs, 2" offset from shingle edge. Sub-flashing required behind step flashing at dormers. Counter-flashing at chimney/masonry. Soffit flashing at chimney cricket. Kickout flashing at eave/sidewall intersections. Crickets for penetrations >30" wide. Valley lining installed BEFORE roofing material. Drip edge fastener spacing 12" OC. Prime metal flashing before applying bituminous materials. Rusted/damaged flashings must be replaced. | CBC 1503.2, 1503.5, 1512.5; CRC R903.2, R905.2.8, R905.2.8.3 |
| 10 | **Roof Drainage** | Drains at low points unless designed to drain over edges. Overflow drains or scuppers required where parapets trap water (inlet 2" above low point). Scuppers: 3x drain size, min 4" opening height. Drainage must not discharge onto adjacent property. | CRC R903.4, R903.4.1; CBC 1503.4 |
| 12 | **Attic Ventilation** | Vented attics: cross ventilation required. NFA = area/150 (unbalanced) or area/300 (balanced with 40-50% upper vents + vapor barrier). 1" min clearance between insulation and sheathing at vents. Vaulted ceilings: each bay ventilated individually. | CRC R806.1, R806.2, R806.3 |
| 13 | **Insulation & Radiant Barrier** | Reroof may trigger insulation upgrade to min R-22 (residential). Radiant barrier required in CZ 2-15 when vented attic with 1" air gap. Commercial low-slope: R-14 continuous insulation in CZ 1-2, 4, 8-16. | Energy Code 150.0(A), 150.1(C)1-2 |
| 14 | **Smoke & CO Alarms** | Verified at final inspection. Working alarms required in each bedroom, outside sleeping areas, each story. CO alarms required where fuel-fired appliances or attached garage. Detectors >10 years old must be replaced. For reroof-only: hardwired/interconnected upgrade NOT required (exterior work exception). | CRC R310, R311 |
| 15 | **Gas Vent Terminations** | Gas vents must extend through roof flashing/jack and terminate with a listed cap. Type B/L: min 5 ft above draft hood. Height above roof follows the applicable termination conditions. Min 3 ft above a forced-air inlet within 10 ft. Single-wall clearance uses the applicable CMC Table 802.7.3.3 or CPC Table 509.7.3.4(1) row; Type B follows its listing/manufacturer. Pipe boots are coordinated with the reroof scope. | CMC 802.6.1, 802.6.2, Table 802.7.3.3; CPC 509.6.1, Table 509.7.3.4(1) |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/attic-ventilation.md` — Attic Ventilation Requirements
- `references/cool-roof-energy.md` — Cool Roof Energy Code Requirements
- `references/gas-vent-terminations.md` — Gas Vent Termination and Roof Penetration Requirements
- `references/insulation-energy.md` — Roof Insulation and Energy Code Requirements
- `references/reroof-overlay-rules.md` — Reroof Overlay and Tear-Off Rules
- `references/roof-covering-fire-class.md` — Roof Covering Fire Classification
- `references/roof-drainage.md` — Roof Drainage, Overflow Drains, and Scuppers
- `references/roof-materials-slope.md` — Roof Materials and Slope Requirements
- `references/sheathing-requirements.md` — Roof Sheathing Requirements
- `references/smoke-co-alarms.md` — Smoke and Carbon Monoxide Alarm Requirements
- `references/tile-structural.md` — Tile Weight and Structural Adequacy
- `references/waste-diversion.md` — Construction Waste Diversion Requirements

**Laguna Beach rules**

- `references/city-fire-amendments.md` — Laguna Beach Fire Code Amendments (Title 15)
- `references/city-roof-color-standards.md` — Laguna Beach — Roof Color, Finish, and Pre-Issuance Approval
- `references/city-wui-roofing.md` — Laguna Beach WUI Code — Fire-Resistive Construction Requirements

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
