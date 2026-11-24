# CrossBeam Feasibility Report

Write a pre-design feasibility report for a lot and a proposed project with CrossBeam: parcel facts, the city's code, state law (including law that starts later), fees, and a verdict up top with every answer tagged by its source, the questions to take to the City, and an intake checklist. For builders, designers and owners.

Version 0.2.0. Generated from the CrossBeam skill; do not edit by hand.

## Install

```
/plugin marketplace add CrossBeam-Permits/plugin
/plugin install feasibility-report@crossbeam-permits
```

The plugin adds the CrossBeam connector (`https://crossbeam-mcp.old-cherry-b095.workers.dev/mcp?mode=compact`). Sign in when your host asks. Then give the address and what
you want to build, for example "feasibility report for a 900 sq ft detached ADU at 123 Main St, Lancaster", and add
your site-visit notes and photos if you have them.

## What is in it

- `skills/feasibility-report/`: the skill (Markdown and an HTML report template, no scripts). It works for any permit: a new unit, a new
  house, an addition or remodel, a lot split or small multi-unit, a commercial tenant improvement, or anything else.
- `/feasibility-report:report`: start a report from an address and a program.

The report is preliminary: the City decides, and the report lists what to confirm with them. The skill never emails,
uploads or files anything without your approval.
