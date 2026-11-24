# City plugin hand-off

Read this when `logs/setup.md` names a city plugin (`00-connect.md` section 8), at stage 8 before you build the bundle, and at stage 9 when a `city_documents` bundle arrives.

A city plugin is a separate skill that files permits with one city. It knows the city's application forms, its portal and its upload categories. This skill knows the drawings. The two pass work through two bundles, so neither does the other's job and the owner is not asked the same thing twice.

The Laguna Beach plugin (`laguna-beach`, skill `laguna-permit-preparer`) is the first plugin that follows this contract. Any city plugin that follows it works the same way.

The schema is `schemas/city-plugin-handoff.schema.json`. A city plugin ships a byte-identical copy. Check a bundle with:

```
PYTHONPATH=<skill>/scripts python3 -c "import json,sys; from permitkit import schema; s=json.load(open('<skill>/schemas/city-plugin-handoff.schema.json')); e=schema.validate(json.load(open(sys.argv[1])), s); print('\n'.join(e) or 'valid')" <bundle.json>
```

## 1. The two bundles

| Bundle | `kind` | Written by | Where | Read by |
|---|---|---|---|---|
| Drawn set | `drawn_set` | this skill, stage 8 (city round 0) or stage 9 (city round 1 and later) | `permit-work/package/round-<n>/handoff/handoff.json` | the city plugin |
| City documents | `city_documents` | the city plugin, after filing | `permit-work/input/city/after-round-<n>/city-documents.json` | this skill, stage 9 |

`<n>` in the drawn-set folder is the city round of that bundle. `<n>` in the city-documents folder is the city round the city answered. Comments on city round 0 start city round 1.

Paths inside a bundle are relative to the folder that holds the bundle file. A path that names another bundle (`corrections_answered.city_documents`, `original_submittal.drawn_set`) is relative to `permit-work/`.

## 2. One project folder

Both skills work in the owner's one `permit-work/` folder.

- This skill writes only its own folders: `sources/`, `project.json`, `sheets/`, `build/`, `package/`, `history/`, `questions/`, and its own files in `logs/`.
- The city plugin writes only its own folders, for example `input/`, `state/` and `output/`. Never write in them. Read them as evidence: a file in the plugin's `input/` is an original the owner gave. Copy it into `sources/` like any other original.
- Each skill writes only its own files in `logs/`. This skill's log files are the ones `working-folder.md` lists.

## 3. The drawn-set bundle

The bundle folder holds `handoff.json`, a copy of `project.json`, and every file the city gets from this skill. Every file is final for this city round. Never change a file after its hash is in the bundle. A change makes a new bundle.

| Field | What it holds | Where it comes from |
|---|---|---|
| `producer` | `permit-drawings`, the skill bundle version, the kit version | `logs/setup.md`, `build/build.json` |
| `consumer` | The city plugin's name and version | `logs/setup.md` |
| `city` | Name, state, the plugin's jurisdiction id, the source | `logs/scope.md`, the plugin |
| `city_round`, `gate`, `status_label` | The city round; always `PERMIT REVIEW`; the printed label | `logs/release.md`, `project.json` |
| `plan_set` | The drawing file the city gets: path, SHA-256, pages, sheet size, sheet ids, `unlocked: true`, `kit_qa_pass: true` | `build/build.json`, `build/qa.json` |
| `project_file` | The copy of `project.json` and its SHA-256 | the copy in the bundle |
| `files` | Every file in the bundle except `project.json` and `handoff.json`, the plan set included. Each has a role, its contents, its hash, its pages, the required-documents row it closes, the packaging rule source, for a resubmittal the earlier upload it `replaces`, and `upload` (whether the plugin uploads it in this city round) | the stage 8 manifest |
| `facts` | Facts the plugin's forms and portal need, each with its value, status and source (section 4) | `project.json`, `logs/scope.md`, other logs |
| `required_documents` | Every row of the Documents table, word for word | `logs/required-documents.md` |
| `open_items` | Every item still open (section 5) | `logs/decisions.md`, `logs/required-documents.md`, `logs/scope.md` |
| `approvals_done` | Each approval this skill already got, with its log entry (section 6) | the logs |
| `left_to_plugin` | What this skill did not do and leaves to the plugin | fixed list in section 6 |
| `crossbeam` | The CrossBeam project id, the passing CrossBeam round and its `package_hash` (or `none (web path)`) | `logs/crossbeam-rounds.md` |
| `corrections_answered` | `null` for city round 0. For a resubmittal: the city round answered, the `city_documents` bundle path and the response sheet path | stage 9 |
| `comments_for_plugin` | City comments about the application, the portal or fees, each with the change the plugin will make | stage 9 |

## 4. Facts

Each fact has an `id`, a `value`, a `status` and a `source`. The source is the file and the place in it (`project.json` and `project.address`, or `logs/scope.md` and the row). The plugin records that provenance, for example "permit-drawings project.json".

Statuses:

- The six `project.json` statuses keep their meaning (`project-file.md`).
- `DOCUMENT`: read from a document in `sources/` (a tax bill, a deed, a survey).
- `OWNER_ANSWER`: the owner's answer, recorded in `logs/questions.md`.
- `SITE_FACTS`: from `crossbeam_get_site_facts` or another cited site-facts source.
- `CROSSBEAM`: from a CrossBeam answer with its citation.
- `UNKNOWN`: no source gives it.

Rules:

