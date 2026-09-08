# Laguna Beach permit concierge — release standard and execution

Date: 2026-09-08. Baseline: public main `88323a8` (PRs #4 and #5).
Status: local implementation qualified; draft release candidate. Live applicant release gate open.
Qualification: [machine-readable results](laguna-qualification-0908.json).

## The standard

A homeowner says “we want a pool in Laguna Beach.” The agent reads the available files,
asks only for missing facts, checks prior review and stage, determines the cited permit
route, prepares the official applications and supporting packet, drafts sheets when the
inputs/tools permit, completes the supported City intake channel, saves the real receipt,
and helps resolve corrections through issuance. A checklist or a populated PDF alone
is not completion. Missing surveys/engineering/signatures remain visible dependencies. The scope includes drawing assistance, not an unsupported promise of autonomous sealed engineering.

Support the same authored skills in Claude Cowork, Codex, and ChatGPT Work. Actual
installation and browser capabilities must be verified per surface before advertising
that surface. A manifest validation or instruction-only model eval is not installation
or browser-transaction proof.

## Audit and changes executed

- Private CrossBeam PR #917 was closed unmerged. Its replacement shipped in public PR
  #4 on August 24; PR #5 folded preparation into the single city plugin on August 25.
- All 22 scope skills lacked the required `name` frontmatter. Added canonical names;
  the official local Codex plugin validator now passes. Added a durable release check.
- Added the homeowner journey: prior private/City review and plan revision, drafting
  inputs, packet readiness, corrections, follow-up, and observed issuance status.
- Fixed the transaction compiler: unconfirmed individual records and unsatisfied
  sourced prerequisites block readiness; duplicate custom-field targets block rather
  than overwrite; exact portal field names survive compilation; malformed online
  records fail rather than disappear from a mixed batch. Submission-plan schema is 1.1.0.
- Corrected Zone Clearance's false appointment-only instruction in the skill and evals.
  Current official form p. 1 and the current City source page both require online filing.
  Exact portal entry remains unverified; use explicit `unverified` channel and blocked
  record until confirmed. A search of the public portal did not establish that entry.
- Found a superseded ADU PDF: source page links document 27032; manifest pins 26710.
  ADU preparation is explicitly blocked pending remap. Do not widen the pool pilot to ADUs.
- Reacquired Design Review from the current source-page link in a visible browser;
  SHA matches the pinned revision. Full form-map scenario: 205 target values verified.
  Partial case: 89 target values filled, 116 withheld targets blank, all 13 conformance
  facts withheld. These are synthetic mapping tests, not a real complete application.
- Reacquired Ordinance 1733 twice with matching bytes; reviewed all 10 pages. Section 4
  retains the 22-month-and-15-day extension. Refreshed that binary receipt; retained the
  overall August 24 law-review date. Full remote ordinance hash check passes locally.
- `claude plugin eval` returned “currently in early access.” Added a portable, tool-free
  model instruction runner using Claude print mode and semantic graders. CI skips the
  model job visibly if credentials are missing; missing evidence cannot qualify release.

## Release gates and next execution

| Gate | Evidence required | State |
|---|---|---|
| Deterministic transactions | Missing approvals, duplicate targets, invalid records, facts, packets tested | Local pass |
| Current official form fill | Full/partial values, field tree, widget values, rendered pages | Local pass on DR |
| Instruction behavior | All 9 real model cases, saved responses and semantic verdicts | 9/9 pass, plus targeted first-exchange retest |
| Codex package | Every skill discoverable and manifest valid | Local validator pass; installed-host test outstanding |
| Cowork / ChatGPT Work | Install the exact release artifact, invoke pool request, fill/render, browser handoff | Outstanding |
| Zone Clearance channel | City-confirmed menu/type, fields, attachments, receipt semantics | Needs City mapping |
| Real online filing | Consenting applicant, current packet, effective prerequisites, signed-in account, personal signature, explicit final click approval, terminal receipt | Needs applicant pilot |
| Corrections / issuance | Resume same case, actual correction letter and City disposition; counter handoff when required | Needs real case progression |
| All-Laguna breadth | Every supported scope current; revised ADU mapped; unsupported forms added and tested | Outstanding beyond pool pilot |

Execution order: finish local qualification and review the diff; test installation on each
promoted host; acquire the City Zone Clearance mapping and a consenting pool project;
prepare its actual packet and drawing gaps; conduct and record the authorized filing;
then release the video with claims limited to the verified host and observed milestone.
Do not claim all gates complete because deterministic CI is green. Do not silently copy
an API key into the public repository's secrets to activate CI; owner-managed credential
provisioning is a separate dependency. No City test records or fake submissions.

## Video brief

Target 35–45 seconds, filmed from the working host rather than a simulated submission UI.

1. “We want a pool in Laguna Beach.” Show the real opening prompt.
2. Agent reads the plans and asks the one missing project/review question.
3. Show cited route and completed official application; obscure applicant details.
4. Agent fills the real City portal and uploads the verified packet.
5. Applicant reviews/signs and approves the named application.
6. End on the real confirmation/record number: “Application submitted. Here’s what’s next.”

Until the live gate passes, show a local rehearsal with a persistent “DEMONSTRATION —
NOT SUBMITTED” label and end at the prepared packet. Suggested verified-outcome wording:
“From your pool idea to a prepared permit application, with CrossBeam’s Laguna Beach
skills.” Upgrade to “prepared and submitted” only after capturing an actual receipt.
Never edit an apparent successful submission into a rehearsal. Do not imply that a
submitted application is an issued permit.

## Verification commands

Run from the public repository root with Python dependencies from the city requirements:

```sh
python cities/laguna-beach/scripts/validate-plugin.py
node scripts/check-laguna-law-sources.mjs --verify-remote --enforce-review-window
python cities/laguna-beach/evals/run-model-evals.py --output-dir /private/task/model-results
python cities/laguna-beach/evals/run-official-partial-scenario.py \
  --forms-dir /private/task/current-official-forms --output-dir /private/task/form-tests
```

The model runner disables tools and uses only public plugin reference text plus synthetic
case prompts. It does not validate UI interactions. The official PDF tests require
freshly acquired City forms and deliberately keep PDFs and all generated data outside
the published plugin.

## Sources

- [Public PR #4](https://github.com/CrossBeam-Permits/plugin/pull/4)
- [Public PR #5](https://github.com/CrossBeam-Permits/plugin/pull/5)
- [City Applications & Handouts](https://www.lagunabeachcity.net/government/departments/community-development/planning-zoning/applications-handouts)
- [Zone Clearance form, p. 1](https://www.lagunabeachcity.net/home/showpublisheddocument/26718/639216211418770000)
- [City portal](https://lagunabeachca-energovweb.tylerhost.net/apps/SelfService#/home)
- [Ordinance 1733](https://ecode360.com/LA4953/laws/LF2782335.pdf)
- [OpenAI skills and plugin distribution](https://learn.chatgpt.com/docs/build-skills)
- [Claude plugin distribution](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization)
