# Form source policy

Use only the exact City revision pinned in `assets/form-manifest.json`. The manifest records source-page URL, document URL/id/ticks, printed revision, retrieval date, SHA-256, byte/page count, canonical field count, widget count, field-map version, and redistribution mode.

## Acquisition

1. Download from the official City link immediately before preparation or release packaging.
2. If automated retrieval receives 403, use a user-visible browser on the official source page and download the visible named link.
3. Run `scripts/check-source-freshness.py` against the local directory.
4. Stop on any checksum, page, canonical-field, widget, document-id/ticks, or printed-revision drift.
5. Never use the repository's older `standard-plans` Planning PDFs as current forms.

The standalone source ZIP does not include City PDF binaries. Redistribution remains unapproved; the installer/task fetches from the official source and verifies the pinned receipt.

## Field maps

`assets/field-maps/*.json` enumerate the exact field tree and widgets for one checksum. Canonical mappings name exact PDF fields; they never fuzzy-match. A field can be intentionally unmapped if visual/manual placement is still required, but the form cannot be called fully automated until every intended field is mapped and verified.

## Logical and visual verification

For editable PDFs, reopen the output and require:

- intended canonical fields present with expected `/V` values;
- each corresponding widget's effective value agrees;
- non-empty `/AP /N` appearance on updated widgets;
- source checksum matches the field map;
- rendered pages show no clipped/overlapped values or stale appearances;
- signature/declaration fields remain unresolved until the user acts.

Never flatten a signed form unless the user explicitly chooses a static output. Preserve an editable copy.
