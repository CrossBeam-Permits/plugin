// GENERATED FILE. Do not edit by hand; the plugin publisher overwrites it.
// A copy of a module the shared CrossBeam fee calculator imports. The code is unchanged.
/**
 * icc-bvd.mjs — the ICC Building Valuation Data table and the one calculation
 * that turns a project's new area into an ICC valuation figure.
 *
 * ICC is national, so the table lives here once for every city. A city's fee
 * schedule decides whether and how it applies (`valuation.minimum_icc_bvd`):
 * which permit types carry new square footage, and any documented counter
 * practice such as pricing a conversion at a share of the R-3 rate. No city
 * names appear in this file.
 *
 * Ships beside fee-calc.mjs, which imports it. Pure: no I/O, no imports.
 */

/** Construction types in the table's column order, as the building code writes them. */
export const ICC_CONSTRUCTION_TYPES = ['I-A', 'I-B', 'II-A', 'II-B', 'III-A', 'III-B', 'IV', 'V-A', 'V-B'];

/**
 * ICC Building Valuation Data, August 2026, "Square Foot Construction Costs"
 * ($/sq ft, 2024 IBC groups). One row per table row, rates in
 * ICC_CONSTRUCTION_TYPES order; null is the table's "N.P." (not permitted).
 * Source: the ICC's published August 2026 edition. The next edition
 * is due February 2027. Footnotes: private garages use U (a, modeled as the
 * garage line); shell-only buildings deduct 20 percent (b) and unfinished R-3
 * basements are $31.50/sq ft (d), neither modeled. The table does not apply
 * to alterations or repairs of existing buildings.
 */
export const ICC_BVD = {
  edition: '2026-08',
  label: 'ICC Building Valuation Data, August 2026',
  short_label: 'Aug 2026 ICC table',
  rows: {
    'A-1-stage': { label: 'A-1 Assembly, theaters, with stage', rates: [360.96, 348.39, 337.35, 324.27, 303.54, 294.94, 313.17, 283.31, 272.34] },
    'A-1': { label: 'A-1 Assembly, theaters, without stage', rates: [331.90, 319.33, 308.29, 295.21, 274.24, 265.63, 284.12, 254.01, 243.04] },
    'A-2-nightclub': { label: 'A-2 Assembly, nightclubs', rates: [281.26, 272.80, 264.60, 254.37, 238.42, 231.98, 245.62, 216.53, 208.41] },
    'A-2': { label: 'A-2 Assembly, restaurants, bars, banquet halls', rates: [280.26, 271.80, 262.60, 253.37, 236.42, 230.98, 244.62, 214.53, 207.41] },
    'A-3-church': { label: 'A-3 Assembly, churches', rates: [335.11, 322.54, 311.50, 298.42, 277.94, 269.33, 287.32, 257.71, 246.74] },
    'A-3': { label: 'A-3 Assembly, general, community halls, libraries, museums', rates: [278.93, 266.35, 254.32, 242.24, 220.51, 212.90, 231.14, 200.28, 190.31] },
    'A-4': { label: 'A-4 Assembly, arenas', rates: [330.90, 318.33, 306.29, 294.21, 272.24, 264.63, 283.12, 252.01, 242.04] },
    B: { label: 'B Business', rates: [312.15, 300.92, 289.96, 277.56, 252.72, 243.79, 266.86, 225.87, 215.44] },
    E: { label: 'E Educational', rates: [298.97, 288.31, 278.58, 266.87, 247.78, 235.15, 257.69, 216.87, 209.85] },
    'F-1': { label: 'F-1 Factory and industrial, moderate hazard', rates: [171.67, 163.34, 153.02, 147.14, 131.07, 124.79, 140.28, 110.60, 101.94] },
    'F-2': { label: 'F-2 Factory and industrial, low hazard', rates: [170.67, 162.34, 153.02, 146.14, 131.07, 123.79, 139.28, 110.60, 100.94] },
    'H-1': { label: 'H-1 High Hazard, explosives', rates: [160.14, 151.81, 142.49, 135.61, 120.87, 113.59, 128.75, 100.40, null] },
    'H-2-4': { label: 'H-2, H-3, H-4 High Hazard', rates: [160.14, 151.81, 142.49, 135.61, 120.87, 113.59, 128.75, 100.40, 90.74] },
    'H-5': { label: 'H-5 HPM', rates: [312.15, 300.92, 289.96, 277.56, 252.72, 243.79, 266.86, 225.87, 215.44] },
    'I-1': { label: 'I-1 Institutional, supervised environment', rates: [286.01, 275.76, 265.91, 255.86, 234.19, 227.89, 255.32, 210.91, 203.38] },
    'I-2': { label: 'I-2 Institutional, hospitals', rates: [489.97, 478.73, 467.77, 455.38, 429.56, null, 444.67, 402.71, null] },
    'I-2-nursing': { label: 'I-2 Institutional, nursing homes', rates: [338.00, 326.76, 315.81, 303.41, 280.56, null, 292.71, 253.71, null] },
    'I-3': { label: 'I-3 Institutional, restrained', rates: [329.08, 317.84, 306.89, 294.49, 272.63, 262.70, 283.79, 266.32, 233.35] },
    'I-4': { label: 'I-4 Institutional, day care facilities', rates: [286.01, 275.76, 265.91, 255.86, 234.19, 227.89, 255.32, 210.91, 203.38] },
    M: { label: 'M Mercantile', rates: [209.97, 201.51, 192.31, 183.08, 166.72, 161.29, 174.33, 144.83, 137.71] },
    'R-1': { label: 'R-1 Residential, hotels', rates: [289.33, 279.08, 269.24, 259.18, 237.00, 230.71, 258.65, 213.72, 206.19] },
    'R-2': { label: 'R-2 Residential, multiple family', rates: [241.56, 231.31, 221.47, 211.41, 190.52, 184.22, 210.88, 167.24, 159.71] },
    'R-3': { label: 'R-3 Residential, one- and two-family dwellings', rates: [226.80, 220.77, 215.47, 210.87, 203.82, 196.56, 215.12, 189.52, 177.63] },
    'R-4': { label: 'R-4 Residential, care/assisted living facilities', rates: [286.01, 275.76, 265.91, 255.86, 234.19, 227.89, 255.32, 210.91, 203.38] },
    'S-1': { label: 'S-1 Storage, moderate hazard', rates: [159.14, 150.81, 140.49, 134.61, 118.87, 112.59, 127.75, 98.40, 89.74] },
    'S-2': { label: 'S-2 Storage, low hazard', rates: [158.14, 149.81, 140.49, 133.61, 118.87, 111.59, 126.75, 98.40, 88.74] },
    U: { label: 'U Utility, miscellaneous (private garages)', rates: [126.44, 119.24, 110.43, 105.97, 94.40, 88.43, 100.90, 75.13, 71.79] },
  },
};

