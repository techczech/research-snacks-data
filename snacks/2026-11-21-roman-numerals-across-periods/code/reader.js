(function () {
  'use strict';
  const R = globalThis.RomanReader;
  const { conventions, sources, presets, letters } = globalThis.RomanResearch;
  const $ = id => document.getElementById(id);
  const q = $('q'), mode = $('mode'), period = $('period'), date = $('date'), out = $('out');
  const periods = Object.fromEntries(R.PERIODS.map(p => [p.id, p]));
  const sourceById = Object.fromEntries(sources.map(s => [s.id, s]));
  const fmt = number => number.toLocaleString('en-GB');
  const display = value => typeof value === 'number' ? fmt(value) : value;
  const esc = value => String(value).replace(/[&<>"]/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[ch]));
  const option = (value, label) => `<option value="${esc(value)}">${esc(label)}</option>`;
  const alphaConventions = Object.entries(conventions).sort(([, a], [, b]) => a.label.localeCompare(b.label, 'en-GB'));

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
      return `<div class="rule"><strong>${esc(f.label)}</strong>
        <p>${esc(f.note)}</p><p class="muted">${esc(f.justification)}</p>
        ${f.where ? `<p><strong>Where</strong> ${esc(f.where)}</p>` : ''}
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
    return `<section class="panel"><h3>Chronogram</h3>${sums.join('') || '<p>No numeral letters found.</p>'}
      ${strip(conventions.chronogram.ratings)}${evidence(['chronogram'])}</section>`;
  }

  function gloss(unknownLetters) {
    const entries = (unknownLetters || []).filter(letter => Object.hasOwn(letters, letter));
    if (!entries.length) return '';
    return `<details class="panel"><summary>Alphabetic numeral gloss for ${esc(entries.join(', '))}</summary>
      <p>Check which list and which letter case your source uses. These reference values do not enter the readings above.</p>
      <dl>${entries.map(letter => `<dt><strong>${esc(letter)}</strong></dt>
        ${letters[letter].map(entry => {
          const source = sourceById[entry.source];
          return `<dd>${esc(entry.value)} · ${sourceLink(source.url, source.title)}</dd>`;
        }).join('')}`).join('')}</dl>
      ${evidence(['medievalLetters'])}</details>`;
  }

  function readingCard(r, leading) {
    const value = r.value === null ? r.values.map(fmt).join(' and ') : fmt(r.value);
    const modern = r.modern && r.modern !== q.value.trim().toUpperCase()
      ? `<span class="modern">${r.modern}</span>` : '';
    const alternatives = r.also.length
      ? `<p class="also">Other explanations for this value · ${r.also.map(a => esc(a.explanation)).join(' / ')}</p>` : '';
    const ids = [...r.features, ...r.also.flatMap(a => [...a.features])];
    return `<article class="panel reading${leading ? ' top' : ''}">
      <div class="value">${value}${modern}</div>
      <div><div class="expl">${esc(r.explanation)}</div><div class="breakdown">${esc(r.breakdown)}</div>
        ${strip(r.scores)}${alternatives}</div>
      ${evidence(ids)}
    </article>`;
  }

  function dateReadings(result) {
    if (!result.years.length) return '';
    if (date.value === 'indiction') {
      const years = [...result.years].sort((a, b) => a.year - b.year);
      const [lo, hi] = periods[period.value].years;
      const from = [...new Set(years.map(y => y.from))].join(', ');
      return `<section class="panel"><h3>Candidate years for indiction ${esc(from)}</h3>
        <p>January reckoning, ${Math.max(lo, 1)}–${hi} CE. The number repeats every 15 years.</p>
        <ul class="candidates">${years.map(y => `<li>${esc(y.text)}</li>`).join('')}</ul>
        ${evidence(['indiction'])}</section>`;
    }
    return '<h2>Date readings</h2>' + result.years.map(y => `<article class="panel reading">
      <div class="value">${esc(y.text)}</div><div><strong>${esc(conventions[y.feature].label)}</strong>
      <p class="muted">From the reading ${fmt(y.from)}.</p>${strip(y.scores)}</div>
      ${evidence([y.feature])}</article>`).join('');
  }

  function render() {
    const labels = { number: 'Numeral as written', passage: 'Paste a passage', chronogram: 'Phrase as written' };
    const placeholders = { number: 'e.g. Mᵒiiijᶜlvj', passage: 'e.g. Paid .xx. for cloth and XII for thread.', chronogram: 'e.g. MIserICorDIae' };
    const isPassage = mode.value === 'passage';
    $('input-label').textContent = labels[mode.value];
    $('insert').hidden = mode.value === 'chronogram';
    $('date-field').hidden = mode.value === 'chronogram';
    q.rows = isPassage ? 5 : 1;
    q.classList.toggle('passage', isPassage);
    q.placeholder = placeholders[mode.value];
    saveState();
    const result = R.analyse(q.value, { mode: mode.value, period: period.value, date: date.value });
    if (!result.input) { out.innerHTML = ''; return; }
    if (result.mode === 'passage') { out.innerHTML = passage(result); return; }
    if (result.mode === 'chronogram') { out.innerHTML = chronogram(result); return; }

    let html = result.warnings.map(w => `<div class="warn">${esc(w)}</div>`).join('');
    if (result.readings.length) {
      const selected = R.PERIODS.findIndex(p => p.id === period.value);
      const [first] = result.readings;
      const best = selected < 0 ? Math.max(...first.scores.map(R.weight)) : R.weight(first.scores[selected]);
      html += '<h2>Possible readings</h2>' + result.readings.map((r, i) => readingCard(r, i === 0 && best >= 2)).join('');
    } else html += '<p class="muted">No numeral value found.</p>';
    html += dateReadings(result) + gloss(result.glossLetters);
    if (result.tokens.length || result.notes.length || result.hints.length) {
      html += `<details class="panel"><summary>Signs and transcription notes</summary>
        <div class="tokens">${result.tokens.map(t => `<div class="tok">
          <b>${esc(t.raw.replace('^', ''))}</b><span>${t.mult ? '×' : ''}${fmt(t.value)}</span></div>`).join('')}</div>
        ${[...result.hints, ...result.notes].map(n => `<p class="muted">${esc(n)}</p>`).join('')}</details>`;
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
      <p>${esc(example.why)}</p>
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
  $('source-summary').textContent = `${sources.length} sources · ${sources.filter(s => s.read_full_text).length} read in full`;
  $('source-list').innerHTML = sources.map(s => `<li>${sourceLink(s.url, s.title)}
    <span class="muted"> · ${esc(s.author)} (${esc(s.year)}) · ${s.read_full_text ? 'Read in full' : 'Partial reading or record only'}
    ${s.pages ? ` · ${esc(s.pages)}` : ''}</span></li>`).join('');

  for (const control of [exampleGroup, examplePeriod, exampleConvention, exampleKind]) {
    control.addEventListener('change', () => { visibleCount = pageSize; renderPresets(); });
  }
  $('more-examples').addEventListener('click', () => { visibleCount += pageSize; renderPresets(); });
  $('examples').addEventListener('click', event => {
    const button = event.target.closest('[data-preset]');
    if (!button) return;
    const example = presets[Number(button.dataset.preset)];
    q.value = example.input;
    period.value = example.period_id;
    mode.value = example.options?.mode || 'number';
    date.value = example.options?.date || '';
    render();
    q.focus({ preventScroll: true });
    q.scrollIntoView({ block: 'center' });
  });
  out.addEventListener('click', event => {
    if (event.target.closest('.result-link')) requestAnimationFrame(() => q.focus());
  });
  for (const control of [mode, period, date]) control.addEventListener('change', render);
  q.addEventListener('input', render);
  window.addEventListener('hashchange', loadState);
  $('page-header').hidden = new URLSearchParams(location.search).get('embed') === '1';
  loadState();
  renderPresets();
})();
