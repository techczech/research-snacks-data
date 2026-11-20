#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["vl-convert-python>=1.6,<2"]
# ///
"""Rebuild the figures and searchable table from shareable stand-off annotations.
Run: uv run snacks/2026-11-17-can-a-cake-be-sickly/code/build-sickly-figures.py
No corpus queries or new linguistic classifications are performed.
"""
from collections import Counter
import csv
from html import escape
import json
from pathlib import Path
import re
import vl_convert as vlc

ENTRY = Path(__file__).resolve().parent.parent
OUT = ENTRY / "actual" / "charts"
OUT.mkdir(parents=True, exist_ok=True)
food = list(csv.DictReader((ENTRY / "data/food-annotations.csv").open()))
assert len(food) == 15
LABELS = {
    "attributive": "Attributive",
    "explicit verbal complement": "Explicit verbal complement",
    "elliptical/supplementary": "Ellipsis or supplement",
}
counts = Counter((r["construction"], r["coordination"]) for r in food)
assert counts == {("attributive", "sole"): 2, ("attributive", "coordinated"): 3,
                  ("explicit verbal complement", "sole"): 3, ("explicit verbal complement", "coordinated"): 2,
                  ("elliptical/supplementary", "sole"): 4, ("elliptical/supplementary", "coordinated"): 1}
BASE = {"$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "config": {"font": "system-ui, sans-serif", "view": {"stroke": None},
                   "axis": {"labelFontSize": 12, "titleFontSize": 12},
                   "legend": {"orient": "top", "title": None, "labelFontSize": 12},
                   "title": {"anchor": "start", "fontSize": 17, "subtitleFontSize": 12}}}


