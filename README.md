# CrossBeam Permits

Open-source permit guidance for all 484 California cities. **One plugin per city.** Each provides 22 simple-permit skills for homeowners, builders, and public-agency reviewers. Laguna Beach goes further: the same plugin also prepares verified official City forms and guides a user-controlled Tyler EnerGov filing.

## Install

One command per city. Nothing else to add.

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

**Claude Cowork** — open the Cowork tab, then **Customize → Plugins → Add from a repository**, point it at `https://github.com/CrossBeam-Permits/plugin`, and install **Laguna Beach Permits**.

Substitute any of the 484 city slugs for `laguna-beach`. Adding the marketplace is a one-time step; installing a city then fetches only that city's subdirectory.

The package shares one skill tree and the same Python helpers across runtimes. Actual browser control and installation must be qualified on each host. For ChatGPT Work distribution, follow the [official plugin guidance](https://learn.chatgpt.com/docs/build-skills); this repository is not evidence of a public directory listing.

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
the filmed-pilot gate. Local form and instruction tests do not prove a live filing.
Zone Clearance requires online submission under the current City form, but its exact
portal entry still needs verification. The revised ADU form needs remapping. Building
application submission and final in-person permit issuance are separate milestones.
