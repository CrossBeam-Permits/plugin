"""Build a whole sheet set from project.json and one script per sheet.

Each sheet script defines build(kit) and returns kit.sheet(...). The build
always regenerates every sheet from project.json. Never patch an output PDF.

Outputs in the build directory:
  <set_name>.pdf        the bound set, page labels = sheet ids
  <set_name>-with-attachments.pdf
                        the set with attached PDFs merged, when pypdf is present
  sheets/<id>.pdf       one PDF per sheet
  build.json            the sidecar: views, scales, every emitted text with its
                        bounding box, claims, clouds. QA reads this file.

Before it writes, a build removes the outputs that the previous build listed in
its build.json (PDFs, SVG previews, qa.json) and every file in png/ (the
preview folder), so a removed sheet, an old merged set or an old preview cannot
stay behind. Other files in the folder are left alone.
"""
from __future__ import annotations

import contextlib
import glob
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile

from . import __version__
from .bind import write_set
from .display import LayoutError
from .drafting import view_linework
from .model import ExprError, PrintRefused, Project, ProjectError, Value, inside_dir
from .notes import Txt, fill
from .sheet import Sheet
from .units import ScaleError

SIDECAR = "build.json"
PREVIEW_DIR = "png"      # PNG previews; the kit owns this folder and clears it on every build
# Fields of each text record that go into the sidecar, in sidecar order.
_TEXT_FIELDS = ("s", "bbox", "size", "bold", "rot", "role", "region", "keys", "fv", "cd", "collide",
                "view", "meta", "seq")


class Kit:
    """What a sheet script receives. Gives access to the project and makes sheets."""

    def __init__(self, project: Project):
        self.project = project
        self.sheets: dict[str, Sheet] = {}

    def sheet(self, sid: str, **kw) -> Sheet:
        """Start sheet `sid`. Its title comes from project.json unless given."""
        sh = Sheet(self, sid, **kw)
        self.sheets[sid] = sh
        return sh

    def value(self, key: str) -> Value:
        return self.project.value(key)

    def v(self, key: str) -> float:
        return self.project.v(key)

    def text(self, template: str, depends_on=(), cd=()) -> Txt:
        """Fill a note template from project values ({key} or {key:in}).

        cd: the code-decision id (or ids) the note prints from, such as
        "CD-014". It is recorded for QA and never prints.
        """
        return fill(self.project, template, False, depends_on, cd)

    def claim(self, template: str, depends_on=(), cd=()) -> Txt:
        """A note that claims compliance. Refused when it rests on an unverified value."""
        return fill(self.project, template, True, depends_on, cd)


@contextlib.contextmanager
def _sheet_imports(folder: str):
    """Let sheet scripts import their neighbours (for example `import common`).

    The sheets folder goes first on sys.path for the whole build. Any module
    named like a .py file in that folder is evicted from sys.modules before and
    after, so a second build (or another project's common.py) never reuses a
    stale copy. Modules evicted that existed before the build are restored.
    """
    names = {os.path.splitext(os.path.basename(f))[0] for f in glob.glob(os.path.join(folder, "*.py"))}
    names |= {os.path.basename(os.path.dirname(f)) for f in glob.glob(os.path.join(folder, "*", "__init__.py"))}

    def evict():
        gone = {}
        for mod in list(sys.modules):
            if mod.split(".")[0] in names:
                gone[mod] = sys.modules.pop(mod)
        return gone
    saved = evict()
    sys.path.insert(0, folder)
    try:
        yield
    finally:
        try:
            sys.path.remove(folder)
        except ValueError:
            pass
        evict()
        sys.modules.update(saved)


def _load_script(path: str):
    name = "permitkit_sheet_" + hashlib.sha1(path.encode()).hexdigest()[:10]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "build"):
        raise AttributeError(f"{path} has no build(kit) function")
    return mod


def _r(x, nd=3):
    if isinstance(x, float):
        r = round(x, nd)
        return 0.0 if r == 0 else r
    if isinstance(x, (list, tuple)):
        return [_r(v, nd) for v in x]
    if isinstance(x, dict):
        return {k: _r(v, nd) for k, v in x.items()}
    return x


def _sheet_record(sh: Sheet, index: int) -> dict:
    pg = sh.page
    regions = {"frame": list(sh.border), "tb": list(sh.tb_box), "notes": list(sh.notes_box)}
    for rid, box in sh.cells:
        regions[rid] = list(box)
    texts = [{k: t[k] for k in _TEXT_FIELDS} for t in pg.texts]
    views = []
    linework = view_linework(pg, [v.id for v in sh.views])
    for v in sh.views:
        views.append({"id": v.id, "number": v.number, "title": v.title,
                      "scale": v.scale.printed,
                      "true_scale": v.scale.is_true, "pt_per_in": v.s,
                      "extents_in": [v.x0, v.y0, v.x1, v.y1], "bbox_pt": list(v.bbox_pt),
                      "cell_pt": list(v.cell), "fits_larger": v.fits_larger,
                      "linework": linework[v.id]})
    return _r({
        "id": sh.id, "title": sh.title, "page_index": index, "size": sh.size_name,
        "size_in": [sh.w_in, sh.h_in], "mediabox_pt": [pg.width, pg.height],
        "scale_text": sh.scale_text, "title_block": sh.tb, "stamp_box": list(sh.stamp_box),
        "regions": regions, "views": views, "texts": texts, "claims": pg.claims,
        "clouds": pg.clouds, "scale_bars": pg.scale_bars, "labeller_collisions": pg.collisions,
        "layout_issues": sh.layout_issues, "text_over_geometry": sh.text_over_geometry,
        "images": pg.images, "legend_kinds": sorted(set(pg.legend_kinds)),
    })


