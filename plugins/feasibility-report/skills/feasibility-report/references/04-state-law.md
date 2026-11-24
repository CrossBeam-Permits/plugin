# Step 4: State law

## 1. Read the state rules for this project type

Use `crossbeam_lookup_code`:

- With a citation you already have (from the city code, Ask, or a prior answer): `code_section`, for example "Gov. Code § 66321".
- Without one: `query` with a few distinctive words plus `volume` (for example `GOV` for California's Government Code, `CRC` for the Residential Code, `CBC`, `CFC`, `CEnC`). Pass `state` for a project outside California.

Read the section text and cite it with its edition. A rule from that text is `CODE`.

The profile's **Questions** table names the state topics for this project type (for a new unit, the state ADU statute; for a tenant improvement, occupancy, accessibility and fire; for a lot split, the state housing path and its eligibility tests). For a building code question (fire separation, egress, occupancy, accessibility, energy), read the building, residential, existing building, fire or energy code section, not a summary. When the person wants drawing-ready values for elements they will draw, `crossbeam_rules` returns them with sources.

In California, also call `crossbeam_hcd_letters` with the city: a letter where HCD told this city a rule breaks state law changes the answer. HCD letters are enforcement guidance, not binding law: tag what they say `CODE` only for the statute they cite, and say "HCD letter, <date>" beside it.

## 2. Code basis

Use the editions `crossbeam_guide` or a `code_basis` field names. If a section you need is not in CrossBeam's library (the lookup returns nothing), say so, read the official text on the state's own site if your host can search (tag it `CODE` with the source and date), or make it a City question. Never cite a section number from memory.

## 3. Law that takes effect later

Builders plan months ahead. A signed bill that starts after today can change the answer for a project filed then.

1. Ask `crossbeam_ask` whether any signed law changes this project type in the next year (pass the city and state). Look in `crossbeam_lookup_code` for the new text if the library holds the future edition.
2. Report it in its own bullet, starting "From <date>:", with the bill or chapter number and the section it changes. Tag it `CODE` only if you read the chaptered text (CrossBeam, or the state legislature's own site). A law-firm or news summary is `INFERRED`, named as such.
3. Never apply future law to today's verdict. Say how it would change the answer, and if filing before or after the date matters, put that in the recommended path ("Time the filing around <date>").
4. Ask the City which date governs (application, complete application, or permit issuance) when the change is about fees or standards.

Law can be signed and still be challenged or amended before it starts. If a source says so, say so.
