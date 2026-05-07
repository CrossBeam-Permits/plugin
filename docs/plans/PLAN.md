# CrossBeam Simple Permits — Open-Source Plan

**Date:** 2026-04-22
**Status:** Future plan — not started. Filed here + mirrored in `~/projects/crossbeam-simple-permits/PLAN.md`.
**Origin:** Brainstorm + reroof POC (see `~/projects/crossbeam-simple-permits/run-01-0422.md`, `run-02-0422.md`, `review-01-0422.md`).

---

## Positioning

**CrossBeam Simple Permits** is an open-source Claude Code / Claude Desktop plugin that gives away simple/over-the-counter permits across California as free skills. Every California city × every OTC permit type = one flat skill file Claude can run, in both builder and city-reviewer modes.

CrossBeam (paid) keeps the complex-permit surface: ADU, single-family residential, multi-unit residential, residential additions, restaurant TI, kitchen-bath remodel. These require the proprietary pipeline — extraction, Artemis vision, pinning, plan-sheet AI review — and cannot be replicated from the open skills alone.

The bet: giving away the simple-permit layer neutralizes competitors who focus there (PermitFlow, Symbium, GovOS, OpenCounter) and repositions CrossBeam as *the* company that does real plan sets. Cities adopting the free tier pre-qualify themselves as leads for the paid complex-permit product.

**Launch model:** announcement + GitHub repo + Anthropic marketplace listing. No conference demo. No paid tier on this repo.

---

## Target audiences (priority order)

### 1. City plan checkers — the primary target

The killer use case: a city drops a folder of 80 mixed-category simple permits into Claude Code and gets back a triage queue. Auto-approves, corrections required (with draft letters), edge cases for human review.

- Buena Park spends ~$340K/year on consultant plan review. This is the budget we're aimed at.
- Half a day of a plan checker's work compresses to 20 minutes.
- Output must be tight, actionable, and respect that plan checkers already know their job.

### 2. Builders / homeowners — informational primarily

- Primary value: Claude teaches what to submit, catches obvious issues before filing.
- PDF form-filling (seen in Run 02): fast, high-value, low-friction. Lead with this.
- Portal automation (seen in Run 01): slow, portal-dependent, shipped as optional capability — not a headline feature.

---

## Architectural pillars

### 1. Flatten-at-build

Internal authoring stays layered: `skills/california/{permit}/` + `skills/cities/{city}/{permit}/` — base + deltas. Clean edits, internal diff-ability. `sync-skills.sh` already does 80% of this.

Public output is flat: one `{city}-{permit}/SKILL.md` per pair, with state content inlined and city deltas woven in. Anti-extraction: a competitor reverse-engineering clean state skills has to scrape many flattened outputs, diff for shared structure, and disambiguate paraphrasing. Hard.

### 2. Plan-check vs inspection tagging (at state level)

Every checklist item in the 30 state skills gets three columns: `stage` (`plan-check` | `inspection` | `documentation`), `severity` (`fail` | `flag` | `verify` | `advisory`), `cite`.

**Why this is load-bearing:**
- Correctness — reviewer mode FAILs only on plan-check items, not inspection items. Cuts false-positive rate dramatically. (Review-01 flagged too much noise because every item was equal-weight.)
- File size — SKILL.md can load only plan-check rows in reviewer mode. Inspection rows split into `inspection.md`, loaded conditionally.
- Scalability — one-time 2-day pass across 30 state skills; tags propagate to every city flatten automatically.

Cities override tags in overlays only if local practice differs (rare — most cities follow the state rhythm).

### 3. Small, flat files

Target shape per (city, permit):

```
{city}-{permit}/
├── SKILL.md               ≤150 lines — intake + plan-check + submission guide
├── inspection.md          ~80 lines  — verify-at-inspection items
└── references/            deep-dives (state's existing reference files)
```

Anyone can edit a 150-line markdown. Cities contributing later is aspirational, but we design for it from day one.

### 4. Overlays as first-class

Coastal Zone, Wildfire WUI, methane/oil overlay are not permits — they're parcel-based modifiers that apply to any permit. Built as `_overlays/{coastal,wui,methane}.md` at state level, injected into flattened city skills only when the city's `meta.json` flags the overlay. HB reroof skill contains the coastal block inline for CZ parcels; Costa Mesa reroof doesn't.

This also cuts per-city authoring effort significantly — no city skill author has to remember "oh, HB also has methane."

### 5. Per-city meta.json

```json
{
  "city": "huntington-beach",
  "county": "orange",
  "climate_zone": 6,
  "portal": {
    "name": "Accela Citizen Access",
    "url": "https://engage.huntingtonbeachca.gov/CitizenAccess/Default.aspx",
    "automation_tier": "tier-1-vetted"
  },
  "overlays": ["coastal", "methane"],
  "fire_agency": "HBFD",
  "otc_permits": ["reroof", "ev-charger", "solar", "water-heater", "hvac", "..."],
  "local_amendments": {
    "reroof": "Class B minimum",
    "sprinklers": "mandatory all new SFR"
  }
}
```

