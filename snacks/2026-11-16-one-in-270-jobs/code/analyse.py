"""Aggregate IPUMS extract: weighted employed counts by OCC1950 for 1950 and 2010,
plus which 2010 OCC codes feed each OCC1950 category. Usage: python3 -I analyse.py DATA_DIR OUT_DIR"""
import csv, glob, gzip, json, os, re, sys
import xml.etree.ElementTree as ET
from collections import defaultdict

DATA, OUT = sys.argv[1], sys.argv[2]
ddi = glob.glob(os.path.join(DATA, "*.xml"))[0]
root = ET.parse(ddi).getroot()
ns = {"d": root.tag.split("}")[0].strip("{")}
labels = {}
for var in root.iter(f"{{{ns['d']}}}var"):
    name = var.get("name")
    if name in ("OCC1950", "OCC"):
        for c in var.findall("d:catgry", ns):
            l = c.find("d:labl", ns); labels[(name, int(c.find("d:catValu", ns).text))] = (l.text or "").strip() if l is not None else ""

emp = defaultdict(float)  # (year, occ1950) -> employed
lf = defaultdict(float)   # (year, occ1950) -> employed + unemployed with occupation
feed = defaultdict(lambda: defaultdict(float))  # occ1950 -> occ2010code -> employed
datafile = glob.glob(os.path.join(DATA, "*.csv.gz"))[0]
with gzip.open(datafile, "rt") as f:
    for r in csv.DictReader(f):
        es = int(r["EMPSTAT"])
        if es not in (1, 2):
            continue
        y, o, w = int(r["YEAR"]), int(r["OCC1950"]), float(r["PERWT"])
        lf[(y, o)] += w
        if es == 1:
            emp[(y, o)] += w
            if y == 2010:
                feed[o][int(r["OCC"])] += w

codes = sorted({o for (_, o) in emp} | {o for (_, o) in lf} |
               {v for (n, v) in labels if n == "OCC1950"})
rows = []
for o in codes:
    if o >= 970:  # non-occupational / unknown
        continue
    e50, e10 = emp.get((1950, o), 0.0), emp.get((2010, o), 0.0)
    top = sorted(feed[o].items(), key=lambda kv: -kv[1])[:3]
    rows.append({
        "occ1950": o, "label": labels.get(("OCC1950", o), "?"),
        "emp1950": round(e50), "emp2010": round(e10),
        "ratio": round(e10 / e50, 3) if e50 else None,
        "fed_by_2010_codes": "; ".join(f"{labels.get(('OCC', c), c)} ({round(w)})" for c, w in top),
    })
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "occ1950_1950_vs_2010.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)
tot = {y: sum(v for (yy, _), v in emp.items() if yy == y) for y in (1950, 2010)}
json.dump({"categories": len(rows), "employed_total": tot}, open(os.path.join(OUT, "summary.json"), "w"), indent=1)
print(len(rows), tot)
