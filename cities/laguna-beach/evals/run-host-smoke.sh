#!/usr/bin/env bash
# Install this plugin into a throwaway home for each agent host CLI and check
# what the host loads: the skill list, the optional CrossBeam connector, and the
# installed copy's own validator and root resolver.
#
# The plugin comes from a local-path marketplace built in a temporary folder,
# so the test never touches the user's real host settings or the network
# (except `claude mcp list`, which probes the connector URL without signing in).
#
# Usage:
#   evals/run-host-smoke.sh [--host claude|codex|gemini|all]... [--output FILE] [--keep]
#
# Host binaries come from PATH, or from CLAUDE_BIN, CODEX_BIN, GEMINI_BIN.
# A host whose CLI is missing is reported as "skipped", not "pass".
# Exit status is non-zero when any host that ran failed.

set -euo pipefail

PLUGIN_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MARKETPLACE_NAME="crossbeam-smoke"
PLUGIN_ID="laguna-beach@${MARKETPLACE_NAME}"
CLAUDE_BIN="${CLAUDE_BIN:-claude}"
CODEX_BIN="${CODEX_BIN:-codex}"
GEMINI_BIN="${GEMINI_BIN:-gemini}"

hosts=()
output=""
keep=0
while [ $# -gt 0 ]; do
  case "$1" in
    --host) hosts+=("$2"); shift 2 ;;
    --output) output="$2"; shift 2 ;;
    --keep) keep=1; shift ;;
    -h|--help) sed -n '2,17p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done