/** The occupancy row ids a capture may name, in table order. */
export const ICC_OCCUPANCY_GROUPS = Object.keys(ICC_BVD.rows);

/**
 * The February 2026 edition, for a city whose valuation calculator has not
 * loaded the August one yet (a schedule's `minimum_icc_bvd.edition`). Same
 * rows and N.P. cells as August. Source: the ICC table as a city building
 * department reposted it (ICC's own copy is members-only).
 */
const FEBRUARY_2026_RATES = {
    'A-1-stage': [357.33, 344.89, 333.96, 321.01, 300.49, 291.98, 310.03, 280.47, 269.61],
    'A-1': [328.57, 316.12, 305.20, 292.25, 271.49, 262.97, 281.27, 251.46, 240.61],
    'A-2-nightclub': [277.44, 269.30, 260.84, 250.89, 234.99, 228.61, 242.28, 213.69, 205.58],
    'A-2': [276.44, 268.30, 258.84, 249.89, 232.99, 227.61, 241.28, 211.69, 204.58],
    'A-3-church': [331.74, 319.29, 308.36, 295.42, 275.14, 266.62, 284.43, 255.12, 244.26],
    'A-3': [276.12, 263.67, 251.75, 239.80, 218.28, 210.76, 228.82, 198.26, 188.40],
    'A-4': [327.57, 315.12, 303.20, 291.25, 269.49, 261.97, 280.27, 249.46, 239.61],
    'B': [309.01, 297.89, 287.04, 274.77, 250.17, 241.34, 264.17, 223.59, 213.27],
    'E': [296.02, 285.47, 275.84, 264.24, 245.34, 232.84, 255.15, 214.74, 207.79],
    'F-1': [169.11, 160.95, 150.84, 145.13, 129.25, 122.95, 138.37, 107.18, 99.77],
    'F-2': [168.11, 159.95, 150.84, 144.13, 129.25, 121.95, 137.37, 107.18, 98.77],
    'H-1': [157.75, 149.59, 140.48, 133.77, 119.20, 111.90, 127.00, 97.13, null],
    'H-2-4': [157.75, 149.59, 140.48, 133.77, 119.20, 111.90, 127.00, 97.13, 88.73],
    'H-5': [309.01, 297.89, 287.04, 274.77, 250.17, 241.34, 264.17, 223.59, 213.27],
    'I-1': [283.25, 273.10, 263.35, 253.39, 231.93, 225.70, 252.86, 208.88, 201.43],
    'I-2': [485.04, 473.91, 463.07, 450.80, 425.24, null, 440.20, 398.66, null],
    'I-2-nursing': [334.61, 323.48, 312.64, 300.37, 277.75, null, 289.77, 251.17, null],
    'I-3': [325.77, 314.64, 303.80, 291.53, 269.89, 260.06, 280.93, 263.64, 230.99],
    'I-4': [283.25, 273.10, 263.35, 253.39, 231.93, 225.70, 252.86, 208.88, 201.43],
    'M': [207.08, 198.94, 189.48, 180.53, 164.30, 158.91, 171.92, 143.00, 135.89],
    'R-1': [286.53, 276.38, 266.63, 256.68, 234.71, 228.48, 256.15, 211.66, 204.20],
    'R-2': [239.24, 229.09, 219.34, 209.38, 188.69, 182.45, 208.85, 165.63, 158.18],
    'R-3': [224.62, 218.65, 213.40, 208.84, 201.86, 194.67, 213.06, 187.70, 175.92],
    'R-4': [283.25, 273.10, 263.35, 253.39, 231.93, 225.70, 252.86, 208.88, 201.43],
    'S-1': [156.75, 148.59, 138.48, 132.77, 117.20, 110.90, 126.00, 95.13, 87.73],
    'S-2': [155.75, 147.59, 138.48, 131.77, 117.20, 109.90, 125.00, 95.13, 86.73],
    'U': [125.18, 118.05, 109.33, 104.91, 93.46, 87.55, 99.89, 74.38, 71.07],
};

