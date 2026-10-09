#!/usr/bin/env python3
"""Fail closed when an official form differs from its pinned source receipt."""

from __future__ import annotations

import argparse
import shutil
import urllib.error
import urllib.request
from pathlib import Path

from _lib import field_tree_sha256, load_json, require_pypdf, sha256_file, utc_now, widget_inventory, write_json


BROWSER_STEPS = (
    "The City web host (Akamai) commonly returns HTTP 403 to scripts. Open the official source page "
    "in the applicant's visible browser with whatever browser or computer-use tool this host provides, "
    "download the named form, save it to permit-work/input/official-forms/, and rerun this check. "
    "If no visible browser is available, stop this form and give the user the exact URL."
)


def locate(directory: Path, form: dict) -> Path | None:
    for name in (form["cache_name"], form["download_name"]):
        candidate = directory / name
        if candidate.is_file():
            return candidate
    return None


def fetch(form: dict, directory: Path) -> Path:
    destination = directory / form["cache_name"]
    directory.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(form["url"], headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response, destination.open("wb") as output:
            shutil.copyfileobj(response, output)
    except (urllib.error.HTTPError, urllib.error.URLError) as exc:
        destination.unlink(missing_ok=True)
        raise RuntimeError(
            f"official download failed ({exc}) for {form['url']}. {BROWSER_STEPS} "
            f"Expected file: {form['official_name']} ({form['download_name']})."
        ) from exc
    return destination


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--forms-dir", required=True)
    parser.add_argument(
        "--form-id",
        "--only",
        dest="form_id",
        action="append",
        help="Verify one form id; repeat for more. --only is the concise alias.",
    )
    parser.add_argument("--fetch", action="store_true")
    parser.add_argument(
        "--receipt",
        help="Write a JSON receipt of every check (hashes, counts, status) to this path.",
    )
    args = parser.parse_args()

    pypdf = require_pypdf()
    manifest = load_json(args.manifest)
    forms_dir = Path(args.forms_dir)
    selected = set(args.form_id or [])
    failures: list[str] = []
    checked = 0
    receipts: list[dict] = []

    for pending in manifest.get("pending_sources") or []:
        if pending["id"] in selected:
            failures.append(
                f"{pending['id']}: needs_source; no pinned revision or field map yet. "
                f"Last known City link: {pending['url']} (last attempt HTTP "
                f"{pending['last_fetch_attempt']['http_status']}). {pending['next_step']}"
            )
            receipts.append({"id": pending["id"], "status": "needs_source", "url": pending["url"]})

    for form in manifest["forms"]:
        if selected and form["id"] not in selected:
            continue
        if form.get("status", "pinned") != "pinned":
            current = form.get("current_source") or {}
            failures.append(
                f"{form['id']}: {form['status']}; the pinned revision is not current. "
                f"Current City link: {current.get('url', 'unknown')}. {current.get('action', '')}".strip()
            )
            receipts.append({"id": form["id"], "status": form["status"], "url": current.get("url")})
            continue
        try:
            path = locate(forms_dir, form)
            if path is None and args.fetch:
                path = fetch(form, forms_dir)
            if path is None:
                raise FileNotFoundError(
                    f"missing {form['cache_name']} or {form['download_name']} in {forms_dir}"
                )
            reader = pypdf.PdfReader(str(path))
            actual = {
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
                "pages": len(reader.pages),
                "canonical_fields": len(reader.get_fields() or {}),
                "widgets": len(widget_inventory(reader)),
                "field_tree_sha256": field_tree_sha256(reader),
            }
            differences = [
                f"{key}: expected {form[key]!r}, got {value!r}"
                for key, value in actual.items()
                if value != form[key]
            ]
            receipts.append(
                {
                    "id": form["id"],
                    "file": str(path.resolve()),
                    "url": form["url"],
                    **actual,
                    "status": "current" if not differences else "drift",
                    "differences": differences,
                }
            )
            if differences:
                raise ValueError(
                    "; ".join(differences)
                    + ". Stop this form: the City file is not the pinned revision."
                )
            checked += 1
            print(f"OK {form['id']}: {actual['sha256']}")
        except FileNotFoundError as exc:
            failures.append(f"{form['id']}: {exc}. Official URL: {form['url']}. {BROWSER_STEPS}")
        except Exception as exc:
            failures.append(f"{form['id']}: {exc}")

    known = {item["id"] for item in manifest["forms"]}
    known |= {item["id"] for item in manifest.get("pending_sources") or []}
    if selected - known:
        failures.append(f"unknown form ids: {sorted(selected - known)}")
    if args.receipt:
        write_json(
            args.receipt,
            {"schema_version": "1.0.0", "checked_at": utc_now(), "forms": receipts, "failures": failures},
        )
    if failures:
        for failure in failures:
            print(f"ERROR {failure}")
        return 1
    print(f"Verified {checked} current official forms")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
