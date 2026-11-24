# Working folder

Work only inside the owner's project folder. Stage 0 creates this tree before it writes anything else:

```text
permit-work/
├── sources/          originals: sketches, photos, quotes, product data, city documents, the owner's first message
├── project.json      every value, with status and source (the measurement register)
├── sheets/           one script per sheet; each reads only project.json
├── build/            kit output: sheet PDFs, previews, QA report, build.json
├── package/          one folder per city round: round-0/, round-1/, ...
├── history/          superseded builds and the frozen approved set, each labeled
├── questions/        pictures sent to the owner with a question; the build never touches it
└── logs/
    ├── setup.md            skill bundle version, guide version, host, tool map
    ├── scope.md            scope statement, room uses, permit type
    ├── required-documents.md  every document the set needs, who prepares it, its status
    ├── sheet-index.md      the planned set: every sheet and form, its source, preparer and kit module
    ├── questions.md        question log
    ├── decisions.md        decision and revision log
    ├── code-decisions.md   code basis; code questions, answers, citations, conversation IDs
    ├── disputes.md         disagreements with CrossBeam, the city or an agent, with evidence
    ├── crossbeam-rounds.md CrossBeam rounds: project ID, CrossBeam round, file hashes, counts, actions
    ├── city.md             city rounds: submittals, comments and responses
    └── release.md          stage lines, gate changes, and the evidence for each gate
```

Rules for the folder:

- Keep every original in `sources/`. Never edit an original. Record which way each sketch faces.
- Put every script in `sheets/` as soon as you write it. Temporary folders get deleted.
- The measurement register is `project.json`. Do not keep a second list of values.
- The field-verify schedule lives in `project.json`. The kit prints it on a sheet.
- Logs are append-only. Correct an entry with a new dated entry that names the old one. Three files are tables that you update in place: `logs/scope.md`, `logs/required-documents.md` and `logs/sheet-index.md`. Record each change to them in `logs/decisions.md`.
- At each stage exit, append `Stage <n> done — <date> — <one-line result>` to `logs/release.md`. Then ask each code question at `waiting` again (`05-code-questions.md` section 2, step 5).
- A choice the owner made stands until the owner changes it or the status of its item changes. Before you ask the owner anything, check `logs/decisions.md` for an earlier answer. Do not ask again. Do not repeat a warning that `logs/decisions.md` records as said.
- After each build, tell the owner the path of the current file. Open it if the host can.

Templates for the logs and prompts are in `templates/`: `setup.md`, `scope.md`, `required-documents.md`, `category-questions.md` (the stage 2 questions to Ask AI), `release.md`, `question-log.md` (also the decision log), `code-decision-log.md` (also the dispute log), `kickoff-prompt.md`, `crossbeam-findings-prompt.md` and `response-sheet.md`.
