# Stage 0: Connect

Read this at the first session on a project, or when the owner moves to a new host.

## 1. Create the working folder

Do this first. Every later step writes a log in this folder.

In Cowork, put `permit-work/` in a folder the owner connected, never in the task's own working space: a cloud task deletes its own files when it ends. If no folder is connected, ask the owner to connect one before you write anything.

1. Create the `permit-work/` tree that `working-folder.md` shows (read its folder rules once), inside the owner's project folder. If a city plugin already made `permit-work/` (it has folders such as `input/`, `state/` and `output/`), keep them and add this skill's folders beside them. Never write in the plugin's folders (`city-plugin-handoff.md` section 2).
2. Copy every file the owner gave you into `sources/`. This includes the originals in a city plugin's `input/` folder. A city plugin's fact file (for example `state/project-facts.json`) is evidence: use a fact from it only with the source it records. Save the owner's first message as `sources/owner-first-message.md`. It is the source for the facts it states, such as the address and the scope words, and it is the only source when the owner sent no files.
3. Start `logs/release.md` with the gate `REVIEW` and today's date. Stage 0 sets the first gate.
4. Start `logs/setup.md` with today's date and the host name. Sections 2 to 4 add to it.

## 2. Connect CrossBeam

1. Check your tool list for tools whose names start with `crossbeam_`.
2. If none exist, tell the owner to add the CrossBeam connector in the host's connector settings and sign in. The recommended connector URL is `https://mcp.crossbeam-permits.com/mcp?mode=compact`: it shows two tools, `crossbeam_search` (lists the CrossBeam tools and returns one's schema) and `crossbeam_call` (runs one by name), and keeps the host's context small while every tool stays reachable. When this skill names a tool such as `crossbeam_rules`, call it through `crossbeam_call` with `name` set to it; call `crossbeam_search` with `names` first when you need its arguments. The plain `/mcp` URL shows every tool directly; either works. Most hosts need a new session after the owner adds a connector. Tell the owner to start one and to say "Continue the permit drawings."
3. If some tools exist and others do not, do not wait for the missing ones. Section 4 gives a fallback for each capability. Leave stage 0 only when Ask AI works (as a tool, or through the owner in the web app) and each other capability has a tool or a recorded fallback.
4. Call `crossbeam_guide`. If `logs/setup.md` records a guide version, pass it in `check_version`.
5. Read the guide. Record the guide version and the code basis it returns in `logs/setup.md`.

## 3. Keep this skill current

This skill comes from CrossBeam. Its files and the CrossBeam tools change together.

1. Call `crossbeam_get_skill` with `skill_id: "permit-drawings"`. The first page gives the bundle version, every file with its SHA-256 digest and its module, and `archive`: a signed one-hour link to the core files as one `.tar.gz`. You need only that first page to compare versions.
2. Compare the bundle version with the one in `logs/setup.md`. If they match, use the files you have.
3. If they differ, ask the owner before you write anything. The skill files live outside the project folder. Name the folder: the folder the host loaded this skill from (in Claude Code, for example, `~/.claude/skills/permit-drawings/` or `.claude/skills/permit-drawings/` in the project). Tell the owner the old version, the new version and the number of files that change.
4. Write the new files only after a clear yes. When the host runs shell commands, install in one step: in a new, empty temporary folder, run the `archive.install` commands. They download the archive, check its digest and unpack it into a `permit-drawings/` folder. Check the unpacked files against `files[]`, then replace the old skill folder with the new one, so no file the new version dropped stays behind. Without a shell, page through the files with `next_cursor`; a large file can arrive in parts that you join in `offset` order before you check it. Either way, check each file against its digest. Record the new version in `logs/setup.md`. If the owner says no, keep the old files and record that.
   Optional modules. A plain install is the core files. The energy (Title 24 and CALGreen sheets), structural and 3D modules (`modules[]` in the result) are separate downloads. Do not wait for the kit to ask for one: at the start of every set, the sheet index decides which the set needs (`02-path.md` section 7), and a set drawn from scratch includes structural and, in California, energy. `python3 -m permitkit modules` shows which are installed, and the kit names the module when a block or command needs a missing one. To add one, call `crossbeam_get_skill` again with `module` set (for example `"module": "structural"`) and install it the same way, in the folder that holds the `permit-drawings/` folder, so its files land inside it. When you update the skill, fetch each module `logs/setup.md` lists into the same new folder before you swap folders. Record the installed modules in `logs/setup.md`. Adding a module writes outside the project folder: ask the owner first, as for any skill update, and name the files it adds.
