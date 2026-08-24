#!/usr/bin/env node

import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const repoRoot = path.resolve(import.meta.dirname, "..");
const receiptPath = path.join(repoRoot, "data", "laguna-law-sources.json");
const verifyRemote = process.argv.includes("--verify-remote");
const enforceReviewWindow = process.argv.includes("--enforce-review-window");

function fail(message) {
  throw new Error(message);
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
    if (bytes.length !== source.bytes) {
      fail(`${source.id}: byte count drifted (${bytes.length} != ${source.bytes})`);
    }
    if (digest !== source.sha256) fail(`${source.id}: SHA-256 drifted`);
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
    `${verifyRemote ? "; official ordinance PDF hashes match" : ""}.\n`,
);
