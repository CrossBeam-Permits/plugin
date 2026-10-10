---
name: solar
description: "Solar PV permits in Laguna Beach, CA. Rooftop or ground-mount PV, battery storage, and the service work that ties them in, including SolarAPP+ approvals and remove-and-reinstall of an existing array. Works in two modes: (A) BUILDER/HOMEOWNER — scopes the project, checks it against California code and Laguna Beach rules, and prepares a portal-ready submission; (B) CITY REVIEWER — runs the plan-check checklist on a submittal and produces tight corrections output. Use when the user mentions solar in Laguna Beach."
metadata:
  version: "2.0"
  source: "2025 California Electrical Code (Title 24, Part 3) -- Articles 690, 705, 250, 310; 2025 California Fire Code (Title 24, Part 9) -- Chapter 12; 2025 California Residential Code (Title 24, Part 2.5) -- Section R329"
  authority: "California Building Standards Commission and City of Laguna Beach"
  law_as_of: "January 1, 2025"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — Solar PV Permit

Handles solar pv permits in Laguna Beach end-to-end. Scope: Rooftop or ground-mount PV, battery storage, and the service work that ties them in, including SolarAPP+ approvals and remove-and-reinstall of an existing array.

**Choose the mode from the request.** A request to plan or file a project selects Builder/Homeowner. Ask only when the role is unclear:

> "Are you (A) planning to file a solar pv permit, or (B) a city reviewer checking a submitted one?"

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
## Ready to Submit — Laguna Beach Solar PV Permit

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

---

### Decision Tree Router

| Topic | Load These References |
|-------|----------------------|
| **Residential rooftop solar permit** | `references/city-solar-ordinance.md` + state skill |
| **Permit timeline / process** | This SKILL.md |
| **Fees** | Fee tool (`estimate_fees`, Master Fee Schedule). §14.84.060 sets only the cap |
| **Which filing (SolarAPP+ or plan review)?** | "Filing Paths" below |
| **Commercial or multifamily solar** | Not Ch. 14.84. Building plan review only; see "Planning Route" and "Non-Residential Storage" below + state skill |
| **Planning approval?** | "Planning Route" below |
| **CDP / Three Arch Bay** | "Coastal zone" row below |

---

### Eligibility for Expedited Review

ALL four conditions must be met:
1. **≤10 kW AC nameplate** or ≤30 kW thermal
2. Conforms to all applicable codes as adopted by Laguna Beach
3. Installed on **single- or duplex-family dwelling**
4. Does not exceed maximum legal building height

If eligible AND meets city's checklist/standard plan → **3 business day permit**.

---

### Filing Paths

The City takes solar two ways. Name both and pick by the system.

| Path | When | Evidence |
|---|---|---|
| **SolarAPP+ first, then EnerGov type 124** | The installer gets SolarAPP+ approval for the system. Type 124 carries the SolarAPP+ approval and spec sheets, not a plan set. The permit issues on submittal. SolarAPP+ eligibility is set by SolarAPP+, not by the 10 kW Ch. 14.84 test | City records: rooftop PV with battery storage applied for and issued the same day (Sept. 2026) |
| **Standard plan review ("Residential - Solar" e-plan filing)** | The system is not run through SolarAPP+ (for example it falls outside SolarAPP+ scope, or the installer does not use it). Plans go through ordinary plan check | City records: a 16.2 kW rooftop PV system with 30 kWh of battery storage, filed as "Residential - Solar", work class Solar, with the reroof and skylight on a separate permit |

**An open plan-review filing does not lock the system out of SolarAPP+.** The two paths are alternatives for the same system. If a "Residential - Solar" plan-review filing is open and the system fits SolarAPP+ scope, say the installer may run it through SolarAPP+ and file type 124 instead, and should ask the Building Division in writing to withdraw or void the plan-review filing so two permits are not open for one system. Whether any fee paid on the first filing is refunded is the City's call (not in our sources).

