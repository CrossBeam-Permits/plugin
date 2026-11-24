# CrossBeam Permit Drawings

Draw your own building-permit plans with CrossBeam: turn sketches, tape measurements and photos into a true-scale permit drawing set, check it against your city's rules until it passes, package it the way the city wants, and answer plan-check corrections. For homeowners, owner-builders and builders.

Version 0.9.10. Generated from the CrossBeam skill; do not edit by hand.

## Install

```
/plugin marketplace add CrossBeam-Permits/plugin
/plugin install permit-drawings@crossbeam-permits
```

The plugin adds the CrossBeam connector (`https://crossbeam-mcp.old-cherry-b095.workers.dev/mcp?mode=compact`). Sign in when your host asks. Then say what you want to build, for example
"turn my garage into an ADU and draw the permit plans".

## What is in it

- `skills/permit-drawings/`: the skill and its drafting kit (Python 3, standard library only). The kit draws and
  checks the sheets on your computer and sends nothing anywhere.
- `/permit-drawings:check`: build the set and run the kit's QA gate.
- `/permit-drawings:status`: where the project stands and the next step.
- `/permit-drawings:package`: package the checked set for the city, with your approval.

The skill never signs, files, pays or sends anything without your fresh approval.
