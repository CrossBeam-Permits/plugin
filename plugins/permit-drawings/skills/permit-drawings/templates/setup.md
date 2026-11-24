# Setup log template

Copy this into `logs/setup.md` at stage 0 (`references/00-connect.md`). Add a new dated section when the host, the skill version or the tool map changes.

```markdown
# Setup

## <date> — <host name>
- Skill bundle version: <version> (from <crossbeam_get_skill / local copy>)
- Optional modules installed: <none / energy, structural, 3d> (`python3 -m permitkit modules`)
- Owner told the copy may be out of date: <date, or "not needed">
- Guide version: <version from crossbeam_guide>
- Python: <python3 --version>
- Kit scripts approved to run: <yes, date / host does not ask>

## Tool map

| Capability | Tool found | Fallback used |
|---|---|---|
| Code basis and guide version | <crossbeam_guide, or "missing"> | <Ask AI code-basis question; guide version "none"> |
| Read check results | <names, or "missing"> | <none needed until stage 7 / fixed on date> |
| Read the drafted response letter | | |
| Ask AI | | |
| Rules for what you draw | | |
| Primary code text | | |
| Permit fee estimate | | |
| Review requirements and packaging rules | | |
| Scope checklist | | |
| Skill files and version | | |
| Site facts | | |
| Start a check | | |
| Review status | | |
```
