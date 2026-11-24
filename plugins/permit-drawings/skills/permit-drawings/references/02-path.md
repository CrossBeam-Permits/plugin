# Stage 2: Path

Read this after the scope is settled and before the first measurement trip.

## 1. Does the work need a permit?

1. Ask `crossbeam_ask`: "Does this scope need a building permit in <jurisdiction>? Which parts, if any, are exempt?" Give the scope statement.
2. Record the answer, the citation and the conversation ID in `logs/code-decisions.md`.
3. If part of the work needs no permit (for example, some finish carpentry), keep that part out of the permit set. Draw it separately if the owner wants drawings.
4. Ask whether other reviews apply: planning or zoning review, coastal, historic, fire hazard zone, flood zone. Planning asks "may you do this on this parcel?" Building plan check asks "is the construction safe and code-compliant?"
5. Ask whether the parcel has earlier permits that the new work touches. Record each one. A note on an approved set can apply to that application only. If CrossBeam cannot see the permit history, ask the owner once whether the owner has earlier permits or approved plans. If neither source answers, record `unknown: confirm with the city` in `logs/scope.md` and go on. It does not block any stage.

## 2. Who may prepare which parts

Each state sets who may prepare permit drawings and calculations, and who must sign them. Some states let an owner prepare drawings for some buildings. Some parts, such as engineered structural design, can need a licensed professional. The answer can depend on who prepares the plans and for whom. This skill holds no law values for this question. Ask every time.

1. Name who actually prepares the plans: the owner, a builder, a designer or another person. Name whether that person prepares them for others (for example, a builder who prepares plans for a client). Do not assume the user owns the property. Record both facts in `logs/scope.md`. Then ask `crossbeam_ask`: "In <state> and <jurisdiction>, <who> will prepare the drawings and calculations for this scope, <for their own property / for a client>. May this person prepare them? Must this person sign them? Which parts need a licensed professional? Cite the law." Give the building type, the number of storeys and the scope.
2. Ask a second question if a structural item is in scope: "Is there a prescriptive path that lets <who> show this item without engineered calculations? Cite it." For a change to an existing wall, also ask: "Is there a prescriptive path that lets the existing wall stay as it is? Cite it." Ask before you draw new bracing.
3. Record each answer in `logs/code-decisions.md` with the citation.
4. If the law requires a licensed professional for a part, first check `logs/decisions.md`. If it records that you already told the owner about that part, do not say it again. Otherwise tell the owner once. Use one or two sentences and the citation. Record that you said it in `logs/decisions.md`. Do not repeat it in later stages.
5. Keep helping. Draw everything else. If the owner wants a draft of that part for the professional, help with it, and label it as prepared for the professional's review.
6. Decide the preparer statement in `project.preparer.statement` in `project.json`. When the field is present, the kit prints it in every title block. The kit never writes it for you. The statement is optional:
   - Two sources can settle the statement: a `quoted` CrossBeam citation (`05-code-questions.md` section 3), or the city's written instruction (an email, a checklist or a counter note), cited by its source and date. Record the source in `logs/code-decisions.md` or `logs/city.md`.
   - When the law lets the person prepare the work, write a statement that cites that law. Use the `quoted` citation, or the wording of the city's written instruction.
   - When CrossBeam or the city says no statement is needed, leave the field out. Add no "Preparer statement" row to `logs/required-documents.md`.
   - When neither source settles it, do not write a statement and do not cite a law from memory. Add a row "Preparer statement" to `logs/required-documents.md` with the status `unknown: confirm with the city`. Tell the owner once, unless `logs/decisions.md` records that you already did: CrossBeam has no citation for this, and the city may ask for a statement. Leave `project.preparer.statement` out until one of the two sources settles it. This row does not block stage 7. Stage 8 resolves it: `done` when a source gives the statement, or `not required (source)` when the city says none is needed.
   - When a professional prepares part of the work, that part carries the professional's own title block. The owner's statement covers only the rest. Say which sheets it covers.

Do not offer a path that neither the city nor CrossBeam stated. Example: an agent told an owner that the city offered an "engineering stamp route". It did not. The owner caught it.

Example: a city plan checker asked for structural support for a wider door opening. The owner asked Ask AI whether a designer exhibit was allowed by law or whether an engineer was required. CrossBeam pointed to a prescriptive path. The owner drew a one-page exhibit comparing the existing and new wall lines, and the city accepted it.

