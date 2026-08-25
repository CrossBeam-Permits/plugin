#!/usr/bin/env python3
"""Freeze human-reviewed semantic mappings into the current pinned Laguna form maps.

This is an authoring utility, not runtime inference. Widget labels were resolved against
rendered official pages. The emitted maps carry exact page/name/rectangle targets so the
filler fails closed on source drift.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from _lib import load_json, write_json


ROOT = Path(__file__).resolve().parent.parent
MAPS = ROOT / "assets" / "field-maps"


def direct(
    fact_id: str,
    *pdf_fields: str,
    required: bool = False,
    controlled: bool = False,
    transform: str = "string",
    on_value: str | None = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "fact_id": fact_id,
        "pdf_fields": list(pdf_fields),
        "required": required,
        "applicant_controlled": controlled,
        "transform": transform,
    }
    if on_value is not None:
        result["on_value"] = on_value
    return result


def exact(
    fact_id: str,
    page: int,
    field_name: str,
    rect: list[float],
    *,
    required: bool = False,
    controlled: bool = False,
    transform: str = "string",
) -> dict[str, Any]:
    return {
        "fact_id": fact_id,
        "pdf_widgets": [{"page": page, "field_name": field_name, "rect": rect}],
        "required": required,
        "applicant_controlled": controlled,
        "transform": transform,
    }


def widgets_named(document: dict[str, Any], page: int, name: str) -> list[dict[str, Any]]:
    return sorted(
        [
            item
            for item in document["widgets"]
            if item["page"] == page and item["field_name"] == name
        ],
        key=lambda item: (item["rect"][0], -item["rect"][1]),
    )


def add_column_widgets(
    mappings: list[dict[str, Any]],
    document: dict[str, Any],
    field_name: str,
    fact_base: str,
) -> None:
    widgets = widgets_named(document, 25, field_name)
    if len(widgets) != 4:
        raise ValueError(f"{field_name}: expected four page-25 widgets, got {len(widgets)}")
    columns = ("required", "existing", "proposed", "conforms")
    for column, widget in zip(columns, widgets):
        mappings.append(
            exact(
                f"{fact_base}.{column}",
                25,
                field_name,
                widget["rect"],
                transform="yes_no" if column == "conforms" else "string",
            )
        )


def common_planning_face(prefix: str = "") -> list[dict[str, Any]]:
    field = lambda value: f"{prefix}{value}"
    mappings = [
        direct("site.address", field("Text2"), required=True),
        direct("site.apn", field("Text4")),
        direct("applicant.company_name", field("Text6"), controlled=True),
        direct("applicant.contact_name", field("Text8"), required=True, controlled=True),
        direct("applicant.mailing_address", field("Text10"), controlled=True),
        direct("applicant.city_state_zip", field("Text12"), controlled=True),
        direct("applicant.phone", field("Text14"), required=True, controlled=True),
        direct("applicant.email", field("Text15"), required=True, controlled=True),
        direct("applicant_representative.company_name", field("Text16"), controlled=True),
        direct("applicant_representative.contact_name", field("Text17"), controlled=True),
        direct("applicant_representative.mailing_address", field("Text18"), controlled=True),
        direct("applicant_representative.city_state_zip", field("Text19"), controlled=True),
        direct("applicant_representative.phone", field("Text20"), controlled=True),
        direct("applicant_representative.email", field("Text21"), controlled=True),
        direct("owner.company_name", field("Text22"), controlled=True),
        direct("owner.contact_name", field("Text23"), required=True, controlled=True),
        direct("owner.mailing_address", field("Text24"), controlled=True),
        direct("owner.city_state_zip", field("Text26"), controlled=True),
        direct("owner.phone", field("Text27"), controlled=True),
        direct("owner.email", field("Text28"), controlled=True),
        direct("project.description", field("Text32"), required=True),
    ]
    for mapping in mappings:
        mapping["font_size"] = 7
    return mappings


def design_review(document: dict[str, Any]) -> list[dict[str, Any]]:
    mappings = common_planning_face()
    mappings.extend(
        [
            direct("site.use", "USE"),
            direct("site.zone", "ZONE"),
            direct("site.lot_slope_percent", "LOT SLOPE"),
        ]
    )

    zoning_metrics = {
        "LOT AREA": "zoning.lot_area_sqft",
        "LOT WIDTH AVG": "zoning.lot_width_average_ft",
        "LOT DEPTH AVG": "zoning.lot_depth_average_ft",
        "MAX BUILDING HEIGHT": "zoning.max_building_height_ft",
        "MAX HEIGHT FROM GRADE": "zoning.max_height_from_grade_ft",
    }
    for pdf_metric, fact_base in zoning_metrics.items():
        for column, prefix in (
            ("required", "REQUIRED"),
            ("existing", "EXISTING"),
            ("proposed", "PROPOSED"),
            ("conforms", "CONFORMS yesno"),
        ):
            mappings.append(
                direct(
                    f"{fact_base}.{column}",
                    f"{prefix}{pdf_metric}",
                    transform="yes_no" if column == "conforms" else "string",
                )
            )

    repeated_zoning = {
        "Front Yard": "zoning.front_yard_setback_ft",
        "Rear Yard": "zoning.rear_yard_setback_ft",
        "Side Yards combinedeach": "zoning.side_yards_combined_each_ft",
        "LOT COVERAGE BSC": "zoning.bsc_lot_coverage",
        "FLOOR AREA RATIO": "zoning.floor_area_ratio",
        "LANDSCAPE OPEN SPACE": "zoning.landscape_open_space",
        "IRRIGATED AREA": "zoning.irrigated_area",
        "PARKING": "zoning.parking_spaces",
    }
    for field_name, fact_base in repeated_zoning.items():
        add_column_widgets(mappings, document, field_name, fact_base)

    project_metrics = {
        "LIVING AREA": "living_area_sqft",
        "LOWER LEVEL": "lower_level_sqft",
        "UPPER LEVEL": "upper_level_sqft",
        "STORAGE": "storage_sqft",
        "TOTAL": "total_sqft",
        "GARAGE": "garage_sqft",
        "ELEVATED DECKTERRACE": "elevated_deck_terrace_sqft",
        "MECHANICAL": "mechanical_sqft",
    }
    for pdf_metric, fact_metric in project_metrics.items():
        for column in ("EXISTING", "PROPOSED", "TOTAL", "REMODEL"):
            mappings.append(
                direct(
                    f"project.area.{fact_metric}.{column.lower()}",
                    f"{column}{pdf_metric}",
                )
            )

    demolition_metrics = {
        "ROOF AREA": "roof_area",
        "FLOOR AREA": "floor_area",
        "LOWER LEVEL": "lower_level",
        "UPPER LEVEL": "upper_level",
        "TOTAL FLOOR  ROOF": "total_floor_and_roof",
        "TOTAL EXTERIOR WALL": "total_exterior_wall",
    }
    for pdf_metric, fact_metric in demolition_metrics.items():
        for column, prefix in (
            ("existing", "EXISTING"),
            ("removed", "REMOVED"),
            ("remaining", "REMAINING"),
            ("demo_total_percent", "DEMO TOTAL "),
        ):
            pdf_name = f"{prefix}{pdf_metric}"
            if column == "existing" and pdf_metric in {"LOWER LEVEL", "UPPER LEVEL"}:
                pdf_name += "_2"
            mappings.append(
                direct(
                    f"project.demolition.{fact_metric}.{column}",
                    pdf_name,
                )
            )

    grading_columns = {
        "OUTSIDE BUILDING FOOTPRINT": "outside_building_footprint",
        "INSIDE BUILDING FOOTPRINT": "inside_building_footprint",
        "POOLSPA": "pool_spa",
        "TOTAL": "total",
    }
    for pdf_action, fact_action in (("CUT", "cut"), ("FILL", "fill"), ("NET EXPORT", "net_export")):
        for prefix, fact_column in grading_columns.items():
            mappings.append(
                direct(
                    f"project.grading.{fact_action}.{fact_column}_cubic_yards",
                    f"{prefix}{pdf_action}",
                )
            )

    impervious_rows = {
        "structure": ("EXISTINGSTRUCTURE", "PROPOSEDSTRUCTURE", "EXISTINGSTRUCTURE_2", "PROPOSEDSTRUCTURE_2"),
        "hardscape_including_driveway": ("EXISTINGHARDSCAPE INCL DRIVEWAY", "PROPOSEDHARDSCAPE INCL DRIVEWAY", "EXISTINGHARDSCAPE INCL DRIVEWAY_2", "PROPOSEDHARDSCAPE INCL DRIVEWAY_2"),
        "total": ("EXISTINGTOTAL_2", "PROPOSEDTOTAL_2", "EXISTINGTOTAL_3", "PROPOSEDTOTAL_3"),
    }
    for fact_row, pdf_names in impervious_rows.items():
        mappings.extend(
            [
                direct(f"project.impervious.{fact_row}.lot_area.existing_sqft", pdf_names[0]),
                direct(f"project.impervious.{fact_row}.lot_area.proposed_sqft", pdf_names[1]),
                direct(f"project.impervious.{fact_row}.lot_percent.existing", pdf_names[2]),
                direct(f"project.impervious.{fact_row}.lot_percent.proposed", pdf_names[3]),
            ]
        )

    mappings.extend(
        [
            direct("project.pool.length_by_width", "DIMENSIONS L x W x DPOOL"),
            direct("project.pool.depth", "DIMENSIONS L x W x DPOOL_2"),
            direct("project.pool.volume_gallons", "VOLUMEGALLONSPOOL"),
            direct("project.spa.length_by_width", "DIMENSIONS L x W x DSPA"),
            direct("project.spa.depth", "DIMENSIONS L x W x DSPA_2"),
            direct("project.spa.volume_gallons", "VOLUMEGALLONSSPA"),
            direct("project.pool_spa.total_volume_gallons", "VOLUMEGALLONSTOTAL"),
            direct("project.lighting.exterior.existing_egress_doors", "EXISTING EGRESS DOORS"),
            direct("project.lighting.exterior.proposed_egress_doors", "PROPOSED EGRESS DOORS"),
            direct("project.lighting.exterior.existing_fixture_count", "EXISTING FIXTURE COUNT"),
            direct("project.lighting.exterior.proposed_fixture_count", "PROPOSED FIXTURE COUNT"),
            direct("project.lighting.landscape.existing_fixture_count", "EXISTING FIXTURE COUNT_2"),
            direct("project.lighting.landscape.proposed_fixture_count", "PROPOSED FIXTURE COUNT_2"),
        ]
    )
    for group, suffix in (("exterior", ""), ("landscape", "_2")):
        for row in range(1, 4):
            mappings.extend(
                [
                    direct(f"project.lighting.{group}.fixtures.{row}.type", f"FIXTURE TYPERow{row}{suffix}"),
                    direct(f"project.lighting.{group}.fixtures.{row}.wattage", f"WATTAGERow{row}{suffix}"),
                    direct(f"project.lighting.{group}.fixtures.{row}.lumens", f"LUMENSRow{row}{suffix}"),
                    direct(f"project.lighting.{group}.fixtures.{row}.quantity", f"QUANTITYRow{row}{suffix}"),
                    direct(f"project.lighting.{group}.fixtures.{row}.comments", f"COMMENTSRow{row}{suffix}"),
                ]
            )
        mappings.extend(
            [
                direct(f"project.lighting.{group}.total_quantity", f"QUANTITYTOTAL{suffix}"),
                direct(f"project.lighting.{group}.total_comments", f"COMMENTSTOTAL{suffix}"),
            ]
        )
    mappings.extend(
        [
            direct("project.lighting.combined.total_quantity", "QUANTITYCOMBINED TOTAL"),
            direct("project.lighting.combined.total_comments", "COMMENTSCOMBINED TOTAL"),
        ]
    )
    return mappings


def coastal_development() -> list[dict[str, Any]]:
    address_rect = [187.2, 488.546, 284.4, 510.546]
    contacts = [
        ("applicant.company_name", [149.945, 397.655, 270.272, 411.365]),
        ("applicant.mailing_address", [150.6, 379.11, 270.927, 392.819]),
        ("applicant.phone", [110.018, 359.474, 230.345, 373.183]),
        ("applicant_representative.company_name", [150.6, 325.001, 270.927, 338.71]),
        ("applicant_representative.mailing_address", [149.29, 309.292, 269.618, 323.001]),
        ("applicant_representative.phone", [108.709, 293.583, 229.036, 307.292]),
        ("owner.company_name", [150.163, 264.347, 270.49, 278.056]),
        ("owner.mailing_address", [151.036, 247.328, 271.363, 261.038]),
        ("owner.phone", [109.145, 232.365, 229.472, 246.074]),
        ("applicant.contact_name", [364.854, 399.619, 485.181, 413.328]),
        ("applicant.city_state_zip", [357.872, 378.237, 478.199, 391.946]),
        ("applicant.email", [361.799, 355.546, 482.126, 369.256]),
        ("applicant_representative.contact_name", [356.999, 338.092, 477.326, 351.801]),
        ("applicant_representative.city_state_zip", [357.435, 317.147, 477.763, 330.856]),
        ("applicant_representative.email", [357.872, 294.892, 478.199, 308.601]),
        ("owner.contact_name", [356.999, 275.256, 477.326, 288.965]),
        ("owner.city_state_zip", [357.872, 254.747, 478.199, 268.456]),
        ("owner.email", [357.872, 233.801, 478.199, 247.51]),
    ]
    mappings = [
        exact("site.address", 2, "Text17", address_rect, required=True),
        direct("site.apn", "Text19"),
        direct("project.description", "Text4", "Text6", "Text8", "Text2", required=True, transform="lines"),
    ]
    required_contacts = {"applicant.contact_name", "applicant.phone", "applicant.email", "owner.contact_name"}
    for fact_id, rect in contacts:
        mapping = exact(
            fact_id,
            2,
            "Text17",
            rect,
            required=fact_id in required_contacts,
            controlled=True,
        )
        if fact_id.endswith(".email"):
            mapping["output_y_offset"] = 2
        mappings.append(mapping)
    for mapping in mappings:
        mapping["font_size"] = 5
    return mappings


def zone_clearance(document: dict[str, Any]) -> list[dict[str, Any]]:
    definitions = [
        ("site.address", "Text1", 1, True, False),
        ("site.apn", "Text2", 1, False, False),
        ("applicant.company_name", "Text3", 1, False, True),
        ("applicant.contact_name", "Text4", 1, True, True),
        ("applicant.mailing_address", "Text5", 1, False, True),
        ("applicant.city_state_zip", "Text6", 1, False, True),
        ("applicant.phone", "Text7", 1, True, True),
        ("applicant.email", "Text8", 1, True, True),
        ("applicant_representative.company_name", "Text9", 1, False, True),
        ("applicant_representative.contact_name", "Text10", 1, False, True),
        ("applicant_representative.mailing_address", "Text11", 1, False, True),
        ("applicant_representative.city_state_zip", "Text12", 1, False, True),
        ("applicant_representative.phone", "Text13", 1, False, True),
        ("applicant_representative.email", "Text14", 1, False, True),
        ("owner.contact_name", "Text15", 1, True, True),
        ("owner.mailing_address", "Text16", 1, False, True),
        ("owner.phone", "Text17", 1, False, True),
        ("owner.city_state_zip", "Text18", 1, False, True),
        ("owner.email", "Text19", 1, False, True),
        ("project.description", "Text20", 2, True, False),
    ]
    mappings: list[dict[str, Any]] = []
    for fact_id, field_name, page, required, controlled in definitions:
        widgets = widgets_named(document, page, field_name)
        if len(widgets) != 1:
            raise ValueError(
                f"zone-clearance {field_name} page {page}: expected one widget, got {len(widgets)}"
            )
        mappings.append(
            exact(
                fact_id,
                page,
                field_name,
                widgets[0]["rect"],
                required=required,
                controlled=controlled,
            )
        )
    for mapping in mappings:
        mapping["font_size"] = 7
    return mappings


def building() -> list[dict[str, Any]]:
    checkbox = {"transform": "checkbox", "on_value": "/On"}
    mappings = [
        direct("application.date", "DATE", controlled=True),
        direct("site.address", "PROJECT ADDRESS", required=True),
        direct("project.description.{record_id}", *(f"Description of Work {number}" for number in range(1, 7)), required=True, transform="lines"),
        direct("project.use.residential", "Residential", **checkbox),
        direct("project.use.commercial", "Commercial", **checkbox),
        direct("project.use.fire", "Fire", **checkbox),
        direct("project.use.multi_family", "MultiFamily", **checkbox),
        direct("project.valuation.{record_id}", "Valuation of Work", required=True, controlled=True, transform="currency"),
        direct("applicant.name", "APPLICANT NAME If none of the below", required=True, controlled=True),
        direct("applicant.phone", "Phone", required=True, controlled=True),
        direct("applicant.email", "Email Address", required=True, controlled=True),
        direct("owner.name", "LEGAL PROPERTY OWNER NAME", required=True, controlled=True),
        direct("owner.phone", "Phone_2", controlled=True),
        direct("owner.email", "Email Address_2", controlled=True),
        direct("owner.mailing_address", "Mailing Address City State Zip", controlled=True),
        direct("contractor.license_name", "CONTRACTOR As Shown on License", controlled=True),
        direct("contractor.dba", "DBA", controlled=True),
        direct("contractor.license_number", "License", controlled=True),
        direct("contractor.license_class", "Class", controlled=True),
        direct("contractor.phone", "Phone_3", controlled=True),
        direct("contractor.email", "Email", controlled=True),
        direct("contractor.mailing_address", "Mailing Address City State Zip_2", controlled=True),
        direct("architect_designer.name", "Architect/Designer", controlled=True),
        direct("architect_designer.license_number", "License_2", controlled=True),
        direct("architect_designer.phone", "Phone_4", controlled=True),
        direct("architect_designer.email", "Email_2", controlled=True),
        direct("architect_designer.mailing_address", "Mailing Address City State Zip_3", controlled=True),
        direct("engineer.name", "ENGINEER", controlled=True),
        direct("engineer.license_number", "License_3", controlled=True),
        direct("engineer.phone", "Phone_5", controlled=True),
        direct("engineer.email", "Email_3", controlled=True),
        direct("engineer.mailing_address", "Mailing Address City State Zip_4", controlled=True),
        direct("building.residential.new_structure_sqft", "New Structure SF"),
        direct("building.residential.new_garage_sqft", "New Garage SF"),
        direct("building.commercial.new_structure_sqft", "New Structure SF_2"),
        direct("building.commercial.new_garage_sqft", "New Garage SF_2"),
        direct("building.residential.adu_sqft", "ADU SF"),
        direct("building.residential.adu_attached", "Attached", **checkbox),
        direct("building.residential.adu_detached", "Detached", **checkbox),
        direct("building.commercial.addition_sqft", "undefined"),
        direct("building.residential.addition_sqft", "undefined_2"),
        direct("building.commercial.tenant_improvement_sqft", "Tenant Improvement SF"),
        direct("building.commercial.tenant_improvement_interior", "Interior", **checkbox),
        direct("building.commercial.tenant_improvement_exterior", "Exterior", **checkbox),
        direct("building.residential.remodel_sqft", "Remodel SF"),
        direct("building.residential.remodel_interior", "Interior_2", **checkbox),
        direct("building.residential.remodel_exterior", "Exterior_2", **checkbox),
        direct("building.commercial.outside_seating_sqft", "undefined_3"),
        direct("building.residential.pool_spa_sqft", "1"),
        direct("building.residential.patio_cover_sqft", "2"),
        direct("building.commercial.sign_awning", "SIGN  Awning"),
        direct("building.commercial.patio_cover_sqft", "undefined_4"),
        direct("building.residential.deck_sqft", "undefined_5"),
        direct("building.commercial.deck_sqft", "undefined_6"),
        direct("building.residential.wall_fence_sqft", "Wall  Fence SF"),
        direct("building.residential.wall_fence_retaining", "Retaining", **checkbox),
        direct("building.residential.wall_fence_property_line", "Property Line", **checkbox),
        direct("building.commercial.wall_fence_sqft", "Wall  Fence SF_2"),
        direct("building.commercial.wall_fence_retaining", "Retaining_2", **checkbox),
        direct("building.commercial.wall_fence_property_line", "Property Line_2", **checkbox),
        direct("building.residential.reroof_sqft", "Reroof SF"),
        direct("building.residential.reroof_flat", "Flat", **checkbox),
        direct("building.residential.reroof_changes_color_or_material", "Change Color Material", **checkbox),
        direct("building.commercial.reroof_sqft", "Reroof SF_2"),
        direct("building.commercial.reroof_flat", "Flat_2", **checkbox),
        direct("building.commercial.reroof_changes_color_or_material", "Change Color Material_2", **checkbox),
        direct("building.residential.solar_description", "Solar"),
        direct("building.commercial.solar_description", "Solar_2"),
    ]
    for mapping in mappings:
        if mapping["transform"] != "checkbox":
            mapping["font_size"] = 7
    return mappings


def target_key(target: dict[str, Any]) -> tuple[Any, ...]:
    return (
        target["page"],
        target["field_name"],
        tuple(round(float(value), 3) for value in target["rect"]),
    )


def finalize(form_id: str, mappings: list[dict[str, Any]]) -> None:
    path = MAPS / f"{form_id}.json"
    document = load_json(path)
    fields = {item["name"] for item in document["fields"]}
    widgets_by_field: dict[str, list[dict[str, Any]]] = {}
    widget_keys: set[tuple[Any, ...]] = set()
    for widget in document["widgets"]:
        widgets_by_field.setdefault(widget["field_name"], []).append(widget)
        widget_keys.add(target_key(widget))

    direct_fields: set[str] = set()
    exact_keys: set[tuple[Any, ...]] = set()
    exact_parent_names: set[str] = set()
    for mapping in mappings:
        for name in mapping.get("pdf_fields") or []:
            if name not in fields:
                raise ValueError(f"{form_id}: mapped field does not exist: {name}")
            if len(widgets_by_field.get(name, [])) != 1:
                raise ValueError(
                    f"{form_id}: {name} has {len(widgets_by_field.get(name, []))} widgets; use exact targets"
                )
            if name in direct_fields:
                raise ValueError(f"{form_id}: duplicate direct mapping: {name}")
            direct_fields.add(name)
        for target in mapping.get("pdf_widgets") or []:
            key = target_key(target)
            if key not in widget_keys:
                raise ValueError(f"{form_id}: exact widget target does not exist: {key}")
            if key in exact_keys:
                raise ValueError(f"{form_id}: duplicate exact widget target: {key}")
            exact_keys.add(key)
            exact_parent_names.add(target["field_name"])

    document["field_map_version"] = "2.0.0"
    document["canonical_mappings"] = mappings
    document["review_fields"] = sorted(fields - direct_fields - exact_parent_names)
    document["review_widgets"] = sorted(
        [
            {
                "page": widget["page"],
                "field_name": widget["field_name"],
                "rect": widget["rect"],
            }
            for name in exact_parent_names
            for widget in widgets_by_field.get(name, [])
            if target_key(widget) not in exact_keys
        ],
        key=lambda item: (item["page"], item["field_name"], item["rect"]),
    )
    write_json(path, document)
    print(
        f"Authored {form_id}: {len(mappings)} semantic facts, "
        f"{len(direct_fields) + len(exact_keys)} exact targets, "
        f"{len(document['review_fields'])} review-only canonical fields"
    )


def main() -> int:
    design_document = load_json(MAPS / "design-review-application.json")
    finalize("design-review-application", design_review(design_document))
    finalize("coastal-development-permit-application", coastal_development())
    zone_document = load_json(MAPS / "zone-clearance-application.json")
    finalize("zone-clearance-application", zone_clearance(zone_document))
    finalize("building-application", building())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
