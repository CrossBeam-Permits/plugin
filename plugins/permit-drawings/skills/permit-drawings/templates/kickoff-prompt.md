# Kickoff prompt (the owner's first message)

Give this template to the owner when the owner asks how to start. Fill the brackets in plain words. A rough list is fine.

```text
I need a permit in <city>, <state> for work on my <house / unit / building>.
<My contractor / the city / my lender> asked for drawings of what exists now and what will change.

The changes:
1. <one change per line, in plain words — for example, "replace the sliding door with a 32-inch door">
2. <...>
3. <...>

I can take tape measurements and photos, and I will send you my sketches.
Use the permit-drawings skill and the CrossBeam connector.
<Optional: who will build it — me as owner-builder, or a contractor.>
```

## What the agent does with it

1. Starts stage 0 (`references/00-connect.md`).
2. Creates the `permit-work/` folder and copies every file the owner sent into `sources/`.
3. Asks only for a missing part of this template. It does not send a form.
4. Replies with the first ranked tape checklist after stage 2, not before.

## Later prompts that worked

Owners can use these at any stage:

- "What's left outstanding? Explain what you need from me."
- "Use the question tool to ask me what you need."
- "Read the text on every page and make sure the pages do not contradict each other."
- "Use vision to check every page for overlap or cut-off text. Do not cut corners."
- "Tell me where in the plans this is true."
