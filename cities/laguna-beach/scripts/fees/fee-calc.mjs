// GENERATED FILE. Do not edit by hand; the plugin publisher overwrites it.
// A copy of the shared CrossBeam fee calculator. The code is unchanged; only internal
// comments are replaced. scripts/estimate-fees.mjs runs it over requirements/fees/fee-schedule.json.
/**
 * CrossBeam permit-fee calculator: pure math, no I/O. Every city runs the same engine
 * over its own fee-schedule data.
 */

// ── Cities with an authored fee schedule ──
export const FEE_CITIES = ['laguna-beach', 'buena-park', 'newport-beach', 'costa-mesa', 'anaheim', 'los-altos-hills', 'stanislaus-county', 'denver', 'corona'];

// ── ICC Building Valuation Data anchors (Feb 2026, Type V-B / typical wood frame) ──
// $/sqft by occupancy. Used to DERIVE a valuation when the applicant gives only
// square footage. Persist the edition so an estimate is reproducible.
export const ICC_BVD_EDITION = 'ICC BVD February 2026 (Type V-B)';
const ICC_BVD_PER_SQFT = {
  'R-3': 175.92, // one/two-family dwellings
  'R-2': 158.18, // multifamily
  U: 71.07, // private garages / utility
  B: 213.27, // business
};

export const FEE_DUE_AT = ['application', 'issuance', 'certificate_of_occupancy'];

/**
 * The FeeInputs a schedule's `fee_capture` block may name directly, beside the
 * quantities its own fee lines consume. Keyed by capture id.
 */
export const FEE_CAPTURE_BUILT_INS = {
  valuation: { field: 'valuation', kind: 'number', label: 'Project valuation', unit: 'USD' },
  new_floor_area_sqft: { field: 'newFloorAreaSqft', kind: 'number', label: 'New floor area', unit: 'sq ft' },
  adu_sqft: { field: 'aduSqft', kind: 'number', label: 'ADU floor area', unit: 'sq ft' },
  primary_dwelling_sqft: { field: 'primaryDwellingSqft', kind: 'number', label: 'Primary dwelling floor area', unit: 'sq ft' },
  new_dwelling_units: { field: 'newDwellingUnits', kind: 'number', label: 'New dwelling units', unit: 'units' },
  stories: { field: 'stories', kind: 'number', label: 'Stories of the building after the work (area table, elevations or sections)', unit: 'stories' },
  structure_use: { field: 'structureUse', kind: 'choice', label: 'Residential or nonresidential (occupancy group)', choices: ['residential', 'nonresidential'] },
  existing_habitable_conversion: { field: 'existingHabitableConversion', kind: 'boolean', label: 'Converts existing habitable space' },
  is_combination_permit: { field: 'isCombinationPermit', kind: 'boolean', label: 'Combination M/E/P permit' },
};

/** A `fee_capture` group input entry is an id, or `{ id, label?, unit? }`. */
export function feeCaptureInputId(entry) {
  return typeof entry === 'string' ? entry : entry?.id;
}

// ─────────────────────────── primitives ───────────────────────────

/** Flat fee for the valuation band containing `valuation` (Laguna shape). */
export function flatBand(valuation, bands) {
  for (const band of bands) {
    if (band.up_to === null || valuation <= band.up_to) return band.fee;
  }
  return bands.length ? bands[bands.length - 1].fee : 0;
}

/**
 * base + marginal-per-unit over the bracket floor.
 *
 * `options.increment`: 'fraction_up' (default) charges each started unit in
 * full ("or fraction thereof" = ceil); 'prorated' charges the exact fraction.
 * `options.rounding`: 'half_up' (default) or 'half_even' for a schedule whose
 * collecting system rounds half-cents to even.
 */
export function steppedSchedule(valuation, brackets, options = {}) {
  const prorated = options.increment === 'prorated';
  const money = options.rounding === 'half_even' ? round2HalfEven : round2;
  const charge = (b) => {
    if (b.per === 0 || b.unit === 0) return b.base;
    const over = Math.max(0, valuation - b.floor) / b.unit;
    return money(b.base + (prorated ? over : Math.ceil(over)) * b.per);
  };
  for (const b of brackets) {
    const inBracket = b.up_to === null ? valuation > b.floor : valuation > b.floor && valuation <= b.up_to;
    // The first (minimum-fee) bracket has floor 0 and per 0; catch <= floor too.
    if (inBracket || (b.floor === 0 && valuation <= (b.up_to ?? Infinity))) return charge(b);
  }
  const top = brackets[brackets.length - 1];
  return top ? charge(top) : 0;
}

/**
 * Area-table variant whose published bracket floors are inclusive base points.
 * For example, an "at 1,001 sq ft" row charges its base at exactly 1,001 and
 * begins the per-unit increment above 1,001.
 */
export function areaSteppedSchedule(areaSqft, brackets) {
  for (const b of brackets) {
    const inBracket = areaSqft >= b.floor && (b.up_to === null || areaSqft <= b.up_to);
    if (inBracket) {
      if (b.per === 0 || b.unit === 0) return b.base;
      const over = Math.max(0, areaSqft - b.floor);
      return round2(b.base + Math.ceil(over / b.unit) * b.per);
    }
  }
  return 0;
}

/**
 * Select the floor-AREA band for a project-type table. Unlike
 * flatBand/steppedSchedule (keyed on valuation), this keys on square footage.
 */
export function areaBand(areaSqft, bands) {
  if (!bands?.length) return null;
  for (const band of bands) {
    if (band.up_to_sqft === null || band.up_to_sqft === undefined || areaSqft <= band.up_to_sqft) return band;
  }
  return bands[bands.length - 1];
}

/**
 * Resolve a fee from an area band. Flat bands return their published amount;
 * incremental bands charge the base plus one increment for each additional
 * 100 sq ft or fraction thereof. A `from_sqft` of 501 means the base covers
 * the first 500 sq ft, so 501 sq ft charges one increment.
 */
export function areaBandFee(areaSqft, bands) {
  const band = areaBand(areaSqft, bands);
  if (!band) return 0;
  if (typeof band.flat === 'number') return band.flat;
  if (typeof band.base === 'number' && typeof band.per_100sqft === 'number') {
    const coveredThrough = (band.from_sqft ?? 1) - 1;
    const additionalArea = Math.max(0, areaSqft - coveredThrough);
    return round2(band.base + Math.ceil(additionalArea / 100) * band.per_100sqft);
  }
  return 0;
}

export function buildingPermitFee(valuation, b) {
  // area_band cities (e.g. Newport) keep a valuation_fallback for the work that
  // IS valuation-based (non-residential / multifamily 3+ / residential alterations).
  if (b.method === 'area_band' && b.valuation_fallback) return buildingPermitFee(valuation, b.valuation_fallback);
  if (b.method === 'stepped' && b.brackets?.length)
    return steppedSchedule(valuation, b.brackets, { increment: b.increment, rounding: b.rounding });
  if (b.bands?.length) return flatBand(valuation, b.bands);
  return 0;
}

/** Derive a valuation from floor area × ICC BVD when none was stated. */
export function valuationFromArea(areaSqft, occupancy = 'R-3') {
  const rate = ICC_BVD_PER_SQFT[occupancy] ?? ICC_BVD_PER_SQFT['R-3'];
  return { valuation: round2(areaSqft * rate), rate };
}

/** SMIP (CGS): schedule may override the published residential rate; $0.50 min. */
export function smip(valuation, residentialLowRise = true, residentialRate = 0.00013, otherRate = 0.00028) {
  return round2(Math.max(0.5, valuation * (residentialLowRise ? residentialRate : otherRate)));
}

/** BSASRF / SB 1473: $1 per $25,000 of valuation, $1 min. */
export function bsasrf(valuation) {
  return Math.max(1, Math.ceil(valuation / 25000));
}

/** ADU impact-fee exemption: <=750 sqft → $0; >750 → proportional to primary. */
export function aduImpactFee(aduSqft, primarySqft) {
  if (aduSqft <= 750) {
    return {
      amount: 0,
      note: 'ADU 750 sq ft or smaller — exempt from all impact fees (Gov. Code §66311.5). The school fee still applies if ≥500 sq ft.',
    };
  }
  if (primarySqft && primarySqft > 0) {
    const ratio = aduSqft / primarySqft;
    return {
      amount: 0,
      note: `ADU over 750 sq ft — impact fees are charged proportionally (~${(ratio * 100).toFixed(0)}% of the primary dwelling's, ${aduSqft}/${primarySqft} sq ft). Exact amounts confirmed by the city/districts at intake.`,
    };
  }
  return {
    amount: 0,
    note: 'ADU over 750 sq ft — impact fees apply proportionally to the primary dwelling (Gov. Code §66311.5). Provide the primary dwelling size for an estimate, or confirm with the city.',
  };
}

function round2(n) {
  // Decimal fee rates routinely land a mathematical half-cent just below the
  // binary floating-point boundary (for example 150000 * 0.0001433). Nudge by
  // a magnitude-scaled machine epsilon before rounding so financial half-cents
  // round deterministically instead of producing $21.49 for a $21.495 result.
  const correction = Number.EPSILON * Math.max(1, Math.abs(n));
  return Math.round((n + Math.sign(n || 1) * correction) * 100) / 100;
}

/**
 * Banker's rounding to the cent. A value within float noise of a half-cent goes
 * to the even cent; everything else rounds normally. The noise band is a few
 * hundred ulps of the cent value: a wider band would send a real 0.497-cent
 * remainder to the even cent.
 */
function round2HalfEven(n) {
  const cents = n * 100;
  const floor = Math.floor(cents);
  const fraction = cents - floor;
  if (Math.abs(fraction - 0.5) < Number.EPSILON * 1024 * Math.max(1, Math.abs(cents))) {
    return (floor % 2 === 0 ? floor : floor + 1) / 100;
  }
  return round2(n);
}

function formatDollars(n, { cents = false } = {}) {
  return n.toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: cents ? 2 : 0, maximumFractionDigits: cents ? 2 : 0 });
}

function formatPercent(decimal) {
  const percent = decimal * 100;
  const digits = Number.isInteger(percent) ? 0 : Number.isInteger(percent * 10) ? 1 : 2;
  return percent.toFixed(digits);
}

/** Canonical schedule interval, with legacy field compatibility for older cities. */
export function scheduleEffectiveFrom(schedule) {
  return schedule?.effective_from ?? schedule?.effective_date ?? null;
}

export function scheduleEffectiveTo(schedule) {
  if (Object.prototype.hasOwnProperty.call(schedule ?? {}, 'effective_to')) return schedule.effective_to;
  return null;
}

// ─────────────────────────── schedule validation (pure) ───────────────────────────

/** The optional permit_fee options, each one of its allowed values when set. */
const PERMIT_FEE_OPTIONS = {
  increment: ['fraction_up', 'prorated'],
  rounding: ['half_up', 'half_even'],
  unlisted_permit_types: ['compute', 'confirm_at_intake'],
};

function validatePermitFeeOptions(permitFee) {
  for (const [key, allowed] of Object.entries(PERMIT_FEE_OPTIONS)) {
    if (permitFee[key] !== undefined && !allowed.includes(permitFee[key]))
      throw new Error(`building.permit_fee.${key} must be ${allowed.join(' or ')}`);
  }
}