/** Every edition on file, by id. `ICC_BVD` is the latest. */
export const ICC_BVD_EDITIONS = {
  [ICC_BVD.edition]: ICC_BVD,
  '2026-02': {
    edition: '2026-02',
    label: 'ICC Building Valuation Data, February 2026',
    short_label: 'Feb 2026 ICC table',
    rows: Object.fromEntries(ICC_OCCUPANCY_GROUPS.map((id) => [id, { label: ICC_BVD.rows[id].label, rates: FEBRUARY_2026_RATES[id] }])),
  },
};

/**
 * An applicant figure more than this share under the ICC figure is flagged
 * for the screener. A flag never changes the figure the fees use.
 */
export const ICC_FLAG_BAND = 0.3;

const DEFAULT_CONSTRUCTION_TYPE = 'V-B';

/**
 * How much of a remodel the work touches, as building departments grade it
 * when they value an alteration from the new-construction rate. A city's rule
 * sets the share of the ICC rate for each (`minimum_icc_bvd.alteration.extents`),
 * or one flat share (`alteration.factor`) when its own valuations use one, with
 * a different share for a permit type its valuations treat differently
 * (`alteration.permit_type_factors`, e.g. an ADU made inside existing living space).
 */
export const ALTERATION_EXTENTS = ['minor', 'medium', 'major', 'full'];

/**
 * A construction type as the table's column id ('V-B'), or null. Accepts the
 * spellings a code-data block uses: "Type V-B", "VB", "V B", "5-B". Every
 * Type IV variant (IV-A, IV-B, IV-C, IV-HT) is the table's one IV column.
 */
export function normalizeConstructionType(value) {
  if (typeof value !== 'string') return null;
  let compact = value.toUpperCase().replace(/^\s*TYPE\s*/, '').replace(/[\s._-]/g, '');
  compact = compact.replace(/^([1-5])/, (digit) => ['I', 'II', 'III', 'IV', 'V'][Number(digit) - 1]);
  if (compact.startsWith('IV')) return 'IV';
  const match = /^(I{1,3}|V)([AB])$/.exec(compact);
  return match ? `${match[1]}-${match[2]}` : null;
}

/**
 * An occupancy group as a table row id, or null. A row id passes through. A
 * bare group with several rows takes its general row: A-1 without stage, A-2
 * restaurants and bars, A-3 general, I-2 hospitals; H-2, H-3 and H-4 share a row.
 */
