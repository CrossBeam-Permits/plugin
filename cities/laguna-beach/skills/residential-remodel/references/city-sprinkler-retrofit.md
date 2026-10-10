# Laguna Beach — Residential Sprinkler Retrofit (TWO triggers)

**This file is the single residential retrofit reference for Laguna Beach.** Every Laguna
residential permit skill points here. Do not restate the rule anywhere else.

## The rule in one line

An existing one- or two-family dwelling in Laguna Beach has **two independent retrofit
triggers**. **Either one firing requires the full retrofit.** Test both on every project.

| Trigger | Basis | Applies to | Test | Ordinance |
|---------|-------|-----------|------|-----------|
| **A. LBMC Ch. 14.52.030** (amends CRC R309.2) | **Valuation** | One- and two-family dwellings + garage attached (within 10 ft) | Cumulative value of additions, alterations and repairs in **any three-year period** exceeds **50%** of the valuation before the work | Ord. 1725, 12/18/2025 |
| **A1. LBMC Ch. 14.52.026** (amends CRC R309.1) | **Valuation** | Townhouses + attached garage; each townhouse is a separate building | Same 50% / three-year test | Ord. 1725, 12/18/2025 |
| **B. LBMC Title 15 §1103.5.4** (adds CFC Ch. 11 §1103.5.4) | **Scope** | ALL existing Group R fire areas | Alteration of ≥50% of the building (which, on one reading, must include work on ≥50% of the exterior; UNSETTLED, see Trigger B), OR addition of one or more stories | Ord. 1726, 12/18/2025 |

State law is silent on retrofits for ordinary additions and alterations, so both triggers are city overlay. The parent state skill
(the California Residential Remodel rules, which come from the CrossBeam connector (see "California Code Compliance" in `../SKILL.md`)) correctly identifies that California amended out the
IRC R313.2 retrofit, leaving an explicit state-level exemption: existing un-sprinklered SFRs are
NOT required to retrofit on additions or alterations under state code. (R313 in the 2025 CA CRC
is "ceiling height," not sprinklers.) Laguna fills that silence twice — once by valuation, once
by scope. One state rule is not silent and overrides both triggers: the ADU carve-out below.

---

## State ADU carve-out — applies to both triggers

State ADU law sets two limits that no city retrofit rule can override. Verbatim from
the City source document (not included in this plugin):

> *"(12) Accessory dwelling units shall not be required to provide fire sprinklers if they are
> not required for the primary residence. The construction of an accessory dwelling unit shall
> not trigger a requirement for fire sprinklers to be installed in the existing primary
> dwelling."* — Gov. Code § 66314(d)(12)

> *"(d) The installation of fire sprinklers shall not be required in an accessory dwelling unit
> or a junior accessory dwelling unit if sprinklers are not required for the primary residence.
> The construction of an accessory dwelling unit or a junior accessory dwelling unit shall not
> trigger a requirement for fire sprinklers to be installed in the existing multifamily
> dwelling."* — Gov. Code § 66323(d) (units approved under 66323, and every JADU)

Laguna's ADU ordinance says the same: sprinklers are required in an ADU "if sprinklers are
required in the primary residence", and the construction of an ADU "does not trigger a
requirement for fire sprinklers to be installed in the existing primary dwelling" (LBMC
25.17.010(f)(3)(A)-(B); `../../adu/SKILL.md`).

How to run it:

1. **The ADU's own work never fires a retrofit of the primary dwelling.** Leave the ADU's
   valuation out of Trigger A's three-year sum, and leave the ADU's scope out of Trigger B's
   prongs, including prong 3: an ADU built as a new story on or over the house is not an
   "addition of one or more stories" for this rule.
2. **The ADU itself needs sprinklers only if the primary residence requires them.** An existing
   house with no sprinklers, and no other work in the project that fires a trigger, does not
   require them, so the ADU needs none, attached, detached or converted. Ch. 14.52.030's
   new-dwelling mandate does not reach the ADU when the house is not required to have them.
