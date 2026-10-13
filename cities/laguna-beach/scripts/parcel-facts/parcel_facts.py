#!/usr/bin/env python3
# GENERATED FILE. Do not edit by hand; the plugin publisher overwrites it.
# Run: python3 scripts/parcel-facts/parcel_facts.py --address "<street address>"
"""Laguna Beach parcel facts from the City's public GIS layers.

Looks up one City of Laguna Beach parcel and reports what the City's public
ArcGIS layers say about it: the parcel record (APN, zone, specific plan,
general plan, lot area, year built, historic rating, flood zone) and whether
each mapped overlay (coastal appeal area, deferred certification area,
categorical exclusion, historic register, fuel modification, open space,
landslide, watercourse, blue-line stream, ridgeline, habitat, oceanfront,
water quality ESA) touches it.

    python3 parcel_facts.py --address "<street address>"
    python3 parcel_facts.py --apn 123-456-78
    python3 parcel_facts.py --lat 33.54 --lon -117.78
    python3 parcel_facts.py --address "<street address>" --out parcel-facts.json

It only fetches and reports. It never decides what a fact means for a permit;
the agent reading the JSON does that, using the plugin's skills.

Python 3.8 or later, standard library only. Network: HTTPS GET requests to the
City of Laguna Beach ArcGIS layers and, only when the City layer has no row for
the typed address, the US Census geocoder. No key, no account.

Privacy: the script asks the City layers for a fixed list of property fields.
It never requests or prints owner names, owner mailing addresses, sale prices,
assessed values or taxes.

Exit codes: 0 = one parcel matched; 2 = no parcel or several possible parcels
(the JSON lists candidates; re-run with --apn); 1 = bad arguments or the parcel
layer itself could not be reached.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

VERSION = "1.0.0"
USER_AGENT = "laguna-beach-parcel-facts/" + VERSION + " (python-urllib)"
TIMEOUT_S = 30
ATTEMPTS = 3

# ---------------------------------------------------------------------------
# Sources. Kept equal to the maintained endpoint inventory and label tables by
# the plugin publisher, which refuses to publish when they differ. The block is
# plain JSON so that check can read it.
# ---------------------------------------------------------------------------
SOURCE_DATA = json.loads(r'''
{
  "parcel_url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/GIS_Map/FeatureServer/4",
  "census_geocoder_url": "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress",
  "fire_map_url": "https://www.lagunabeachcity.net/government/departments/fire/fire-prevention/new-lra-fhsz-maps-for-public-comments",
  "layers": {
    "zoning": {
      "name": "Zoning map",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/GIS_Map/FeatureServer/72",
      "reads_as": "The zoning map row for this APN. ZONING1 is the base zone; ZONING2 and ZONING3 carry a second zone or an overlay code. Compare with parcel.zone."
    },
    "specific_plan": {
      "name": "Specific plans",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/All_SpecificPlans/FeatureServer/0",
      "reads_as": "A specific plan whose standards apply in addition to, or instead of, the base zone. Compare with parcel.specific_plan."
    },
    "coastal_appeal": {
      "name": "Coastal Commission appeal jurisdiction",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/GIS_Map/FeatureServer/34",
      "reads_as": "Inside the Coastal Commission appeal jurisdiction, a City coastal development permit can be appealed to the Commission. Compare with parcel.coastal_appeal_or_deferred."
    },
    "coastal_deferred": {
      "name": "Coastal area of deferred certification",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/GIS_Map/FeatureServer/33",
      "reads_as": "Inside an area of deferred certification the Coastal Commission, not the City, issues the coastal development permit."
    },
    "cat_exclusion": {
      "name": "Coastal categorical exclusion areas",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/CatExclusion_Areas/FeatureServer/0",
      "reads_as": "Every City parcel has a row; the CatExclusion column (Yes/No) is the answer. A categorical exclusion does not reach development that stays appealable to the Coastal Commission, so read it together with coastal_appeal."
    },
    "historic": {
      "name": "Historic register and inventory parcels",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/CLB_Historical_Parcels/FeatureServer/0",
      "reads_as": "Only listed parcels have a row. HISTREG_ST = Yes means on the City Historic Register; HISTRATE is the inventory rating; MILLSACT marks a Mills Act contract."
    },
    "fuel_modification": {
      "name": "Fuel modification zones",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/FuelManagementZones/FeatureServer/1",
      "supplemental_urls": [
        "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/AllFuelModAreas/FeatureServer/0",
        "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/Fuel_Modification_Public/FeatureServer/1"
      ],
      "reads_as": "Any contact between the parcel and a mapped fuel modification area counts. Three Fire Department layers are read."
    },
    "open_space_preserve": {
      "name": "Open space preserve",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/GIS_Map/FeatureServer/36",
      "reads_as": "The skills also count the parcel as open space preserve when parcel.environmental_constraints lists OSP."
    },
    "landslide": {
      "name": "Seismic hazard landslide areas (City map)",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/GIS_Map/FeatureServer/39",
      "reads_as": "A screening map. The skills treat a parcel as a mapped major landslide only when this layer touches it AND parcel.environmental_constraints carries a landslide flag."
    },
    "watercourse_buffer": {
      "name": "Drainage course 25-foot buffer",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/GIS_Map/FeatureServer/41",
      "reads_as": "The City's 25-foot buffer around mapped drainage courses."
    },
    "blueline_stream": {
      "name": "Significant drainage course (blue-line stream) centerline",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/GIS_Map/FeatureServer/42",
      "reads_as": "Hit when the parcel is within 25 ft of a mapped drainage course centerline.",
      "buffer_basis": "25 ft, the width of the City's own drainage course buffer layer."
    },
    "ridgeline": {
      "name": "Ridgelines",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/GIS_Map/FeatureServer/43",
      "reads_as": "Hit when the parcel is within the screening distance of a mapped ridgeline.",
      "buffer_basis": "The City has not published a ridgeline buffer width; this distance is a conservative screening assumption. Read distance_ft and confirm with Planning."
    },
    "habitat_vhvh": {
      "name": "Very high value habitat",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/GIS_Map/FeatureServer/44",
      "reads_as": "Very high value habitat (an environmentally sensitive area). Coastal sage scrub has no separate City layer; it is part of the habitat layers."
    },
    "habitat_hvh": {
      "name": "High value habitat",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/GIS_Map/FeatureServer/45",
      "reads_as": "High value habitat (an environmentally sensitive area)."
    },
    "oceanfront": {
      "name": "Oceanfront / coastal screening polygon",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/Oceanfront/FeatureServer/0",
      "reads_as": "One coast-wide screening polygon, not a bluff edge. The skills treat the parcel as oceanfront only when this polygon covers it AND parcel.environmental_constraints lists Coastal AND parcel.flood_zone has no V or VE zone. A bluff edge determination decides the rest."
    },
    "wqesa": {
      "name": "Water Quality Environmentally Sensitive Area",
      "url": "https://services9.arcgis.com/DPQ7yLDIWIyMUXzD/arcgis/rest/services/WQESA/FeatureServer/0",
      "reads_as": "Water Quality Environmentally Sensitive Area: adds water quality requirements for development."
    }
  },
  "ridgeline_buffer_ft": 100,
  "deferred_certification_names": {
    "1": "Irvine Cove Area of Deferred Certification",
    "2": "Hobo Canyon Area of Deferred Certification",
    "3": "Hobo Canyon Area of Deferred Certification",
    "4": "Blue Lagoon Area of Deferred Certification",
    "5": "Three Arch Bay Area of Deferred Certification",
    "6": "Three Arch Bay Area of Deferred Certification"
  },
  "open_space_preserve_names": {
    "1": {
      "name": "Laguna Coast Wilderness Park",
      "confidence": "high"
    },
    "2": {
      "name": "Laguna Coast Wilderness Park",
      "confidence": "high"
    },
    "3": {
      "name": "Laguna Coast Wilderness Park",
      "confidence": "medium"
    },
    "4": {
      "name": "Laguna Coast Wilderness Park",
      "confidence": "medium"
    },
    "5": {
      "name": "Aliso and Wood Canyons Wilderness Park",
      "confidence": "high"
    },
    "6": {
      "name": "Bluebird Canyon Open Space",
      "confidence": "medium"
    },
    "10": {
      "name": "Aliso and Wood Canyons Wilderness Park",
      "confidence": "medium"
    },
    "11": {
      "name": "Laguna Coast Wilderness Park",
      "confidence": "high"
    }
  },
  "specific_plan_aliases": {
    "Diamond Crestview": "Diamond Crest Specific Plan",
    "Diamond Crestview Specific Plan": "Diamond Crest Specific Plan"
  },
  "parcel_fields": [
    [
      "ADDRESS",
      "address",
      "Site address as the City parcel layer prints it"
    ],
    [
      "SITECSZ",
      "city_state_zip",
      "Site city, state and ZIP"
    ],
    [
      "AP",
      "apn",
      "Assessor parcel number"
    ],
    [
      "PIN",
      "city_parcel_id",
      "City parcel identification number"
    ],
    [
      "ZONING",
      "zone",
      "Zone district"
    ],
    [
      "SPECPLAN",
      "specific_plan",
      "Specific plan area code (None = not in a specific plan)"
    ],
    [
      "GENPLAN",
      "general_plan",
      "General Plan land use designation"
    ],
    [
      "AREA",
      "lot_area_sqft",
      "Parcel area in square feet, as the City records it"
    ],
    [
      "YRBUILT",
      "year_built",
      "Year built"
    ],
    [
      "STORIES",
      "stories",
      "Number of stories"
    ],
    [
      "NOUNITS",
      "units",
      "Number of units"
    ],
    [
      "TOTLBAR",
      "building_living_area_sqft",
      "Building living area in square feet"
    ],
    [
      "HISTRATE",
      "historic_rating",
      "Historic Resources Inventory rating (E, K or C)"
    ],
    [
      "HISTREG",
      "historic_register_date",
      "Historic Register designation date"
    ],
    [
      "FLZONE",
      "flood_zone",
      "FEMA flood zone(s) the City records for the parcel"
    ],
    [
      "FLDATE",
      "flood_map_date",
      "FEMA flood map effective date"
    ],
    [
      "FLPANEL",
      "flood_map_panel",
      "FEMA flood map panel number"
    ],
    [
      "CDPAPPL",
      "coastal_appeal_or_deferred",
      "Coastal Commission appeal or deferred area (Yes, No or Deferred)"
    ],
    [
      "CNSTRNT",
      "environmental_constraints",
      "Environmentally sensitive area flags the City records on the parcel"
    ],
    [
      "HOA",
      "hoa",
      "Home owners' association area"
    ],
    [
      "BLDGSITE",
      "building_site",
      "Building site designation"
    ],
    [
      "BLDGSTBK",
      "subdivision_setbacks",
      "Special subdivision map building setbacks"
    ],
    [
      "HGHTSTND",
      "subdivision_height_standard",
      "Special subdivision map height standards"
    ],
    [
      "STRTPLAN",
      "street_plan",
      "Special street plan requirements"
    ],
    [
      "GUIDELN",
      "landscaping_setback_guideline",
      "Recommended landscaping and setbacks"
    ],
    [
      "ONSITE",
      "onsite_turnaround_required",
      "On-site turnaround required"
    ],
    [
      "WSHEDS",
      "watershed",
      "Watershed"
    ],
    [
      "SUBDIVIS",
      "tract",
      "Legal subdivision tract number"
    ],
    [
      "BLCKBLDG",
      "block",
      "Legal block number"
    ],
    [
      "LOTUNIT",
      "lot",
      "Legal lot number"
    ],
    [
      "LGLDSCRP",
      "legal_description",
      "Legal description"
    ]
  ],
  "not_available": [
    {
      "fact": "coastal_zone",
      "why": "The coastal zone boundary is a California Coastal Commission map, not a City layer this script reads.",
      "provide_instead": "The skills say nearly all of Laguna Beach is in the coastal zone (the certified Land Use Element excludes only the 522-acre Sycamore Hills area). Confirm the parcel with the City or the Coastal Commission's coastal zone boundary map."
    },
    {
      "fact": "fire_hazard_severity_zone",
      "why": "The adopted 2025 LRA Fire Hazard Severity Zone map is a CAL FIRE map, not read here.",
      "provide_instead": "Check the parcel on the map the City adopted: https://www.lagunabeachcity.net/government/departments/fire/fire-prevention/new-lra-fhsz-maps-for-public-comments"
    },
    {
      "fact": "slope",
      "why": "No public City layer gives parcel slope or grades.",
      "provide_instead": "A topographic survey by a licensed land surveyor or civil engineer."
    },
    {
      "fact": "bluff_edge",
      "why": "The oceanfront layer is a screening polygon, not a bluff edge line.",
      "provide_instead": "A bluff edge determination (and geotechnical report) by a qualified professional."
    },
    {
      "fact": "heritage_trees",
      "why": "The City's heritage tree list is not a public layer. A CHTree flag in parcel.environmental_constraints marks a candidate, not a designation.",
      "provide_instead": "An arborist report, or ask the City whether a designated heritage tree is on or next to the parcel."
    },
    {
      "fact": "state_geologic_hazard_zones",
      "why": "Alquist-Priolo fault zones and state seismic hazard zones (liquefaction, landslide) are state maps, not read here. The landslide entry is the City's own map.",
      "provide_instead": "A geotechnical report, or the California Geological Survey maps."
    },
    {
      "fact": "fema_flood_map",
      "why": "parcel.flood_zone is the FEMA zone the City records on the parcel, not a live read of the FEMA flood map.",
      "provide_instead": "The current FEMA FIRM panel for the parcel, or an elevation certificate."
    },
    {
      "fact": "draft_historic_register",
      "why": "Properties proposed in the City's draft historic register update are not in the public historic layer.",
      "provide_instead": "Ask Planning whether the property is on the draft register or needs a historic resource assessment."
    },
    {
      "fact": "transit_distance",
      "why": "Distance to transit stops (ADU and parking rules) is not computed.",
      "provide_instead": "Measure the walking distance to the nearest major transit stop on a public transit map."
    },
    {
      "fact": "zoning_standards",
      "why": "The script reports the zone code only, not setbacks, height or coverage.",
      "provide_instead": "Read the zone's standards in the plugin's zoning references."
    }
  ]
}
''')

PARCEL_URL = SOURCE_DATA["parcel_url"]
CENSUS_URL = SOURCE_DATA["census_geocoder_url"]
LAYER_URLS = SOURCE_DATA["layers"]
CITY = "Laguna Beach"

# The parcel fields the script asks for, in output order: (City field, output
# key, what it means). Owner, mailing, sale and tax fields are never on this
# list, so they never leave the City's server.
PARCEL_FIELDS = [tuple(entry) for entry in SOURCE_DATA["parcel_fields"]]
INTEGER_KEYS = {"lot_area_sqft", "year_built", "stories", "units", "building_living_area_sqft"}

# Fields that must never appear in the output, whatever a layer returns.
PRIVATE_FIELDS = {
    "OWNERLAB", "OWNERS", "OWNER", "ADRESLAB", "CSZLAB", "SALEPRCE", "SALEDATE",
    "LANDVLUE", "TOTIMPVU", "TOTTAXVU", "TOTTAXES", "TAXCODE", "CORNOTDT", "COMCLRDT",
}

FIRE_MAP_URL = SOURCE_DATA["fire_map_url"]

# A polygon that covers less than this share of the parcel and misses its
# interior point is an edge sliver: usually two maps' edges disagreeing.
SLIVER_SHARE = 0.02
# How far around the parcel the script looks, to report the nearest feature.
NEARBY_FT = 200.0

# One entry per overlay, in output order.
#   method: polygon (share of the parcel), touch (any contact counts),
#           line (distance to a mapped line), record (row keyed by APN)
#   skill_fact: the fact name the plugin's skills use for this layer
# Each layer's reads_as text (how the skills combine it with the parcel record)
# is in SOURCE_DATA, so the README can quote it.
OVERLAY_SPECS = [
    {
        "id": "zoning", "method": "record", "key_field": "ASSESSNO",
        "fields": ["ASSESSNO", "SITUS", "ZONING1", "ZONING2", "ZONING3", "LAND_USE_D"],
        "skill_fact": "zoning.code",
    },
    {
        "id": "specific_plan", "method": "polygon", "fields": ["OBJECTID", "Name"],
        "skill_fact": "specific_plan_or_association",
    },
    {
        "id": "coastal_appeal", "method": "polygon", "fields": ["OBJECTID", "Name", "BUFF_DIST"],
        "skill_fact": "coastal_designation.in_appeals_jurisdiction",
    },
    {
        "id": "coastal_deferred", "method": "polygon", "fields": ["OBJECTID", "Name"],
        "skill_fact": "coastal_designation.area_of_deferred_certification_name",
    },
    {
        "id": "cat_exclusion", "method": "record", "key_field": "AP",
        "fields": ["AP", "ADDRESS", "CatExclusion", "CatExclusionName"],
        "skill_fact": "coastal_designation.in_categorical_exclusion",
    },
    {
        "id": "historic", "method": "record", "key_field": "AP",
        "fields": ["AP", "HISTRATE", "HISTREGNUM", "HISTREG_ST", "HISTREG", "MILLSACT", "MILLSACTDA", "STYLE", "YRBUILT"],
        "skill_fact": "historic",
    },
    {
        "id": "fuel_modification", "method": "touch",
        "fields": ["OBJECTID", "Number", "Name", "Category", "Method"],
        "supplemental_fields": [["FID", "Name", "Permit", "Method"], ["OBJECTID", "Name", "Status"]],
        "skill_fact": "esa_overlays.fuel_modification",
    },
    {
        "id": "open_space_preserve", "method": "polygon", "fields": ["OBJECTID", "ID"],
        "skill_fact": "esa_overlays.open_space_preserve",
    },
    {
        "id": "landslide", "method": "polygon", "fields": ["OBJECTID", "ID"],
        "skill_fact": "esa_overlays.major_landslides",
    },
    {
        "id": "watercourse_buffer", "method": "polygon", "fields": ["OBJECTID", "BUFF_DIST"],
        "skill_fact": "esa_overlays.watercourse",
    },
    {
        "id": "blueline_stream", "method": "line", "buffer_ft": 25.0, "fields": ["OBJECTID", "LAYER"],
        "skill_fact": "esa_overlays.blueline_stream",
    },
    {
        "id": "ridgeline", "method": "line", "buffer_ft": float(SOURCE_DATA["ridgeline_buffer_ft"]), "fields": ["OBJECTID", "ID"],
        "skill_fact": "esa_overlays.ridgeline",
    },
    {
        "id": "habitat_vhvh", "method": "polygon", "fields": ["OBJECTID", "VERYHIGH"],
        "skill_fact": "esa_overlays.vhvh_habitat",
    },
    {
        "id": "habitat_hvh", "method": "polygon", "fields": ["OBJECTID", "VERYHIGH"],
        "skill_fact": "esa_overlays.hvh_habitat",
    },
    {
        "id": "oceanfront", "method": "polygon", "fields": ["OBJECTID", "Id"],
        "skill_fact": "esa_overlays.oceanfront",
    },
    {
        "id": "wqesa", "method": "polygon", "fields": ["OBJECTID", "WQESA"],
        "skill_fact": "esa_overlays.wqesa",
    },
]

NOT_AVAILABLE = SOURCE_DATA["not_available"]

STATIC_NOTES = [
    "Fire hazard: the plugin's skills treat every Laguna Beach parcel as inside a Fire Hazard Severity Zone / wildland-urban interface area. Whether this parcel is in the Very High tier is parcel-specific; check the 2025 LRA map the City adopted (" + FIRE_MAP_URL + "). A VHFHSZ flag in parcel.environmental_constraints comes from the City parcel record and may reflect an older map.",
    "These are mapped GIS facts. A layer that could not be read is reported as hit = \"unknown\", never as false. Confirm anything that changes the permit path with the City.",
]


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

class FetchError(Exception):
    pass


def http_get_json(url, params):
    """GET url?params and parse JSON. Retries timeouts, 429 and 5xx."""
    full = url + "?" + urllib.parse.urlencode(params)
    last = None
    for attempt in range(ATTEMPTS):
        if attempt:
            time.sleep(2 ** (attempt - 1))
        request = urllib.request.Request(full, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=TIMEOUT_S) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            last = "HTTP %s" % exc.code
            if exc.code == 429 or exc.code >= 500:
                continue
            raise FetchError(last)
        except (urllib.error.URLError, OSError, ValueError) as exc:
            last = "%s: %s" % (type(exc).__name__, getattr(exc, "reason", exc))
            continue
        error = payload.get("error") if isinstance(payload, dict) else None
        if error:
            code = error.get("code") if isinstance(error, dict) else None
            last = "ArcGIS error %s: %s" % (code, error.get("message") if isinstance(error, dict) else error)
            if isinstance(code, int) and (code == 429 or code >= 500):
                continue
            raise FetchError(last)
        return payload
    raise FetchError("%s after %d attempts" % (last, ATTEMPTS))


def arcgis_query(fetch, layer_url, params, max_pages=10):
    """Run a /query and follow exceededTransferLimit pages."""
    base = {"f": "json", "returnGeometry": "true", "outSR": "4326"}
    base.update(params)
    features = []
    offset = 0
    for _ in range(max_pages):
        page = dict(base)
        if offset:
            page["resultOffset"] = str(offset)
        payload = fetch(layer_url.rstrip("/") + "/query", page)
        batch = payload.get("features") or []
        features.extend(batch)
        if not payload.get("exceededTransferLimit") or not batch:
            return features
        offset += len(batch)
    raise FetchError("more than %d pages of results" % max_pages)


def sql_quote(value):
    return "'" + str(value).replace("'", "''") + "'"


# ---------------------------------------------------------------------------
# Address text (mechanical normalization of a known address format)
# ---------------------------------------------------------------------------

STREET_SUFFIXES = [
    (r"\b(avenue|ave|av)\b", "av"), (r"\b(street|st)\b", "st"), (r"\b(road|rd)\b", "rd"),
    (r"\b(drive|dr)\b", "dr"), (r"\b(boulevard|blvd|bl)\b", "bl"), (r"\b(highway|hwy|hy)\b", "hwy"),
    (r"\b(lane|ln)\b", "ln"), (r"\b(court|ct)\b", "ct"), (r"\b(place|pl)\b", "pl"),
    (r"\b(circle|cir|cr)\b", "cir"), (r"\b(way|wy)\b", "way"), (r"\b(terrace|ter|te)\b", "ter"),
    (r"\b(view|vw)\b", "vw"),
]
DIRECTIONS = [
    (r"\b(north|n)\b", "n"), (r"\b(south|s)\b", "s"), (r"\b(east|e)\b", "e"), (r"\b(west|w)\b", "w"),
    (r"\b(northeast|ne)\b", "ne"), (r"\b(northwest|nw)\b", "nw"), (r"\b(southeast|se)\b", "se"),
    (r"\b(southwest|sw)\b", "sw"),
]
DIRECTION_TOKENS = {"n", "s", "e", "w", "ne", "nw", "se", "sw"}
# Street-type tokens after normalization, plus abbreviations the City layer
# prints that the normalizer leaves alone ("Ci", "Tr"). "vw" is left out:
# "View" is usually part of the name ("Ocean View").
STREET_SUFFIX_TOKENS = {
    "av", "st", "rd", "dr", "bl", "hwy", "ln", "ct", "pl", "cir", "ci", "way", "ter",
    "tr", "trl", "trail", "pkwy", "pky", "sq", "aly",
}
UNIT_DESIGNATORS = {"unit", "apt", "apartment", "ste", "suite", "spc", "space", "#"}
ORDINAL_TOKEN = re.compile(r"^(\d+)(?:st|nd|rd|th)$")


def normalize_address(value, city=CITY):
    """Canonical street line: lower case, no city/state/ZIP, short street types."""
    street = (value or "").strip().lower()
    comma = street.find(",")
    if comma >= 0:
        street = street[:comma]
    if city:
        index = street.find(city.lower())
        if index > 0:
            street = street[:index]
    street = re.sub(r"\b(usa|united states)\b", " ", street)
    street = re.sub(r"\b(ca|california)\b", " ", street)
    street = re.sub(r"\s\d{5}(?:-\d{4})?(?=\s|$)", " ", street)
    for pattern, replacement in DIRECTIONS:
        street = re.sub(pattern, replacement, street)
    for pattern, replacement in STREET_SUFFIXES:
        street = re.sub(pattern, replacement, street)
    street = re.sub(r"[^a-z0-9# ]", " ", street)
    return re.sub(r"\s+", " ", street).strip()


def _street_name_index(tokens):
    if len(tokens) < 2 or not tokens[0][:1].isdigit():
        return -1
    return 2 if tokens[1] in DIRECTION_TOKENS and len(tokens) >= 3 else 1


def _without_ordinal(normalized):
    """'12 3rd st' -> '12 3 st' (the City layer prints numbered streets as digits)."""
    tokens = normalized.split(" ")
    index = _street_name_index(tokens)
    match = ORDINAL_TOKEN.match(tokens[index]) if index > 0 else None
    if not match:
        return normalized
    tokens[index] = match.group(1)
    return " ".join(tokens)


def _without_street_type(normalized):
    tokens = [token for token in normalized.split(" ") if token]
    if len(tokens) >= 3 and tokens[-1] in STREET_SUFFIX_TOKENS:
        tokens.pop()
    return " ".join(tokens)


def _without_lone_direction(a, b):
    """Same line when only one side has a directional right after the house number."""
    a_tokens, b_tokens = a.split(" "), b.split(" ")
    if not a_tokens[0][:1].isdigit() or a_tokens[0] != b_tokens[0]:
        return False

    def prefix(tokens):
        return tokens[1] if len(tokens) >= 3 and tokens[1] in DIRECTION_TOKENS else None

    a_dir, b_dir = prefix(a_tokens), prefix(b_tokens)
    if bool(a_dir) == bool(b_dir):
        return False
    a_rest = [a_tokens[0]] + a_tokens[2:] if a_dir else a_tokens
    b_rest = [b_tokens[0]] + b_tokens[2:] if b_dir else b_tokens
    return a_rest == b_rest


def addresses_match(query, candidate):
    q, c = normalize_address(query), normalize_address(candidate)
    if not q or not c:
        return False
    if q == c:
        return True
    q, c = _without_ordinal(q), _without_ordinal(c)
    return q == c or _without_lone_direction(q, c)


def addresses_match_ignoring_type(query, candidate):
    """'12 Example St' ~ '12 Example Dr': only the street type differs or is missing."""
    q = _without_ordinal(_without_street_type(normalize_address(query)))
    c = _without_ordinal(_without_street_type(normalize_address(candidate)))
    if not q or not c or not q[:1].isdigit():
        return False
    return q == c or _without_lone_direction(q, c)


def fold_unit_designator(address):
    """'12 Example Hwy Unit 3' -> '12 Example Hwy 3' (how the layer prints units)."""
    comma = address.find(",")
    street = address[:comma] if comma >= 0 else address
    rest = address[comma:] if comma >= 0 else ""
    tokens = re.sub(r"#\s*", "# ", street.strip()).split()
    if len(tokens) < 4 or not tokens[0][:1].isdigit():
        return None
    designator = tokens[-2].lower().rstrip(".")
    unit = tokens[-1]
    if designator not in UNIT_DESIGNATORS or not re.match(r"^[a-z0-9-]+$", unit, re.I):
        return None
    return " ".join(tokens[:-2] + [unit]) + rest


def strip_unit_designator(address):
    """'12 S Example Hwy #3' -> '12 S Example Hwy' (the building's own line)."""
    folded = fold_unit_designator(address)
    if not folded:
        return None
    comma = folded.find(",")
    street = folded[:comma] if comma >= 0 else folded
    rest = folded[comma:] if comma >= 0 else ""
    return " ".join(street.split()[:-1]) + rest


def matches_with_unit_suffix(query, candidate):
    """'12 Example Dr' ~ '12 Example Dr R1': the typed line plus one unit token."""
    if fold_unit_designator(query):
        return False
    q = _without_ordinal(normalize_address(query)).split()
    c = _without_ordinal(normalize_address(candidate)).split()
    if len(q) < 2 or not q[0][:1].isdigit() or len(c) != len(q) + 1:
        return False
    unit = c[-1]
    if not re.search(r"\d", unit) and not re.match(r"^[a-z]$", unit):
        return False
    return c[:-1] == q


def named_city(address):
    """The city an address names after its street line ('..., Laguna Niguel, CA'), or None."""
    parts = [part.strip() for part in address.split(",") if part.strip()]
    if len(parts) < 2:
        return None
    city = re.sub(r"\b(ca|california)\b.*$", "", parts[1], flags=re.I).strip()
    city = re.sub(r"\d{5}(?:-\d{4})?", "", city).strip()
    return city or None


def search_terms(address):
    """House number and the street-name token for the City layer's LIKE search."""
    tokens = normalize_address(address).split()
    if not tokens or not tokens[0][:1].isdigit():
        return None, None
    rest = tokens[1:]
    name_tokens = [token for token in rest if token not in DIRECTION_TOKENS and token != "#"]
    token = next((t for t in name_tokens if len(t) > 2), name_tokens[0] if name_tokens else None)
    if not token:
        return tokens[0], None
    match = ORDINAL_TOKEN.match(token)
    return tokens[0], (match.group(1) if match else token)


def canonical_apn(value):
    return re.sub(r"[^0-9a-z]", "", str(value or "").lower())


def apn_key_variants(apn):
    """'012-345-67' and '12-345-67': the zoning map drops the leading zero."""
    if not apn:
        return []
    variants = [apn]
    head, sep, tail = apn.partition("-")
    trimmed = head.lstrip("0")
    if sep and trimmed and trimmed != head:
        variants.append(trimmed + sep + tail)
    return variants


def format_apn(value):
    """'12345678' -> '123-456-78' (the City layer's printed form)."""
    digits = re.sub(r"\D", "", str(value or ""))
    if len(digits) == 8:
        return "%s-%s-%s" % (digits[:3], digits[3:6], digits[6:])
    return str(value or "").strip()


# ---------------------------------------------------------------------------
# Geometry (lon/lat from the server, projected locally to feet around the parcel)
# ---------------------------------------------------------------------------

FEET_PER_METER = 3.280833333


class Frame(object):
    """Local planar frame in feet, centred on a lon/lat."""

    def __init__(self, lon, lat):
        phi = math.radians(lat)
        self.lon0, self.lat0 = lon, lat
        self.ky = (111132.954 - 559.822 * math.cos(2 * phi) + 1.175 * math.cos(4 * phi)) * FEET_PER_METER
        self.kx = (111412.84 * math.cos(phi) - 93.5 * math.cos(3 * phi) + 0.118 * math.cos(5 * phi)) * FEET_PER_METER

    def to_ft(self, lon, lat):
        return ((lon - self.lon0) * self.kx, (lat - self.lat0) * self.ky)

    def to_lonlat(self, x, y):
        return (self.lon0 + x / self.kx, self.lat0 + y / self.ky)

    def project(self, parts):
        return [[self.to_ft(p[0], p[1]) for p in part] for part in parts]


def geometry_parts(geometry):
    """Rings of a polygon or paths of a polyline, as lists of [x, y]."""
    if not geometry:
        return [], None
    if geometry.get("rings"):
        return geometry["rings"], "polygon"
    if geometry.get("paths"):
        return geometry["paths"], "line"
    return [], None


def bbox(parts):
    xs = [p[0] for part in parts for p in part]
    ys = [p[1] for part in parts for p in part]
    if not xs:
        return None
    return (min(xs), min(ys), max(xs), max(ys))


def point_in_rings(x, y, rings):
    """Even-odd ray cast over every ring (handles holes and multipart polygons)."""
    inside = False
    for ring in rings:
        n = len(ring)
        j = n - 1
        for i in range(n):
            xi, yi = ring[i]
            xj, yj = ring[j]
            if (yi > y) != (yj > y):
                cross = (xj - xi) * (y - yi) / (yj - yi) + xi
                if x < cross:
                    inside = not inside
            j = i
    return inside


def edges_near(parts, box):
    """Polygon edges that can affect a point-in-polygon test inside `box`.

    A ray cast toward +x from a point in the box only crosses edges that span
    the point's y and reach past the box's left side, so the rest are dropped.
    The answer is exact; the filter only saves time on large polygons.
    """
    out = []
    for ring in parts:
        n = len(ring)
        for i in range(n):
            xi, yi = ring[i]
            xj, yj = ring[i - 1]
            if max(yi, yj) < box[1] or min(yi, yj) > box[3] or max(xi, xj) < box[0]:
                continue
            out.append((xi, yi, xj, yj))
    return out


def point_in_edges(x, y, edges):
    inside = False
    for xi, yi, xj, yj in edges:
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            inside = not inside
    return inside


def rings_area(rings):
    total = 0.0
    for ring in rings:
        s = 0.0
        for i in range(len(ring)):
            x1, y1 = ring[i]
            x2, y2 = ring[(i + 1) % len(ring)]
            s += x1 * y2 - x2 * y1
        total += s / 2.0
    return abs(total)


def segments(parts, closed):
    out = []
    for part in parts:
        count = len(part)
        for i in range(count - 1):
            out.append((part[i], part[i + 1]))
        if closed and count > 2 and part[0] != part[-1]:
            out.append((part[-1], part[0]))
    return out


def _point_segment_distance(p, a, b):
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    length2 = dx * dx + dy * dy
    if length2 == 0:
        return math.hypot(p[0] - ax, p[1] - ay)
    t = max(0.0, min(1.0, ((p[0] - ax) * dx + (p[1] - ay) * dy) / length2))
    return math.hypot(p[0] - (ax + t * dx), p[1] - (ay + t * dy))


def _orientation(a, b, c):
    value = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    return 0 if abs(value) < 1e-12 else (1 if value > 0 else 2)


def _segments_cross(p1, p2, q1, q2):
    o1, o2 = _orientation(p1, p2, q1), _orientation(p1, p2, q2)
    o3, o4 = _orientation(q1, q2, p1), _orientation(q1, q2, p2)
    return o1 != o2 and o3 != o4


def segment_distance(p1, p2, q1, q2):
    if _segments_cross(p1, p2, q1, q2):
        return 0.0
    return min(
        _point_segment_distance(p1, q1, q2), _point_segment_distance(p2, q1, q2),
        _point_segment_distance(q1, p1, p2), _point_segment_distance(q2, p1, p2),
    )


def _bbox_gap(a, b):
    dx = max(0.0, max(a[0], b[0]) - min(a[2], b[2]))
    dy = max(0.0, max(a[1], b[1]) - min(a[3], b[3]))
    return math.hypot(dx, dy)


def distance_to_parcel(parcel, feature_parts, feature_kind, limit):
    """Shortest distance in feet between the parcel and a feature; 0 when they touch.

    Returns None when the feature is farther than `limit`.
    """
    rings = parcel["rings"]
    box = parcel["bbox"]
    if feature_kind == "polygon":
        edges = edges_near(feature_parts, box)
        if any(point_in_edges(p[0], p[1], edges) for p in parcel["vertices"]):
            return 0.0
    for part in feature_parts:
        for p in part:
            if box[0] <= p[0] <= box[2] and box[1] <= p[1] <= box[3] and point_in_rings(p[0], p[1], rings):
                return 0.0
    best = None
    for q1, q2 in segments(feature_parts, feature_kind == "polygon"):
        seg_box = (min(q1[0], q2[0]), min(q1[1], q2[1]), max(q1[0], q2[0]), max(q1[1], q2[1]))
        bound = limit if best is None else min(best, limit)
        if _bbox_gap(seg_box, box) > bound:
            continue
        for p1, p2 in parcel["segments"]:
            d = segment_distance(p1, p2, q1, q2)
            if best is None or d < best:
                best = d
                if best == 0.0:
                    return 0.0
    if best is None or best > limit:
        return None
    return best


def sample_points(rings, target=4000, minimum=400):
    """A regular grid of points inside the parcel, for area shares."""
    box = bbox(rings)
    if not box:
        return []
    width, height = box[2] - box[0], box[3] - box[1]
    if width <= 0 or height <= 0:
        return []
    step = math.sqrt(width * height / float(target))
    points = []
    for _ in range(4):
        points = []
        y = box[1] + step / 2.0
        while y < box[3]:
            x = box[0] + step / 2.0
            while x < box[2]:
                if point_in_rings(x, y, rings):
                    points.append((x, y))
                x += step
            y += step
        if len(points) >= minimum:
            break
        step /= 2.0
    return points


def build_parcel_shape(geometry):
    """Project the parcel polygon to local feet and precompute what overlays need."""
    rings_ll, kind = geometry_parts(geometry)
    if kind != "polygon" or not rings_ll:
        return None
    box_ll = bbox(rings_ll)
    frame = Frame((box_ll[0] + box_ll[2]) / 2.0, (box_ll[1] + box_ll[3]) / 2.0)
    rings = frame.project(rings_ll)
    samples = sample_points(rings)
    if samples:
        cx = sum(p[0] for p in samples) / len(samples)
        cy = sum(p[1] for p in samples) / len(samples)
        interior = min(samples, key=lambda p: (p[0] - cx) ** 2 + (p[1] - cy) ** 2)
    else:
        verts = [p for ring in rings for p in ring]
        interior = (sum(p[0] for p in verts) / len(verts), sum(p[1] for p in verts) / len(verts))
    lon, lat = frame.to_lonlat(interior[0], interior[1])
    return {
        "frame": frame,
        "rings": rings,
        "bbox": bbox(rings),
        "bbox_ll": box_ll,
        "vertices": [p for ring in rings for p in ring],
        "segments": segments(rings, True),
        "samples": samples,
        "interior": interior,
        "interior_lonlat": (lon, lat),
        "area_sqft": rings_area(rings),
    }


def envelope_params(shape, pad_ft):
    frame = shape["frame"]
    box = shape["bbox"]
    xmin, ymin = frame.to_lonlat(box[0] - pad_ft, box[1] - pad_ft)
    xmax, ymax = frame.to_lonlat(box[2] + pad_ft, box[3] + pad_ft)
    return {
        "geometry": "%.8f,%.8f,%.8f,%.8f" % (xmin, ymin, xmax, ymax),
        "geometryType": "esriGeometryEnvelope",
        "inSR": "4326",
        "spatialRel": "esriSpatialRelIntersects",
    }


# ---------------------------------------------------------------------------
# Values
# ---------------------------------------------------------------------------

def clean(value):
    if isinstance(value, str):
        value = value.strip()
        return value or None
    return value


def as_int(value):
    value = clean(value)
    if isinstance(value, bool) or value is None:
        return value
    if isinstance(value, (int, float)):
        return int(round(value))
    text = str(value).replace(",", "")
    return int(text) if text.isdigit() else value


def is_yes(value):
    return str(clean(value) or "").lower() in ("yes", "y", "true", "1")


def public_attributes(attributes, fields):
    out = {}
    for field in fields:
        if field in PRIVATE_FIELDS or field not in (attributes or {}):
            continue
        value = clean(attributes[field])
        if value is not None:
            out[field] = value
    return out


def scrub(value):
    """Drop any private field name anywhere in the output (belt and braces)."""
    if isinstance(value, dict):
        return {k: scrub(v) for k, v in value.items() if k not in PRIVATE_FIELDS}
    if isinstance(value, list):
        return [scrub(v) for v in value]
    return value


# ---------------------------------------------------------------------------
# Parcel matching
# ---------------------------------------------------------------------------

PARCEL_OUT_FIELDS = ",".join(field for field, _, _ in PARCEL_FIELDS)


def parcel_rows_where(fetch, where, limit_pages=5):
    return arcgis_query(fetch, PARCEL_URL, {"where": where, "outFields": PARCEL_OUT_FIELDS}, max_pages=limit_pages)


def parcel_rows_at_point(fetch, lon, lat, distance_ft=None):
    params = {
        "geometry": "%.8f,%.8f" % (lon, lat),
        "geometryType": "esriGeometryPoint",
        "inSR": "4326",
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": PARCEL_OUT_FIELDS,
    }
    if distance_ft:
        params["distance"] = str(distance_ft)
        params["units"] = "esriSRUnit_Foot"
    return arcgis_query(fetch, PARCEL_URL, params)


def dedupe_rows(rows):
    seen = {}
    for row in rows:
        apn = canonical_apn((row.get("attributes") or {}).get("AP"))
        if apn and apn not in seen:
            seen[apn] = row
    return [seen[key] for key in sorted(seen)]


def row_address(row):
    return clean((row.get("attributes") or {}).get("ADDRESS"))


def candidate_summary(row, method):
    attributes = row.get("attributes") or {}
    return {
        "address": clean(attributes.get("ADDRESS")),
        "apn": clean(attributes.get("AP")),
        "zone": clean(attributes.get("ZONING")),
        "lot_area_sqft": as_int(attributes.get("AREA")),
        "legal_description": clean(attributes.get("LGLDSCRP")),
        "matched_by": method,
    }


FALLBACK_MESSAGES = {
    "unit_number": "The address matched a unit row. Unit rows usually carry the whole lot's area and outline, so lot facts describe the lot, not the unit.",
    "unit_base": "The address names a unit that has no parcel row of its own; matched the building's parcel. Lot facts describe the whole lot, not the unit.",
    "unit_suffix": "The address matches one unit row of a multi-unit property. Confirm the unit with the owner.",
    "street_type": "No parcel row has this exact address; matched the only parcel with the same house number and street name but a different or missing street type. Confirm the address with the owner.",
}


def choose_by_address(typed, rows):
    """Pick parcel rows for a typed address. Never picks one of several silently.

    Returns (status, method, rows, message). status is matched | needs_choice | not_found.
    """
    rows = dedupe_rows(rows)
    folded = fold_unit_designator(typed)
    variants = [typed] + ([folded] if folded else [])

    def matching(test, options):
        return [row for row in rows if row_address(row) and any(test(v, row_address(row)) for v in options)]

    exact = matching(addresses_match, variants)
    if len(exact) == 1:
        if addresses_match(typed, row_address(exact[0])):
            units = [row for row in rows if row is not exact[0] and row_address(row) and matches_with_unit_suffix(typed, row_address(row))]
            message = None
            if units:
                message = ("Other parcel rows (%d) carry this street address plus a unit number (condominium or air-space units). "
                           "The matched row is the one without a unit; if the project is in one unit, re-run with that unit's APN." % len(units))
            return "matched", "exact_address", exact, message
        return "matched", "unit_number", exact, FALLBACK_MESSAGES["unit_number"]
    if len(exact) > 1:
        return "needs_choice", "exact_address", exact, (
            "This address is on %d parcels. Choose an APN (re-run with --apn) before using lot-specific facts." % len(exact))
    base = strip_unit_designator(typed)
    tiers = [
        ("unit_base", matching(addresses_match, [base]) if base else []),
        ("unit_suffix", matching(matches_with_unit_suffix, variants)),
        ("street_type", matching(addresses_match_ignoring_type, variants + ([base] if base else []))),
    ]
    for method, found in tiers:
        if len(found) == 1:
            return "matched", method, found, FALLBACK_MESSAGES[method]
        if len(found) > 1:
            return "needs_choice", method, found, (
                "No parcel row has exactly this address. %d parcels are close (%s). Choose an APN (re-run with --apn)."
                % (len(found), "; ".join("%s (APN %s)" % (row_address(r), clean(r["attributes"].get("AP"))) for r in found)))
    return "not_found", None, [], None


def unique_containing(rows, lon, lat):
    hits = []
    for row in rows:
        rings, kind = geometry_parts(row.get("geometry"))
        if kind == "polygon" and point_in_rings(lon, lat, rings):
            hits.append(row)
    return hits[0] if len(hits) == 1 else None


def census_points(fetch, address):
    line = address if named_city(address) else address.strip() + ", " + CITY + ", CA"
    payload = fetch(CENSUS_URL, {"address": line, "benchmark": "Public_AR_Current", "format": "json"})
    matches = ((payload.get("result") or {}).get("addressMatches")) or []
    out = []
    for match in matches:
        coordinates = match.get("coordinates") or {}
        if "x" in coordinates and "y" in coordinates:
            out.append((float(coordinates["x"]), float(coordinates["y"]), match.get("matchedAddress")))
    return out


def find_parcel(fetch, address=None, apn=None, lat=None, lon=None):
    """Returns a match dict: status, method, message, row (when matched), candidates, notes."""
    notes = []
    has_point = lat is not None and lon is not None

    if apn:
        printed = format_apn(apn)
        rows = dedupe_rows(parcel_rows_where(fetch, "AP = " + sql_quote(printed)))
        rows = [r for r in rows if canonical_apn(r["attributes"].get("AP")) == canonical_apn(printed)]
        if len(rows) == 1:
            if address and not addresses_match(address, row_address(rows[0]) or ""):
                notes.append("The APN's parcel row is addressed %r, not %r. Facts are for the APN." % (row_address(rows[0]), address))
            return {"status": "matched", "method": "apn", "row": rows[0], "candidates": [], "message": None, "notes": notes}
        return {"status": "not_found", "method": "apn", "row": None, "candidates": [],
                "message": "No City parcel has APN %s." % printed, "notes": notes}

    if address:
        city = named_city(address)
        if city and city.lower() != CITY.lower():
            notes.append("The address names %s. This tool reads only City of Laguna Beach parcels." % city)
        number, street = search_terms(address)
        if not number or not street:
            return {"status": "not_found", "method": None, "row": None, "candidates": [],
                    "message": "The address needs a house number and a street name.", "notes": notes}
        where = "UPPER(ADDRESS) LIKE " + sql_quote("%s %%%s%%" % (number.upper(), street.upper()))
        rows = parcel_rows_where(fetch, where)
        status, method, chosen, message = choose_by_address(address, rows)
        if status == "needs_choice" and has_point:
            picked = unique_containing(chosen, lon, lat)
            if picked:
                return {"status": "matched", "method": method + "+coordinates", "row": picked, "candidates": [],
                        "message": "Several parcels share this address; the supplied coordinates fall in one of them.", "notes": notes}
        if status == "matched":
            if message:
                notes.append(message)
            return {"status": "matched", "method": method, "row": chosen[0], "candidates": [], "message": message, "notes": notes}
        if status == "needs_choice":
            return {"status": "needs_choice", "method": method, "row": None,
                    "candidates": [candidate_summary(r, method) for r in chosen], "message": message, "notes": notes}

    if has_point:
        rows = dedupe_rows(parcel_rows_at_point(fetch, lon, lat))
        if len(rows) == 1:
            if address:
                notes.append("No City parcel row carries the typed address; matched the parcel at the supplied coordinates (%s, APN %s). Confirm the address." % (row_address(rows[0]), clean(rows[0]["attributes"].get("AP"))))
            return {"status": "matched", "method": "point", "row": rows[0], "candidates": [], "message": None, "notes": notes}
        if len(rows) > 1:
            return {"status": "needs_choice", "method": "point", "row": None,
                    "candidates": [candidate_summary(r, "point") for r in rows],
                    "message": "%d parcel rows share the location at these coordinates (often condominium or air-space units). Choose an APN." % len(rows),
                    "notes": notes}
        near = dedupe_rows(parcel_rows_at_point(fetch, lon, lat, distance_ft=60))
        if near:
            return {"status": "needs_choice", "method": "near_point", "row": None,
                    "candidates": [candidate_summary(r, "near_point") for r in near[:8]],
                    "message": "No parcel contains these coordinates (they may fall in a street). These parcels are within 60 ft. Choose an APN (re-run with --apn).",
                    "notes": notes}
        return {"status": "not_found", "method": "point", "row": None, "candidates": [],
                "message": "No City of Laguna Beach parcel is at or within 60 ft of these coordinates.", "notes": notes}

    if address:
        # Last resort: a public geocoder point, offered as candidates only.
        candidates = []
        try:
            points = census_points(fetch, address)
        except FetchError as exc:
            notes.append("The US Census geocoder could not be reached (%s)." % exc)
            points = []
        for x, y, matched in points[:3]:
            near = dedupe_rows(parcel_rows_at_point(fetch, x, y, distance_ft=60))
            for row in near:
                summary = candidate_summary(row, "census_geocoder_point")
                summary["geocoder_matched_address"] = matched
                if summary["apn"] not in [c["apn"] for c in candidates]:
                    candidates.append(summary)
        if candidates:
            return {"status": "needs_choice", "method": "census_geocoder_point", "row": None, "candidates": candidates[:8],
                    "message": "No City parcel row carries this address. These parcels are near where the US Census geocoder places it. Choose an APN (re-run with --apn); never assume the first one.",
                    "notes": notes}
        return {"status": "not_found", "method": None, "row": None, "candidates": [],
                "message": "No City of Laguna Beach parcel matches this address. Check the spelling, or the parcel may be outside the City (unincorporated areas such as Emerald Bay use Laguna Beach mailing addresses). Re-run with --apn or --lat/--lon.",
                "notes": notes}

    return {"status": "not_found", "method": None, "row": None, "candidates": [],
            "message": "Give --address, --apn or --lat/--lon.", "notes": notes}


# ---------------------------------------------------------------------------
# Parcel and overlays
# ---------------------------------------------------------------------------

def parcel_facts(row, shape):
    attributes = row.get("attributes") or {}
    out = {}
    sources = {}
    for field, key, _ in PARCEL_FIELDS:
        value = clean(attributes.get(field))
        if key in INTEGER_KEYS:
            value = as_int(value)
        out[key] = value
        sources[key] = field
    constraints = out.get("environmental_constraints")
    out["environmental_constraint_flags"] = [t.strip() for t in constraints.split("/") if t.strip()] if constraints else []
    if shape:
        out["lot_area_gis_sqft"] = int(round(shape["area_sqft"]))
        lon, lat = shape["interior_lonlat"]
        out["interior_point"] = {"lat": round(lat, 7), "lon": round(lon, 7)}
    out["source_fields"] = sources
    out["source_url"] = PARCEL_URL
    return out


def feature_label(spec_id, attributes):
    oid = str(attributes.get("OBJECTID", ""))
    if spec_id == "specific_plan":
        name = clean(attributes.get("Name"))
        return SOURCE_DATA["specific_plan_aliases"].get(name, name), "City layer"
    if spec_id == "coastal_deferred":
        name = clean(attributes.get("Name")) or SOURCE_DATA["deferred_certification_names"].get(oid)
        return name, "Coastal Commission LCP records (the City layer has no name)"
    if spec_id == "open_space_preserve":
        entry = SOURCE_DATA["open_space_preserve_names"].get(oid)
        if entry:
            return entry["name"], "public park records, %s confidence (the City layer has no name)" % entry["confidence"]
        return None, None
    if spec_id == "fuel_modification":
        parts = [clean(attributes.get("Number")), clean(attributes.get("Name"))]
        return " ".join(p for p in parts if p) or None, "Fire Department layer"
    if spec_id in ("habitat_vhvh", "habitat_hvh"):
        return clean(attributes.get("VERYHIGH")), "City layer"
    if spec_id == "wqesa":
        return clean(attributes.get("WQESA")), "City layer"
    if spec_id == "coastal_appeal":
        return clean(attributes.get("Name")), "City layer"
    return None, None


def overlay_entry(spec):
    layer = LAYER_URLS[spec["id"]]
    entry = {
        "name": layer["name"],
        "hit": "unknown",
        "label": None,
        "method": spec["method"],
        "basis": None,
        "skill_fact": spec["skill_fact"],
        "reads_as": layer["reads_as"],
        "source_url": layer["url"],
    }
    if layer.get("supplemental_urls"):
        entry["supplemental_source_urls"] = list(layer["supplemental_urls"])
    if spec.get("buffer_ft") is not None:
        entry["buffer_ft"] = spec["buffer_ft"]
        entry["buffer_basis"] = layer.get("buffer_basis")
    return entry


def describe_share(share):
    pct = share * 100.0
    if pct >= 99.95:
        return "all"
    if pct < 0.1:
        return "under 0.1%"
    return "about %s%%" % (("%.1f" % pct) if pct < 1 else ("%d" % round(pct)))


def resolve_geometric(fetch, spec, shape):
    entry = overlay_entry(spec)
    layer = LAYER_URLS[spec["id"]]
    urls = [layer["url"]] + list(layer.get("supplemental_urls") or [])
    field_lists = [spec["fields"]] + list(spec.get("supplemental_fields") or [])
    if len(field_lists) != len(urls):
        raise ValueError("%s: one field list per layer URL" % spec["id"])
    pad = max(NEARBY_FT, (spec.get("buffer_ft") or 0) + 50.0)
    frame = shape["frame"]
    measured = []
    for url, fields in zip(urls, field_lists):
        params = envelope_params(shape, pad)
        params["outFields"] = ",".join(fields)
        for feature in arcgis_query(fetch, url, params):
            parts_ll, kind = geometry_parts(feature.get("geometry"))
            if not kind:
                continue
            parts = frame.project(parts_ll)
            distance = distance_to_parcel(shape, parts, kind, pad)
            if distance is None:
                continue
            attributes = feature.get("attributes") or {}
            item = {"distance_ft": round(distance, 1)}
            if kind == "polygon":
                edges = edges_near(parts, shape["bbox"]) if distance == 0 else []
                inside = sum(1 for p in shape["samples"] if point_in_edges(p[0], p[1], edges)) if distance == 0 else 0
                share = inside / float(len(shape["samples"])) if shape["samples"] else 0.0
                item["share_of_parcel"] = round(share, 4)
                item["contains_interior_point"] = distance == 0 and point_in_edges(shape["interior"][0], shape["interior"][1], edges)
                item["_edges"] = edges
            label, label_source = feature_label(spec["id"], attributes)
            item["label"] = label
            if label and label_source:
                item["label_source"] = label_source
            item["attributes"] = public_attributes(attributes, fields)
            if len(urls) > 1:
                item["source_url"] = url
            measured.append(item)

    measured.sort(key=lambda m: (-(m.get("share_of_parcel") or 0), m["distance_ft"]))
    method = spec["method"]
    if method == "line":
        nearest = measured[0]["distance_ft"] if measured else None
        hit = nearest is not None and nearest <= spec["buffer_ft"]
        entry["distance_ft"] = nearest
        entry["basis"] = (
            "nearest mapped line is %.0f ft from the parcel (screening distance %.0f ft)" % (nearest, spec["buffer_ft"])
            if nearest is not None else "no mapped line within %.0f ft of the parcel" % pad)
    else:
        samples = shape["samples"]
        touching = [m for m in measured if m["distance_ft"] == 0]
        union = 0
        if samples and touching:
            union = sum(1 for p in samples if any(point_in_edges(p[0], p[1], m["_edges"]) for m in touching))
        share = union / float(len(samples)) if samples else 0.0
        interior = any(m.get("contains_interior_point") for m in touching)
        entry["share_of_parcel"] = round(share, 4)
        entry["contains_interior_point"] = interior
        entry["distance_ft"] = min(m["distance_ft"] for m in measured) if measured else None
        if method == "touch":
            hit = bool(touching)
            entry["basis"] = (
                "a mapped area touches the parcel (covers %s of it)" % describe_share(share) if hit else
                ("nearest mapped area is %.0f ft away" % entry["distance_ft"] if measured else "no mapped area within %.0f ft" % pad))
        else:
            hit = share >= SLIVER_SHARE or interior
            if hit:
                entry["basis"] = "covers %s of the parcel" % describe_share(share)
            elif touching:
                entry["basis"] = "touches only an edge sliver of the parcel (%s, under 2%%, likely a mapping edge); not counted" % describe_share(share)
                entry["edge_sliver"] = True
            elif measured:
                entry["basis"] = "does not touch the parcel; nearest mapped area is %.0f ft away" % entry["distance_ft"]
            else:
                entry["basis"] = "no mapped area within %.0f ft of the parcel" % pad
    for m in measured:
        m.pop("_edges", None)
    entry["hit"] = bool(hit)
    hits = [m for m in measured if (m["distance_ft"] == 0 if method != "line" else m["distance_ft"] <= spec["buffer_ft"])]
    labels = []
    for m in hits:
        if m.get("label") and m["label"] not in labels:
            labels.append(m["label"])
    entry["label"] = "; ".join(labels) if (labels and hit) else None
    entry["features"] = measured[:8]
    return entry


def resolve_record(fetch, spec, row, shape):
    entry = overlay_entry(spec)
    layer = LAYER_URLS[spec["id"]]
    apn = clean((row.get("attributes") or {}).get("AP"))
    keys = apn_key_variants(apn)
    where = "%s IN (%s)" % (spec["key_field"], ", ".join(sql_quote(k) for k in keys))
    params = {"where": where, "outFields": ",".join(spec["fields"]), "returnGeometry": "false"}
    records = arcgis_query(fetch, layer["url"], params) if apn else []
    matched_by = "apn"
    if not records and spec["id"] != "historic" and shape:
        lon, lat = shape["interior_lonlat"]
        records = arcgis_query(fetch, layer["url"], {
            "geometry": "%.8f,%.8f" % (lon, lat), "geometryType": "esriGeometryPoint", "inSR": "4326",
            "spatialRel": "esriSpatialRelIntersects", "outFields": ",".join(spec["fields"]), "returnGeometry": "false",
        })
        matched_by = "interior_point"
    attrs = [public_attributes(r.get("attributes") or {}, spec["fields"]) for r in records]
    entry["records"] = attrs[:5]
    if spec["id"] == "historic":
        entry["hit"] = bool(attrs)
        first = attrs[0] if attrs else {}
        entry["on_register"] = is_yes(first.get("HISTREG_ST")) if attrs else False
        parts = []
        if entry["on_register"]:
            number = first.get("HISTREGNUM")
            parts.append("Historic Register" + ((" #%s" % number) if number not in (None, 0, "0") else ""))
        if first.get("HISTRATE"):
            parts.append("inventory rating %s" % first["HISTRATE"])
        label = ", ".join(parts)
        entry["label"] = (label[:1].upper() + label[1:]) if label else None
        entry["basis"] = "a historic layer row carries this APN" if attrs else "no historic layer row carries this APN"
        return entry
    if not attrs:
        entry["basis"] = "no row for this APN or at the parcel's interior point"
        return entry
    entry["matched_by"] = matched_by
    first = attrs[0]
    if spec["id"] == "zoning":
        codes = [first.get(k) for k in ("ZONING1", "ZONING2", "ZONING3") if first.get(k)]
        entry["hit"] = True
        entry["label"] = " / ".join(codes) or None
        entry["basis"] = "zoning map row matched by %s" % matched_by.replace("_", " ")
    elif spec["id"] == "cat_exclusion":
        entry["hit"] = is_yes(first.get("CatExclusion"))
        entry["label"] = first.get("CatExclusionName") if entry["hit"] else None
        entry["basis"] = "parcel row (matched by %s) reads CatExclusion = %s" % (matched_by.replace("_", " "), first.get("CatExclusion"))
    if len(attrs) > 1:
        entry["note"] = "%d rows matched; the first is reported." % len(attrs)
    return entry


def resolve_overlay(fetch, spec, row, shape):
    try:
        if spec["method"] == "record":
            return resolve_record(fetch, spec, row, shape), None
        if not shape:
            entry = overlay_entry(spec)
            entry["basis"] = "the parcel has no usable geometry"
            return entry, {"layer": spec["id"], "url": entry["source_url"], "error": "parcel geometry missing"}
        return resolve_geometric(fetch, spec, shape), None
    except Exception as exc:  # one layer failing never stops the others
        entry = overlay_entry(spec)
        entry["basis"] = "layer could not be read"
        return entry, {"layer": spec["id"], "url": entry["source_url"], "error": "%s: %s" % (type(exc).__name__, exc)}


def comparison_notes(parcel, overlays):
    notes = []
    zoning = overlays.get("zoning") or {}
    parcel_zone = parcel.get("zone")
    map_zone = None
    for record in zoning.get("records") or []:
        map_zone = record.get("ZONING1")
        break
    if parcel_zone and map_zone and re.sub(r"[^0-9A-Z]", "", parcel_zone.upper()) != re.sub(r"[^0-9A-Z]", "", map_zone.upper()):
        notes.append("The parcel record lists zone %s; the zoning map lists %s. Confirm the zone with Planning." % (parcel_zone, map_zone))
    recorded, measured = parcel.get("lot_area_sqft"), parcel.get("lot_area_gis_sqft")
    if isinstance(recorded, int) and isinstance(measured, int) and recorded > 0 and abs(recorded - measured) > 0.1 * recorded:
        notes.append("The recorded lot area (%d sq ft) and the mapped parcel polygon (%d sq ft) differ by more than 10%%. Use the survey or the recorded map for lot area." % (recorded, measured))
    return notes


def lookup(address=None, apn=None, lat=None, lon=None, fetch=http_get_json, workers=6, now=None):
    result = {
        "tool": "laguna-beach parcel_facts",
        "version": VERSION,
        "queried_at": now or datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "query": {"address": address, "apn": apn, "lat": lat, "lon": lon},
        "match": None,
        "parcel": None,
        "overlays": {},
        "not_available": NOT_AVAILABLE,
        "notes": [],
        "errors": [],
    }
    try:
        match = find_parcel(fetch, address=address, apn=apn, lat=lat, lon=lon)
    except FetchError as exc:
        result["match"] = {"status": "error", "method": None, "message": "The City parcel layer could not be read.", "candidates": []}
        result["errors"].append({"layer": "parcel", "url": PARCEL_URL, "error": str(exc)})
        return scrub(result)
    row = match.pop("row")
    result["notes"].extend(match.pop("notes"))
    result["match"] = match
    if match["status"] != "matched":
        result["notes"].extend(STATIC_NOTES)
        return scrub(result)

    shape = build_parcel_shape(row.get("geometry"))
    result["parcel"] = parcel_facts(row, shape)
    if not shape:
        result["errors"].append({"layer": "parcel", "url": PARCEL_URL, "error": "the parcel row has no polygon geometry"})

    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        futures = [(spec, pool.submit(resolve_overlay, fetch, spec, row, shape)) for spec in OVERLAY_SPECS]
        for spec, future in futures:
            entry, error = future.result()
            result["overlays"][spec["id"]] = entry
            if error:
                result["errors"].append(error)
    result["notes"].extend(comparison_notes(result["parcel"], result["overlays"]))
    result["notes"].extend(STATIC_NOTES)
    return scrub(result)


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Laguna Beach parcel facts from the City's public GIS layers.")
    parser.add_argument("--address", help="street address, e.g. \"<number> <street>, Laguna Beach, CA\"")
    parser.add_argument("--apn", help="assessor parcel number, e.g. 123-456-78")
    parser.add_argument("--lat", type=float, help="latitude (WGS84)")
    parser.add_argument("--lon", type=float, help="longitude (WGS84)")
    parser.add_argument("--out", help="also write the JSON to this file")
    args = parser.parse_args(argv)
    if (args.lat is None) != (args.lon is None):
        parser.error("--lat and --lon go together")
    if not (args.address or args.apn or args.lat is not None):
        parser.error("give --address, --apn or --lat/--lon")
    return args


def main(argv=None):
    args = parse_args(sys.argv[1:] if argv is None else argv)
    result = lookup(address=args.address, apn=args.apn, lat=args.lat, lon=args.lon)
    text = json.dumps(result, indent=2, ensure_ascii=True)
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    sys.stdout.write(text + "\n")
    status = (result.get("match") or {}).get("status")
    if status == "matched":
        return 0
    if status == "error":
        return 1
    return 2


if __name__ == "__main__":
    sys.exit(main())
