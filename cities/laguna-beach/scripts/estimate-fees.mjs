#!/usr/bin/env node
/**
 * Estimate Laguna Beach permit fees. Every result is an ESTIMATE.
 *
 * This command does no fee math of its own. It loads the City fee schedule
 * (requirements/fees/fee-schedule.json) and runs the shared calculator
 * (scripts/fees/fee-calc.mjs, `calcFees`). Both files are generated from the
 * maintained source; do not edit them here.
 *
 * The agent decides the inputs from the project documents. A value the
 * documents do not give stays out of the input; never guess one.
 *
 * Usage (Node 18 or later, no packages):
 *
 *   node scripts/estimate-fees.mjs --input project.json
 *   node scripts/estimate-fees.mjs --input '{"permitType":"adu","valuation":180000,"aduSqft":600}'
 *   node scripts/estimate-fees.mjs --input - < project.json
 *   node scripts/estimate-fees.mjs --input project.json --json permit-work/fees/estimate.json
 *   node scripts/estimate-fees.mjs --list
 *
 * Input: one JSON object with the calcFees fields (scripts/fees/README.md has
 * the table):
 *
 *   {
 *     "permitType": "adu",                 // required; --list prints the types
 *     "valuation": 180000,                 // dollars
 *     "newFloorAreaSqft": 600,
 *     "aduSqft": 600,
 *     "primaryDwellingSqft": 1800,
 *     "newDwellingUnits": 1,
 *     "occupancy": "R-3",                  // R-3, R-2, U or B
 *     "isCombinationPermit": true,
 *     "permitCount": 1,
 *     "structureUse": "residential",       // or "nonresidential"
 *     "stories": 1,
 *     "scopes": ["geotechnical_peer_review"],
 *     "scopeQuantities": { "electrical_outlets": 12 },
 *     "conditions": ["utility:laguna_main_sewer"],
 *     "resolvedConditionGroups": ["laguna_main_sewer"],
 *     "existingHabitableConversion": false,
 *     "planningFeeIds": ["design_review_admin"]   // not a calcFees field: Planning rows to list as published
 *   }
 *
 * The command rejects ids the schedule does not define, so a typo cannot drop
 * a fee silently.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { calcFees, validateFeeSchedule } from './fees/fee-calc.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const DEFAULT_SCHEDULE = path.join(ROOT, 'requirements', 'fees', 'fee-schedule.json');

const INPUT_FIELDS = {
  permitType: 'string',
  valuation: 'number',
  newFloorAreaSqft: 'number',
  newDwellingUnits: 'number',
  occupancy: 'string',
  isCombinationPermit: 'boolean',
  aduSqft: 'number',
  primaryDwellingSqft: 'number',
  permitCount: 'number',
  structureUse: 'string',
  stories: 'number',
  scopes: 'array',
  scopeQuantities: 'object',
  conditions: 'array',
  resolvedConditionGroups: 'array',
  existingHabitableConversion: 'boolean',
  planningFeeIds: 'array',
};

const DUE = {
  application: 'At application',
  issuance: 'At permit issuance',
  certificate_of_occupancy: 'At final / certificate of occupancy',
};

class UsageError extends Error {}

// ─────────────────────────── loading ───────────────────────────

export function loadSchedule(file = DEFAULT_SCHEDULE) {
  const schedule = JSON.parse(fs.readFileSync(file, 'utf8'));
  if (!String(schedule.estimate_notice ?? '').includes('ESTIMATE')) {
    throw new UsageError(`${file} has no ESTIMATE notice; refusing to estimate from it`);
  }
  return validateFeeSchedule(schedule);
}

/** Every id the schedule defines, so the input can be checked for typos. */
export function scheduleIds(schedule) {
  const quantities = new Set();
  const scopes = new Set();
  const conditions = new Set();
  const groups = new Set();
  const addCondition = (spec) => {
    if (spec?.condition) conditions.add(spec.condition);
    if (spec?.condition_group) groups.add(spec.condition_group);
  };
  for (const addon of schedule.scope_addons ?? []) {
    scopes.add(addon.trigger_scope);
    for (const key of ['input', 'first_input', 'second_input', 'primary_input']) if (addon.rule?.[key]) quantities.add(addon.rule[key]);
    addCondition(addon);
  }
  for (const deposit of [...(schedule.building?.deposit ?? []), ...(schedule.public_works?.deposit ?? [])]) scopes.add(deposit.trigger_scope);
  for (const route of schedule.fee_review_triggers ?? []) for (const scope of route.trigger_scopes ?? []) scopes.add(scope);
  for (const ask of schedule.open_asks ?? []) for (const scope of ask.trigger_scopes ?? []) scopes.add(scope);
  for (const group of schedule.fee_capture?.groups ?? []) {
    for (const entry of group.inputs ?? []) quantities.add(typeof entry === 'string' ? entry : entry?.id);
  }
  addCondition(schedule.sewer_connection);
  for (const spec of schedule.site_fact_conditions ?? []) addCondition(spec);
  for (const lookup of schedule.external_lookups ?? []) {
    groups.add(lookup.condition_group);
    for (const match of lookup.matches ?? []) conditions.add(match.condition);
  }
  const planning = new Map();
  for (const [kind, rows] of Object.entries({
    flat: schedule.planning?.flat,
    deposit: schedule.planning?.deposit,
    variable: schedule.planning?.variable,
    not_in_schedule: schedule.planning?.known_gaps,
  })) {
    for (const row of rows ?? []) planning.set(row.id, { ...row, listKind: kind });
  }
  quantities.delete(undefined);
  scopes.delete(undefined);
  return { quantities, scopes, conditions, groups, planning, permitTypes: new Set(Object.keys(schedule.permit_types ?? {})) };
}