3. **Other work on the primary dwelling in the same project is tested on its own.** A remodel or a
   non-ADU addition on the house still runs both triggers without the ADU's numbers. If that work
   fires a trigger, the house must be sprinklered, and from then on sprinklers are required for
   the primary residence, so the ADU's exemption under the first sentence no longer holds. Say so
   when the two pieces are filed together.
4. **What is an ADU** (versus a guest room or a second story of the house) is decided under the ADU
   skill (`load_skills('adu')`), not here.

---

## Three different 50% rules — do not merge them

Laguna has three separate rules that use the number 50. They measure different things and they
have different consequences. Confusing them produces a wrong correction.

| Rule | Measures | Decides | Where |
|------|----------|---------|-------|
| **Valuation 50%** | Dollars — cumulative permit valuation over any three-year period vs. pre-work valuation | Sprinkler retrofit (Trigger A) | Ch. 14.52.030 |
| **Scope 50%** | Physical scope — % of building altered, or % of exterior worked on | Sprinkler retrofit (Trigger B) | Title 15 §1103.5.4 |
| **LCP major-remodel 50%** | Demolition/alteration extent measured from the Jan 13, 1993 baseline | Design Review tier and CDP tier — **not** sprinklers | `city-major-remodel-methodology.md` |

The major-remodel determination is still the operational test for **prong 1** of Trigger B. It
is not the test for Trigger A, and it does not by itself decide the retrofit.

---

## Trigger A — Ch. 14.52.030 (valuation)

Verbatim from the City source document (not included in this plugin)
§14.52.030, "Amendment to Subsection R309.2 of the California Residential Code"
(Ord. 1536 §2, 2010; Ord. 1581 §2, 2013; Ord. 1620 §2, 2016; Ord. 1641 §2, 2019; Ord. 1681 §2,
2023; **Ord. 1725, 12/18/2025**):

> *"**R309.2 One- and two-family dwellings automatic sprinkler systems.** An automatic
> residential fire sprinkler system shall be installed in one- and two-family dwellings and
> garages attached to one- and two-family dwellings. A garage is considered attached for the
> purposes of this subsection if it is within ten feet of the one- or two-family dwelling. If
> the cumulative value of additions, alterations and repairs done to a one- or two-family
> dwelling and attached garage in any three-year period exceeds fifty percent of the valuation
> of the one- or two-family dwelling and attached garage prior to the additions, alterations,
> and repairs, the entire one- or two-family dwelling and attached garage must be sprinklered
> throughout. The valuation used for the existing building and for the additions, alterations,
> and repairs is the valuation established in the City's resolution for computation of building
> permit fees. For the purposes of this subsection, firewalls, fire barriers, or fire partitions
> shall not define separate buildings or fire areas."*

One section carries two duties. It mandates sprinklers in **new** one- and two-family dwellings
and attached garages, **and** it imposes the valuation retrofit on existing ones. Citing it for
the retrofit is correct.

### How to run Trigger A

| Rule | Detail |
|------|--------|
| **Threshold** | Cumulative value > 50% of the pre-work valuation of the dwelling **plus** attached garage |
| **Rolling period** | Any three-year period. Not a calendar year. Prior permits inside the window count. |
| **Valuation method** | The valuation established in the **City's resolution for computation of building permit fees** — for both the existing building and the work. Not an appraisal, not the construction contract price, not assessed value. |
| **What counts** | ALL additions, alterations and repairs — including prior permits within the three-year window |
| **Attached garage** | A garage within **10 feet** of the dwelling is "attached." It counts in the valuation and it must be sprinklered. |
| **Separate buildings** | Firewalls, fire barriers and fire partitions do NOT define separate buildings or fire areas here. |
| **Scope of the retrofit** | The ENTIRE dwelling and attached garage, not the remodeled area. |

### Townhouses — Ch. 14.52.026 (CRC R309.1)

