# Stage 10: Release

Read this before you change the gate label on the sheets, and when the owner asks "Is this ready?"

## The gates

The set moves through five gates in order. Each gate needs its own evidence. A later gate never skips an earlier one.

| Gate | Meaning | Label printed on every sheet |
|---|---|---|
| REVIEW | Design review set. Not final. | `REVIEW — NOT FOR CONSTRUCTION` |
| READY TO SUBMIT | The set is fixed and ready for a CrossBeam check. | `READY TO SUBMIT — NOT FOR CONSTRUCTION` |
| PERMIT REVIEW | The set passed CrossBeam and is packaged for the city, or is under city review. | `PERMIT REVIEW — NOT FOR CONSTRUCTION`, or the city's required designation |
| APPROVED | The city approved this set. | The city's approval stamp. Nothing else changes. |
| FOR CONSTRUCTION | Field values confirmed and build details complete. | `FOR CONSTRUCTION` |

## Who sets each gate

| Gate | Set by | When |
|---|---|---|
| REVIEW | Stage 0, section 1 | When the folder is created |
| READY TO SUBMIT | Stage 7, section 1 | Before the first CrossBeam round |
| PERMIT REVIEW | Stage 8, section 5 | After the CrossBeam stop rule, before the city package build |
| APPROVED | This stage | When the city's approval document arrives |
| FOR CONSTRUCTION | This stage | After APPROVED, when its evidence below is met |

The label prints in every title block. A label change changes every file hash. So a gate change that prints follows this order:

1. Confirm the evidence for the gate.
2. Set the label in `project.status_label` in `project.json`. `kit-sheets.md` ("Title block") describes how the kit prints it.
3. Run a full build: `python3 -m permitkit build project.json`. Run the kit QA. Run the text audit (`06-draw-checks.md` section 3). The kit checks the label in the title block only. A note that repeats an old label passes QA.
4. Record the file hashes: the SHA-256 of each file in the build (`file_sha256` in `build/build.json`, plus any file you add).
5. Record the gate change in `logs/release.md`: date, gate, evidence, file hashes.

At READY TO SUBMIT, stage 7 then uploads these files, validates them (CrossBeam returns `package_hash` and `price`), gets the owner's approval of the price, and submits. Record the `package_hash` next to the file hashes. Use the name `package_hash` only for the value CrossBeam returns. On the web path no tool returns one. Record `package_hash: none (web path)` (`07-crossbeam-check.md` section 3).

## Evidence for each gate

### REVIEW

- `project.json` passes the kit's model checks (`python3 -m permitkit validate project.json`).
- The draft sheets build.
- Open questions are in `logs/questions.md`.
- The field-verify schedule exists and is ranked.

### READY TO SUBMIT

- No row in `logs/required-documents.md` blocks a CrossBeam check (`02-path.md` section 3, step 8). A code question at `waiting` may stay open only with the owner's approval to check without it (`07-crossbeam-check.md` section 0).
- The kit QA passes. You did a vision pass on this build.
- The cross-sheet text audit found no open contradiction and no unresolved "or" choice (`06-draw-checks.md` section 3).
- Every code citation and code limit on the sheets is `quoted` or `primary-read` (`05-code-questions.md` section 3).
- No sheet prints a compliance claim on an ASSUMED value.
- The site-visit list ran, and the owner chose to measure or to draw with FV tags (`06-draw.md` section 0).
- The owner saw the permit sheets of this build, not only the stage 4 draft plan. If the owner asked for changes, apply them, rebuild, and run the QA, the vision pass and the text audit again. Then tell the owner each change in one line. A second review is needed only when you changed something the owner did not ask for.

### PERMIT REVIEW

Evidence to set the label:

- The CrossBeam stop rule is met (`07-crossbeam-check.md` section 8).
- The city file manifest has a row for every file, each with a rule source or `unknown: confirm with the city` (`08-package.md` section 2).

Evidence to send city round 0 (`08-package.md` section 6). Record it in `logs/city.md`:

- The owner saw the "measure these" list of this build (`python3 -m permitkit measure`) and every open connection, and measured them or approved sending with them open (`08-package.md` section 3, step 6).
- Every unknown in the manifest, in `logs/required-documents.md` and in `logs/scope.md` is resolved, or the owner approved sending without it. `logs/decisions.md` records the approval, the owner's words and the list of open items (`08-package.md` section 3, step 6). The city may still reject the submittal for an open item. The approval message says so once.
- No title block prints `OWNER NAME PENDING`. The property owner's name replaces it (`08-package.md` section 5, step 2).
- Every form value traces to a sheet or a source.
- The owner signed what the owner must sign.
- The owner gave fresh approval to send.

When a city plugin files the set (`city-plugin-handoff.md`), the plugin sends round 0. Record its filing receipt in `logs/city.md` as the send evidence: the record number, the date and the file hashes it uploaded.

### APPROVED

- The city's approval document is in `sources/city/`.
- The approved files are copied to `history/approved-<date>/` with their file hashes. Copy `project.json`, `sheets/` and `build/build.json` of that build there too.
- No rebuild. Record the gate change in `logs/release.md`.

After approval, the approved set is frozen:

- Never edit, rebuild over or regenerate the approved files.
- Right after approval, before you change `project.json`, check that the sheet scripts still reproduce the approved set. Run `python3 -m permitkit build project.json --out build-check --no-determinism`. Compare `file_sha256` in `build-check/build.json` with `file_sha256` in `history/approved-<date>/build.json`. Record the result in `logs/release.md`. Then delete `build-check/`.
- If a later drawing shows that a note on the approved set is wrong, record it in `logs/decisions.md`. Tell the owner. The owner decides whether to tell the city. A life-safety conflict needs that decision.

FOR CONSTRUCTION is the last gate of the same set. Closing FV tags and adding build details for permitted work stay in this set. A later design change to permitted work starts a new set with its own gates, from REVIEW. A new set's scripts may read `project.json` values but write only their own output.

Example: after approval, an agent found that an approved sheet showed two shelves where three were planned. It did not touch the approved file. It recorded the difference and drew the shelves on a separate build sheet that was not a permit document.

### FOR CONSTRUCTION

- Every row in the field-verify schedule is closed by a tape value or a site check, and has its `signed_off` entry.
- If a field value changed permitted work, the change is in `logs/decisions.md` and the owner decided whether to tell the city.
- Assemblies, materials, sections, connections and tolerances are detailed for each item a builder must build.
- The construction drawings do not contradict the approved set for permitted work.
- The owner signed off. Record the date and the owner's words.

Until all of these are true, `NOT FOR CONSTRUCTION` stays on every sheet.

## Honest status

When the owner asks whether the set is ready, give the gate and the gaps.
Example answer: "Not yet. This is a design review set. Six items stand between it and a contractor set:" followed by the list.

A good rendering or a 3D model does not replace dimensioned sheets. City approval of one scope does not approve later work on the same house.

## Exit condition

- `logs/release.md` shows the current gate, its date, its evidence and its file hashes. A gate that used a CrossBeam round also shows the `package_hash`.
- The label on every sheet matches the gate in `logs/release.md`. An APPROVED set keeps the label it was approved with.