1. An unknown value is `null`, with status `PLACEHOLDER` or `UNKNOWN` and a `null_reason`. Never fill it to make a form complete.
2. An `ASSUMED` value carries its FV tag in `fv`.
3. Set `applicant_controlled: true` on a fact only the owner can assert: the property owner, the builder (owner-builder or contractor), the contractor's licence, and the valuation. The plugin confirms these with the owner before it uses them. Send the value you have, so the owner confirms it and does not retype it.
4. Send no valuation you computed. Send `valuation.owner_stated` only when the owner gave a value, with its source. Otherwise send it as `null`. Areas from `project.json` are inputs the owner may use to state a valuation. They are not a valuation.
5. Send each value once. Do not send a second copy of a value under another id.

Use these ids when the fact exists. Add other facts under clear ids. The plugin maps ids to its own fields by reading what each fact means, not by its name.

| Id | Typical source |
|---|---|
| `site.address` | `project.json` `project.address` |
| `site.apn`, `site.legal_description`, `site.zoning` | site facts or a document |
| `owner.name` | `project.json` `project.owner` (applicant controlled) |
| `owner.mailing_address` | a document or the owner's answer (applicant controlled) |
| `preparer.name`, `preparer.role`, `preparer.statement` | `project.json` `project.preparer` |
| `project.title` | `project.json` `project.title` |
| `project.scope_statement` | `logs/scope.md`, word for word |
| `project.permit_type` | `logs/scope.md`; the drawing side's permit type, not the filing route |
| `project.code_basis` | the top of `logs/code-decisions.md` |
| `building.occupancy_group`, `building.construction_type` | a `quoted` CrossBeam answer or a document |
| `area.<name>` | an area value in `project.json` (`unit: sf`), named for what it measures |
| `builder.kind`, `contractor.name`, `contractor.license_number` | `logs/scope.md` or the owner's answer (applicant controlled) |
| `valuation.owner_stated` | the owner's answer (applicant controlled), or `null` |

## 5. Open items

List every item still open when you write the bundle.

- **Items printed open on the sheets** (`changes_sheets: true`): a value drawn with an FV tag, a deferred decision, a `waiting` code question, a Sheet content plan row at `open`. Stage 7 section 8 already asked the owner to resolve each one or send it open. The bundle records the owner's words and the log entry. The schema refuses such an item without them.
- **Items that do not change the sheets** (`changes_sheets: false`): a document row still open, an `unknown: confirm with the city` in the manifest or in `logs/scope.md`, the preparer statement row. In plugin mode this skill does not ask the stage 8 send question. Leave `owner_decision.status: pending`. The plugin shows these items in its pre-submit manifest and names them in its one submit question.

## 6. Who asks the owner for which approval

Each approval is asked once, by one side.

| Approval | Asked by | When |
|---|---|---|
| Save this skill's files outside the project folder | The side that fetched them. When the plugin fetched them, this skill does not ask again | Before writing them |
| CrossBeam check price, and a check with open items | This skill | Stage 7, each CrossBeam round |
| Resolve or send open each item that changes the sheets | This skill | Stage 7 section 8 |
| Signature, or a signature image, on a document this skill prepared (sheets, energy forms, response sheet) | This skill | Stage 8 section 4, stage 9; before the hash goes in the bundle |
| Filing route: which applications and records | The plugin | Before it fills a form |
| Confirm applicant-controlled facts (owner, builder, licence, valuation) | The plugin | In its question batches |
| Signatures on the city's application forms and the portal attestation | The plugin; the owner signs personally | Before upload |
| Send with the open document items, and the final submit | The plugin, in one question | Immediately before submit |
| Resubmit into the existing record | The plugin | Immediately before resubmit |
| Payment and appointments | The plugin | Each one separately |

`approvals_done` lists each approval this skill got, with its log entry. `left_to_plugin` lists what the plugin does: `filing_route`, `city_application_forms`, `applicant_fact_confirmations`, `valuation`, `fees`, `city_signatures`, `open_items_send_approval`, `portal_upload`, `final_submit`, `payment`, `after_filing_downloads`.

## 7. What the plugin does with the drawn set

This is the contract the plugin follows. You do not do these steps.

1. Validate `handoff.json` against the schema. Check every file's SHA-256 and size, the plan set's page count, and that the plan set opens without a password.
2. Refuse a bundle for another jurisdiction, or one whose gate is not `PERMIT REVIEW`.
3. Copy the files into its own input folder unchanged. Upload the plan set byte for byte. If one of its tools must rewrite a file, it records both hashes and checks the pages.
4. Record each fact with its provenance. Keep unknowns null. Confirm applicant-controlled facts with the owner.
5. Build its own filing route, forms and portal answers. Compare the application's description with the scope statement and the sheets. A difference stops the filing and comes back to this skill.
6. After filing, write its receipt. When the city returns documents, write a `city_documents` bundle.

## 8. The city-documents bundle

The plugin downloads what the city sends after filing, through the owner's signed-in session. It writes the files and `city-documents.json`:

| Field | What it holds |
|---|---|
| `outcome` | `corrections`, `approved` or `other_notice` |
| `answers_city_round` | The city round the city answered |
| `record` | The plugin's record id, the city's record number, the portal type, the status exactly as the portal shows it |
| `city_round_marker` | A round marker the city put on its files, copied exactly. Evidence only |
| `documents` | Each file: path, kind (letter, comment list, red-marked set, resubmittal form, email body, approval, portal status, other), SHA-256, size, pages, where it came from, when |
| `instructions_seen` | Each packaging instruction the plugin saw, with its source |
| `original_submittal` | The drawn-set bundle that was filed, and each file the plugin uploaded with its city category and hash |
| `due_date` | Only a date the city states |

Stage 9 reads this bundle (`09-city-corrections.md` section 1). On `approved`, read `10-release.md` and set the gate APPROVED from the approval document.

## 9. Version

The schema id is `crossbeam.permit-drawings-handoff/1`. A change that a reader of version 1 cannot read gets a new id. The plugin refuses an id it does not know. When this file and the schema change, the plugin's copy changes in the same release.
