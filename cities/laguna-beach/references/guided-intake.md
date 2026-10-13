# Guided intake

Build one provenance-bearing fact table for Planning forms, Building forms, portal answers, routing, and attachment rules. Ask progressively; do not reproduce the City's entire application as chat questions.

## First exchange

Ask for:

1. Laguna Beach property address.
2. Plain-language description of all proposed work, including demolition, grading, pool/spa, ADU/JADU, utilities, reroof, and equipment.
3. Current stage: exploring, preparing Planning, Planning submitted, Planning approved/effective, preparing Building, correction/resubmittal, or permit issuance.
4. Available files: plans, surveys, title report, prior approvals, correction letters, calculations/studies, applications, and contractor materials.

Inventory first. Extract facts before asking the user to retype them.

## Fact contract

Every entry in `project-facts.json.facts` contains:

- stable canonical `id`;
- `value` or null;
- `source.kind`: `user_confirmed`, `plan`, `application`, `title_report`, `site_facts`, or `portal`;
- a receipt with file/page/sheet/field or user-answer timestamp;
- confidence from 0 to 1;
- whether applicant confirmation is required and, if so, its state;
- downstream consumers.

Use `site.address`, `project.description`, `project.stage`, `owner.*`, `applicant.*`, `contractor.*`, `designer.*`, `project.valuation.<record-id>`, and scoped plan facts such as `zoning.lot_area.existing`.

## Question batches

After extracting documents, present short batches in this order:

1. Identity and roles: owner, applicant, authorized agent, contact details.
2. Scope and process facts that change the filing route.
3. Separate Building record descriptions and valuations.
4. Contractor/designer/engineer details only where applicable.
5. Design-contingent requirements identified by the routing corpus.
6. Applicant-controlled assertions, declarations, and acknowledgements.

State why each answer is needed and which record it affects.

## Site facts

Coastal zone, Coastal Commission appeal area, bluff or oceanfront, fire hazard zone,
zoning and flood zone change the filing route and the plan-sheet list. Get them from a
source, record the source as `site_facts`, and keep any fact you cannot source null.

**With the CrossBeam connector.** When the host has the CrossBeam connector (tools whose
names start with `crossbeam_`), call `crossbeam_get_site_facts` with the address. Store
each returned value with the tool name and the time as its receipt. Treat the result as
evidence: if it conflicts with the plans or a City document, follow the conflict protocol.

**Without the connector.** Run the parcel lookup, which reads the City's public map layers
(read-only; nothing is submitted):

```sh
python3 "<plugin-root>/scripts/parcel-facts/parcel_facts.py" --address "<number> <street>, Laguna Beach, CA" \
  --out permit-work/state/parcel-facts.json
```

Store each fact with the script's `queried_at` time as its receipt. Exit code 2 means
several parcels or none matched: show the candidates and ask which one. Facts it lists
under `not_available` (coastal zone, fire hazard tier, slope, bluff edge and others) come
from the source it names; keep them null until then. `scripts/parcel-facts/README.md`
explains each fact. If the host cannot run Python, use the City's public GIS directly:

- City public GIS viewer: https://gis.lagunabeachcity.net/Html5Viewer/index.html?viewer=LagunaBeachPublicGIS
  (the City's "City Maps & GIS" menu opens this viewer).
- City ArcGIS map viewer: https://lagunabeach.maps.arcgis.com/apps/webappviewer/index.html?id=75a3aa3236c7475bb5e81925d130a763
  (the City's FAQ points here for the "building site designation").
- City parcel layer (ArcGIS REST, public, no sign-in):
  `https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/GIS_Map/FeatureServer/4/query`.
  Query by address with `where=ADDRESS LIKE '<number> <street>%'`,
  `outFields=AP,ADDRESS,ZONING,SPECPLAN,CDPAPPL,FLZONE,BLDGSITE,CNSTRNT`,
  `returnGeometry=false`, `f=json`. Add `returnCentroid=true&outSR=4326` to get a point
  for the layers below. Field meanings (from the layer's own aliases): `ZONING` zone
  district, `SPECPLAN` specific plan, `CDPAPPL` Coastal Commission appeal or deferred
  area, `FLZONE` FEMA flood zone(s), `BLDGSITE` building site designation, `CNSTRNT`
  environmentally sensitive areas. Do not request the owner fields.
- Coastal Commission appeal jurisdiction: `.../GIS_Map/FeatureServer/34`.
  Area of deferred certification: `.../GIS_Map/FeatureServer/33`.
  Oceanfront and bluff screening area: `https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/Oceanfront/FeatureServer/0`.
  Fuel modification zones: `https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/FuelManagementZones/FeatureServer/1`.
  Query each with the parcel point: `geometry=<lon>,<lat>&geometryType=esriGeometryPoint&inSR=4326&spatialRel=esriSpatialRelIntersects&returnCountOnly=true&f=json`.
  A count of 1 or more means the point is inside.
- Fire hazard severity zone: the City adopted the State's 2025 Very High Fire Hazard
  Severity Zone map for the local responsibility area. The City page for it is
  https://www.lagunabeachcity.net/government/departments/fire/fire-prevention/new-lra-fhsz-maps-for-public-comments;
  it refuses scripted requests, so open it in a visible browser or ask the user to. The
  parcel layer's `CNSTRNT` field may say `VHFHSZ`; treat that as a lead and confirm it on
  the adopted map. Never infer the zone from a citywide percentage.

Whether a parcel is in the coastal zone, on a bluff, or in a hazard zone is a fact to
read from these sources, not to guess from the address or the view. A point query tests
one point; a parcel that straddles a boundary needs a look at the map. If a source is
down or unclear, keep the fact null and tell the user which map to check.

Sources: the City's GIS endpoints and viewer links are recorded in CrossBeam's Laguna
Beach city research (2026-07 to 2026-09). The viewer, map viewer and the REST layers
answered a public GET on 2026-10-09; the City fire page returned HTTP 403 to a script.

## Conflict protocol

If two sources disagree, store both candidates in the fact's `conflicts` array, stop the affected consumer, and ask the user to resolve it. Never silently prefer the value that makes the form complete. A plan/portal mismatch in address, scope, valuation, counts, or contact identity blocks the affected record.