## 3. Build the required-documents list

Build this list now, before the first CrossBeam check. Use `logs/required-documents.md`.

1. Ask CrossBeam for the required documents for this permit type in this jurisdiction. Call `crossbeam_get_review_requirements` with the city and the permit type ID from `logs/scope.md`. If it does not exist, ask `crossbeam_ask`. Read its `packaging_rules` now too. Some cities publish plan-set standards there: the sheets each kind of project needs, what the cover sheet and title block show, north arrows, legends, scales and sheet size. Put each one that applies to this scope in the Sheet content plan (step 5), with its source, so the set meets it as it is drawn. Stage 8 checks the package against the same rules.
2. Get the scope checklist. Call `crossbeam_get_scope_checklist` with these inputs. The call can take some seconds.
   - `scope`: the scope statement from `logs/scope.md`, as free text. It is the only required input.
   - `city`, `permit_type` (the ID from `logs/scope.md`) and `address`.
   - `facts`: each fact you already know, keyed by its `needs_facts[].id` from an earlier call, with units.
3. Read the answer:
   - Save the rows in `logs/required-documents.md`. Each row has `requirement`, `where_to_look` (where the reviewer looks on the plans) and `layer` (state or city). Stage 6 draws to these rows.
   - The tool can return `needs_facts[]`. Each item has an `id`, a `question` and `where_on_plans`. First look for the answer in the documents, at the place `where_on_plans` names. Ask the owner only the questions no document answers, following `asking-the-owner.md`.
   - Call the tool again. Put each answer in `facts` under its `id`. Do not ask an `id` again after you sent an answer for it. If the same `id` comes back, record it in `logs/questions.md` and stop calling for it.
   - If it returns `coverage: none` for this city or state, write that down. It means CrossBeam has no checklist here. It does not mean nothing is required.
   - If the tool does not exist, ask the category questions in step 4.
4. Ask the category questions. Copy `templates/category-questions.md`, fill its placeholders and ask `crossbeam_ask`. The five categories are: (a) documents that go with the plans, (b) the project data the cover sheet shows, (c) the general notes, (d) what the site plan shows, (e) the plan sheets the reviewer expects. Ask each category question unless the scope checklist rows name that category's individual items: each document, each cover-data item, each general note, each site-plan item or each plan sheet. A row that names only the category, such as "cover sheet data", does not replace the question. Also ask every question when the tool returns `coverage: none` or is missing. This skill does not list what any city requires in these categories. Only the answers do.

   If a category question gets no answer (a failed turn, an empty answer, or `rate_limited`), follow `05-code-questions.md` section 2. Record the question in `logs/code-decisions.md` at the level `waiting`, and go on. Ask it again at each stage exit and when a session resumes (section 2, step 5 there). Fill the Sheet content plan when the answer arrives.

   Example: in one replay, about a third of the CrossBeam corrections were standard documents, cover data and general notes that nobody had asked about.
5. Record the answers. Write one row per document and one row per sheet in the Documents table. Write each cover-data item, general note and site-plan item in the Sheet content plan. `templates/required-documents.md` gives both tables. Each row keeps the level of its source (`05-code-questions.md` section 3). A row at `unquoted` stays on the list, because the reviewer will look for it. Its note prints no code limit and no citation until a `quoted` or `primary-read` entry holds them.
   Also add a row for a preparer statement on the sheets when the jurisdiction asks for one (section 2, step 6).
6. Status values:
   - `needed`: nobody has started it.
   - `drafted`: you started it and it is not complete.
   - `owner to supply (<what>, by <date>)`: a source says the document is required, and only the owner can get it (an official blank form you cannot download, a product data sheet from the dealer, a document from the county). Write what the owner sends. Write the date the owner gave, or "no date" if the owner gave none.
   - `owner to sign`: complete except for the owner's signature.
   - `by others (<who>)`: a named person or firm other than you and the owner prepares it, such as an engineer or an energy consultant the owner hired.
   - `by others: not engaged (<kind of preparer>)`: a source says the document needs a preparer that you cannot be (a licensed professional, or a consultant with approved software), and nobody is engaged. First check `logs/decisions.md`. If you already told the owner about this kind of preparer for this document, do not say it again. Otherwise tell the owner once what kind of preparer the source names, with the source. Record that you said it in `logs/decisions.md`. Then keep helping (non-negotiable 11).
   - `done`, `not required (source)`.
   - `unknown: confirm with the city`: no source says whether the document is required.
   - `by city plugin (<plugin>)`: the city's own application form or a portal answer, when `logs/setup.md` names a city plugin (`00-connect.md` section 8). The plugin fills it from the city's current form. Do not fill it here. This row does not block a CrossBeam check, and stage 8 lists it in the hand-off (`city-plugin-handoff.md` section 6).