The identical 50% / three-year valuation rule applies to townhouses and their attached garages.
One difference: each townhouse with its attached garage is a **separate building** for the
calculation.

### Worked example

A kitchen remodel in Laguna Beach can run $80,000–$200,000. If the home's pre-work valuation
per the City fee resolution is $400,000, a $200,000 remodel alone reaches the 50% threshold. If
the owner also permitted a bathroom remodel the prior year, both valuations are summed. Trigger
A can fire on a project that alters well under 50% of the building — that is exactly why Trigger
B does not replace it.

---

## Trigger B — Title 15 §1103.5.4 (scope)

Verbatim from the City source document (not included in this plugin), Section
15.01.040, "Amendment to Chapter 11 of the Fire Code" (Ord. 1640 §1, 2019; Ord. 1682 §1, 2023;
**Ord. 1726, 12/18/2025**):

> *"Section 1103.5.4 is hereby added as follows:*
>
> ***Section 1103.5.4 Group R.** An automatic sprinkler system installed in accordance with Section 903.3 shall be provided throughout all existing Group R fire areas when work requiring a building permit that involves alteration of 50 percent or more of a building, which includes or involves work on 50 percent or more of the building's exterior, or which involves the addition of one or more stories.*
>
> ***Exception:** Work that consists only of the installation of fire-resistant siding."*

Trigger B reaches **all** Group R fire areas, not only one- and two-family dwellings. It is the
Fire Code scope trigger for existing multi-family (R-2 / 3+ units). Multi-family must also be
checked under **LBMC §14.50.104 / CBC §903.6**, whose clauses expressly include Group R: a
50%-valuation trigger and a separate substantial-renovation determination by the Building
Official. Ch. 14.52.030 covers only one- and two-family dwellings and Ch. 14.52.026 covers only
townhouses.

---

### Trigger B: two readings of the exterior clause (UNSETTLED)

The enacted sentence is: "alteration of 50 percent or more of a building, which includes or involves work on 50 percent or more of the building's exterior, or which involves the addition of one or more stories."

- **Reading 1 (one compound prong):** "which includes or involves work on 50 percent or more of the building's exterior" describes the alteration of 50% of the building. Trigger B then has two prongs: (1) an alteration of 50% or more of the building that also reaches 50% or more of the exterior, and (2) the addition of a story. Exterior-only work under 50% of the building does not trigger it.
- **Reading 2 (three independent prongs):** the exterior clause stands alone, so work on 50% or more of the exterior triggers sprinklers by itself.

The grammar (a "which" clause modifying "alteration", followed by a parallel "or which" clause) favors Reading 1; the fire-resistant-siding exception, which only makes sense if exterior-only work could trigger the rule, favors Reading 2. The City has not ruled. When the exterior prong is what decides the answer, give both readings, do not say sprinklers are "very likely", and say "confirm with Building and Fire at pre-application." The prong descriptions below follow Reading 2 so that both tests are run; report prong 2 alone as UNSETTLED.

Under Reading 2, Trigger B fires when work requiring a building permit involves **any** of the following:

#### Prong 1 — Alteration of 50% or More of a Building

Use the Step B major-remodel methodology (`city-major-remodel-methodology.md`) as the operational test. The "50% of a building" prong tracks the major-remodel determination, with the same dual coastal zone appealable vs coastal zone non-appealable methodology (October 2026 handout: walls counted on each floor, each structure tested independently) and the same Jan 13, 1993 cumulative baseline. When Step B classifies the project as a major remodel, prong 1 fires.

#### Prong 2 — Work on 50% or More of the Building's Exterior

Under Reading 2 this is **independent** of the major-remodel determination (UNSETTLED; see above). It catches projects whose scope is concentrated on the building exterior (reroof + reside + fenestration replacement) but that may not hit 50% of the whole-building methodology.