/** Every fee in the schedule's planning tables, each carrying its kind. */
export function planningFeeRows(schedule) {
  const planning = schedule?.planning ?? {};
  return [
    ...(planning.flat ?? []).map((fee) => ({ ...fee, kind: 'flat' })),
    ...(planning.deposit ?? []).map((fee) => ({ ...fee, kind: 'actual_cost_deposit' })),
    ...(planning.variable ?? []),
    ...(planning.known_gaps ?? []),
  ];
}

/**
 * `fee_capture.planning.decisions`: one decision per fee family a Planning
 * screen settles. Each option is a planning fee id, so the list cannot drift
 * from the rates, and no fee id answers two decisions.
 */
function validatePlanningFeeCapture(obj) {
  const planning = obj.fee_capture?.planning;
  if (planning === undefined) return;
  if (!planning || !Array.isArray(planning.decisions) || !planning.decisions.length)
    throw new Error('fee_capture.planning requires non-empty decisions');
  const known = new Set(planningFeeRows(obj).map((fee) => fee.id));
  const decisionIds = new Set();
  const optionIds = new Set();
  for (const decision of planning.decisions) {
    if (!decision?.id || !decision?.label || !decision?.question || !Array.isArray(decision.options) || !decision.options.length)
      throw new Error('fee_capture.planning.decisions entries require id, label, question, and non-empty options');
    if (decisionIds.has(decision.id)) throw new Error(`fee_capture.planning decision ${decision.id} is listed twice`);
    decisionIds.add(decision.id);
    for (const option of decision.options) {
      if (!known.has(option)) throw new Error(`fee_capture.planning.${decision.id} option ${option} is not a planning fee id`);
      if (optionIds.has(option)) throw new Error(`fee_capture.planning option ${option} answers two decisions`);
      optionIds.add(option);
    }
  }
}

/** Every fee_capture input must feed a fee line or be a built-in FeeInput. */
/** The staff-facing text a lookup may declare: its map name and site-flag chips. */
function validateLookupDisplay(lookup) {
  const flag = lookup.site_flag;
  if (lookup.source_label !== undefined && (typeof lookup.source_label !== 'string' || !lookup.source_label.trim()))
    throw new Error(`external_lookups.${lookup.id}.source_label must be a non-empty string`);
  if (flag !== undefined && (!flag || typeof flag !== 'object' ||
      ['inside', 'outside', 'unknown'].some((key) => typeof flag[key] !== 'string' || !flag[key].trim())))
    throw new Error(`external_lookups.${lookup.id}.site_flag requires inside, outside and unknown labels`);
}

function validateFeeCapture(obj) {
  const capture = obj.fee_capture;
  // A combination permit's replaced groups must name real capture groups: a typo
  // would silently charge the itemized trade rows beside the combination line.
  const replaced = obj.building?.trades_new?.replaces_capture_groups ?? [];
  const groupIds = new Set(Array.isArray(capture?.groups) ? capture.groups.map((group) => group?.id) : []);
  for (const id of replaced) {
    if (!groupIds.has(id)) throw new Error(`building.trades_new.replaces_capture_groups ${id} is not a fee_capture group`);
  }
  if (capture === undefined) return;
  if (!capture) throw new Error('fee_capture must be an object');
  validatePlanningFeeCapture(obj);
  if (capture.groups === undefined && capture.planning) return;
  if (!Array.isArray(capture.groups) || !capture.groups.length)
    throw new Error('fee_capture requires non-empty groups');
  const consumed = new Set(Object.keys(FEE_CAPTURE_BUILT_INS));
  // A separate permit's own valuation prices that permit's record.
  for (const spec of obj.separate_permits ?? []) if (spec?.valuation_input) consumed.add(spec.valuation_input);
  const scopes = new Set();
  for (const addon of obj.scope_addons ?? []) {
    scopes.add(addon.trigger_scope);
    if (addon.rule?.input) consumed.add(addon.rule.input);
    for (const key of ['first_input', 'second_input', 'primary_input']) if (addon.rule?.[key]) consumed.add(addon.rule[key]);
  }
  for (const deposit of [...(obj.building?.deposit ?? []), ...(obj.public_works?.deposit ?? [])]) scopes.add(deposit.trigger_scope);
  for (const route of obj.fee_review_triggers ?? []) for (const scope of route.trigger_scopes ?? []) scopes.add(scope);
  const seen = new Set();
  for (const group of capture.groups) {
    if (!group?.id || !group?.label || !Array.isArray(group.inputs) || !group.inputs.length)
      throw new Error('fee_capture.groups entries require id, label, and non-empty inputs');
    if (group.scope !== undefined && !scopes.has(group.scope))
      throw new Error(`fee_capture.groups.${group.id}.scope ${group.scope} triggers no fee line`);
    for (const entry of group.inputs) {
      const input = feeCaptureInputId(entry);
      if (!input) throw new Error(`fee_capture.groups.${group.id}.inputs entries require an id`);
      if (!consumed.has(input)) throw new Error(`fee_capture input ${input} feeds no fee line`);
      if (seen.has(input)) throw new Error(`fee_capture input ${input} is listed twice`);
      seen.add(input);
    }
  }
  for (const scope of capture.scopes ?? []) {
    if (!scope?.id || !scope?.question) throw new Error('fee_capture.scopes entries require id and question');
    if (!scopes.has(scope.id)) throw new Error(`fee_capture scope ${scope.id} triggers no fee line`);
  }
  const conditionsByGroup = new Map();
  for (const spec of [...(obj.scope_addons ?? []), obj.sewer_connection ?? {}]) {
    if (!spec.condition_group || !spec.condition) continue;
    if (!conditionsByGroup.has(spec.condition_group)) conditionsByGroup.set(spec.condition_group, new Set());
    conditionsByGroup.get(spec.condition_group).add(spec.condition);
  }
  for (const group of capture.conditions ?? []) {
    const known = conditionsByGroup.get(group?.group);
    if (!known || !group.label || !Array.isArray(group.choices) || !group.choices.length)
      throw new Error(`fee_capture.conditions ${group?.group} must name a fee condition group, a label, and choices`);
    for (const choice of group.choices) {
      if (!choice?.label || !known.has(choice.id))
        throw new Error(`fee_capture.conditions.${group.group} choice ${choice?.id} is not a condition of that group`);
    }
  }
}

/** The capture inputs a separate permit takes off the screened record, its valuation included. */
function separatePermitInputs(spec) {
  return [...(spec.inputs ?? []), ...(spec.valuation_input ? [spec.valuation_input] : [])];
}

/**
 * Each separate permit is priced as its own record: a real permit type, scopes
 * that trigger fee lines, capture inputs the schedule asks for, and no scope or
 * input claimed by two permits.
 */
function validateSeparatePermits(obj) {
  if (obj.separate_permits === undefined) return;
  if (!Array.isArray(obj.separate_permits)) throw new Error('separate_permits must be a list');
  const permitTypes = new Set(Object.keys(obj.permit_types ?? {}));
  const triggers = new Set((obj.scope_addons ?? []).map((addon) => addon.trigger_scope));
  // validateFeeCapture runs after this and reports a malformed groups list.
  const groups = Array.isArray(obj.fee_capture?.groups) ? obj.fee_capture.groups : [];
  const captureInputs = new Set(groups.flatMap((group) => (Array.isArray(group?.inputs) ? group.inputs.map(feeCaptureInputId) : [])));
  const ids = new Set();
  const claimed = new Set();
  for (const spec of obj.separate_permits) {
    if (!spec?.id || !spec?.label || !permitTypes.has(spec.permit_type))
      throw new Error(`separate_permits entries require id, label, and a permit_type in permit_types (${spec?.id})`);
    if (ids.has(spec.id)) throw new Error(`separate_permits ${spec.id} is listed twice`);
    ids.add(spec.id);
    for (const type of spec.permit_types ?? []) {
      if (!permitTypes.has(type)) throw new Error(`separate_permits.${spec.id} permit type ${type} is not in permit_types`);
    }
    for (const scope of spec.scopes ?? []) {
      if (!triggers.has(scope)) throw new Error(`separate_permits.${spec.id} scope ${scope} triggers no fee line`);
    }
    const inputs = separatePermitInputs(spec);
    for (const input of inputs) {
      if (!captureInputs.has(input)) throw new Error(`separate_permits.${spec.id} input ${input} is not a fee_capture input`);
    }
    if (!spec.scopes?.length && !inputs.length)
      throw new Error(`separate_permits.${spec.id} needs scopes or inputs that say when it applies`);
    for (const key of [...(spec.scopes ?? []), ...inputs]) {
      if (claimed.has(key)) throw new Error(`separate_permits ${key} is filed under two permits`);
      claimed.add(key);
    }
    if (spec.over !== undefined && (!spec.over?.input || typeof spec.over.value !== 'number'))
      throw new Error(`separate_permits.${spec.id}.over requires an input and a numeric value`);
  }
}

/**
 * Validate + default a fee-schedule OBJECT (parsed from YAML, or read from the
 * store JSONB / a JSON snapshot). Lenient-in, strict-out. Pure — the YAML/JSON
 * I/O that produces `input` stays per-runtime; this shared check guarantees the
 * chatbot, the publish script, and the sandbox tool reject the same bad data.
 */
// Plan review: the building-wide rate, the optional exempt-through valuation, and the optional
// per-permit-type rate. Also checks each permit type's optional display label.
function validatePlanReviewOptions(building, permitTypes) {
  if (typeof building.plan_review_pct !== 'number')
    throw new Error('fee schedule missing building.plan_review_pct');
  if (building.plan_review_exempt_through_valuation !== undefined &&
      typeof building.plan_review_exempt_through_valuation !== 'number')
    throw new Error('building.plan_review_exempt_through_valuation must be numeric');
  for (const [permitType, cfg] of Object.entries(permitTypes ?? {})) {
    if (cfg?.label !== undefined && (typeof cfg.label !== 'string' || !cfg.label.trim()))
      throw new Error(`permit_types.${permitType}.label must be a non-empty string`);
    if (cfg?.plan_review_pct !== undefined && (typeof cfg.plan_review_pct !== 'number' || cfg.plan_review_pct < 0))
      throw new Error(`permit_types.${permitType}.plan_review_pct must be a non-negative number`);
  }
}

