# Stage 6 checks: site-visit list, sheet list, text audit

Three stage 6 procedures that `06-draw.md` sections 0, 3 and 6 point to. Run them in the normal stage path. The "Drawing only" path in `06-draw.md` says when each one does not apply.

## 1. Site-visit list

Run this once, before the first permit build. When a CrossBeam round sends you back to stage 3, run it again for new values only: values that no earlier site-visit list held. The owner's earlier choice for a value stands until the owner changes it (section 1, step 6).

A set that rests on many unmeasured values draws many corrections. Example: in one replay the owner taped only the outside of a garage. The ceiling height, the door opening, the wall thickness and the equipment stayed unmeasured, and the CrossBeam check and the city each asked for them.

1. List every value in `project.json` that is ASSUMED or PLACEHOLDER, and every open question in `logs/questions.md` that a sheet depends on.
2. For each one, count what depends on it: the entries in `logs/code-decisions.md` whose facts include it, and the rows in `logs/required-documents.md` (Documents and Sheet content plan) that need it. The sheet scripts do not exist yet, so do not count from them.
3. Rank the list. Put first the value that the most code decisions and rows depend on.
4. Turn the ranked list into one site-visit list for the owner (`asking-the-owner.md` section 2). For each item, give the physical spot, where the tape starts and ends, and the decision the number changes. Show a picture where words could confuse.
5. Tell the owner once: "These values are not measured yet. You can measure them now, or I can draw the set with field-verify tags. Each tag stays an open item on the sheets until someone measures it." `07-crossbeam-check.md` section 0 tells the owner what CrossBeam will likely flag.
6. The owner chooses: measure, or draw with FV tags. The owner may also measure some items and leave the rest. Record the choice and the owner's words in `logs/decisions.md`. The choice stands for each value until the owner changes it or measures the value.
7. If the owner measures, apply each answer as `03-measure.md` section 5 says. If the owner accepts the tags, draw. Do not ask again about these values. Do not block the owner.

## 2. Sheet list from the stage 2 checklist

1. Start from the drawing rows in `logs/required-documents.md`.
2. Draw to the checklist rows from stage 2. Each row names what a plan reviewer looks for (`requirement`) and where on the plans (`where_to_look`). Put each item where the row says. If you have no rows, use the Sheet content plan that the category questions filled in stage 2 (`02-path.md` section 3, step 4).
3. Before each CrossBeam check, go through the rows once. Mark each row with the sheet and note that answers it, or with "not shown" and why. Record the result in `logs/required-documents.md`.
4. Draw each plan sheet that the scope checklist or category question (e) named at stage 2 (`templates/category-questions.md`). When stage 3 recorded existing devices on walls the work touches, and the question (e) answer did not have them, ask question (e) again in the same conversation with the device list (`03-measure.md` section 7). Draw each sheet the answer names, with the existing devices on it. A note such as "locations not shown" does not replace a plan the reviewer expects. If the owner gave counts, ask for positions.

Then draw the sheets: `06-draw.md` section 3.

## 3. Audit the text of all sheets

Before each CrossBeam check and each city package, read the text of every sheet together and look for contradictions:

- the same element with two different sizes;
- a scope item on one sheet and missing on another;
- one topic cited under two section numbers;
- a note that says "no new" work that another sheet shows;
- one word used for two different things. Retire the ambiguous word;
- a code limit (a minimum, a maximum, a required size) that does not trace to a `quoted` or `primary-read` entry in `logs/code-decisions.md`, or whose number is not in that entry's quote. Ask `crossbeam_ask` to quote it, or remove it;
- a claim that an exception applies with no `quoted` citation or no printed arithmetic (`05-code-questions.md` section 7);
- an "or" choice ("CASEMENT OR FIXED", "BATTERY OR PLUG-IN"). Each one is an open decision. List them all. Resolve each one from `logs/decisions.md`, or print it as an owner decision ("OWNER TO SELECT: ...") and record it in `logs/questions.md`. None stays open at stage 7;
- a value or label that an owner answer changed, still printed with the old value;
- a limit from a rule with conditions, printed without its condition, or without the branch and the fact that selects it (`05-code-questions.md` section 6). Read each note in the QA list `advisory.conditional_code_notes` (`kit-qa.md`);
- an exemption or a "not required" note that rests on a fact that is not MEASURED or confirmed, or that does not address every trigger the answer named (`05-code-questions.md` section 7);
- a value, limit or exemption from a `waiting` entry in `logs/code-decisions.md`;
- a note that names a gate or a status label. The title block carries the gate. A note that repeats it goes stale at the next gate change;
- an item in the Sheet content plan that no sheet shows and that is not marked open.

Record each contradiction and its fix in `logs/decisions.md`.

Run the whole audit again, on every sheet, after any change that came back through stage 5 or changed the scope, and after every gate label change (`10-release.md`). A change on one sheet can make another sheet wrong.

Example: an owner asked the agent to "read the text you have on each page and make sure the pages are not contradictory." The audit found six contradictions.
