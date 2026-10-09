// node --test scripts/check-laguna-law-sources.test.mjs
//
// The content-stream fingerprint lets a re-issued ordinance PDF pass only when
// its page content is unchanged. These cases pin the parts that are easy to get
// wrong: an indirect /Length, a renumbered re-issue, and a truncated download.

import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { test } from "node:test";
import { deflateSync } from "node:zlib";

const script = path.join(import.meta.dirname, "check-laguna-law-sources.mjs");
const work = mkdtempSync(path.join(tmpdir(), "law-fingerprint-"));

function pdf(name, content, { lengthObject = 17, documentId = "AAAA", truncateTo } = {}) {
  const data = deflateSync(Buffer.from(content));
  let bytes = Buffer.concat([
    Buffer.from("%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n"),
    Buffer.from(`4 0 obj\n<< /Filter /FlateDecode /Length ${lengthObject} 0 R >>\nstream\n`),
    data,
    Buffer.from(`\nendstream\nendobj\n${lengthObject} 0 obj\n${data.length}\nendobj\n`),
    Buffer.from(`trailer\n<< /ID [<${documentId}>] >>\n%%EOF\n`),
  ]);
  if (truncateTo) bytes = bytes.subarray(0, truncateTo);
  const file = path.join(work, name);
  writeFileSync(file, bytes);
  return file;
}

function fingerprint(file) {
  const output = execFileSync(process.execPath, [script, "--fingerprint", file], { encoding: "utf8", timeout: 10000 });
  return JSON.parse(output).contentStreamsSha256;
}

const ordinance = "BT (Section 4 extends the ordinance for 22 months and 15 days) Tj ET";

test("a renumbered re-issue with the same page content keeps its fingerprint", () => {
  const original = pdf("original.pdf", ordinance);
  const reissued = pdf("reissued.pdf", ordinance, { lengthObject: 23, documentId: "BBBB" });
  assert.equal(fingerprint(reissued), fingerprint(original));
});

test("a content change behind an indirect multi-digit /Length changes the fingerprint", () => {
  const original = pdf("before.pdf", ordinance);
  const amended = pdf("after.pdf", ordinance.replace("22 months", "23 months"));
  assert.notEqual(fingerprint(amended), fingerprint(original));
});

test("a truncated download fails instead of hanging or passing", () => {
  const truncated = pdf("truncated.pdf", ordinance, { truncateTo: 110 });
  assert.throws(() => fingerprint(truncated));
});
