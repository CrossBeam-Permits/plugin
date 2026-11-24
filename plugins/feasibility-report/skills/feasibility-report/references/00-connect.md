# Step 0: Connect

## 1. Find the CrossBeam tools

1. Look for tools whose names start with `crossbeam_`. On a compact connection you see only `crossbeam_search` and `crossbeam_call`: call `crossbeam_search` with no arguments for the list, and run each tool through `crossbeam_call` with its name.
2. Call `crossbeam_guide` once. Note the code basis it states (code family, edition, effective date) and use it over your memory.

| Step | Tools | If it is missing |
|---|---|---|
| Site | `crossbeam_get_site_facts` | Ask `crossbeam_ask` for the parcel facts with the full address; tag what comes back `CROSSBEAM` and note "from Ask, not the parcel layers". |
| City code | `crossbeam_municipal_code` | `03-city-code.md` section 2. |
| State law | `crossbeam_lookup_code`, `crossbeam_hcd_letters` (California) | Ask `crossbeam_ask` to quote the section; tag it `CODE` only if the quote names the section and edition. |
| Requirements | `crossbeam_get_review_requirements` | Build the intake checklist from the city code and Ask; say the City's own checklist was not available. |
| Fees | `crossbeam_fees` | `05-fees.md` section 2. |
| Cross-check | `crossbeam_ask` | Skip the cross-check, and say so in the sources line. |
| Skill updates | `crossbeam_get_skill` | Use the copy you have. |

A tool your account cannot use is not in your list. Say which step it leaves thin; do not look for a way around it.

## 2. No CrossBeam tools at all

Tell the person to add the CrossBeam connector in the host's connector settings and sign in with their CrossBeam account, then start a new chat. The connector URL is `https://mcp.crossbeam-permits.com/mcp`. Do not write the report from memory while you wait.

## 3. Keep this skill current

Call `crossbeam_get_skill` with `skill_id: "feasibility-report"` and compare its `version` with `metadata.version` in this skill's `SKILL.md` frontmatter. If they differ, tell the person once and follow that result's `instructions` to update; ask before you replace any file. A host that cannot save files reads the newer `SKILL.md` and references with `path` and follows them for this report.

## 4. The header

Ask once, if you do not already know it, for the name the report goes out under (company, license number if they print one, website). Never invent a license number. If they give none, the header carries only what they gave.