5. The skill includes the drafting kit (Python scripts). The host can ask the owner to approve running them. Tell the owner the scripts draw and check the sheets on this computer and send nothing anywhere.
6. When this host loads skills only from the owner's Claude account, not from a folder you can write (Cowork and claude.ai chat do), steps 1 to 4 do not apply. When the versions differ, give the owner `upload.url` and `upload.how` from the `crossbeam_get_skill` result, as written. It is the CrossBeam Permit Drawings plugin: this skill with every module, the CrossBeam connector and the `/permit-drawings:` commands. If an older copy still shows under Customize > Plugins or Customize > Skills, they remove it. Record the version they installed in `logs/setup.md`. Until then, keep working with the copy you have.
7. If the host loads skills from CrossBeam directly, or the skill came with the CrossBeam permit-drawings plugin from a plugin marketplace (the marketplace updates it, with every module included), the host keeps it current. Skip steps 1 to 4.
8. If a city plugin fetched these files with `crossbeam_get_skill` and the owner approved saving them, that approval covers this bundle version. Do not ask again. Record "saved by <plugin>, owner approved <date>" in `logs/setup.md`.

## 4. Map the tools by capability

Find each tool by its name first. On a compact connection (only `crossbeam_search` and `crossbeam_call`), call `crossbeam_search` with no arguments for the list; a tool it lists counts as found, and you run it through `crossbeam_call`. If a name is missing, read the tool descriptions for the same capability. The names below are the current ones.
Record the table you found, with the fallback for each missing row, in `logs/setup.md`.

