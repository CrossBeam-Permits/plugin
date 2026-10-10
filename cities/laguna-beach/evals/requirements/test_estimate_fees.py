"""Fee estimate command (scripts/estimate-fees.mjs).

The command must add no math of its own. Every expected number here comes from
calling calcFees in scripts/fees/fee-calc.mjs directly on the same schedule and
input, never from hand arithmetic. The scopes are fictional."""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "estimate-fees.mjs"
CALC = ROOT / "scripts" / "fees" / "fee-calc.mjs"
SCHEDULE = ROOT / "requirements" / "fees" / "fee-schedule.json"
NODE = shutil.which("node")

# Calls the shared calculator directly: the reference the command must match.
DIRECT = """
import fs from 'node:fs';
import { pathToFileURL } from 'node:url';
const [calcPath, schedulePath, input] = process.argv.slice(1);
const { calcFees, validateFeeSchedule } = await import(pathToFileURL(calcPath).href);
const schedule = validateFeeSchedule(JSON.parse(fs.readFileSync(schedulePath, 'utf8')));
process.stdout.write(JSON.stringify(calcFees(schedule, JSON.parse(input))));
"""

ADU = {"permitType": "adu", "valuation": 180000, "aduSqft": 600, "isCombinationPermit": True, "structureUse": "residential", "stories": 1}
ADDITION = {"permitType": "addition", "valuation": 260000, "newFloorAreaSqft": 650, "structureUse": "residential", "stories": 2}
REMODEL = {"permitType": "remodel", "valuation": 250000, "structureUse": "residential", "stories": 1}


def direct(inputs: dict) -> dict:
    process = subprocess.run(
        [NODE, "--input-type=module", "-e", DIRECT, str(CALC), str(SCHEDULE), json.dumps(inputs)],
        capture_output=True, text=True, check=True,
    )
    return json.loads(process.stdout)


def cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([NODE, str(SCRIPT), *args], capture_output=True, text=True, check=False, cwd=ROOT)


def estimate(inputs: dict) -> tuple[dict, str]:
    with tempfile.TemporaryDirectory() as directory:
        out = Path(directory) / "estimate.json"
        process = cli("--input", json.dumps(inputs), "--json", str(out))
        if process.returncode != 0:
            raise AssertionError(process.stderr)
        return json.loads(out.read_text(encoding="utf-8")), process.stdout


def money(value: float) -> str:
    return f"${value:,.2f}"


def amounts(lines: list[dict]) -> dict:
    return {line["id"]: line["amount"] for line in lines}


@unittest.skipUnless(NODE, "node is required for the fee estimate command")
class MatchesSharedCalculator(unittest.TestCase):
    def test_breakdown_is_calc_fees_output(self):
        for inputs in [ADU, ADDITION, REMODEL, {"permitType": "reroof"}, {"permitType": "grading", "scopeQuantities": {"grading_cubic_yards": 350}}]:
            with self.subTest(permit=inputs["permitType"]):
                result, _ = estimate(inputs)
                self.assertEqual(result["breakdown"], direct(inputs))

    def test_printed_lines_and_subtotals_match(self):
        result, stdout = estimate(REMODEL)
        expected = direct(REMODEL)
        for line in expected["firmLines"]:
            self.assertIn(money(line["amount"]), stdout, line["id"])
        self.assertIn(f"**{money(expected['buildingSubtotal'])}**", stdout)
        for item in expected["confirmAtIntake"]:
            self.assertIn(item["label"], stdout)

    def test_school_fee_is_listed_with_other_agencies(self):
        result, stdout = estimate(ADDITION)
        expected = direct(ADDITION)
        school = [line for line in expected["otherAgencyLines"] if line["id"] == "school"]
        self.assertEqual(len(school), 1)
        self.assertNotIn("school", amounts(expected["buildingFirmLines"]))
        other_section = stdout.split("### Other City divisions and other agencies", 1)[1].split("###", 1)[0]
        self.assertIn(money(school[0]["amount"]), other_section)
        self.assertIn(school[0]["ownerDivision"], other_section)

    def test_flat_line_carries_its_surcharge(self):
        result, _ = estimate({"permitType": "reroof"})
        lines = amounts(result["breakdown"]["firmLines"])
        self.assertIn("reroof_permit", lines)
        self.assertIn("technology", lines)
        self.assertEqual(lines, amounts(direct({"permitType": "reroof"})["firmLines"]))

    def test_stepped_grading_line(self):
        inputs = {"permitType": "grading", "scopeQuantities": {"grading_cubic_yards": 350}}
        result, _ = estimate(inputs)
        grading = amounts(result["breakdown"]["firmLines"])["grading_permit"]
        self.assertGreater(grading, 0)
        self.assertEqual(grading, amounts(direct(inputs)["firmLines"])["grading_permit"])


