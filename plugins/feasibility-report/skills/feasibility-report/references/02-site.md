# Step 2: Site facts

## 1. Look up the parcel

Call `crossbeam_get_site_facts` with the full address (or `apn`, with the city in `address`). Keep the source each fact names: it goes in the site-facts table in grey after the fact.

Pull these into the report when the result has them:

| Row | Facts |
|---|---|
| APN / lot | APN, lot area, rough dimensions, slope |
| Zoning | Zone and its source. If the source is a statewide or regional layer rather than the city's live zoning map, say "approximate" and add "confirm the zone" to the City questions |
| Coastal / fire | Coastal zone, fire hazard severity zone, WUI |
| Flood / seismic | FEMA flood zone, other floodplain layers, liquefaction or landslide zones, fault zones, soils |
| Energy / utilities | Climate zone, electric utility, water and sewer provider |
| Transit | Nearest stops, distance and how it was measured (straight line or walking), whether any is a major transit stop |
| Historic / other overlays | Any district or overlay the result lists |

Every fact here is tagged `CROSSBEAM` in the questions section, with its layer named, unless you also read the law that makes it matter (then the rule is `CODE` and the fact stays `CROSSBEAM`).

## 2. Settle the parcel when in doubt

Most addresses are not in doubt. Check only when something conflicts: two street numbers in the sources, a result that says the parcel was not confirmed, a lot size far from what the person described, or an APN that differs from a document.

1. Run `crossbeam_get_site_facts` once for each candidate address.
2. Compare APN, lot area and zoning. If the conclusions hold for both lots, say so in an "Address check" box under the summary and use the address the person gave.
3. If they differ in a way that changes the verdict, stop and ask which lot it is before you write.
4. "Parcel not confirmed" means the facts are for a point, not a lot. Ask for the APN. Never fill in a neighbor's facts.

## 3. The aerial image

If the site-facts result carries an aerial or satellite image (or a link to one), put it in the report beside the site-facts table with its source and date, and use it to read rough lot shape, existing structures, trees and access. Anything you read off the image is `INFERRED` and needs a survey or a site visit to confirm. If there is no image, leave the slot out; never draw or describe one you did not get.

## 4. Permit history

Call `crossbeam_permit_status` with the address (and `city`). It returns the City's public permit and planning records where CrossBeam reads that city.

- An open permit or a live approval at the address means the project may be a revision of that filing, not a new one: say so in the summary and the City questions.
- Earlier permits tell you what is legal today: an existing room, garage conversion or tenant space with no permit behind it is a risk to rank (`06-synthesize.md` section 5). Tag what the records show `CROSSBEAM`, with the record number and date.
- Open code-enforcement cases, expired permits and holds are risks too.

## 5. When there are no permit records

If the tool has no records for this city, say "CrossBeam does not have <city>'s permit records" in the sources, ask the person whether the owner knows of earlier permits or unpermitted work (put the answer in as `FIELD`), and add "permit history for the address" to the City questions.

## 6. What site facts cannot tell you

Easements, the exact house footprint, setbacks as built, utility locations and soils depth need a title report, a survey, a soils report or the site visit. List each one the project turns on under the intake checklist as an owner-paid item.
