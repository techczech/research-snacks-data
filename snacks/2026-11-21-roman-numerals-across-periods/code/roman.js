// Roman numeral reader: every plausible reading of a numeral, with the
// convention each reading assumes and how usual that convention was per period.
// Classic script (works from file:// and in Node via globalThis.RomanReader).
(function (root) {
  'use strict';

  const PERIODS = [
    { id: 'classical', short: 'Classical', label: 'Classical Roman', range: 'to c. 300 CE', years: [-500, 300] },
    { id: 'early-medieval', short: 'Early medieval', label: 'Late antique & early medieval', range: 'c. 300–1000', years: [300, 1000] },
    { id: 'late-medieval', short: 'Late medieval', label: 'High & late medieval', range: 'c. 1000–1500', years: [1000, 1500] },
    { id: 'early-modern', short: 'Early modern', label: 'Early modern', range: 'c. 1500–1800', years: [1500, 1800] },
    { id: 'modern', short: 'Modern', label: 'Modern', range: '1800 onwards', years: [1800, 2100] },
  ];

  const LEVELS = ['unlikely', 'rare', 'attested', 'typical'];
  const { conventions } = root.RomanResearch;
  const DATE_MODES = ['ad', 'auc', 'spanishEra', 'indiction'];
  const dateFeatures = new Set([...DATE_MODES, 'omittedMillennium', 'omittedCentury']);
  const FEATURES = Object.fromEntries(Object.entries(conventions).filter(([id]) => !dateFeatures.has(id)));
  const YEAR_FEATURES = Object.fromEntries(Object.entries(conventions).filter(([id]) => dateFeatures.has(id)));
  const weight = (score) => score ?? 1;

  const BASE = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
  const UNICODE_NUMERALS = {
    'Ⅰ': 'I', 'Ⅱ': 'II', 'Ⅲ': 'III', 'Ⅳ': 'IV', 'Ⅴ': 'V', 'Ⅵ': 'VI', 'Ⅶ': 'VII', 'Ⅷ': 'VIII', 'Ⅸ': 'IX', 'Ⅹ': 'X', 'Ⅺ': 'XI', 'Ⅻ': 'XII', 'Ⅼ': 'L', 'Ⅽ': 'C', 'Ⅾ': 'D', 'Ⅿ': 'M',
    'ⅰ': 'i', 'ⅱ': 'ii', 'ⅲ': 'iii', 'ⅳ': 'iv', 'ⅴ': 'v', 'ⅵ': 'vi', 'ⅶ': 'vii', 'ⅷ': 'viii', 'ⅸ': 'ix', 'ⅹ': 'x', 'ⅺ': 'xi', 'ⅻ': 'xii', 'ⅼ': 'l', 'ⅽ': 'c', 'ⅾ': 'd', 'ⅿ': 'm',
  };
  const SPECIAL = { 'ↀ': [1000, 'apostrophus'], 'ↁ': [5000, 'apostrophus'], 'ↂ': [10000, 'apostrophus'], 'ↇ': [50000, 'apostrophus'], 'ↈ': [100000, 'apostrophus'], 'ↅ': [6, 'lateSix'], 'ↆ': [50, 'earlyFifty'] };
  const SUPERSCRIPTS = { 'ᵐ': 'm', 'ᶜ': 'c', 'ˣ': 'x', 'ᵒ': 'o', '°': 'o', 'º': 'o', 'ᵘ': 'u', 'ˢ': 's', 'ᵗ': 't', 'ⁱ': 'i', 'ᵛ': 'v', 'ᵃ': 'a', 'ⁿ': 'n', 'ᵉ': 'e', 'ᵈ': 'd', 'ˡ': 'l' };
  const MULTIPLIERS = { m: 1000, c: 100, xx: 20 };
  const ENDINGS = new Set(['o', 'mo', 'to', 'no', 'do', 'us', 'a', 'e', 'is', 'um', 'ti', 'ta', 'tus', 'mus', 'nus', 'ie', 'tie', 'th', 'st', 'nd', 'rd']);
  const SEPARATORS = /[.\s·•,:;\-–—'’]/;

  function isPow10(n) { while (n >= 10 && n % 10 === 0) n /= 10; return n === 1; }
  function fmt(n) { return n.toLocaleString('en-GB'); }

  function toRoman(n) {
    if (!Number.isInteger(n) || n < 1 || n > 3999) return null;
    const t = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']];
    let s = '';
    for (const [v, r] of t) while (n >= v) { s += r; n -= v; }
    return s;
  }

  const MAX_CONVERSION = 3999999;
  const SUBTRACTIVE = { IV: 'IIII', IX: 'VIIII', XL: 'XXXX', XC: 'LXXXX', CD: 'CCCC', CM: 'DCCCC' };
  const expandRoman = input => Array.from(input, ch => UNICODE_NUMERALS[ch] || ch).join('').toUpperCase();

  function romanForms(value) {
    if (!Number.isSafeInteger(value) || value < 1 || value > MAX_CONVERSION) return [];
    const barred = value >= 4000;
    const thousands = barred ? toRoman(Math.floor(value / 1000)) : '';
    const units = toRoman(barred ? value % 1000 : value) || '';
    const withBar = signs => Array.from(signs, sign => sign + '̅').join('');
    const additive = signs => signs.replace(/IV|IX|XL|XC|CD|CM/g, pair => SUBTRACTIVE[pair]);
    const numeral = withBar(thousands) + units;
    const forms = [{ numeral, convention: barred ? 'vinculum' : 'standard' }];
    const expanded = withBar(additive(thousands)) + additive(units);
    if (expanded !== numeral) forms.push({ numeral: expanded, convention: 'additive4', clock: value === 4 });
    return forms;
  }

  function ordinalIn(input) {
    const match = /^([\p{L}\p{M} .’'-]+?)[ \t]+([IVXLCDMⅠ-ⅿ]+)$/iu.exec(input);
    if (!match) return null;
    const [, label, numeral] = match;
    const descriptor = /^(chapter|page|section|part|book|volume|outline|act|scene|appendix|article|p\.|vol\.)$/i.test(label);
    const title = /^\p{Lu}[\p{L}\p{M}’'-]*(?: (?:\p{Lu}[\p{L}\p{M}’'-]*|of|the|and))*$/u.test(label);
    if (!descriptor && (!title || /^[IVXLCDMJUↀ-ↈⅠ-ⅿƆↄ\s]+$/i.test(label))) return null;
    if (!descriptor && numeral !== numeral.toUpperCase()) return null;
    const canonical = expandRoman(numeral);
    const tokens = Array.from(canonical, letter => ({ value: BASE[letter] }));
    if (tokens.some(token => token.value === undefined) || toRoman(readPairs(tokens).value) !== canonical) return null;
    return { label, numeral };
  }

  // ---------- 1. Characters → items ----------
  function toItems(input) {
    let s = '';
    for (const ch of input) s += UNICODE_NUMERALS[ch] || ch;
    s = s.normalize('NFD');
    const items = [];
    const hints = new Set();
    let pendingSup = false, pendingOver = false, frame = 0, nextFrame = 0;
    for (const ch of s) {
      if (ch === '̅' || ch === '̄' || ch === '̿') { if (items.length) items[items.length - 1].over = true; hints.add('vinculum'); continue; }
      if (ch === '^') { pendingSup = true; continue; }
      if (ch === '_') { pendingOver = true; hints.add('vinculum'); continue; }
      if (ch === '|') { frame = frame ? 0 : ++nextFrame; continue; }
      if (SEPARATORS.test(ch)) { pendingSup = false; if (ch === '.' || ch === '·' || ch === '•') hints.add('dots'); items.push({ sep: true }); continue; }
      if (SUPERSCRIPTS[ch]) { items.push({ ch: SUPERSCRIPTS[ch], sup: true }); hints.add('superscript'); continue; }
      let c = ch;
      if (c === 'Ɔ' || c === 'ↄ' || c === ')') c = 'Ↄ';
      if (c === '(') c = 'C';
      if (SPECIAL[c]) { items.push({ ch: c, special: true, frame }); pendingSup = false; continue; }
      if (c === 'Ↄ') { items.push({ ch: 'Ↄ', orig: ch, frame }); continue; }
      if (!/[a-z]/i.test(c)) { items.push({ ch: c, unknown: true }); continue; }
      const lower = c === c.toLowerCase();
      const item = { ch: c.toUpperCase(), orig: ch, lower, sup: pendingSup, over: pendingOver, frame };
      pendingOver = false;
      if (item.ch === 'J') { item.ch = 'I'; item.j = true; hints.add('j'); }
      if (item.ch === 'U') { item.ch = 'V'; item.u = true; }
      if (lower && !item.sup) hints.add('lowercase');
      items.push(item);
    }
    return { items, hints };
  }

  // ---------- 2. Items → tokens ----------
  function tokenize(input, distinction = false) {
    const { items, hints } = toItems(input);
    const tokens = [];
    const notes = [];
    const unknown = [];
    let i = 0;
    const plain = (k) => items[k] && !items[k].sep && !items[k].sup && (!items[k].over || distinction) && items[k].frame === items[i].frame;
    const seq = (k, str) => { for (let n = 0; n < str.length; n++) { if (!plain(k + n) || items[k + n].ch !== str[n]) return false; } return true; };
    while (i < items.length) {
      const it = items[i];
      if (it.sep) { i++; continue; }
      if (it.unknown) { unknown.push(it.ch); i++; continue; }
      if (it.special) {
        const [value, kind] = SPECIAL[it.ch];
        const factor = it.frame ? 100000 : it.over && !distinction ? 1000 : 1;
        tokens.push({ raw: it.ch + (it.over ? '̅' : ''), value: value * factor, kind,
          frame: it.frame, distinction: it.over && distinction && !it.frame, vinculum: factor === 1000 });
        i++;
        continue;
      }
      if (it.sup) {
        let g = ''; let j = i;
        while (j < items.length && items[j].sup) { g += items[j].ch.toLowerCase(); j++; }
        if (MULTIPLIERS[g]) tokens.push({ raw: '^' + g, value: MULTIPLIERS[g], kind: g === 'xx' ? 'vigesimal' : 'multiplier', mult: true });
        else if (ENDINGS.has(g)) notes.push(`Superscript “${g}” read as a grammatical ending (e.g. -mo in millesimo), not a numeral.`);
        else if (/^[ivxlcdm]+$/.test(g)) { for (const ch of g) tokens.push({ raw: ch, value: BASE[ch.toUpperCase()], kind: 'letter' }); notes.push(`Superscript “${g}” treated as ordinary numerals.`); }
        else notes.push(`Superscript “${g}” not recognised; ignored.`);
        i = j; continue;
      }
      // Apostrophus groups must stay inside the same frame or outside it.
      const apostrophus = (len, value) => {
        const group = items.slice(i, i + len);
        tokens.push({
          raw: group.map(x => (x.orig || x.ch) + (x.over ? '̅' : '')).join(''),
          value: value * (it.frame ? 100000 : 1),
          kind: 'apostrophus', frame: it.frame,
          distinction: distinction && group.some(x => x.over),
        });
        i += len;
      };
      let matched = false;
      for (let n = 3; n >= 1 && !matched; n--) {
        if (seq(i, 'C'.repeat(n) + 'I' + 'Ↄ'.repeat(n))) {
          apostrophus(2 * n + 1, 10 ** (n + 2));
          matched = true;
        }
      }
      for (let n = 3; n >= 1 && !matched; n--) {
        if (seq(i, 'I' + 'Ↄ'.repeat(n))) {
          apostrophus(n + 1, 5 * 10 ** (n + 1));
          matched = true;
        }
      }
      if (matched) continue;
      if (it.ch === 'Ↄ') { unknown.push('Ↄ'); notes.push('A reversed C outside an apostrophus group was ignored (it can also be the abbreviation con-).'); i++; continue; }
      if (BASE[it.ch] === undefined) { unknown.push(it.orig || it.ch); i++; continue; }
      let value = BASE[it.ch];
      let kind = 'letter';
      if (it.frame) { value *= 100000; kind = 'frame'; } else if (it.over && !distinction) { value *= 1000; kind = 'vinculum'; }
      tokens.push({ raw: (it.orig || it.ch) + (it.over ? '̅' : ''), value, kind, distinction: it.over && distinction && !it.frame, j: !!it.j, lower: it.lower, letter: it.ch });
      i++;
    }
    // A j that is not the last numeral marks a probable boundary.
    tokens.forEach((t, k) => { if (t.j && k < tokens.length - 1 && !tokens[k + 1].mult) t.boundary = true; });
    return { tokens, hints, notes, unknown };
  }

  // ---------- 3. Reading methods ----------
  function kindFeatures(tokens) {
    const f = new Set();
    for (const t of tokens) {
      if (['apostrophus', 'earlyFifty', 'lateSix', 'vinculum', 'frame'].includes(t.kind)) f.add(t.kind);
      if (t.frame) f.add('frame');
      if (t.vinculum) f.add('vinculum');
      if (t.distinction) f.add('distinctionMarks');
    }
    return f;
  }

  const show = (ts) => ts.map(t => t.raw).join('');

  // Usual reading: a smaller symbol before a larger one is subtracted from it.
  function readPairs(tokens) {
    const units = [];
    let i = 0;
    while (i < tokens.length) {
      const a = tokens[i], b = tokens[i + 1];
      if (b && a.value < b.value) { units.push({ v: b.value - a.value, sub: true, a: a.value, b: b.value, text: a.raw + b.raw }); i += 2; }
      else { units.push({ v: a.value, sub: false, text: a.raw }); i++; }
    }
    const f = kindFeatures(tokens);
    let odd = false, irregular = false, four = false;
    let run = 1;
    for (let k = 0; k < units.length; k++) {
      const u = units[k], p = units[k - 1];
      if (u.sub) {
        const r = u.b / u.a;
        if (!(isPow10(u.a) && (r === 5 || r === 10))) irregular = true;
        if (p && !p.sub && (p.v < u.b || (p.v === u.b && !isPow10(p.v)))) odd = true;
        if (p && !p.sub && p.v === u.a) odd = true; // e.g. IIX handled by repeated subtraction
      } else if (p) {
        if (p.sub ? u.v >= p.a : u.v > p.v) odd = true;
      }
      if (p && !u.sub && !p.sub && p.v === u.v) {
        run++;
        if (!isPow10(u.v)) odd = true;
        if (run === 4) four = true;
        if (run > 4) odd = true;
      } else run = 1;
    }
    // VIIII / LXXXX / DCCCC count as additive nines; IIII after a subtractive pair is odd
    if (irregular) f.add('irregularSub');
    if (odd) f.add('oddOrder');
    if (four && !odd) f.add('additive4');
    if (!irregular && !odd && !four && f.size === 0) f.add('standard');
    const value = units.reduce((s, u) => s + u.v, 0);
    return { value, features: f, method: 'pairs', breakdown: units.map(u => `${u.text} ${fmt(u.v)}`).join(' + ') };
  }

  // Runs of identical letters before a larger one subtracted together (IIX = 8).
  function readRuns(tokens) {
    const runs = [];
    for (const t of tokens) {
      const last = runs[runs.length - 1];
      if (last && last.value === t.value && last.raw === t.raw) { last.count++; last.text += t.raw; }
      else runs.push({ value: t.value, raw: t.raw, count: 1, text: t.raw });
    }
    if (!runs.some((r, k) => r.count > 1 && runs[k + 1] && runs[k + 1].value > r.value)) return null;
    let value = 0; const parts = [];
    for (let k = 0; k < runs.length; k++) {
      const r = runs[k], n = runs[k + 1];
      if (n && n.value > r.value) { value += n.value - r.count * r.value; parts.push(`${r.text}${n.text} ${fmt(n.value - r.count * r.value)}`); k++; if (n.count > 1) { value += (n.count - 1) * n.value; parts[parts.length - 1] += ` + ${fmt((n.count - 1) * n.value)}`; } }
      else { value += r.count * r.value; parts.push(`${r.text} ${fmt(r.count * r.value)}`); }
    }
    const f = kindFeatures(tokens); f.add('runSub');
    return { value, features: f, method: 'runs', breakdown: parts.join(' + ') };
  }

  function readSum(tokens) {
    const value = tokens.reduce((s, t) => s + t.value, 0);
    const f = kindFeatures(tokens); f.add('additiveSum');
    return { value, features: f, method: 'sum', breakdown: tokens.map(t => `${t.raw} ${fmt(t.value)}`).join(' + ') };
  }

  // Superscript multipliers (iiᵐ), scores (iiijˣˣ), and optionally M/C on the line as multipliers.
  function readMultiplied(tokens, allowPlain) {
    let total = 0, seg = [], used = false;
    const f = kindFeatures(tokens); const parts = [];
    const close = (mult, label, feat) => {
      const base = seg.length ? readPairs(seg).value : 1;
      total += base * mult; parts.push(`${seg.length ? show(seg) : '1'} × ${label} ${fmt(base * mult)}`);
      seg = []; used = true; f.add(feat);
    };
    for (const t of tokens) {
      if (t.mult) {
        const boundary = seg.findLastIndex(token => token.value >= t.value) + 1;
        if (boundary && boundary === seg.length) return null;
        const prefix = seg.splice(0, boundary);
        if (prefix.length) {
          const reading = readPairs(prefix);
          total += reading.value;
          parts.push(reading.breakdown);
        }
        close(t.value, t.raw.replace('^', ''), t.kind === 'vigesimal' ? 'vigesimal' : 'multiplicative');
        continue;
      }
      if (allowPlain && t.kind === 'letter' && (t.value === 1000 || t.value === 100) && seg.length) {
        const segVal = readPairs(seg).value;
        const maxSeg = Math.max(...seg.map(s => s.value));
        const stdPair = seg.length === 1 && (t.value / seg[0].value === 10 || t.value / seg[0].value === 5 || (seg[0].value === 100 && t.value === 1000));
        if (maxSeg < t.value && segVal >= 2 && !stdPair) { close(t.value, t.raw, 'multiplicativePlain'); continue; }
      }
      seg.push(t);
    }
    if (!used) return null;
    if (seg.length) { const r = readPairs(seg); total += r.value; parts.push(`${show(seg)} ${fmt(r.value)}`); }
    return { value: total, features: f, method: 'multiplied', breakdown: parts.join(' + ') };
  }

  function splitAtBoundaries(tokens) {
    const groups = [[]];
    for (const t of tokens) { groups[groups.length - 1].push(t); if (t.boundary) groups.push([]); }
    return groups.filter(g => g.length);
  }

  // ---------- 4. Scoring ----------
  function minimumRating(scores) {
    const minimum = Math.min(...scores.map(weight));
    return minimum === 1 && scores.includes(null) ? null : minimum;
  }

  function scoresFor(features, table) {
    return PERIODS.map((_, p) => minimumRating([...features].map(k => table[k].ratings[p])));
  }

  function rank(r, periodIndex) {
    return periodIndex >= 0 ? weight(r.scores[periodIndex]) : Math.max(...r.scores.map(weight));
  }

  function explain(features, table) { return [...features].map(k => table[k].label).join(' · '); }

  function readTokens(tokens) {
    const out = [];
    const add = (r) => { if (r && Number.isFinite(r.value)) out.push(r); };
    const hasMult = tokens.some(t => t.mult);
    const boundaries = tokens.some(t => t.boundary);
    if (hasMult) {
      add(readMultiplied(tokens, false));
      const plainToo = readMultiplied(tokens, true);
      if (plainToo && !out.some(o => o.value === plainToo.value)) add(plainToo);
    } else {
      add(readPairs(tokens));
      add(readRuns(tokens));
      add(readMultiplied(tokens, true));
      const s = readSum(tokens);
      if (!out.some(o => o.value === s.value)) add(s);
    }
    if (boundaries) {
      const groups = splitAtBoundaries(tokens);
      const vals = groups.map(g => readPairs(g).value);
      if (groups.length === 2 && vals[1] === 20 && vals[0] < 20 && !hasMult) {
        const f = new Set(['vigesimal']);
        out.push({ value: vals[0] * 20, features: f, method: 'scores', breakdown: `${show(groups[0])} × ${show(groups[1])} = ${fmt(vals[0])} × 20` });
      }
      out.push({ value: null, values: vals, features: new Set(['separate']), method: 'separate', breakdown: groups.map((g, k) => `${show(g)} = ${fmt(vals[k])}`).join(' and ') });
    }
    return out;
  }

  // On-line score notation has an explicit XX group and an optional remainder.
  function readDottedScores(raw) {
    const terms = raw.trim().replace(/^[.·•]+|[.·•]+$/g, '').split(/[.·•]/).map(t => t.trim());
    if (terms.length < 2 || terms.length > 3 || !/^xx$/i.test(terms[1])) return null;
    if (!terms.every(t => /^[ivxlj]+$/i.test(t))) return null;
    const values = terms.map(t => readPairs(tokenize(t).tokens).value);
    const [count, , remainder = 0] = values;
    if (count < 1 || count >= 20 || remainder >= 20) return null;
    return { value: count * 20 + remainder, features: new Set(['vigesimal']), method: 'scores',
      breakdown: `${terms[0]} × 20${terms[2] ? ' + ' + terms[2] : ''}` };
  }

  function findNumerals(input) {
    const signs = 'IVXLCDMJUↀ-ↈⅠ-ⅿƆↄ';
    const term = `[${signs}][ ${signs}\u0304\u0305\u033fᵐᶜˣᵒº°]*`;
    const pattern = new RegExp(
      `(?<![\\p{L}\\p{N}\\p{M}])(?:\\.${term}\\.\\s*xx\\.(?:${term}\\.)?|\\.${term}\\.|[${signs}][${signs}\\u0304\\u0305\\u033fᵐᶜˣᵒº°]*)(?![\\p{L}\\p{N}\\p{M}])`, 'giu');
    return [...input.matchAll(pattern)].map(match => ({ input: match[0], offset: match.index }));
  }

  // ---------- 5. Public entry ----------
  function analyse(input, options = {}) {
    const period = options.period || 'unknown';
    const periodIndex = PERIODS.findIndex(p => p.id === period);
    let raw = (input || '').trim();
    const result = { input: raw, period, mode: 'number', readings: [], years: [], hints: [], notes: [], warnings: [], tokens: [] };
    if (!raw) return result;

    if (options.mode === 'chronogram' || options.chronogram) return chronogram(raw, result);
    if (options.mode === 'passage') {
      result.mode = 'passage';
      result.matches = findNumerals(raw);
      return result;
    }

    if (/^\d+$/.test(raw)) {
      const value = Number(raw);
      const forms = romanForms(value);
      result.conversion = { value, forms };
      if (!forms.length) result.warnings.push('Enter a whole number from 1 to 3,999,999 for Roman conversion.');
      return result;
    }

    const ordinal = ordinalIn(raw);
    if (ordinal) {
      result.ordinal = ordinal;
      raw = ordinal.numeral;
    }
    result.numeral = raw;
    const tk = tokenize(raw);
    result.tokens = tk.tokens;
    result.notes.push(...tk.notes);
    const ignored = [...new Set(tk.unknown.filter(u => u !== 'Ↄ'))];
    if (ignored.length) result.warnings.push(`The Roman-numeral readings leave out ${ignored.join(' ')}.`);
    if (ordinal) tk.hints.delete('lowercase');
    result.hints = periodHints(tk);

    if (ignored.some(ch => /\p{L}/u.test(ch))) {
      result.warnings.push('For a phrase with letters selected to encode a year, choose Chronogram.');
      result.glossLetters = [...new Set(ignored.map(ch => ch.toUpperCase()))];
    }
    let readings = tk.tokens.length ? readTokens(tk.tokens) : [];
    if (tk.hints.has('vinculum')) {
      const marked = tokenize(raw, true);
      readings.push(...readTokens(marked.tokens).filter(r => r.features.has('distinctionMarks')));
    }
    const scores = readDottedScores(raw);
    if (scores && !readings.some(r => r.method === 'scores' && r.value === scores.value)) readings.push(scores);
    if (ignored.length) readings.forEach(r => r.features.add('ignored'));

    // Minim misreadings: n → ii, m (after small numerals) → iii, u → ii.
    for (const variant of minimVariants(raw)) {
      const vt = tokenize(variant.text);
      if (!vt.tokens.length) continue;
      const best = readTokens(vt.tokens).filter(r => r.value !== null)[0];
      if (!best) continue;
      const f = new Set(best.features); f.add('minim');
      readings.push({ value: best.value, features: f, method: 'minim', breakdown: `if ${variant.why}: ${variant.text} → ${best.breakdown}` });
    }

    for (const r of readings) { r.scores = scoresFor(r.features, FEATURES); r.explanation = explain(r.features, FEATURES); r.modern = r.value != null ? toRoman(r.value) : null; }

    // Merge readings with the same value, keeping the most plausible explanation first.
    const byValue = new Map();
    for (const r of readings) {
      const key = r.value === null ? 'sep:' + r.values.join(',') : r.value;
      const ex = byValue.get(key);
      if (!ex) { byValue.set(key, { ...r, also: [] }); continue; }
      if (rank(r, periodIndex) > rank(ex, periodIndex)) { byValue.set(key, { ...r, also: [ex, ...ex.also] }); }
      else ex.also.push(r);
    }
    readings = [...byValue.values()].map(r => {
      // a value is as plausible as its best explanation
      r.scores = r.scores.map((s, p) => [s, ...r.also.map(a => a.scores[p])].reduce((best, score) => weight(score) > weight(best) || (best === null && score === 1) ? score : best));
      return r;
    });
    const order = { pairs: 0, runs: 1, multiplied: 2, scores: 2, separate: 3, minim: 4, sum: 5 };
    readings.sort((a, b) => rank(b, periodIndex) - rank(a, periodIndex) || (order[a.method] - order[b.method]));
    result.readings = readings;

    const dateMode = options.date || (options.year ? 'ad' : '');
    if (!ordinal && DATE_MODES.includes(dateMode)) {
      result.years = yearReadings(readings, periodIndex, dateMode);
      if (dateMode === 'indiction' && periodIndex < 0) result.warnings.push('Choose a source period to list candidate indiction years.');
      else if (dateMode === 'indiction' && !result.years.length) result.warnings.push('An indiction number runs from 1 to 15.');
    }
    return result;
  }

  function minimVariants(raw) {
    const out = [];
    if (/n/.test(raw)) out.push({ text: raw.replace(/n/g, 'ii'), why: '“n” is a misread “ii”' });
    if (/[ivx]m/.test(raw)) out.push({ text: raw.replace(/([ivx])m/g, '$1iii'), why: '“m” after small numerals is a misread “iii”' });
    if (/[ivx]u|u[ivxj]/.test(raw)) out.push({ text: raw.replace(/u/g, 'ii'), why: '“u” is a misread “ii”' });
    return out;
  }

  function periodHints(tk) {
    const h = [];
    if (tk.hints.has('j')) h.push('Final j (iij, viij) is a scribal and printing habit of the later Middle Ages and early modern period.');
    if (tk.hints.has('lowercase')) h.push('Lower-case numerals occur in manuscripts and print, including modern page and outline numbering.');
    if (tk.hints.has('dots')) h.push('Numerals set off by dots (.xx.) are common in medieval manuscripts.');
    if (tk.hints.has('superscript')) h.push('Superscript multipliers and endings are typical of medieval and early modern documents and accounts.');
    if (tk.tokens.some(t => t.kind === 'apostrophus')) h.push('The apostrophus (CIↃ, IↃ) points to Roman inscriptions or to early modern printed books, where it was revived.');
    if (tk.tokens.some(t => t.kind === 'vinculum')) h.push('A vinculum is a bar that can multiply a numeral by 1,000.');
    return h;
  }

  function yearReadings(readings, periodIndex, mode) {
    const out = [];
    const seen = new Set();
    const push = (year, feature, from) => {
      if (seen.has(year)) return;
      seen.add(year);
      const scores = PERIODS.map((p, i) => {
        const [lo, hi] = p.years;
        return minimumRating([YEAR_FEATURES[feature].ratings[i], from.scores[i],
          year >= lo - 100 && year <= hi + 50 ? 3 : 1]);
      });
      const text = year > 0 ? year + ' CE' : (1 - year) + ' BCE';
      out.push({ year, feature, from: from.value, scores, text });
    };
    for (const r of readings) {
      const v = r.value;
      if (!Number.isSafeInteger(v) || v < 1) continue;
      if (mode === 'auc') push(v - 753, 'auc', r);
      if (mode === 'spanishEra') push(v - 38, 'spanishEra', r);
      if (mode === 'indiction' && v <= 15 && periodIndex >= 0) {
        const [lo, hi] = PERIODS[periodIndex].years;
        for (let year = Math.max(lo, 1); year <= hi; year++) {
          if ((year + 2) % 15 + 1 === v) push(year, 'indiction', r);
        }
      }
      if (mode !== 'ad') continue;
      push(v, 'ad', r);
      if (v < 1000) push(1000 + v, 'omittedMillennium', r);
      if (v < 100 && periodIndex >= 0) {
        const [lo, hi] = PERIODS[periodIndex].years;
        for (let century = Math.max(10, Math.floor(lo / 100)); century * 100 + v <= hi; century++) {
          const year = century * 100 + v;
          if (year >= lo) push(year, 'omittedCentury', r);
        }
      }
    }
    out.sort((a, b) => rank(b, periodIndex) - rank(a, periodIndex) || a.year - b.year);
    return out;
  }

  function chronogram(raw, result) {
    const val = { I: 1, J: 1, V: 5, U: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
    let all = 0, caps = 0, w = 0, capW = 0; const letters = [], capLetters = [];
    for (const ch of raw) {
      const up = ch.toUpperCase();
      if (up === 'W') { w += 10; if (ch === 'W') capW += 10; }
      if (val[up] !== undefined) { all += val[up]; letters.push(up); if (ch === up && ch !== ch.toLowerCase()) { caps += val[up]; capLetters.push(up); } }
    }
    result.mode = 'chronogram';
    result.chronogram = {
      all, letters: letters.join(''),
      caps, capLetters: capLetters.join(''),
      withW: all + w, capsWithW: caps + capW,
      hasMixedCase: /[a-z]/.test(raw) && /[A-Z]/.test(raw),
    };
    return result;
  }

  root.RomanReader = { analyse, toRoman, expandRoman, PERIODS, LEVELS, FEATURES, YEAR_FEATURES, DATE_MODES, weight };
})(typeof globalThis !== 'undefined' ? globalThis : window);
