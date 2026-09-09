# Laguna pool browser rehearsal

A local browser destination for a fictional agent demonstration. No City connection,
account, legal signature, payment, or production record is created. Current public City
configuration verifies Zone Clearance under **type 114, Residential Planning Entitlements**.
This demo follows its required core inputs and Application/Plans PDF categories; the
screen layout and fictional signature are simulated. Prior review is CrossBeam intake
context. Required upload categories are not the City’s complete project checklist.

## Run

From the repository root, choose a private output directory outside the public checkout:

```sh
python3 demos/laguna-pool/server.py --state-dir /absolute/private/demo-state --port 8765
```

Open `http://127.0.0.1:8765`. The server binds to loopback only. It uses Python's standard
library and SQLite; no npm install is needed. Each case has a stable URL. Returning to
that URL resumes the saved draft or receipt across browser and server restarts. A
repeated Submit returns the same receipt. Submitted demo cases are immutable. Fields
are saved when moving between steps; edits not yet saved do not survive a reload.

PDF uploads are stored in the private SQLite database with category, filename, size,
and SHA-256. The local demo accepts PDF files up to 16 MB each. The downloadable JSON
receipt includes values and hashes without embedding the PDF bytes. This local limit
is not a claim about the City's upload limits. Do not expose this development server
on a public interface.

## Fictional files

`fixture.json` is the source of the example inputs. 505 Forest Avenue is a labeled
placeholder, not a proposal for City Hall or evidence of residential zoning. Unknown
real parcel and eligibility facts remain null.

Use the Python dependencies declared in `cities/laguna-beach/requirements.txt`:

```sh
python3 demos/laguna-pool/build-fixture.py --output-dir /absolute/private/demo-packet
```

This creates a sample intake summary, a drawing register, and three visibly fictional
concept sheets: project brief, dimensioned site layout, and pool section/equipment
concept. `draw-plans.py` uses the shared synthetic geometry and a deterministic PDF
canvas. These concepts are not construction plans or permit-ready plan sheets. Nothing in
this generator establishes a permit route or professional compliance.

To exercise the **installed plugin** against the official Zone Clearance form, acquire
its current PDF from the City source page in the browser, then run:

```sh
python3 demos/laguna-pool/fill-official-demo.py \
  --plugin-dir /absolute/path/to/installed/laguna-beach \
  --source-pdf /absolute/private/zone-clearance-application.pdf \
  --packet-dir /absolute/private/demo-packet
```

This verifies the source hash against the installed manifest, invokes the installed
schema/fill/verification helpers, fills the six known contact/project fields, labels
all 43 pages, and updates the packet manifest to use `zone-clearance-demo.pdf` for
Application. Other fields stay unresolved; this is not a complete filing packet.
Inspect rendered output before recording. No official City PDFs are bundled here.

## Browser qualification

Use the host's actual browser tools, not direct API writes, for the rehearsal:

1. Start a new local demo case. Read `fixture.json` and enter its values.
2. Leave prior review blank and omit PDFs; attempt Submit and observe the missing-input
   error. Supply the known fixture answer and continue in the same case.
3. Upload the manifest's Application and Plans files using the browser file chooser.
4. Inspect every value and file in Review, then Submit to the local demo.
5. Verify the visible DEMO receipt. Reload and restart the server; the same case must
   remain available. Compare the persisted upload bytes and values:

```sh
python3 demos/laguna-pool/verify-receipt.py \
  --database /absolute/private/demo-state/demo.sqlite3 \
  --case-id DEMO-REPLACE-WITH-OBSERVED-ID \
  --manifest /absolute/private/demo-packet/fixture-manifest.json \
  --output /absolute/private/browser-verification.json
python3 -m unittest discover -s demos/laguna-pool -p 'test_*.py' -v
```

The September 8 browser runs and Codex installation evidence are in
[`docs/qualification`](../../docs/qualification). Installation/cache discovery,
manual installed-helper/browser operation, automatic skill activation in a fresh
conversation, and production City filing are separate qualifications. Only the first
two have evidence so far; do not report all four as passed.

## Fresh-session activation test

With the candidate installed and Codex authenticated, run this separately from browser
qualification, using a new private output directory each time:

```sh
python3 cities/laguna-beach/evals/run-codex-activation.py \
  --output-dir /absolute/private/new-activation-run
```

The runner opens an ephemeral read-only CLI session in an empty directory with only
“Hey, we want to get a pool in Laguna Beach.” It saves the response and tool events for
manual semantic review; process success alone is not a pass. The September 8 retest
automatically selected the pool skill and read the homeowner journey, then asked about
address, scope, and drawings/prior review. This proves CLI opening behavior, not a
complete fresh-conversation run in the desktop filming app.
