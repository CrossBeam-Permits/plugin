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


def stacked(document: dict[str, Any], page: int, name: str, count: int) -> list[dict[str, Any]]:
    """Widgets that share one field name on one page, top of the page first."""

    widgets = sorted(widgets_named(document, page, name), key=lambda item: -item["rect"][3])
    if len(widgets) != count:
        raise ValueError(f"{name} page {page}: expected {count} widgets, got {len(widgets)}")
    return widgets


def stacked_lines(fact_id: str, document: dict[str, Any], page: int, name: str, count: int) -> dict[str, Any]:
    """A multi-line answer over one field's stacked widgets (one field name, several lines)."""

    return {
        "fact_id": fact_id,
        "pdf_widgets": [
            {"page": page, "field_name": widget["field_name"], "rect": widget["rect"]}
            for widget in stacked(document, page, name, count)
        ],
        "required": True,
        "applicant_controlled": False,
        "transform": "lines",
    }


CONTACT_ROLES = ("applicant", "applicant_representative", "owner")
CONTACT_ITEMS = ("company_name", "contact_name", "mailing_address", "city_state_zip", "phone", "email")
REQUIRED_CONTACTS = {"applicant.contact_name", "applicant.phone", "applicant.email", "owner.contact_name"}


def contact_block(targets: dict[str, list[Any]]) -> list[dict[str, Any]]:
    """Applicant, representative, and owner rows of the City's Planning application face.

    `targets` gives, per contact item, three targets in role order: a PDF field name, or
    a widget (page/field_name/rect) where the City reused one name across blocks.
    """

    mappings = []
    for index, role in enumerate(CONTACT_ROLES):
        for item in CONTACT_ITEMS:
            fact_id = f"{role}.{item}"
            target = targets[item][index]
            options = {"required": fact_id in REQUIRED_CONTACTS, "controlled": True}
            if isinstance(target, str):
                mappings.append(direct(fact_id, target, **options))
            else:
                mappings.append(exact(fact_id, target["page"], target["field_name"], target["rect"], **options))
    return mappings


def with_font(mappings: list[dict[str, Any]], size: float = 7) -> list[dict[str, Any]]:
    for mapping in mappings:
        if mapping["transform"] != "checkbox":
            mapping["font_size"] = size
    return mappings


def add_column_widgets(
    mappings: list[dict[str, Any]],
    document: dict[str, Any],
    field_name: str,
    fact_base: str,
    page: int,
) -> None:
    widgets = widgets_named(document, page, field_name)
    if len(widgets) != 4:
        raise ValueError(f"{field_name}: expected four page-{page} widgets, got {len(widgets)}")
    columns = ("required", "existing", "proposed", "conforms")
    for column, widget in zip(columns, widgets):
        mappings.append(
            exact(
                f"{fact_base}.{column}",
                page,
                field_name,
                widget["rect"],
                transform="yes_no" if column == "conforms" else "string",
            )
        )


def common_planning_face(prefix: str = "") -> list[dict[str, Any]]:
    rows = {
        "company_name": (6, 16, 22),
        "contact_name": (8, 17, 23),
        "mailing_address": (10, 18, 24),
        "city_state_zip": (12, 19, 26),
        "phone": (14, 20, 27),
        "email": (15, 21, 28),
    }
    mappings = [
        direct("site.address", f"{prefix}Text2", required=True),
        direct("site.apn", f"{prefix}Text4"),
        *contact_block({item: [f"{prefix}Text{n}" for n in numbers] for item, numbers in rows.items()}),
        direct("project.description", f"{prefix}Text32", required=True),
    ]
    return with_font(mappings)


def design_review(document: dict[str, Any]) -> list[dict[str, Any]]:
    return common_planning_face() + project_summary_tables(document, 25)


