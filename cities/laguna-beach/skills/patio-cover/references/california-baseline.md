# California Baseline — Patio Cover

> The statewide rules for this permit. The Laguna Beach rules in `../SKILL.md` add to or override these where they differ.

## California Patio Cover — State Regulatory Decision Engine

This skill routes residential patio-cover questions through the statewide 2025
California Residential Code. Appendix BF defines the patio-cover scope and a
small set of requirements; it does not provide statewide footing, post, brace,
beam, rafter, cantilever, connection or inspection tables.

**What this covers:** State-code requirements in the cited CRC provisions.

**What this does not cover:** City setbacks, local standard-plan recipes,
utility or HOA rules, permit fees, local inspection sequences, or a
project-specific structural design. A local recipe is not a statewide rule.

### How to Use This Skill

Start with Appendix BF. Then load only the references needed for the actual
foundation, framing, roof-covering, attachment, or local-source question.

### Decision Tree Router

#### Step 1: Is the project within Appendix BF?

Appendix BF applies to a structure with open or glazed walls used for
recreational outdoor living associated with a dwelling unit. It permits attached
and detached patio covers, but not use as a carport, garage, storage room or
habitable room. See BF101.2 and BF102.1.

Do not classify an Appendix BF patio cover as a separate statewide “open
lattice” or “solid roof” structural type. Appendix BF contains no 50-percent
roof-opening or 1-1/2-inch shade-bar test and no separate 10/20 psf load rule.

#### Step 2: Check walls, openings and egress

Under BF103.1, the open or glazed area of the longer wall and one additional
wall must be at least 65 percent of the area below 6 feet 8 inches of each wall,
measured from the floor. Those openings may use:

- insect screening;
- approved translucent or transparent plastic no more than 0.125 inch thick;
- glass conforming to R324; or
- a combination of those materials.

BF103.2 separately protects required light, ventilation, emergency-escape and
exit paths. A failed BF103 condition means the proposal is outside that Appendix
BF provision; it does not by itself establish that the project is a habitable
room addition.

#### Step 3: Check height and design loads

- BF104.1 limits a patio cover to one story and no more than 12 feet in height.
- BF105.1 requires actual dead load, a vertical live load of at least 10 psf,
  higher snow load where applicable, and the minimum wind loads in R301.2.1.
- A project above 12 feet is outside Appendix BF. Route it to the applicable
  alternate code path and project-specific design documentation accepted by the
  authority having jurisdiction; do not label a nonexistent BF exception as the
  governing rule.

#### Step 4: Select the technical references

| Review question | Load these references |
|---|---|
| Appendix BF scope, use, enclosure, height or load | `appendix-bf-patio-covers.md` |
| Footing, slab support, post or decay protection | `footings-posts.md` |
| Rafter, beam, sheathing, roof covering or fire class | `roof-framing-spans.md` |
| Attached-cover load-path or wall-connection question | `ledger-attachment.md` plus the applicable approved design source |
| Full permit review | All four references, limited to the provisions that actually apply |

### State-Code Review Checklist

