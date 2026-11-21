// Run: node test.mjs
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import './data/research.js';
import './roman.js';
const { analyse } = globalThis.RomanReader;

const cases = [
  // input, options, expected top value (or null to skip), values that must appear somewhere
  ['MCMLXXXIV', {}, 1984, []],
  ['mmxxvi', { period: 'modern' }, 2026, []],
  ['IIII', {}, 4, []],
  ['VIIII', {}, 9, []],
  ['XIIX', { period: 'late-medieval' }, 18, []],
  ['IIC', {}, null, [98, 200]],
  ['iiᵐvᶜxxiiij', {}, 2524, []],
  ['ii^m v^c xxiiij', {}, 2524, []],
  ['iiijˣˣ', {}, 80, []],
  ['iiijxx', {}, null, [80]],
  ['CIↃIↃCXXIV', {}, 1624, []],
  ['(I)', {}, 1000, []],
  ['((I))', {}, 10000, []],
  ['I))', {}, 5000, []],
  ['X̅V', { period: 'classical' }, 10005, [15]],
  ['_XV', { period: 'classical' }, 10005, [15]],
  ['|X̅|', {}, 1000000, []],
  ['Mᵒccccᵒlxxv', {}, 1475, []],
  ['.xx.', {}, 20, []],
  ['xin', { period: 'late-medieval' }, 13, []],
  ['IC', {}, null, [99]],
  ['Ⅻ', {}, 12, []],
  ['Mᵒiiijᶜlvj', { period: 'late-medieval' }, 1456, []],
  ['MMXIIᶜlx', { period: 'late-medieval' }, 3260, []],
  ['X̅V', { period: 'late-medieval' }, 15, [10005]],
  ['|(I)|', { period: 'classical' }, 100000000, []],
  ['|ↀ|', { period: 'classical' }, 100000000, []],
  ['.iiij.xx.', { period: 'late-medieval' }, 80, [24]],
  ['IX.XX.XVI', { period: 'late-medieval' }, 196, []],
  ['ↆ', { period: 'classical' }, 50, []],
  ['ↅ', { period: 'early-medieval' }, 6, []],
];

let fail = 0;
for (const [input, opts, top, must] of cases) {
  const r = analyse(input, opts);
  const vals = r.readings.map(x => x.value);
  const ok = (top === null || vals[0] === top) && must.every(m => vals.includes(m));
  if (!ok) { fail++; console.log('FAIL', input, '→', vals, r.readings.map(x => x.explanation)); }
  else console.log('ok  ', input.padEnd(16), '→', vals.slice(0, 4).join(', '));
}

