"""Read JPEG and PNG files into PDF image data, standard library only.

JPEG passes through untouched as DCTDecode: the kit reads only the frame
header (size, components, precision) and the EXIF orientation. PNG without
transparency passes through as FlateDecode with the PNG predictor, so the
compressed rows go into the PDF as they are. A PNG with an alpha channel or a
tRNS chunk, or with 16-bit samples, is decoded here (zlib and the five PNG row
filters), written as 8-bit samples, and its alpha becomes a soft mask (SMask).

Unsupported files raise ImageError with what to do: interlaced PNG,
arithmetic-coded, lossless or 12-bit JPEG, any other format.

The output depends only on the file bytes, so a build stays byte-identical.
This is mechanical parsing of two known binary formats.
"""
from __future__ import annotations

import hashlib
import struct
import zlib

from .model import PrintRefused


class ImageError(PrintRefused):
    """The kit cannot read or may not place an image."""


PNG_SIG = b"\x89PNG\r\n\x1a\n"
#: JPEG frame markers PDF's DCTDecode reads: baseline, extended sequential, progressive.
_SOF_OK = {0xC0: "baseline", 0xC1: "extended", 0xC2: "progressive"}
_SOF_NO = {0xC3: "lossless", 0xC5: "differential", 0xC6: "differential progressive",
           0xC7: "differential lossless", 0xC9: "arithmetic", 0xCA: "arithmetic progressive",
           0xCB: "arithmetic lossless", 0xCD: "arithmetic differential",
           0xCE: "arithmetic differential progressive", 0xCF: "arithmetic differential lossless"}
_PNG_CHANNELS = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}
_PNG_DEPTHS = {0: (1, 2, 4, 8, 16), 2: (8, 16), 3: (1, 2, 4, 8), 4: (8, 16), 6: (8, 16)}


class Raster:
    """One image, ready for the PDF writer.

    width, height    pixels of the stored data
    colorspace       "DeviceRGB", "DeviceGray", "DeviceCMYK", or ("Indexed", palette bytes)
    bpc              bits per component
    filter           "DCTDecode" or "FlateDecode"
    data             the stream bytes
    predictor        (colors, bpc, columns) when the data carries PNG row filters
    decode           a /Decode array or None
    smask            a Raster (DeviceGray) holding the alpha, or None
    orientation      EXIF orientation 1-8; the placement turns the image upright
    mime, original   the file type and bytes, for an SVG data URI
    sha256           of the file bytes
    """

    def __init__(self, **kw):
        self.smask = None
        self.predictor = None
        self.decode = None
        self.orientation = 1
        self.original = b""
        self.mime = ""
        self.sha256 = ""
        self.__dict__.update(kw)

    @property
    def display_size(self) -> tuple:
        """Pixel width and height as the image is meant to be seen (after EXIF orientation)."""
        if self.orientation in (5, 6, 7, 8):
            return self.height, self.width
        return self.width, self.height


def load(path: str) -> Raster:
    with open(path, "rb") as fh:
        data = fh.read()
    return from_bytes(data, name=path)


def from_bytes(data: bytes, name: str = "image") -> Raster:
    if data[:8] == PNG_SIG:
        r = _png(data, name)
        r.mime = "image/png"
    elif data[:2] == b"\xff\xd8":
        r = _jpeg(data, name)
        r.mime = "image/jpeg"
    else:
        raise ImageError(f"{name}: not a JPEG or PNG file. Save it as JPEG (.jpg) or PNG (.png) "
                         "and point images[].path at that file")
    r.original = data
    r.sha256 = hashlib.sha256(data).hexdigest()
    return r


# ------------------------------------------------------------------ JPEG

