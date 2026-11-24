# Question log template

Copy this into `logs/questions.md`. Append entries. Record an answer as soon as it arrives, including answers given through a structured-question tool.

```markdown
# Questions to the owner

## Q-001
- Date asked: <date>
- Question: "<exact words sent>"
- Picture: <path in questions/ or sources/, or none — never build/png/, which every build clears>
- Spot: <the physical place, in the owner's words>
- Tape: <start point> to <end point>; <along floor / along slope>; from <reference floor>
- Decides: <the value or decision this answer changes>
- Answer: "<the owner's exact words>"   Date answered: <date>
- Applied to: <project.json value IDs>; status set to <MEASURED / ...>
- Status: <open / answered / superseded by Q-xxx>
```

## Decision log entry (in `logs/decisions.md`)

```markdown
## DEC-001 — <short title>
- Date: <date>
- Decision: <what was decided>
- Decided by: <owner / agent, with owner confirmation>
- Reason and evidence: <sources, log IDs>
- Old value → new value: <if a value changed>
- Changed in: <project.json IDs; sheet scripts; forms; notes>
- Rebuild: <build folder or hash>
```