const checks = [
  ['decimal input gives the standard Roman form and relevant alternatives', () => {
    const forms = input => analyse(input).conversion?.forms.map(form => form.numeral);
    assert.deepEqual(forms('2026'), ['MMXXVI']);
    assert.deepEqual(forms(' 01999 '), ['MCMXCIX', 'MDCCCCLXXXXVIIII']);
    assert.deepEqual(forms('4'), ['IV', 'IIII']);
    assert.equal(analyse('4').conversion.forms[1].clock, true);
  }],
  ['decimal conversion uses an overbar beyond the usual range and handles unsupported values', () => {
    const result = analyse('4001');
    assert.equal(result.conversion?.forms[0].numeral, 'I̅V̅I');
    assert.equal(result.conversion.forms[0].convention, 'vinculum');
    assert(result.conversion.forms.every(form =>
      analyse(form.numeral, { period: 'classical' }).readings.some(reading => reading.value === 4001)));
    for (const input of ['0', '4000000', '999999999999999999999']) {
      const unsupported = analyse(input);
      assert.deepEqual(unsupported.conversion?.forms, []);
      assert(unsupported.warnings.length > 0);
    }
  }],
  ['names, titles and page labels use the final numeral as an ordinal', () => {
    for (const [input, numeral, value] of [
      ['Henry VIII', 'VIII', 8], ['Louis XIV', 'XIV', 14], ['Super Bowl LIX', 'LIX', 59],
      ['Chapter xiv', 'xiv', 14], ['Rocky II', 'II', 2], ['Elizabeth II', 'II', 2],
      ['page ⅻ', 'ⅻ', 12], ['Pope John Paul II', 'II', 2],
    ]) {
      const result = analyse(input, { date: 'ad' });
      assert.equal(result.ordinal?.numeral, numeral, input);
      assert.equal(result.readings[0]?.value, value, input);
      assert.deepEqual(result.years, [], input);
      assert.deepEqual(result.warnings, [], input);
    }
  }],
  ['explicit modes take precedence over ordinal extraction and decimal conversion', () => {
    assert.equal(analyse('Henry VIII', { mode: 'chronogram' }).mode, 'chronogram');
    assert.equal(analyse('2026', { mode: 'passage' }).mode, 'passage');
    assert.equal(analyse('m mix').ordinal, undefined);
    assert.equal(analyse('X V').ordinal, undefined);
    assert.equal(analyse('CIↃ IↃ XCIV').ordinal, undefined);
    assert.equal(analyse('LVDoVICVs DeCIMVs').ordinal, undefined);
  }],
  ['a short date offers candidate centuries within the selected period', () => {
    const years = analyse('lxxv', { date: 'ad', period: 'late-medieval' }).years.map(x => x.year);
    assert.deepEqual(years.filter(x => x >= 1000).sort(), [1075, 1175, 1275, 1375, 1475]);
  }],
  ['AUC and Spanish era are opt-in and cross the civil era boundary', () => {
    assert.equal(analyse('DCCLIV', { date: 'ad' }).years.some(x => x.feature === 'auc'), false);
    for (const [date, inputs] of [['auc', ['I', 'DCCLIII', 'DCCLIV']], ['spanishEra', ['I', 'XXXVIII', 'XXXIX']]]) {
      const expected = date === 'auc' ? ['753 BCE', '1 BCE', '1 CE'] : ['38 BCE', '1 BCE', '1 CE'];
      assert.deepEqual(inputs.map(input => analyse(input, { date }).years[0].text), expected);
    }
    assert.equal(analyse('DCLXXXIII', { date: 'spanishEra' }).years[0].text, '645 CE');
  }],
  ['indiction offers every match in range and needs a source period', () => {
    const options = { date: 'indiction', period: 'early-medieval' };
    const years = analyse('vi', options).years.map(x => x.year).sort((a, b) => a - b);
    assert.equal(years[0], 303);
    assert.equal(years.at(-1), 993);
    assert(years.includes(933));
    assert(years.slice(1).every((year, i) => year - years[i] === 15));
    assert.deepEqual(analyse('VI', { date: 'indiction' }).years, []);
    assert.deepEqual(analyse('XVI', options).years, []);
  }],
  ['chronograms are explicit and count W as VV in each case-sensitive sum', () => {
    const phrase = 'LVDoVICVs DeCIMVs';
    const ordinary = analyse(phrase);
    assert.equal(ordinary.mode, 'number');
    assert(ordinary.warnings.some(w => w.includes('Chronogram')));
    assert.equal(analyse(phrase, { mode: 'chronogram' }).chronogram.caps, 2272);
    const c = analyse('Win win', { mode: 'chronogram' }).chronogram;
    assert.deepEqual([c.caps, c.capsWithW, c.all, c.withW], [0, 10, 2, 22]);
  }],
  ['passage mode finds numeral words and dot-delimited scores with offsets', () => {
    const passage = 'Paid .xx., XII and .iiij.xx. The word civilised and A1IV stay whole.';
    const result = analyse(passage, { mode: 'passage' });
    assert.deepEqual(result.matches.map(x => x.input), ['.xx.', 'XII', '.iiij.xx.']);
    assert(result.matches.every(({ input, offset }) => passage.slice(offset, offset + input.length) === input));
  }],
  ['unknown letters can offer a gloss without generating a numeric reading', () => {
    const q = analyse('Q', { period: 'late-medieval' });
    assert.deepEqual(q.glossLetters, ['Q']);
    assert.deepEqual(q.readings, []);
    assert.deepEqual(RomanResearch.letters.Q.map(item => item.source), ['cappelli1901', 'chrisomalis']);
  }],
  ['unknown and unlikely are separate, with unknown ranked as rare', () => {
    const index = RomanReader.PERIODS.findIndex(p => p.id === 'early-medieval');
    const result = analyse('iiᶜ', { period: 'early-medieval' });
    assert.equal(result.readings[0].scores[index], null);
    assert.equal(result.readings[0].scores[0], 0);
    assert.equal(RomanReader.weight(null), RomanReader.weight(1));
  }],
  ['historical signs and scope use their own conventions', () => {
    assert(analyse('ↆ').readings[0].features.has('earlyFifty'));
    assert(analyse('ↅ').readings[0].features.has('lateSix'));
    assert(analyse('|(I)|').readings[0].features.has('frame'));
    assert(analyse('X̅V').readings.find(reading => reading.value === 15).features.has('distinctionMarks'));
    assert(!analyse('Mᵒiiijᶜlvj').readings.some(reading => reading.value === 100456));
  }],
  ['browser data is current and each exposed convention has sources and a teaching example', () => {
    execFileSync(process.execPath, [fileURLToPath(new URL('./build-data.mjs', import.meta.url)), '--check']);
    const { conventions, sources, presets, letters } = RomanResearch;
    const sourceIds = new Set(sources.map(source => source.id));
    assert.equal(sourceIds.size, sources.length);
    assert.equal(sources.filter(source => source.read_full_text).length, 2);
    const constructed = presets.filter(preset => preset.kind === 'constructed');
    for (const [id, convention] of Object.entries(conventions)) {
      assert.equal(convention.ratings.length, RomanReader.PERIODS.length);
      assert(convention.citations.length && convention.citations.every(cite => sourceIds.has(cite)), id);
      assert(constructed.some(preset => preset.convention_ids.includes(id)), id);
    }
    for (const preset of presets) {
      assert(preset.convention_ids.every(id => Object.hasOwn(conventions, id)), preset.input);
      assert(RomanReader.PERIODS.some(p => p.id === preset.period_id), preset.input);
      assert(preset.values.length && preset.why, preset.input);
    }
    for (const entry of Object.values(letters).flat()) assert(sourceIds.has(entry.source));
    assert(presets.length >= 60);
  }],
];