export function validateFeeSchedule(input) {
  const obj = input;
  if (!obj || typeof obj !== 'object') throw new Error('fee schedule is not an object');
  if (!obj.city_slug) throw new Error('fee schedule missing city_slug');
  const effectiveFrom = scheduleEffectiveFrom(obj);
  if (!isIsoDate(effectiveFrom))
    throw new Error('fee schedule missing a valid effective_from (or legacy effective_date)');
  if (obj.effective_from !== undefined && obj.effective_date !== undefined && obj.effective_from !== obj.effective_date)
    throw new Error('fee schedule effective_from and legacy effective_date disagree');
  if (obj.effective_to !== undefined && obj.effective_to !== null) {
    if (!isIsoDate(obj.effective_to)) throw new Error('fee schedule effective_to must be null or YYYY-MM-DD');
    if (obj.effective_to < effectiveFrom) throw new Error('fee schedule effective_to precedes effective_from');
  }
  if (!obj.building?.permit_fee) throw new Error('fee schedule missing building.permit_fee');
  const m = obj.building.permit_fee.method;
  if (!['flat_band', 'stepped', 'area_band', 'area_stepped', 'confirm_at_intake'].includes(m))
    throw new Error(`unsupported building.permit_fee.method: ${String(m)}`);
  if (m === 'flat_band' && !obj.building.permit_fee.bands?.length)
    throw new Error('flat_band permit_fee missing bands');
  if (m === 'stepped' && !obj.building.permit_fee.brackets?.length)
    throw new Error('stepped permit_fee missing brackets');
  validatePermitFeeOptions(obj.building.permit_fee);
  for (const band of obj.building.permit_fee.unresolved_bands ?? []) {
    if ((band.from !== undefined && typeof band.from !== 'number') ||
        (band.up_to !== null && typeof band.up_to !== 'number') || !band.note)
      throw new Error('building.permit_fee.unresolved_bands entries require numeric/null bounds and a note');
  }
  if (m === 'area_band') {
    const pf = obj.building.permit_fee;
    if (!pf.area_tables || typeof pf.area_tables !== 'object')
      throw new Error('area_band permit_fee missing area_tables');
    for (const [type, table] of Object.entries(pf.area_tables)) {
      if (Array.isArray(table)) {
        if (table.length === 0)
          throw new Error(`area_band area_tables.${type} must be a non-empty array`);
        for (const [index, band] of table.entries()) {
          if (typeof band?.permit !== 'number')
            throw new Error(`area_band area_tables.${type}[${index}] missing numeric permit`);
          if (band.plan_review !== undefined && typeof band.plan_review !== 'number')
            throw new Error(`area_band area_tables.${type}[${index}].plan_review must be numeric`);
        }
        continue;
      }
      if (!table || typeof table !== 'object')
        throw new Error(`area_band area_tables.${type} must be a legacy band array or fee table`);
      validateAreaFeeBands(table.permit, `area_tables.${type}.permit`);
      if (table.plan_review_building !== undefined)
        validateAreaFeeBands(table.plan_review_building, `area_tables.${type}.plan_review_building`);
      if (table.plan_review_planning !== undefined)
        validateAreaFeeBands(table.plan_review_planning, `area_tables.${type}.plan_review_planning`, true);
    }
    // Non-area permit types (commercial / alterations) fall through to the
    // valuation_fallback; without it they would silently compute a $0 permit fee.
    if (!pf.valuation_fallback?.method)
      throw new Error('area_band permit_fee missing valuation_fallback (needed for non-area permit types)');
  }
  if (m === 'area_stepped') {
    const pf = obj.building.permit_fee;
    if (!pf.area_tables || typeof pf.area_tables !== 'object')
      throw new Error('area_stepped permit_fee missing area_tables');
    for (const [type, brackets] of Object.entries(pf.area_tables))
      if (!Array.isArray(brackets) || brackets.length === 0)
        throw new Error(`area_stepped area_tables.${type} must be a non-empty array`);
    const split = obj.building.combined_fee_split;
    if (!split || typeof split.building_permit_pct !== 'number' || typeof split.plan_review_pct !== 'number')
      throw new Error('area_stepped building fees require combined_fee_split');
    if (Math.abs(split.building_permit_pct + split.plan_review_pct - 1) > 0.000001)
      throw new Error('area_stepped combined_fee_split must total 1');
  }
  validatePlanReviewOptions(obj.building, obj.permit_types);
  for (const [permitType, exemptThrough] of Object.entries(obj.statewide?.school_fee_exempt_through_sqft_by_permit_type ?? {})) {
    if (!permitType || typeof exemptThrough !== 'number' || !Number.isFinite(exemptThrough) || exemptThrough < 0)
      throw new Error('statewide.school_fee_exempt_through_sqft_by_permit_type entries require non-negative numeric thresholds');
  }
  if (obj.statewide?.school_fee_excludes_existing_habitable_conversion !== undefined &&
      typeof obj.statewide.school_fee_excludes_existing_habitable_conversion !== 'boolean')
    throw new Error('statewide.school_fee_excludes_existing_habitable_conversion must be boolean');
  if (obj.sewer_connection?.condition && !obj.sewer_connection.condition_group)
    throw new Error('sewer_connection.condition requires condition_group');
  const lineGroupIds = new Set();
  for (const group of obj.fee_line_groups ?? []) {
    if (!group?.id || !group?.label)
      throw new Error('fee_line_groups entries require id and label');
    if (lineGroupIds.has(group.id))
      throw new Error(`fee_line_groups.${group.id} is declared twice`);
    lineGroupIds.add(group.id);
  }
  const validateLineGroup = (entry, path) => {
    if (entry.line_group !== undefined && !lineGroupIds.has(entry.line_group))
      throw new Error(`${path}.line_group must name a fee_line_groups id`);
  };
  for (const addon of obj.scope_addons ?? []) {
    if (!addon?.id || !addon?.label || !addon?.trigger_scope)
      throw new Error('scope_addons entries require id, label, and trigger_scope');
    validateLineGroup(addon, `scope_addons.${addon.id}`);
    if (addon.outside_valuation !== true)
      throw new Error(`scope_addons.${addon.id}.outside_valuation must be true`);
    if ((typeof addon.amount === 'number') === Boolean(addon.rule))
      throw new Error(`scope_addons.${addon.id} must define exactly one of amount or rule`);
    validateDueAt(addon.due_at, `scope_addons.${addon.id}.due_at`);
    if (addon.rule) validateAddonRule(addon.rule, `scope_addons.${addon.id}.rule`);
    if (addon.rule?.omit_when_exempt !== undefined && typeof addon.rule.omit_when_exempt !== 'boolean')
      throw new Error(`scope_addons.${addon.id}.rule.omit_when_exempt must be boolean`);
    if (addon.confirm_note !== undefined && (typeof addon.confirm_note !== 'string' || !addon.confirm_note.trim()))
      throw new Error(`scope_addons.${addon.id}.confirm_note must be a non-empty string`);
  }
  for (const [owner, deposits] of [
    ['building', obj.building?.deposit],
    ['public_works', obj.public_works?.deposit],
  ]) {
    for (const deposit of deposits ?? []) {
      if (!deposit?.id || !deposit?.label || !deposit?.trigger_scope ||
          (typeof deposit.amount !== 'number' && typeof deposit.min !== 'number'))
        throw new Error(`${owner}.deposit entries require id, label, trigger_scope, and numeric amount or min`);
      validateDueAt(deposit.due_at, `${owner}.deposit.${deposit.id}.due_at`);
      validateLineGroup(deposit, `${owner}.deposit.${deposit.id}`);
    }
  }
  for (const fee of obj.excluded_fees ?? []) {
    if (!fee?.id || !fee?.label || !fee?.reason)
      throw new Error('excluded_fees entries require id, label, and reason');
  }
  for (const ask of obj.open_asks ?? []) {
    if (!ask?.id || !ask?.question || !ask?.status)
      throw new Error('open_asks entries require id, question, and status');
  }
  if (obj.review_trigger_definitions !== undefined) {
    const definitions = obj.review_trigger_definitions;
    if (definitions?.schema_version !== 1 || definitions?.city !== obj.city_slug ||
        !definitions?.trigger_scopes || !Array.isArray(definitions?.required_reviews)) {
      throw new Error('review_trigger_definitions must be the city\'s schema-v1 trigger data');
    }
    const known = new Set(Object.keys(definitions.trigger_scopes));
    for (const route of obj.fee_review_triggers ?? []) {
      for (const id of route.trigger_definition_ids ?? []) {
        if (!known.has(id)) throw new Error(`fee_review_triggers references unknown trigger definition ${id}`);
        if (!(route.trigger_scopes ?? []).includes(id)) {
          throw new Error(`fee_review_triggers ${route.review} must wire trigger definition ${id} to the same trigger_scope`);
        }
      }
    }
  }
  const planningIds = new Set();
  const registerPlanningFee = (fee, path) => {
    if (!fee?.id || !fee?.label) throw new Error(`${path} entries require id and label`);
    if (planningIds.has(fee.id)) throw new Error(`duplicate planning fee id: ${fee.id}`);
    planningIds.add(fee.id);
  };
  for (const fee of obj.planning?.flat ?? []) {
    registerPlanningFee(fee, 'planning.flat');
    if (typeof fee.amount !== 'number') throw new Error(`planning.flat.${fee.id}.amount must be numeric`);
    if (fee.kind !== undefined && fee.kind !== 'flat') throw new Error(`planning.flat.${fee.id}.kind must be flat`);
    validateDueAt(fee.due_at, `planning.flat.${fee.id}.due_at`);
  }
  for (const fee of obj.planning?.deposit ?? []) {
    registerPlanningFee(fee, 'planning.deposit');
    if (fee.kind !== undefined && fee.kind !== 'actual_cost_deposit')
      throw new Error(`planning.deposit.${fee.id}.kind must be actual_cost_deposit`);
    if (fee.min !== undefined && typeof fee.min !== 'number')
      throw new Error(`planning.deposit.${fee.id}.min must be numeric`);
  }
  for (const fee of obj.planning?.variable ?? []) {
    registerPlanningFee(fee, 'planning.variable');
    if (!['percent_of_base', 'base_plus_actual_cost', 'base_plus_per_unit'].includes(fee.kind))
      throw new Error(`planning.variable.${fee.id}.kind is unsupported: ${String(fee.kind)}`);
    if (fee.kind === 'percent_of_base' && (typeof fee.pct !== 'number' || !fee.of?.length))
      throw new Error(`planning.variable.${fee.id} percent_of_base requires pct and of`);
    if (fee.kind === 'base_plus_actual_cost' && typeof fee.base !== 'number')
      throw new Error(`planning.variable.${fee.id} base_plus_actual_cost requires numeric base`);
    if (fee.kind === 'base_plus_per_unit' &&
        (typeof fee.base !== 'number' || typeof fee.per_unit !== 'number' || !fee.unit_label))
      throw new Error(`planning.variable.${fee.id} base_plus_per_unit requires base, per_unit, and unit_label`);
  }
  for (const fee of obj.planning?.known_gaps ?? []) {
    registerPlanningFee(fee, 'planning.known_gaps');
    if (fee.kind !== 'known_gap' || !fee.note)
      throw new Error(`planning.known_gaps.${fee.id} requires kind known_gap and a note`);
  }
  const peerReviewPackages = obj.planning?.peer_review_packages ?? [];
  if (!Array.isArray(peerReviewPackages))
    throw new Error('planning.peer_review_packages must be an array');
  const peerReviewPackageIds = new Set();
  const peerReviewStudyIds = new Set();
  for (const reviewPackage of peerReviewPackages) {
    if (!reviewPackage?.id || !reviewPackage?.label || !Array.isArray(reviewPackage.studies) || !reviewPackage.studies.length)
      throw new Error('planning.peer_review_packages entries require id, label, and non-empty studies');
    if (peerReviewPackageIds.has(reviewPackage.id))
      throw new Error(`duplicate planning peer-review package id: ${reviewPackage.id}`);
    peerReviewPackageIds.add(reviewPackage.id);
    for (const study of reviewPackage.studies) {
      if (!study?.id || !study?.label)
        throw new Error(`planning.peer_review_packages.${reviewPackage.id}.studies entries require id and label`);
      if (peerReviewStudyIds.has(study.id))
        throw new Error(`duplicate planning peer-review technical study id: ${study.id}`);
      peerReviewStudyIds.add(study.id);
    }
  }
  if (planningIds.has('peer_review') && peerReviewPackages.length === 0)
    throw new Error('planning.deposit.peer_review requires planning.peer_review_packages metadata');
  for (const spec of obj.site_fact_conditions ?? []) {
    if (!spec?.path || typeof spec.equals !== 'string' || !spec.equals || !spec?.condition || !spec?.condition_group)
      throw new Error('site_fact_conditions entries require path, string equals, condition, and condition_group');
  }
  for (const lookup of obj.external_lookups ?? []) {
    if (lookup?.kind !== 'arcgis_address_polygon_intersect' || !lookup?.id || !lookup?.condition_group ||
        !lookup?.address_service_url || !Number.isInteger(lookup?.address_layer) || !lookup?.address_search_fields?.length ||
        !lookup?.boundary_layer_url || !lookup?.out_fields?.length || !lookup?.matches?.length)
      throw new Error('external_lookups entries require a supported kind, ids, ArcGIS layer fields/URLs, and matches');
    for (const match of lookup.matches) {
      // `fields: {}` matches any intersecting feature (a one-polygon service area).
      if (!match?.condition || !match?.fields || typeof match.fields !== 'object' || Array.isArray(match.fields) ||
          Object.values(match.fields).some((value) => typeof value !== 'string'))
        throw new Error(`external_lookups.${lookup.id}.matches require a condition and string field values`);
    }
    if (lookup.outside_resolves !== undefined && typeof lookup.outside_resolves !== 'boolean')
      throw new Error(`external_lookups.${lookup.id}.outside_resolves must be a boolean`);
    validateLookupDisplay(lookup);
  }
  validateSeparatePermits(obj);
  validateFeeCapture(obj);
  // Fill safe defaults for optional blocks.
  obj.statewide ??= {};
  obj.status ??= 'scaffolded';
  obj.valuation ??= { source: 'applicant_or_icc_bvd' };
  return obj;
}