export function iccOccupancyRow(value) {
  if (typeof value !== 'string') return null;
  const trimmed = value.trim();
  if (ICC_BVD.rows[trimmed]) return trimmed;
  const compact = trimmed.toUpperCase().replace(/^(GROUP|OCCUPANCY)\s+/, '').replace(/\s+/g, '');
  const match = /^([ABEFHIMRSU])-?(\d)?$/.exec(compact);
  if (!match) return null;
  const [, letter, digit] = match;
  if (letter === 'H' && ['2', '3', '4'].includes(digit)) return 'H-2-4';
  const id = digit ? `${letter}-${digit}` : letter;
  return ICC_BVD.rows[id] ? id : null;
}

/** $/sq ft for an occupancy row and construction type, or null when unknown or N.P. */
export function iccRate(occupancy, constructionType, edition = ICC_BVD.edition) {
  const row = (ICC_BVD_EDITIONS[edition] ?? ICC_BVD).rows[iccOccupancyRow(occupancy) ?? ''];
  const column = ICC_CONSTRUCTION_TYPES.indexOf(normalizeConstructionType(constructionType) ?? '');
  if (!row || column < 0) return null;
  return row.rates[column];
}

function area(value) {
  return typeof value === 'number' && Number.isFinite(value) && value >= 0 ? value : null;
}

function round2(value) {
  return Math.round(value * 100) / 100;
}

/**
 * Validate a schedule's `valuation.minimum_icc_bvd` block. Throws on a shape
 * the calculation cannot use.
 */
export function validateIccMinimum(rule) {
  if (rule === undefined || rule === null) return;
  if (typeof rule !== 'object' || typeof rule.enabled !== 'boolean')
    throw new Error('valuation.minimum_icc_bvd requires enabled: true|false');
  if (rule.permit_types !== undefined && !Array.isArray(rule.permit_types))
    throw new Error('valuation.minimum_icc_bvd.permit_types must be a list');
  if (rule.prices_on !== undefined && !['applicant', 'higher'].includes(rule.prices_on))
    throw new Error('valuation.minimum_icc_bvd.prices_on must be applicant or higher');
  if (rule.edition !== undefined && !ICC_BVD_EDITIONS[rule.edition])
    throw new Error(`valuation.minimum_icc_bvd.edition must be one of ${Object.keys(ICC_BVD_EDITIONS).join(', ')}`);
  if (rule.multiplier !== undefined && !(typeof rule.multiplier === 'number' && rule.multiplier > 0 && rule.multiplier <= 5))
    throw new Error('valuation.minimum_icc_bvd.multiplier must be a number above 0 and at most 5');
  if (rule.default_construction_type !== undefined && !normalizeConstructionType(rule.default_construction_type))
    throw new Error(`valuation.minimum_icc_bvd.default_construction_type ${rule.default_construction_type} is not an ICC construction type`);
  validateAlteration(rule.alteration);
  validateUnitCosts(rule.unit_costs);
  for (const key of ['conversion', 'site_work']) {
    const practice = rule[key];
    if (practice === undefined) continue;
    if (!practice || !iccOccupancyRow(practice.occupancy) || !practice.cite)
      throw new Error(`valuation.minimum_icc_bvd.${key} requires an ICC occupancy and a cite`);
    if (practice.factor !== undefined && !(typeof practice.factor === 'number' && practice.factor > 0 && practice.factor <= 1))
      throw new Error(`valuation.minimum_icc_bvd.${key}.factor must be a number above 0 and at most 1`);
  }
}

function validateAlteration(alteration) {
  if (alteration === undefined) return;
  if (!alteration || !alteration.cite || (alteration.factor === undefined) === (typeof alteration.extents !== 'object'))
    throw new Error('valuation.minimum_icc_bvd.alteration requires a cite and either extents or one factor');
  if (alteration.factor !== undefined) {
    if (!(typeof alteration.factor === 'number' && alteration.factor > 0 && alteration.factor <= 1))
      throw new Error('valuation.minimum_icc_bvd.alteration.factor must be a number above 0 and at most 1');
    validatePermitTypeFactors(alteration.permit_type_factors);
  } else if (alteration.permit_type_factors !== undefined) {
    throw new Error('valuation.minimum_icc_bvd.alteration.permit_type_factors needs a flat factor');
  } else validateAlterationExtents(alteration);
  if (alteration.permit_types !== undefined && (!Array.isArray(alteration.permit_types) || alteration.permit_types.some((type) => typeof type !== 'string' || type === '')))
    throw new Error('valuation.minimum_icc_bvd.alteration.permit_types must be a list of permit types');
}

