# Source tags

Every claim in the report starts with one tag. The legend sits above the questions.

| Tag | Means | Use for | Never for |
|---|---|---|---|
| `CODE` | Law text you read this session | A statute, regulation, building code or municipal code section, with its citation and edition or "codified through" date | An Ask answer, a summary, a bill analysis, or a section you did not open |
| `CROSSBEAM` | CrossBeam data | Site facts (with the layer), a CrossBeam fee estimate (with its schedule), CrossBeam's review requirements | A rule CrossBeam merely mentioned: read the law and tag it `CODE` |
| `FIELD` | The site visit or the owner | Measurements, existing conditions, photos, the owner's stated facts, the builder's estimates | Anything the visit did not observe |
| `INFERRED` | Our reading; confirm with the City | How a rule applies to this lot, a value read off a photo or aerial, a common practice, a summary from a non-official source, a conflicting answer you set aside | A fact you could look up and did not |

Rules:

1. One tag per bullet. If a bullet needs two (a `CODE` rule applied to a `FIELD` measurement), split it, or tag the rule and say the measurement's source in words.
2. A `CODE` bullet names the section. A `CROSSBEAM` bullet names the layer or schedule.
3. Every `INFERRED` bullet that the verdict depends on has a matching City question.
4. In plain-text output (no colours), write the tag in capitals at the start of the bullet: `CODE`, `CROSSBEAM`, `FIELD`, `INFERRED`.
5. Law that starts after today keeps its tag and starts with "From <date>:".

A report written before this skill may use only `CODE` and `INFERRED`. That is fine for a reader: `CROSSBEAM` and `FIELD` split the old `CODE` bucket so a reader can tell public law from CrossBeam's data and the site visit.