**What rides on type 124, and what does not.** The City's type 124 form says, verbatim: "Separate permits are required for the following items: Generators, Ground-mounted PV systems, Service upgrades not within SolarAPP scope, Main panel upgrades, New service meter installations, Reroofs as part of solar install." Apply it this way:
- Generators, ground-mounted PV, new meters and a reroof: always a separate permit.
- A backup or critical-loads subpanel, a battery and other equipment inside the SolarAPP+ approval: not on the list, so they ride on type 124.
- A main panel upgrade: the form lists it as separate, but City practice differs. Four Laguna SolarAPP+ permits marked "Main Panel Upgrade: Yes" issued with no separate electrical permit. Give the form's rule, then the practice: include the upgrade in the SolarAPP+ application, and file a separate electrical permit if the City asks for one. Do not state either one as the only answer.
- A service upgrade outside SolarAPP+ scope: separate (the form).

A system over 10 kW AC is not a Ch. 14.84 expedited system, so the 3-business-day clock does not apply to it; it can still use SolarAPP+ if SolarAPP+ accepts it.

---

### Permit Review Checklist

| # | Check | What to Verify |
|---|-------|---------------|
| 1 | System eligible? | ≤10 kW AC, single/duplex dwelling, within height limit |
| 2 | Meets checklist? | City's standard plan/checklist requirements |
| 3 | State code compliance? | CEC, fire, structural per state solar skill |
| 4 | Health/safety only? | Review limited to health/safety — no aesthetic review for qualifying systems |
| 5 | Fee paid? | Amount from the fee tool, not from memory. §14.84.060 caps the building permit fee at 10% of system cost and "in no case more than one thousand dollars", and requires conformity with Gov. Code 65850.55 and 66015. Fee may be waived upon WRITTEN DETERMINATION by the Director of Community Development that the system results in no significant aesthetic or view impacts (§14.84.060). This is not automatic. |
| 6 | HOA not blocking? | City cannot condition on HOA approval |

---

### Key Laguna Beach Solar Facts

| Parameter | Value |
|-----------|-------|
| **Ordinance** | Ch. 14.84 (Ord. 1607, 2015) |
| **Permit type** | Administrative, nondiscretionary |
| **Expedited timeline** | **3 business days** |
| **Fee** | Look up in the fee tool. Code cap: 10% of system cost, never over $1,000 (§14.84.060) |
| **Fee waiver** | Requires WRITTEN DETERMINATION by Director of Community Development (§14.84.060) — not automatic |
| **Inspections** | **1 only** (expedited-eligible) |
| **Inspection scheduling** | Within **2 business days** of request |
| **Electronic submittal** | Available (email/web/fax) |
| **Board of appeals** | Planning Commission |
| **HOA override** | Cannot condition on HOA approval |
| **Maintenance/like-kind** | No permit required |
| **Re-inspection** | If system fails initial inspection, subsequent inspection is authorized but not bound by expedited timeline (§14.84.070(i)) |
| **Coastal zone, single-family house** | LBMC §25.07.008(A)(1) exempts improvements to single-family dwellings from a CDP unless an (A)(1) exception applies (for rooftop PV: (b) on a beach, in a wetland or stream, within 50 ft of a bluff edge, in an ESA or highly scenic area; (f) the original CDP required permits for future improvements). Rooftop panels add no floor area and no height. The City record shows no CDP exemption for rooftop PV, including on streets next to the ocean. Planning does not review it (Building Division, 2026-09-01). |
| **Coastal zone, duplex, multifamily, commercial and public buildings** | Rooftop PV and its paired storage on an existing building are an improvement to an existing structure: exempt from a CDP (PRC 30610(b); LBMC §25.07.008(A)(2)) unless the work changes the intensity of use or falls in a listed sensitive spot ((A)(2)(a)-(d)). **Cost never makes it a CDP:** a "major energy facility" excludes development "governed by the provisions of Public Resources Code Section 30610" (§25.07.006). The (A)(2) exemption does not cover a "public works facility" as §25.07.006 defines it (public-agency or PUC utility facilities, public transportation facilities, publicly financed recreational facilities, special-district development): a fire station, City hall or library is not one; on a park building or a water or sanitation district facility, ask Planning for the exemption determination (§25.07.012(B)). Guide detail: a CrossBeam reference that is not included in this plugin Step 3 |
| **Three Arch Bay (and other areas of deferred certification)** | The City's CDP exemption does not apply. Three Arch Bay, Blue Lagoon and Irvine Cove stay under Coastal Commission CDP jurisdiction (City LCP page; Commission LCP status chart; `../coastal-development/SKILL.md`). The Coastal Commission, not the City, decides whether the work is exempt or needs a CDP. Tell the applicant to get the Commission's exemption or CDP, and the Three Arch Bay association's review, before the City issues the building permit. Use the parcel's coastal flag; do not assume |