Operational test: aggregate the exterior square footage of:
- Reroof scope (sq ft)
- Re-side scope (sq ft of exterior wall cladding being replaced)
- Window/door replacement scope (sq ft of exterior wall opening being modified — note: same-opening change-outs do not count toward Step B major-remodel demolition, but for §1103.5.4 prong 2 they count toward the exterior work tally because the cladding around them is necessarily disturbed)
- Any other exterior work (deck, porch, etc.)

Compare to total exterior surface area (roof + exterior walls). If ≥50%, prong 2 fires.

#### Prong 3 — Addition of One or More Stories

Geometric, not %-based. If the scope adds a story (upper-level addition, second-story addition, vertical expansion), prong 3 fires regardless of demolition or exterior percentages.

**Exception for ADU stories (state law).** A story that is an ADU or JADU does not fire prong 3:
"The construction of an accessory dwelling unit shall not trigger a requirement for fire
sprinklers to be installed in the existing primary dwelling" (Gov. Code § 66314(d)(12); § 66323(d)).
See "State ADU carve-out" above. A story added to the house itself, in the same project, still
fires it.

**Does a basement or lower level count as an "added story"? (UNSETTLED)**

Title 15 does not define "story", so the CFC Chapter 2 definitions apply (2025 CFC §202, same as CBC §202):

> *"STORY. That portion of a building included between the upper surface of a floor and the upper surface of the floor or roof next above (see "Basement," "Building height," "Grade plane" and "Mezzanine")."*
>
> *"BASEMENT. A story that is not a story above grade plane."*

- By these definitions a basement **is** a story, and §1103.5.4 says "addition of one or more stories", not "stories above grade plane". So on the plain text, a new basement or a new lower level (for example a level dug out under a hillside house) reads as an added story.
- A new level that is a "story above grade plane" under §202 (common on a downslope lot) is an added story on any reading.
- A mezzanine that complies with CBC §505.2 "shall be considered a portion of the story below", so it is not an added story.
- The City has not ruled on whether excavating a basement or lower level under an existing house fires prong 3. Report it as **UNSETTLED; confirm with Building and Fire at pre-application**. Give the plain-text reading (it fires) and say the City has not confirmed it. Trigger A (valuation) still applies either way, and a basement often pushes it past 50%.

---

### Trigger B exception (the only one) — fire-resistant siding only

> *"Exception: Work that consists only of the installation of fire-resistant siding."*

Narrow exception, and it belongs to Trigger B only. **It does not exempt a project from Trigger A** — a large re-side can still push the three-year cumulative valuation past 50%. Two key constraints:
- "Consists only of" — the scope must be entirely fire-resistant siding installation. Add any other scope (window replacement, structural work, etc.) and the exception is lost.
- "Fire-resistant siding" — installation of fire-rated cladding to comply with VHFHSZ Ch. 7A or LBMC §14.70.030 (noncombustible/ignition-resistant exterior wall coverings). This recognizes that a city-mandated fire-hardening upgrade should not itself trigger a sprinkler retrofit.

For any other scope mix, the exception does not apply.

---

## Common Misattributions — DO NOT Cite These for the Retrofit Trigger

### Do not substitute CBC §903.6 for the CRC rule on a house

CBC §903.6, as amended by **LBMC §14.50.104**, is not non-residential-only: clauses (1) and
(5) expressly cover Group R. It is the correct additional retrofit framework for CBC-track
multi-family buildings. For a CRC-track one- or two-family dwelling or townhouse, cite the
more specific Ch. 14.52.030 or Ch. 14.52.026 valuation rule instead. For commercial work,
§903.6(2) requires both a post-work sprinklers-required finding and the valuation threshold;
do not quote the 50% number without that condition.

### Wrong: CRC R313 (ceiling height in 2025 CA CRC)

R313 in 2025 CA CRC is **ceiling height**, not sprinklers. The state's sprinkler-retrofit silence lives in CRC §R309.2 Exception 1 (with the city overlay filling the silence). Do not import IRC R313.2 numbering — that's the IRC framework California amended out.