export function parseInput(text) {
  let input;
  try {
    input = JSON.parse(text);
  } catch (error) {
    throw new UsageError(`input is not valid JSON: ${error.message}`);
  }
  if (!input || typeof input !== 'object' || Array.isArray(input)) throw new UsageError('input must be one JSON object');
  return input;
}

export function checkInput(input, ids) {
  for (const [key, value] of Object.entries(input)) {
    const type = INPUT_FIELDS[key];
    if (!type) throw new UsageError(`unknown input field: ${key} (see scripts/fees/README.md)`);
    if (value === null) continue;
    const actual = Array.isArray(value) ? 'array' : typeof value;
    if (actual !== type) throw new UsageError(`${key} must be ${type === 'array' ? 'an array' : `a ${type}`}`);
  }
  if (typeof input.permitType !== 'string' || !input.permitType.trim()) throw new UsageError('permitType is required (see --list)');
  const unknown = (label, values, known) => {
    const bad = values.filter((value) => !known.has(value));
    if (bad.length) throw new UsageError(`unknown ${label}: ${bad.join(', ')} (see --list)`);
  };
  unknown('scope', input.scopes ?? [], ids.scopes);
  unknown('fee quantity id', Object.keys(input.scopeQuantities ?? {}), ids.quantities);
  unknown('condition', input.conditions ?? [], ids.conditions);
  unknown('condition group', input.resolvedConditionGroups ?? [], ids.groups);
  unknown('Planning fee id', input.planningFeeIds ?? [], new Set(ids.planning.keys()));
  for (const [id, quantity] of Object.entries(input.scopeQuantities ?? {})) {
    if (typeof quantity !== 'number' || !Number.isFinite(quantity) || quantity < 0) throw new UsageError(`scopeQuantities.${id} must be a number of 0 or more`);
  }
}

// ─────────────────────────── estimate ───────────────────────────

function planningRow(row) {
  if (row.listKind === 'not_in_schedule') return null;
  if (row.listKind === 'flat') return { amount: row.amount, basis: 'flat fee' };
  if (row.listKind === 'deposit') return { amount: row.min ?? null, basis: 'minimum deposit; actual cost billed' };
  if (row.kind === 'base_plus_actual_cost') return { amount: row.base, basis: 'base; actual consultant cost billed on top' };
  if (row.kind === 'base_plus_per_unit') return { amount: row.base, basis: `base plus ${money(row.per_unit)} per ${row.unit_label}` };
  if (row.kind === 'percent_of_base') return { amount: null, basis: `${+(row.pct * 100).toFixed(2)}% of ${row.of.join(' and ')}` };
  return { amount: null, basis: row.note ?? 'Confirm with Planning.' };
}