def project_summary_tables(document: dict[str, Any], page: int) -> list[dict[str, Any]]:
    """The City's Project Summary Tables exhibit (one page, same field names in every package)."""

    mappings: list[dict[str, Any]] = []
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
        add_column_widgets(mappings, document, field_name, fact_base, page)

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


# Laguna Beach issues Building permits only to an owner-builder or a contractor with a
# City business license. The applicant declares which; contractor blocks are filled only
# after the applicant confirms a licensed-contractor permit (references/applicant-confirmations.md).
CONTRACTOR_ONLY = {"fact_id": "permittee.type", "equals": "licensed_contractor"}

# Signature locations on the portal-linked Building Permit Application. Page 1 has no
# signature widget; the box is located from the printed "SIGNATURE:" and "DATE:" labels.
# The applicant signs these after fill and verify; the agent never fills them.
BUILDING_SIGNATURE_BLOCKS = [
    {"id": "application_signature", "page": 1, "rect": [108.0, 15.0, 408.0, 35.0], "kind": "signature", "pdf_field": None, "label": "Page 1 SIGNATURE"},
    {"id": "application_signature_date", "page": 1, "rect": [444.0, 15.0, 574.0, 35.0], "kind": "date", "pdf_field": None, "label": "Page 1 DATE beside the signature"},
    {"id": "stormwater_signature", "page": 2, "rect": [78.8845, 143.049, 374.795, 165.049], "kind": "signature", "pdf_field": "Text32", "label": "Stormwater Quality Certification Signed:"},
    {"id": "stormwater_signature_date", "page": 2, "rect": [415.561, 145.111, 572.78, 167.111], "kind": "date", "pdf_field": "Date34_af_date", "label": "Stormwater Quality Certification Date:"},
]


