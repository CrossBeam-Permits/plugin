"""Units, drawing scales and dimension text.

All model lengths are real inches. All paper lengths are PDF points (72 per inch).
A scale is "paper inches per real inch". Points per real inch = ratio * 72.

Dimension text uses fractions, never decimals: 11'-9 1/4".
"""
from __future__ import annotations

import math
import re
from fractions import Fraction

PT_PER_IN = 72.0

# Sheet sizes in inches, landscape (width, height).
SHEET_SIZES = {
    "ARCH_E": (48.0, 36.0),
    "ARCH_D": (36.0, 24.0),
    "ARCH_C": (24.0, 18.0),
    "ANSI_B": (17.0, 11.0),
    "LETTER": (11.0, 8.5),
}


class ScaleError(ValueError):
    """A view does not fit at its stated scale, or a scale label is unknown."""


class Scale:
    """A drawing scale. `ratio` is paper inches per real inch."""

    def __init__(self, label: str, ratio: float | None):
        self.label = label
        self.ratio = ratio            # None means not to scale (N.T.S.)

    @property
    def pt_per_in(self) -> float:
        if self.ratio is None:
            raise ScaleError("N.T.S. has no points per inch")
        return self.ratio * PT_PER_IN

    @property
    def is_true(self) -> bool:
        return self.ratio is not None

    @property
    def printed(self) -> str:
        """The scale a sheet prints. A scale that is not true prints N.T.S."""
        return self.label if self.is_true else NTS.label

    def __repr__(self):
        return f"Scale({self.label!r}, {self.ratio})"


def _arch(paper_in: str) -> tuple[str, float]:
    # Architectural: <paper_in>" = 1'-0". Ratio = paper inches per 12 real inches.
    label = f'{paper_in}" = 1\'-0"'
    return label, float(_parse_mixed(paper_in)) / 12.0


def _eng(feet: int) -> tuple[str, float]:
    # Engineering: 1" = <feet>'. Ratio = 1 paper inch per feet*12 real inches.
    return f"1\" = {feet}'-0\"", 1.0 / (feet * 12.0)


def _parse_mixed(s: str) -> Fraction:
    """'1-1/2' or '1 1/2' or '3/16' or '3' -> Fraction."""
    parts = s.strip().replace(" ", "-").split("-")
    return sum((Fraction(p) for p in parts if p), Fraction(0))


_STANDARD = [_arch(p) for p in ("1/32", "1/16", "1/8", "3/16", "1/4", "3/8", "1/2", "3/4", "1", "1-1/2", "3", "6")]
_STANDARD += [_eng(f) for f in (10, 20, 30, 40, 50, 60, 100)]
_STANDARD += [("FULL SIZE", 1.0), ("HALF SIZE", 0.5)]

#: Every scale the kit knows, keyed by its printed label.
SCALES = {label: Scale(label, ratio) for label, ratio in _STANDARD}
NTS = Scale("N.T.S.", None)

_ALIASES = {"NTS": "N.T.S.", "N.T.S.": "N.T.S.", "FULL": "FULL SIZE", "1:1": "FULL SIZE",
            "12\" = 1'-0\"": "FULL SIZE"}


def scale(label: str) -> Scale:
    """Look up a scale by its printed label or a short form.

    Short forms: '1/4' means 1/4" = 1'-0". '1:10' or "1\"=10'" means 1" = 10'-0".
    """
    if isinstance(label, Scale):
        return label
    key = label.strip()
    key = _ALIASES.get(key.upper(), key)
    if key == "N.T.S.":
        return NTS
    if key in SCALES:
        return SCALES[key]
    norm = key.replace(" ", "")
    for s in SCALES.values():
        if s.label.replace(" ", "") == norm:
            return s
    m = re.fullmatch(r"(\d+(?:[- ]\d+)?(?:/\d+)?)", key)
    if m:
        lab, _ = _arch(m.group(1))
        if lab in SCALES:
            return SCALES[lab]
    m = re.fullmatch(r"1:(\d+)|1\"?=(\d+)'(?:-0\")?", norm)
    if m:
        feet = int(m.group(1) or m.group(2))
        lab, _ = _eng(feet)
        if lab in SCALES:
            return SCALES[lab]
    raise ScaleError(f"unknown scale {label!r}; known: {', '.join(SCALES)}")