---

## When either trigger fires — system stack

The system stack is the same whichever trigger fired. When the retrofit trigger fires, the system must be installed "in accordance with Section 903.3" (CFC §903.3). Group R retrofits in Laguna use NFPA 13D for SFRs/duplexes/townhouses, NFPA 13R for low-rise multi-family, or NFPA 13 for higher-density. Laguna has extensive amendments to NFPA 13D and 13R per Title 15 §15.01.070 (Ord. 1726, 12/18/2025) — relevant retrofit considerations:

### Design method — NFPA 13D is mandatory (Ch. 14.52.031 and .032)

> *"**R309.3 Dwelling unit fire sprinkler systems.** Where installed, residential fire sprinkler systems, or portions thereof, shall be in accordance with the most current NFPA 13D standard for design and calculation. All residential fire sprinkler systems shall have a flow switch installed that activates an electric exterior alarm. The residential fire sprinkler flow switch shall also activate all interconnected interior smoke detectors."* — Ch. 14.52.031 (CRC R309.3 as amended, Ord. 1725, 12/18/2025)

Ch. 14.52.032 **deletes CRC R309.3.1 through R309.3.8.2 in their entirety**. The CRC
prescriptive sprinkler design method is therefore not available in Laguna Beach. Every such
system is engineered to NFPA 13D. Title 15 §15.01.070 requires supervision when an NFPA 13D
system has a separate control valve; its blanket 24-hour UL-certified central-station mandate
is in the NFPA 13R amendment and does not apply to every NFPA 13D system.

### NFPA 13D Amendments (SFR / 1- and 2-family)

| Section | Requirement |
|---------|-------------|
| §4.1.3 | Stock of spare sprinklers — minimum 2 for each type, in temperature-controlled cabinet, with sprinkler wrench |
| §7.1.2 | Piping system shall not have a separate control valve unless supervised by a central station, proprietary, or remote station alarm service |
| §7.3.1 | At least one water pressure gauge on the riser assembly |
| §7.6 | Exterior alarm — listed for outside service, audible and visible from the street from which the house is addressed; on front or side of structure, location subject to fire code official approval |
| §7.6.1 | Additional interior alarm devices for audibility throughout structure; sleeping-area sound levels min 15 dBA above ambient OR ≥75 dBA; uninterruptible-circuit power |
| §8.3.4 | Sprinklers required in ALL attached garages, attached carports, open attached porches, AND all detached garages and carports within 30 feet of the dwelling |
| §8.3.5.1 | Sprinklers required in attics with storage, penthouse equipment rooms, elevator machine rooms, concealed spaces dedicated to ventilation equipment, accessible floor/ceiling spaces, top of elevator shafts, accessible crawl spaces, other accessible concealed spaces |
| §8.3.5.2 | All attics — intermediate-temperature quick-response sprinkler at attic penetrations from access scuttles or mechanical equipment |
| §8.3.5.3 | All exterior overhangs ≥48" — sprinkler coverage required |

### NFPA 13R Amendments (low-rise multi-family)

| Section | Requirement |
|---------|-------------|
| §6.16.1 | NFPA 72 fire alarm system with **24-hour UL-certified central station monitoring** required on all sprinkler systems; connected to building fire alarm or water-flow monitoring system; min one exterior alarm indicating device, listed for outside service, audible and visible from access roadway |
| §6.16.1.1 | Additional interior alarm devices throughout — sleeping-area sound levels per same standard as 13D §7.6.1 |

### Interaction with Step E (Bluff Overlay)

A retrofit-triggered SFR on the coastal bluff still has the §25.50.004(B)(4) 25-ft setback. The retrofit installation (riser, FDC, exterior alarm) must respect both setback and bluff geometry; FDC location is "subject to final approval by the fire code official."

---

## Diff Discipline — both source files

Both ordinance files were scraped 2026-03-13 and both are current.