7. Choose between `owner to supply` and `unknown: confirm with the city` by one fact: does a source say the document is required (step 6)? For `unknown: confirm with the city`, ask the owner to check the city's page or call. Do not guess.
8. Stage 7 can start when no row is `needed` or `drafted`. A row that is `owner to sign`, `by others (<who>)`, `by city plugin (<plugin>)` or `unknown: confirm with the city` does not block a CrossBeam check. A row that is `owner to supply` or `by others: not engaged` blocks it unless the owner approves a CrossBeam check without that document (`07-crossbeam-check.md` section 0). Stage 8 resolves every open row before the city submittal.

## 4. Deliver the documents. Do not only list them

For every row that the owner may prepare, prepare it:

- When a city plugin is the filing step, the city's application forms and portal answers are its rows (`by city plugin (<plugin>)`). Prepare every other document here.
- Get the current official form. Use the city's or state's own page. If a direct download fails, use the host's browser tool, or give the owner the exact link.
- If no tool returns the form, the host has no web access, and you have no exact link, do not make up a link. Name the form the way CrossBeam named it and the agency that publishes it. If a source says the form is required, set the row to `owner to supply` (section 3, step 7). Ask the owner to get the blank form and send it to you. Fill it when it arrives.
- A document that needs a preparer you cannot be stays `by others (<who>)`, or `by others: not engaged (<kind>)` until the owner hires one (section 3, step 6). You may still prepare its inputs from `project.json` (areas, window sizes, equipment) so the preparer has them. Label that file as inputs for the preparer.
- Fill it from `project.json` and the logs. Every value must trace to a sheet or a source.
- Leave signatures and declarations for the owner.
- Put the file in `build/` and update the row.

Example: an agent made no energy compliance form until a CrossBeam check reported it missing. The owner said, "Don't tell me I'm missing a standardized document without giving me the document itself." The agent then found the current form and filled it.

Example: an owner asked, "Can't you do this for me? You have all the info you need. I understand it won't be signed." The agent prepared the energy form. The owner signed it.

## 5. Collect site facts

1. Ask CrossBeam for the parcel's site facts: parcel number, zoning, overlays, setbacks if relevant. Call `crossbeam_get_site_facts` with the full address. If it does not exist, ask `crossbeam_ask`.
2. Confirm the parcel number against the county assessor. Record the source.
3. If no tool has the facts, ask the owner only for facts an owner can find: the parcel number on the tax bill, which way the house faces, the year built, and what the city's or the state's public maps show. Do not ask the owner for engineering design values such as a seismic design category or a wind speed. Ask `crossbeam_ask` for them, or record them as PLACEHOLDER and ask the city.
4. Record the orientation of the lot (which way is north) with its source. A photo of the house from the street is not enough to set north.
5. Do not treat your own drawing as a source of site facts.
6. Get the values the site plan needs (category question (d) in section 3). These are usually the lot dimensions, the lot lines, and the distance from each building to each lot line. Look in the documents first: a survey, the county assessor's parcel map, a deed or title report, an earlier approved set, or the site facts. Then ask the owner once whether the owner has any of these documents. If no document gives a value, ask the owner directly for the lot dimensions and the distance from each building to each lot line. An owner's answer that is not a tape value is ASSUMED with an FV tag (`03-measure.md` section 3). Ask the owner to tape a distance only when neither a document nor the owner gives it. Record each value in `project.json` with its status and source.
7. Each value the site plan needs and nobody has given is an open item. `06-draw.md` section 3 says how the site plan shows it.

Example: an owner had the lot dimensions, but the agent never asked for them. The site plan showed only the garage and one unsurveyed side line. The plan check asked for a complete, dimensioned site plan.

## 6. Note fees

