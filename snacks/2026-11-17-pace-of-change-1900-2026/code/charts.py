"""Charts for the pace-of-change snack: for each chart a CSV of the plotted data, a Vega-Lite spec
(interactive on the page) and a PNG rendered from the same spec (fallback and social image).
Usage: uv run --with vl-convert-python python3 charts.py ENTRY_DIR"""
import copy, csv, json, os, sys
import vl_convert as vlc

P = sys.argv[1]
D, C = os.path.join(P, "data"), os.path.join(P, "charts")
os.makedirs(C, exist_ok=True)
BLUE, ORANGE, INK, GREY, TEAL, GOLD = "#2a78d6", "#eb6834", "#1d2433", "#8f8e88", "#1f9e89", "#c9a227"
SRC = "Source: IPUMS USA (www.ipums.org), census 1900–2000 and American Community Survey 2010, 2024."
BASE = {"$schema": "https://vega.github.io/schema/vega-lite/v5.json", "background": "white",
        "config": {"font": "Inter, Helvetica, Arial, sans-serif", "view": {"stroke": None},
                   "axis": {"labelColor": "#52514e", "titleColor": "#52514e", "gridColor": "#e4e3df", "domainColor": "#cfcdc6"},
                   "legend": {"orient": "top", "title": None, "labelFontSize": 12, "labelLimit": 300},
                   "title": {"anchor": "start", "fontSize": 17, "subtitleColor": "#52514e", "subtitleFontSize": 12.5}}}


def rd(name):
    return list(csv.DictReader(open(os.path.join(D, name))))