function validateDueAt(value, path) {
  if (value !== undefined && !FEE_DUE_AT.includes(value))
    throw new Error(`${path} must be one of ${FEE_DUE_AT.join(', ')}`);
}

function isIsoDate(value) {
  if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(value)) return false;
  const parsed = new Date(`${value}T00:00:00Z`);
  return Number.isFinite(parsed.getTime()) && parsed.toISOString().slice(0, 10) === value;
}

function validateAddonRule(rule, path) {
  const supported = ['per_unit', 'percent_of_valuation', 'percent_of_lines', 'stepped', 'adu_proportional', 'lesser_of'];
  if (!supported.includes(rule?.type)) throw new Error(`${path}.type is unsupported: ${String(rule?.type)}`);
  if (rule.type === 'per_unit' && (typeof rule.rate !== 'number' || !rule.input))
    throw new Error(`${path} per_unit requires input and numeric rate`);
  if (rule.type === 'percent_of_valuation' && typeof rule.pct !== 'number')
    throw new Error(`${path} percent_of_valuation requires numeric pct`);
  if (rule.type === 'percent_of_lines' && (!rule.line_ids?.length || typeof rule.multiplier !== 'number'))
    throw new Error(`${path} percent_of_lines requires line_ids and numeric multiplier`);
  if (rule.type === 'stepped' && !rule.brackets?.length)
    throw new Error(`${path} stepped requires brackets`);
  if (rule.type === 'adu_proportional' && typeof rule.full_amount !== 'number')
    throw new Error(`${path} adu_proportional requires full_amount`);
  if (rule.type === 'lesser_of' &&
      (!rule.first_input || typeof rule.first_rate !== 'number' || !rule.second_input || typeof rule.second_rate !== 'number'))
    throw new Error(`${path} lesser_of requires two inputs and two numeric rates`);
}

function validateAreaFeeBands(bands, path, flatOnly = false) {
  if (!Array.isArray(bands) || bands.length === 0)
    throw new Error(`area_band ${path} must be a non-empty array`);
  for (const [index, band] of bands.entries()) {
    const at = `${path}[${index}]`;
    const hasFlat = typeof band?.flat === 'number';
    const hasBase = typeof band?.base === 'number';
    const hasIncrement = typeof band?.per_100sqft === 'number';
    if (flatOnly) {
      if (!hasFlat || hasBase || hasIncrement)
        throw new Error(`area_band ${at} must be flat-only`);
    } else if (hasFlat === (hasBase || hasIncrement) || hasBase !== hasIncrement) {
      throw new Error(`area_band ${at} must define either flat or base + per_100sqft`);
    }
    if (hasBase && typeof band.from_sqft !== 'number')
      throw new Error(`area_band ${at} base + per_100sqft band missing from_sqft`);
  }
}

// ─────────────────────────── calculator ───────────────────────────

const RESIDENTIAL_TYPES = new Set([
  'adu',
  'jadu',
  'new_sfr',
  'sfr',
  'addition',
  'remodel',
  'residential-remodel',
  'residential-addition',
]);

export function normalizePermitType(value) {
  const raw = String(value ?? '').trim().toLowerCase();
  const hyphenated = raw.replace(/[\s_]+/g, '-');
  const compact = hyphenated.replace(/[^a-z0-9]/g, '');

  if (compact === 'adu' || compact === 'accessorydwellingunit') return 'adu';
  if (compact === 'jadu' || compact === 'junioraccessorydwellingunit') return 'jadu';
  if ([
    'newsfr',
    'sfr',
    'newhome',
    'newsinglefamilyhome',
    'singlefamilyhome',
    'singlefamilyresidential',
    'singlefamilydwelling',
  ].includes(compact)) return 'new_sfr';
  if ([
    'addition',
    'residentialaddition',
    'homeaddition',
  ].includes(compact)) return 'addition';
  if ([
    'remodel',
    'residentialremodel',
    'alteration',
    'residentialalteration',
    'repair',
    'sfrrepair',
  ].includes(compact)) return 'remodel';
  if ([
    'commercialti',
    'tenantimprovement',
    'commercialtenantimprovement',
  ].includes(compact)) return 'commercial-ti';
  if ([
    'reroof',
    'roofing',
    'roofreplacement',
    'residentialreroof',
  ].includes(compact)) return 'reroof';
  if ([
    'garage',
    'carport',
    'detachedgarage',
    'residentialgarage',
    'garagecarport',
  ].includes(compact)) return 'detached-garage';
  if ([
    'solar',
    'solarpv',
    'photovoltaic',
    'residentialsolar',
  ].includes(compact)) return 'solar';
  if ([
    'commercialsolar',
    'commercialsolarpv',
    'commercialphotovoltaic',
  ].includes(compact)) return 'commercial-solar';
  if ([
    'swimmingpool',
    'pool',
    'spa',
    'poolspa',
    'swimmingpoolspa',
  ].includes(compact)) return 'swimming-pool';
  if (['demolitiononefamily', 'onefamilydemolition', 'sfrdemolition'].includes(compact)) return 'demolition-one-family';
  if (['demolitionmultifamily', 'multifamilydemolition'].includes(compact)) return 'demolition-multifamily';
  if (['demolitionsimplestructure', 'simplestructuredemolition'].includes(compact)) return 'demolition-simple-structure';
  if (['demolitionother', 'otherdemolition', 'demolitionotherthanstructure'].includes(compact)) return 'demolition-other';
  if (['drainagealteration', 'drainagepermit', 'drainagealterationpermit'].includes(compact)) return 'drainage-alteration';
  if (['grading', 'gradingpermit', 'gradingonly'].includes(compact)) return 'grading';
  if (['firesprinkleralarm', 'firesprinkleralarmmisc', 'buildingfiremisc', 'buildingfiresprinkleralarmmisc'].includes(compact)) return 'building-fire-misc';
  if (['electrical', 'electricalpermit'].includes(compact)) return 'electrical';
  if (['mechanical', 'mechanicalpermit'].includes(compact)) return 'mechanical';
  if (['plumbing', 'plumbingpermit'].includes(compact)) return 'plumbing';
  if ([
    'patiocover',
    'coveredpatio',
    'residentialpatiocover',
  ].includes(compact)) return 'patio-cover';

  return raw.replace(/\s+/g, '_');
}

function inferredScopes(permitType, inputs) {
  const scopes = new Set(inputs.scopes ?? []);
  // Quantity keys are themselves explicit scope assertions. This lets a city
  // publish dozens of unit rows without showing every unrelated row whenever a
  // caller asks for a single outlet, fixture, appliance, or inspection item.
  for (const key of Object.keys(inputs.scopeQuantities ?? {})) scopes.add(key);
  if (permitType === 'new_sfr') {
    for (const scope of ['new_sfr', 'new_building', 'new_residential_unit', 'new_floor_area', 'construction_demolition']) scopes.add(scope);
  } else if (permitType === 'adu') {
    for (const scope of ['adu', 'new_building', 'new_residential_unit', 'new_floor_area', 'construction_demolition']) scopes.add(scope);
  } else if (permitType === 'jadu') {
    for (const scope of ['jadu', 'new_residential_unit', 'new_floor_area', 'construction_demolition']) scopes.add(scope);
  } else if (permitType === 'addition') {
    for (const scope of ['addition', 'new_floor_area', 'construction_demolition']) scopes.add(scope);
  } else if (permitType === 'remodel') {
    for (const scope of ['remodel', 'construction_demolition']) scopes.add(scope);
  } else if (permitType === 'commercial-ti') {
    for (const scope of ['commercial_tenant_improvement', 'remodel', 'construction_demolition']) scopes.add(scope);
  } else if (permitType === 'reroof') {
    for (const scope of ['reroof', 'construction_demolition']) scopes.add(scope);
  } else if (permitType === 'solar') {
    scopes.add('residential_solar');
  } else if (permitType === 'commercial-solar') {
    scopes.add('commercial_solar');
  } else if (permitType === 'swimming-pool') {
    scopes.add('pool_spa');
  } else if (permitType.startsWith('demolition-')) {
    scopes.add(permitType.replace(/-/g, '_'));
  } else if (permitType === 'grading') {
    scopes.add('grading');
  } else if (permitType === 'drainage-alteration') {
    scopes.add('drainage_alteration');
  } else if (permitType === 'building-fire-misc') {
    scopes.add('building_fire_misc');
  }
  return scopes;
}

function quantityFor(name, inputs, valuation, area) {
  const builtIn = {
    valuation,
    new_floor_area_sqft: inputs.newFloorAreaSqft ?? area,
    adu_sqft: inputs.aduSqft ?? area,
    new_dwelling_units: inputs.newDwellingUnits ?? (['adu', 'jadu', 'new_sfr'].includes(normalizePermitType(inputs.permitType)) ? 1 : null),
    primary_dwelling_sqft: inputs.primaryDwellingSqft,
  };
  const value = builtIn[name] ?? inputs.scopeQuantities?.[name];
  return typeof value === 'number' && Number.isFinite(value) ? value : null;
}