def write_figure(name, data, spec):
    with (OUT / f"{name}.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0])); writer.writeheader(); writer.writerows(data)
    spec = {**BASE, **spec, "data": {"url": f"charts/{name}.csv"}}
    (OUT / f"{name}.vl.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n")
    # The fallback uses the same spec and exact rows, with a fixed publication width.
    static = {**spec, "data": {"values": data}}
    if static.get("width") == "container": static["width"] = 580
    (OUT / f"{name}.png").write_bytes(vlc.vegalite_to_png(static, scale=2))


plot = [{"construction": label, "coordination": "Sole adjective" if coord == "sole" else "Coordinated",
         "cases": counts[(key, coord)]} for key, label in LABELS.items() for coord in ["sole", "coordinated"]]
write_figure("1-sickly-food-constructions", plot, {
    "width": "container", "height": 215,
    "title": {"text": "Sickly can be the only adjective",
              "subtitle": ["15 selected BNC food/drink cases; not population proportions.",
                           "Explicit complements include object predication."]},
    "params": [{"name": "pick", "select": {"type": "point", "fields": ["coordination"]}, "bind": "legend"}],
    "mark": {"type": "bar", "cornerRadiusEnd": 2},
    "encoding": {
        "x": {"field": "cases", "type": "quantitative", "title": "Selected cases", "scale": {"domain": [0, 4]}, "axis": {"tickMinStep": 1}},
        "y": {"field": "construction", "type": "nominal", "title": None, "sort": list(LABELS.values()), "axis": {"labelLimit": 165}},
        "yOffset": {"field": "coordination", "sort": ["Sole adjective", "Coordinated"]},
        "color": {"field": "coordination", "scale": {"domain": ["Sole adjective", "Coordinated"], "range": ["#2679a4", "#ca641f"]}},
        "opacity": {"condition": {"param": "pick", "value": 1}, "value": 0.18},
        "tooltip": [{"field": "construction", "title": "Construction"}, {"field": "coordination", "title": "Adjectives"}, {"field": "cases", "title": "Selected cases", "type": "quantitative"}]}})

rows = list(csv.DictReader((ENTRY / "data/example-locators.csv").open()))
assert len(rows) == 39
# A Vega-Lite version and PNG accompany the enhanced HTML table and its exact CSV.
write_figure("2-sickly-kwic", rows, {
    "width": 830, "height": {"step": 24},
    "title": {"text": "39 curated sickly example locators", "subtitle": "Corpus text withheld; recover contexts through licensed access."},
    "transform": [{"window": [{"op": "row_number", "as": "row"}]},
                  {"calculate": "datum.corpus + ' | ' + datum.document_id + ' | ' + datum.token + ' | ' + datum.construction + ' | ' + datum.reading", "as": "excerpt"}],
    "mark": {"type": "text", "align": "left", "baseline": "middle", "limit": 820, "fontSize": 16},
    "encoding": {"x": {"value": 0}, "y": {"field": "row", "type": "ordinal", "axis": None},
                 "text": {"field": "excerpt"},
                 "tooltip": [{"field": field} for field in rows[0]]}})

COLS = [("corpus", "Corpus"), ("document_id", "Document ID"), ("token", "Token anchor"),
        ("construction", "Construction"), ("coordination", "Coordination"), ("reading", "Reading")]
body = []
for row in rows:
    cells = []
    for field, _ in COLS:
        val = escape(str(row[field]))
        cells.append(f'<td>{val}</td>')
    body.append(f'<tr data-corpus="{escape(row["corpus"])}">' + ''.join(cells) + '</tr>')
head = ''.join(f'<th scope="col" aria-sort="none"><button type="button" data-sort="{i}">{label}</button></th>' for i, (_, label) in enumerate(COLS))
options = '<option value="">All corpora</option>' + ''.join(f'<option>{escape(c)}</option>' for c in dict.fromkeys(r['corpus'] for r in rows))
html = r'''<div id="sickly-kwic" class="sickly-kwic">
<style>
.sickly-kwic{font-size:16px;color:#1d2433;color-scheme:light}.sickly-kwic table{color:inherit}.sickly-kwic a{color:#17618b}.sickly-kwic .controls{display:flex;gap:.8rem;flex-wrap:wrap;align-items:end;margin-block:1rem}
.sickly-kwic .controls[hidden]{display:none}.sickly-kwic label{display:grid;gap:.25rem}.sickly-kwic input,.sickly-kwic select,.sickly-kwic button{font:inherit;color:inherit;background:transparent;border:1px solid #888;border-radius:4px;padding:.35rem .5rem}
.sickly-kwic .scroll{overflow:auto;border:1px solid #888}.sickly-kwic table{margin:0;width:auto;max-width:100%}
.sickly-kwic th{position:sticky;top:0;background:Canvas;z-index:1}.sickly-kwic th button{border:0;font-weight:600;cursor:pointer}
.sickly-kwic td{vertical-align:top}.sickly-kwic td:nth-child(5){min-width:17rem}.sickly-kwic td:last-child{max-width:20rem;overflow-wrap:anywhere}
.sickly-kwic :focus-visible{outline:2px solid #2679a4;outline-offset:2px}.sickly-kwic tr[hidden]{display:none}
@media print{.sickly-kwic .scroll{max-height:none;overflow:visible}.sickly-kwic table{min-width:0;font-size:.65rem}.sickly-kwic .controls{display:none}}
</style>
<div class="controls" hidden>
<label>Search all columns<input type="search" id="sickly-search" placeholder="Try sole, visual or BNC"></label>
<label>Corpus<select id="sickly-corpus">OPTIONS</select></label>
<button type="button" id="sickly-export">Export visible CSV</button>
</div>
<p id="sickly-count" role="status" aria-live="polite">39 of 39 examples. Select a heading to sort.</p>
<div class="scroll" tabindex="0" role="region" aria-label="Sickly example locators">
<table><caption>Stand-off annotations and source anchors; corpus contexts are withheld.</caption><thead><tr>HEAD</tr></thead><tbody>BODY</tbody></table>
</div>
<p><a href="charts/2-sickly-kwic.csv" download>All rows (CSV)</a> · <a href="charts/2-sickly-kwic.vl.json">Vega-Lite version</a> · <a href="https://github.com/techczech/research-snacks-data/blob/main/snacks/2026-11-17-can-a-cake-be-sickly/README.md">Method and licensed reconstruction</a></p>
<script>
(function(){
 const root=document.getElementById('sickly-kwic');
 const input=root.querySelector('input'), corpus=root.querySelector('select'), tbody=root.querySelector('tbody');
 const trs=Array.from(tbody.rows), source=DATA;
 const records=new Map(trs.map((tr,i)=>[tr,source[i]]));
 root.querySelector('.controls').hidden=false;
 function filter(){const q=input.value.toLocaleLowerCase();let n=0;trs.forEach(tr=>{
   tr.hidden=!(tr.textContent.toLocaleLowerCase().includes(q)&&(!corpus.value||tr.dataset.corpus===corpus.value));if(!tr.hidden)n++;
 });root.querySelector('#sickly-count').textContent=n+' of 39 examples. Select a heading to sort.';}
 input.addEventListener('input',filter);corpus.addEventListener('change',filter);
 root.querySelectorAll('[data-sort]').forEach(button=>button.addEventListener('click',()=>{
   const th=button.parentElement, asc=th.getAttribute('aria-sort')!=='ascending', col=Number(button.dataset.sort);
   root.querySelectorAll('th').forEach(h=>h.setAttribute('aria-sort','none'));th.setAttribute('aria-sort',asc?'ascending':'descending');
   Array.from(tbody.rows).sort((a,b)=>a.cells[col].textContent.localeCompare(b.cells[col].textContent,undefined,{numeric:true})*(asc?1:-1)).forEach(tr=>tbody.appendChild(tr));
 }));
 root.querySelector('#sickly-export').addEventListener('click',()=>{
   const fields=Object.keys(source[0]), quote=v=>'"'+String(v).replaceAll('"','""')+'"';
   const visible=Array.from(tbody.rows).filter(tr=>!tr.hidden).map(tr=>records.get(tr));
   const csv=[fields.map(quote).join(','),...visible.map(r=>fields.map(f=>quote(r[f])).join(','))].join('\r\n')+'\r\n';
   const url=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));const a=document.createElement('a');
   a.href=url;a.download='sickly-visible-examples.csv';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
 });
})();
</script></div>'''
html = html.replace('OPTIONS', options).replace('HEAD', head).replace('BODY', '\n'.join(body)).replace('DATA', json.dumps(rows, ensure_ascii=False).replace('</', '<\\/'))
(OUT/'2-sickly-kwic.html').write_text(html+'\n')
print('Built two PNG/CSV/Vega-Lite sets and the searchable, sortable 39-row stand-off locator table.')
