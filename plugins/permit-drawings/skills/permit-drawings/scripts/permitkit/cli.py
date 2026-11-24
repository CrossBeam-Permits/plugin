"""Command line.

  python3 -m permitkit validate project.json
  python3 -m permitkit build project.json [--out DIR] [--no-determinism] [--svg]
  python3 -m permitkit qa BUILD_DIR [--project project.json] [--out qa.json]
  python3 -m permitkit preview BUILD_DIR [--dpi 50] [--out DIR] [--sheet ID] [--prefix P]
  python3 -m permitkit new-sheet A-3.1 [--title TITLE] [--dir sheets]
  python3 -m permitkit rules project.json        check drawn values against `rules`, no build
  python3 -m permitkit measure project.json [--build build] [--out FILE]   the "measure these" list
  python3 -m permitkit energy --zip 92651         climate zone for a ZIP, as a Value to paste
  python3 -m permitkit energy project.json [--write-rules]   Title 24 checks from the energy block
  python3 -m permitkit green project.json         CALGreen measure decisions from the green block
  python3 -m permitkit struct project.json [--calc-md FILE]   structural checks and preliminary calcs
  python3 -m permitkit api [module ...]       every drawing call, with its signature
  python3 -m permitkit modules                which optional modules are installed (optional.py)

Run with PYTHONPATH set to the skill's scripts folder.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

from . import optional

TEMPLATE = '''"""{sid} - {title}.

One script per sheet. Read every number from project.json through the kit.
Do not type a shared number here. Rebuild the whole set after any change:
    python3 -m permitkit build project.json && python3 -m permitkit qa build