[ ${#hosts[@]} -eq 0 ] && hosts=(claude)
if [ "${hosts[*]}" = "all" ]; then hosts=(claude codex gemini); fi

WORK="$(mktemp -d "${TMPDIR:-/tmp}/laguna-host-smoke.XXXXXX")"
cleanup() { if [ "$keep" -eq 0 ]; then rm -rf "$WORK"; else echo "kept $WORK" >&2; fi; }
trap cleanup EXIT
mkdir -p "$WORK/tmp" "$WORK/results"

# A local marketplace that holds an exact copy of this plugin.
MARKET="$WORK/market"
mkdir -p "$MARKET/.claude-plugin"
tar -C "$(dirname "$PLUGIN_DIR")" \
  --exclude='__pycache__' --exclude='evals/results' --exclude='*.pyc' \
  -cf - "$(basename "$PLUGIN_DIR")" | tar -C "$MARKET" -xf -
if [ "$(basename "$PLUGIN_DIR")" != "laguna-beach" ]; then
  mv "$MARKET/$(basename "$PLUGIN_DIR")" "$MARKET/laguna-beach"
fi
cat > "$MARKET/.claude-plugin/marketplace.json" <<EOF
{
  "name": "${MARKETPLACE_NAME}",
  "owner": {"name": "Laguna host smoke test"},
  "plugins": [
    {"name": "laguna-beach", "source": "./laguna-beach", "description": "Local smoke-test copy"}
  ]
}
EOF

# Run a host command with a throwaway home and nothing inherited from the
# caller's agent session (no session ids, no plugin sync, no credentials).
in_home() {
  local home="$1"; shift
  local pass=()
  local name
  for name in HTTPS_PROXY HTTP_PROXY NO_PROXY https_proxy http_proxy no_proxy \
              SSL_CERT_FILE NODE_EXTRA_CA_CERTS REQUESTS_CA_BUNDLE; do
    if [ -n "${!name:-}" ]; then pass+=("$name=${!name}"); fi
  done
  env -i HOME="$home" CODEX_HOME="$home/.codex" PATH="$PATH" LANG=C.UTF-8 \
    TMPDIR="$WORK/tmp" TERM=dumb NO_COLOR=1 ${pass[@]+"${pass[@]}"} "$@"
}

# Compare the installed copy with the source copy and run its own checks.
# Prints a JSON fragment.
installed_checks() {
  python3 - "$MARKET/laguna-beach" "$1" <<'PY'
import hashlib, json, subprocess, sys
from pathlib import Path
source, installed = Path(sys.argv[1]), Path(sys.argv[2])
def tree(root):
    out = {}
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root).as_posix()
        if path.is_file() and "__pycache__" not in rel and not rel.startswith(".mcpb-cache"):
            out[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    return out
a, b = tree(source), tree(installed)
result = {
    "installed_path": str(installed),
    "files": len(a),
    "missing_in_install": sorted(set(a) - set(b)),
    "changed_in_install": sorted(k for k in a if k in b and a[k] != b[k]),
}
def run(args):
    done = subprocess.run([sys.executable, *args], cwd="/", capture_output=True, text=True)
    return {"exit": done.returncode, "last_line": (done.stdout.strip() or done.stderr.strip()).splitlines()[-1:]}
result["installed_validator"] = run([str(installed / "scripts/validate-plugin.py"), "--skip-evals", "--skip-claude-validation"])
result["plugin_root_resolver"] = run([str(installed / "scripts/plugin_root.py")])
result["plugin_root_resolver"]["matches_install"] = result["plugin_root_resolver"]["last_line"] == [str(installed.resolve())]
print(json.dumps(result))
PY
}

expected_skills() {
  python3 - "$MARKET/laguna-beach" <<'PY'
import json, sys
from pathlib import Path
names = []
for skill in sorted(Path(sys.argv[1], "skills").glob("*/SKILL.md")):
    text = skill.read_text(encoding="utf-8")
    name = next((line.split(":", 1)[1].strip() for line in text.split("---", 2)[1].splitlines()
                 if line.startswith("name:")), skill.parent.name)
    names.append(name)
print(json.dumps(sorted(names)))
PY
}
EXPECTED="$(expected_skills)"

write_result() {
  # $1 host, $2 JSON object with the host's raw facts
  python3 - "$1" "$2" "$EXPECTED" "$WORK/results/$1.json" <<'PY'
import json, sys
host, raw, expected, out = sys.argv[1], json.loads(sys.argv[2]), json.loads(sys.argv[3]), sys.argv[4]
found = sorted(raw.get("skills") or [])
raw["skills_expected"] = len(expected)
raw["skills_found"] = len(found)
raw["skills_missing"] = sorted(set(expected) - set(found))
raw["skills_unexpected"] = sorted(set(found) - set(expected))
inst = raw.get("installed") or {}
checks = {
    "installed": raw.get("installed_version") is not None,
    "skills": not raw["skills_missing"] and not raw["skills_unexpected"],
    "connector_declared": bool(raw.get("connector_declared")),
    "copy_identical": not inst.get("missing_in_install") and not inst.get("changed_in_install"),
    "installed_validator": (inst.get("installed_validator") or {}).get("exit") == 0,
    "plugin_root_resolver": bool((inst.get("plugin_root_resolver") or {}).get("matches_install")),
}
raw["checks"] = checks
raw["result"] = "pass" if all(checks.values()) else "fail"
json.dump(raw, open(out, "w"), indent=2)
print(f"{raw['result'].upper()} {host}: {raw['skills_found']}/{raw['skills_expected']} skills, "
      f"connector={'yes' if checks['connector_declared'] else 'no'}, "
      f"failed checks={[k for k, v in checks.items() if not v]}")
PY
}

skip_host() {
  printf '{"host": "%s", "result": "skipped", "reason": "%s"}\n' "$1" "$2" > "$WORK/results/$1.json"
  echo "SKIP $1: $2"
}

smoke_claude() {
  command -v "$CLAUDE_BIN" >/dev/null 2>&1 || { skip_host claude "Claude Code CLI not found"; return 0; }
  local home="$WORK/home-claude"; mkdir -p "$home"
  local version; version="$(in_home "$home" "$CLAUDE_BIN" --version 2>/dev/null | head -1)"
  in_home "$home" "$CLAUDE_BIN" plugin marketplace add "$MARKET" >"$WORK/claude-market.log" 2>&1 || true
  in_home "$home" "$CLAUDE_BIN" plugin install "$PLUGIN_ID" >"$WORK/claude-install.log" 2>&1 || true
  in_home "$home" "$CLAUDE_BIN" plugin list --json >"$WORK/claude-list.json" 2>/dev/null || echo '[]' >"$WORK/claude-list.json"
  in_home "$home" "$CLAUDE_BIN" plugin details "$PLUGIN_ID" >"$WORK/claude-details.txt" 2>&1 || true
  (cd "$WORK/tmp" && in_home "$home" timeout 90 "$CLAUDE_BIN" mcp list </dev/null >"$WORK/claude-mcp.txt" 2>&1) || true
  local install_path
  install_path="$(python3 -c 'import json,sys; d=[p for p in json.load(open(sys.argv[1])) if p.get("id")==sys.argv[2]]; print(d[0].get("installPath","") if d else "")' "$WORK/claude-list.json" "$PLUGIN_ID")"
  local installed='{}'
  [ -n "$install_path" ] && [ -d "$install_path" ] && installed="$(installed_checks "$install_path")"
  local raw
  raw="$(python3 - "$WORK" "$PLUGIN_ID" "$version" "$installed" <<'PY'
import json, re, sys
from pathlib import Path
work, plugin_id, version, installed = Path(sys.argv[1]), sys.argv[2], sys.argv[3], json.loads(sys.argv[4])
listing = [p for p in json.loads((work / "claude-list.json").read_text() or "[]") if p.get("id") == plugin_id]
details = (work / "claude-details.txt").read_text()
skills, mcp = [], []
for line in details.splitlines():
    match = re.match(r"\s*Skills \(\d+\)\s+(.*)$", line)
    if match:
        skills = [item.strip() for item in match.group(1).split(",") if item.strip()]
    match = re.match(r"\s*MCP servers \(\d+\)\s+(\S+)", line)
    if match:
        mcp = [match.group(1)]
mcp_status = [line.strip() for line in (work / "claude-mcp.txt").read_text().splitlines() if "crossbeam" in line]
print(json.dumps({
    "host": "claude-code", "cli_version": version,
    "installed_version": listing[0].get("version") if listing else None,
    "skills": skills, "connector_declared": mcp == ["crossbeam"],
    "connector_status_unauthenticated": mcp_status[:1],
    "installed": installed,
}))
PY
)"
  write_result claude "$raw"
}

smoke_codex() {
  command -v "$CODEX_BIN" >/dev/null 2>&1 || { skip_host codex "Codex CLI not found"; return 0; }
  local home="$WORK/home-codex"; mkdir -p "$home/.codex" "$WORK/task-codex"
  local version; version="$(in_home "$home" "$CODEX_BIN" --version 2>/dev/null | grep -v WARNING | head -1)"
  in_home "$home" "$CODEX_BIN" plugin marketplace add "$MARKET" >"$WORK/codex-market.log" 2>&1 || true
  in_home "$home" "$CODEX_BIN" plugin add "$PLUGIN_ID" --json >"$WORK/codex-install.json" 2>"$WORK/codex-install.err" || true
  in_home "$home" "$CODEX_BIN" mcp list >"$WORK/codex-mcp.txt" 2>&1 || true
  local install_path
  install_path="$(python3 -c 'import json,sys
try: print(json.load(open(sys.argv[1])).get("installedPath",""))
except Exception: print("")' "$WORK/codex-install.json")"
  local installed='{}'
  [ -n "$install_path" ] && [ -d "$install_path" ] && installed="$(installed_checks "$install_path")"
  local raw
  raw="$(cd "$WORK/task-codex" && in_home "$home" python3 - "$CODEX_BIN" "$WORK" "$version" "$installed" <<'PY'
import json, os, subprocess, sys, time
from pathlib import Path
codex, work, version, installed = sys.argv[1], Path(sys.argv[2]), sys.argv[3], json.loads(sys.argv[4])
try:
    install = json.loads((work / "codex-install.json").read_text())
except ValueError:
    install = {}
skills, errors = [], []
proc = subprocess.Popen([codex, "app-server"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.DEVNULL, text=True)
def send(message):
    proc.stdin.write(json.dumps(message) + "\n"); proc.stdin.flush()
try:
    send({"id": 1, "method": "initialize", "params": {"clientInfo": {"name": "laguna-host-smoke", "version": "1"}}})
    send({"method": "initialized"})
    send({"id": 2, "method": "skills/list", "params": {"cwds": [os.getcwd()], "forceReload": True}})
    deadline = time.time() + 90
    while time.time() < deadline:
        line = proc.stdout.readline()
        if not line:
            break
        message = json.loads(line)
        if message.get("id") == 2:
            for entry in (message.get("result") or {}).get("data", []):
                errors += entry.get("errors", [])
                skills += [s["name"].split(":", 1)[-1] for s in entry.get("skills", [])
                           if (s.get("pluginId") or "").startswith("laguna-beach@") and s.get("enabled")]
            break
finally:
    proc.kill()
mcp = [" ".join(line.split()) for line in (work / "codex-mcp.txt").read_text().splitlines()
       if line.startswith("crossbeam ")]
print(json.dumps({
    "host": "codex-cli", "cli_version": version,
    "installed_version": install.get("version"), "auth_policy": install.get("authPolicy"),
    "skills": sorted(set(skills)), "skill_errors": errors,
    "connector_declared": bool(mcp), "connector_status_unauthenticated": mcp[:1],
    "installed": installed,
}))
PY
)"
  write_result codex "$raw"
}

smoke_gemini() {
  command -v "$GEMINI_BIN" >/dev/null 2>&1 || { skip_host gemini "Gemini CLI not found"; return 0; }
  local home="$WORK/home-gemini"; mkdir -p "$home" "$WORK/task-gemini"
  local version; version="$(in_home "$home" "$GEMINI_BIN" --version 2>/dev/null | head -1)"
  # The install asks whether to trust the source folder; answer yes for the copy.
  (cd "$WORK/task-gemini" && echo y | in_home "$home" timeout 120 "$GEMINI_BIN" extensions install \
    "$MARKET/laguna-beach" --consent --skip-settings >"$WORK/gemini-install.log" 2>&1) || true
  (cd "$WORK/task-gemini" && in_home "$home" timeout 120 "$GEMINI_BIN" skills list </dev/null >"$WORK/gemini-skills.txt" 2>&1) || true
  (cd "$WORK/task-gemini" && in_home "$home" timeout 120 "$GEMINI_BIN" mcp list </dev/null >"$WORK/gemini-mcp.txt" 2>&1) || true
  local install_path="$home/.gemini/extensions/laguna-beach"
  local installed='{}'
  [ -d "$install_path" ] && installed="$(installed_checks "$install_path")"
  local raw
  raw="$(python3 - "$WORK" "$version" "$installed" "$install_path" <<'PY'
import json, re, sys
from pathlib import Path
work, version, installed, install_path = Path(sys.argv[1]), sys.argv[2], json.loads(sys.argv[3]), sys.argv[4]
skills, current = [], None
for line in (work / "gemini-skills.txt").read_text().splitlines():
    match = re.match(r"^(\S+) \[(Enabled|Disabled)\]", line)
    if match:
        current = match.group(1) if match.group(2) == "Enabled" else None
        continue
    match = re.match(r"\s+Location:\s+(.*)$", line)
    if match and current and match.group(1).startswith(install_path + "/"):
        skills.append(current)
mcp = [line.strip() for line in (work / "gemini-mcp.txt").read_text().splitlines()
       if "crossbeam (from laguna-beach)" in line]
manifest = Path(install_path, "gemini-extension.json")
print(json.dumps({
    "host": "gemini-cli", "cli_version": version,
    "installed_version": json.loads(manifest.read_text()).get("version") if manifest.is_file() else None,
    "skills": skills, "connector_declared": bool(mcp), "connector_status_unauthenticated": mcp[:1],
    "installed": installed,
}))
PY
)"
  write_result gemini "$raw"
}