| Source file | Section | Last amended |
|-------------|---------|--------------|
| the City source document (not included in this plugin) | §14.52.030 (R309.2), §14.52.026 (R309.1), §14.52.031 (R309.3), §14.52.032 | Ord. 1725, 12/18/2025 |
| the City source document (not included in this plugin) | §15.01.040 (adds §1103.5.4) | Ord. 1726, 12/18/2025 |

Ord. 1725 and Ord. 1726 were adopted the same day, 12/18/2025, for the 2026 code cycle. Both
triggers are current. If a future pass finds only one of them, that pass is incomplete — check
the other file before rewriting this one.

---

## Output Format

```
## Sprinkler Retrofit — LBMC Ch. 14.52.030 and Title 15 §1103.5.4
**Result:** REQUIRED | NOT REQUIRED | EXEMPTION APPLIES
**Trigger A — Ch. 14.52.030 (valuation, Ord. 1725 12/18/2025):** FIRED | NOT FIRED | CANNOT DETERMINE
  - Pre-work valuation of dwelling + attached garage (City fee resolution): $____
  - Cumulative value of additions/alterations/repairs in the three-year period: $____
  - Ratio vs. 50%: ____%
  - If the documents do not state a valuation, report CANNOT DETERMINE and request it. Do not assume.
**Trigger B — Title 15 §1103.5.4 (scope, Ord. 1726 12/18/2025):** FIRED | NOT FIRED
  - Prong 1 (alteration ≥50% of building per Step B methodology): YES | NO
  - Prong 2 (work ≥50% of exterior): YES | NO — if prong 2 alone fires, report UNSETTLED (Reading 1 vs Reading 2) and "confirm with Building and Fire at pre-application"
  - Prong 3 (added story): YES | NO — a new basement or lower level alone: report UNSETTLED (plain text says yes; City has not ruled). A story that is an ADU or JADU: NO (Gov. Code § 66314(d)(12))
  - Exception ("work that consists only of the installation of fire-resistant siding"): YES | NO
**State ADU carve-out (Gov. Code § 66314(d)(12); § 66323(d)):** APPLIES | N/A — the ADU's work is left out of both triggers; the ADU needs sprinklers only if the primary residence requires them
**Either trigger firing requires the retrofit. Report which one(s) fired.**
**Citations:**
  - Ch. 14.52.030: "If the cumulative value of additions, alterations and repairs done to a one- or two-family dwelling and attached garage in any three-year period exceeds fifty percent of the valuation of the one- or two-family dwelling and attached garage prior to the additions, alterations, and repairs, the entire one- or two-family dwelling and attached garage must be sprinklered throughout."
  - Title 15 §1103.5.4: "An automatic sprinkler system installed in accordance with Section 903.3 shall be provided throughout all existing Group R fire areas when work requiring a building permit that involves alteration of 50 percent or more of a building, which includes or involves work on 50 percent or more of the building's exterior, or which involves the addition of one or more stories."
  - Gov. Code § 66314(d)(12), when an ADU is in the project: "Accessory dwelling units shall not be required to provide fire sprinklers if they are not required for the primary residence. The construction of an accessory dwelling unit shall not trigger a requirement for fire sprinklers to be installed in the existing primary dwelling."
**Action required:** [If REQUIRED: full sprinkler retrofit of the ENTIRE dwelling and attached garage per NFPA 13D (SFR) or 13R (multi-family) with city amendments per Title 15 §15.01.070 — attached + detached-within-30-ft garages, attic protection, exterior overhangs ≥48", exterior alarm + interior ≥75 dBA, 24-hr UL central station monitoring (13R). NFPA 13D design is mandatory; the CRC prescriptive method is deleted (Ch. 14.52.032). Cover sheet shall be notated "FIRE SPRINKLERS REQUIRED" per Building Plan Check Submittal Requirements page 4. The project is no longer OTC-eligible — full plan review.]
```
