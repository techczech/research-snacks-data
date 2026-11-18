"""Weighted employed counts by OCC1990 x census year, and rise-and-fall candidates.
Usage: python3 -I analyse2.py DATA_DIR OUT_DIR"""
import csv, glob, gzip, json, os, re, sys
from collections import defaultdict

DATA, OUT = sys.argv[1], sys.argv[2]
ddi = open(glob.glob(os.path.join(DATA, "*.xml"))[0]).read()
block = re.search(r'<var[^>]*name="OCC1990".*?</var>', ddi, re.S).group(0)
labels = {int(v): re.sub(r"\s+", " ", l).strip() for v, l in
          re.findall(r"<catValu>(\d+)</catValu>\s*<labl>(.*?)</labl>", block, re.S)}

cnt = defaultdict(float)
with gzip.open(glob.glob(os.path.join(DATA, "*.csv.gz"))[0], "rt") as f:
    for r in csv.DictReader(f):
        if r["EMPSTAT"] != "1":
            continue
        cnt[(int(r["YEAR"]), int(r["OCC1990"]))] += float(r["PERWT"])

years = sorted({y for y, _ in cnt})
codes = sorted({o for _, o in cnt})
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "occ1990_by_year.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["occ1990", "label"] + years)
    for o in codes:
        w.writerow([o, labels.get(o, "?")] + [round(cnt.get((y, o), 0)) for y in years])

cands = []
for o in codes:
    s = [cnt.get((y, o), 0) for y in years]
    pk = max(s); iy = s.index(pk)
    if pk < 20000 or not (1960 <= years[iy] <= 2000):
        continue
    if s[0] < 0.5 * pk and s[-1] < 0.35 * pk:
        cands.append((labels.get(o, "?"), years[iy], [round(x) for x in s]))
cands.sort(key=lambda c: -max(c[2]))
print(years)
for c in cands:
    print(c[0][:50].ljust(50), c[1], c[2])