#: The size scales: a detail drawn at (or at half) its real size.
SIZE_SCALES = ("FULL SIZE", "HALF SIZE")


def scale_kind(sc) -> str:
    """'size' (FULL SIZE, HALF SIZE), 'arch' (<n>" = 1'-0"), 'eng' (1" = <n>'-0") or 'nts'."""
    sc = scale(sc)
    if not sc.is_true:
        return "nts"
    if sc.label in SIZE_SCALES:
        return "size"
    return "arch" if sc.label.endswith("= 1'-0\"") else "eng"


def parse_scale_label(label: str) -> float | None:
    """Paper inches per real inch, read from a printed scale label.

    QA uses this to check a placed view without trusting the kit's own table.
    Returns None for N.T.S.
    """
    t = label.upper().replace(" ", "")
    if t in ("N.T.S.", "NTS"):
        return None
    if t == "FULLSIZE":
        return 1.0
    if t == "HALFSIZE":
        return 0.5
    m = re.fullmatch(r'(\d+(?:-\d+)?(?:/\d+)?)"=1\'-0"', t)
    if m:
        return float(_parse_mixed(m.group(1))) / 12.0
    m = re.fullmatch(r'1"=(\d+)\'(?:-0")?', t)
    if m:
        return 1.0 / (int(m.group(1)) * 12.0)
    raise ScaleError(f"cannot read scale label {label!r}")


# ---------------------------------------------------------------- lengths


def _split(inches: float, denom: int, toward: str | None = None) -> tuple[int, int, Fraction, bool]:
    """Round to 1/denom, half up, and split into (feet, whole inches, fraction, negative).

    Half up, not Python's round-half-to-even: 1/32 in. at 1/16 prints 1/16, and
    3/32 prints 1/8, so equal halves always round the same way. `toward` "up" or
    "down" rounds that way instead (a value with a maximum prints rounded up).
    """
    if toward in ("up", "down"):
        step = math.ceil if toward == "up" else math.floor
        signed = Fraction(step(inches * denom + (-1e-6 if toward == "up" else 1e-6)), denom)
        neg, q = signed < 0, abs(signed)
    elif toward is None:
        neg = inches < 0
        q = Fraction(math.floor(abs(inches) * denom + 0.5), denom)
    else:
        raise ValueError(f"toward must be 'up', 'down' or None, got {toward!r}")
    whole_in = int(q)
    frac = q - whole_in
    feet, rem = divmod(whole_in, 12)
    return feet, rem, frac, neg


def _frac_text(frac: Fraction) -> str:
    return f"{frac.numerator}/{frac.denominator}" if frac else ""


def fmt_in(inches: float, denom: int = 16, toward: str | None = None) -> str:
    """Inches only: 141.25 -> 141 1/4"   0.5 -> 1/2"   6 -> 6"."""
    _check_denom(denom)
    feet, rem, frac, neg = _split(inches, denom, toward)
    whole = feet * 12 + rem
    sign = "-" if neg and (whole or frac) else ""
    if whole and frac:
        return f'{sign}{whole} {_frac_text(frac)}"'
    if frac:
        return f'{sign}{_frac_text(frac)}"'
    return f'{sign}{whole}"'


def fmt_ftin(inches: float, denom: int = 16, toward: str | None = None) -> str:
    """Feet and inches: 141.25 -> 11'-9 1/4"   144 -> 12'-0".

    Under a foot (after rounding) it prints inches only, the way a professional
    set does: 9.5 -> 9 1/2", not 0'-9 1/2".
    """
    _check_denom(denom)
    feet, rem, frac, neg = _split(inches, denom, toward)
    if not feet:
        return fmt_in(inches, denom, toward)
    sign = "-" if neg else ""
    inch = f"{rem} {_frac_text(frac)}" if frac else f"{rem}"
    return f"{sign}{feet}'-{inch}\""


def fmt_len(inches: float, style: str = "ftin", denom: int = 16, toward: str | None = None) -> str:
    """Format a length by style: 'ftin', 'in', 'both' (216" (18'-0")), or 'auto'.

    'auto' prints inches below 10'-0" and feet-inches at or above it. `toward`
    ("up", "down") rounds that way to the 1/denom grid instead of to the nearest.
    """
    if style == "in":
        return fmt_in(inches, denom, toward)
    if style == "ftin":
        return fmt_ftin(inches, denom, toward)
    if style == "both":
        a, b = fmt_in(inches, denom, toward), fmt_ftin(inches, denom, toward)
        return a if a == b else f"{a} ({b})"          # under a foot both forms are inches
    if style == "auto":
        return fmt_in(inches, denom, toward) if abs(inches) < 120 else fmt_ftin(inches, denom, toward)
    raise ValueError(f"unknown length style {style!r}")


