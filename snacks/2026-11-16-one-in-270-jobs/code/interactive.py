"""Interactive versions of the charts: one CSV (the plotted data) and one Vega-Lite spec per chart.
Usage: python3 -I interactive.py ENTRY_DIR   (reads data/, writes charts/<name>.csv and charts/<name>.vl.json)"""
import csv, json, os, sys

P = sys.argv[1]
OUT = os.path.join(P, "charts")
rows = {int(r["occ1950"]): r for r in csv.DictReader(open(os.path.join(P, "data", "occ1950_1950_vs_2010.csv")))}
tr = {int(r["occ1990"]): r for r in csv.DictReader(open(os.path.join(P, "data", "occ1990_by_year.csv")))}
_y = list(csv.reader(open(os.path.join(P, "data", "occ1990_by_year.csv"))))
TOTAL = {int(_y[0][i]): sum(int(r[i]) for r in _y[1:]) for i in range(2, len(_y[0]))}  # all employed people per year
share = lambda n, y: round(n / TOTAL[y] * 100, 4)
TECH, DEMAND, INK, GREY, LIGHT = "#2a78d6", "#eb6834", "#1d2433", "#a9a8a2", "#dddcd6"
SRC1 = "Source: IPUMS USA (www.ipums.org), employed persons."
SRC2 = "Source: IPUMS USA (www.ipums.org), employed persons."
BASE = {"$schema": "https://vega.github.io/schema/vega-lite/v5.json", "width": "container",
        "config": {"font": "Inter, system-ui, sans-serif", "view": {"stroke": None},
                   "axis": {"labelColor": "#52514e", "titleColor": "#52514e", "gridColor": "#e4e3df", "domainColor": "#e4e3df"},
                   "legend": {"orient": "top", "title": None, "labelFontSize": 13, "symbolSize": 160},
                   "title": {"anchor": "start", "fontSize": 17, "subtitleColor": "#52514e", "subtitleFontSize": 13}}}