@unittest.skipUnless(NODE, "node is required for the fee estimate command")
class Labelling(unittest.TestCase):
    def test_notice_is_printed_before_and_after(self):
        _, stdout = estimate({"permitType": "reroof"})
        self.assertEqual(stdout.count("ESTIMATE ONLY"), 2)
        self.assertTrue(stdout.startswith("**ESTIMATE ONLY"))
        self.assertTrue(stdout.rstrip().endswith("invoices the permit.**"))

    def test_refuses_a_schedule_without_the_notice(self):
        schedule = json.loads(SCHEDULE.read_text(encoding="utf-8"))
        schedule.pop("estimate_notice")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "schedule.json"
            path.write_text(json.dumps(schedule), encoding="utf-8")
            process = cli("--schedule", str(path), "--list")
        self.assertEqual(process.returncode, 2)
        self.assertIn("ESTIMATE", process.stderr)

    def test_calculator_copy_is_marked_generated(self):
        self.assertTrue(CALC.read_text(encoding="utf-8").startswith("// GENERATED FILE."))


@unittest.skipUnless(NODE, "node is required for the fee estimate command")
class NotEstimated(unittest.TestCase):
    def test_unit_rows_need_quantities(self):
        result, _ = estimate({"permitType": "electrical"})
        self.assertIn("building_permit", [item["id"] for item in result["breakdown"]["confirmAtIntake"]])
        self.assertEqual(result["breakdown"]["buildingSubtotal"], direct({"permitType": "electrical"})["buildingSubtotal"])

    def test_planning_gap_is_not_priced(self):
        result, stdout = estimate({"permitType": "remodel", "planningFeeIds": ["zone_clearance"]})
        self.assertEqual(result["planning"]["listed"], [])
        self.assertEqual(result["planning"]["notInSchedule"][0]["id"], "zone_clearance")
        self.assertIn("Zone Clearance", stdout.split("### Not estimated", 1)[1])

    def test_published_planning_row_is_listed_not_totalled(self):
        schedule = json.loads(SCHEDULE.read_text(encoding="utf-8"))
        row = next(fee for fee in schedule["planning"]["flat"] if fee["id"] == "design_review_admin")
        result, stdout = estimate({"permitType": "remodel", "valuation": 50000, "planningFeeIds": ["design_review_admin"]})
        self.assertEqual(result["planning"]["listed"][0]["amount"], row["amount"])
        self.assertEqual(result["breakdown"], direct({"permitType": "remodel", "valuation": 50000}))
        self.assertIn("not in any subtotal", stdout)


@unittest.skipUnless(NODE, "node is required for the fee estimate command")
class RejectsTypos(unittest.TestCase):
    def check(self, inputs: dict, message: str):
        process = cli("--input", json.dumps(inputs))
        self.assertEqual(process.returncode, 2, process.stdout)
        self.assertIn(message, process.stderr)

    def test_unknown_quantity_id(self):
        self.check({"permitType": "electrical", "scopeQuantities": {"not_a_fee": 2}}, "unknown fee quantity id")

    def test_unknown_field(self):
        self.check({"permitType": "adu", "valuationUsd": 1}, "unknown input field")

    def test_unknown_planning_id(self):
        self.check({"permitType": "adu", "planningFeeIds": ["not_a_fee"]}, "unknown Planning fee id")

    def test_permit_type_required(self):
        self.check({"valuation": 100000}, "permitType is required")

    def test_list_names_the_ids(self):
        process = cli("--list")
        self.assertEqual(process.returncode, 0)
        for text in ["Permit types", "grading_cubic_yards", "utility:laguna_main_sewer", "zone_clearance"]:
            self.assertIn(text, process.stdout)


if __name__ == "__main__":
    unittest.main()