One-time scrape during onboarding (batch-onboard already captures most of this). Enables programmatic routing, tier labeling, and user expectation-setting.

### 6. Tight reviewer output (hard requirement)

Every reviewer-mode output conforms to:

```
PLAN CHECK — {address} ({permit-type})

❌ CORRECTIONS REQUIRED (N)
   {plan-check + severity:fail items, code cite, one-line explanation}

⚠️ VERIFY BEFORE ISSUANCE (N)
   {plan-check + severity:flag items requiring documentation}

ℹ️ LOCAL FLAGS (N) — city discretion
   {city-specific items flagged, not blocking}

✓ {N} checks PASS (expand for detail)

➡ {N} checks deferred to inspection
```

No noise. No enumeration of every passing item unless asked. No mixing inspection items into corrections.

### 7. Batch review command

```bash
$ claude
> /batch-review ./inbox/2026-04-22/

Analyzing 80 permits...
  47 reroofs, 18 EV chargers, 9 water heaters, 4 panel upgrades, 2 solar

AUTO-APPROVE (52)
CORRECTIONS REQUIRED (19) — letters drafted in ./out/corrections/
NEEDS HUMAN REVIEW (7) — edge cases, scope oddities, valuation outliers
UNKNOWN PERMIT TYPE (2) — ./out/unknown/

Summary: crossbeam-batch-2026-04-22.csv
Draft emails: ./out/emails/ (71 ready to send)
```

This is the anchor feature. Single command, heterogeneous folder, triage queue out.

---

## What ships in v1

### In scope — permits

~20 OTC permit types at state level, flattened across all onboarded cities. Likely set:

reroof · ev-charger · solar · water-heater · hvac · window-replacement · panel-upgrade · temporary-power · repipe · siding-replacement · fence · block-wall · retaining-wall · patio-cover · deck-patio-repair · pool-demolition · ltia-demolition · cleanout · sign · fireworks-temp-use

Gray-area (per-city OTC check via meta.json): retaining-wall (height), sign (type/size), swimming-pool (new vs spa).

### In scope — cities

