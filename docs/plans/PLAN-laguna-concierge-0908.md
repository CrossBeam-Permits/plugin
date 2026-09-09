# Laguna Beach permit concierge — release standard and execution

Date: 2026-09-08. Baseline: public main `88323a8` (PRs #4 and #5).
Status: local checks, Codex installation/discovery, and manual installed-helper-to-demo-browser rehearsal passed. Exact City mapping, fresh-conversation activation, and complete filming packet remain outstanding.
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

## Next milestone: fictional video, no applicant dependency

The requested video uses fictional project facts and a demo account/packet. It does not
require a consenting applicant, a real applicant account, or a live applicant pilot.
The agent should actually operate the installed tools and browser during the recording.
A local replica or City-provided sandbox can demonstrate Submit and a clearly marked
sample receipt; this is evidence of a demonstration workflow, not a production City filing.
Do not insert fictional records into the City's production queue.

505 Forest Avenue may be used as a visibly labeled demo address. Do not infer residential
zoning, ownership, setbacks, or pool eligibility from that address: this scenario's
residential parcel facts are fictional fixtures, not findings about City Hall. Every
export and the portal demonstration must retain that distinction.

## Before filming: executable work packages

| Order | Work | Deliverable and acceptance condition | Current state |
|---|---|---|---|
| 1 | Map Zone Clearance intake | Dated source/evidence bundle identifying the exact portal menu, application type/ID, category, step sequence, required fields, conditional questions, uploads, fees, and confirmation behavior. Distinguish observed UI from City documentation and unknowns. Do not assume Residential Planning Entitlements type 114 is Zone Clearance. Update the application-set mapping and its fixture tests only when supported. | Official online channel verified; exact entry and authenticated flow unresolved |
| 2 | Build one coherent fictional pool case | Versioned fixture folder with project facts, fictional contacts, prior-review answer, sample plan inputs, matching completed forms and attachments. All exports labeled demonstration. Unknown real property facts stay unknown; mock facts stay explicitly synthetic. | Coherent browser fixture and sample plan inputs built; six facts filled in official Zone Clearance form. Full project packet/drawings outstanding |
| 3 | Provide a browser demo destination | Prefer a City-provided test environment if available; otherwise build a local replica from the verified mapping. Support fields, validation, upload, review, Submit, and a persistent receipt with a DEMO-prefixed record ID. Show “DEMONSTRATION — NOT A CITY SUBMISSION” throughout, including the receipt. Save uploaded files and submitted values for comparison. Mark any unobserved portal behavior as simulated. | Local provisional simulation built and exercised; no City sandbox established; exact portal fidelity remains blocked on mapping |
| 4 | Verify actual installation and browser operation | Start with Codex, the available filming candidate. Install the exact candidate artifact in a clean test scope, record its commit/version and host version, discover/invoke the skill from the pool prompt, read the fixtures, fill/render the PDFs, and use that host's browser tools to complete the demo destination. Save screenshots, tool/run evidence, and the resulting submission data. Repeat separately in Cowork and ChatGPT Work before promoting either. | Codex 0.153.4 install and 23-skill discovery pass; manual installed-helper/browser flow passes. Fresh-conversation activation and other hosts outstanding |
| 5 | Rehearse and inspect the result | Complete one uninterrupted prompt-to-demo-receipt run; compare every submitted value and attachment with the fixture. Also test a missing required attachment, an unknown project fact, and resuming the same saved case without duplicating submission. Confirm labels are readable and no credentials are visible. | Manual browser rehearsals pass, including missing inputs and same-receipt reload/server restart; uninterrupted fresh-conversation run outstanding |

For work package 1, inspect the public portal first. If relevant pages require login,
use a dedicated test account or City-supplied screenshots/test access; a real applicant's
account is not a dependency. If that access is unavailable, keep the exact mapping
unverified and document the missing screens. Public documents alone do not establish
hidden required fields or receipt semantics. City clarification may resolve gaps; no
message has been sent. Read-only production discovery and the fictional submission
rehearsal are separate activities.

For work package 4, a passing manifest check or tool-free model eval does not count as
installation evidence. Test the supported installation path and tool access in each
actual app. A platform fails qualification if it cannot read/write the packet or operate
the browser; record the limitation rather than silently substituting a different app.
Filming requires one qualified host. It does not require all three hosts to pass, and
video copy should name only the host(s) actually qualified.

The video is ready when work packages 1–5 have their evidence saved and the first host
passes. A clearly labeled prototype can be recorded earlier for internal review, but
it must not claim verified parity with the City's unmapped screens. ADU remapping and
a real applicant pilot are not prerequisites for this pool demonstration.

## September 8 execution evidence

Work is isolated in the `codex/laguna-permit-concierge-0908` git worktree and delivered
through PR #6. The [runnable rehearsal](../../demos/laguna-pool/README.md) includes a
loopback-only browser destination, durable drafts/receipts/uploads, reproducible fixture
PDF generation, installed-plugin official-form filling, and a receipt/byte comparator.

- [Codex installation](../qualification/laguna-codex-install-0908.json): exact installed
  cache comparison (227 files), app-server discovery (23 enabled skills, zero errors).
- [Sample browser transaction](../qualification/laguna-demo-browser-0908.json): all six
  project values and both uploaded files matched; missing inputs blocked; receipt
  survived browser reload and server restart.
- [Official-form browser transaction](../qualification/laguna-official-form-browser-0908.json):
  installed helpers filled and verified six exact official Zone Clearance fields;
  labeled PDF uploaded through the in-app browser and compared byte-for-byte at receipt.
  Remaining official form fields and project documents are not qualified as complete.
- [Current portal mapping evidence](../qualification/laguna-zone-clearance-mapping-0908.json):
  public search and type 114 login boundary checked; no evidence yet ties 114 to Zone
  Clearance. This remains an explicit unresolved requirement.

These are manual agent-operated qualification runs in the current task. They do not
prove automatic skill selection and full execution in a new user conversation. The
browser demo's required fields, upload categories, and receipt are simulated controls.
They are not substitutes for the missing production mapping.

## Broader product qualification

| Gate | Evidence required | State |
|---|---|---|
| Deterministic transactions | Missing approvals, duplicate targets, invalid records, facts, packets tested | Local pass |
| Current official form fill | Full/partial values, field tree, widget values, rendered pages | Local pass on DR |
| Instruction behavior | All 9 real model cases, saved responses and semantic verdicts | 9/9 pass, plus targeted first-exchange retest |
| Installed hosts and browser | Work package 4 per promoted host | Outstanding |
| Zone Clearance channel | Work package 1 | Incomplete |
| Production submission | Evidence of actual City acceptance and receipt, beyond a simulated demonstration | Not tested; not a video prerequisite |
| Corrections / issuance | Same-case continuation and observed City disposition; counter handoff when required | Not tested; not a video prerequisite |
| All-Laguna breadth | Every supported scope current; revised ADU mapped; unsupported forms added and tested | Outside this pool video milestone |

Do not claim the production end-to-end standard from a simulated receipt or green CI.
Owner-managed CI credential provisioning remains separate; do not silently copy API keys
into the public repository's secrets.

## Video brief

Target 35–45 seconds, captured from the qualified host actually operating the demo.
Persistent label: “DEMONSTRATION — FICTIONAL PROJECT — NOT A CITY SUBMISSION.”

1. “We want a pool in Laguna Beach.” Show the real opening prompt.
2. Agent reads the fictional project packet and asks the missing prior-review question.
3. Show the cited route and filled official application using the fictional inputs.
4. Agent fills the mapped demo portal and uploads the sample packet.
5. Show review, then the agent clicking Submit in the demo environment.
6. End on “Demo submission complete” and its visibly marked sample receipt/next steps.

Suggested wording: “See how CrossBeam's Laguna Beach skills help your agent prepare
permit paperwork and work through the submission process. Fictional demonstration.”
Do not present the sample receipt as City acceptance or an issued permit. A real filing
claim requires separate production evidence; it is not necessary to make this video.

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