"""
from permitkit import annot, arch  # also: fixtures, symbols, hatch, site, section. `python3 -m permitkit api` lists every call.


def build(kit):
    p = kit.project
    sh = kit.sheet("{sid}")

    # 1. Place each drawing at a true scale. extents = (x0, y0, x1, y1) real
    #    inches, including room for dimensions and labels. cell = (x, y, w, h)
    #    paper inches from the drawing-area lower-left. A view that does not fit
    #    raises ScaleError; change the scale or the cell, never shrink. cell=None
    #    uses the whole drawing area. Pass "fit" as the scale to take the largest
    #    standard scale that fits the cell.
    v = sh.view("DRAWING TITLE", '1/2" = 1\\'-0"', extents=(-24, -24, 240, 180), cell=None)

    # 2. Geometry first, in real inches (x east, y north on plans).
    # shell = arch.Shell(v, 0, 0, p.v("room_w"), p.v("room_d"),
    #                    t={{"N": p["t_ext"], "S": p["t_int"], "E": p["t_int"], "W": p["t_int"]}})
    # shell.N.window(p.v("w1_offset"), p["w1_width"])

    # 3. Dimensions and labels last. Dimension text comes from Values only.
    # annot.dim_chain(v, [p["seg_a"], p["seg_b"]], start=0, at=p.v("room_d") + 30,
    #                 axis="x", ext_from=p.v("room_d"))

    # 4. Notes. kit.text() prints values with their FV tags; kit.claim() refuses
    #    a compliance note that rests on an ASSUMED value.
    sh.notes([
        kit.text("EXAMPLE NOTE."),
    ])
    return sh
'''


def _issues(project):
    return {"ok": not project.errors, "errors": project.errors,
            "warnings": [i for i in project.issues if i["severity"] == "warning"],
            "chains": project.chain_report()}


def cmd_validate(a) -> int:
    from .model import Project, ProjectError
    try:
        p = Project.load(a.project)
    except ProjectError as exc:
        print(json.dumps({"ok": False, "errors": exc.errors}, indent=1))
        return 1
    print(json.dumps(_issues(p), indent=1))
    return 0 if not p.errors else 1


def cmd_build(a) -> int:
    from .build import main_build
    return main_build(a.project, a.out, check_determinism=not a.no_determinism, svg=a.svg)


def cmd_qa(a) -> int:
    from . import qa
    rep = qa.run(a.build_dir, a.project)
    text = json.dumps(rep, indent=1, ensure_ascii=False)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
        short = {"pass": rep["pass"], "summary": rep["summary"], "counts": rep["counts"],
                 "failed": {k: rep["checks"][k]["detail"] for k in rep["failed_checks"]}}
        if "rules" in short["failed"]:          # the rules list below carries the warnings
            short["failed"]["rules"] = [r["message"] for r in rep["checks"]["rules"]["rules"]
                                        if r["status"] == "fail"]
        if rep["checks"]["rules"]["status"] != "n/a":
            short["rules"] = [f"{r['status'].upper()}  {r['message']}" for r in rep["checks"]["rules"]["rules"]]
        fill = rep["advisory"]["sheet_fill"]
        if fill["low"]:                         # advisory: listed so the short report shows it
            short["sheet_fill_low"] = [f"{r['sheet']}: {r['used']:.0%} of the drawing area in use; an empty band "
                                       f"{r['empty_band_in']:g} in. tall" for r in fill["sheets"]
                                       if r["sheet"] in fill["low"]]
        short["report"] = a.out
        print(json.dumps(short, indent=1, ensure_ascii=False))
    else:
        print(text)
    return 0 if rep["pass"] else 1


def cmd_rules(a) -> int:
    """The QA `rules` report on project.json alone, without a build (a self-check)."""
    from .model import Project, ProjectError
    from .qa import rule_counts, rules_report
    try:
        p = Project.load(a.project)
    except ProjectError as exc:
        print(json.dumps({"ok": False, "errors": exc.errors}, indent=1))
        return 1
    rows = rules_report(p)
    order = {"fail": 0, "warn": 1, "pass": 2}
    counts = rule_counts(rows)
    print(json.dumps({"ok": not p.errors and not counts["fail"], "counts": counts,
                      "errors": p.errors,
                      "lines": [f"{r['status'].upper()}  {r['message']}"
                                for r in sorted(rows, key=lambda r: order[r["status"]])],
                      "rules": rows}, indent=1, ensure_ascii=False))
    return 0 if not p.errors and not counts["fail"] else 1


def cmd_measure(a) -> int:
    """The "measure these" list (measure.py): open field-verify tags, ranked by what rests on them."""
    from .measure import markdown, measure_list
    from .model import Project, ProjectError
    try:
        p = Project.load(a.project)
    except ProjectError as exc:
        print(json.dumps({"ok": False, "errors": exc.errors}, indent=1))
        return 1
    build = a.build or os.path.join(p.dir, "build")
    rep = measure_list(p, build)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(markdown(rep))
    print(json.dumps(dict(rep, open=len(rep["items"]) + len(rep["untagged"]), report=a.out),
                     indent=1, ensure_ascii=False))
    return 0


# ---- struct (struct.py): structural checks and the preliminary calc package
def cmd_struct(a) -> int:
    """The structure block: prescriptive table checks, triggers and preliminary calcs."""
    if not optional.installed("structural"):
        return _missing("structural")
    from .model import Project, ProjectError
    from .struct import calc_markdown, report
    try:
        p = Project.load(a.project)
    except ProjectError as exc:
        print(json.dumps({"ok": False, "errors": exc.errors}, indent=1))
        return 1
    rep = report(p)
    rep["errors"] = p.errors
    if a.calc_md:
        target = os.path.abspath(a.calc_md)
        from .model import inside_dir
        if not inside_dir(os.path.dirname(target) or ".", p.dir):
            return _fail(f"--calc-md {a.calc_md} is outside the project folder")
        with open(target, "w", encoding="utf-8") as fh:
            fh.write(calc_markdown(p))
        rep["calc_md"] = os.path.relpath(target, p.dir)
    if not a.full:
        rep = {k: rep[k] for k in ("ok", "edition", "counts", "lines", "issues", "members", "errors", "banner")
               if k in rep} | ({"calc_md": rep["calc_md"]} if "calc_md" in rep else {})
    print(json.dumps(rep, indent=1, ensure_ascii=False))
    return 0 if rep["ok"] and not p.errors else 1


def _fail(msg: str) -> int:
    print(json.dumps({"ok": False, "msg": msg}))
    return 1


def _missing(name: str) -> int:
    return _fail(optional.message(name))


def cmd_modules(a) -> int:
    """Which optional modules (energy, structural, 3D) this install has, and how to fetch the rest."""
    print(json.dumps(optional.report(), indent=1))
    return 0


def cmd_preview(a) -> int:
    from .model import inside_dir
    with open(os.path.join(a.build_dir, "build.json"), encoding="utf-8") as fh:
        sc = json.load(fh)
    if os.sep in a.prefix or (os.altsep and os.altsep in a.prefix) or ".." in a.prefix:
        return _fail(f"--prefix {a.prefix!r} must be a plain file name prefix, with no path separator or '..'")
    # The project folder is the folder of project.json, which build.json records.
    project_dir = os.path.dirname(os.path.normpath(os.path.join(a.build_dir, sc["paths"]["project"])))
    build_png = os.path.join(a.build_dir, "png")
    out = a.out or build_png
    if a.out and not inside_dir(a.out, project_dir):
        return _fail(f"--out {out!r} is outside the project folder {os.path.realpath(project_dir)!r}; "
                     "preview writes only inside the project folder")
    os.makedirs(out, exist_ok=True)
    engine = a.engine
    if engine == "auto":
        # poppler on macOS loads the regular face of Helvetica.ttc for Helvetica-Bold,
        # so bold text previews as regular. Apple's renderer (sips) does not.
        engine = "sips" if sys.platform == "darwin" and shutil.which("sips") else "pdftoppm"
    tool = shutil.which(engine)
    if not tool:
        return _fail(f"{engine} not found; rebuild with --svg and open the SVGs")
    width_in = {s["id"]: s["size_in"][0] for s in sc["sheets"]}
    wanted = a.sheet or list(sc["sheet_pdfs"])
    unknown = [sid for sid in wanted if sid not in sc["sheet_pdfs"]]
    if unknown:
        return _fail(f"no drawn sheet {', '.join(unknown)} in this build")
    targets = [(sid, os.path.join(out, f"{a.prefix}{sid}.png")) for sid in wanted]
    # The build clears build/png on every build, so a file there may be
    # replaced. Any other folder (such as permit-work/questions/ for pictures
    # sent to the owner) is never cleared, so preview never overwrites a file
    # there. The test is per file, by its real path.
    build_png_real = os.path.realpath(build_png)
    taken = [png for _, png in targets
             if os.path.exists(png) and os.path.dirname(os.path.realpath(png)) != build_png_real]
    if taken:
        return _fail("these files exist and preview never overwrites a file "
                     f"outside build/png: {', '.join(taken)}. Use a new --prefix")
    made = []
    for sid, png in targets:
        src = os.path.join(a.build_dir, sc["sheet_pdfs"][sid])
        if engine == "sips":
            subprocess.run([tool, "-s", "format", "png", src, "--out", png, "-Z",
                            str(int(width_in[sid] * a.dpi))], check=True, capture_output=True)
        else:
            subprocess.run([tool, "-r", str(a.dpi), "-png", "-singlefile", src, png[:-4]], check=True)
        made.append(png)
    print(json.dumps({"ok": True, "engine": engine, "png": made}, indent=1))
    return 0


def cmd_new_sheet(a) -> int:
    os.makedirs(a.dir, exist_ok=True)
    name = a.sid.lower().replace("-", "").replace(".", "_") + ".py"
    path = os.path.join(a.dir, name)
    if os.path.exists(path):
        print(f"{path} exists; not overwritten", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEMPLATE.format(sid=a.sid, title=a.title))
    entry = {"id": a.sid, "title": a.title, "script": os.path.relpath(path, a.project_dir)}
    print(json.dumps({"wrote": path, "add_to_project_sheets": entry}, indent=1))
    return 0


# ---- energy and green (energy.py, greensheets.py; references/energy-and-green.md)

def cmd_energy(a) -> int:
    """Climate zone for a ZIP; or the Title 24 plan of project.json, optionally written into `rules`."""
    if not optional.installed("energy"):
        return _missing("energy")
    from . import energy
    from .model import Project, ProjectError
    if a.zip:
        try:
            print(json.dumps(energy.zone_entry(a.zip), indent=1))
        except energy.EnergyError as exc:
            return _fail(str(exc))
        return 0
    if not a.project:
        return _fail("give project.json or --zip")
    written = None
    if a.write_rules:
        try:
            written = energy.write_rules(a.project)
        except (energy.EnergyError, ProjectError) as exc:
            return _fail(str(exc))
    try:
        p = Project.load(a.project)
    except ProjectError as exc:
        print(json.dumps({"ok": False, "errors": exc.errors}, indent=1))
        return 1
    pl = energy.plan(p)
    if pl is None:
        return _fail("project.json has no energy block")
    out = {"ok": not p.errors, "errors": [e for e in p.errors if e["code"].startswith("energy")],
           **pl.summary(), "rules_in_project": energy.rules_in_sync(p)}
    if written is not None:
        out["rules_written"] = written
    print(json.dumps(out, indent=1, ensure_ascii=False))
    return 0 if out["ok"] and not out["checks"]["fail"] and not out["requirements_failed"] else 1


def cmd_green(a) -> int:
    if not optional.installed("energy"):
        return _missing("energy")
    from . import greensheets
    from .model import Project, ProjectError, PrintRefused
    try:
        p = Project.load(a.project)
        rep = greensheets.report(p)
    except ProjectError as exc:
        print(json.dumps({"ok": False, "errors": exc.errors}, indent=1))
        return 1
    except PrintRefused as exc:
        return _fail(str(exc))
    print(json.dumps({"ok": not rep["undecided"], **rep}, indent=1, ensure_ascii=False))
    return 0 if not rep["undecided"] else 1


#: What `permitkit api` lists, in reading order: (title, object, members or None for every public one).
API_SECTIONS = (
    ("kit (the `kit` passed to build)", "build:Kit", ("sheet", "value", "v", "text", "claim")),
    ("Sheet (kit.sheet)", "sheet:Sheet", ("view", "largest_scale", "panel", "notes", "sheet_index", "side_panel",
                                          "key_plan", "slot", "connection", "place_image", "drawing_area_in")),
    ("Panel (sh.panel)", "sheet:Panel", ("heading", "banner", "para", "numbered", "table", "legend", "grid_table",
                                          "opening_schedule", "fv_schedule", "columns", "fit", "space")),
    ("View (sh.view): geometry in real inches", "display:View",
     ("line", "polyline", "polygon", "rect", "circle", "arc", "path", "hatch", "text", "reserve", "P")),
    ("Project (kit.project)", "model:Project", ("value", "lookup", "v", "pt", "field", "item", "items", "fmt")),
    ("arch: walls, openings, stairs, elevation symbols, electrical", "arch", None),
    ("arch.Wall openings", "arch:Wall", ("door", "window", "slider", "bypass", "bifold", "cased", "infill",
                                         "overhead", "cut", "pt")),
    ("fixtures: plumbing, kitchen, appliances", "fixtures", None),
    ("annot: dimensions, leaders, keynotes, bubbles, clouds", "annot", None),
    ("symbols: opening, room, elevation, grid and level symbols", "symbols", None),
    ("hatch: material patterns for sections, details and site plans", "hatch", None),
    ("site: site-plan symbols", "site", None),
    ("section: elevations and sections", "section", None),
    ("layout: pick scales and cells for several views", "layout", None),
    ("tables: zoning table and rule limits", "tables", None),
    ("pens: named line weights and text sizes", "pens", None),
)

STYLE_NOTE = """Style keywords on every View geometry call: stroke (colour, e.g. "#111111"), width (points),
fill (colour or None), dash (tuple of points, e.g. (4, 2)), status ("ASSUMED" draws grey dashed),
layer. Layers: "back" (textures, never collides), "geom" (building linework, the default; QA fails
text that sits on it), "annot" (dimension lines, leaders, setback lines; text may cross it).
Colours: permitkit.display INK, INK2, GREY, LIGHT, DIM, POCHE_E, POCHE_N, WHITE.
Project fields: kit.project.meta["title" | "address" | "owner" | "date" ...]."""


def _first_para(doc) -> str:
    import inspect
    doc = inspect.cleandoc(doc or "")
    return doc.split("\n\n")[0].replace("\n", " ").strip()


def _indent(text: str, pad: str) -> str:
    return "\n".join(pad + line if line else line for line in text.splitlines())


def _api_names(mod, obj, cls_name, members):
    import inspect
    if members is not None:
        return [n for n in members if hasattr(obj, n)]
    aliases = getattr(obj, "ALIASES", {}) if not cls_name else {}
    return [n for n, m in vars(obj).items() if not n.startswith("_")
            and (inspect.isfunction(m) or inspect.isclass(m))
            and (getattr(m, "__module__", "") == mod.__name__ or n in aliases)]


def _api_entry(mod, obj, mod_name, cls_name, n, full: bool) -> list:
    """One call: its signature, then its first docstring paragraph (full=True: the whole docstring)."""
    import inspect
    m = getattr(obj, n)
    if isinstance(m, property):
        return [f"  {n}  (property) {_first_para(m.__doc__)}"]
    try:
        sig = str(inspect.signature(m)).replace("(self, ", "(").replace("(self)", "()")
        sig = re.sub(r"(: |-> )\"?'([^']*)'\"?", r"\1\2", sig)    # string annotations, unquoted
    except (TypeError, ValueError):
        sig = ""
    out = [f"  {mod_name + '.' if not cls_name else ''}{n}{sig}"]
    doc = _indent(inspect.cleandoc(m.__doc__ or ""), "      ").strip() if full else _first_para(m.__doc__)
    aliases = getattr(obj, "ALIASES", {}) if not cls_name else {}
    if n in aliases and getattr(m, "__module__", "") != mod.__name__:
        doc = f"Alias of {aliases[n]}. {doc}"
    return out + ([f"      {doc}"] if doc else [])


def api_text(module_filter=None) -> str:
    """The kit's API from the code itself, in three depths.

    No filter: an index of every call by name. Module names (arch, fixtures):
    each call's signature and first docstring paragraph. module.call (or
    Panel.fit, Sheet.view): that call's whole docstring, with the module notes.
    """
    import importlib
    import inspect
    version = __import__("permitkit").__version__
    wanted = list(module_filter or [])
    calls = {w.lower() for w in wanted if "." in w}
    mods = {w.lower() for w in wanted if "." not in w}
    known = {t.partition(":")[0] for _, t, _ in API_SECTIONS} | {t.partition(":")[2].lower() for _, t, _ in API_SECTIONS}
    unknown = sorted(m for m in mods | {c.split(".", 1)[0] for c in calls} if m not in known)
    if not wanted:
        out = [f"permitkit {version} API. Positions are real inches on a view; text and symbol sizes are "
               "points.", "", STYLE_NOTE, "",
               "Index of every call. `api arch fixtures` gives signatures and one line each; "
               "`api tables.zoning_table` gives one call's full docs.", ""]
    else:
        out = [f"permitkit {version}. Real inches on a view, points for text. Plain `api` lists every call "
               "and the style keywords.", ""]
    for title, target, members in API_SECTIONS:
        mod_name, _, cls_name = target.partition(":")
        heads = {mod_name, cls_name.lower()} - {""}
        names_here = None
        if wanted:
            hit = [w.split(".", 1)[1] for w in calls if w.split(".", 1)[0] in heads]
            if not (heads & mods) and not hit:
                continue
            names_here = hit
        mod = importlib.import_module(f"permitkit.{mod_name}")
        obj = getattr(mod, cls_name) if cls_name else mod
        names = _api_names(mod, obj, cls_name, members)
        out.append(f"## {title}")
        if not wanted:
            out += ["  " + ", ".join(names), ""]
            continue
        if names_here:
            # One call in full, with the module notes it may point to (row formats, cell names).
            if not cls_name and mod.__doc__:
                out.extend([_indent(inspect.cleandoc(mod.__doc__), "  "), ""])
            lower = {n.lower(): n for n in names}
            for n in names_here:
                if n in lower:
                    out += _api_entry(mod, obj, mod_name, cls_name, lower[n], full=True)
                else:
                    out.append(f"  no call {n!r} here; calls: {', '.join(names)}")
        else:
            if not cls_name and mod.__doc__:
                out.append("  " + _first_para(mod.__doc__))
            for n in names:
                out += _api_entry(mod, obj, mod_name, cls_name, n, full=False)
        out.append("")
    if wanted and unknown:
        out.append(f"No module or class named {', '.join(unknown)}. Names: {', '.join(sorted(known - {''}))}.")
    return "\n".join(out)


def cmd_api(a) -> int:
    print(api_text(a.module or None))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="permitkit", description="Permit drawing kit")
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate", help="check project.json")
    v.add_argument("project")
    v.set_defaults(fn=cmd_validate)
    b = sub.add_parser("build", help="build every sheet into a set")
    b.add_argument("project")
    b.add_argument("--out")
    b.add_argument("--no-determinism", action="store_true", help="skip the two extra rebuilds")
    b.add_argument("--svg", action="store_true", help="also write SVG previews")
    b.set_defaults(fn=cmd_build)
    q = sub.add_parser("qa", help="run the QA gate on a build folder")
    q.add_argument("build_dir")
    q.add_argument("--project")
    q.add_argument("--out")
    q.set_defaults(fn=cmd_qa)
    p = sub.add_parser("preview", help="render PNG previews (sips on macOS, else pdftoppm)")
    p.add_argument("build_dir")
    p.add_argument("--dpi", type=int, default=50)
    p.add_argument("--engine", choices=["auto", "pdftoppm", "sips"], default="auto")
    p.add_argument("--out", help="folder for the PNGs, inside the project folder (default BUILD_DIR/png, "
                                 "which every build clears). Use permit-work/questions for pictures you "
                                 "send to the owner")
    p.add_argument("--sheet", action="append", help="render only this sheet id; repeat for more")
    p.add_argument("--prefix", default="", help="file name prefix, for example Q-012- gives Q-012-A-1.png; "
                                                "no path separator or '..'")
    p.set_defaults(fn=cmd_preview)
    r = sub.add_parser("rules", help="check drawn values in project.json against its rules, without a build")
    r.add_argument("project")
    r.set_defaults(fn=cmd_rules)
    m = sub.add_parser("measure", help="the 'measure these' list: open field-verify tags, ranked")
    m.add_argument("project")
    m.add_argument("--build", help="build folder to read where each tag prints (default ./build beside project.json)")
    m.add_argument("--out", help="also write the list as markdown for the owner")
    m.set_defaults(fn=cmd_measure)
    st = sub.add_parser("struct", help="structural checks (CRC tables) and preliminary calcs, without a build")
    st.add_argument("project")
    st.add_argument("--calc-md", help="write the preliminary calc package (markdown) to this file")
    st.add_argument("--full", action="store_true", help="print every row and calc in full")
    st.set_defaults(fn=cmd_struct)
    n = sub.add_parser("new-sheet", help="write a sheet script template")
    n.add_argument("sid")
    n.add_argument("--title", default="SHEET TITLE")
    n.add_argument("--dir", default="sheets")
    n.add_argument("--project-dir", default=".")
    n.set_defaults(fn=cmd_new_sheet)
    e = sub.add_parser("energy", help="Title 24 Part 6 checks from the energy block, or --zip for a climate zone")
    e.add_argument("project", nargs="?")
    e.add_argument("--zip", help="print the climate zone of this ZIP as a Value and source entry")
    e.add_argument("--write-rules", action="store_true",
                   help="replace the T24- rules in project.json with the generated checks")
    e.set_defaults(fn=cmd_energy)
    g = sub.add_parser("green", help="CALGreen measure decisions from the green block")
    g.add_argument("project")
    g.set_defaults(fn=cmd_green)
    api = sub.add_parser("api", help="print every drawing call with its signature, from the code")
    api.add_argument("module", nargs="*", help="limit to these modules, e.g. fixtures site section")
    api.set_defaults(fn=cmd_api)
    mo = sub.add_parser("modules", help="which optional modules are installed, and how to fetch the rest")
    mo.set_defaults(fn=cmd_modules)
    a = ap.parse_args(argv)
    return a.fn(a)