def building() -> list[dict[str, Any]]:
    """Portal-linked two-page Building Permit Application (PDF modified 2024-09-27).

    Widget names on this form do not follow their labels (for example "Text37" is the
    architect/designer name and "New SF" is the commercial new-structure area). Each name
    below was resolved against the rendered page by widget rectangle.
    """

    checkbox = {"transform": "checkbox", "on_value": "/Yes"}
    contractor = {"controlled": True}
    mappings = [
        direct("application.date", "Date31_af_date", controlled=True),
        direct("site.address", "PROJECT ADDRESS", required=True),
        direct("project.description.{record_id}", *(f"Description of Work {number}" for number in range(1, 7)), required=True, transform="lines"),
        direct("project.use.residential", "Check Box38", **checkbox),
        direct("project.use.commercial", "Check Box39", **checkbox),
        direct("project.use.fire", "Check Box40", **checkbox),
        direct("project.valuation.{record_id}", "Valuation of Work", required=True, controlled=True, transform="currency"),
        direct("applicant.name", "APPLICANT NAME If none of the below 1", required=True, controlled=True),
        direct("applicant.phone", "Phone", required=True, controlled=True),
        direct("applicant.email", "Email Address", required=True, controlled=True),
        direct("owner.name", "LEGAL PROPERTY OWNER NAME", required=True, controlled=True),
        direct("owner.phone", "Phone 1", controlled=True),
        direct("owner.email", "Email Address_2", controlled=True),
        direct("owner.mailing_address", "Mailing Address City State Zip", controlled=True),
        direct("contractor.license_name", "CONTRACTOR As Shown on License", **contractor),
        direct("contractor.dba", "DBA", **contractor),
        direct("contractor.license_number", "License", **contractor),
        direct("contractor.license_class", "Class", **contractor),
        direct("contractor.phone", "Phone 1_2", **contractor),
        direct("contractor.email", "Email", **contractor),
        direct("contractor.mailing_address", "Mailing Address City State Zip_2", **contractor),
        direct("architect_designer.name", "Text37", controlled=True),
        direct("architect_designer.license_number", "License_2", controlled=True),
        direct("architect_designer.phone", "Phone 1_3", controlled=True),
        direct("architect_designer.email", "Email_2", controlled=True),
        direct("architect_designer.mailing_address", "Mailing Address City State Zip_3", controlled=True),
        direct("engineer.name", "ENGINEER", controlled=True),
        direct("engineer.license_number", "License_3", controlled=True),
        direct("engineer.phone", "Phone_2", controlled=True),
        direct("engineer.email", "Email_3", controlled=True),
        direct("engineer.mailing_address", "Mailing Address City State Zip_4", controlled=True),
        direct("building.residential.new_structure_sqft", "New Structure SF"),
        direct("building.residential.new_garage_sqft", "New Garage SF"),
        direct("building.commercial.new_structure_sqft", "New SF"),
        direct("building.commercial.new_garage_sqft", "New Garage SF_2"),
        direct("building.residential.adu_sqft", "ADU SF"),
        direct("building.residential.adu_attached", "Check Box42", **checkbox),
        direct("building.residential.adu_detached", "Check Box43", **checkbox),
        direct("building.commercial.addition_sqft", "Addition SF"),
        direct("building.residential.addition_sqft", "Addition SF_3"),
        direct("building.commercial.tenant_improvement_sqft", "Tenant Improvement SF"),
        direct("building.commercial.tenant_improvement_interior", "Check Box50", **checkbox),
        direct("building.commercial.tenant_improvement_exterior", "Check Box51", **checkbox),
        direct("building.residential.remodel_sqft", "Remodel SF"),
        direct("building.residential.remodel_interior", "Check Box45", **checkbox),
        direct("building.residential.remodel_exterior", "Check Box44", **checkbox),
        direct("building.commercial.outside_seating_sqft", "Outside Seating SF"),
        direct("building.residential.alteration_or_repair", "Alteration  Repair circle one"),
        direct("building.commercial.alteration_or_repair", "Alteration  Repair circle one_2"),
        direct("building.residential.pool_spa_sqft", "POOL  SPA SF"),
        direct("building.commercial.sign_awning", "SIGN  Awning"),
        direct("building.residential.patio_cover_sqft", "Patio Cover SF"),
        direct("building.commercial.patio_cover_sqft", "Patio Cover SF_3"),
        direct("building.residential.deck_sqft", "Deck SF"),
        direct("building.commercial.deck_sqft", "Deck SF_3"),
        direct("building.residential.wall_fence_sqft", "Wall  Fence SF"),
        direct("building.residential.wall_fence_retaining", "Check Box46", **checkbox),
        direct("building.residential.wall_fence_property_line", "Check Box47", **checkbox),
        direct("building.commercial.wall_fence_sqft", "Wall  Fence SF_2"),
        direct("building.commercial.wall_fence_retaining", "Check Box52", **checkbox),
        direct("building.commercial.wall_fence_property_line", "Check Box53", **checkbox),
        direct("building.residential.reroof_sqft", "Reroof SF"),
        direct("building.residential.reroof_flat", "Check Box48", **checkbox),
        direct("building.residential.reroof_changes_color_or_material", "Check Box49", **checkbox),
        direct("building.commercial.reroof_sqft", "Reroof SF_2"),
        direct("building.commercial.reroof_flat", "Check Box55", **checkbox),
        direct("building.commercial.reroof_changes_color_or_material", "Check Box54", **checkbox),
        direct("building.residential.solar_description", "Solar"),
        direct("building.commercial.solar_description", "Solar_2"),
    ]
    for mapping in mappings:
        if mapping["fact_id"].startswith("contractor."):
            mapping["only_when"] = dict(CONTRACTOR_ONLY)
        if mapping["transform"] != "checkbox":
            mapping["font_size"] = 7

    # Page 2: Stormwater Quality Certification. The certifier is "the applicant authorizing
    # construction activities"; who that is stays an applicant confirmation.
    stormwater = [
        direct("stormwater_certification.certifier_name", "I", required=True, controlled=True),
        direct("site.address", "at", required=True),
        direct("stormwater_certification.certifier_name", "Text35", required=True, controlled=True),
        direct("stormwater_certification.certifier_address", "Address", required=True, controlled=True),
        direct("stormwater_certification.certifier_phone", "Text36", controlled=True),
        direct("stormwater_certification.certifier_email", "Text33", controlled=True),
    ]
    for mapping in stormwater:
        mapping["font_size"] = 9
    return mappings + stormwater


