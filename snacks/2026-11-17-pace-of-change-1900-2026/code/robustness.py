"""Same dissimilarity index with occupations coded to the 1990 and 2010 census schemes (later schemes
split modern work more finely, so they work against the claim's earlier period).
Usage: python3 -I robustness.py CSV_GZ OUT_DIR"""
import csv, gzip, os, sys
from collections import defaultdict

SRC, OUT = sys.argv[1], sys.argv[2]
cnt = {v: defaultdict(float) for v in ("OCC1990", "OCC2010")}
tot = {v: defaultdict(float) for v in cnt}
for r in csv.DictReader(gzip.open(SRC, "rt")):
    if int(r["AGE"]) < 16:
        continue
    y, w = int(r["YEAR"]), float(r["PERWT"])
    for v in cnt:
        if not r[v].strip(): continue
        c = int(r[v])
        if (v == "OCC1990" and 3 <= c <= 890) or (v == "OCC2010" and 10 <= c <= 9830):
            cnt[v][(y, c)] += w; tot[v][y] += w
years = sorted({y for y, _ in cnt["OCC1990"]})


def D(v, a, b):
    if not tot[v][a] or not tot[v][b]:
        return float("nan")  # scheme not coded for that year
    ks = {c for (y, c) in cnt[v] if y in (a, b)}
    return 50 * sum(abs(cnt[v].get((a, k), 0) / tot[v][a] - cnt[v].get((b, k), 0) / tot[v][b]) for k in ks)


pairs = [(years[k], years[k + 1]) for k in range(len(years) - 1)] + [(1900, 1970), (1960, 2024), (1950, 2024)]
with open(os.path.join(OUT, "dissimilarity_robustness.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["from", "to", "years", "occ1990_D", "occ2010_D", "occ1990_categories_used_from", "occ1990_categories_used_to"])
    for a, b in pairs:
        na = sum(1 for (y, c) in cnt["OCC1990"] if y == a); nb = sum(1 for (y, c) in cnt["OCC1990"] if y == b)
        w.writerow([a, b, b - a, round(D("OCC1990", a, b), 1), round(D("OCC2010", a, b), 1), na, nb])
print(open(os.path.join(OUT, "dissimilarity_robustness.csv")).read())