def _check_denom(denom: int) -> None:
    if denom not in (1, 2, 4, 8, 16, 32, 64):
        raise ValueError(f"precision denominator must be a power of two up to 64, got {denom}")


_LEN = re.compile(
    r"""^\s*(?P<neg>-)?\s*
        (?:(?P<ft>\d+)\s*'\s*-?\s*)?
        (?:(?P<in>\d+)(?:\s+(?P<fn>\d+)/(?P<fd>\d+))?|(?P<on>\d+)/(?P<od>\d+))?
        \s*"?\s*$""",
    re.X,
)


def parse_len(text: str) -> float:
    """Inverse of the formatters: 11'-9 1/4" -> 141.25. Mechanical parsing only."""
    m = _LEN.match(text)
    if not m or not any(m.group(g) for g in ("ft", "in", "on")):
        raise ValueError(f"not a length: {text!r}")
    v = 0.0
    if m.group("ft"):
        v += 12 * int(m.group("ft"))
    if m.group("in"):
        v += int(m.group("in"))
    if m.group("fn"):
        v += int(m.group("fn")) / int(m.group("fd"))
    if m.group("on"):
        v += int(m.group("on")) / int(m.group("od"))
    return -v if m.group("neg") else v


def fmt_len_exact(inches: float, style: str = "ftin", denom: int = 16, places: int | None = None) -> str:
    """A length that must keep its value, such as a code limit: fractions when the
    value is a whole number of 1/denom inches, else decimal inches (0.019 -> 0.019").

    Rounding a limit to the drawing precision changes it (a 0.019 in. flashing
    prints 0"), so a value that is not on the 1/denom grid prints as decimals:
    `places` of them when given (the source's own), else up to four.
    """
    _check_denom(denom)
    x = float(inches)
    if abs(x * denom - round(x * denom)) < 1e-6:
        return fmt_len(x, style, denom)
    nd = places if places is not None else 4
    t = f"{x:.{nd}f}"
    if places is None:
        t = t.rstrip("0").rstrip(".")
    return t + '"'


def num(v: float, nd: int = 3) -> str:
    """Stable number text for PDF and SVG output. No exponent, no '-0'."""
    if not math.isfinite(v):
        raise ValueError(f"non-finite coordinate {v}")
    s = f"{v:.{nd}f}".rstrip("0").rstrip(".")
    return "0" if s in ("", "-0") else s


# ---------------------------------------------------------------- unit conversion

#: Each accepted unit spelling, by dimension, with its factor to the base unit
#: of that dimension (inch, square inch, percent, degree, count). Spellings
#: are compared lower-case with spaces and periods removed, so "sq ft",
#: "Sq. Ft." and "SQFT" are one unit. Mechanical name lookup only.
_UNITS = {
    "in": ("length", 1.0), "inch": ("length", 1.0), "inches": ("length", 1.0), '"': ("length", 1.0),
    "ft": ("length", 12.0), "foot": ("length", 12.0), "feet": ("length", 12.0), "'": ("length", 12.0),
    "sf": ("area", 144.0), "sqft": ("area", 144.0), "ft2": ("area", 144.0), "ft^2": ("area", 144.0),
    "squarefeet": ("area", 144.0), "squarefoot": ("area", 144.0),
    "sqin": ("area", 1.0), "in2": ("area", 1.0), "in^2": ("area", 1.0), "squareinches": ("area", 1.0),
    "pct": ("percent", 1.0), "%": ("percent", 1.0), "percent": ("percent", 1.0),
    "ratio": ("percent", 100.0),
    "deg": ("angle", 1.0), "degree": ("angle", 1.0), "degrees": ("angle", 1.0),
    "count": ("count", 1.0), "ea": ("count", 1.0), "each": ("count", 1.0),
    # time: a fire rating in hours, a cure or inspection period in days
    "hr": ("time", 1.0), "hrs": ("time", 1.0), "hour": ("time", 1.0), "hours": ("time", 1.0),
    "days": ("time", 24.0), "day": ("time", 24.0),
}