def _jpeg(data: bytes, name: str) -> Raster:
    pos, n = 2, len(data)
    orientation, adobe, frame = 1, False, None
    while pos + 4 <= n:
        if data[pos] != 0xFF:
            raise ImageError(f"{name}: damaged JPEG (no marker at byte {pos})")
        marker = data[pos + 1]
        if marker == 0xFF:                      # fill byte
            pos += 1
            continue
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        if marker in (0xD9, 0xDA):              # end of image, start of scan
            break
        seg_len = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        seg = data[pos + 4:pos + 2 + seg_len]
        if marker == 0xE1 and seg[:6] == b"Exif\x00\x00":
            orientation = _exif_orientation(seg[6:]) or 1
        elif marker == 0xEE and seg[:5] == b"Adobe":
            adobe = True
        elif marker in _SOF_NO:
            raise ImageError(f"{name}: {_SOF_NO[marker]} JPEG is not supported by PDF readers. "
                             "Re-save it as an ordinary (baseline) JPEG or as PNG")
        elif marker in _SOF_OK and frame is None:
            prec, h, w, comps = struct.unpack(">BHHB", seg[:6])
            frame = (prec, w, h, comps)
        pos += 2 + seg_len
    if frame is None:
        raise ImageError(f"{name}: JPEG has no frame header the kit can read")
    prec, w, h, comps = frame
    if prec != 8:
        raise ImageError(f"{name}: {prec}-bit JPEG is not supported; re-save it as 8-bit JPEG or PNG")
    if w == 0 or h == 0:
        raise ImageError(f"{name}: JPEG gives no image size in its header; re-save it")
    spaces = {1: "DeviceGray", 3: "DeviceRGB", 4: "DeviceCMYK"}
    if comps not in spaces:
        raise ImageError(f"{name}: JPEG with {comps} color components is not supported")
    decode = [1, 0, 1, 0, 1, 0, 1, 0] if comps == 4 and adobe else None
    return Raster(width=w, height=h, colorspace=spaces[comps], bpc=8, filter="DCTDecode",
                  data=data, decode=decode, orientation=orientation if 1 <= orientation <= 8 else 1)


def _exif_orientation(tiff: bytes) -> int | None:
    """The Orientation tag (0x0112) of IFD0 in a TIFF-structured EXIF block."""
    if len(tiff) < 8 or tiff[:2] not in (b"II", b"MM"):
        return None
    e = "<" if tiff[:2] == b"II" else ">"
    try:
        ifd = struct.unpack(e + "I", tiff[4:8])[0]
        count = struct.unpack(e + "H", tiff[ifd:ifd + 2])[0]
        for i in range(count):
            at = ifd + 2 + 12 * i
            tag, typ = struct.unpack(e + "HH", tiff[at:at + 4])
            if tag == 0x0112 and typ == 3:
                return struct.unpack(e + "H", tiff[at + 8:at + 10])[0]
    except struct.error:
        return None
    return None


# ------------------------------------------------------------------ PNG