---

### Planning Route (Ord. 1732, LBMC 25.05.040(B))

**Lead line, any building: "Building only (state law), unless the same job reroofs or adds exterior
equipment."** Gov. Code 65850.5(b) requires approval "through the issuance of a building permit or
similar nondiscretionary permit", for homes, businesses and public buildings alike. The same-job
extras run the lists on their own: a reroof is Zone Clearance (B)(2)(e) like for like, ADR
(B)(3)(a)(ix) for a white, light or glare-prone roof and (x) for a change in dimensions, area or
pitch; a new carport, shed or enclosure built to hold the system runs the catch-alls. The battery
cabinets themselves, indoors or out, are part of the solar energy system and run no list item. Say
it in one line; do not branch.
- **Batteries installed with the panels as their storage are solar storage, whatever their size.**
  A "solar energy system" includes storage of solar energy (Gov. Code 65850.5(j)(4); Civil Code
  801.5(a)(1)), and the statute sets no ratio of battery kWh to panel kW. Never test one.
- **City capital-project tiers never apply** ((B)(1)(p), (B)(3)(a)(xvii), (B)(2)(bb)): solar and its
  storage on a City or other public building is still a building permit under 65850.5(b), whatever
  it costs.
- **Fire code review of the storage** (CFC 1207, or CRC R330 on a house) is a Building and Fire item
  in plan check, not a Planning step ("Non-Residential Storage" below).

| Scope | Planning |
|---|---|
| Rooftop PV on a single-family home or duplex (Ch. 14.84 system) | None. Building Division administrative, nondiscretionary review only (§14.84.070); review is limited to health and safety. No Planning record exists for rooftop PV in the City permit data (a CrossBeam reference that is not included in this plugin Step 1) |
| Reroof done with the PV | Planning applies to the reroof: Zone Clearance (B)(2)(e) if same shape and not white/light/glare; ADR (B)(3)(a)(ix)-(x) otherwise. Load `reroof` |
| Ground-mounted array | Not a Ch. 14.84 rooftop system, but still a solar energy system: Gov. Code 65850.5(b) requires administrative approval through a building permit or similar nondiscretionary permit, so no Design Review of the array. Objective setbacks and height still apply. Whether the City checks them with a Zone Clearance ((B)(2)(b), 15 ft or less) is **UNSETTLED; confirm with Planning at pre-application** |
| Carport or trellis that holds PV | The panels are a solar energy system (Gov. Code 65850.5(b)). Whether the carport or trellis structure itself is reviewed under the closed lists (Zone Clearance (B)(2)(b) if 15 ft or less; Design Review (B)(1)(c) if over 15 ft; "new building" (B)(1)(b)) is **UNSETTLED; confirm with Planning at pre-application** |
| Battery storage that is part of a rooftop PV system on a house or duplex, indoors or on an outside wall | No discretionary Planning review: it is part of the solar energy system (Gov. Code 65850.5(b)), so no Design Review, ADR or CDP step comes from the lists. City practice: rooftop PV with a battery has issued through SolarAPP+ with no Planning record, and no Planning record names PV or its equipment in 403 City solar permits (2020-10 to 2026-09). If the counter asks for a zoning sign-off, it is a same-day zoning plan check stamp, not a review tier |
| Battery storage not tied to a PV system (standalone), or a generator outside | **UNSETTLED.** LBMC 7.25.130 names only "HVAC and pool/spa equipment", so its six-part test does not by its terms reach a battery or generator. The lists' equipment items read "Mechanical equipment, including air conditioners and pool/spa equipment, that meets [or does not meet] Section 7.25.130(C)" ((B)(2)(v), (B)(3)(a)(v)); whether a battery is "mechanical equipment" is not decided. The other candidate is the utility-structure pair by height: under 4 ft (B)(2)(w) Zone Clearance, 4 ft or more (B)(3)(a)(xiv) ADR. Give both and confirm with Planning at pre-application (a CrossBeam reference that is not included in this plugin, generators). Load `hvac` for the noise test |
| Commercial, mixed-use, multifamily or public (City, school, fire station) PV, and battery storage that is part of it, any size | None. Gov. Code 65850.5(b): "A city or county shall administratively approve applications to install solar energy systems through the issuance of a building permit or similar nondiscretionary permit." The duty is not limited to houses, and a solar energy system includes storage of solar energy (Civil Code 801.5(a)(1)). It is not a Ch. 14.84 expedited system, so it gets ordinary Building plan review. A use permit is allowed only on the building official's good-faith finding of a specific, adverse impact on public health and safety (65850.5(b); LBMC 14.84.070 for houses). A reroof, new structure or standalone equipment in the same job follows its own route |