#: Units QA compares only against the same unit: a drawn 50 cfm checks a limit
#: in cfm, never one in gpm or in inches. Each is a dimension of its own, so a
#: limit in another unit is refused as a unit of another kind, the way a length
#: limit on an area is. Canonical spelling (the one project.json and
#: crossbeam_rules kit_checks use) -> (dimension name, other accepted spellings).
SAME_UNIT_ONLY = {
    "cfm": ("airflow, cfm", ("cubicfeetperminute", "ft3/min", "ft^3/min")),
    "gpm": ("flow rate, gpm", ("gal/min", "gallonsperminute")),
    "gpf": ("flush volume, gpf", ("gal/flush", "gallonsperflush")),
    "A": ("current, A", ("amp", "amps", "ampere", "amperes")),
    "psi": ("pressure, psi", ("lb/sqin", "lb/in2", "lb/in^2", "poundspersquareinch")),
    "psf": ("load, psf", ("lb/sqft", "lb/ft2", "lb/ft^2", "lbs/sqft", "poundspersquarefoot")),
    "lb": ("weight, lb", ("lbs", "pound", "pounds")),
    "mph": ("speed, mph", ("milesperhour",)),
    "degF": ("temperature, degF", ("°f", "fahrenheit", "degreesfahrenheit")),
    "u-factor": ("U-factor", ("ufactor", "btu/h-ft2-f", "btu/hft2f")),
    "in/ft": ("slope, in/ft", ("inperft", "inchesperfoot", "in/foot")),
    # Title 24 energy (energy.py): an insulation R-value checks only an R-value limit.
    "R-value": ("thermal resistance, R-value", ("rvalue", "r-val")),
    # A test index with no unit: flame spread index, smoke-developed index (ASTM E84).
    "index": ("test index", ("idx",)),
}
for _canon, (_dim, _spellings) in SAME_UNIT_ONLY.items():
    for _s in (_canon, *_spellings):
        _UNITS[_s.lower().replace(" ", "").replace(".", "").replace("_", "")] = (_dim, 1.0)

#: Every unit a rule or a value may name, canonical spellings, for messages.
KNOWN_UNITS = ("in", "ft", "sf (sq ft)", "sq in", "pct (%)", "ratio", "deg", "count", "hr", "days",
               *SAME_UNIT_ONLY)

#: How a sheet names a unit after a number: 50 CFM, 100 A, 2 HR, 0.30 U-FACTOR.
#: Units not listed print upper-case.
_UNIT_WORDS = {"sf": "SQ FT", "sqft": "SQ FT", "sq ft": "SQ FT", "sq in": "SQ IN", "sqin": "SQ IN",
               "pct": "%", "%": "%", "percent": "%", "deg": "DEG", "degF": "DEG F", "hr": "HR",
               "days": "DAYS", "count": "", "ratio": "", "R-value": "", "index": ""}


def unit_word(unit: str) -> str:
    """The word a sheet prints after a number in this unit ('' for a count or a ratio)."""
    return _UNIT_WORDS.get(unit, _UNIT_WORDS.get(str(unit).lower(), str(unit).upper()))


class UnitError(ValueError):
    """A unit the kit does not know, or two units that measure different things."""


def unit_info(unit: str) -> tuple[str, float]:
    """(dimension, factor to the dimension's base unit) for a unit spelling."""
    key = str(unit).strip().lower().replace(" ", "").replace(".", "").replace("_", "")
    if key not in _UNITS:
        raise UnitError(f"unknown unit {unit!r}; known: {', '.join(KNOWN_UNITS)}")
    return _UNITS[key]


def convert(x: float, from_unit: str, to_unit: str) -> float:
    """Convert a number between units of one dimension: 84 in -> 7 ft, 0.08 ratio -> 8 pct.

    A unit in SAME_UNIT_ONLY converts only to itself (50 cfm -> 50 cfm).
    Raises UnitError for an unknown unit or for units of different dimensions.
    """
    d_from, f_from = unit_info(from_unit)
    d_to, f_to = unit_info(to_unit)
    if d_from != d_to:
        raise UnitError(f"cannot convert {from_unit!r} ({d_from}) to {to_unit!r} ({d_to})")
    return float(x) * f_from / f_to