/** Run calcFees and attach the published Planning rows the caller named. */
export function estimate(schedule, input) {
  const ids = scheduleIds(schedule);
  checkInput(input, ids);
  const { planningFeeIds = [], ...calcInput } = input;
  const breakdown = calcFees(schedule, calcInput);
  const planning = { listed: [], notInSchedule: [] };
  for (const id of planningFeeIds) {
    const row = ids.planning.get(id);
    const priced = planningRow(row);
    if (priced) planning.listed.push({ id, label: row.label, amount: priced.amount, basis: priced.basis, cite: row.cite ?? null });
    else planning.notInSchedule.push({ id, label: row.label, note: row.note ?? null, cite: row.cite ?? null });
  }
  const notes = [];
  if (!ids.permitTypes.has(breakdown.permitType)) {
    notes.push(`Permit type "${breakdown.permitType}" is not listed in the schedule, so the calculator uses its defaults for it. Confirm the permit type with the City.`);
  }
  return {
    estimate_notice: schedule.estimate_notice,
    source: { title: schedule.source?.resolution ?? null, url: schedule.source?.url ?? null, effective_from: schedule.effective_from, effective_to: schedule.effective_to ?? null },
    input,
    notes,
    breakdown,
    planning,
  };
}

// ─────────────────────────── rendering ───────────────────────────

function money(value) {
  return `$${Number(value).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
}

function cell(text) {
  return String(text ?? '').replace(/\|/g, '\\|').replace(/\s+/g, ' ').trim();
}

function feeTable(lines, { paidTo }) {
  const out = paidTo
    ? ['| Fee | Paid to | When | Estimate | Source |', '|---|---|---|---:|---|']
    : ['| Fee | When | Estimate | Source |', '|---|---|---:|---|'];
  for (const line of lines) {
    const tail = line.tag === 'exempt' ? ' (exempt by law)' : line.refundable ? ' (refundable deposit)' : '';
    const cells = [cell(line.label + tail)];
    if (paidTo) cells.push(cell(line.ownerDivision ?? 'Not stated'));
    cells.push(DUE[line.dueAt] ?? line.dueAt, money(line.amount), cell(line.cite));
    out.push(`| ${cells.join(' | ')} |`);
  }
  return out;
}

function needsList(lines) {
  return lines.map((line) => {
    const deposit = typeof line.minDeposit === 'number' ? ` From a ${money(line.minDeposit)} deposit.` : '';
    const who = line.ownerDivision ? ` (${line.ownerDivision})` : '';
    return `- ${line.label}${who}: ${line.note}${deposit}${line.cite ? ` [${line.cite}]` : ''}`;
  });
}

export function render(result) {
  const b = result.breakdown;
  const notice = `**${result.estimate_notice}**`;
  const valuation = b.valuationSource === 'none'
    ? 'no valuation given'
    : `valuation ${money(b.valuation)} (${{ applicant: 'from the applicant', derived: 'estimated from floor area', icc_floor: 'ICC minimum' }[b.valuationSource] ?? b.valuationSource})`;
  const out = [notice, '', `Laguna Beach fee estimate: permit type \`${b.permitType}\`, ${valuation}.`];
  if (b.valuationBasisNote) out.push('', b.valuationBasisNote);
  for (const note of result.notes) out.push('', note);

  out.push('', '### Building Division', '');
  if (b.buildingFirmLines.length) {
    out.push(...feeTable(b.buildingFirmLines, { paidTo: false }));
    out.push(`| **Building Division subtotal** | | **${money(b.buildingSubtotal)}** | |`);
  } else {
    out.push('No Building Division fee could be computed from this input.');
  }

  if (b.otherAgencyLines.length) {
    out.push('', '### Other City divisions and other agencies (not in the Building subtotal)', '');
    out.push(...feeTable(b.otherAgencyLines, { paidTo: true }));
    out.push(`| **Other divisions and agencies subtotal** | | | **${money(b.otherAgencySubtotal)}** | |`);
  }

  const needs = [...b.buildingNeedsDetails, ...b.otherAgencyNeedsDetails];
  if (needs.length || result.planning.notInSchedule.length) {
    out.push('', '### Not estimated: needs project details or a City decision', '');
    out.push(...needsList(needs));
    for (const row of result.planning.notInSchedule) out.push(`- ${row.label} (Planning): ${row.note ?? 'Not in the adopted schedule; confirm with Planning.'}`);
  }

  if (result.planning.listed.length) {
    out.push('', '### Planning fees, as published (only if the City routes the project to them; not in any subtotal)', '');
    out.push('| Fee | Amount | Basis | Source |', '|---|---:|---|---|');
    for (const row of result.planning.listed) {
      out.push(`| ${cell(row.label)} | ${row.amount === null ? 'see basis' : money(row.amount)} | ${cell(row.basis)} | ${cell(row.cite)} |`);
    }
  }

  if (b.openAsks.length) {
    out.push('', '### Open questions to the City (not estimated)', '');
    for (const ask of b.openAsks) out.push(`- ${ask.question}`);
  }
  if (b.excludedFees.length) {
    out.push('', '### Billed outside the permit', '');
    for (const fee of b.excludedFees) out.push(`- ${fee.label}: ${fee.reason}${fee.billed_by ? ` Billed by ${fee.billed_by}.` : ''}`);
  }

  const source = result.source;
  out.push(
    '',
    `Source: ${source.title ?? 'City of Laguna Beach Master Fee Schedule'}, effective ${source.effective_from}${source.effective_to ? ` through ${source.effective_to}` : ''}.${source.url ? ` ${source.url}` : ''}`,
    'Keep the Building subtotal and the other-agency subtotal separate. Never add a number for an item that is not estimated.',
    '',
    notice,
  );
  return out.join('\n');
}