Call `crossbeam_fees` for an estimate from the city's adopted fee schedule, and give the owner its total with the schedule it names. If the tool is missing, ask `crossbeam_ask` whether CrossBeam can estimate the fees for this permit. If neither can, tell the owner that the city sets the fees at intake. Do not compute fees from memory. When a city plugin is the filing step, it handles fees. Skip this section.

## 7. Plan the set: write the sheet index

Plan the whole set before the first measurement, so the set does not stop at the architectural sheets. One test set drawn from scratch had eight clean A sheets and no structural, Title 24 or CALGreen sheet, because nobody asked for them until the end. Under "Drawing only" for a single sheet or detail, or a self-check, there is no set to plan: skip this section.

1. Copy `templates/sheet-index.md` into `logs/sheet-index.md`.
2. Read what sections 3 and 5 gathered: the Documents table, the Sheet content plan, the scope checklist rows, the `packaging_rules` and the site facts. Each sheet the Documents table or category question (e) names becomes a row in the index. The Documents table stays the record of each document's status; the index is the plan of the drawn set.
3. Write one row per sheet: number, title, discipline, what it shows, its source (a Documents row, checklist row, packaging rule or code decision), who prepares it, and the kit module it needs. Disciplines: architectural (cover, site or plot plan, existing and demolition, proposed plans, ceiling and power, elevations, sections and details), structural (framing plan, members, connections, the preliminary calc for the engineer), energy, green, electrical (a load calculation and panel schedule, when the scope adds load), and anything else the city lists. Number the sheets the way the city's packaging rules say; with none, use A, S and T prefixes.
4. Structural and energy sheets. A whole set drawn from scratch includes a structural sheet and the energy sheets: in California, the Title 24 energy sheet (with its CF1R worksheet) and the CALGreen sheet, which the `energy` module draws; elsewhere, the energy and green documents the city's list names. Take one out only when a source says this scope does not need it: a `quoted` answer, the city's document list, or the city's written instruction. Its row then reads `not required (source)`. When a part needs a licensed professional or an energy consultant, the row stays, with `by others (<who>)` or `by others: not engaged (<kind>)` (section 3, step 6); you may still prepare its inputs (section 4).
5. Forms. Check that the Documents table lists every form the set goes with (application, owner-builder declaration, CF1R, CALGreen checklist and the rest), with who fills it and who signs it. Add a missing one there, not in the index.
6. Modules. Run `python3 -m permitkit modules`. List the modules the rows need: `energy` for the California energy and green sheets, `structural` for the structural sheet, `3d` for a 3D view. 3D views are the owner's choice: offer one when a view the sheets cannot show would help the owner or the reviewer.
7. Ask the owner once, at the start of every set, following `asking-the-owner.md`. Show the sheet list with why each sheet is there and its source. Ask about the structural and energy sheets: say that a set drawn from scratch includes them, and that one comes out only when a source says the scope does not need it (step 4). Ask whether to add 3D views. Installing a module writes outside the project folder, so ask in the same message to add the missing modules, and name the files each adds (`00-connect.md` section 3). Record the answer and the owner's words in `logs/decisions.md`. If the owner wants out a sheet that a source requires, or that no source lets go, it is a constraint conflict (`01-scope.md` section 6).
8. Install each approved module (`00-connect.md` section 3) and record it in `logs/setup.md`.
9. The index drives the rest. The `sheets` list in `project.json` follows its order. Stage 6 draws each row (`06-draw.md` section 3), and stage 8 checks the package against it. When the scope changes, update the index in the same turn.

## Exit condition

- The permit need, the other reviews, and the permit type are recorded with sources.
- The preparer question is answered with a `quoted` citation or the city's written instruction, or `logs/required-documents.md` has the row "Preparer statement" at `unknown: confirm with the city` and the owner was told once. If a professional is required for a part, the owner was told once and the decision is in `logs/decisions.md`.
- `logs/required-documents.md` has a row for every document, and each row has an owner and a status. Its Sheet content plan lists the cover data, general notes and site-plan items from the category questions or the scope checklist, each with its level. A category question that Ask AI could not answer may instead be recorded as `waiting` in `logs/code-decisions.md` (`05-code-questions.md` section 2). Its items join the Sheet content plan when the answer arrives.
- `logs/sheet-index.md` lists every sheet with its source and preparer, the owner answered the structural, energy and 3D question, and each module the index needs is installed or the owner's no is in `logs/decisions.md`.
- `logs/release.md` has the line `Stage 2 done`.
