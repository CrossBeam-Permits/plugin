# Resume a session

Run these steps at the start of every session after the first.

1. Read `logs/release.md` for the last stage line and the current gate. Then read the last entries of `logs/decisions.md` and `logs/questions.md`.
2. Call `crossbeam_guide`. Pass the guide version from `logs/setup.md` in `check_version`.
3. Call `crossbeam_get_skill` with `skill_id: "permit-drawings"`. If the bundle version differs from the one in `logs/setup.md`, follow `references/00-connect.md` section 3. If the tool is missing, follow the tool map in `00-connect.md` section 4.
4. Call `crossbeam_list_conversations`. Match each open Ask AI conversation with its entry in `logs/code-decisions.md`. Read any answer that arrived after the last session with `crossbeam_get_conversation`. Ask each question still at `waiting` again (`05-code-questions.md` section 2, step 5).
5. Rebuild into a separate check folder: `python3 -m permitkit build project.json --out build-check --no-determinism`. Compare `file_sha256` in `build-check/build.json` with `file_sha256` in `build/build.json`. If they match, delete `build-check/`. If they differ, find the cause before you change anything, and record it in `logs/decisions.md`. Never rebuild over `build/` for this check.
6. Tell the owner the stage, the open questions and the next step in five lines or fewer.