The Director may refer any Zone Clearance or ADR item up (25.05.040(A)(2)(d)). A CDP is a separate Ch. 25.07 question (see the Coastal zone and Three Arch Bay rows above).

---

### Non-Residential Storage (city delta only)

Battery storage on a commercial, mixed-use or multifamily building is reviewed under CFC 1207 (permit and construction documents 1207.1.4-1207.1.5, size and separation 1207.5.1, indoor and outdoor locations 1207.7-1207.8, rooftop 1207.9 and 1207.9.5), not CRC R330. Rooftop PV on a building other than Group R-3 uses the CFC 1205.3 perimeter and interior pathways. Apply them from the state skill and the code; do not restate them here.

The Laguna delta:
- Laguna does not amend CFC Chapter 12. LBMC 15.01 amends Fire Code Chapters 1, 2, 3, 9, 11, 50, 56, 57, 61 and 80 only (LBMC 15.01.020-15.01.070).
- The fire code official is the Laguna Beach Fire Department, not OCFA (`../city-reference/SKILL.md`). Route a CFC 1207 storage system to Fire review with the Building permit.

---

### Laguna Beach vs. Other Cities

| Aspect | Buena Park | Costa Mesa | Laguna Beach |
|--------|-----------|-----------|-------------|
| **Process** | Symbium (SB 379) | SolarAPP+ via TESSA | SolarAPP+ → EnerGov type 124, or a "Residential - Solar" plan-review filing; expedited Ch. 14.84 |
| **Timeline** | Instant (automated) | Instant (automated) | SolarAPP+: issued on submittal. Ch. 14.84 expedited: **3 business days** |
| **Inspections** | 1 | 1 | **1** |
| **Fee cap in code** | Varies | Varies | 10% of cost, max $1,000 (actual fee: fee tool) |
| **Electronic submit** | Yes | Yes | Yes |

---

## California Plan-Check Checklist (applies to both modes)

Every item here is verified at plan-check time, after the Laguna Beach rules above. Severity drives reviewer-mode output. The full state text is in `references/california-baseline.md`.

