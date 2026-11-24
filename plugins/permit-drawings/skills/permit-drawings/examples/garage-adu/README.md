# Worked example: garage to ADU

A six-sheet set that passes kit QA (a unit test rebuilds it). Values are invented: copy patterns, never numbers. Open only the script for the sheet you are drawing.

| Script | Sheet | Pattern it shows | Card |
|---|---|---|---|
| `sheets/a0_cover.py` | A-0 cover | `sh.panel` blocks: `banner` title, `table` project data from `p.meta` and `kit.text`, `sh.sheet_index`, `numbered` scope list | `kit-sheets.md` |
| `sheets/a1_site.py` | A-1 site plan | `site.property_line`, `site.footprint` (existing and new), `site.paving`, `site.centerline`, `site.street_label`, `site.utility`, `annot.north_arrow`, setback `annot.dim_chain`s, `table` and `legend` panels | `kit-site.md` |
| `sheets/a2_existing.py` | A-2 existing / demo plan | `common.shell` walls, a demo `overhead` door, `annot.room_tag`, `annot.keynote` with leaders, `annot.opening_tag`, dim chains, keynote and legend panels | `kit-plans.md` |
| `sheets/a3_proposed.py` | A-3 proposed plan | `infill`, `door`, `window`, `slider` on shell walls; new `arch.Wall` partitions with doors, a `bypass` closet; `fixtures` (tub, toilet, vanity, counter, range, sink, refrigerator); room tags with areas; `opening_schedule` panels | `kit-plans.md` |
| `sheets/a4_elev.py` | A-4 four elevations | `section.siding`, `roof_profile` (gable end) and `roof_eave` (eave side), `arch.elev_door` / `elev_window`, `section.grade`, `pitch_symbol`, `level_marker`, opening tags | `kit-elevations-sections.md` |
| `sheets/a5_section.py` | A-5 building section | `"fit"` scale, `section.concrete` slab and footings, `earth`, `insulation`, `wood_cut`, roof profile, level markers, `annot.leader` notes | `kit-elevations-sections.md` |
| `sheets/common.py` | (shared) | Plan scale, `arch.Shell`, extents; A-2 and A-3 `import common` | `kit-plans.md` |

`project.json` shows `values` with statuses and sources, `walls` with `action`, `openings`, a closing `chains` entry and the `sheets` list (`references/project-file.md`). It has no ASSUMED value, so `field_verify` is empty.
