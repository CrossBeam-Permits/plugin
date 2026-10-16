---
name: city-website
description: "Laguna Beach Community Development website and online permit portal facts: counter hours and contacts, the building and planning process, which fees exist, forms, FAQs, and how to submit each application type online (channel, link, intake questions, required attachments). Use for \"how do I apply\", \"where do I file this\", \"what do I upload\", \"when is the counter open\". Not code requirements: use the permit skills and the guide for those."
metadata:
  version: "2.0"
  authority: "City of Laguna Beach"
  generated: "Generated from the CrossBeam corpus. Edit the source, not this file."
---

# Laguna Beach — City website knowledge pack

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

A curated snapshot of the City's Community Development web section, built so a
resident-facing assistant can answer department questions without sending anyone
to go hunting on lagunabeachcity.net.

**Scope:** 34 pages under
`lagunabeachcity.net/government/departments/community-development` plus the staff
directory and the fee schedule PDF, **and** the City's Tyler EnerGov permit
portal — all 19 online application types, their wizard instructions, intake
questions, and attachment requirements. **Not** in scope: municipal code text and
zoning standards — those live in the sibling skills under
the permit skills in this plugin and in the City source document (not included in this plugin).
(The submittal checklists here are the *portal's* — what the online form demands
before it will accept a filing — not code compliance.)

> **Dollar amounts for modeled fees come from the fee estimate, not this pack.**
> They live in the city's `../../requirements/fees/fee-schedule.json`. A reference file here may
> describe *which* fees exist, who bills them, and when they are due — never how
> much.

Unmodeled charges live in `references/fees.md`. Only two of those may include
figures: annual sewer service charges and City Attorney hourly rates. Everything
else unmodeled is named there without an amount.

## Topic router

| Topic | Reference file | Load it when the resident asks… |
|---|---|---|
| **Submitting: which channel, which link** | `references/how-to-submit.md` | "How do I apply for X?" "Where do I file this?" "Can I do it online?" "What's the link?" — **the router for every submission question.** Maps any project type to one of four channels (EnerGov portal / SolarAPP+ then EnerGov / appointment / counter) and gives the exact deep link. |
| **Submitting: one specific application type** | `references/submit-<type>.md` | Load the matching guide when the resident is ready to apply — one per online type (`references/submit-adu.md`, `references/submit-solar.md`, `references/submit-residential-permit.md`, `references/submit-plumbing.md`, …, 18 in all; Transportation Permits (394) is covered inside `references/submit-right-of-way.md`). `references/how-to-submit.md` names the right one. Each covers prerequisites, the wizard step by step in the City's own words, the intake questions, required and optional attachments with file rules, contacts and licences, and what happens after submit. |
| Hours, addresses, division phones, appointments, portals | `../city-reference/references/contacts-hours.md` | "When are you open?" "What's the number for Planning?" "Where do I go?" "How do I book an appointment?" |
| Building permits: need one?, process, counter review, inspections | `references/building-permits.md` | "Do I need a permit for X?" "How do I get an inspection?" "Can I do this over the counter?" "How long is my permit good for?" |
| Planning applications, design review, historic, views/trees | `references/planning-applications.md` | "How does design review work?" "What application do I file?" "How long until my hearing?" "Can I appeal?" |
| Code enforcement, complaints, leaf blowers, civil vs. code | `references/code-enforcement.md` | "My neighbor is…" "How do I report…?" "Is that even a violation?" |
| Fees | `references/fees.md` | "What does it cost?" "What's the plan check fee?" "Sewer connection fee?" — call the fee estimate for any modeled amount. `references/fees.md` names which fees exist, which are deposit-based, and which the tool does not model. |
| Published FAQs | `references/faqs.md` | Any question phrased the way the City's own FAQ phrases it |
| Document/form links with version stamps | `references/forms-index.md` | "Where's the form?" "Send me the fee schedule." |

## How to answer from this pack