275 cities already have overlays on disk (batch-onboard completed through ~57% of CA's 482 incorporated cities). Ship with whatever is onboarded at launch; batch continues post-launch, auto-releases new city bundles.

Tiering at launch:
- **Tier 1 (vetted end-to-end):** HB, BP, Costa Mesa, Laguna Beach — partner cities, QA'd, portal-verified.
- **Tier 2 (skills vetted, portal unvetted):** ~20–50 cities with manual QA on skills.
- **Tier 3 (skills only):** remainder. Honest labeling — "community-reviewed pending."

### Out of scope (moat preservation)

- ADU, SFR, multi-unit, residential-addition — plan-set required, stays CrossBeam paid.
- Restaurant TI — plan-set required.
- Kitchen-bath-remodel — triage funnel back to CrossBeam paid (gray-area scope; AI triage value is in the paid product).
- Plan extraction pipeline, Artemis vision, pinning, corrections-letter polish, Bluebeam XFDF round-trip — all stay CrossBeam.
- Computer Use / browser-driven Accela as a headline feature — shipped as optional capability with honest tier labeling per portal.

---

## Sequenced milestones (no dates — sequence only)

1. **Plan-check/inspection tagging.** One-time pass across 30 state skills. Columnar table format. 2-day effort.
2. **Overlays as first-class.** Create `_overlays/{coastal,wui,methane}.md`. Flatten script injects per city's meta.json flags.
3. **Flatten script.** Extend `sync-skills.sh` → `scripts/flatten-skill.ts`. Inputs: state skill + city overlay + applicable overlay blocks. Output: flattened per-(city,permit) skill. Splits `SKILL.md` (plan-check) from `inspection.md` (inspection items).
4. **Tight reviewer output format.** Bake into every skill header. Update instructions so reviewer mode produces the 5-section structure by default.
5. **Batch review command.** `/batch-review <folder>` slash command. PDF routing + per-permit plan check + triage report + draft correction letters.
6. **Per-city meta.json audit.** 275 cities × OTC list, portal URL, automation tier, overlays, fire agency. Mostly automatable from batch-onboard data.
7. **QA pass on Tier-1 cities.** HB, BP, Costa Mesa, Laguna — manual end-to-end verification of flattened skills.
8. **Legal + licensing.** Disclaimer copy, license choice (MIT vs custom-with-disclaimer), municipal-code quotation review (ecode360 / ICC fair use).
9. **Plugin packaging.** `.claude-plugin/plugin.json`, commands/ directory, README, install-one-liner. Publish to Anthropic marketplace.
10. **Announcement.** GitHub repo public, landing page, blog post, Anthropic-portal listing. Partner cities named.

---

## Open questions

1. **License choice.** MIT is simplest, but plain MIT may not carry the liability disclaimer we need. Options: MIT + NOTICE, Apache-2.0 (has patent clause + NOTICE), or a bespoke "informational use, not legal advice" license. Needs real legal review before launch.
2. **Municipal code quoting.** HB's ecode360 content and ICC model codes have varying license terms. Skill files cite sections by number and paraphrase requirements, but in some cases quote short passages. Need a quote-not-reproduce audit before launch.
3. **Code update cadence.** CBC/CRC cycle is every 3 years (next: 2028). City amendments change more often. Release cadence: quarterly minor, annual major, emergency patch for city-breaking changes?
4. **Kitchen-bath triage funnel.** Keep debating. A free scope-triage skill ("do you need plans?") routes homeowners back to CrossBeam paid or adjacent free skills. Design TBD.
5. **Attribution in output.** Does every skill output carry "via CrossBeam Simple Permits — onboard.ai"? Subtle enough not to be obnoxious, visible enough that contractors arriving with CrossBeam-generated packages are recognizable by city staff.
6. **Cities editing their own skills.** Aspirational for v1. Design file layout so a city IT person or vendor can edit a 150-line markdown without architectural expertise. Actual contribution tooling (dashboard, forms) is v2+.
7. **Governance if Anthropic features it.** If the Anthropic marketplace highlights us and contributions flood in, we need a maintainer policy, PR review SLAs, and a decision rule for what changes Anthropic-branded vs partner-city-branded skills.

---

## Risks

- **Strictness calibration.** Too strict = false positives erode city trust immediately. Too loose = real issues slip through. Plan-check/inspection tagging + tight output format are the controls; validate against Tier-1 cities before wider release.
- **Stale portal assumptions.** Accela permit category names change, URLs move. Reroof POC already exposed "Residential Re-roof" vs "Residential Combo" drift. Solution: defensive prompt wording + "last verified" metadata per portal fact.
- **Competitor forks.** Open-source means anyone can fork. Accept. Complex-permit moat is execution, not knowledge — forking skills doesn't give a competitor extraction, Artemis, pinning, or UI.
- **Liability from wrong info.** Cities publish wrong info; our skill summarizes; applicant relies on it; something fails. Disclaimer + license language must make the informational-only stance airtight.
- **Network egress / sandbox limits.** POC hit real blocks downloading third-party PDFs. This is a Claude Code sandbox config issue for us, but users running in Claude Desktop with full permissions won't hit it. Document expectations per environment.
- **Municipal-code licensing trap.** Reproducing ecode360 or ICC content at scale could draw cease-and-desists. Paraphrase + cite, don't reproduce.

---

## Go-live criteria

- ✅ Plan-check/inspection tagging complete on all 30 state skills
- ✅ Overlays (coastal, WUI, methane) promoted to first-class
- ✅ Flatten script produces clean per-(city,permit) outputs
- ✅ Batch review command works end-to-end on a 40+ permit test folder
- ✅ Tier-1 cities (HB, BP, Costa Mesa, Laguna) QA'd end-to-end
- ✅ Legal disclaimer reviewed and attached
- ✅ License chosen and applied
- ✅ README + landing page ready
- ✅ Plugin listed on Anthropic marketplace (if that path coordinates)
- ✅ Partner cities notified pre-launch

---

## Proof-of-concept notes (what we learned from Reroof 0422)

**Worked well:**
- Single flattened SKILL.md drove both builder and reviewer modes cleanly
- Mode detection ("are you filing or reviewing?") was natural
- PDF form-fill (Run 02) was fast, accurate, and produced a genuinely useful output
- Reviewer mode caught real issues: Cool Roof CRRC blank, missing waste-management plan, undervalued valuation
- Parcel-lookup via Accela (address auto-fill, parcel number, owner) was impressive when it worked
- Owner-builder flow (license "000000") worked through the portal

**Didn't work well:**
- Reviewer mode too strict — flagged inspection items as plan-check corrections (drives the tagging requirement above)
- Skill's Accela category assumption was stale ("Residential Re-roof" vs actual "Residential Combo")
- Network egress blocked third-party PDF downloads (sandbox config issue)
- Claude asked for permission too much instead of just pushing forward

**Strategic takeaways:**
- Batch review for cities is the anchor use case — not consumer form-fill
- Portal automation is slow and per-portal. Ship it as optional, not headline.
- Plan-check/inspection tagging is the single highest-leverage architectural change before scaling
- Tight reviewer output format is as important as correct content

---

*Filed mirror at `~/projects/crossbeam-simple-permits/PLAN.md`.*