function validatePermitTypeFactors(byType) {
  if (byType === undefined) return;
  if (!byType || typeof byType !== 'object') throw new Error('valuation.minimum_icc_bvd.alteration.permit_type_factors must map permit types to { factor, cite }');
  for (const [permitType, entry] of Object.entries(byType)) {
    if (!(typeof entry?.factor === 'number' && entry.factor > 0 && entry.factor <= 1) || !entry.cite)
      throw new Error(`valuation.minimum_icc_bvd.alteration.permit_type_factors.${permitType} needs a factor above 0 and at most 1 and a cite`);
  }
}

function validateAlterationExtents(alteration) {
  for (const [extent, share] of Object.entries(alteration.extents)) {
    if (!ALTERATION_EXTENTS.includes(extent)) throw new Error(`valuation.minimum_icc_bvd.alteration extent ${extent} is not one of ${ALTERATION_EXTENTS.join(', ')}`);
    if (!(typeof share === 'number' && share > 0 && share <= 1)) throw new Error(`valuation.minimum_icc_bvd.alteration.extents.${extent} must be a number above 0 and at most 1`);
  }
  if (!(alteration.default_extent in alteration.extents))
    throw new Error('valuation.minimum_icc_bvd.alteration.default_extent must name one of its extents');
}

/** Where a unit cost comes from, in the order a city's schedule should prefer them. */
export const UNIT_COST_SOURCES = ['city_practice', 'city_history', 'published_table', 'industry'];

function validRange(range) {
  return Array.isArray(range) && range.length === 2 && range.every((value) => typeof value === 'number' && value >= 0) && range[0] <= range[1];
}

/**
 * Validate `minimum_icc_bvd.unit_costs`: the scope the ICC table has no row
 * for (a pool, grading, a deck, an exterior-only renovation), each priced by
 * exactly one of `rate` (dollars per unit), `bands` (a typical valuation by
 * quantity) or `calculator_share` (a share of the record's calculator rate),
 * with its source named. Throws on a shape the estimate cannot use.
 */
function validateUnitCosts(items) {
  if (items === undefined) return;
  if (!Array.isArray(items)) throw new Error('valuation.minimum_icc_bvd.unit_costs must be a list');
  const seen = new Set();
  for (const item of items) {
    const path = `valuation.minimum_icc_bvd.unit_costs.${item?.id ?? '?'}`;
    if (!item?.id || !item.label || !item.input || !item.unit || !item.cite || !item.source_label)
      throw new Error(`${path} requires id, label, input, unit, source_label and cite`);
    if (seen.has(item.id)) throw new Error(`${path} is listed twice`);
    seen.add(item.id);
    if (!UNIT_COST_SOURCES.includes(item.source)) throw new Error(`${path}.source must be one of ${UNIT_COST_SOURCES.join(', ')}`);
    const methods = ['rate', 'bands', 'calculator_share'].filter((key) => item[key] !== undefined);
    if (methods.length !== 1) throw new Error(`${path} needs exactly one of rate, bands or calculator_share`);
    if (item.rate !== undefined && !(typeof item.rate === 'number' && item.rate > 0)) throw new Error(`${path}.rate must be a number above 0`);
    if (item.calculator_share !== undefined && !(typeof item.calculator_share === 'number' && item.calculator_share > 0 && item.calculator_share <= 1))
      throw new Error(`${path}.calculator_share must be a number above 0 and at most 1`);
    if (item.range !== undefined && (item.rate === undefined || !validRange(item.range) || item.rate < item.range[0] || item.rate > item.range[1]))
      throw new Error(`${path}.range is a [low, high] rate around rate`);
    if (item.bands !== undefined) {
      if (!Array.isArray(item.bands) || !item.bands.length) throw new Error(`${path}.bands must be a non-empty list`);
      item.bands.forEach((band, index) => {
        const last = index === item.bands.length - 1;
        if (!(typeof band?.amount === 'number' && band.amount > 0)) throw new Error(`${path}.bands[${index}].amount must be a number above 0`);
        if (last ? band.up_to !== null : !(typeof band.up_to === 'number' && band.up_to > (item.bands[index - 1]?.up_to ?? 0)))
          throw new Error(`${path}.bands must rise, the last one up_to: null`);
        if (band.range !== undefined && !validRange(band.range)) throw new Error(`${path}.bands[${index}].range must be [low, high]`);
      });
    }
  }
}

