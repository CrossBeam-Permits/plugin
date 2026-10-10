# Form source policy

Use only the exact City revision pinned in `assets/form-manifest.json`. The manifest records source-page URL, document URL/id/ticks, printed revision, retrieval date, SHA-256, byte/page count, canonical field count, widget count, field-map version, redistribution mode, and a `status`. Fill only forms whose status is `pinned`. A `needs_source` form names the current City link and stops until that revision is pinned and remapped. `retired_forms` keeps the receipt of a revision the plugin no longer fills; a file with that checksum fails the freshness check.

## Acquisition

1. Download from the official City link immediately before preparation or release packaging.
2. Save every downloaded form to `permit-work/input/official-forms/`. Keep the City's file name or the manifest `cache_name`.
3. Run the freshness check against that folder:

   ```sh
   python3 scripts/check-source-freshness.py \
     --manifest assets/form-manifest.json \
     --forms-dir permit-work/input/official-forms \
     --only building-application \
     --receipt permit-work/state/form-source-receipt.json
   ```

4. Stop on any checksum, page, canonical-field, widget, document-id/ticks, or printed-revision drift, and on any `needs_source` status. Report the exact URL from the error.
5. Never use the repository's older `standard-plans` Planning PDFs as current forms.

`--fetch` tries a direct download first. The Building application is on `gis.lagunabeachcity.net`, which serves scripts normally; fetch it over `https://` (the portal prints an `http://` link that returns 404).

### When the City returns 403

The City website, `www.lagunabeachcity.net`, sits behind Akamai. It returns HTTP 403 ("Access Denied", server `AkamaiGHost`) to scripts, `curl`, and headless browsers. This includes the Applications & Handouts pages and every `showpublisheddocument` link. Do not retry, rotate user agents, or look for mirrors.

Download in the applicant's own visible browser instead. This works on any host:

1. Use whatever browser or computer-use tool the host provides that drives a browser the user can see. Do not assume a product or tool name. If the host has none, give the user the exact URL and ask them to download the form themselves.
2. Open the official source page from the manifest (`source_pages`), not a search result or a saved copy.
3. Find the named application link. Compare its document id and ticks with the manifest entry. A different id or ticks means the City has a new revision: stop that form as `needs_source` and report both links.
4. Download the file. Save it, or ask the user to move it, into `permit-work/input/official-forms/`.
5. Run `check-source-freshness.py` as above. Only a passing check makes the file usable.

If the browser download is blocked too, or no visible browser exists, stop that form. Mark it blocked with the exact official URL. Do not claim a refresh.

The plugin does not include City PDF binaries. Redistribution remains unapproved; the task fetches from the official source and verifies the pinned receipt.

## Field maps

`assets/field-maps/*.json` enumerate the exact field tree and widgets for one checksum. Canonical mappings name exact PDF fields; they never fuzzy-match. A field can be intentionally unmapped if visual/manual placement is still required, but the form cannot be called fully automated until every intended field is mapped and verified.

A map can also carry:

- `required_declarations`: applicant declarations that must be confirmed before the form fills (for the Building application, `permittee.type`; see `applicant-confirmations.md`).
- `only_when` on a mapping: the field fills only when a confirmed declaration has that value. Contractor blocks fill only on a licensed-contractor permit and stay blank on an owner-builder permit.
- `signature_blocks`: every place the applicant signs or dates, with page and rectangle. `fill-form.py` refuses any mapping that targets one.

## Logical and visual verification

For editable PDFs, reopen the output and require:

- intended canonical fields present with expected `/V` values;
- each corresponding widget's effective value agrees;
- non-empty `/AP /N` appearance on updated widgets;
- source checksum matches the field map;
- rendered pages show no clipped/overlapped values or stale appearances;
- signature/declaration fields remain unresolved until the user acts.

If a rendered checkbox shows "NO GLYPH", the renderer lacks the ZapfDingbats font. The check state is still in the PDF; confirm it from `verify-form.py` and install the URW base fonts for a faithful preview.

Never flatten a signed form unless the user explicitly chooses a static output. Preserve an editable copy.

## Sign before upload

The portal says: "Please be sure to sign applications before uploading into the permit portal." [source: EnerGov type 183 and 214 attachment instructions, 2026-10-09]. Hash the signed file, not the unsigned fill.

1. Fill, verify, and render the form. Show the rendered pages to the applicant.
2. The applicant signs the filled PDF themselves: print, wet-sign, and scan, or use their own e-signature tool. The agent never draws, types, places, or applies a signature or signature date, and never uses a stored signature image.
3. Save the signed file as `permit-work/output/forms/<form>-signed.pdf`.
4. Check it:

   ```sh
   python3 scripts/verify-signed-form.py \
     --signed permit-work/output/forms/building-application-signed.pdf \
     --filled permit-work/output/forms/building-application-filled.pdf \
     --answers permit-work/output/forms/building-application-filled.answers-used.json \
     --field-map assets/field-maps/building-application.json \
     --output-dir permit-work/output/previews/building-application-signed
   ```

   The script confirms the file changed and kept its page count. It re-runs `verify-form.py` when the fields survive signing. When the file is flattened or scanned, it lists every value to compare by eye. It measures new ink in each signature block and renders close-ups in `signature-crops/`.
5. Look at every rendered page and every signature crop. Values must match the unsigned preview, and each signature line must carry the applicant's signature. The ink measurement is only a pointer; the visual check decides.
6. `signature_missing` means a signature block has no new ink. Ask the applicant to sign it. Use `--visually-confirmed <block id>` only when the applicant's signature is plainly visible but sits outside the measured box.
7. Use `signed_sha256` from `signed-verification.json` in the packet manifest. Upload only that file. Re-run the check if the file changes.