1. **Always carry the source.** Every fact line ends with `[source: <url>, as of <YYYY-MM-DD>]`. Give the resident the date and the link — the SOW requires a source reference on every response, and it lets them verify a fact that may have moved.
2. **The "as of" date is the City's own `lastmod`**, not the day you're answering. Say "as of July 8, 2026 the City published…", not "currently".
4. **Six things on the City's site contradict themselves or mislead** — the Planning phone number, the permit-counter closing time, the design-review appeal period, how planning applications are accepted (portal vs. appointment), the Code Enforcement click-to-call that dials Police dispatch, and the over-the-counter walk-in hours (the appointment page still prints the 2021 "afternoon" window; the City's 06/08/2026 handout says Monday–Thursday 7:30 a.m. – 2:00 p.m., last check-in 12:45 p.m.). All are flagged in place with ⚠️. Present both readings and the safe fallback; never silently pick one.
5. **Never give a staff member's own email address, even where a City page prints one.** A few City pages print an individual's address, for example the Interested Parties page. Send the resident to the City's staff contact form instead: the "Email" link next to the staff member on the [Community Development staff directory](https://www.lagunabeachcity.net/government/departments/community-development/community-development-staff-directory). The City's form delivers the message. Also give the person's direct phone line. A shared mailbox that is not a person, such as lbinspectors@lagunabeachcity.net, is fine to give. Never guess an address from a name pattern — that would be fabrication.
6. **When you can't answer**, route to Ask Laguna (https://clients.comcate.com/newrequest.php?id=167, 24/7) plus the relevant division phone from `../city-reference/references/contacts-hours.md`.
7. **Every "how do I get a permit for X" answer ENDS with a "Next step" line.** Name the channel and give the link as a **labelled markdown link — never a bare URL** (the voice rules already require labelled links). If an account is needed first, say so in the same line. Example:
   > **Next step:** file a Residential Permit in the City's permit portal — [Residential Permit (type 183)](https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/permit/apply/183/0/0). You'll need a portal account first — [registration guide](https://www.lagunabeachcity.net/home/showpublisheddocument/20625/638678768735230000).

   Two things must never be dropped from a submission answer: **ADU is two filings** (plan 182, then permit 183), and **most building permits are still issued in person at the counter** even when applied for online.

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

- `references/building-permits.md` — Laguna Beach — Building Permits (from the City website)
- `references/code-enforcement.md` — Laguna Beach — Code Enforcement
- `references/faqs.md` — Laguna Beach Community Development — FAQs
- `references/fees.md` — Laguna Beach — fee topics (Master Fee Schedule)
- `references/forms-index.md` — Laguna Beach — document / forms index
- `references/how-to-submit.md` — Laguna Beach — How to Submit: the channel map
- `references/planning-applications.md` — Laguna Beach — Planning Division: applications and the design review process
- `references/submit-adu.md` — Submit: ADUs and JADUs — EnerGov type 182
- `references/submit-commercial-permit.md` — Submit: Commercial Permit — EnerGov type 184
- `references/submit-commercial-planning-entitlements.md` — Submit: Commercial Planning Entitlements — EnerGov type 116
- `references/submit-electrical.md` — Submit: Electrical Permit — EnerGov type 187
- `references/submit-fire-commercial.md` — Submit: Fire Commercial Permit — EnerGov type 191
- `references/submit-fire-residential.md` — Submit: Fire Residential Permit — EnerGov type 190
- `references/submit-grading.md` — Submit: Grading Permit — EnerGov type 214
- `references/submit-mechanical.md` — Submit: Mechanical Permit — EnerGov type 186
- `references/submit-mixed-use.md` — Submit: Mixed Use Permit — EnerGov type 374
- `references/submit-multifamily.md` — Submit: Multifamily Permit — EnerGov type 322
- `references/submit-plumbing.md` — Submit: Plumbing Permit — EnerGov type 188
- `references/submit-real-property-report.md` — Submit: Real Property Report — EnerGov type 192
- `references/submit-residential-permit.md` — Submit: Residential Permit — EnerGov type 183
- `references/submit-residential-planning-entitlements.md` — Submit: Residential Planning Entitlements — EnerGov type 114
- `references/submit-right-of-way.md` — Submit: Right-of-Way Permits — EnerGov type 315 (and Transportation Permits, type 394)
- `references/submit-sign.md` — Submit: Sign Permit — EnerGov type 197
- `references/submit-solar.md` — Submit: SolarAPP+ Permit — EnerGov type 124
- `references/submit-view-preservation.md` — Submit: View Preservation — EnerGov type 301

---

*Generated by CrossBeam Permits · crossbeam-permits.com · © Onboard Dot AI LLC · Apache-2.0*
*Informational use only; not legal advice; jurisdiction governs.*