def write(name, fields, data, spec):
    with open(os.path.join(OUT, f"{name}.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(data)
    spec = {**BASE, **spec, "data": {"url": f"charts/{name}.csv"}}
    json.dump(spec, open(os.path.join(OUT, f"{name}.vl.json"), "w"), indent=1, ensure_ascii=False)


def legend_select(field):
    return [{"name": "pick", "select": {"type": "point", "fields": [field]}, "bind": "legend"}]


fade = {"condition": {"param": "pick", "value": 1}, "value": 0.18}

# 1. Every 1950 category, by what happened to it
GONE = [761, 365, 360, 325, 542, 520, 960, 631, 785, 304, 752, 751, 645, 501, 525, 571]
S = ["Gone through automation (elevator operator)", "Also gone or nearly gone", "Lost only through reclassification", "Still a category in 2010"]
def status(o, r):
    if o == 761: return S[0]
    if o in GONE: return S[1]
    if int(r["emp2010"]) == 0: return S[2]
    return S[3]
cells = sorted(((status(o, r), r) for o, r in rows.items()), key=lambda t: (S.index(t[0]), -int(t[1]["emp1950"])))
data = [{"occupation": r["label"], "status": st, "workers_1950": int(r["emp1950"]), "workers_2010": int(r["emp2010"]),
         "col": i % 20, "row": i // 20} for i, (st, r) in enumerate(cells)]
write("1-waffle-1950-occupations", list(data[0]), data, {
    "title": {"text": "“Only 1 of 270 jobs from 1950 is obsolete”?",
              "subtitle": f"Each square is one of the {len(rows)} occupation categories of the 1950 US census. Hover for the job."},
    "params": legend_select("status"), "height": {"step": 26},
    "mark": {"type": "rect", "cornerRadius": 2},
    "encoding": {"x": {"field": "col", "type": "ordinal", "axis": None, "scale": {"paddingInner": 0.15}},
                 "y": {"field": "row", "type": "ordinal", "axis": None, "scale": {"paddingInner": 0.15}},
                 "color": {"field": "status", "type": "nominal", "scale": {"domain": S, "range": [INK, TECH, LIGHT, GREY]},
                           "legend": {"columns": 1, "labelLimit": 320}},
                 "opacity": fade,
                 "tooltip": [{"field": "occupation", "title": "Occupation"}, {"field": "status", "title": "In 2010"},
                             {"field": "workers_1950", "title": "Workers 1950", "format": ","},
                             {"field": "workers_2010", "title": "Workers 2010", "format": ","}]}})

# 2. The jobs that went
CAUSE = {761: ("Elevator operators", "Technology"), 365: ("Telegraph operators", "Technology"), 360: ("Telegraph messengers", "Technology"),
         325: ("Railway mail clerks and express messengers", "Technology"), 542: ("Locomotive firemen", "Technology"),
         520: ("Electrotypers and stereotypers", "Technology"), 960: ("Teamsters (horse and wagon)", "Technology"),
         631: ("Bus and streetcar conductors", "Technology"), 785: ("Crossing watchmen and bridge tenders", "Technology"),
         304: ("Baggagemen", "Falling demand"), 752: ("Boarding-house keepers", "Falling demand"), 751: ("Bootblacks", "Falling demand"),
         645: ("Milliners", "Falling demand"), 501: ("Blacksmiths", "Technology"), 525: ("Furriers", "Falling demand")}
data = [{"occupation": n, "workers_1950": int(rows[o]["emp1950"]), "share_of_all_workers_1950_pct": share(int(rows[o]["emp1950"]), 1950),
         "workers_2010": int(rows[o]["emp2010"]), "removed_by": c} for o, (n, c) in CAUSE.items()]
write("2-jobs-that-disappeared", list(data[0]), data, {
    "title": {"text": "The jobs of 1950 that have (nearly) disappeared", "subtitle": ["US workers in each occupation in 1950", SRC1]},
    "height": {"step": 26},
    "encoding": {"y": {"field": "occupation", "type": "nominal", "sort": {"field": "workers_1950", "order": "descending"}, "title": None, "axis": {"labelLimit": 280}},
                 "x": {"field": "workers_1950", "type": "quantitative", "title": "Workers in 1950", "axis": {"format": "~s"}},
                 "tooltip": [{"field": "occupation", "title": "Occupation"}, {"field": "workers_1950", "title": "Workers 1950", "format": ","},
                             {"field": "share_of_all_workers_1950_pct", "title": "Share of all workers 1950 (%)"},
                             {"field": "workers_2010", "title": "Workers 2010", "format": ","}, {"field": "removed_by", "title": "Removed by"}]},
    "layer": [{"mark": {"type": "bar", "cornerRadiusEnd": 3}, "params": legend_select("removed_by"),
               "encoding": {"color": {"field": "removed_by", "type": "nominal", "scale": {"domain": ["Technology", "Falling demand"], "range": [TECH, DEMAND]}},
                            "opacity": fade}},
              {"mark": {"type": "text", "align": "left", "dx": 4, "color": "#52514e"},
               "encoding": {"text": {"field": "workers_1950", "format": ","}}}]})

# 3. Survived on the list, collapsed in the workforce
SHRINK = {624: "Railway brakemen", 684: "Textile weavers", 570: "Pattern and model makers", 100: "Farmers (owners and tenants)",
          512: "Compositors and typesetters", 565: "Paperhangers", 370: "Telephone operators",
          680: "Stationary firemen (boilers)", 674: "Sawyers", 635: "Metal filers, grinders and polishers"}
data = []
for o, n in SHRINK.items():
    a, b = int(rows[o]["emp1950"]), int(rows[o]["emp2010"])
    data.append({"occupation": n, "workers_1950": a, "workers_2010": b, "change_pct": round((b - a) / a * 100, 1), "label": f"−{round((a - b) / a * 100)}%",
                 "share_of_all_workers_1950_pct": share(a, 1950), "share_of_all_workers_2010_pct": share(b, 2010)})
write("3-survived-but-collapsed", list(data[0]), data, {
    "title": {"text": "Still on the list, mostly gone from the workforce", "subtitle": ["Change in US employment 1950–2010", SRC1]},
    "height": {"step": 30},
    "encoding": {"y": {"field": "occupation", "type": "nominal", "sort": {"field": "change_pct", "order": "ascending"}, "title": None, "axis": {"labelLimit": 280}},
                 "x": {"field": "change_pct", "type": "quantitative", "title": "Change 1950–2010 (%)", "scale": {"domain": [-100, 0]}},
                 "tooltip": [{"field": "occupation", "title": "Occupation"}, {"field": "workers_1950", "title": "Workers 1950", "format": ","},
                             {"field": "workers_2010", "title": "Workers 2010", "format": ","}, {"field": "change_pct", "title": "Change (%)"},
                             {"field": "share_of_all_workers_1950_pct", "title": "Share of all workers 1950 (%)"},
                             {"field": "share_of_all_workers_2010_pct", "title": "Share of all workers 2010 (%)"}]},
    "layer": [{"mark": {"type": "bar", "color": TECH, "cornerRadiusEnd": 3}},
              {"mark": {"type": "text", "align": "left", "dx": 6, "color": "white", "fontWeight": "bold"},
               "encoding": {"x": {"field": "change_pct", "type": "quantitative"}, "text": {"field": "label"}}}]})

# 5 and 6. Trends (OCC1990); categories with no comparable code that year are left out
YRS = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2019]
def long(spec_list):
    out = []
    for code, name, drop in spec_list:
        out += [{"occupation": name, "year": y, "workers": int(tr[code][str(y)])} for y in YRS if y not in drop]
    return out
RISE = [(308, "Computer operators", (1950, 1960, 2019)), (385, "Data-entry keyers", (1950, 1960)),
        (315, "Typists", (1950,)), (348, "Telephone operators", ()),
        (774, "Photo-lab workers", ()), (314, "Stenographers", (1950, 2000, 2010, 2019))]
data = long(RISE)
write("5-rise-and-fall", list(data[0]), data, {
    "title": {"text": "Jobs that technology created, then took away", "subtitle": ["US workers. Hover a point for the number.", SRC2]},
    "facet": {"field": "occupation", "type": "nominal", "sort": [r[1] for r in RISE], "title": None,
              "header": {"labelFontSize": 14, "labelFontWeight": "bold", "labelAnchor": "start"}},
    "columns": 3, "resolve": {"scale": {"y": "independent"}},
    "spec": {"width": 165, "height": 140,
             "encoding": {"x": {"field": "year", "type": "quantitative", "scale": {"domain": [1950, 2019]}, "axis": {"format": "d", "values": [1950, 1970, 1990, 2010], "title": None}},
                          "y": {"field": "workers", "type": "quantitative", "axis": {"format": "~s", "title": None}},
                          "tooltip": [{"field": "occupation"}, {"field": "year", "title": "Year"}, {"field": "workers", "title": "Workers", "format": ","}]},
             "layer": [{"mark": {"type": "line", "color": TECH, "strokeWidth": 2.4}},
                       {"mark": {"type": "point", "filled": True, "color": TECH, "size": 50}}]}})

NEW = [(229, "Software developers", (1950, 1960)), (64, "Computer systems analysts and scientists", (1950, 1960))]
data = long(NEW)
write("6-new-work", list(data[0]), data, {
    "title": {"text": "Meanwhile: work nobody did in 1950", "subtitle": ["US workers in two computing occupations that were not census categories before 1970", SRC2]},
    "height": 320,
    "encoding": {"x": {"field": "year", "type": "quantitative", "axis": {"format": "d", "values": YRS[2:], "title": None}, "scale": {"domain": [1970, 2019]}},
                 "y": {"field": "workers", "type": "quantitative", "axis": {"format": "~s", "title": "Workers"}},
                 "color": {"field": "occupation", "type": "nominal", "scale": {"range": [TECH, DEMAND]}, "legend": {"labelLimit": 360}},
                 "opacity": fade,
                 "tooltip": [{"field": "occupation", "title": "Occupation"}, {"field": "year", "title": "Year"}, {"field": "workers", "title": "Workers", "format": ","}]},
    "layer": [{"mark": {"type": "line", "strokeWidth": 2.6}, "params": legend_select("occupation")},
              {"mark": {"type": "point", "filled": True, "size": 60}}]})
print("ok")
