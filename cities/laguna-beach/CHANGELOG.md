# Laguna Beach plugin changelog

The version in `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`,
`.cursor-plugin/plugin.json`, `gemini-extension.json`, and this plugin's entry in the
repository `.claude-plugin/marketplace.json` must match. `scripts/validate-plugin.py`
fails when they differ or when this file has no section for the current version.

`main` is the release line. Hosts that install from the marketplace get whatever
`main` holds for `cities/laguna-beach`. See "Pinning a release" at the end.

## 0.5.0 (unreleased)

Host packaging:

- Optional CrossBeam connector. `.mcp.json` declares the `crossbeam` remote MCP server
  (`https://crossbeam-mcp.old-cherry-b095.workers.dev/mcp`, OAuth). Codex loads the same
  file. Gemini and Cursor declare it in their own manifests. Every skill works without it.
- New `gemini-extension.json` and `.cursor-plugin/plugin.json`. These hosts get the
  skills only; see `docs/qualification/HOSTS.md` at the repository root.
- `scripts/plugin_root.py` prints the plugin root. The preparer entry skill now tells the
  agent to use absolute plugin paths, because the user's task directory is the working
  directory and Claude Code does not export `CLAUDE_PLUGIN_ROOT` to shell commands.
- `scripts/validate-plugin.py` runs in an installed copy. It skips marketplace checks
  there and says so. CI passes `--require-marketplace`.
- `evals/run-host-smoke.sh` installs the plugin from a local marketplace into a
  throwaway home and checks the skill list.
- CI shows the model-eval job as skipped, not passed, when no Claude credential is set.

Content:

- Generated from the CrossBeam corpus by the plugin publisher in the private
  repo; `.generated/manifest.json` records the source commit and hashes, and a CI drift
  check fails when this copy falls behind. Fixes the fireworks advice (Laguna bans
  fireworks), the reroof advice (Class A, color rules) and the "HBFD clearance" line that
  had leaked into every city.
- New plan-set permit skills: new single-family home, ADU, addition, remodel, kitchen and
  bath, multi-unit, commercial and restaurant TI, demolition, coastal development and
  general building. The plan-set kinds carry the Laguna Beach layer only; California
  code compliance comes from the CrossBeam connector (`crossbeam_get_review_requirements`,
  `crossbeam_ask`, a CrossBeam check). Without it, the skill says what it cannot check.
- `requirements/`: the City's Building and Planning checklists, the plan-sheet matrix
  (21 project types by 16 sheet columns), the issuance checklist and the fee schedule.
- New `plan-set-check` skill: checks the merged plan set against the City's sheet lists
  and cites pages.
- Fee estimate runs the shared CrossBeam fee calculator (`scripts/estimate-fees.mjs`).
- Building application re-pinned to the City's current 2-page form with the Stormwater
  Quality Certification. The applicant signs before upload, and
  `scripts/verify-signed-form.py` checks the signed copy.
- Portal map v2: every online work class with its questions, uploads and fee timing. The
  agent picks the work class by reasoning and the user confirms it. Standalone demolition
  and Zone Clearance are filed online. A weekly job checks the live portal for drift.
- New references: `plan-sheets.md` (drawing with CrossBeam permit-drawings and its
  hand-off), `portal-account.md`, `after-filing.md`.
- Law reviewed through 2026-10-10 (no ordinance after 1733). HVAC and pool/spa equipment
  now only has to stay out of the required front yard setback to skip Design Review
  (Ord. 1731, LBMC §7.25.130(C)(2)), and that test applies in any zone, not only in or
  adjacent to residential areas. A required side yard is still closed to that equipment
  under §25.50.004(F)(2). The coastal exemption record no longer has to be on the City's
  website (Ord. 1732, §25.07.008(B)).
- Pinned six Planning forms from the City's Applications & Handouts page (2026-10-10,
  headless browser, same-origin fetch from the loaded page; receipts in the manifest):
  ADU & JADU (document 27032, replacing 26710, which moves to `retired_forms`), SB 9
  (26958, replacing the DRAFT 26708), Temporary Use Permit, Revocable Encroachment
  Permit, Lot Line Adjustment, and Sign Permit. Each fillable form has an exact semantic
  map and a fill/verify round trip in `evals/forms`. `pending_sources` is empty.
- The Sign Permit Application and the SB 9 application sections have no form fields.
  Their maps list `manual_sections`; `fill-form.py` prints them, and refuses a map with
  no mappings instead of writing an unchanged copy.

## 0.4.0 (2026-09-08, PR #6)

Release candidate for the Laguna permit concierge. Evidence lives in
`docs/plans/PLAN-laguna-concierge-0908.md` and `docs/qualification/`.

- Added `name` frontmatter to all 22 scope skills and moved source fields under
  `metadata`, so Codex and other Agent Skills hosts discover every skill.
- Added the homeowner journey (`references/homeowner-journey.md`): prior City or private
  review, plan revision, drafting inputs, packet readiness, corrections, and issuance.
- Fixed the submission-plan compiler (schema 1.1.0). Unconfirmed records and unmet
  sourced prerequisites block readiness. Duplicate custom-field targets block instead of
  overwriting. Malformed online records fail instead of dropping out of a batch.
- Corrected Zone Clearance from appointment-only to online filing under Residential
  Planning Entitlements, type 114, with dated source receipts in
  `assets/portal-maps/zone-clearance-2026-09-08/`.
- Blocked ADU preparation: the City replaced the ADU form (document 27032) and the pinned
  map is for 26710.
- Re-verified the Design Review form and Ordinance 1733 receipts.
- Added `evals/run-model-evals.py`, a tool-free model instruction eval with semantic
  graders, plus the official-form partial scenario runner.
- Recorded Codex 0.153.4 install (23 skills), CLI opening activation, a fictional local
  browser rehearsal, and real Tyler type 114 uploads through the Signature step. No
  production filing was made.

## 0.3.0 (2026-08-24, PRs #4 and #5)

- Folded the separate Laguna submit plugin into `laguna-beach`: one plugin per city.
- Added the preparer: guided intake, Planning and Building routing, SHA-pinned official
  City forms and semantic field maps, fill/verify/render helpers, packet assembly, and
  Tyler EnerGov submission gates with receipt capture.

## Pinning a release

Claude Code and Codex both accept `ref` (branch or tag) and `sha` (full 40-character
commit) on a `git-subdir` marketplace source. Both were checked on 2026-10-09 with a
local repository: Claude Code 2.1.295 and Codex CLI 0.162.0 installed the pinned commit,
not the branch tip, with `ref` plus `sha` and with `sha` alone.

When the lead decides to cut pinned releases:

1. Merge the release to `main` with matching versions and a dated section here.
2. Tag it `laguna-beach--v<version>`. `claude plugin tag cities/laguna-beach` creates
   that tag and checks that `plugin.json` and the marketplace entry agree.
3. Add `"ref": "laguna-beach--v<version>"` and `"sha": "<commit>"` to the
   `laguna-beach` source in `.claude-plugin/marketplace.json`.

Until then, the entry has no pin and `main` is what users install.