function conditionState(addon, inputs) {
  if (!addon.condition) return 'matched';
  const conditions = new Set(inputs.conditions ?? []);
  if (conditions.has(addon.condition)) return 'matched';
  if (addon.condition_group && !(inputs.resolvedConditionGroups ?? []).includes(addon.condition_group)) return 'unresolved';
  return 'not_matched';
}

function evaluateAddon(addon, inputs, valuation, area, firm) {
  if (typeof addon.amount === 'number') return { amount: addon.amount, tag: 'computable_now' };
  const rule = addon.rule;
  if (rule.type === 'percent_of_valuation') {
    if (!(valuation > 0)) return { note: 'Provide the project valuation to compute this fee.' };
    return { amount: round2(valuation * rule.pct), tag: 'percent_of_base' };
  }
  if (rule.type === 'percent_of_lines') {
    const base = firm.filter((line) => rule.line_ids.includes(line.id)).reduce((sum, line) => sum + line.amount, 0);
    if (!(base > 0)) return { note: rule.missing_note ?? 'The referenced permit or plan-check fee must be resolved before this fee can be computed.' };
    let amount = base * rule.multiplier;
    if (typeof rule.minimum === 'number') amount = Math.max(amount, rule.minimum);
    return { amount: round2(amount), tag: 'percent_of_base' };
  }
  if (rule.type === 'stepped') {
    const quantity = quantityFor(rule.input ?? 'valuation', inputs, valuation, area);
    if (typeof quantity !== 'number' || quantity < 0) return { note: `Provide ${rule.input ?? 'valuation'} to compute this fee.` };
    return { amount: round2(steppedSchedule(quantity, rule.brackets) * (rule.multiplier ?? 1)), tag: 'computable_now' };
  }
  if (rule.type === 'per_unit') {
    const quantity = quantityFor(rule.input, inputs, valuation, area);
    if (typeof quantity !== 'number' || quantity < 0) return { note: `Provide ${rule.input.replace(/_/g, ' ')} to compute this fee.` };
    if (typeof rule.min_input === 'number' && quantity < rule.min_input) return { skip: true };
    if (typeof rule.withhold_above === 'number' && quantity > rule.withhold_above) {
      return { note: rule.withhold_note ?? `The published calculation is incomplete above ${rule.withhold_above.toLocaleString()} units; confirm the operational amount with the city.` };
    }
    const unit = rule.unit ?? 1;
    const adjustedQuantity = Math.max(0, quantity - (rule.offset ?? 0));
    const count = rule.rounding === 'ceil' ? Math.ceil(adjustedQuantity / unit) : adjustedQuantity / unit;
    let amount = count * rule.rate;
    if (typeof rule.minimum === 'number') amount = Math.max(amount, rule.minimum);
    if (typeof rule.maximum === 'number') amount = Math.min(amount, rule.maximum);
    return { amount: round2(amount), tag: 'per_unit_lookup' };
  }
  if (rule.type === 'lesser_of') {
    const first = quantityFor(rule.first_input, inputs, valuation, area);
    const second = quantityFor(rule.second_input, inputs, valuation, area);
    if (!(first >= 0) || !(second >= 0)) {
      return { note: `Provide ${rule.first_input.replace(/_/g, ' ')} and ${rule.second_input.replace(/_/g, ' ')} to compute the published lesser-of formula.` };
    }
    return { amount: round2(Math.min(first * rule.first_rate, second * rule.second_rate)), tag: 'per_unit_lookup' };
  }
  if (rule.type === 'adu_proportional') {
    const aduSqft = quantityFor(rule.input ?? 'adu_sqft', inputs, valuation, area);
    if (!(aduSqft > 0)) return { note: 'Provide the ADU floor area to classify this impact fee.' };
    const exemptThrough = rule.exempt_through_sqft ?? 750;
    if (aduSqft <= exemptThrough) return rule.omit_when_exempt ? { skip: true } : { amount: 0, tag: 'exempt' };
    const primary = quantityFor(rule.primary_input ?? 'primary_dwelling_sqft', inputs, valuation, area);
    if (!(primary > 0)) return { note: `ADUs over ${exemptThrough} sq ft pay this fee proportionally to the primary dwelling; provide the primary dwelling area.` };
    return { amount: round2(rule.full_amount * (aduSqft / primary)), tag: 'per_unit_lookup' };
  }
  return { note: 'Confirm this fee with the collecting division.' };
}

/** The labeled group a schedule puts a fee line in, spread onto the line. */
function lineGroup(schedule, entry) {
  const group = entry.line_group && schedule.fee_line_groups?.find((candidate) => candidate.id === entry.line_group);
  return group ? { group: { id: group.id, label: group.label } } : {};
}

function applyScopedFees(schedule, inputs, context, firm, confirm) {
  const scopes = inferredScopes(context.permitType, inputs);
  const captureGroups = schedule.fee_capture?.groups ?? [];
  const countedGroups = new Set(captureGroups
    .filter((group) => group.inputs.some((entry) => inputs.scopeQuantities?.[feeCaptureInputId(entry)] > 0))
    .map((group) => group.id));
  for (const group of captureGroups) {
    if (group.scope && countedGroups.has(group.id)) scopes.add(group.scope);
  }
  // A combination permit asserts its trade scopes and replaces the itemized unit rows.
  for (const scope of context.combinationTrades?.asserts_scopes ?? []) scopes.add(scope);
  const replacedGroups = context.combinationTrades?.replaces_capture_groups ?? [];
  const replacedInputs = new Set(captureGroups
    .filter((group) => replacedGroups.includes(group.id))
    .flatMap((group) => group.inputs.map(feeCaptureInputId)));
  const seenConfirm = new Set(confirm.map((line) => line.id));
  const addConfirm = (line) => {
    if (!seenConfirm.has(line.id)) {
      seenConfirm.add(line.id);
      confirm.push(line);
    }
  };
  // A trade the work includes but whose unit counts the packet does not state:
  // its base fee prices from the scope, and the counts are asked for, never assumed.
  // A permit type that already requires those counts asks for them itself.
  const requiredInputs = new Set(context.requiredAnyInputs ?? []);
  for (const group of captureGroups) {
    if (!group.scope || !scopes.has(group.scope) || replacedGroups.includes(group.id) || countedGroups.has(group.id)) continue;
    if (group.inputs.some((entry) => requiredInputs.has(feeCaptureInputId(entry)))) continue;
    const baseFee = (schedule.scope_addons ?? []).find((addon) => addon.trigger_scope === group.scope);
    const trade = group.label.toLowerCase();
    addConfirm({
      id: `counts_${group.id}`,
      label: `${group.label} unit counts`,
      note: `The work includes ${trade} work, but the packet states no ${trade} unit counts. Provide them to price the per-unit ${trade} fees.`,
      cite: baseFee?.cite,
      ownerDivision: baseFee?.owner_division,
    });
  }
  for (const addon of schedule.scope_addons ?? []) {
    if (!scopes.has(addon.trigger_scope)) continue;
    if (addon.permit_types?.length && !addon.permit_types.includes(context.permitType)) continue;
    if (replacedInputs.has(addon.trigger_scope) || replacedInputs.has(addon.rule?.input)) continue;
    const result = evaluateAddon(addon, inputs, context.valuation, context.area, firm);
    if (result.skip) continue;
    const state = conditionState(addon, inputs);
    if (state === 'not_matched') continue;
    if (state === 'unresolved') {
      addConfirm({
        id: `condition_${addon.condition_group}`,
        label: addon.condition_label ?? 'Location-based fee applicability',
        note: addon.unresolved_note ?? 'Resolve the parcel against the adopted fee boundary before adding this fee.',
        cite: addon.cite,
        ownerDivision: addon.owner_division,
      });
      continue;
    }
    // A `confirm_note` add-on is priced, but staff decide whether the City collects it.
    const confirmNote = result.note ??
      (addon.confirm_note && `${addon.confirm_note} As entered: ${formatDollars(result.amount, { cents: true })}.`);
    if (confirmNote) {
      addConfirm({ id: `scope_${addon.id}`, label: addon.label, note: confirmNote, cite: addon.cite, ownerDivision: addon.owner_division });
      continue;
    }
    firm.push({
      id: addon.id,
      label: addon.label,
      amount: result.amount,
      tag: result.tag,
      dueAt: addon.due_at ?? 'issuance',
      cite: addon.cite,
      ownerDivision: addon.owner_division,
      surchargeIds: addon.surcharge_ids,
      ...lineGroup(schedule, addon),
    });
  }

  for (const [owner, deposits] of [
    ['Building', schedule.building?.deposit],
    ['Public Works', schedule.public_works?.deposit],
  ]) {
    for (const deposit of deposits ?? []) {
      if (!scopes.has(deposit.trigger_scope)) continue;
      if (deposit.permit_types?.length && !deposit.permit_types.includes(context.permitType)) continue;
      if (typeof deposit.amount === 'number') {
        firm.push({
          id: deposit.id,
          label: deposit.label,
          amount: deposit.amount,
          tag: 'computable_now',
          dueAt: deposit.due_at ?? 'issuance',
          cite: deposit.cite,
          ownerDivision: owner,
          refundable: deposit.refundable === true,
          ...lineGroup(schedule, deposit),
        });
      } else {
        addConfirm({
          id: deposit.id,
          label: deposit.label,
          note: deposit.note ?? 'Deposit billed against actual review cost; final amount is reconciled by the collecting division.',
          minDeposit: deposit.min,
          cite: deposit.cite,
          ownerDivision: owner,
        });
      }
    }
  }

  return scopes;
}

/** A surcharge deferred until scoped is charged on its base lines and on lines that carry it. */
function feedsScopedSurcharge(s, line) {
  return Boolean(s.base_line_ids?.includes(line.id) || line.surchargeIds?.includes(s.id) ||
    line.surchargeIds?.some((id) => s.base_surcharge_ids?.includes(id)));
}

/** A capture input's value on FeeInputs: a built-in field or a scope quantity. */
function captureInputValue(inputs, id) {
  const field = FEE_CAPTURE_BUILT_INS[id]?.field;
  const value = field ? inputs[field] : inputs.scopeQuantities?.[id];
  return typeof value === 'number' && Number.isFinite(value) ? value : null;
}

function withoutCaptureInputs(inputs, ids) {
  const next = { ...inputs, scopeQuantities: { ...(inputs.scopeQuantities ?? {}) } };
  for (const id of ids) {
    const field = FEE_CAPTURE_BUILT_INS[id]?.field;
    if (field) delete next[field];
    else delete next.scopeQuantities[id];
  }
  return next;
}

/**
 * The FeeInputs of every City record the project files, the screened record
 * first. Each `separate_permits` entry that applies is its own record, priced
 * like one: its own permit type and valuation (`valuation_input`, the value on
 * its own application), the scopes and inputs it takes off the screened
 * record, and what every record shares (use, stories, location conditions, and
 * a percent-of-plan-review scope such as expedited review). Laguna's ledgers
 * show each record carries its own plan check, SMIP, SB 1473 and surcharges,
 * so a combined estimate cannot be split after the fact.
 *
 * An entry applies when one of its scopes does, or (with no scopes) when one of
 * its inputs or its valuation is above zero; `over` adds a threshold. It never
 * applies on a record of one of its own `permit_types`. The record is filed as
 * the entry's permit type that implies an applying scope (a shed demolition is
 * a simple-structure demolition record), else as `permit_type`.
 */
