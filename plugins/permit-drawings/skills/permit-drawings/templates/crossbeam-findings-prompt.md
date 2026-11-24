# CrossBeam findings prompt

The owner sends this when a CrossBeam check finishes. Fill the brackets. If the owner does not know the project ID, leave it out. The agent finds it with `crossbeam_list_projects`.

```text
My CrossBeam check finished. Connect to my CrossBeam project <project ID> ("<project name or address>").
Pull the project summary and all FAIL findings, then CORRECTION, then FLAG.
Walk me through fixing them, one at a time.

Important: CrossBeam's findings cite the code edition stated in code_basis.
If a cited section conflicts with what you remember, your memory is presumed out of date.
Check the primary text through CrossBeam before you dispute a citation.
If the primary text does not support CrossBeam, record it as a dispute with the quote.

The drawing source is in permit-work/. Change project.json and the sheet scripts,
rebuild the whole set, and never patch the PDF.
If a finding says a document is missing, prepare the document, do not only list it.
```

## What the agent records

For each finding, one line in `logs/crossbeam-rounds.md`:

| CrossBeam round | Finding ID | Status | Sheet (from pin) | Decision | Change | Sheets rebuilt |
|---|---|---|---|---|---|---|

Decision values: `fixed`, `document added`, `asked owner`, `disputed (see disputes.md; record whether the owner accepted it)`, `advice — no change (reason)`.
