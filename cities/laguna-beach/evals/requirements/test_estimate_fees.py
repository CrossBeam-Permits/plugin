"""Fee estimator arithmetic and labelling. Expected values are hand-computed from
the published FY 2026/27 rows in requirements/fees/fee-data.json."""

from __future__ import annotations

import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "estimate-fees.py"

spec = importlib.util.spec_from_file_location("estimate_fees", SCRIPT)
estimate_fees = importlib.util.module_from_spec(spec)
spec.loader.exec_module(estimate_fees)
DATA = estimate_fees.load(estimate_fees.DEFAULT_DATA)
TABLE = DATA["building_valuation_fee"]


def run_json(*args: str) -> dict:
    with tempfile.TemporaryDirectory() as directory:
        out = Path(directory) / "estimate.json"
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            estimate_fees.main([*args, "--json", str(out)])
        result = json.loads(out.read_text(encoding="utf-8"))
        result["_stdout"] = buffer.getvalue()
        return result


class BuildingPermitFee(unittest.TestCase):
    def fee(self, valuation: int) -> Decimal:
        amount, _ = estimate_fees.building_permit_fee(Decimal(valuation), TABLE)
        return amount

    def test_row_one_is_flat(self):
        self.assertEqual(self.fee(1500), Decimal("179.67"))
        self.assertEqual(self.fee(2000), Decimal("179.67"))

    def test_row_base_at_floor(self):
        # $2,001 is $1 above the $2,000 floor: 478.40 + 10.39 * 0.001
        self.assertEqual(self.fee(2001), Decimal("478.41"))

    def test_prorated_within_row(self):
        # 478.40 + 10.39 * 23 = 717.37
        self.assertEqual(self.fee(25000), Decimal("717.37"))
        # 2,988.32 + 10.39 * 150 = 4,546.82
        self.assertEqual(self.fee(250000), Decimal("4546.82"))
        # Partial $1,000 is prorated, not rounded up: 2,988.32 + 10.39 * 150.5 = 4,552.015 -> half-even 4,552.02
        self.assertEqual(self.fee(250500), Decimal("4552.02"))

    def test_top_row_has_no_ceiling(self):
        # 39,441.24 + 10.39 * 1,000 = 49,831.24
        self.assertEqual(self.fee(6000000), Decimal("49831.24"))

    def test_zero_valuation_rejected(self):
        with self.assertRaises(SystemExit):
            estimate_fees.building_permit_fee(Decimal(0), TABLE)


class Estimate(unittest.TestCase):
    def test_valuation_estimate_lines_and_total(self):
        result = run_json("--valuation", "250000")
        amounts = {line["label"].split(" (")[0]: Decimal(line["amount"]) for line in result["lines"]}
        self.assertEqual(amounts["Building permit fee"], Decimal("4546.82"))
        self.assertEqual(amounts["Plan review"], Decimal("2955.43"))
        self.assertEqual(amounts["Technology Surcharge"], Decimal("131.29"))
        self.assertEqual(amounts["General Plan Maintenance"], Decimal("262.58"))
        self.assertEqual(amounts["Permit issuance"], Decimal("80.90"))
        self.assertEqual(Decimal(result["total_estimate"]), Decimal("7977.02"))

    def test_notice_is_always_printed(self):
        result = run_json("--line", "reroof_permit")
        self.assertIn("ESTIMATE", result["estimate_notice"])
        self.assertEqual(result["_stdout"].count("ESTIMATE ONLY"), 2)

    def test_flat_line_carries_its_surcharge(self):
        result = run_json("--line", "reroof_permit")
        labels = [line["label"] for line in result["lines"]]
        self.assertIn("Re-roof permit", labels)
        self.assertIn("Technology Surcharge on Re-roof permit", labels)

    def test_stepped_grading_line(self):
        result = run_json("--line", "grading_permit=350")
        grading = next(line for line in result["lines"] if line["label"].startswith("Grading permit"))
        self.assertEqual(Decimal(grading["amount"]), Decimal("1269.84"))

    def test_unit_line_needs_quantity(self):
        result = run_json("--line", "electrical_outlets")
        self.assertEqual(result["not_estimated"][0]["id"], "electrical_outlets")

    def test_planning_gap_is_not_priced(self):
        result = run_json("--planning", "zone_clearance")
        self.assertEqual(result["lines"], [])
        self.assertEqual(result["not_estimated"][0]["id"], "zone_clearance")

    def test_unknown_line_fails(self):
        process = subprocess.run(
            [sys.executable, str(SCRIPT), "--line", "not_a_fee"],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(process.returncode, 0)
        self.assertIn("unknown fee line", process.stderr)


if __name__ == "__main__":
    unittest.main()