export function feeInputsByPermit(schedule, inputs) {
  const recordType = normalizePermitType(inputs.permitType);
  const scopes = inputs.scopes ?? [];
  const shared = new Set((schedule.scope_addons ?? [])
    .filter((addon) => addon.rule?.type === 'percent_of_lines')
    .map((addon) => addon.trigger_scope));
  let record = inputs;
  const separate = [];
  for (const spec of schedule.separate_permits ?? []) {
    if (spec.permit_types?.some((type) => normalizePermitType(type) === recordType)) continue;
    const own = separatePermitInputs(spec);
    const applying = (spec.scopes ?? []).filter((scope) => scopes.includes(scope));
    const applies = spec.scopes?.length ? applying.length > 0 : own.some((id) => captureInputValue(inputs, id) > 0);
    if (!applies) continue;
    if (spec.over && !(captureInputValue(inputs, spec.over.input) > spec.over.value)) continue;
    const permitInputs = {
      permitType: spec.permit_types?.find((type) =>
        applying.some((scope) => inferredScopes(normalizePermitType(type), {}).has(scope))) ?? spec.permit_type,
      valuation: spec.valuation_input ? captureInputValue(inputs, spec.valuation_input) : null,
      structureUse: inputs.structureUse,
      stories: inputs.stories,
      conditions: inputs.conditions,
      resolvedConditionGroups: inputs.resolvedConditionGroups,
      scopes: scopes.filter((scope) => spec.scopes?.includes(scope) || shared.has(scope)),
      scopeQuantities: {},
    };
    for (const id of spec.inputs ?? []) {
      const field = FEE_CAPTURE_BUILT_INS[id]?.field;
      if (field) permitInputs[field] = inputs[field];
      else if (inputs.scopeQuantities?.[id] !== undefined) permitInputs.scopeQuantities[id] = inputs.scopeQuantities[id];
    }
    separate.push({ id: spec.id, label: spec.label, inputs: permitInputs });
    record = withoutCaptureInputs(record, own);
    record.scopes = (record.scopes ?? []).filter((scope) => !spec.scopes?.includes(scope));
  }
  return [{ id: 'record', label: null, inputs: record }, ...separate];
}

/** `calcFees` for each record `feeInputsByPermit` returns, the screened record first. */
export function calcFeesByPermit(schedule, inputs) {
  return feeInputsByPermit(schedule, inputs).map((permit) => ({ ...permit, breakdown: calcFees(schedule, permit.inputs) }));
}

export function recomputeFeeTotals(breakdown) {
  for (const line of breakdown.firmLines) line.dueAt ??= 'issuance';
  const subtotalsByDueAt = Object.fromEntries(FEE_DUE_AT.map((dueAt) => [dueAt, 0]));
  for (const line of breakdown.firmLines) subtotalsByDueAt[line.dueAt] = round2(subtotalsByDueAt[line.dueAt] + line.amount);
  breakdown.subtotalsByDueAt = subtotalsByDueAt;
  breakdown.permitSubtotal = round2(subtotalsByDueAt.application + subtotalsByDueAt.issuance);
  breakdown.firmSubtotal = round2(breakdown.firmLines.reduce((sum, line) => sum + line.amount, 0));
  breakdown.buildingFirmLines = breakdown.firmLines.filter((line) => line.ownerDivision === 'Building');
  breakdown.otherAgencyLines = breakdown.firmLines.filter((line) => line.ownerDivision !== 'Building');
  breakdown.buildingNeedsDetails = breakdown.confirmAtIntake.filter((line) => line.ownerDivision === 'Building');
  breakdown.otherAgencyNeedsDetails = breakdown.confirmAtIntake.filter((line) => line.ownerDivision !== 'Building');
  breakdown.buildingSubtotal = round2(breakdown.buildingFirmLines.reduce((sum, line) => sum + line.amount, 0));
  breakdown.otherAgencySubtotal = round2(breakdown.otherAgencyLines.reduce((sum, line) => sum + line.amount, 0));
  return breakdown;
}

/** The per-permit issuance line, or null when the schedule or permit type charges none. */
function issuanceLine(b, ptCfg, rawPermitCount, buildingFeeAtIntake) {
  const permitCount = typeof rawPermitCount === 'number' ? Math.max(0, Math.floor(rawPermitCount)) : 1;
  if (ptCfg?.issuance === false || !(permitCount > 0) || !(b.issuance?.first > 0)) return null;
  if (buildingFeeAtIntake && b.issuance.independent !== true) return null;
  const issuanceAmount = b.issuance.first + Math.max(0, permitCount - 1) * (b.issuance.each_additional ?? 0);
  return {
    id: 'issuance',
    label: permitCount === 1 ? 'Permit issuance' : `Permit issuance (${permitCount} permits)`,
    amount: round2(issuanceAmount),
    tag: 'computable_now',
    cite: b.issuance.cite,
    ownerDivision: b.owner_division,
  };
}