for (const [label, run] of checks) {
  try { run(); console.log('ok  ', label); }
  catch (error) { fail++; console.log('FAIL', label, error); }
}

const attested = RomanResearch.presets.filter(preset => preset.kind === 'attested');
const unmatched = [];
const presetResults = [];
for (const preset of attested) {
  const result = analyse(preset.input, { period: preset.period_id, ...preset.options });
  const values = preset.options?.mode === 'chronogram'
    ? [result.chronogram.caps]
    : preset.options?.date
      ? result.years.map(year => year.year)
      : result.readings.map(r => r.value).filter(value => value !== null);
  const match = preset.values.every(expected => values.includes(expected));
  presetResults.push({ input: preset.input, period: preset.period_id, expected: preset.values, values, match });
  console.log(match ? 'match   ' : 'mismatch', preset.input, '→', match ? preset.values : values,
    match ? '' : 'expected ' + preset.values.join(', '), '·', preset.source);
  if (!match) unmatched.push({ preset, values });
}

const total = cases.length + checks.length;
const matched = attested.length - unmatched.length;
const summary = matched + '/' + attested.length + ' attested presets matched';
console.log((total - fail) + '/' + total + ' regression and data checks passed');
console.log(summary + '; ' + (RomanResearch.presets.length - attested.length) + ' constructed presets');

if (process.argv.includes('--write-preset-check')) {
  const reasons = {
    'IIII CĐXI': 'The struck Đ and the implied unit of thousands in the inscription require a source-specific interpretation.',
    'IIIIˣˣ et huit': 'The remaining eight is written out in French. The reader does not add words as numbers.',
  };
  const lines = unmatched.map(({ preset, values }) => [
    '', preset.input.replaceAll('|', '\\|'), preset.values.join(', '), values.join(', ') || 'None',
    reasons[preset.input] || preset.why, '',
  ].join(' | ').trim());
  const report = [
    '---', 'title: Version 3 preset check', 'date: 2026-11-21', '---', '',
    '# Version 3 preset check', '',
    'The tool matched ' + matched + ' of ' + attested.length + ' reported examples from sources. A match means that the documented numerical value, converted year, chronogram sum or indiction year appears among the results with the preset’s settings. This check measures coverage of the documented readings. Source availability and rank are recorded separately.', '',
    'The Madalfredus example XLVIII was removed before this check because the transcription could not be confirmed on the cited page.', '',
    '## Mismatches', '',
    '| Preset | Expected | Reader output | Source context |', '| --- | --- | --- | --- |',
    ...lines, '',
    'Run node test.mjs for each result or add --write-preset-check to regenerate this file.', '',
  ].join('\n');
  writeFileSync(new URL('../data/preset-check.md', import.meta.url), report);
}
process.exitCode = fail ? 1 : 0;

if (process.argv.includes('--json')) {
  console.log(JSON.stringify({ presetResults, total, fail, constructed: RomanResearch.presets.length - attested.length }));
}