def _sha(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def inputs_sha256(project) -> dict:
    """SHA-256 of every input besides project.json: each .py file in the sheet
    script folders (a sheet can import common.py) and each attached PDF. QA
    compares them with the build, so a script edited after a build, or a build
    that failed and left the old outputs, reads as stale."""
    out = {}
    folders = {os.path.dirname(project.resolve_path(e["script"])) for e in project.sheets if e.get("script")}
    for folder in sorted(folders):
        for name in sorted(os.listdir(folder)):
            path = os.path.join(folder, name)
            if name.endswith(".py") and os.path.isfile(path):
                out[os.path.relpath(path, project.dir).replace(os.sep, "/")] = _sha(path)
    for e in project.sheets:
        if e.get("attach"):
            path = project.resolve_path(e["attach"])
            if os.path.isfile(path):
                out[e["attach"]] = _sha(path)
    return out


def build_set(project_path: str, out_dir: str, check_determinism: bool = False,
              svg: bool = False) -> dict:
    """Build every sheet listed in project.json into out_dir. Returns the sidecar dict.

    Raises ProjectError when project.json has errors, ScaleError when a view does
    not fit at its scale, PrintRefused when a value or claim may not be printed.
    """
    project = Project.load(project_path)
    if project.errors:
        raise ProjectError([f"{i['where']}: {i['code']}: {i['msg']}" for i in project.errors])
    if not project.sheets:
        raise ProjectError(["sheets: no-sheets: list at least one sheet in project.json before building"])
    kit = Kit(project)
    pages, records, attachments, order = [], [], [], []
    scripts_dir = project.dir
    folders = {os.path.dirname(project.resolve_path(e["script"])) for e in project.sheets if e.get("script")}
    with contextlib.ExitStack() as stack:
        for folder in sorted(folders):
            stack.enter_context(_sheet_imports(folder))
        for entry in project.sheets:
            order.append(entry["id"])
            if entry.get("attach"):
                attachments.append({"id": entry["id"], "path": entry["attach"], "position": len(order) - 1})
                continue
            script = project.resolve_path(entry["script"])
            if not os.path.isfile(script):
                raise ProjectError([f"sheet {entry['id']}: script {entry['script']} does not exist. Write it with "
                                    f"`python3 -m permitkit new-sheet {entry['id']}`, or fix its path in sheets"])
            mod = _load_script(script)
            sh = mod.build(kit)
            if not isinstance(sh, Sheet) or sh.id != entry["id"]:
                raise ValueError(f"{entry['script']}: build(kit) must return kit.sheet({entry['id']!r})")
            pages.append(sh.finish())
            records.append(_sheet_record(sh, len(pages) - 1))
    os.makedirs(out_dir, exist_ok=True)
    _remove_previous_outputs(out_dir)
    files = write_set(pages, out_dir, project.set_name, project.meta.get("title", ""),
                      attachments=attachments, base_dir=scripts_dir)
    if svg:
        from .svg import write_svg
        os.makedirs(os.path.join(out_dir, "svg"), exist_ok=True)
        for pg in pages:
            write_svg(pg, os.path.join(out_dir, "svg", f"{pg.sheet_id}.svg"))
    merged = sorted({a["merged_into"] for a in files["attachments"] if a["merged_into"]})
    sidecar = {
        "kit": "permitkit", "kit_version": __version__,
        "project_sha256": project.sha256,
        "inputs_sha256": inputs_sha256(project),
        "bound_order": order,
        "set_pdf": files["set_pdf"],
        "sheet_pdfs": files["sheet_pdfs"],
        "attachments": files["attachments"],
        "model_issues": project.issues,
        "chains": _r(project.chain_report()),
        "sheets": records,
        "file_sha256": {name: _sha(os.path.join(out_dir, name))
                        for name in [files["set_pdf"]] + merged + list(files["sheet_pdfs"].values())},
        "svg": sorted(f"svg/{pg.sheet_id}.svg" for pg in pages) if svg else [],
        "paths": {"project": os.path.relpath(os.path.abspath(project_path), os.path.abspath(out_dir))},
    }
    core = _core_hash(sidecar)
    sidecar["sidecar_core_sha256"] = core
    if check_determinism:
        sidecar["determinism"] = determinism(project_path, reference=sidecar)
    with open(os.path.join(out_dir, SIDECAR), "w", encoding="utf-8") as fh:
        json.dump(sidecar, fh, indent=1, sort_keys=False, ensure_ascii=False)
        fh.write("\n")
    return sidecar


def outputs_listed(sidecar: dict) -> set:
    """Every output file a sidecar names, relative to its build folder."""
    names = {sidecar.get("set_pdf"), SIDECAR, "qa.json"}
    names |= set(sidecar.get("file_sha256", {}))
    names |= set(sidecar.get("sheet_pdfs", {}).values())
    names |= {a.get("merged_into") for a in sidecar.get("attachments", [])}
    names |= set(sidecar.get("svg", []))
    for sid in sidecar.get("sheet_pdfs", {}):
        names |= {f"png/{sid}.png", f"svg/{sid}.svg"}
    return {n for n in names if n}


def _remove_previous_outputs(out_dir: str) -> None:
    """Delete what the previous build in out_dir wrote, as its build.json lists it.

    Only files a permitkit sidecar names are removed, so pointing --out at a
    folder that holds other files never deletes them.
    """
    side = os.path.join(out_dir, SIDECAR)
    try:
        with open(side, encoding="utf-8") as fh:
            prev = json.load(fh)
    except (OSError, ValueError):
        return
    if not isinstance(prev, dict) or prev.get("kit") != "permitkit":
        return
    root = os.path.realpath(out_dir)
    previews = glob.glob(os.path.join(root, PREVIEW_DIR, "*.png"))
    for rel in sorted(outputs_listed(prev)) + sorted(os.path.relpath(f, root) for f in previews):
        full = os.path.realpath(os.path.join(root, rel))
        if inside_dir(full, root) and os.path.isfile(full):
            os.remove(full)


def _core_hash(sidecar: dict) -> str:
    core = {k: v for k, v in sidecar.items()
            if k not in ("paths", "determinism", "sidecar_core_sha256", "svg")}
    return hashlib.sha256(json.dumps(core, sort_keys=True).encode()).hexdigest()


#: Hash seeds for the two determinism rebuilds. Different seeds change the
#: iteration order of sets and dicts keyed by strings, so a sheet script that
#: depends on that order builds different files.
DETERMINISM_SEEDS = ("1", "2")


def determinism(project_path: str, reference: dict | None = None) -> dict:
    """Build the set twice more, each in a fresh Python process with its own
    PYTHONHASHSEED and its own temporary folder, and compare every output hash.

    Pass the sidecar of a third build as `reference` to compare it too.
    """
    kit_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    runs, errors = [], []
    for seed in DETERMINISM_SEEDS:
        tmp = tempfile.mkdtemp(prefix="permitkit-det-")
        try:
            env = dict(os.environ, PYTHONHASHSEED=seed,
                       PYTHONPATH=os.pathsep.join(filter(None, [kit_root, os.environ.get("PYTHONPATH")])))
            proc = subprocess.run(
                [sys.executable, "-m", "permitkit", "build", os.path.abspath(project_path),
                 "--out", tmp, "--no-determinism"],
                env=env, capture_output=True, text=True, cwd=tmp)
            if proc.returncode != 0:
                errors.append(f"seed {seed}: rebuild failed: {(proc.stdout + proc.stderr)[-400:]}")
                continue
            with open(os.path.join(tmp, SIDECAR), encoding="utf-8") as fh:
                sc = json.load(fh)
            runs.append({"files": sc["file_sha256"], "core": sc["sidecar_core_sha256"]})
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    if reference is not None:
        runs.append({"files": reference["file_sha256"], "core": reference["sidecar_core_sha256"]})
    if not runs:
        return {"ok": False, "builds_compared": 0, "differing_files": [], "sidecar_core_equal": False,
                "seeds": list(DETERMINISM_SEEDS), "errors": errors}
    ok = not errors and all(r == runs[0] for r in runs[1:])
    diffs = sorted({name for r in runs[1:] for name, h in r["files"].items()
                    if runs[0]["files"].get(name) != h})
    return {"ok": ok, "builds_compared": len(runs), "differing_files": diffs,
            "sidecar_core_equal": all(r["core"] == runs[0]["core"] for r in runs),
            "seeds": list(DETERMINISM_SEEDS), "errors": errors}


def main_build(project_path: str, out_dir: str | None = None, check_determinism: bool = True,
               svg: bool = False) -> int:
    out = out_dir or os.path.join(os.path.dirname(os.path.abspath(project_path)), "build")
    try:
        sc = build_set(project_path, out, check_determinism=check_determinism, svg=svg)
    except ProjectError as exc:
        print(json.dumps({"ok": False, "errors": exc.errors}, indent=1))
        return 1
    except (ScaleError, LayoutError, PrintRefused, ExprError) as exc:
        print(json.dumps({"ok": False, "error": type(exc).__name__, "msg": str(exc)}, indent=1))
        return 1
    det = sc.get("determinism", {})
    print(json.dumps({"ok": True, "out_dir": out, "set_pdf": sc["set_pdf"],
                      "sheets": list(sc["sheet_pdfs"]), "attachments": sc["attachments"],
                      "determinism": det}, indent=1))
    sys.stdout.flush()
    return 0
