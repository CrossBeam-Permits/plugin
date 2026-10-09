#!/usr/bin/env node

import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import { inflateSync } from "node:zlib";
import path from "node:path";
import process from "node:process";

const repoRoot = path.resolve(import.meta.dirname, "..");
const receiptPath = path.join(repoRoot, "data", "laguna-law-sources.json");
const verifyRemote = process.argv.includes("--verify-remote");
const enforceReviewWindow = process.argv.includes("--enforce-review-window");

function fail(message) {
  throw new Error(message);
}

// eCode360 re-generates its ordinance PDFs from time to time (new PDF ModDate,
// document ID and cross-reference table) without changing the ordinance. A
// byte hash alone then reports drift every week. This fingerprint hashes every
// decoded page-content and image stream, sorted, and skips only the streams that
// carry file bookkeeping: XRef, ObjStm and XMP Metadata. Any change to the text
// layer or the scanned page images changes it. Mechanical parsing only.
export function pdfContentStreamsSha256(bytes) {
  const text = bytes.toString("latin1");
  const hashes = [];
  const keyword = /stream\r?\n/g;
  let match;
  while ((match = keyword.exec(text))) {
    let close = match.index - 1;
    while (close >= 0 && /\s/.test(text[close])) close -= 1;
    if (text.slice(close - 1, close + 1) !== ">>") continue; // "endstream" or prose, not a stream start
    let depth = 0;
    let open = -1;
    for (let i = close - 1; i > 0; i -= 1) {
      const pair = text.slice(i - 1, i + 1);
      if (pair === ">>") {
        depth += 1;
        i -= 1;
      } else if (pair === "<<") {
        if (depth === 0) {
          open = i - 1;
          break;
        }
        depth -= 1;
        i -= 1;
      }
    }
    if (open < 0) continue;
    const dictionary = text.slice(open, close + 1);
    const start = match.index + match[0].length;
    const length = dictionary.match(/\/Length\s+(\d+)(?!\s+\d+\s+R)/);
    let end = length ? start + Number(length[1]) : text.indexOf("endstream", start);
    if (!length) while (end > start && (bytes[end - 1] === 0x0a || bytes[end - 1] === 0x0d)) end -= 1;
    keyword.lastIndex = end;
    const type = (dictionary.match(/\/Type\s*\/(\w+)/) || [])[1];
    if (["XRef", "ObjStm", "Metadata"].includes(type)) continue;
    let data = bytes.subarray(start, end);
    if (/\/FlateDecode/.test(dictionary)) {
      try {
        data = inflateSync(data);
      } catch {
        // Keep the raw bytes; the fingerprint is still deterministic.
      }
    }
    hashes.push(createHash("sha256").update(data).digest("hex"));
  }
  if (hashes.length === 0) fail("no PDF content streams found");
  hashes.sort();
  return createHash("sha256").update(hashes.join("\n")).digest("hex");
}

if (process.argv.includes("--fingerprint")) {
  const file = process.argv[process.argv.indexOf("--fingerprint") + 1];
  const bytes = await readFile(file);
  process.stdout.write(
    `${JSON.stringify({ bytes: bytes.length, sha256: createHash("sha256").update(bytes).digest("hex"), contentStreamsSha256: pdfContentStreamsSha256(bytes) })}\n`,
  );
  process.exit(0);
}

const receipt = JSON.parse(await readFile(receiptPath, "utf8"));

if (receipt.schemaVersion !== "1.0") fail("unsupported law-source receipt version");
if (!Array.isArray(receipt.sources) || receipt.sources.length !== 3) {
  fail("expected the three operative Laguna ordinance receipts");
}

for (const check of receipt.contentChecks ?? []) {
  const text = await readFile(path.join(repoRoot, check.path), "utf8");
  for (const marker of check.contains ?? []) {
    if (!text.includes(marker)) fail(`${check.path}: missing required law marker: ${marker}`);
  }
}

if (verifyRemote) {
  for (const source of receipt.sources) {
    const response = await fetch(source.url, { redirect: "follow" });
    if (!response.ok) fail(`${source.id}: official PDF returned HTTP ${response.status}`);
    const bytes = Buffer.from(await response.arrayBuffer());
    const digest = createHash("sha256").update(bytes).digest("hex");
    if (!/^[a-f0-9]{64}$/.test(source.contentStreamsSha256 ?? "")) {
      fail(`${source.id}: receipt has no contentStreamsSha256`);
    }
    if (bytes.length === source.bytes && digest === source.sha256) continue;
    const content = pdfContentStreamsSha256(bytes);
    if (content !== source.contentStreamsSha256) {
      fail(
        `${source.id}: official PDF changed: byte count ${bytes.length} (receipt ${source.bytes}), ` +
          `SHA-256 ${digest.slice(0, 12)}, and its content streams differ. Read the new PDF, review the law, then re-receipt it.`,
      );
    }
    process.stdout.write(
      `NOTICE ${source.id}: PDF re-issued (${bytes.length} bytes, SHA-256 ${digest.slice(0, 12)}; receipt ` +
        `${source.bytes} bytes). Every page-content and image stream is identical, so the ordinance is unchanged. ` +
        "Re-receipt bytes and sha256 when convenient.\n",
    );
  }
}

if (enforceReviewWindow) {
  const today = new Date().toISOString().slice(0, 10);
  if (today > receipt.nextReviewOn) {
    fail(
      `semantic law review overdue after ${receipt.nextReviewOn}; refresh the current eCode pages ` +
        "with a visible browser or Parallel AI, update lawAsOf/nextReviewOn, and review the skill diff",
    );
  }
}

process.stdout.write(
  `Laguna law sources verified as of ${receipt.lawAsOf}` +
    `${verifyRemote ? "; official ordinance PDFs match their receipts" : ""}.\n`,
);
