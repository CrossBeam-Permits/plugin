# project.json: revisions and optional blocks

Topic card for `project-file.md`. Each block below `revisions` is optional and has its own reference with the fields. Read the block's reference only when the project needs it.

## Revisions

`revisions` lists `{delta, date, desc, sheets}`. Every revision cloud on a sheet must name a listed `delta`. `sheets` is an optional list of the sheet ids that the revision changes. It is a record for the plan checker and for you; QA does not check it.

Clouds are for the city only. Stage 9 (`09-city-corrections.md`) adds a revision for each round of city corrections, and only a city round adds one. Before the city has reviewed the set (stages 4 to 8, including every CrossBeam round), `revisions` stays empty and no sheet carries a cloud or a delta: you change the drawing and rebuild a clean set. A CrossBeam round is not a city round.

## Energy and green blocks

`energy` records the Title 24 Part 6 facts of a single-family addition or alteration: `building`, `work`, `zip`, `climate_zone` (a Value reference), `path`, `path_reason`, `cd`, and the lists `addition`, `house`, `fenestration`, `doors`, `insulation`, `ducts`, `hvac`, `water_heating` and `lighting`. `green` records the CALGreen 301.1.1 `trigger` and the drafter's `measures` and `local` decisions. Both are optional. `references/energy-and-green.md` gives the fields, an example and what each one selects; `schemas/project.schema.json` (`Energy`, `Green`) has the full list.

A value read from a table, such as the climate zone from the Energy Commission's ZIP list, is DERIVED with a `source` and no `expr`.

## Structure

The optional `structure` block holds the design criteria (snow, wind, seismic category), the framing members (header, beam, joist, rafter, ceiling joist, post, footing) and their spans, spacings, sizes, species, grades and loads, and the preliminary calc inputs. Its checks join `rules` at load as `STRUCT-*` rules (`project-rules.md`). `structural.md` gives the fields.

## 3D model

The optional `model3d` block holds the elements (walls, slabs, roofs, cabinets and their openings), materials and cameras that the kit's printed 3D views draw. Its geometry is `$key` refs or inline Values, like the rest of the file. `3d-views.md` gives the fields.

## Connections

`connections` lists the connections that carry a load the kit does not size: `{id, what, load, cd, basis, evidence}`. `basis` is `open`, `manufacturer` (the maker's tested detail, with its evaluation report and rated load) or `engineer` (an engineer's calculation); a settled basis needs `evidence`, and a `load` needs the `cd` it comes from. `sh.connection(id, cell)` prints the entry on a sheet. `kit-elevations-sections.md`, "Connections that carry a load", gives the steps.

## Images and finishes

- `images` lists the raster images that sheets place by id: `{id, path, kind, source, date}`, with `kind` one of `photo`, `concept`, `aerial`, `product`. `source` prints under every image. An aerial also takes `north_deg` and `site_px`.
- `finishes` is the finish and color schedule: `{id, location, item, material, color_name, rgb, manufacturer, product, finish, status, image}`, with `status` `SELECTED`, `PROPOSED` or `TBD`. Text fields are note templates, so a size prints from a Value.

`images-and-finishes.md` gives both blocks, the concept guard and `finishes.rgb(project, id)` for other modules.