/**
 * The unit-cost lines for one record: each `unit_costs` item whose quantity
 * the record carries, at its rate, band or share of the calculator rate.
 * A line is an estimate for staff: it never feeds the fees.
 */
function unitCostLines(rule, quantityOf, permitType, calculatorRate) {
  const lines = [];
  for (const item of rule.unit_costs ?? []) {
    const quantity = quantityOf(item.input);
    if (!(typeof quantity === 'number' && quantity > 0)) continue;
    let rate = null;
    let amount;
    let range = null;
    let band = null;
    if (item.bands) {
      band = item.bands.find((entry) => entry.up_to === null || quantity <= entry.up_to);
      amount = band.amount;
      range = band.range ? [...band.range] : null;
    } else if (item.calculator_share !== undefined) {
      if (calculatorRate === null) continue;
      rate = round2(calculatorRate * item.calculator_share);
      amount = round2(quantity * rate);
    } else {
      rate = item.rate;
      amount = round2(quantity * rate);
      range = item.range ? [round2(quantity * item.range[0]), round2(quantity * item.range[1])] : null;
    }
    lines.push({
      id: item.id,
      label: item.label,
      input: item.input,
      quantity,
      unit: item.unit,
      rate,
      calculatorShare: item.calculator_share ?? null,
      calculatorRate: item.calculator_share !== undefined ? calculatorRate : null,
      bandUpTo: band ? band.up_to : null,
      bandFloor: band ? (item.bands[item.bands.indexOf(band) - 1]?.up_to ?? 0) : null,
      amount,
      low: range ? range[0] : amount,
      high: range ? range[1] : amount,
      source: item.source,
      sourceLabel: item.source_label,
      cite: item.cite,
      note: item.note ?? null,
      ownApplication: item.own_application ?? null,
    });
  }
  return lines;
}

/** The occupancy row a record's new area takes when the packet names none. */
export function defaultIccOccupancy(permitType) {
  if (permitType === 'detached-garage') return 'U';
  if (permitType === 'commercial-ti') return 'B';
  return 'R-3';
}

/** Area × ICC rate; an unknown construction type takes V-B, an unknown occupancy R-3. */
export function valuationFromArea(areaSqft, occupancy = 'R-3', constructionType = DEFAULT_CONSTRUCTION_TYPE) {
  const rate = iccRate(occupancy, constructionType) ?? iccRate(occupancy, DEFAULT_CONSTRUCTION_TYPE) ?? iccRate('R-3', DEFAULT_CONSTRUCTION_TYPE);
  return { valuation: round2(areaSqft * rate), rate };
}

/**
 * One ICC line as text: "2,793 sq ft at $177.63/sq ft (R-3, V-B)", with "× 50%"
 * for a factored line and the city's multiplier when it has one:
 * "999 sq ft at $351.84/sq ft (R-3, V-B; 2 × ICC $175.92)".
 */
export function iccLineMath(line) {
  const factor = line.factor !== 1 ? ` × ${Math.round(line.factor * 100)}%` : '';
  const multiplier = line.multiplier !== 1 ? `; ${line.multiplier} × ICC $${line.iccRate.toFixed(2)}` : '';
  return `${line.sqft.toLocaleString('en-US')} sq ft at $${line.rate.toFixed(2)}/sq ft${factor} (${line.occupancy}, ${line.constructionType}${multiplier})`;
}

/** The remodel estimate applies to the permit types the block names, or, with no list, to a type that is not new square footage. */
function alterationApplies(rule, permitType, newAreaType) {
  if (!rule.alteration) return false;
  return Array.isArray(rule.alteration.permit_types) ? rule.alteration.permit_types.includes(permitType) : !newAreaType;
}