def _png(data: bytes, name: str) -> Raster:
    pos, idat, plte, trns, ihdr = 8, [], None, None, None
    while pos + 8 <= len(data):
        length, ctype = struct.unpack(">I4s", data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + length]
        crc = data[pos + 8 + length:pos + 12 + length]
        if len(body) != length or len(crc) != 4 or zlib.crc32(ctype + body) != struct.unpack(">I", crc)[0]:
            raise ImageError(f"{name}: damaged PNG (chunk {ctype.decode('latin-1')!r} fails its checksum)")
        if ctype == b"IHDR":
            ihdr = struct.unpack(">IIBBBBB", body)
        elif ctype == b"PLTE":
            plte = body
        elif ctype == b"tRNS":
            trns = body
        elif ctype == b"IDAT":
            idat.append(body)
        elif ctype == b"IEND":
            break
        pos += 12 + length
    if ihdr is None or not idat:
        raise ImageError(f"{name}: PNG has no image header or no image data")
    w, h, depth, ctype, comp, filt, interlace = ihdr
    if ctype not in _PNG_CHANNELS or depth not in _PNG_DEPTHS[ctype] or comp or filt:
        raise ImageError(f"{name}: PNG color type {ctype} at {depth} bits is not a valid PNG")
    if interlace:
        raise ImageError(f"{name}: interlaced PNG is not supported. Re-save it without interlacing "
                         "(most editors: uncheck 'interlaced' or 'progressive')")
    if ctype == 3 and not plte:
        raise ImageError(f"{name}: paletted PNG has no palette")
    stream = b"".join(idat)
    colors = _PNG_CHANNELS[ctype] if ctype in (0, 2, 3) else _PNG_CHANNELS[ctype] - 1
    if trns is None and ctype in (0, 2, 3) and depth <= 8:
        # Pass the compressed rows through; the PNG predictor undoes the row filters.
        space = ("Indexed", plte) if ctype == 3 else ("DeviceRGB" if ctype == 2 else "DeviceGray")
        return Raster(width=w, height=h, colorspace=space, bpc=depth, filter="FlateDecode",
                      data=stream, predictor=(colors, depth, w))
    try:
        raw = zlib.decompress(stream)
    except zlib.error as exc:
        raise ImageError(f"{name}: damaged PNG data ({exc})") from None
    rows = _unfilter(raw, w, h, _PNG_CHANNELS[ctype], depth, name)
    color, alpha = _samples(rows, w, h, ctype, depth, plte, trns)
    space = "DeviceGray" if ctype in (0, 4) else "DeviceRGB"
    r = Raster(width=w, height=h, colorspace=space, bpc=8, filter="FlateDecode",
               data=zlib.compress(bytes(color), 9))
    if alpha is not None and min(alpha) < 255:
        r.smask = Raster(width=w, height=h, colorspace="DeviceGray", bpc=8, filter="FlateDecode",
                         data=zlib.compress(bytes(alpha), 9))
    return r