def adu(document: dict[str, Any]) -> list[dict[str, Any]]:
    """ADU & JADU Application, document 27032 (file ADU_Application 090126_fillable.pdf).

    Page 3 is the application face, page 4 the five description lines (one field, five
    widgets), page 9 the rent-reporting line, page 34 the Project Summary Tables.
    The deposit agreement, notices, Exhibit J dates, and the water quality form stay
    review-only, as on the other planning packages.
    """

    checkbox = {"transform": "checkbox", "on_value": "/Yes"}
    mappings = [
        direct("adu.application_type.adu_jadu_only", "Check Box35", **checkbox),
        direct("adu.application_type.adu_jadu_and_cdp", "Check Box36", **checkbox),
        direct("adu.application_type.with_new_dwelling", "Check Box37", **checkbox),
        direct("site.address", "Text38", required=True),
        direct("site.apn", "Text39"),
    ]
    # Text40-57: six fields per role block, read left to right, top to bottom: company,
    # contact, mailing address, city/state/zip, phone, email.
    mappings.extend(
        contact_block(
            {item: [f"Text{40 + role * 6 + offset}" for role in range(3)] for offset, item in enumerate(CONTACT_ITEMS)}
        )
    )
    mappings.append(stacked_lines("project.description", document, 4, "Text58", 5))
    mappings.append(direct("adu.projected_annualized_rent", "Text59", controlled=True))
    return with_font(mappings) + project_summary_tables(document, 34)


def conditional_use(document: dict[str, Any]) -> list[dict[str, Any]]:
    """Conditional Use Permit Application, document 26463 (CUP Application_Oct 2026_fillable.pdf).

    Page 2 is the application face. The applicant and representative rows share field
    names Text3-Text8 (top row = applicant), so those targets are exact widgets; the owner
    row is Text9-Text14. Page 25 holds the Project Summary Tables. The Exhibit J dates
    (page 40) stay review-only.
    """

    shared = {"company_name": "Text3", "mailing_address": "Text4", "phone": "Text5", "contact_name": "Text6", "city_state_zip": "Text7", "email": "Text8"}
    owner = {"company_name": "Text9", "mailing_address": "Text10", "phone": "Text11", "contact_name": "Text12", "city_state_zip": "Text13", "email": "Text14"}
    mappings = [
        direct("site.address", "Text1", required=True),
        direct("site.apn", "Text2"),
        *contact_block({item: [*stacked(document, 2, name, 2), owner[item]] for item, name in shared.items()}),
        direct("project.description", "Text15", required=True),
    ]
    return with_font(mappings) + project_summary_tables(document, 25)


SB9_MANUAL_SECTIONS = [
    {"pages": [2, 3, 4, 5], "title": "SB 9 Lot Split Application: I. Application Information, II. Property Owner's Letter of Agency, III. Project Information (questions 1-21)"},
    {"pages": [8, 9, 10], "title": "SB 9 Two-Unit Application: I. Application Information, II. Property Owner's Letter of Agency, III. Project Information"},
    {"pages": [38], "title": "Exhibit H Affidavit (owner name line)"},
    {"pages": [49], "title": "Bundled Coastal Development Permit Application Form"},
]