/**
 * The ICC valuation figure for one City record, or null when the schedule
 * applies no ICC minimum.
 *
 * Lines, each from the captured facts:
 *   - new: new area at the record's occupancy and construction type, for a
 *     permit type the schedule lists as new square footage. The area is
 *     `iccNewAreaSqft`; without it, the new floor area (or the ADU's area)
 *     less the captured garage and, for an ADU's area, the converted part
 *     and any interior alteration already priced on its own line.
 *   - garage: new private garage area at U (ICC footnote a).
 *   - conversion: existing non-habitable area made habitable, at the
 *     schedule's occupancy × factor (a documented counter practice).
 *   - site_work: hardscape area at the schedule's site-work occupancy.
 *   - alteration: remodeled existing area at the record's occupancy × the
 *     share the schedule sets for the extent of the work (an estimate, the way
 *     building departments value a remodel; the ICC table itself prices none).
 *     Only a permit type the alteration block lists, or, with no list, a type
 *     that is not new square footage. A re-roof, tenant improvement or repair
 *     stays "no ICC figure" when the list does not name it.
 *
 * `unitLines` price the scope the ICC table has no row for, from the
 * schedule's `unit_costs` (a pool by water area, grading by cubic yards, a
 * deck, an exterior-only renovation), each with its source. They are an
 * estimate for staff: `total`, the figure the fees can use, leaves them out,
 * and `estimateTotal` (with `estimateLow` and `estimateHigh`) adds them in.
 *
 * `reason` says why there is no figure: 'not_new_area' for work the table does
 * not price, 'no_new_area' when the packet shows zero new area, 'needs_area'
 * for a new-area record with no area captured yet. `partial` is true when the
 * figure is site work alone: the application's valuation also covers the
 * building work, so the figure says nothing about the whole valuation.
 */
export function iccValuation(rule, inputs, permitType, quantityOf = (id) => inputs.scopeQuantities?.[id] ?? null) {
  if (rule?.enabled !== true) return null;
  const captured = normalizeConstructionType(inputs.constructionType);
  const constructionType = captured ?? normalizeConstructionType(rule.default_construction_type) ?? DEFAULT_CONSTRUCTION_TYPE;
  const capturedOccupancy = iccOccupancyRow(inputs.occupancy);
  const occupancy = capturedOccupancy ?? defaultIccOccupancy(permitType);
  const newAreaType = !rule.permit_types?.length || rule.permit_types.includes(permitType);
  const alterationType = alterationApplies(rule, permitType, newAreaType);
  const garage = area(inputs.iccGarageAreaSqft);
  const conversion = area(inputs.iccConversionAreaSqft);
  const hardscape = area(inputs.iccHardscapeAreaSqft);
  const remodeled = area(inputs.iccAlterationAreaSqft);
  // A flat share needs no extent; graded extents fall back to the rule's default.
  const extents = rule.alteration?.extents ?? null;
  const capturedExtent = extents && inputs.alterationExtent in extents ? inputs.alterationExtent : null;
  const extent = extents ? capturedExtent ?? rule.alteration.default_extent : null;

  let newArea = null;
  let newAreaSource = null;
  if (newAreaType) {
    newArea = area(inputs.iccNewAreaSqft);
    newAreaSource = newArea === null ? null : 'captured';
    if (newArea === null) {
      const floorArea = area(inputs.newFloorAreaSqft);
      const aduArea = floorArea === null ? area(inputs.aduSqft) : null;
      const total = floorArea ?? aduArea;
      if (total !== null) {
        newArea = Math.max(0, total - (garage ?? 0) - (aduArea !== null ? (conversion ?? 0) + (remodeled ?? 0) : 0));
        newAreaSource = floorArea !== null ? 'new_floor_area' : 'adu_area';
      }
    }
  }

  const edition = ICC_BVD_EDITIONS[rule.edition] ?? ICC_BVD;
  const multiplier = rule.multiplier ?? 1;
  const lines = [];
  const notPermitted = [];
  const push = (kind, sqft, rowId, factor, basis, cite, lineExtent = null) => {
    if (!(sqft > 0)) return;
    const nationalRate = iccRate(rowId, constructionType, edition.edition);
    if (nationalRate === null) {
      notPermitted.push({ kind, occupancy: rowId, constructionType });
      return;
    }
    lines.push({
      kind,
      occupancy: rowId,
      constructionType,
      sqft,
      rate: round2(nationalRate * multiplier),
      iccRate: nationalRate,
      multiplier,
      factor,
      amount: round2(sqft * round2(nationalRate * multiplier) * factor),
      basis,
      cite: cite ?? null,
      extent: lineExtent,
    });
  };
  if (newAreaType) {
    push('new', newArea, occupancy, 1, 'icc', rule.cite);
    push('garage', garage, 'U', 1, 'icc', rule.cite);
  }
  if (rule.conversion) push('conversion', conversion, iccOccupancyRow(rule.conversion.occupancy), rule.conversion.factor ?? 1, 'city_practice', rule.conversion.cite);
  if (rule.site_work) push('site_work', hardscape, iccOccupancyRow(rule.site_work.occupancy), rule.site_work.factor ?? 1, 'city_practice', rule.site_work.cite);
  if (alterationType) {
    const byType = extents ? null : rule.alteration.permit_type_factors?.[permitType] ?? null;
    const factor = extents ? extents[extent] : byType?.factor ?? rule.alteration.factor;
    push('alteration', remodeled, occupancy, factor, 'estimate', byType?.cite ?? rule.alteration.cite, extent);
  }

  const total = round2(lines.reduce((sum, line) => sum + line.amount, 0));
  const nationalRecordRate = iccRate(occupancy, constructionType, edition.edition);
  const unitLines = unitCostLines(rule, quantityOf, permitType, nationalRecordRate === null ? null : round2(nationalRecordRate * multiplier));
  const unitTotal = round2(unitLines.reduce((sum, line) => sum + line.amount, 0));
  const areaKnown = [inputs.iccNewAreaSqft, inputs.newFloorAreaSqft, inputs.aduSqft, inputs.iccGarageAreaSqft, inputs.iccConversionAreaSqft, inputs.iccHardscapeAreaSqft, inputs.iccAlterationAreaSqft]
    .some((value) => typeof value === 'number' && Number.isFinite(value));
  let reason = null;
  if (!lines.length) {
    if (newAreaType) reason = areaKnown ? 'no_new_area' : 'needs_area';
    else reason = alterationType && remodeled === null ? 'needs_alteration_area' : 'not_new_area';
  }
  return {
    edition: edition.edition,
    editionLabel: edition.short_label,
    multiplier,
    constructionType,
    constructionTypeAssumed: captured === null,
    occupancy,
    occupancyAssumed: capturedOccupancy === null,
    newAreaSource,
    lines,
    notPermitted,
    total,
    partial: lines.length > 0 && lines.every((line) => line.kind === 'site_work'),
    estimated: lines.some((line) => line.basis === 'estimate'),
    extentAssumed: extents !== null && lines.some((line) => line.kind === 'alteration') && capturedExtent === null,
    reason,
    unitLines,
    estimateTotal: round2(total + unitTotal),
    estimateLow: round2(total + unitLines.reduce((sum, line) => sum + line.low, 0)),
    estimateHigh: round2(total + unitLines.reduce((sum, line) => sum + line.high, 0)),
  };
}

