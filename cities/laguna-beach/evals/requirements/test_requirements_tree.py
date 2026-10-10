"""Structure and publication checks for the generated requirements/ tree and the
hand-written plan-set check wiring. These are mechanical checks of files; they do
not judge any permit requirement."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REQ = ROOT / "requirements"


def load(rel: str):
    return json.loads((REQ / rel).read_text(encoding="utf-8"))


class GeneratedTree(unittest.TestCase):
    def test_index_and_core_files_exist(self):
        for rel in [
            "README.md",
            "building/checklists.json",
            "building/review-triggers.json",
            "building/adu-state-law.json",
            "planning/applications.json",
            "planning/application-index.md",
            "plan-sheets/plan-sheet-matrix.json",
            "plan-sheets/plan-sheet-matrix.md",
            "issuance/issuance-checklist.json",
            "fees/fee-schedule.json",
            "fees/README.md",
        ]:
            self.assertTrue((REQ / rel).is_file(), rel)

    def test_files_named_in_the_index_exist(self):
        index = (REQ / "README.md").read_text(encoding="utf-8")
        for rel in re.findall(r"`((?:building|planning|plan-sheets|issuance|fees)/[\w./-]+\.(?:md|json))`", index):
            self.assertTrue((REQ / rel).is_file(), rel)

    def test_brief_checklists_are_present(self):
        building = {item["id"] for item in load("building/checklists.json")["checklists"]}
        for checklist in ["residential", "interior-alterations", "grading", "demolition", "pool-spa", "wui-amendments", "otc", "express-permits"]:
            self.assertIn(checklist, building)
            self.assertTrue((REQ / "building" / f"{checklist}.md").is_file())
        planning = {item["id"] for item in load("planning/applications.json")["applications"]}
        for application in ["design-review", "coastal-development-permit", "adu", "zone-clearance", "conditional-use-permit", "variance"]:
            self.assertIn(application, planning)
        self.assertTrue((REQ / "planning/filing-context.md").is_file())

    def test_every_building_item_is_sourced_and_scoped(self):
        for checklist in load("building/checklists.json")["checklists"]:
            for item in checklist["items"]:
                self.assertTrue(item["source"].get("citation"), item["id"])
                self.assertTrue(item["scopes"], item["id"])
                self.assertIn(item["stage"], {"intake", "plan_check", "issuance"}, item["id"])
                if not item["source"].get("published", True):
                    self.assertIn("Confirm", item["source"]["note"])

    def test_plan_sheet_matrix_shape(self):
        matrix = load("plan-sheets/plan-sheet-matrix.json")
        self.assertEqual(len(matrix["columns"]), 16)
        self.assertGreaterEqual(len(matrix["rows"]), 20)
        keys = {column["key"] for column in matrix["columns"]}
        statuses = {"required", "conditional", "not_listed", "merged", "affected_sheets_only"}
        for row in matrix["rows"]:
            self.assertEqual(set(row["sheets"]), keys, row["row_key"])
            for cell in row["sheets"].values():
                self.assertIn(cell["status"], statuses)
                if cell["status"] == "conditional":
                    self.assertTrue(cell["city_text"])
        for key in keys - {"app-forms"}:
            self.assertTrue(matrix["sheet_contents"][key]["items"], key)
        self.assertIn("26714", matrix["source"])

    def test_issuance_items(self):
        issuance = load("issuance/issuance-checklist.json")
        self.assertGreaterEqual(len(issuance["items"]), 20)
        for item in issuance["items"]:
            self.assertTrue(item["handout_label"], item["id"])
            self.assertIn(item["decided_by"], {"project_scope", "city_record", "plans_examiner", "public_works", "city_staff"})

    def test_fee_schedule_is_labelled_estimate(self):
        fees = load("fees/fee-schedule.json")
        self.assertIn("ESTIMATE", fees["estimate_notice"])
        self.assertEqual(fees["city_slug"], "laguna-beach")
        self.assertTrue(fees["effective_from"])
        readme = (REQ / "fees/README.md").read_text(encoding="utf-8")
        self.assertIn("ESTIMATE", readme)
        self.assertIn(fees["effective_from"], readme)
        self.assertIn("What the City has not confirmed", readme)
        self.assertTrue(fees["source"]["url"].startswith("https://www.lagunabeachcity.net/"))

    def test_no_private_markers(self):
        patterns = {
            "internal path": re.compile(r"\b(?:data|docs|skills|server|frontend)/[\w./-]+"),
            "private file": re.compile(r"\b[\w-]+\.(?:ya?ml|csv|png|mjs|ts)\b"),
            "screener wording": re.compile(r"screener|needs_human|needs_source|tech[- ]?book|OneNote|internal_ref|staff_question", re.I),
            "City record number": re.compile(r"\b(?:[A-Z]{1,3}\d{2}-\d{3,5}|[A-Z]{2,4}-\d{4}-\d{2,5})\b"),
            "cost telemetry": re.compile(r"\b(?:input_tokens|output_tokens|cost_usd|cacheWrite)\b"),
        }
        for path in REQ.rglob("*"):
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for name, pattern in patterns.items():
                match = pattern.search(text)
                self.assertIsNone(match, f"{path.relative_to(ROOT)}: {name}: {match and match.group(0)}")


class HandWrittenWiring(unittest.TestCase):
    def test_plan_set_check_skill(self):
        skill = (ROOT / "skills/plan-set-check/SKILL.md").read_text(encoding="utf-8")
        frontmatter = skill.split("---", 2)[1]
        self.assertIn("name: plan-set-check", frontmatter)
        self.assertIn("completeness check", skill)
        self.assertIn("not a code", skill)
        self.assertIn("CrossBeam", skill)
        self.assertIn("pdftoppm", skill)
        for rel in re.findall(r"`(requirements/[\w./-]+\.(?:md|json))`", skill):
            self.assertTrue((ROOT / rel).is_file(), rel)
        for rel in re.findall(r"`(scripts/[\w./-]+\.py)`", skill):
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_packaging_requires_plan_set_check(self):
        text = (ROOT / "references/packaging-checklist.md").read_text(encoding="utf-8")
        self.assertIn("plan-set-check", text)
        self.assertTrue((ROOT / "skills/plan-set-check/SKILL.md").is_file())

    def test_guided_intake_site_facts(self):
        text = (ROOT / "references/guided-intake.md").read_text(encoding="utf-8")
        self.assertIn("crossbeam_get_site_facts", text)
        self.assertIn("https://gis.lagunabeachcity.net/Html5Viewer/index.html?viewer=LagunaBeachPublicGIS", text)
        self.assertIn("FeatureServer/34", text)


if __name__ == "__main__":
    unittest.main()