def sb9(document: dict[str, Any]) -> list[dict[str, Any]]:
    """SB 9 Application, document 26958 (file SB 9 Application_82526.pdf).

    The City built the application sections without form fields; only the exhibits are
    fillable. The Project Summary Tables (page 29) are mapped. The deposit agreement,
    notices, and water quality form stay review-only, as on the other planning packages.
    The flat sections are listed in `manual_sections` for the applicant to complete.
    """

    return project_summary_tables(document, 29)


SIGN_MANUAL_SECTIONS = [
    {"pages": [3], "title": "Sign Permit Application Form: project location, contact information, project description"},
    {"pages": [6], "title": "Exhibit A Affidavit (owner name line and owner signature)"},
    {"pages": [7], "title": "Exhibit B Use and Disclosure of Architectural Drawings (signatures and dates)"},
    {"pages": [8, 9, 10], "title": "Exhibit C Government Code Section 65940 Checklist (applicant signatures)"},
]


def temporary_use() -> list[dict[str, Any]]:
    """Temporary Use Permit Application, document 26473 (TUP Application 71426_fillable.pdf)."""

    mappings = [
        direct("site.address", "a Address", required=True),
        direct("site.apn", "b APNs"),
    ]
    mappings.extend(
        contact_block(
            {
                "company_name": ["Company Name", "Company Name_2", "Company Name_3"],
                "contact_name": ["Contact Name", "Contact Name_2", "Contact Name_3"],
                "mailing_address": ["Mailing Address", "Mailing Address_2", "Mailing Address_3"],
                "city_state_zip": ["CityStateZip", "CityStateZip_2", "CityStateZip_3"],
                "phone": ["Phone", "Phone_2", "Phone_3"],
                "email": ["Email Address", "Email Address_2", "Email Address_3"],
            }
        )
    )
    event_lines = [
        f"events number of attendees food and alcohol service live entertainment or amplification {line}"
        for line in range(1, 7)
    ]
    mappings.append(direct("temporary_use.event_description", *event_lines, required=True, transform="lines"))
    # Exhibit A: "I, ____, hereby certify that I am the property owner ..."
    mappings.append(
        direct(
            "owner_affidavit.owner_name",
            "property for which this application is submitted and hereby further certify to the following",
            controlled=True,
        )
    )
    return with_font(mappings)


def revocable_encroachment(document: dict[str, Any]) -> list[dict[str, Any]]:
    """Revocable Encroachment Permit Application, document 26469 (REP Application 71426_fillable.pdf).

    The City reused one field name for the same item in all three contact blocks, so those
    targets are exact widgets (top block = applicant). Pages 8-9 are the recordable license
    agreement the applicant completes after DRB approval; they stay review-only.
    """

    mappings = [
        direct("site.address", "Address", required=True),
        direct("site.apn", "APN(s)"),
    ]
    shared = {
        "company_name": "Company Name",
        "contact_name": "Contact Name",
        "mailing_address": "Mailing Address",
        "city_state_zip": "CityStateZip",
        "email": "Email Address",
    }
    columns = {item: stacked(document, 3, name, 3) for item, name in shared.items()}
    applicant_phone, owner_phone = stacked(document, 3, "Phone", 2)
    columns["phone"] = [applicant_phone, "Phone_2", owner_phone]  # the representative's phone is its own field
    mappings.extend(contact_block(columns))
    mappings.append(stacked_lines("project.description", document, 3, "Descibe proposed improvements", 6))
    # Exhibit A: "I, ____, hereby certify that I am the property owner ..."
    mappings.append(direct("owner_affidavit.owner_name", "Property Owner", controlled=True))
    return with_font(mappings)