/**
 * The applicant's figure beside the ICC figure. Null when there is no ICC figure.
 *
 * `uses` is the figure the fees use: the applicant's whenever one is stated,
 * unless the schedule's rule says `prices_on: higher` and the ICC figure is
 * higher. With no applicant figure the ICC figure fills in, unless it is
 * `partial` (it would price part of the work as the whole), then null. An
 * `estimated` figure (a remodel graded by extent) never raises a stated one.
 * `flag` marks an applicant figure more than ICC_FLAG_BAND under the ICC
 * figure; a partial figure is never flagged. A figure well above it is not
 * flagged: on real screens that is an addition whose valuation also covers
 * remodel work, not a problem for the screener.
 */
export function compareToIcc(applicant, icc, rule = null) {
  if (!icc || !(icc.total > 0)) return null;
  const stated = typeof applicant === 'number' && applicant > 0 ? applicant : null;
  let uses = 'applicant';
  if (stated === null) uses = icc.partial ? null : 'icc';
  else if (rule?.prices_on === 'higher' && !icc.partial && !icc.estimated && stated < icc.total) uses = 'icc';
  return { applicant: stated, icc: icc.total, uses, ...compareFigures(stated, icc.total, icc.partial) };
}

/**
 * The applicant's figure as a share of a comparison figure (floored to 0.1%),
 * and `flag: 'under'` when it is more than ICC_FLAG_BAND under it. Compared in
 * cents. A `partial` figure (site work alone) is never flagged.
 */
export function compareFigures(applicant, figure, partial = false) {
  if (applicant === null || !(figure > 0)) return { ratio: null, flag: null };
  const cents = (value) => Math.round(value * 100);
  const band = Math.round(ICC_FLAG_BAND * 100);
  const under = !partial && cents(applicant) * 100 < cents(figure) * (100 - band);
  return { ratio: Math.floor((applicant / figure) * 1000) / 1000, flag: under ? 'under' : null };
}