| Capability | Tools | If it is missing |
|---|---|---|
| Code basis and guide version | `crossbeam_guide` | Ask AI the code-basis question in section 6, step 2. Record the guide version as "none". |
| Read check results | `crossbeam_list_projects`, `crossbeam_get_project_summary`, `crossbeam_get_findings`, `crossbeam_get_finding_detail`, `crossbeam_get_sheet_annotations`, `crossbeam_search_findings` | Needed from stage 7 section 5 (reading results) and in stage 9. Stages 1 to 6 do not use it. Record the gap and keep working. Fix the connection before you read the first CrossBeam round. |
| Read the drafted response letter after a corrections check | `crossbeam_get_corrections_letter` | The owner copies the letter from the CrossBeam web app. |
| Ask AI (open questions, saved conversation) | `crossbeam_ask`, `crossbeam_get_conversation`, `crossbeam_list_conversations` | The owner asks the question in the CrossBeam web app's **Chat** page and pastes the answer and the conversation link to you. If a channel gives no conversation ID or link, save each answer word for word in `sources/askai/` (`05-code-questions.md` section 3). |
| Rules for what you draw (limits per element, with `kit_checks` for the kit QA) | `crossbeam_rules` | Ask AI the element list in one numbered question (`05-code-questions.md` section 0). Write the `rules` entries in `project.json` yourself from each `quoted` limit. |
| Primary code text (a code section, statute or regulation; a city's own code by chapter) | `crossbeam_lookup_code`, `crossbeam_municipal_code` | Ask AI to quote the section (`05-code-questions.md` section 3), or read it in a document the owner gives you. |
| Permit fee estimate | `crossbeam_fees` | Ask AI (`02-path.md` section 6). |
| Review requirements and city packaging rules | `crossbeam_get_review_requirements` (required documents, `packaging_rules`) | Ask AI. If Ask AI has no answer, the owner checks the city's page or calls the city. |
| Scope checklist (what a reviewer looks for, and where) | `crossbeam_get_scope_checklist` | Ask AI the category questions (`02-path.md` section 3, step 4). |
| Skill files and version | `crossbeam_get_skill` | Use the copy you have. In your next message to the owner, say once that this copy may be out of date. Record in `logs/setup.md` that you said it. |
| Site facts (parcel, zoning, overlays, climate zone) | `crossbeam_get_site_facts` | Ask AI with the full address. |
| Start a check | `crossbeam_create_review_draft`, `crossbeam_validate_review_draft`, `crossbeam_submit_review`, `crossbeam_start_resubmittal` | The owner uploads the set PDF in the CrossBeam web app and starts the check. |
| Review status | `crossbeam_get_review_status`, or a task notification from the submit call | The owner waits for the CrossBeam completion email and tells you. |

A fallback is a normal path. Record which path you used for each question and each check.

`crossbeam_ask` can return two errors: `rate_limited` (with `resets_at`) and `turn_in_progress`. Neither means the tool is missing. `05-code-questions.md` section 2 says how to handle each.

## 5. Find the jurisdiction and the state

1. Get the property address from the owner's first message or from the documents. Do not ask for it again if a document already has it. If no message or document has it, ask the owner for it (`asking-the-owner.md`).
2. Ask `crossbeam_ask` which agency issues building permits at that address. The mailing city can differ from the permitting agency. A county can issue permits for unincorporated land.
3. Record the jurisdiction and the state in `logs/scope.md` with the source.
4. Ask `crossbeam_ask` whether CrossBeam covers this jurisdiction. If it does not, tell the owner once. Code answers then come from the adopted primary text that you find and read. Each such entry is `primary-read` when you record the source URL and the edition (`05-code-questions.md` section 3). Mark each one "not checked by CrossBeam" in `logs/code-decisions.md`.

## 6. Adopt the code basis

1. Read the code basis from the `crossbeam_guide` answer: code family, edition, effective date.
2. Ask `crossbeam_ask` only for what the guide did not return. Local amendments are usually missing. Ask: "Which local amendments to <code family, edition> apply to a permit filed today in <jurisdiction, state>?" If the guide returned no code basis, ask: "Which building codes, editions and effective dates apply to a permit filed today in <jurisdiction, state>? Which local amendments apply?"
3. Write the code basis at the top of `logs/code-decisions.md`: code family, edition, effective date, local amendments, the source of each, date asked.
4. Treat this code basis as the authority for the session. Your memory may hold an older edition.
5. If the owner's application date or jurisdiction changes, ask again. Do not carry an old answer to a new jurisdiction.

Findings tools later return a `code_basis` block. Stage 7 compares it with this entry.

### The "prove it to yourself" rule

When a CrossBeam citation conflicts with your memory:

1. Assume your memory is out of date. Section numbers change between editions.
2. Do not refuse the change and do not argue with the owner.
3. Read the quote that CrossBeam gives for the citation in `citations[]`. If the citation has no quote, ask `crossbeam_ask`, in the same conversation, to quote the section in the stated edition. A citation is `quoted` when the answer gives the section, the edition and the verbatim text, and the text holds the limit (`05-code-questions.md` section 3).
4. If you can reach the primary text (a tool, the host's browser, or a document the owner gave), read it too. Then the entry is also `primary-read`.
5. If the quote or the primary text supports CrossBeam, adopt it and note it in `logs/code-decisions.md`.
6. If the primary text you read does not support CrossBeam, record the conflict in `logs/disputes.md` with the quoted text. Then tell the owner in two sentences.

If no source gives you the primary text, follow `05-code-questions.md` section 4.

Example: an agent refused correct current-edition section numbers for most of an hour because its memory held the previous edition. The owner fixed it with one instruction: "CrossBeam is the source of truth; prove it to yourself." After the agent checked the primary text, the work went fast.

## 7. Prepare the host to run the kit

1. Confirm that the host can run Python 3. Run `python3 --version`. The kit uses the standard library only.
2. Some hosts ask the owner to approve each script. Tell the owner why the kit needs to run before you run it the first time.
3. Record the Python version in `logs/setup.md`.

## 8. Find the city's filing step

Some cities have a city plugin: a separate skill that fills the city's application forms and files through the city's portal. When one is installed for this jurisdiction, it is the filing step. Stage 8 then hands the set to it instead of sending it to the city, and stage 9 accepts the city's documents from it. `city-plugin-handoff.md` is the contract.

1. Read the descriptions of the skills the host has loaded. Look for a skill that prepares and files permit applications for this jurisdiction and accepts a permit-drawings hand-off bundle. Decide from what the skill says it does, not from its name. The Laguna Beach plugin (skill `laguna-permit-preparer`) is the first one.
2. If the owner started this skill from a city plugin, that plugin is the filing step. Do not ask again.
3. If you found a plugin and the owner did not start from it, tell the owner once: "The <city> plugin can file this set with the city when the drawings are ready. I will hand the set to it at the end." Record the answer in `logs/decisions.md`. If the owner wants to file another way, record "City plugin: none (owner's choice)".
4. Record in `logs/setup.md`: "City plugin: <name> <version>, jurisdiction id <id>", or "City plugin: none".
5. If no plugin exists, stage 8 sends the package as it says. Nothing else changes.

## Exit condition

- The folder exists, and every original file is in `sources/`.
- `logs/setup.md` names the city plugin, or says "City plugin: none" (section 8).
- Ask AI works, as a tool or through the owner. Each other capability in section 4 has a tool or a recorded fallback. `logs/setup.md` has the skill bundle version, the guide version and the tool map.
- The code basis and its source are at the top of `logs/code-decisions.md`.
- The jurisdiction and state are in `logs/scope.md`.
- `logs/release.md` has the gate `REVIEW` and the line `Stage 0 done`.
