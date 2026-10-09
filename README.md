# CrossBeam Permits

Open-source permit guidance for all 484 California cities. **One plugin per city.** Each provides 22 simple-permit skills for homeowners, builders, and public-agency reviewers. Laguna Beach goes further: the same plugin also prepares verified official City forms and guides a user-controlled Tyler EnerGov filing.

## Install

Add the marketplace once, then install a city. Installing a city fetches only that
city's folder.

**Claude Code**

```sh
claude plugin marketplace add CrossBeam-Permits/plugin --sparse .claude-plugin
claude plugin install laguna-beach@crossbeam-permits
```

**Codex**

```sh
codex plugin marketplace add CrossBeam-Permits/plugin --sparse .claude-plugin
codex plugin add laguna-beach@crossbeam-permits
```

**Claude Cowork and claude.ai**

1. Open **Customize**, then **Plugins**.
2. Choose **Add marketplace** and enter `CrossBeam-Permits/plugin`
   (or `https://github.com/CrossBeam-Permits/plugin`).
3. Find **Laguna Beach Permits** and click **Install**.

A plugin installed this way is saved to your Claude account, so it also appears in chat
and in Claude Code.

**Gemini CLI** (skills only). Gemini installs a whole repository or a local folder, so
check out just the city folder first:

```sh
git clone --depth 1 --filter=blob:none --sparse https://github.com/CrossBeam-Permits/plugin.git
git -C plugin sparse-checkout set cities/laguna-beach
gemini extensions install ./plugin/cities/laguna-beach
```

In Claude Code, Codex, Cowork, and claude.ai, substitute any of the 484 city slugs for
`laguna-beach`. Only Laguna Beach ships the Gemini and Cursor manifests.

### What each host can do with Laguna Beach

| Tier | Hosts | What you get |
|---|---|---|
| Full filing | Claude Code, Codex, Claude Cowork | Intake, routing, official forms, packet, and a user-controlled City portal session through the receipt. Needs a browser the agent can drive (for example Claude in Chrome, or a browser tool in Codex). |
| Prepare only | claude.ai chat, ChatGPT | Intake, routing, and a `portal_ready` packet with an answer sheet. You file in your own browser. |
| Skills only, best effort | Gemini CLI, Cursor, Grok | The skills load as instructions. No supported portal path. |

Details, evidence, and what each host lacks: [docs/qualification/HOSTS.md](docs/qualification/HOSTS.md).

### Optional CrossBeam connector

The Laguna plugin declares the CrossBeam MCP server
(`https://crossbeam-mcp.old-cherry-b095.workers.dev/mcp`). It lets the agent ask
CrossBeam permit and code questions and look up parcels. It uses your own CrossBeam
sign-in (OAuth) and is **optional**: every skill works without it, and the agent carries
on if it is not connected.

- Claude Code: run `/mcp` and pick `crossbeam` to sign in.
- Codex: `codex mcp login crossbeam`.
- Cowork and claude.ai: open the plugin's **Connectors** tab. Installing does not connect it.
- Gemini CLI: `/mcp auth crossbeam`.

For ChatGPT Work distribution, follow the [official plugin guidance](https://learn.chatgpt.com/docs/build-skills); this repository is not evidence of a public directory listing.

## What each city includes

The catalog contains 10,648 skills: 22 permit types for each of 484 cities.

`reroof` · `ev-charger` · `solar` · `water-heater` · `hvac` · `window-replacement` · `panel-upgrade` · `temporary-power` · `repipe` · `siding-replacement` · `fence` · `block-wall` · `retaining-wall` · `patio-cover` · `deck-patio-repair` · `pool-demolition` · `ltia-demolition` · `cleanout` · `sign` · `fireworks-temp-use` · `swimming-pool` · `rewire`

Each skill supports two modes:

- **Builder or homeowner:** guided intake, compliance review, and a submission guide.
- **City reviewer:** checklist-based plan review and concise correction output.

Permit-system facts are generated from the repository's onboarding data. The current catalog has a known system or documented offline intake method for 166 cities and an absolute HTTP(S) portal URL for 195 cities. Unknown facts remain `null`; a skill does not guess a vendor or URL.

## Laguna Beach goes deeper

Most cities ship the 22 plan-check skills. Laguna Beach adds a full preparation and filing layer inside the same plugin:

- guided project-fact intake with provenance, unknown values kept null;
- cited Planning and Building routing — pool height above grade, coastal, bluff, geotechnical, and equipment questions, with LBMC authorities;
- SHA-256-pinned official City forms and exact semantic field maps;
- local fill, render, verification, and packet assembly;
- Tyler EnerGov draft navigation, duplicate checks, effective-value review, and receipt capture;
- a safe `portal_ready` handoff when browser control is unavailable.

Nothing is ever submitted without fresh, explicit, per-record approval. You enter your own signature. A filing is only reported as submitted when the portal shows a terminal confirmation and a receipt is written.

City form downloads reject headless clients. Acquire blocked forms in a user-visible browser, then run the included freshness verifier against the pinned receipt before filling them.

## Laguna qualification status

The [September 8 release plan](docs/plans/PLAN-laguna-concierge-0908.md) defines the
homeowner-to-filing standard, verified behavior, remaining City/host dependencies, and
the fictional video gates. A [local browser rehearsal](demos/laguna-pool/README.md) now
supports sample uploads and durable demo receipts. Codex candidate installation and
manual installed-helper/browser operations have passed. Fresh CLI opening activation
also passes; an uninterrupted desktop conversation-to-browser run is still unverified. Local demonstrations do not prove a live City filing.
The current City public configuration verifies Zone Clearance under Residential
Planning Entitlements, type 114. Authenticated screen layout remains unobserved. The revised ADU form needs remapping. Building
application submission and final in-person permit issuance are separate milestones.

## Checks for maintainers

From `cities/laguna-beach`:

```sh
python3 evals/run-evals.py                 # deterministic evals
python3 scripts/validate-plugin.py         # manifests, versions, connector, skills
evals/run-host-smoke.sh --host claude      # install into a throwaway home
```

`validate-plugin.py` also runs inside an installed copy, where it skips the marketplace
checks and says so. Release notes live in `cities/laguna-beach/CHANGELOG.md`.

CI (`.github/workflows/laguna-permit-skill.yml`) runs the model instruction evals only
when the repository has an `ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN` Actions
secret. Without one, the `model-evals` job shows as skipped, and the run summary says
model behavior was not verified.
