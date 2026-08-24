#!/usr/bin/env node

import { readFile, readdir, writeFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const repoRoot = path.resolve(import.meta.dirname, "..");
const citiesRoot = path.join(repoRoot, "cities");
const overridesPath = path.join(repoRoot, "data", "permit-portals.json");
const checkOnly = process.argv.includes("--check");

const SYSTEM_PATHS = [
  ["permitSystem"],
  ["portalSystem"],
  ["portalPlatform"],
  ["permitPortalSystem"],
  ["permitPortalPlatform"],
  ["onlinePermitPlatform"],
  ["portal"],
  ["portalName"],
  ["buildingDepartment", "portalName"],
  ["buildingDepartment", "portal"],
  ["buildingDept", "portalSystem"],
  ["buildingDept", "portalPlatform"],
  ["buildingDept", "portalName"],
  ["buildingDept", "portal"],
];

const URL_PATHS = [
  ["portalUrl"],
  ["permitPortalUrl"],
  ["onlinePermitUrl"],
  ["buildingPortalUrl"],
  ["permitPortal"],
  ["onlinePermitPortal"],
  ["portal"],
  ["buildingDepartment", "portal"],
  ["buildingDept", "portalUrl"],
  ["buildingDept", "portal"],
];

const UNKNOWN_VALUES = new Set(["", "unknown", "not confirmed", "n/a", "none"]);

function valueAt(object, keys) {
  let value = object;
  for (const key of keys) {
    if (value === null || typeof value !== "object" || Array.isArray(value)) return null;
    value = value[key];
  }
  if (typeof value !== "string") return null;
  const trimmed = value.trim();
  const lower = trimmed.toLowerCase();
  return UNKNOWN_VALUES.has(lower) || lower.startsWith("none ") || lower.startsWith("unknown") || lower.startsWith("unconfirmed")
    ? null
    : trimmed;
}

function normalizePermitSystem(value) {
  if (value === null) return null;
  try {
    const parsed = new URL(value);
    if (["http:", "https:", "mailto:"].includes(parsed.protocol)) return null;
  } catch {
    // A permit-system name is expected to be plain text, not a URL.
  }
  return value;
}

function normalizePortalUrl(value) {
  if (value === null) return null;
  try {
    const parsed = new URL(value);
    return ["http:", "https:"].includes(parsed.protocol) ? parsed.href : null;
  } catch {
    return null;
  }
}

function firstExactValue(object, paths, normalize) {
  for (const keys of paths) {
    const value = normalize(valueAt(object, keys));
    if (value !== null) return value;
  }
  return null;
}

function renderCell(value) {
  return value === null
    ? "Not confirmed — verify with City"
    : value.replaceAll("|", "\\|").replaceAll("\n", " ");
}

function updateCityInfo(markdown, permitSystem, portalUrl, skillPath) {
  const heading = "## City Info\n";
  const headingIndex = markdown.indexOf(heading);
  if (headingIndex === -1) throw new Error(`${skillPath}: missing City Info heading`);

  const sectionStart = headingIndex + heading.length;
  const sectionEnd = markdown.indexOf("\n---\n", sectionStart);
  if (sectionEnd === -1) throw new Error(`${skillPath}: missing City Info section boundary`);

  const section = markdown.slice(sectionStart, sectionEnd);
  const lines = section.split("\n");
  const dividerIndex = lines.findIndex(
    (line) => line.includes("-") && /^\|[-:| ]+\|$/.test(line),
  );
  if (dividerIndex === -1) throw new Error(`${skillPath}: missing City Info table divider`);

  const retained = lines.filter(
    (line) => !/^\|\s*Permit (?:portal|system)\s*\|/i.test(line),
  );
  const retainedDividerIndex = retained.findIndex(
    (line) => line.includes("-") && /^\|[-:| ]+\|$/.test(line),
  );
  retained.splice(
    retainedDividerIndex + 1,
    0,
    `| Permit system | ${renderCell(permitSystem)} |`,
    `| Permit portal | ${renderCell(portalUrl)} |`,
  );

  return `${markdown.slice(0, sectionStart)}${retained.join("\n")}${markdown.slice(sectionEnd)}`;
}

async function main() {
  const overridesDocument = JSON.parse(await readFile(overridesPath, "utf8"));
  const overrides = overridesDocument.cities ?? {};
  const citySlugs = (await readdir(citiesRoot, { withFileTypes: true }))
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .sort();

  let skillCount = 0;
  let knownSystemCount = 0;
  let knownUrlCount = 0;
  let staleFileCount = 0;

  for (const slug of citySlugs) {
    const cityRoot = path.join(citiesRoot, slug);
    const metaPath = path.join(cityRoot, "meta.json");
    const meta = JSON.parse(await readFile(metaPath, "utf8"));
    const override = overrides[slug] ?? {};
    const permitSystem = normalizePermitSystem(override.permitSystem ?? null) ??
      firstExactValue(meta, SYSTEM_PATHS, normalizePermitSystem);
    const portalUrl = normalizePortalUrl(override.portalUrl ?? null) ??
      firstExactValue(meta, URL_PATHS, normalizePortalUrl);

    meta.permitSystem = permitSystem;
    meta.portalUrl = portalUrl;
    const originalMetaText = await readFile(metaPath, "utf8");
    const updatedMetaText = `${JSON.stringify(meta, null, 2)}\n`;
    if (updatedMetaText !== originalMetaText) {
      staleFileCount += 1;
      if (!checkOnly) await writeFile(metaPath, updatedMetaText);
    }

    if (permitSystem !== null) knownSystemCount += 1;
    if (portalUrl !== null) knownUrlCount += 1;

    const skillsRoot = path.join(cityRoot, "skills");
    const permitTypes = (await readdir(skillsRoot, { withFileTypes: true }))
      .filter((entry) => entry.isDirectory())
      .map((entry) => entry.name)
      .sort();

    for (const permitType of permitTypes) {
      const skillPath = path.join(skillsRoot, permitType, "SKILL.md");
      const original = await readFile(skillPath, "utf8");
      const portalNeutral = original
        .replaceAll("Accela-ready", "portal-ready")
        .replaceAll("city-portal-ready", "portal-ready")
        .replaceAll("an portal-ready", "a portal-ready");
      const updated = updateCityInfo(portalNeutral, permitSystem, portalUrl, skillPath);
      if (updated !== original) {
        staleFileCount += 1;
        if (!checkOnly) await writeFile(skillPath, updated);
      }
      skillCount += 1;
    }
  }

  process.stdout.write(
    `${checkOnly ? "Checked" : "Updated"} ${citySlugs.length} city metadata files and ${skillCount} skills; ` +
      `${knownSystemCount} systems and ${knownUrlCount} URLs are confirmed.\n`,
  );
  if (checkOnly && staleFileCount > 0) {
    throw new Error(`${staleFileCount} generated portal metadata files are stale`);
  }
}

await main();