def save(name, rows, spec, width=720):
    with open(os.path.join(C, f"{name}.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    page = {**BASE, **spec, "data": {"url": f"charts/{name}.csv"}}
    json.dump(page, open(os.path.join(C, f"{name}.vl.json"), "w"), indent=1, ensure_ascii=False)
    png = copy.deepcopy(page); png["data"] = {"values": rows}
    fix = lambda s: s.update({"width": width}) if s.get("width") == "container" else None
    fix(png)
    for k in ("vconcat",):
        for s in png.get(k, []):
            fix(s)
    open(os.path.join(C, f"{name}.png"), "wb").write(vlc.vegalite_to_png(png, scale=2))


def typed(rows):
    out = []
    for r in rows:
        out.append({k: (float(v) if v.replace(".", "", 1).replace("-", "", 1).isdigit() else v) for k, v in r.items()})
    return out


# 1. Change per decade, with events
dis = [r for r in rd("dissimilarity.csv") if int(r["to"]) - int(r["from"]) <= 14]
ev = rd("events.csv")
rows = [{"row": "change", "from": int(r["from"]), "to": int(r["to"]), "measure": "Occupations (about 270 categories)",
         "value": float(r["occupations_D"]), "event": "", "kind": ""} for r in dis]
rows += [{"row": "change", "from": int(r["from"]), "to": int(r["to"]), "measure": "Industries (about 150 categories)",
          "value": float(r["industries_D"]), "event": "", "kind": ""} for r in dis]
rows += [{"row": "event", "from": int(e["year"]), "to": int(e["year"]), "measure": "", "value": 0, "event": e["event"], "kind": e["kind"]} for e in ev]
X = {"field": "from", "type": "quantitative", "scale": {"domain": [1900, 2026]}, "axis": {"format": "d", "title": None, "values": list(range(1900, 2030, 10))}}
save("1-change-per-decade", rows, {
    "title": {"text": "How much the US job mix changed in each decade", "subtitle": ["Share of workers who would have to change category to make one census look like the next (dissimilarity index, %). Below: key events; hover for names.", SRC]},
    "vconcat": [
        {"width": "container", "height": 230, "transform": [{"filter": "datum.row == 'change'"}],
         "params": [{"name": "pick", "select": {"type": "point", "fields": ["measure"]}, "bind": "legend"}],
         "mark": {"type": "rule", "strokeWidth": 5, "strokeCap": "round"},
         "encoding": {"x": X, "x2": {"field": "to"}, "y": {"field": "value", "type": "quantitative", "title": "% of workers", "scale": {"domain": [0, 20]}},
                      "color": {"field": "measure", "type": "nominal", "scale": {"range": [BLUE, ORANGE]}},
                      "opacity": {"condition": {"param": "pick", "value": 1}, "value": 0.15},
                      "tooltip": [{"field": "measure", "title": "Measure"}, {"field": "from", "title": "From"}, {"field": "to", "title": "To"}, {"field": "value", "title": "% of workers"}]}},
        {"width": "container", "height": 70, "transform": [{"filter": "datum.row == 'event'"}],
         "mark": {"type": "point", "filled": True, "size": 90, "opacity": 0.9},
         "encoding": {"x": X, "y": {"field": "kind", "type": "nominal", "title": None, "axis": {"labelLimit": 140}},
                      "color": {"field": "kind", "type": "nominal", "scale": {"domain": ["Technology", "Economy", "War and politics"], "range": [TEAL, GOLD, GREY]}, "legend": None},
                      "tooltip": [{"field": "from", "title": "Year"}, {"field": "event", "title": "Event"}]}}],
    "resolve": {"scale": {"color": "independent"}}})

# 2. The two spans side by side
span = {(r["from"], r["to"]): r for r in rd("dissimilarity.csv")}
SP = [("1900", "1970", "1900 to 1970 (70 years)"), ("1950", "2024", "1950 to 2024 (74 years)"), ("1960", "2024", "1960 to 2024 (64 years)")]
M = [("occupations_D", "Occupations (about 270)"), ("industries_D", "Industries (about 150)"), ("occupation_groups_D", "Occupation groups (11)"), ("sectors_D", "Sectors (3)")]
rows = [{"span": lab, "measure": mlab, "pct": float(span[(a, b)][m])} for a, b, lab in SP for m, mlab in M]
save("2-two-spans", rows, {
    "title": {"text": "Two long spans: how different was the end from the start?", "subtitle": ["Share of workers who would have to change category to make the later year look like the earlier one (%)", SRC]},
    "width": "container", "height": {"step": 13},
    "encoding": {"y": {"field": "measure", "type": "nominal", "title": None, "sort": [m for _, m in M], "axis": {"labelLimit": 200}},
                 "yOffset": {"field": "span", "sort": [l for _, _, l in SP]},
                 "x": {"field": "pct", "type": "quantitative", "title": "% of workers", "scale": {"domain": [0, 60]}},
                 "color": {"field": "span", "type": "nominal", "sort": [l for _, _, l in SP], "scale": {"range": [ORANGE, "#7fb0ea", BLUE]}},
                 "tooltip": [{"field": "span", "title": "Span"}, {"field": "measure", "title": "Measure"}, {"field": "pct", "title": "% of workers"}]},
    "layer": [{"mark": {"type": "bar", "cornerRadiusEnd": 3}},
              {"mark": {"type": "text", "align": "left", "dx": 4, "color": "#52514e", "fontSize": 11}, "encoding": {"text": {"field": "pct", "format": ".0f"}}}]})

# 3. Occupation groups
g = rd("groups.csv"); yrs = [k for k in g[0] if k.isdigit()]
rows = [{"group": r["group"], "year": int(y), "share_pct": float(r[y])} for r in g if r["kind"] == "occupation group" for y in yrs
        if not (r["group"] == "Private household workers" and int(y) >= 2000)]
save("3-occupation-groups", rows, {
    "title": {"text": "What kind of work people did, 1900–2024", "subtitle": ["Share of workers in each major occupation group (%). Click the legend to pick a group.", SRC]},
    "width": "container", "height": 340,
    "params": [{"name": "pick", "select": {"type": "point", "fields": ["group"]}, "bind": "legend"}],
    "mark": {"type": "line", "point": {"size": 30, "filled": True}, "strokeWidth": 2.2},
    "encoding": {"x": {"field": "year", "type": "quantitative", "axis": {"format": "d", "title": None}, "scale": {"domain": [1900, 2024]}},
                 "y": {"field": "share_pct", "type": "quantitative", "title": "% of workers"},
                 "color": {"field": "group", "type": "nominal", "legend": {"columns": 3, "symbolType": "stroke"},
                           "scale": {"range": [INK, BLUE, "#7fb0ea", ORANGE, "#f4a77f", TEAL, "#8fd1c5", GOLD, "#e6d38f", GREY, "#c9c7c0"]}},
                 "opacity": {"condition": {"param": "pick", "value": 1}, "value": 0.1},
                 "tooltip": [{"field": "group", "title": "Group"}, {"field": "year", "title": "Year"}, {"field": "share_pct", "title": "% of workers"}]}})

# 4. Life beyond jobs
ind = rd("indicators.csv"); yrs = [k for k in ind[0] if k.isdigit()]
skip = {("Teenagers 14-17 in school (%)", "1950"), ("Teenagers 14-17 in school (%)", "1970")}
keep = ["Population living on farms (%)", "Married women 16-64 in the labour force (%)", "Women as share of the labour force (%)",
        "Workers self-employed (%)", "Teenagers 14-17 in school (%)", "Population born abroad (%)"]
SHORT = {"Population living on farms (%)": "Living on farms", "Married women 16-64 in the labour force (%)": "Married women in work",
         "Women as share of the labour force (%)": "Women's share of workers", "Workers self-employed (%)": "Self-employed",
         "Teenagers 14-17 in school (%)": "Teenagers 14–17 in school", "Population born abroad (%)": "Born abroad"}
rows = [{"measure": SHORT[r["indicator"]], "year": int(y), "pct": float(r[y])} for r in ind if r["indicator"] in keep
        for y in yrs if r[y] != "" and (r["indicator"], y) not in skip]
if os.path.exists(os.path.join(D, "college.csv")):
    rows += [{"measure": "College graduates (25+)", "year": int(r["year"]), "pct": float(r["pct"])} for r in rd("college.csv")]
order = [SHORT[m] for m in keep] + ["College graduates (25+)"]
save("4-life-beyond-jobs", rows, {
    "title": {"text": "Beyond jobs: farms, women's work, school, migration", "subtitle": ["% of people or workers. Each panel has its own scale. Hover for values.", SRC]},
    "facet": {"field": "measure", "type": "nominal", "sort": order, "title": None, "header": {"labelFontSize": 12.5, "labelFontWeight": "bold", "labelAnchor": "start", "labelLimit": 230}},
    "columns": 3, "resolve": {"scale": {"y": "independent"}},
    "spec": {"width": 200, "height": 120,
             "layer": [{"mark": {"type": "line", "color": BLUE, "strokeWidth": 2.2, "point": {"color": BLUE, "size": 25}},
                        "encoding": {"x": {"field": "year", "type": "quantitative", "scale": {"domain": [1900, 2024]}, "axis": {"format": "d", "title": None, "values": [1900, 1950, 2000]}},
                                     "y": {"field": "pct", "type": "quantitative", "title": None, "scale": {"zero": True}},
                                     "tooltip": [{"field": "measure"}, {"field": "year", "title": "Year"}, {"field": "pct", "title": "%"}]}}]}})

# 5. When job titles entered written English
ng = [r for r in rd("ngram_takeoff.csv") if r["take_off_year"] and r["title"] not in ("prompt engineer", "systems analyst", "electrician", "stewardess", "lineman", "recording engineer", "television producer")]
rows = [{"title": r["title"], "group": r["group"], "take_off_year": int(r["take_off_year"]), "peak_year": int(r["peak_year"])} for r in ng]
save("5-new-job-titles", rows, {
    "title": {"text": "When new job titles took off in print", "subtitle": ["Year a title first reached 10% of its peak frequency in Google Books (English, 1880–2022). Hover for the peak year.", "Source: Google Books Ngram Viewer. Titles chosen in advance, two lists of 25; seven with scanning noise left out."]},
    "width": "container", "height": {"step": 15},
    "mark": {"type": "point", "filled": True, "size": 70},
    "encoding": {"x": {"field": "take_off_year", "type": "quantitative", "scale": {"domain": [1890, 2025]}, "axis": {"format": "d", "title": "Take-off year"}},
                 "y": {"field": "title", "type": "nominal", "sort": {"field": "take_off_year"}, "title": None, "axis": {"labelLimit": 220}},
                 "color": {"field": "group", "type": "nominal", "scale": {"range": [ORANGE, BLUE]}},
                 "tooltip": [{"field": "title", "title": "Title"}, {"field": "take_off_year", "title": "Take-off"}, {"field": "peak_year", "title": "Peak"}, {"field": "group", "title": "List"}]}})
print("ok")
