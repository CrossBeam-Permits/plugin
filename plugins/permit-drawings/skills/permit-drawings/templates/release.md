# Release log template

Copy this into `logs/release.md` at stage 0 (`references/00-connect.md` section 1). Append only. `references/10-release.md` defines the gates and their evidence.

```markdown
# Release

Gate: REVIEW — <date>

Stage 0 done — <date> — <one-line result>
Stage 1 done — <date> — <one-line result>

## Waiting on owner
<date> — <document or answer> — by <date, or "no date"> — <what the owner must send>

## Gate change — <gate> — <date>
- Evidence: <each item from 10-release.md, with where it is recorded>
- File hashes: <file name — SHA-256>
- package_hash: <value CrossBeam returned, for a gate that used a CrossBeam round, or "none (web path)">
```