/** Run a project through a city's schedule → itemized, two-bucket breakdown. */
export function calcFees(schedule, inputs) {
  const displayName = schedule.display_name ?? schedule.city_slug;
  const permitType = normalizePermitType(inputs.permitType);
  const isResidential = RESIDENTIAL_TYPES.has(permitType);
  const isAdu = permitType === 'adu' || permitType === 'jadu';
  const occupancy = inputs.occupancy ?? (
    permitType === 'detached-garage' ? 'U' : permitType === 'commercial-ti' ? 'B' : 'R-3'
  );

  // 1) Valuation: applicant-stated, else derive from area × ICC BVD. A schedule
  // may opt new-square-foot scopes into an ICC minimum without city branches.
  let valuation = typeof inputs.valuation === 'number' && inputs.valuation > 0 ? inputs.valuation : 0;
  let valuationSource = 'applicant';
  let valuationBasisNote;
  const area = inputs.newFloorAreaSqft ?? inputs.aduSqft ?? null;
  const valuationFloor = schedule.valuation?.minimum_icc_bvd;
  const floorApplies =
    valuationFloor?.enabled === true &&
    area && area > 0 &&
    (!valuationFloor.permit_types?.length || valuationFloor.permit_types.includes(permitType));
  if (floorApplies) {
    const derived = valuationFromArea(area, occupancy);
    if (!valuation || valuation < derived.valuation) {
      const applicant = valuation;
      valuation = derived.valuation;
      valuationSource = applicant > 0 ? 'icc_floor' : 'derived';
      valuationBasisNote = applicant > 0
        ? `The applicant valuation (${formatDollars(applicant)}) is below the city's ICC minimum for this new-floor-area scope, so the estimate uses ${area.toLocaleString()} sq ft at $${derived.rate.toFixed(2)}/sq ft (${ICC_BVD_EDITION}, ${occupancy}).`
        : `Estimated from ${area.toLocaleString()} sq ft at $${derived.rate.toFixed(2)}/sq ft (${ICC_BVD_EDITION}, ${occupancy}). Give a contractor bid value for a tighter number.`;
    }
  } else if (!valuation && area && area > 0) {
    const derived = valuationFromArea(area, occupancy);
    valuation = derived.valuation;
    valuationSource = 'derived';
    valuationBasisNote = `Estimated from ${area.toLocaleString()} sq ft at $${derived.rate.toFixed(2)}/sq ft (${ICC_BVD_EDITION}, ${occupancy}). Give a contractor bid value for a tighter number.`;
  }
  if (!valuation) valuationSource = 'none';

  const firm = [];
  const confirm = [];
  const b = schedule.building;
  const ptCfg = schedule.permit_types?.[permitType];
  const buildingOwner = b.owner_division;
  const scopedOnly = ptCfg?.building_fee_rule === 'scope_addons_only';
  const unresolvedBuildingBand = (b.permit_fee.unresolved_bands ?? []).find((band) =>
    valuation > (band.from ?? 0) && (band.up_to === null || valuation <= band.up_to));
  const publishedBuildingRows = Array.isArray(b.permit_fee.published_rows)
    ? b.permit_fee.published_rows
    : [];
  const publishedBuildingRow = publishedBuildingRows.find((row) =>
    valuation >= (row.from ?? 0) && (row.up_to === null || valuation <= row.up_to));
  const buildingFeeAtIntake = !scopedOnly && (
    b.permit_fee.method === 'confirm_at_intake' ||
    ptCfg?.building_fee_rule === 'confirm_at_intake' ||
    (!ptCfg && b.permit_fee.unlisted_permit_types === 'confirm_at_intake') ||
    Boolean(unresolvedBuildingBand));

  // 2) Building permit + plan review + issuance (the computable core).
  let permitFee = 0;
  // Area-band cities (Newport): residential permit & plan review are flat dollars
  // keyed to project type + floor-area band, NOT a function of valuation. This
  // branch only runs when the schedule opts in (method 'area_band' AND a table
  // for this permit type); every valuation-based city (Laguna flat_band, Buena
  // Park stepped) falls straight through to the valuation path below, unchanged.
  const areaTable = b.permit_fee.method === 'area_band' ? b.permit_fee.area_tables?.[permitType] : null;
  const areaSteppedTable = b.permit_fee.method === 'area_stepped' ? b.permit_fee.area_tables?.[permitType] : null;
  const areaForBand = typeof area === 'number' && Number.isFinite(area) && area > 0 ? area : null;
  const legacyAreaBands = Array.isArray(areaTable) ? areaTable : null;
  const permitAreaBands = legacyAreaBands ?? areaTable?.permit ?? null;
  const hasSingleCatchAllAreaBand =
    permitAreaBands?.length === 1 &&
    (permitAreaBands[0].up_to_sqft === null || permitAreaBands[0].up_to_sqft === undefined);
  if (scopedOnly) {
    // The adopted schedule supplies this permit type through explicit flat or
    // unit rows in scope_addons. Do not fall through to a structure-valuation
    // formula merely because the caller also supplied a valuation.
  } else if (buildingFeeAtIntake) {
    const confirmationReason = unresolvedBuildingBand?.note ?? ptCfg?.building_fee_note ??
      b.permit_fee.reason ?? 'This permit type requires a city-specific fee determination at intake.';
    const publishedRowNote = publishedBuildingRow
      ? `Applicable published row ${publishedBuildingRow.row}: ${publishedBuildingRow.text}. `
      : '';
    confirm.push({
      id: 'building_permit',
      label: 'Building permit + plan review',
      note: `${publishedRowNote}${confirmationReason}`,
      cite: ptCfg?.building_fee_cite ?? b.permit_fee.cite,
      ownerDivision: buildingOwner,
    });
  } else if (areaTable && (areaForBand !== null || hasSingleCatchAllAreaBand)) {
    const feeArea = areaForBand ?? 1;
    if (legacyAreaBands) {
      const band = areaBand(feeArea, legacyAreaBands) ?? {};
      permitFee = band.permit ?? 0;
      firm.push({ id: 'building_permit', label: 'Building permit & inspection (per floor-area schedule)', amount: permitFee, tag: 'computable_now', cite: b.permit_fee.cite, ownerDivision: buildingOwner });
      if (typeof band.plan_review === 'number') {
        firm.push({ id: 'plan_review', label: 'Plan review (per floor-area schedule)', amount: band.plan_review, tag: 'computable_now', cite: b.plan_review_cite, ownerDivision: buildingOwner });
      }
    } else {
      permitFee = areaBandFee(feeArea, areaTable.permit);
      firm.push({ id: 'building_permit', label: 'Building permit & inspection (per floor-area schedule)', amount: permitFee, tag: 'computable_now', cite: b.permit_fee.cite, ownerDivision: buildingOwner });
      if (areaTable.plan_review_building) {
        firm.push({
          id: 'plan_review_building',
          label: 'Plan review - Building (per floor-area schedule)',
          amount: areaBandFee(feeArea, areaTable.plan_review_building),
          tag: 'computable_now',
          cite: b.permit_fee.cite,
          ownerDivision: buildingOwner,
        });
      }
      if (areaTable.plan_review_planning) {
        firm.push({
          id: 'plan_review_planning',
          label: 'Plan review - Planning (per floor-area schedule)',
          amount: areaBandFee(feeArea, areaTable.plan_review_planning),
          tag: 'computable_now',
          cite: b.permit_fee.cite,
          ownerDivision: b.planning_owner_division,
        });
      }
    }
  } else if (areaTable) {
    confirm.push({
      id: 'building_permit',
      label: 'Building permit + plan review',
      note: 'Provide the new or affected floor area (sq ft) to compute the adopted floor-area fee.',
      cite: b.permit_fee.cite,
      ownerDivision: buildingOwner,
    });
  } else if (areaSteppedTable && areaForBand !== null) {
    const combinedFee = areaSteppedSchedule(areaForBand, areaSteppedTable);
    const split = b.combined_fee_split;
    permitFee = round2(combinedFee * split.building_permit_pct);
    const planFee = round2(combinedFee - permitFee);
    firm.push({
      id: 'building_permit',
      label: `Building permit & inspection (${Math.round(split.building_permit_pct * 100)}% of combined area fee)`,
      amount: permitFee,
      tag: 'computable_now',
      cite: b.permit_fee.cite,
      ownerDivision: buildingOwner,
    });
    firm.push({
      id: 'plan_review',
      label: `Plan review (${Math.round(split.plan_review_pct * 100)}% of combined area fee)`,
      amount: planFee,
      tag: 'percent_of_base',
      cite: b.permit_fee.cite,
      ownerDivision: buildingOwner,
    });
    if (b.permit_fee.assumption_note) {
      confirm.push({
        id: 'building_classification',
        label: 'Construction tier / occupancy classification',
        note: b.permit_fee.assumption_note,
        cite: b.permit_fee.cite,
      });
    }
  } else if (b.permit_fee.method === 'area_stepped') {
    confirm.push({
      id: 'building_permit',
      label: 'Building permit + plan review',
      note: areaSteppedTable
        ? 'Provide the new or affected floor area (sq ft) to compute the adopted area-stepped fee.'
        : ptCfg?.building_fee_note ?? 'This permit type is not represented by a single deterministic row in the adopted area schedule; confirm the classification with the city.',
      cite: ptCfg?.building_fee_cite ?? b.permit_fee.cite,
      ownerDivision: buildingOwner,
    });
  } else if (valuation > 0) {
    permitFee = buildingPermitFee(valuation, b.permit_fee);
    firm.push({ id: 'building_permit', label: 'Building permit fee', amount: permitFee, tag: 'computable_now', cite: b.permit_fee.cite, ownerDivision: buildingOwner });

    // A permit type may carry its own plan-review rate (0 = no plan review), and a
    // schedule may publish a valuation at or below which no plan review is charged.
    const planRate = ptCfg?.plan_review_pct ?? b.plan_review_pct;
    const planReviewCharged = planRate > 0 &&
      !(typeof b.plan_review_exempt_through_valuation === 'number' && valuation <= b.plan_review_exempt_through_valuation);
    if (planReviewCharged) {
      let planFee = round2(permitFee * planRate);
      if (b.plan_review_min) planFee = Math.max(planFee, b.plan_review_min);
      firm.push({ id: 'plan_review', label: `Plan review (${Math.round(planRate * 100)}% of permit fee)`, amount: planFee, tag: 'percent_of_base', cite: b.plan_review_cite, ownerDivision: buildingOwner });
    }
  } else {
    confirm.push({ id: 'building_permit', label: 'Building permit + plan review', note: 'Provide the project valuation or new floor area (sq ft) and I can compute these exactly.', ownerDivision: buildingOwner });
  }

  // Some schedules publish issuance independently from an unresolved permit
  // calculation. Preserve the historical all-or-intake behavior unless the
  // authored city schedule explicitly opts into that independent row.
  const issuance = issuanceLine(b, ptCfg, inputs.permitCount, buildingFeeAtIntake);
  if (issuance) firm.push(issuance);

  // 3) Trade permits (new construction; gated on combination scope).
  const isCombination = inputs.isCombinationPermit ?? ptCfg?.combination_trades ?? Boolean(ptCfg);
  // A combination permit can stand in for the itemized trade unit rows and carry
  // its own trade scopes; the schedule says which (trades_new.*).
  let combinationTrades = null;
  if (permitFee > 0 && b.trades_new && isCombination) {
    const t = b.trades_new;
    if (typeof t.combination_pct === 'number') {
      firm.push({ id: 'trades', label: `Combination M/E/P permit (${Math.round(t.combination_pct * 100)}% of permit fee, new construction)`, amount: round2(permitFee * t.combination_pct), tag: 'percent_of_base', cite: t.cite, ownerDivision: buildingOwner });
      combinationTrades = t;
    } else {
      if (t.electrical_pct) firm.push({ id: 'electrical', label: `Electrical permit (${Math.round(t.electrical_pct * 100)}% of permit fee)`, amount: round2(permitFee * t.electrical_pct), tag: 'percent_of_base', cite: t.cite, ownerDivision: buildingOwner });
      if (t.plumbing_pct) firm.push({ id: 'plumbing', label: `Plumbing permit (${Math.round(t.plumbing_pct * 100)}% of permit fee)`, amount: round2(permitFee * t.plumbing_pct), tag: 'percent_of_base', cite: t.cite, ownerDivision: buildingOwner });
      if (t.mechanical_pct) firm.push({ id: 'mechanical', label: `Mechanical permit (${Math.round(t.mechanical_pct * 100)}% of permit fee)`, amount: round2(permitFee * t.mechanical_pct), tag: 'percent_of_base', cite: t.cite, ownerDivision: buildingOwner });
    }
  }
  if (isCombination && b.trades_confirm_at_intake) {
    confirm.push({
      id: 'trades',
      label: 'Electrical / plumbing / mechanical permits',
      note: b.trades_confirm_at_intake,
      ownerDivision: buildingOwner,
    });
  }

  // 4) Energy / NPDES (city-specific, % of building permit).
  if (permitFee > 0 && b.energy_pct) firm.push({ id: 'energy', label: `California Energy compliance (${Math.round(b.energy_pct * 100)}% of permit fee)`, amount: round2(permitFee * b.energy_pct), tag: 'percent_of_base' });
  if (permitFee > 0 && b.npdes_pct) firm.push({ id: 'npdes', label: `NPDES / water-quality (${Math.round(b.npdes_pct * 100)}% of permit fee)`, amount: round2(permitFee * b.npdes_pct), tag: 'percent_of_base' });

  // 5) State-mandated layer (default-on).
  // `bsasrf_only`: a record that pays SB 1473 on its valuation but no SMIP (a grading permit).
  const statewideFeesApply = ptCfg?.statewide_fees !== false;
  if (statewideFeesApply && ptCfg?.statewide_fees !== 'bsasrf_only' && valuation > 0 && schedule.statewide.smip !== false) {
    const explicitSmip = schedule.statewide.smip_requires_explicit_classification === true;
    const explicitUse = ['residential', 'nonresidential'].includes(inputs.structureUse) ? inputs.structureUse : null;
    const explicitStories = typeof inputs.stories === 'number' && Number.isFinite(inputs.stories) && inputs.stories >= 1
      ? inputs.stories
      : null;
    const needsClassification = explicitSmip && (
      !explicitUse || (explicitUse === 'residential' && explicitStories === null)
    );
    if (!needsClassification) {
      const residentialCategory = explicitSmip
        ? explicitUse === 'residential' && explicitStories <= 3
        : isResidential;
      firm.push({
        id: 'smip',
        label: 'SMIP (state strong-motion fee)',
        amount: smip(
          valuation,
          residentialCategory,
          schedule.statewide.smip_residential_rate,
          schedule.statewide.smip_other_rate,
        ),
        tag: 'computable_now',
        cite: residentialCategory
          ? schedule.statewide.smip_cite ?? 'CGS'
          : schedule.statewide.smip_other_cite ?? 'Cal. Pub. Res. Code §2705(a)(2)',
        ownerDivision: schedule.statewide.smip_owner_division,
      });
    } else {
      // Ask only for the part that is missing: the use, or (use known, so residential) the stories.
      const note = explicitUse
        ? 'Provide the number of stories of the building after the work. A residential building of one to three stories uses the residential rate; a taller one uses the statewide other-building rate.'
        : 'Provide whether the building is residential or nonresidential, and for a residential building its number of stories after the work. A residential building of one to three stories uses the residential rate; other buildings use the statewide other-building rate.';
      confirm.push({ id: 'smip', label: 'SMIP (state strong-motion fee)', note, cite: schedule.statewide.smip_cite, ownerDivision: schedule.statewide.smip_owner_division });
    }
  }
  if (statewideFeesApply && valuation > 0 && schedule.statewide.bsasrf !== false) {
    firm.push({ id: 'bsasrf', label: 'CA Building Standards fee (SB 1473)', amount: bsasrf(valuation), tag: 'computable_now', cite: schedule.statewide.bsasrf_cite, ownerDivision: schedule.statewide.bsasrf_owner_division });
  }

  // 6) City surcharges (% of the specified base lines).
  if (ptCfg?.surcharges !== false) {
    for (const s of b.surcharges ?? []) {
      if (s.defer_until_scoped) continue;
      const base = sumLines(firm, s.of);
      if (base > 0) firm.push({ id: s.id, label: `${s.label} (${formatPercent(s.pct)}%)`, amount: round2(base * s.pct), tag: 'percent_of_base', cite: s.note, ownerDivision: s.owner_division });
    }
  }

  // 7) School developer fee (per sqft, district-collected upper bound).
  const minArea = schedule.statewide.school_fee_min_area_sqft ?? 500;
  const exemptThrough = schedule.statewide.school_fee_exempt_through_sqft_by_permit_type?.[permitType];
  const schoolAreaApplies = area && (typeof exemptThrough === 'number' ? area > exemptThrough : area >= minArea);
  const schoolRate = isResidential ? schedule.statewide.school_fee_residential_per_sqft : schedule.statewide.school_fee_commercial_per_sqft;
  const schoolExcludedConversion = schedule.statewide.school_fee_excludes_existing_habitable_conversion === true &&
    inputs.existingHabitableConversion === true;
  if (!schoolExcludedConversion && schoolAreaApplies && schoolRate && (ptCfg?.school_fee ?? isResidential)) {
    // Paid to the school district, which certifies payment before the permit issues
    // (Ed. Code §17620); the city does not collect it.
    firm.push({ id: 'school', label: `School developer fee (≤ $${schoolRate.toFixed(2)}/sq ft × ${area.toLocaleString()} sq ft — district-set, often lower)`, amount: round2(area * schoolRate), tag: 'per_unit_lookup', cite: schedule.statewide.school_fee_cite, ownerDivision: schedule.statewide.school_fee_owner_division, paidToOtherAgency: true });
  }

  // 8) Sewer connection (per the city's own table; additions ≥ min area).
  const sc = schedule.sewer_connection;
  const sewerApplies = ptCfg?.sewer_connection ?? (!ptCfg && (isAdu || permitType === 'new_sfr'));
  const sewerMinArea = isAdu ? (sc?.adu_min_area_sqft ?? sc?.applies_min_area_sqft ?? 500) : (sc?.applies_min_area_sqft ?? 500);
  const sewerState = sc ? conditionState(sc, inputs) : 'not_matched';
  // An unknown area cannot rule the fee out, so the location question stays open.
  // A known 0 sq ft (no new area) rules it out.
  if (sc && sewerApplies && (area == null || area >= sewerMinArea) && sewerState === 'unresolved') {
    confirm.push({
      id: `condition_${sc.condition_group}`,
      label: sc.condition_label ?? 'Sewer connection applicability',
      note: sc.unresolved_note ?? 'Confirm whether the project is served by the applicable sewer system before adding this fee.',
      cite: sc.cite,
      ownerDivision: sc.owner_division,
    });
  } else if (sc && sewerApplies && area && area >= sewerMinArea && sewerState === 'matched') {
    if ((isAdu || ['addition', 'remodel'].includes(permitType)) && sc.adu_addition_per_100sqft) {
      firm.push({ id: 'sewer', label: `Sewer connection ($${sc.adu_addition_per_100sqft}/100 sq ft)`, amount: round2((area / 100) * sc.adu_addition_per_100sqft), tag: 'per_unit_lookup', cite: sc.cite, ownerDivision: sc.owner_division });
    } else if (permitType === 'new_sfr' && sc.single_family_per_unit) {
      firm.push({ id: 'sewer', label: 'Sewer connection (per dwelling unit)', amount: sc.single_family_per_unit, tag: 'per_unit_lookup', cite: sc.cite, ownerDivision: sc.owner_division });
    }
  }

  // 9) Impact fees — exempt (ADU), or named confirm-at-intake.
  const rule = ptCfg?.impact_fee_rule ?? (isAdu ? 'ca_adu_exemption' : 'confirm_at_intake');
  if (rule === 'ca_adu_exemption') {
    const aduArea = inputs.aduSqft ?? area ?? null;
    if (aduArea && aduArea > 0) {
      const exemption = aduImpactFee(aduArea, inputs.primaryDwellingSqft);
      if (aduArea <= 750) {
        firm.push({ id: 'impact_fees', label: 'Development impact fees', amount: exemption.amount, tag: 'exempt', cite: 'Gov. Code §66311.5' });
      }
      confirm.push({
        id: 'impact_note',
        label: aduArea <= 750 ? 'Impact-fee exemption' : 'Development impact fees',
        note: exemption.note,
        cite: 'Gov. Code §66311.5',
      });
    } else {
      confirm.push({
        id: 'impact_note',
        label: 'ADU impact-fee exemption',
        note: 'Provide the ADU floor area to classify the impact-fee rule: ADUs 750 sq ft or smaller are exempt; larger ADUs are charged proportionally to the primary dwelling.',
        cite: 'Gov. Code §66311.5',
      });
    }
  } else if (rule === 'confirm_at_intake') {
    const names = ptCfg?.impact_fee_names?.length ? ptCfg.impact_fee_names.join(', ') : 'traffic, parks, drainage, public facilities';
    confirm.push({ id: 'impact_fees', label: 'Development impact fees', note: `Apply to net-new units / added floor area (${names}). City- and district-specific, set by nexus study — confirmed at intake. Remodels with no added sq ft owe $0.` });
  }

  // 10) Utility capacity (separate agencies — always confirm).
  if (!schedule.output_policy?.other_agencies_only_when_triggered || (inputs.scopes ?? []).includes('utility_capacity')) {
    confirm.push({ id: 'utility', label: 'Water / sewer capacity & connection (other agencies)', note: 'Charged by the serving water/sanitation district by meter size or EDU — confirm a will-serve quote with the district.', ownerDivision: 'Other agency' });
  }

  // 11) Planning entitlements — flat (firm, "if required") + deposits (confirm).
  if (schedule.planning?.flat?.length && !schedule.output_policy?.planning_only_when_routed) {
    const flatRefs = schedule.planning.flat.map((f) => `${f.label} $${f.amount.toLocaleString()}`).join(' · ');
    confirm.push({ id: 'planning_flat', label: 'Planning / entitlement fees (if your project needs them)', note: `Flat city fees — added only if the project triggers them: ${flatRefs}.`, ownerDivision: 'Planning' });
  }
  if (!schedule.output_policy?.planning_only_when_routed) for (const d of schedule.planning?.deposit ?? []) {
    confirm.push({ id: `deposit_${d.id}`, label: d.label, note: d.note ?? 'Deposit billed hourly against actual cost — final amount set at intake.', minDeposit: d.min, ownerDivision: 'Planning' });
  }

  // 12) Data-driven scope add-ons, refundable deposits, conditionally located
  // fees, and structured exclusions/open questions. No city-specific branches.
  const scopes = applyScopedFees(schedule, inputs, { permitType, valuation, area, combinationTrades, requiredAnyInputs: ptCfg?.required_any_inputs }, firm, confirm);
  if (ptCfg?.plan_review_of_scope_addons?.line_ids?.length) {
    const spec = ptCfg.plan_review_of_scope_addons;
    const base = firm.filter((line) => spec.line_ids.includes(line.id)).reduce((sum, line) => sum + line.amount, 0);
    if (base > 0) {
      firm.push({
        id: spec.id ?? 'plan_review_mep',
        label: spec.label ?? `Plan review (${formatPercent(spec.pct)}% of permit fee)`,
        amount: round2(base * spec.pct),
        tag: 'percent_of_base',
        dueAt: spec.due_at ?? 'application',
        cite: spec.cite,
        ownerDivision: buildingOwner,
        surchargeIds: spec.surcharge_ids,
      });
    }
  }
  if (ptCfg?.required_any_inputs?.length) {
    const hasAnyInput = ptCfg.required_any_inputs.some((input) => quantityFor(input, inputs, valuation, area) !== null);
    if (!hasAnyInput) {
      confirm.push({
        id: 'building_permit',
        label: ptCfg.required_inputs_label ?? 'Building permit quantities',
        note: ptCfg.building_fee_note ?? `Provide at least one applicable published quantity: ${ptCfg.required_any_inputs.join(', ')}.`,
        cite: ptCfg.building_fee_cite,
        ownerDivision: buildingOwner,
      });
    }
  }
  if (ptCfg?.surcharges !== false) {
    for (const s of b.surcharges ?? []) {
      if (!s.defer_until_scoped) continue;
      const base = firm.filter((line) => feedsScopedSurcharge(s, line)).reduce((sum, line) => sum + line.amount, 0);
      if (base > 0) firm.push({ id: s.id, label: `${s.label} (${formatPercent(s.pct)}%)`, amount: round2(base * s.pct), tag: 'percent_of_base', cite: s.note, ownerDivision: s.owner_division });
    }
  }
  if (unresolvedBuildingBand?.ask_scope) scopes.add(unresolvedBuildingBand.ask_scope);
  const openAsks = (schedule.open_asks ?? []).filter((ask) =>
    !ask.trigger_scopes?.length || ask.trigger_scopes.some((scope) => scopes.has(scope)));

  const breakdown = {
    city: schedule.city_slug,
    displayName,
    permitType,
    status: schedule.status,
    effectiveDate: scheduleEffectiveFrom(schedule),
    valuation,
    valuationSource,
    valuationBasisNote,
    departmentScoped: schedule.output_policy?.building_subtotal_only === true,
    firmLines: firm,
    firmSubtotal: 0,
    permitSubtotal: 0,
    subtotalsByDueAt: { application: 0, issuance: 0, certificate_of_occupancy: 0 },
    confirmAtIntake: confirm,
    excludedFees: schedule.excluded_fees ?? [],
    openAsks,
    source: { resolution: schedule.source.resolution, url: schedule.source.url },
    escalatorNote: schedule.escalator?.note,
  };
  return recomputeFeeTotals(breakdown);
}

