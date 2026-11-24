# Code-decision log template

Copy this into `logs/code-decisions.md`. Append entries. Never edit an old entry. Correct it with a new entry that names the old ID.

```markdown
# Code decisions

## Code basis
- Jurisdiction: <city or county, state>
- Codes and editions: <as CrossBeam states them>
- Effective date: <date>
- Local amendments: <list, or "none stated">
- Source: <CrossBeam code_basis / Ask AI conversation ID>, asked <date>
- CrossBeam covers this jurisdiction: <yes / no — if no, every entry is "not checked by CrossBeam">
- Primary text available: <yes — where / no — why (record this once here, not in each entry)>

## CD-001 — <short topic, e.g. "egress window in bedroom 2">
- Date: <date>
- Question (as sent): "<exact question>"
- Asked through: <crossbeam_rules (element: "<element as sent>", confidence <high/medium/low>, quote_has_values <true/false>) / crossbeam_ask / owner in web app / other channel>   Conversation: <ID or link, or sources/askai/AI-nnn.md when the channel gives neither>
- Answer: <one or two sentences, or "none: failed turn / empty answer / rate_limited until <resets_at>">
- Jurisdiction / edition used: <jurisdiction_used> / <edition_used>
- Citations: <code, edition, section, verbatim quote, link — only items the answer quotes verbatim (citations[] or the pasted text), or primary text you read (source URL, edition)> — level <quoted / primary-read>; <...>
- Unquoted claims: <every section number or limit in the answer that no verbatim quote holds, every paraphrase or summary, plus any unverified[] items, or "none"> — these never print
- Primary text read: <yes — where / no (the reason is in the code basis above)>
- Facts assumed: <value — status>; <...>
- Conditions in the quote: <each condition and the branch that applies, with the fact that selects it and its status, or "none"> — if any, add `{"cd": "CD-001", "conditions": true}` to `code_notes` in project.json
- Affects: <project.json values>; sheets <IDs>; rules entries <R-ids in project.json, or none>
- Sheet note: "<exact note text, with the threshold and the citation>" — written with `kit.text(..., cd="CD-001")` so QA can find it; the ID never prints
- Code limits printed: <each limit — the citation whose quote holds it>
- Level: <quoted / primary-read / unquoted / disputed (see disputes.md) / waiting> — the lowest level of any citation or limit the sheet note prints
- Supersedes: <CD-xxx, or none>
```

## Dispute entry (in `logs/disputes.md`)

```markdown
## DS-001 — <topic>
- Date: <date>
- Parties: <CrossBeam / city / agent / owner>
- Claim A: <who said what, with citation>
- Claim B: <who said what, with citation>
- Primary text: "<quote>" (<code, edition, section>)
- Outcome: <which claim held, and why>
- Owner told: <date>
- Owner accepted the dispute: <yes, date, the owner's words / no>
- Note sent to CrossBeam: <yes, date / no>
```
