---
description: Build the permit drawing set and run the drafting kit's QA gate, then report what fails
argument-hint: "[project folder, default permit-work/]"
---

Use the permit-drawings skill. In the project folder ($ARGUMENTS, or `permit-work/` when empty), build the set and run
the kit's QA gate:

```
PYTHONPATH="${CLAUDE_PLUGIN_ROOT}/skills/permit-drawings/scripts" python3 -m permitkit build project.json
PYTHONPATH="${CLAUDE_PLUGIN_ROOT}/skills/permit-drawings/scripts" python3 -m permitkit qa build --out build/qa.json
```

Report in a few lines: pass or fail, each failed check with what to fix (`references/kit-qa.md` in the skill says
what each check means), and every rule that FAILs or WARNs. This is the free local check, not a paid CrossBeam plan
check; never start a paid check without the owner's fresh approval.