function sumLines(lines, of) {
  return lines
    .filter((l) => {
      if (of.includes('building_permit') && l.id === 'building_permit') return true;
      if (of.includes('plan_review') && ['plan_review', 'plan_review_building', 'plan_review_planning'].includes(l.id)) return true;
      if (of.includes('trades') && ['trades', 'electrical', 'plumbing', 'mechanical'].includes(l.id)) return true;
      if (of.includes('energy_npdes') && ['energy', 'npdes'].includes(l.id)) return true;
      return false;
    })
    .reduce((sum, l) => sum + l.amount, 0);
}

// ── City-slug resolution ──
export function resolveFeeCity(rawCity) {
  if (!rawCity) return { slug: null, displayName: 'that city' };
  const normalized = rawCity.trim().toLowerCase().replace(/_/g, '-');
  const compact = normalized.replace(/[^a-z0-9]/g, '');
  if (/^(laguna-?beach|lagunabeach(ca|california)?|cityoflagunabeach(ca|california)?)$/.test(compact) || normalized === 'laguna-beach')
    return { slug: 'laguna-beach', displayName: 'Laguna Beach' };
  if (/^(buena-?park|buenapark(ca|california)?|cityofbuenapark(ca|california)?)$/.test(compact) || normalized === 'buena-park')
    return { slug: 'buena-park', displayName: 'Buena Park' };
  if (/^(newport-?beach|newportbeach(ca|california)?|cityofnewportbeach(ca|california)?)$/.test(compact) || normalized === 'newport-beach')
    return { slug: 'newport-beach', displayName: 'Newport Beach' };
  if (/^(costa-?mesa|costamesa(ca|california)?|cityofcostamesa(ca|california)?)$/.test(compact) || normalized === 'costa-mesa')
    return { slug: 'costa-mesa', displayName: 'Costa Mesa' };
  if (/^(anaheim|anaheim(ca|california)?|cityofanaheim(ca|california)?)$/.test(compact) || normalized === 'anaheim')
    return { slug: 'anaheim', displayName: 'Anaheim' };
  const titled = rawCity
    .trim()
    .split(/[\s-]+/)
    .filter(Boolean)
    .map((p) => p.charAt(0).toUpperCase() + p.slice(1).toLowerCase())
    .join(' ');
  return { slug: normalized.replace(/\s+/g, '-'), displayName: titled };
}

export function hasFeeSchedule(slug) {
  return !!slug && FEE_CITIES.includes(slug);
}