export function listIds(schedule) {
  const ids = scheduleIds(schedule);
  const sorted = (set) => [...set].sort();
  const out = [schedule.estimate_notice, '', 'Permit types (permitType):', ...sorted(ids.permitTypes).map((id) => `  ${id}`)];
  out.push('', 'Fee scopes (scopes):', ...sorted(ids.scopes).map((id) => `  ${id}`));
  const labels = new Map((schedule.scope_addons ?? []).map((addon) => [addon.rule?.input, addon.label]));
  out.push('', 'Unit-row quantities (scopeQuantities):', ...sorted(ids.quantities).map((id) => `  ${id}${labels.get(id) ? `: ${labels.get(id)}` : ''}`));
  out.push('', 'Conditions (conditions):', ...sorted(ids.conditions).map((id) => `  ${id}`));
  out.push('', 'Condition groups (resolvedConditionGroups):', ...sorted(ids.groups).map((id) => `  ${id}`));
  out.push('', 'Planning fee ids (planningFeeIds):', ...[...ids.planning.values()].map((row) => `  ${row.id}: ${row.label}`));
  return out.join('\n');
}

// ─────────────────────────── command line ───────────────────────────

function readInputArg(value) {
  if (value === '-') return fs.readFileSync(0, 'utf8');
  if (value.trim().startsWith('{')) return value;
  return fs.readFileSync(value, 'utf8');
}

export function main(argv = process.argv.slice(2), io = { stdout: process.stdout, stderr: process.stderr }) {
  const args = { list: false, input: null, json: null, schedule: DEFAULT_SCHEDULE };
  try {
    for (let index = 0; index < argv.length; index++) {
      const flag = argv[index];
      const next = () => {
        const value = argv[++index];
        if (value === undefined) throw new UsageError(`${flag} needs a value`);
        return value;
      };
      if (flag === '--list') args.list = true;
      else if (flag === '--input') args.input = next();
      else if (flag === '--json') args.json = next();
      else if (flag === '--schedule') args.schedule = next();
      else if (flag === '--help' || flag === '-h') {
        io.stdout.write('usage: estimate-fees.mjs --input <file | JSON | -> [--json out.json] | --list\n');
        return 0;
      } else throw new UsageError(`unknown option: ${flag}`);
    }
    const schedule = loadSchedule(args.schedule);
    if (args.list) {
      io.stdout.write(`${listIds(schedule)}\n`);
      return 0;
    }
    if (!args.input) throw new UsageError('give --input <file | JSON | -> or --list');
    const result = estimate(schedule, parseInput(readInputArg(args.input)));
    if (args.json) {
      fs.mkdirSync(path.dirname(path.resolve(args.json)), { recursive: true });
      fs.writeFileSync(args.json, `${JSON.stringify(result, null, 2)}\n`);
    }
    io.stdout.write(`${render(result)}\n`);
    return 0;
  } catch (error) {
    if (!(error instanceof UsageError)) throw error;
    io.stderr.write(`estimate-fees: ${error.message}\n`);
    return 2;
  }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  process.exitCode = main();
}