| # | Check | What to verify | Authority |
|---|---|---|---|
| 1 | **Use and scope** | Open or glazed walls; recreational outdoor-living use associated with a dwelling; not a carport, garage, storage room or habitable room. | CRC BF101.2, BF102.1 |
| 2 | **Enclosure walls** | The longer wall and one additional wall meet the 65-percent BF103.1 test below 6 feet 8 inches; proposed screening, plastic or glass is one of the permitted options. | CRC BF103.1 |
| 3 | **Light, ventilation and egress** | Openings serving sleeping-room emergency escape remain unenclosed; a patio structure enclosing a dwelling exit provides exits under R318. | CRC BF103.2 |
| 4 | **Height** | One story and no more than 12 feet. | CRC BF104.1 |
| 5 | **Loads** | Actual dead load, at least 10 psf vertical live load, controlling snow load and R301.2.1 wind are all included. | CRC BF105.1, R301.2.1 |
| 6 | **Foundation or slab support** | Column footings are sized from tributary load and allowable soil pressure. In a zero-frostline area, slab-only support is used only when the R506 slab is at least 3.5 inches thick and total live plus dead load is no more than 750 pounds per column. | CRC R403.1.1, BF105.2 |
| 7 | **Wood and concrete** | Load-supporting sawn lumber is grade marked; actual material weights are used; R304 decay protection and R402.2 concrete exposure requirements are applied where triggered. | CRC R301.4, R304, R402.2, R802.1 |
| 8 | **Rafters and beams** | Rafter-table selection matches span, load, spacing, species, grade, dead load and ceiling condition. Other rafter conditions route to AWC STJR; beams and framing outside a prescriptive CRC path route to R802.2/AWC NDS or accepted engineering. | CRC R802.2, R802.4.1 |
| 9 | **Connections and lateral resistance** | The approved design transfers applicable gravity, wind and uplift forces through connections to the foundation. Hardware and fasteners follow the applicable code path and listed-product instructions. | CRC BF105.1, R802.11.2 |
| 10 | **Attached-cover support** | The submitted connection has an applicable approved design source. Do not apply R507 deck-ledger schedules to a patio roof without an authority that expressly covers that use. | CRC BF105.1; project design source |
| 11 | **Roof sheathing** | Panel span rating, thickness, edge support, strength-axis orientation, continuity and load come from R803.2.2 and Table R503.2.1.1(1) or APA E30. Installation and fastening separately follow R803.2.3 and the applicable Table R602.3(1), APA E30 or approved attachment path, including table notes. | CRC R803.2.2, R803.2.3, R503.2.1.1, R602.3(1) |
| 12 | **Roof covering and slope** | The selected covering, underlayment, flashing and drainage comply with its applicable R905 section and approved manufacturer instructions. | CRC R905 |
| 13 | **Roof fire classification** | Outside an FHSZ or WUI area, new roof covering is at least Class C under R902.1.2. | CRC R902.1.2 |
| 14 | **FHSZ/WUI overlay** | A project in a Fire Hazard Severity Zone or WUI area is also routed to Part 7. Do not infer a categorical statewide ban on wood from this routing rule. | CRC R902.1.1 |
| 15 | **Local standard plan** | Any local numeric recipe passes the full provenance gate below and is labeled local rather than statewide. | Named local source |

### Corpus-Backed Quick Reference

#### Appendix BF numbers

| Subject | State-code rule | Authority |
|---|---|---|
| Wall openings | At least 65 percent of the area below 6 feet 8 inches in the longer wall and one additional wall | BF103.1 |
| Height | One story; no more than 12 feet | BF104.1 |
| Vertical live load | At least 10 psf, with higher snow load where applicable | BF105.1 |
| Slab-only support | Zero-frostline area; R506 slab at least 3.5 inches; no more than 750 pounds total live plus dead load per column | BF105.2 |

#### Common roof-covering slopes

| Covering | Minimum design slope | Additional condition | Authority |
|---|---|---|---|
| Asphalt shingles | 2:12 | From 2:12 to under 4:12, use an applicable underlayment path in Table R905.1.1(2), preserving its qualifying alternatives | R905.2.2, R905.1.1 |
| Clay or concrete tile | 2.5:12 | From 2.5:12 to under 4:12, use an applicable underlayment path in Table R905.1.1(2), preserving its qualifying alternatives | R905.3.2, R905.1.1 |
| Built-up roof | 1/4:12 | Coal-tar built-up roof may use 1/8:12 | R905.9.1 |
| Modified bitumen | 1/4:12 | Install under R905.11 and approved manufacturer instructions | R905.11.1 |

### Local-Source Retention Gate

A footing, post, brace, rafter, beam, cantilever, connection, inspection, tile,
setback or WUI recipe may be retained only as a local or external rule with all
of the following:

1. named jurisdiction, agency, manufacturer or standards publisher;
2. document, product-instruction or standard title and edition or effective date;
3. exact page, table, section or detail locator;
4. explicit geographic and project-type scope; and
5. confirmation that the source remains current.

If any element is missing, do not use the recipe as an operative requirement.
Obtain the current applicable local or external source, or use a nonnumeric
applicable-code or approved-design route.

### Output the Review Result

For each applicable checklist item, output:

- **PASS** — the submitted information demonstrates the cited requirement;
- **FAIL** — the submitted information contradicts the cited requirement;
- **FLAG** — the needed project fact, design source or provenance is missing; or
- **N/A** — the check does not apply.

### Key Principles

1. Appendix BF is a scope-and-routing provision, not a statewide standard-plan
   span book.
2. Open and glazed wall area is governed by BF103.1; Appendix BF does not ban
   conforming glass.
3. All patio covers use actual dead load, at least 10 psf vertical live load,
   controlling snow load and R301.2.1 wind.
4. Above 12 feet is outside Appendix BF, not an “engineering exception” inside
   it.
5. Useful local or external details remain useful only when the named source,
   document/product/standard title, edition or effective date, exact locator,
   geography, project scope and current-source confirmation are explicit.
