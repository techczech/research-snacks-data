(function () {
  'use strict';
  const R = globalThis.RomanReader;
  const { conventions, sources, presets, letters, glossary } = globalThis.RomanResearch;
  const $ = id => document.getElementById(id);
  const q = $('q'), mode = $('mode'), period = $('period'), date = $('date'), out = $('out');
  const periods = Object.fromEntries(R.PERIODS.map(p => [p.id, p]));
  const sourceById = Object.fromEntries(sources.map(s => [s.id, s]));
  const fmt = number => number.toLocaleString('en-GB');
  const display = value => typeof value === 'number' ? fmt(value) : value;
  const esc = value => String(value).replace(/[&<>"]/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ch]));
  const option = (value, label) => `<option value="${esc(value)}">${esc(label)}</option>`;
  const alphaConventions = Object.entries(conventions).sort(([, a], [, b]) => a.label.localeCompare(b.label, 'en-GB'));

  const termIds = new Map(glossary.flatMap(entry => [entry.term, ...entry.aliases]
    .map(term => [term.toLowerCase(), entry.id])));
  const termPattern = new RegExp('\\b(?:' + [...termIds.keys()].sort((a, b) => b.length - a.length)
    .map(term => term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')\\b', 'gi');
  let currentPreset = null;
  let readingNotes = [];

  function linked(value) {
    let html = '';
    let end = 0;
    for (const match of String(value).matchAll(termPattern)) {
      const [term] = match;
      html += esc(value.slice(end, match.index));
      html += `<a href="#term-${termIds.get(term.toLowerCase())}" data-reveal>${esc(term)}</a>`;
      end = match.index + term.length;
    }
    return html + esc(value.slice(end));
  }

  function sourceLink(url, label) {
    return `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${esc(label)}</a>`;
  }

  function citationLinks(ids) {
    return `<ul class="source-links">${ids.map(id => {
      const source = sourceById[id];
      return `<li>${sourceLink(source.url, source.title)}</li>`;
    }).join('')}</ul>`;
  }

  const levels = new Map([
    [3, ['typical', 'Usual in the named context.']],
    [2, ['attested', 'Documented in the named context.']],
    [1, ['rare', 'A limited occurrence or plausible exception.']],
    [0, ['unlikely', 'There is reason to expect a different convention.']],
    [null, ['no evidence found', 'The material consulted leaves this cell open.']],
  ]);

  function cell(score, periodLabel = '', selected = false) {
    const style = score === null ? 'no-evidence' : `l${score}`;
    const label = levels.get(score)[0];
    return `<span class="cell ${style}${selected ? ' sel' : ''}">${esc(periodLabel ? periodLabel + ' · ' + label : label)}</span>`;
  }
  function strip(scores) {
    return `<div class="strip">${R.PERIODS.map((p, i) => cell(scores[i], p.short, period.value === p.id)).join('')}</div>`;
  }

  function featureEvidence(ids) {
    return ids.map(id => {
      const f = conventions[id];
      return `<div class="rule"><strong>${linked(f.label)}</strong>
        <p>${linked(f.note)}</p><p class="muted">${linked(f.justification)}</p>
        ${f.where ? `<p><strong>Where</strong> ${linked(f.where)}</p>` : ''}
        ${citationLinks(f.citations)}</div>`;
    }).join('');
  }

  function evidence(ids) {
    return `<details class="evidence"><summary>Evidence and sources</summary>${featureEvidence([...new Set(ids)])}</details>`;
  }

  function stateHash(input, sourcePeriod, inputMode, dateMode) {
    const params = new URLSearchParams();
    if (input) params.set('q', input);
    if (sourcePeriod !== 'unknown') params.set('p', sourcePeriod);
    if (inputMode !== 'number') params.set('m', inputMode);
    if (dateMode) params.set('d', dateMode);
    return params.size ? '#' + params.toString() : '';
  }

  function saveState() {
    const hash = stateHash(q.value, period.value, mode.value, date.value);
    if (location.hash !== hash) history.replaceState(null, '', hash || location.href.split('#')[0]);
  }

  function loadState() {
    const params = new URLSearchParams(location.hash.slice(1));
    const p = params.get('p');
    const m = params.get('m');
    const d = params.get('d');
    currentPreset = null;
    q.value = params.get('q') || '';
    period.value = Object.hasOwn(periods, p) ? p : 'unknown';
    mode.value = ['chronogram', 'passage'].includes(m) ? m : 'number';
    date.value = R.DATE_MODES.includes(d) ? d : params.get('y') === '1' ? 'ad' : '';
    render();
  }

  function passage(result) {
    if (!result.matches.length) return '<p class="muted">No standalone numeral tokens found.</p>';
    const links = result.matches.map(match => {
      const hash = stateHash(match.input, period.value, 'number', date.value);
      return `<li><a class="result-link" href="${esc(hash)}">${esc(match.input)}</a>
        <span class="muted"> at character ${fmt(match.offset + 1)}</span></li>`;
    });
    return `<section class="panel"><h3>Numerals found in the passage</h3>
      <p class="muted">Check the surrounding words. A numeral-like word such as “mix” can also be ordinary text.</p>
      <ol>${links.join('')}</ol></section>`;
  }

  function chronogram({ chronogram: c }) {
    const sums = [];
    if (c.capLetters) {
      sums.push(`<p><strong>${fmt(c.caps)}</strong> from the capital numeral letters ${esc(c.capLetters)}.</p>`);
    }
    if (c.letters && (!c.capLetters || c.all !== c.caps)) {
      sums.push(`<p><strong>${fmt(c.all)}</strong> from numeral letters of either case ${esc(c.letters)}.</p>`);
    }
    if (c.withW !== c.all) {
      sums.push(`<p>If W counts as VV, the sum is <strong>${fmt(c.capsWithW)}</strong> for capitals and <strong>${fmt(c.withW)}</strong> for either case.</p>`);
    }
    return `<section class="panel"><h3>${linked('Chronogram')}</h3>${sums.join('') || '<p>No numeral letters found.</p>'}
      ${strip(conventions.chronogram.ratings)}${evidence(['chronogram'])}</section>`;
  }

  function gloss(unknownLetters) {
    const entries = (unknownLetters || []).filter(letter => Object.hasOwn(letters, letter));
    if (!entries.length) return '';
    return `<section class="panel letter-gloss"><h3>Alphabetic numeral gloss for ${esc(entries.join(', '))}</h3>
      <p>Check which list and which letter case your source uses. These reference values do not enter the readings above.</p>
      <dl>${entries.map(letter => `<dt><strong>${esc(letter)}</strong></dt>
        ${letters[letter].map(entry => {
          const source = sourceById[entry.source];
          return `<dd>${esc(entry.value)} · ${sourceLink(source.url, source.title)}</dd>`;
        }).join('')}`).join('')}</dl>
      ${evidence(['medievalLetters'])}</section>`;
  }

  function readingValue(reading) {
    return reading.value === null ? reading.values.map(fmt).join(' and ') : fmt(reading.value);
  }

  const plainExplanations = {
    additive4: 'Add the repeated signs together.',
    irregularSub: 'This uses subtraction outside the six modern pairs.',
    runSub: 'Subtract the total of the smaller signs from the larger one.',
    oddOrder: 'Read each smaller sign before a larger one as subtraction.',
    additiveSum: 'Add the value of every sign.',
    multiplicative: 'The superscript multiplier applies to the signs before it.',
    multiplicativePlain: 'A sign on the line multiplies the signs before it.',
    vigesimal: 'Read the group marked XX as counting in twenties.',
    separate: 'Read each group as a separate number.',
    vinculum: 'The thousands bar multiplies the signs it covers by 1,000.',
    frame: 'Read the frame as multiplication by 100,000.',
    apostrophus: 'Read the apostrophus signs as grouped values.',
    minim: 'This reading treats some handwritten strokes as different letters.',
    distinctionMarks: 'Read the distinction bar as a mark around the numeral.',
  };

  function answerCard(result) {
    const [first, ...others] = result.readings;
    const selected = R.PERIODS.findIndex(p => p.id === period.value);
    const best = selected < 0 ? Math.max(...first.scores.map(R.weight)) : R.weight(first.scores[selected]);
    const canonical = first.modern && first.modern === R.expandRoman(result.numeral);
    let explanation = [...first.features].map(id => plainExplanations[id]).find(Boolean)
      || 'Add the values of the individual signs and any subtractive pairs.';
    if (result.ordinal) {
      const position = first.value;
      const suffix = position % 100 >= 11 && position % 100 <= 13
        ? 'th' : ({ 1: 'st', 2: 'nd', 3: 'rd' }[position % 10] || 'th');
      explanation = `In “${result.input}”, ${result.numeral} means ${fmt(position)}${suffix} in the sequence.`;
    } else if (canonical) {
      explanation = `Add ${first.breakdown.match(/\d[\d,]*/g).join(' + ')}.`;
    } else if (R.expandRoman(result.numeral) === 'IIII' && first.value === 4) {
      explanation = 'Four ones add to 4, a form used on some clock faces.';
    }

    let alternatives = '';
    if (others.length) {
      const values = new Intl.ListFormat('en-GB', { type: 'disjunction' }).format(others.slice(0, 3).map(readingValue));
      const onlySum = others.length === 1 && others[0].method === 'sum';
      const intro = onlySum ? 'Adding every sign gives' : 'Other conventions could give';
      alternatives = `<p class="answer-alternatives">${intro} <a href="#reading-details" data-reveal>${esc(values)}${others.length > 3 ? ' or more' : ''}</a>.</p>`;
    }

    let label = 'Most likely reading';
    if (result.ordinal) label = 'Position in a sequence';
    else if (canonical) label = 'Value in standard notation';
    else if (best === 0 || first.features.has('ignored')) label = 'Tentative reading';

    return `<section class="panel answer" aria-label="Answer">
      <p class="answer-label">${label}${selected >= 0 && !result.ordinal ? `<span> · ${esc(R.PERIODS[selected].short)}</span>` : ''}</p>
      <output class="answer-value" for="q">${esc(readingValue(first))}</output>
      ${first.modern ? `<p class="answer-form"><strong>${esc(first.modern)}</strong> is the standard modern form.</p>` : ''}
      <p>${linked(explanation)}</p>${alternatives}${presetContext()}
    </section>`;
  }

  function conversionCard({ conversion: { value, forms } }) {
    const [first, ...others] = forms;
    if (!first) return '';
    const barred = first.convention === 'vinculum';
    return `<section class="panel answer" aria-label="Answer">
      <p class="answer-label">${fmt(value)} in Roman numerals</p>
      <output class="answer-value" for="q">${esc(first.numeral)}</output>
      <p>${barred ? linked('The vinculum multiplies the barred part by 1,000.') : 'Standard modern form.'}</p>
      ${others.map(form => `<p class="answer-alternatives"><strong>${esc(form.numeral)}</strong> ·
        ${linked(form.clock ? 'Additive notation used on clocks' : 'Additive notation')}${barred ? ' with a ' + linked('vinculum') : ''}</p>`).join('')}
      ${presetContext()}
      <details class="evidence"><summary>Evidence and sources</summary>
        ${featureEvidence([...new Set([first.convention, ...others.map(form => form.clock ? 'clockIIII' : form.convention)])])}
      </details>
    </section>`;
  }

  function presetContext() {
    if (!currentPreset?.topic) return '';
    const { kind, topic, why, url } = currentPreset;
    return `<p class="preset-context"><strong>${esc(topic)}.</strong> ${linked(why)}
      ${kind === 'constructed' ? '<span class="muted">Constructed example.</span>' : sourceLink(url, 'Source')}</p>`;
  }

  function shortReference(id) {
    const source = sourceById[id];
    return `${source.author} (${source.year})`;
  }

  function noteText(reading, others, input) {
    const ids = [...new Set([...reading.features].flatMap(id => conventions[id].citations))];
    const matching = presets.filter(preset => preset.kind === 'attested'
      && preset.input.trim().toUpperCase() === input.toUpperCase()
      && preset.values.includes(reading.value)
      && preset.convention_ids.some(id => reading.features.has(id)));
    const idsInOrder = [...new Set([...matching.map(preset => preset.source),
      ...ids.map(shortReference)])];
    const shortSources = idsInOrder.slice(0, 3).join(', ');
    const more = others.length ? ` Other readings: ${others.map(other => {
      const value = readingValue(other);
      return other.features.has('multiplicativePlain') ? value + ' (multiplier on the line)' : value;
    }).join(', ')}.` : '';
    return `${input} — read as ${readingValue(reading)} (${reading.explanation.toLowerCase()}${shortSources ? ', references: ' + shortSources : ''}).${more} ${noteCitation()}`;
  }

  function noteCitation() {
    const url = new URL(location.href);
    url.hash = stateHash(q.value, period.value, mode.value, date.value);
    const accessed = new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' });
    return `Roman Numeral Reader, ${url.href}, accessed ${accessed}.`;
  }

  function copyAction(note, value) {
    const index = readingNotes.push(note) - 1;
    return `<div class="copy-action">
      <button type="button" data-copy-note="${index}" aria-label="Copy as note for ${esc(value)}">Copy as note</button> <span role="status"></span>
    </div>`;
  }

  async function copyNote(button) {
    const note = readingNotes[Number(button.dataset.copyNote)];
    const action = button.parentElement;
    const status = action.querySelector('[role="status"]');
    action.querySelector('textarea')?.remove();
    try {
      await navigator.clipboard.writeText(note);
    } catch {
      if (!action.isConnected) return;
      // Some offline files and iframes lack permission for the Clipboard API.
      const field = document.createElement('textarea');
      field.readOnly = true;
      field.setAttribute('aria-label', 'Reading note');
      field.value = note;
      action.append(field);
      field.select();
      let copied = false;
      try { copied = document.execCommand('copy'); } catch { /* Leave the selected note available. */ }
      if (!copied) {
        field.focus();
        field.select();
        status.textContent = 'Note selected. Copy it using your browser’s copy command.';
        return;
      }
      field.remove();
      button.focus({ preventScroll: true });
    }
    status.textContent = 'Note copied.';
  }

  function readingCard(r, others, input) {
    const value = readingValue(r);
    const modern = r.modern && r.modern !== R.expandRoman(input)
      ? `<span class="modern">${esc(r.modern)}</span>` : '';
    const alternatives = r.also.length
      ? `<p class="also">Other explanations for this value · ${r.also.map(a => linked(a.explanation)).join(' / ')}</p>` : '';
    const ids = [...r.features, ...r.also.flatMap(a => [...a.features])];
    return `<article class="panel reading">
      <div class="value">${esc(value)}${modern}</div>
      <div><div class="expl">${linked(r.explanation)}</div><div class="breakdown">${linked(r.breakdown)}</div>
        ${strip(r.scores)}${alternatives}
        ${copyAction(noteText(r, others, input), value)}
      </div>
      ${evidence(ids)}
    </article>`;
  }

  function dateReadings(result) {
    if (!result.years.length) return '';
    if (date.value === 'indiction') {
      const years = [...result.years].sort((a, b) => a.year - b.year);
      const [lo, hi] = periods[period.value].years;
      const from = [...new Set(years.map(y => y.from))].join(', ');
      return `<section class="panel"><h3>Candidate years for ${linked('indiction')} ${esc(from)}</h3>
        <p>January reckoning, ${Math.max(lo, 1)}–${hi} CE. The number repeats every 15 years.</p>
        <ul class="candidates">${years.map(y => `<li>${esc(y.text)}</li>`).join('')}</ul>
        ${evidence(['indiction'])}</section>`;
    }
    return '<h2>Date readings</h2>' + result.years.map(y => {
      const convention = conventions[y.feature];
      const references = convention.citations.slice(0, 3).map(shortReference).join(', ');
      const note = `${result.input} — read as ${y.text} (${convention.label}, from ${fmt(y.from)}, references: ${references}). ${noteCitation()}`;
      return `<article class="panel reading">
      <div class="value">${esc(y.text)}</div><div><strong>${linked(convention.label)}</strong>
      <p class="muted">From the reading ${fmt(y.from)}.</p>${strip(y.scores)}
      ${copyAction(note, y.text)}</div>
      ${evidence([y.feature])}</article>`;
    }).join('');
  }

  function render() {
    const labels = { number: 'Enter a Roman numeral or a number', passage: 'Paste a passage', chronogram: 'Phrase as written' };
    const placeholders = { number: 'e.g. MCMXCIX, 2026 or Henry VIII', passage: 'e.g. Paid .xx. for cloth and XII for thread.', chronogram: 'e.g. MIserICorDIae' };
    const isPassage = mode.value === 'passage';
    const isChronogram = mode.value === 'chronogram';
    $('input-label').textContent = labels[mode.value];
    $('insert').hidden = isChronogram;
    q.rows = isPassage ? 5 : 1;
    q.classList.toggle('passage', isPassage);
    q.placeholder = placeholders[mode.value];
    saveState();
    readingNotes = [];
    const result = R.analyse(q.value, { mode: mode.value, period: period.value, date: date.value });
    $('period-field').hidden = isChronogram || Boolean(result.conversion);
    $('date-field').hidden = isChronogram || Boolean(result.conversion || result.ordinal);
    if (!result.input) { out.innerHTML = ''; return; }
    if (result.mode === 'passage') { out.innerHTML = passage(result); return; }
    if (result.mode === 'chronogram') { out.innerHTML = chronogram(result); return; }

    const warnings = result.warnings.map(w => `<div class="warn">${linked(w)}</div>`).join('');
    if (result.conversion) { out.innerHTML = conversionCard(result) + warnings; return; }

    const expanded = $('reading-details')?.open;
    let html = result.readings.length ? answerCard(result) : '<p class="muted">No numeral value found.</p>';
    html += warnings + dateReadings(result);
    let detail = result.readings.map((r, i) =>
      readingCard(r, result.readings.filter((_, j) => i !== j), result.numeral)).join('');
    detail += gloss(result.glossLetters);
    if (result.tokens.length || result.notes.length || result.hints.length) {
      detail += `<details class="panel"><summary>Signs and transcription notes</summary>
        <div class="tokens">${result.tokens.map(t => `<div class="tok">
          <b>${esc(t.raw.replace('^', ''))}</b><span>${t.mult ? '×' : ''}${fmt(t.value)}</span></div>`).join('')}</div>
        ${[...result.hints, ...result.notes].map(n => `<p class="muted">${linked(n)}</p>`).join('')}</details>`;
    }
    if (detail) {
      const title = result.readings.length > 1 ? 'Why could this be something else?'
        : result.readings.length ? 'How is this read?' : 'Signs and letter gloss';
      html += `<details id="reading-details" class="panel secondary"${expanded ? ' open' : ''}>
        <summary>${title}</summary>
        ${result.readings.length ? '<h2>Possible readings</h2>' : ''}${detail}
      </details>`;
    }
    out.innerHTML = html;
  }

  const examplePeriod = $('example-period'), exampleConvention = $('example-convention');
  const exampleGroup = $('example-group'), exampleKind = $('example-kind');
  const pageSize = 12;
  let visibleCount = pageSize;

  function renderPreset(example, index) {
    const id = example.convention_ids[0];
    const source = example.kind === 'constructed'
      ? `Constructed teaching example · reference ${sourceLink(sourceById[conventions[id].citations[0]].url, sourceById[conventions[id].citations[0]].title)}`
      : `${esc(example.date)} · ${sourceLink(example.url, example.source)}`;
    const expected = example.options?.date && typeof example.values[0] === 'number'
      ? example.values.map(year => `${display(year)} CE`) : example.values.map(display);
    return `<article class="panel preset">
      <button type="button" class="preset-button" data-preset="${index}">${esc(example.input)}</button>
      <p class="expected">Expected · ${esc(expected.join(' / '))}</p>
      <p>${example.topic ? `<strong>${esc(example.topic)}.</strong> ` : ''}${linked(example.why)}</p>
      <p class="muted example-source">${source}</p>
      ${example.source_status ? `<p class="muted">${esc(example.source_status)}</p>` : ''}
      </article>`;
  }

  function renderPresets() {
    const groupByPeriod = exampleGroup.value === 'period';
    const groups = groupByPeriod
      ? R.PERIODS.map(p => [p.id, { label: p.label }]) : alphaConventions;
    const matches = presets.flatMap((example, index) => {
      if (examplePeriod.value && example.period_id !== examplePeriod.value) return [];
      if (exampleKind.value && example.kind !== exampleKind.value) return [];
      if (exampleConvention.value && !example.convention_ids.includes(exampleConvention.value)) return [];
      const group = groupByPeriod ? example.period_id : exampleConvention.value || example.convention_ids[0];
      return [{ example, index, group }];
    });
    const sorted = groups.flatMap(([id]) => matches.filter(row => row.group === id)).slice(0, visibleCount);
    $('examples').innerHTML = groups.map(([id, group]) => {
      const rows = sorted.filter(row => row.group === id);
      if (!rows.length) return '';
      return `<h3>${esc(group.label)}</h3><div class="preset-group">${rows.map(row => renderPreset(row.example, row.index)).join('')}</div>`;
    }).join('');
    $('example-count').textContent = matches.length
      ? `Showing ${sorted.length} of ${matches.length} examples` : 'No examples match these filters.';
    $('more-examples').hidden = sorted.length >= matches.length;
  }

  const palette = [
    ['Ↄ', 'Ↄ', 'reversed C'], ['ↀ', 'ↀ', '1,000'], ['ↁ', 'ↁ', '5,000'], ['ↂ', 'ↂ', '10,000'],
    ['ↇ', 'ↇ', '50,000'], ['ↈ', 'ↈ', '100,000'], ['̅', 'x̅', 'bar over last sign'],
    ['ᵐ', 'ᵐ', '×1,000'], ['ᶜ', 'ᶜ', '×100'], ['ˣˣ', 'ˣˣ', '×20'], ['ᵒ', 'ᵒ', 'ending'],
    ['j', 'j', ''], ['·', '·', ''], ['ↆ', 'ↆ', 'early 50'], ['ↅ', 'ↅ', 'late 6'],
  ];
  $('palette').innerHTML = palette.map(([, sign, meaning], i) => `<button type="button" data-sign="${i}">${esc(sign)}
    ${meaning ? `<small>${esc(meaning)}</small>` : ''}</button>`).join('');
  $('palette').addEventListener('click', event => {
    const button = event.target.closest('button');
    if (!button) return;
    currentPreset = null;
    q.setRangeText(palette[Number(button.dataset.sign)][0], q.selectionStart, q.selectionEnd, 'end');
    q.focus();
    render();
  });

  const periodOptions = R.PERIODS.map(p => option(p.id, `${p.label} (${p.range})`)).join('');
  period.innerHTML = option('unknown', 'Not sure') + periodOptions;
  examplePeriod.innerHTML = option('', 'All periods') + R.PERIODS.map(p => option(p.id, p.short)).join('');
  exampleConvention.innerHTML = option('', 'All conventions') + alphaConventions.map(([id, f]) => option(id, f.label)).join('');
  $('rating-key').innerHTML = [...levels].map(([score, [, description]]) => `<li>${cell(score)} ${esc(description)}</li>`).join('');
  $('rule-list').innerHTML = alphaConventions.map(([id, f]) => `<div>${featureEvidence([id])}
    ${f.referenceOnly ? '' : strip(f.ratings)}</div>`).join('');
  $('source-summary').textContent = `Sources · ${sources.length} listed, ${sources.filter(s => s.read_full_text).length} read in full`;
  $('source-list').innerHTML = sources.map(s => `<li>${sourceLink(s.url, s.title)}
    <span class="muted"> · ${esc(s.author)} (${esc(s.year)}) · ${s.read_full_text ? 'Read in full' : 'Partial reading or record only'}
    ${s.pages ? ` · ${esc(s.pages)}` : ''}</span></li>`).join('');

  for (const control of [exampleGroup, examplePeriod, exampleConvention, exampleKind]) {
    control.addEventListener('change', () => { visibleCount = pageSize; renderPresets(); });
  }
  $('more-examples').addEventListener('click', () => { visibleCount += pageSize; renderPresets(); });
  const starters = presets.map((example, index) => ({ example, index }))
    .filter(({ example }) => example.start).sort((a, b) => a.example.start - b.example.start);
  $('starter-examples').innerHTML = starters.map(({ example, index }) => `<button type="button" data-preset="${index}">
    <strong>${esc(example.input)}</strong><span>${esc(example.topic)}</span></button>`).join('');

  $('glossary-list').innerHTML = glossary.map(entry => `<dt id="term-${entry.id}" tabindex="-1"><strong>${esc(entry.term)}</strong></dt>
    <dd>${esc(entry.definition)}</dd>`).join('');
  $('typing-help').innerHTML = 'Use <code>^m</code>, <code>^c</code> and <code>^xx</code> for ' + linked('superscripts')
    + ', <code>_X</code> for a bar over X, <code>|X̅|</code> for a framed numeral and <code>(I)</code> or <code>CIↃ</code> for the '
    + linked('apostrophus') + '. A ' + linked('final j') + ' can stand for i, and a u for v.';

  function selectPreset(event) {
    const button = event.target.closest('[data-preset]');
    if (!button) return;
    const example = presets[Number(button.dataset.preset)];
    currentPreset = example;
    q.value = example.input;
    period.value = example.period_id;
    mode.value = example.options?.mode || 'number';
    date.value = example.options?.date || '';
    if ($('reading-details')) $('reading-details').open = false;
    render();
    q.focus({ preventScroll: true });
    q.scrollIntoView({ block: 'center' });
  }

  $('examples').addEventListener('click', selectPreset);
  $('starter-examples').addEventListener('click', selectPreset);
  out.addEventListener('click', event => {
    if (event.target.closest('.result-link')) requestAnimationFrame(() => q.focus());
    const copy = event.target.closest('[data-copy-note]');
    if (copy) copyNote(copy);
  });
  document.querySelector('main').addEventListener('click', event => {
    const link = event.target.closest('[data-reveal]');
    if (!link || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const target = $(link.hash.slice(1));
    if (!target) return;
    event.preventDefault();
    for (let group = target.closest('details'); group; group = group.parentElement.closest('details')) {
      group.open = true;
    }
    (target.querySelector('summary') || target).focus({ preventScroll: true });
    target.scrollIntoView({ block: 'start' });
  });
  for (const control of [mode, period, date]) control.addEventListener('change', render);
  q.addEventListener('input', () => { currentPreset = null; render(); });
  window.addEventListener('hashchange', loadState);
  $('page-header').hidden = new URLSearchParams(location.search).get('embed') === '1';
  loadState();
  renderPresets();
})();
