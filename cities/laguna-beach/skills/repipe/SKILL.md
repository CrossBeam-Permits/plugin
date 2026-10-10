---
name: repipe
description: "Repipe permits in Laguna Beach, CA. Water supply piping replaced through an existing dwelling, with the wall and ceiling patches that follow. Laguna issues this on the state skill alone, with no city delta. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions repipe in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Plumbing Code (Title 24, Part 5) — Chapters 3, 6"
  authority: "California Building Standards Commission / Uniform Plumbing Code with California Amendments"
  law_as_of: "January 1, 2025"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Repipe Permit

Handles repipe permits in Laguna Beach end-to-end. Scope: Water supply piping replaced through an existing dwelling, with the wall and ceiling patches that follow. Laguna issues this on the state skill alone, with no city delta.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a repipe permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Repipe Permit

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

> Laguna Beach's local layer for this permit.

Laguna Beach has no local amendment for this permit; the City issues it on the California rules alone (verified in the City's code research). The California checklist below applies in full. The citywide overlays above still apply when the scope reaches them.

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **Pipe material approved?** | ❌ **fail** | Material is on CPC Table 604.1 approved list; polybutylene (PB) is NOT approved for new; PEX-AL-PEX not adopted for HCD 1 & 2 potable water | CPC 604.1, Table 604.1 |
| 2 | **NSF 61 & lead content?** | ❌ **fail** | All materials comply with NSF 61; max 0.25% weighted avg lead (drinking water); max 0.2% lead in solder/flux | CPC 604.1, 604.2, 604.2.1 |
| 3 | **Copper type adequate?** | ❌ **fail** | If copper: Type L minimum; Type M only aboveground; markings: K=green, L=blue, M=red | CPC 604.3, 604.4 |
| 4 | **Pipe sizing adequate?** | ❌ **fail** | Based on fixture count -> WSFU -> pipe size per pressure range and developed length | CPC 610.3, Table 610.3, Table 610.4 |
| 5 | **Building supply minimum?** | ❌ **fail** | Minimum 3/4" water service; 1/2" branch minimum; water heater manifold one size larger if fed from end | CPC 610.8, CRC P2903.7 |
| 6 | **Water pressure?** | ❌ **fail** | Min 15 psi at fixtures; PRV required if >80 psi; pipe sizing at 80% of regulated pressure | CPC 608.1, 608.2 |
| 7 | **Expansion tank?** | ❌ **fail** | Required downstream of PRV; also required where check valve or backflow preventer creates a closed system | CPC 608.2, 608.3 |
| 8 | **Valves correct?** | ❌ **fail** | Main fullway valve per building after meter (606.3); water heater fullway valve on cold supply; control valve at each fixture/appliance; all accessible. Multi-unit buildings: individual shutoff valves for each dwelling unit (CPC 606.3). | CPC 606.2, 606.3, 606.5, 606.6 |
| 17 | **Backflow prevention?** | ❌ **fail** | Hose bibbs need vacuum breaker; irrigation systems need AVB/PVB/SVB/RP; pool/spa makeup needs air gap or RP | CPC 603.5.7, 603.5.6, 603.5.21 |
| 19 | **PVC/PEX UV protection?** | ⚠️ **flag** | PVC: no direct sunlight (exception: max 24 in. with 0.04 in. UV tape); PEX: min 30-day UV protection per CPC | CPC 605.12, 605.9 |

---

## Deferred to Inspection

The inspector verifies these in the field. They are **not** plan-check corrections; the reviewer does not list them.

| # | Inspector verifies | What to look for | Code |
|---|---|---|---|
| 9 | **Unions near equipment?** | Within 12 in. of water heater, softeners, filters, regulators, similar equipment | CPC 609.5 |
| 10 | **Joint method correct?** | Solder per ASTM B828 (max 0.2% lead); CPVC one-step cements yellow or red (605.2.2); female threaded CPVC fittings with male plastic only (605.2.3); PVC threaded fittings minimum Schedule 80 (605.12.3); press-connect per mfr; push-fit per ASSE 1061; plastic-to-other-piping adapter fittings per 605.16.2 | CPC 605.1.4, 605.2.2, 605.2.3, 605.1.3.2, 605.9.3, 605.12.3, 605.16.2 |
| 11 | **Dissimilar metals?** | Dielectric unions/fittings at copper-to-galvanized connections; dissimilar metal connections at accessible locations only | CPC 605.15, 605.16.1, 310.6 |
| 12 | **Pipe protection?** | Steel nail plates (min 18 ga.) where pipes are within 1-1/4 in. of framing face; plates extend 1-1/2 in. beyond pipe OD; 2 in. above/below sole and top plates | CPC 312.9 |
| 13 | **Underground installation?** | Min 12 in. below grade; min 6 in. below frost line (CPC 609.1); tracer wire on plastic (#14 blue, CPC 604.10.1); common trench separation from sewer (12 in. above, 12 in. horizontal, CPC 609.2); no pipes within 45 deg. of footings (CPC 314.1). Backfill: smooth continuous bearing support; no rocks in first 12 in.; thin layers max 6 in. tamped; no heavy equipment until 12 in. of tamped earth over pipe (CPC 314.4, 314.4.1). Piping not directly embedded in concrete/masonry (CPC 312.2); protective sheath min 8 mil plastic for corrosive soil (CPC 312.3). Bored/drilled openings: sleeve not required but annular spaces sealed (CPC 312.10.2). | CPC 312.2, 312.3, 314.1, 314.4, 314.4.1, 604.10.1, 609.1, 609.2 |
| 14 | **Under-slab piping?** | Galvanized prohibited; copper joints brazed (not soldered) with wrought-copper fittings; Type L minimum; pressure tested before pouring | CPC 609.3, 604.3, 609.4 |
| 15 | **Hot water insulation?** | All hot water piping insulated; thickness >= pipe diameter (up to 2 in.), 2 in. for larger pipe | CPC 609.12.1, 609.12.2 |
| 16 | **Water hammer arrestors?** | Mechanical ASSE 1010 devices (not air chambers) near quick-close valves (dishwasher, clothes washer) | CPC 609.11 |
| 18 | **Pressure test?** | Test at working pressure or min 50 psi (air); hold 15 min with no leakage | CPC 609.4 |
| 20 | **General installation?** | Burred ends reamed; dead legs have flushing method; flex connectors accessible; no reuse of non-potable pipe; slip joints on exposed fixture supply only | CPC 609.1, 309.6, 604.5, 604.8, 605.14 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/backflow-prevention.md` — CPC Section 603 — Backflow Prevention (Cross-Connection Control)
- `references/hot-water-piping.md` — CPC Hot Water Piping, Insulation & General Installation
- `references/joints-connections.md` — CPC Section 605 — Joints and Connections
- `references/pipe-materials.md` — CPC Section 604 — Water Supply Pipe Materials
- `references/pipe-protection-underground.md` — CPC Pipe Protection & Underground Installation
- `references/pipe-sizing.md` — CPC Section 610 — Water Supply Pipe Sizing
- `references/valves.md` — CPC Section 606 — Valves
- `references/water-pressure.md` — CPC Section 608 — Water Pressure Requirements

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