def _unfilter(raw: bytes, w: int, h: int, channels: int, depth: int, name: str) -> list:
    """Undo the PNG row filters. Returns one bytearray per row."""
    bpp = max(1, channels * depth // 8)
    stride = (w * channels * depth + 7) // 8
    if len(raw) < h * (stride + 1):
        raise ImageError(f"{name}: PNG data is shorter than its size says")
    prev = bytearray(stride)
    rows = []
    for y in range(h):
        at = y * (stride + 1)
        ftype = raw[at]
        row = bytearray(raw[at + 1:at + 1 + stride])
        if ftype == 1:
            for i in range(bpp, stride):
                row[i] = (row[i] + row[i - bpp]) & 0xFF
        elif ftype == 2:
            row = bytearray((a + b) & 0xFF for a, b in zip(row, prev))
        elif ftype == 3:
            for i in range(stride):
                left = row[i - bpp] if i >= bpp else 0
                row[i] = (row[i] + ((left + prev[i]) >> 1)) & 0xFF
        elif ftype == 4:
            for i in range(stride):
                a = row[i - bpp] if i >= bpp else 0
                b = prev[i]
                c = prev[i - bpp] if i >= bpp else 0
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                pred = a if pa <= pb and pa <= pc else (b if pb <= pc else c)
                row[i] = (row[i] + pred) & 0xFF
        elif ftype != 0:
            raise ImageError(f"{name}: damaged PNG (row filter {ftype})")
        rows.append(row)
        prev = row
    return rows


def _unpack(row: bytes, w: int, depth: int) -> list:
    """Samples of a row with 1, 2 or 4 bits per sample, one int per sample."""
    per = 8 // depth
    mask = (1 << depth) - 1
    out = []
    for b in row:
        for k in range(per):
            out.append((b >> (8 - depth * (k + 1))) & mask)
    return out[:w]


def _samples(rows, w, h, ctype, depth, plte, trns):
    """8-bit color samples and alpha (or None) for a PNG that cannot pass through."""
    color, alpha = bytearray(), bytearray()
    has_alpha = ctype in (4, 6) or trns is not None
    if ctype == 3:
        table = [plte[3 * i:3 * i + 3] for i in range(len(plte) // 3)]
        ta = list(trns or b"") + [255] * (256 - len(trns or b""))
        for row in rows:
            for idx in (_unpack(row, w, depth) if depth < 8 else row):
                color += table[idx] if idx < len(table) else b"\x00\x00\x00"
                alpha.append(ta[idx])
        return color, alpha
    ch = _PNG_CHANNELS[ctype]
    for row in rows:
        if depth == 16:
            row = row[0::2]                      # the high byte of each sample
        elif depth < 8:                          # gray only
            maxv = (1 << depth) - 1
            row = bytearray(v * 255 // maxv for v in _unpack(row, w, depth))
        if ctype in (4, 6):
            n = ch - 1
            px = bytearray(w * n)
            for k in range(n):
                px[k::n] = row[k::ch]
            color += px
            alpha += row[ch - 1::ch]
        else:
            color += row
    if ctype in (0, 2) and trns is not None:
        # tRNS names one color that is fully transparent (16-bit values, compared at the source depth)
        key = [struct.unpack(">H", trns[i:i + 2])[0] for i in range(0, len(trns), 2)]
        if depth == 16:
            key = [k >> 8 for k in key]
        elif depth < 8:
            key = [k * 255 // ((1 << depth) - 1) for k in key]
        n = ch
        for i in range(w * h):
            alpha.append(0 if list(color[i * n:i * n + n]) == key else 255)
    return color, (alpha if has_alpha else None)


# ------------------------------------------------------------------ placement

#: EXIF orientation -> (X = a*u + b*v + c, Y = d*u + e*v + f), mapping the stored
#: image's unit square (u right, v up) onto the upright image's unit square.
ORIENT = {1: (1, 0, 0, 0, 1, 0), 2: (-1, 0, 1, 0, 1, 0), 3: (-1, 0, 1, 0, -1, 1),
          4: (1, 0, 0, 0, -1, 1), 5: (0, -1, 1, -1, 0, 1), 6: (0, 1, 0, -1, 0, 1),
          7: (0, 1, 0, 1, 0, 0), 8: (0, -1, 1, 1, 0, 0)}


def placement_matrix(orientation: int, box) -> tuple:
    """The PDF image matrix [a b c d e f] that draws the image upright filling box (points)."""
    x0, y0, x1, y1 = box
    bw, bh = x1 - x0, y1 - y0
    p, q, r, s, t, u = ORIENT.get(orientation, ORIENT[1])
    return (p * bw, s * bh, q * bw, t * bh, x0 + r * bw, y0 + u * bh)


def encode_png(width: int, height: int, pixels: bytes, color_type: int = 2, depth: int = 8,
               palette: bytes | None = None, trns: bytes | None = None) -> bytes:
    """A PNG file from raw rows (no filter bytes), standard library only.

    For placeholder and test images. color_type 0 gray, 2 RGB, 3 paletted
    (pass palette, 3 bytes per entry, and optional trns), 4 gray+alpha, 6 RGBA.
    """
    stride = (width * _PNG_CHANNELS[color_type] * depth + 7) // 8
    if len(pixels) != stride * height:
        raise ValueError(f"pixels hold {len(pixels)} bytes; {width} x {height} needs {stride * height}")
    raw = b"".join(b"\x00" + pixels[y * stride:(y + 1) * stride] for y in range(height))

    def chunk(kind: bytes, body: bytes) -> bytes:
        return struct.pack(">I", len(body)) + kind + body + struct.pack(">I", zlib.crc32(kind + body))
    out = PNG_SIG + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, depth, color_type, 0, 0, 0))
    if palette is not None:
        out += chunk(b"PLTE", palette)
    if trns is not None:
        out += chunk(b"tRNS", trns)
    return out + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