def lot_line_adjustment() -> list[dict[str, Any]]:
    """Lot Line Adjustment Application, document 26467 (LLA Application_71426_fillable.pdf).

    Page 2 has one block per parcel (four). Pages 10-12 are Exhibits C, D, and E, each
    headed by the same Owners / Existing Parcels AP Numbers / Proposed Parcel Reference
    Number table; each row fact fills all three. The City assigns the LLA number.
    """

    mappings = []
    for parcel in range(1, 5):
        suffix = "" if parcel == 1 else f"_{parcel}"
        base = f"lot_line_adjustment.parcels.{parcel}"
        required = parcel <= 2
        mappings.extend(
            [
                direct(f"{base}.address", f"Address{suffix}", required=required),
                direct(f"{base}.apn", f"APNs{suffix}"),
                direct(f"{base}.owner_name", f"Property Owner{suffix}", required=required, controlled=True),
                direct(f"{base}.owner_mailing_address", f"Mailing Address{suffix}", controlled=True),
                direct(f"{base}.owner_city_state_zip", f"CityStateZip{suffix}", controlled=True),
                direct(f"{base}.owner_phone", f"Phone{suffix}", controlled=True),
                direct(f"{base}.owner_email", f"Email Address{suffix}", controlled=True),
            ]
        )
    mappings.append(
        direct(
            "owner_affidavit.owner_name",
            "property for which this application is submitted and hereby further certify to the following",
            controlled=True,
        )
    )
    for exhibit_suffix in ("", "_2", "_3"):
        for row in range(1, 4):
            base = f"lot_line_adjustment.exhibit_table.rows.{row}"
            mappings.extend(
                [
                    direct(f"{base}.owners", f"OwnersRow{row}{exhibit_suffix}", controlled=True),
                    direct(f"{base}.existing_apns", f"Existing Parcels AP NumbersRow{row}{exhibit_suffix}"),
                    direct(f"{base}.proposed_parcel_reference", f"Proposed Parcel Reference NumberRow{row}{exhibit_suffix}"),
                ]
            )
    return with_font(mappings)


def target_key(target: dict[str, Any]) -> tuple[Any, ...]:
    return (
        target["page"],
        target["field_name"],
        tuple(round(float(value), 3) for value in target["rect"]),
    )


def finalize(
    form_id: str,
    mappings: list[dict[str, Any]],
    *,
    version: str = "2.0.0",
    extras: dict[str, Any] | None = None,
) -> None:
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

    signature_fields = {
        block["pdf_field"]
        for block in (extras or {}).get("signature_blocks") or []
        if block.get("pdf_field")
    }
    if signature_fields & direct_fields:
        raise ValueError(f"{form_id}: signature fields must never be filled: {sorted(signature_fields & direct_fields)}")
    if signature_fields - fields:
        raise ValueError(f"{form_id}: signature field does not exist: {sorted(signature_fields - fields)}")

    document["field_map_version"] = version
    for key, value in (extras or {}).items():
        document[key] = value
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
    finalize(
        "conditional-use-permit-application",
        conditional_use(load_json(MAPS / "conditional-use-permit-application.json")),
    )
    zone_document = load_json(MAPS / "zone-clearance-application.json")
    finalize("zone-clearance-application", zone_clearance(zone_document))
    finalize(
        "building-application",
        building(),
        version="3.0.0",
        extras={
            "required_declarations": ["permittee.type"],
            "signature_blocks": BUILDING_SIGNATURE_BLOCKS,
        },
    )
    finalize("adu-application", adu(load_json(MAPS / "adu-application.json")))
    finalize(
        "sb-9-application",
        sb9(load_json(MAPS / "sb-9-application.json")),
        version="1.0.0",
        extras={"manual_sections": SB9_MANUAL_SECTIONS},
    )
    finalize(
        "sign-permit-application",
        [],
        version="1.0.0",
        extras={"manual_sections": SIGN_MANUAL_SECTIONS},
    )
    finalize("temporary-use-permit-application", temporary_use(), version="1.0.0")
    finalize(
        "revocable-encroachment-permit-application",
        revocable_encroachment(load_json(MAPS / "revocable-encroachment-permit-application.json")),
        version="1.0.0",
    )
    finalize("lot-line-adjustment-application", lot_line_adjustment(), version="1.0.0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