for host in "${hosts[@]}"; do
  case "$host" in
    claude) smoke_claude ;;
    codex) smoke_codex ;;
    gemini) smoke_gemini ;;
    *) echo "unknown host: $host" >&2; exit 2 ;;
  esac
done

summary="$(python3 - "$WORK/results" "$PLUGIN_DIR" "$WORK" <<'PY'
import json, sys
from datetime import datetime, timezone
from pathlib import Path
results = [json.loads(p.read_text()) for p in sorted(Path(sys.argv[1]).glob("*.json"))]
manifest = json.loads(Path(sys.argv[2], ".claude-plugin/plugin.json").read_text())
text = json.dumps({
    "kind": "laguna-host-install-smoke",
    "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    "plugin_version": manifest["version"],
    "method": "Local-path marketplace holding an exact copy of cities/laguna-beach; each host CLI run with a throwaway HOME and an empty environment; no sign-in.",
    "proves": "Install, skill discovery, connector declaration, and the installed copy's own validator. It does not prove skill activation, model behavior, browser control, or a filing.",
    "hosts": results,
}, indent=2)
# Throwaway paths carry no meaning outside this run.
print(text.replace(sys.argv[3], "<tmp>"))
PY
)"
if [ -n "$output" ]; then printf '%s\n' "$summary" > "$output"; echo "wrote $output"; else printf '%s\n' "$summary"; fi
python3 -c 'import json,sys; sys.exit(1 if any(h.get("result")=="fail" for h in json.loads(sys.argv[1])["hosts"]) else 0)' "$summary"