| # | Check | Severity | What to verify | Code |
|---|---|---|---|---|
| 1 | **System type identified?** | ❌ **fail** | Microinverter, AC module, or string inverter; number of modules, branches, total AC power rating | CEC 690.1, 690.2, 690.6 |
| 2 | **Equipment listed?** | ❌ **fail** | Modules listed per UL 1703 or UL 61730; inverters listed per UL 1741; mounting per UL 2703 | CEC 690.4(B), CRC R329.3.1 |
| 3 | **Max DC voltage correct?** | ❌ **fail** | Voc x temperature correction factor (Table 690.7(A)) does not exceed 600V for 1- and 2-family dwellings | CEC 690.7, 690.7(A) |
| 4 | **Circuit sizing correct?** | ❌ **fail** | Branch circuit conductors sized at 125% of max current; OCPD rated per 690.9(B); conduit sized for conductor fill | CEC 690.8, 690.9, 310.16 |
| 5 | **Ambient temperature correction applied?** | ❌ **fail** | Rooftop conductors derated for elevated temps (22C adder for rooftop, Table 690.31(A) correction factors) | CEC 690.31(A), Table 310.16 |
| 6 | **Arc-fault protection?** | ❌ **fail** | AFCI required for DC circuits >=80V; exception for metal raceways/MC cable not on buildings | CEC 690.11 |
| 7 | **Rapid shutdown compliant?** | ❌ **fail** | Outside array boundary: <=30V within 30 sec; inside array boundary: PVHCS listed per UL 3741 or <=80V within 30 sec; initiation device at readily accessible outdoor location | CEC 690.12 |
| 8 | **Fire setbacks met?** | ❌ **fail** | Ridge setback (18" or 36" depending on array coverage); 36" pathways; hip/valley clearances; emergency escape openings clear | CFC 1205.2, CRC R329.6 |
| 9 | **DC conductor routing correct?** | ❌ **fail** | DC circuits inside buildings in metal raceways or MC cable; labeled every 10 ft; rooftop conduit minimizes trip hazards | CEC 690.31(D), CFC 1205.2.4 |
| 10 | **Interconnection method valid?** | ❌ **fail** | Load-side: 120% busbar rule (705.12(B)(2)); supply-side: utility-approved adapter or listed service equipment | CEC 705.12, 705.11 |
| 11 | **Busbar capacity adequate?** | ❌ **fail** | Combined inverter OCPD + main OCPD <= busbar rating x (100% or 120% depending on position) | CEC 705.12(B) |
| 12 | **Grounding and bonding correct?** | ❌ **fail** | Module frames bonded; EGC sized per Table 250.122; connection to building grounding electrode system | CEC 690.43, 690.45, 690.47 |
| 13 | **Disconnect means provided?** | ❌ **fail** | PV system disconnect readily accessible, lockable, marked "PV SYSTEM DISCONNECT"; max 6 switches per system | CEC 690.13 |
| 14 | **Labeling complete?** | ❌ **fail** | Rapid shutdown label at service equipment; DC circuit labels (white on red, 3/8" min); power source directory per 705.10; max voltage label at disconnect | CEC 690.12(D), 690.31(D)(2), 690.7(D), 705.10 |
| 15 | **Structural adequate?** | ❌ **fail** | Roof designed for dead + live loads with PV weight; wind loading per Table R301.2.1; penetrations flashed/sealed | CRC R329.4.1, R329.4.3 |
| 16 | **Fire classification?** | ❌ **fail** | PV system fire rating matches required roof assembly rating | CRC R329.4.2, R902 |
| 17 | **ESS requirements met (if applicable)?** | ❌ **fail** | Listed per UL 9540; apply the R330.1 habitable-space exception path and R330.4 sleeping-room restrictions; verify smoke/heat alarms, impact protection, and capacity limits in Table R330.5 | CRC R330, CFC 1207 |
| 18 | **Inverter anti-islanding?** | ❌ **fail** | Interactive inverter ceases export on grid outage per 705.40; reconnects only after all phases restored | CEC 705.40 |

---

## References

Load these on demand. Paths are relative to this file.

- `references/california-baseline.md` — the full California rules for this permit (decision tree and checklist)
- `../city-reference/SKILL.md` — Laguna Beach codes adopted, design criteria, processing tracks, construction hours, and contacts

**California rules**

- `references/ess-requirements.md` — Energy Storage System (ESS) Requirements
- `references/fire-setbacks-cfc.md` — Fire Setbacks, Access Pathways, and Smoke Ventilation for Solar PV
- `references/grounding-bonding-690.md` — Grounding and Bonding for PV Systems
- `references/interconnection-705.md` — CEC Article 705 -- Interconnected Electric Power Production Sources
- `references/labeling-marking-690.md` — Labeling and Marking Requirements for PV Systems
- `references/pv-systems-690.md` — CEC Article 690 -- Solar Photovoltaic (PV) Systems
- `references/structural-roof-crc.md` — Structural and Building Requirements for Solar PV
- `references/wire-sizing-solar.md` — Wire Sizing and Conduit for Solar PV Circuits

**Laguna Beach rules**

- `references/city-solar-ordinance.md` — Laguna Beach Solar — Municipal Code Ch. 14.84

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
