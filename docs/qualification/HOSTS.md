# Laguna Beach plugin: host support

Last checked: 2026-10-09, plugin 0.5.0.

This page says which agent hosts can run the `laguna-beach` plugin and how far each
can go. "Tested" means we installed it here and checked the result. "Docs" means we
read the host's documentation but did not run it. Nothing below is evidence of a
filing with the City.

## Tiers

| Tier | What the user gets | Hosts |
|---|---|---|
| Full filing | Intake, routing, official form fill and verification, packet assembly, and a user-controlled EnerGov session through receipt capture | Claude Code, Codex, Claude Cowork |
| Prepare only | Intake, routing, and a `portal_ready` handoff. The user files in their own browser | claude.ai chat, ChatGPT |
| Skills only, best effort | The 23 skills load as instructions. Helpers run where the host has a shell. No supported browser path | Gemini CLI, Cursor, Grok |

Full filing still needs a user-visible browser the agent can drive, a signed-in City
account the user controls, and the user's own signature, approval, and payment. The
plugin never submits without fresh approval for each record.

## Host details

| Host | Install | Skills | Shell for helpers | Browser for the portal | CrossBeam connector | What it lacks | Evidence |
|---|---|---|---|---|---|---|---|
| Claude Code | Tested: `claude plugin marketplace add` then `claude plugin install laguna-beach@crossbeam-permits` | Tested: 23/23 | Yes | Claude in Chrome (docs). Not yet run against the City portal | Tested: listed as "Needs authentication"; `/mcp` signs in with OAuth | A completed live City filing | [smoke](laguna-host-smoke-1009.json), [probes](laguna-host-probes-1009.json), [Chrome docs](https://code.claude.com/docs/en/chrome) |
| Codex CLI | Tested: reads the Claude marketplace file directly | Tested: 23/23 via app-server `skills/list` | Yes | None built in. Needs a browser MCP or the Codex desktop in-app browser. One fresh CLI run hit "Chrome denied uploads" | Tested: listed, "Not logged in"; `codex mcp login crossbeam` | Built-in browser in the CLI; uninterrupted desktop run | [smoke](laguna-host-smoke-1009.json), [0908 install](laguna-codex-install-0908.json), [0908 fresh run](laguna-fresh-rehearsal-0908.json), [OpenAI plugin docs](https://developers.openai.com/plugins/build/plugins) |
| Claude Cowork | Docs: Customize, Plugins, Add marketplace, then install | Docs: same plugin, synced to the account | Yes (Cowork session) | Claude in Chrome (docs) | Docs: install does not connect it; open the plugin's Connectors tab | Not tested here. Marketplace repo archive limit is 512 MB; this repository is about 760 MB uncompressed | [Cowork plugins](https://claude.com/docs/cowork/guide/plugins), [plugins overview](https://claude.com/docs/plugins/overview) |
| claude.ai chat | Docs: same Customize, Plugins, Add marketplace; plugins sync to the account | Docs: skills load in chat | Only with code execution turned on | None | Docs: Connectors tab | Browser control, so no portal session | [plugins overview](https://claude.com/docs/plugins/overview) |
| ChatGPT | ChatGPT on the web cannot add a custom marketplace (2026-10-08 audit). OpenAI docs say the desktop app reads `.claude-plugin/marketplace.json` from a local repository; not tested | Skills only where installed | Varies | None we can rely on | Not tested | Remote marketplace install, browser control | [OpenAI plugin docs](https://developers.openai.com/plugins/build/plugins) |
| Gemini CLI | Tested: `gemini extensions install <path>` with `gemini-extension.json` | Tested: 23/23 via `gemini skills list` | Yes | None built in | Tested: listed as Disconnected until `/mcp auth crossbeam` | Browser control; installs a whole repository or a local path, not a subfolder of this monorepo | [smoke](laguna-host-smoke-1009.json), [extension reference](https://geminicli.com/docs/extensions/reference/), [MCP docs](https://geminicli.com/docs/tools/mcp-server/) |
| Cursor | Docs: `.cursor-plugin/plugin.json` names `./skills/` and the connector | Docs only | Yes (agent terminal) | Not verified | Docs only; OAuth for plugin servers is not documented | A repository-root `.cursor-plugin/marketplace.json` to install from this monorepo; any test | [Cursor plugin reference](https://cursor.com/docs/reference/plugins) |
| Grok | Docs: Grok Build says it reads Claude Code marketplaces, plugins, skills, and MCP servers | Not tested | Yes (terminal) | Not verified | Not tested | Any test | [xAI skills and plugins](https://docs.x.ai/build/features/skills-plugins-marketplaces) |

Gemini CLI note: its docs say Gemini CLI was replaced by Antigravity CLI for unpaid and
Google One users on 2026-06-18. We tested Gemini CLI 0.63.0 with an API key.

## How each host finds the plugin root

Helpers live in the plugin, but the agent works in the user's task directory. The
preparer entry skill (`cities/laguna-beach/skills/laguna-permit-preparer/SKILL.md`)
handles this:

- Claude Code replaces `${CLAUDE_PLUGIN_ROOT}` in skill text with the absolute path. It
  does not export it to shell commands (tested; see probes).
- Other hosts leave the text alone, so the agent uses the folder two levels above the
  skill file.
- `python3 "<plugin-root>/scripts/plugin_root.py"` confirms the root from any directory.

## Skill names

Claude Code loads skills from `skills/` and ignores the root `SKILL.md` while `skills/`
exists. Codex and Gemini also load only `skills/`. So the preparer loads once, as
`laguna-beach:laguna-permit-preparer`, on every tested host. The root `SKILL.md` is the
canonical instruction file that the entry skill reads.

## Run the install smoke test

```sh
cd cities/laguna-beach
evals/run-host-smoke.sh --host claude                 # CI runs this
evals/run-host-smoke.sh --host all --output result.json
```

It copies the plugin into a temporary local marketplace, installs it into a throwaway
home for each host CLI it finds, and checks: the install, the skill list against
`skills/*/SKILL.md`, the connector declaration, that the installed copy matches the
source, and that the installed copy's own `validate-plugin.py` and `plugin_root.py`
pass. Set `CODEX_BIN` or `GEMINI_BIN` to use a CLI that is not on `PATH`. A missing CLI
is reported as skipped.

It does not prove that the model picks the right skill, that a browser works, or that a
filing succeeds. Those need the per-host runs in `PLAN-laguna-concierge-0908.md`.

## Results on 2026-10-09

| Host | Version | Install | Skills | Connector | Installed validator |
|---|---|---|---|---|---|
| Claude Code | 2.1.295 | pass | 23/23 | declared, needs auth | pass |
| Codex CLI | 0.162.0 | pass | 23/23 | declared, not logged in | pass |
| Gemini CLI | 0.63.0 | pass | 23/23 | declared, disconnected | pass |

Codex reports `authPolicy: ON_INSTALL` for entries in the Claude-format marketplace.
The CLI did not prompt. Whether the ChatGPT desktop app asks for the connector at install
is untested.
