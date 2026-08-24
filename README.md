# CrossBeam Permits

Open-source permit guidance for all 484 California cities. Each city plugin provides 22 simple-permit skills for homeowners, builders, and public-agency reviewers. Laguna Beach also has an optional submittal plugin that prepares verified City forms and guides a user-controlled Tyler EnerGov filing.

## Install with Claude Code

Add the marketplace once. Sparse checkout keeps the marketplace catalog small; installing a plugin then fetches only that plugin's subdirectory.

```sh
claude plugin marketplace add CrossBeam-Permits/plugin --sparse .claude-plugin
claude plugin install laguna-beach@crossbeam-permits
```

For the complete Laguna preparation and submittal workflow, install the submit plugin. Its Claude manifest declares the Laguna city plugin as a dependency, so this is the only install command needed:

```sh
claude plugin install laguna-beach-submit@crossbeam-permits
```

## Install with Codex

```sh
codex plugin marketplace add CrossBeam-Permits/plugin --sparse .claude-plugin
codex plugin add laguna-beach@crossbeam-permits
codex plugin add laguna-beach-submit@crossbeam-permits
```

Claude Code and Codex load the same canonical Laguna preparer instructions and deterministic Python tools. Codex currently installs the city and submit plugins separately.

## What each city includes

The catalog contains 10,648 skills: 22 permit types for each of 484 cities.

`reroof` · `ev-charger` · `solar` · `water-heater` · `hvac` · `window-replacement` · `panel-upgrade` · `temporary-power` · `repipe` · `siding-replacement` · `fence` · `block-wall` · `retaining-wall` · `patio-cover` · `deck-patio-repair` · `pool-demolition` · `ltia-demolition` · `cleanout` · `sign` · `fireworks-temp-use` · `swimming-pool` · `rewire`

Each skill supports two modes:

- **Builder or homeowner:** guided intake, compliance review, and a submission guide.
- **City reviewer:** checklist-based plan review and concise correction output.

Permit-system facts are generated from the repository's onboarding data. The current catalog has a known system or documented offline intake method for 166 cities and an absolute HTTP(S) portal URL for 195 cities. Unknown facts remain `null`; a skill does not guess a vendor or URL.

## Laguna Beach submittal plugin

`laguna-beach-submit` adds the transaction layer to the Laguna city guidance:

- guided project-fact intake with provenance and unknown values kept null;
- cited Planning and Building routing, including pool height, coastal, bluff, geotechnical, and equipment questions;
- SHA-256-pinned official forms and exact semantic field maps;
- local fill, render, verification, and packet-assembly tools;
- Tyler EnerGov draft navigation, duplicate checks, effective-value review, and receipt capture;
- a safe `portal_ready` handoff when browser control is unavailable.

City form downloads can reject headless clients. Acquire blocked forms in a user-visible browser, then run the included freshness verifier against the pinned receipt before filling them.

The plugin never treats preparation as authority to file. The applicant enters signatures, credentials, MFA, and payment information personally. It pauses for fresh approval immediately before each final Submit action and reports `submitted` only after a terminal portal confirmation and written receipt. Development and CI never file a live application.

## Source quality

Source quality varies by city, and the catalog retains each plugin's review-tier label. A higher tier means more local review; it does not override the issuing agency. Statutory and form-source receipts are checked in CI, while time-sensitive Laguna law sources also have a scheduled freshness check.

This project is informational and is not legal advice. The issuing jurisdiction controls every final interpretation and permit decision. See [NOTICE](NOTICE).

## License

[Apache-2.0](LICENSE)

CrossBeam Permits is a project of [Onboard Dot AI LLC](https://crossbeam-permits.com). The paid CrossBeam product handles more complex review workflows such as ADUs, additions, multi-unit projects, and tenant improvements.
