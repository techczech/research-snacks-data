"""Pace of change in US work and life, 1900-2024, from IPUMS USA census and ACS microdata.
Usage: python3 -I analyse.py DATA_DIR OUT_DIR
Writes: dist_occ1950.csv and dist_ind1950.csv (share of workers per category per year), groups.csv (major
occupation groups and sectors), indicators.csv (other census measures), dissimilarity.csv (pairs of years)."""
import csv, glob, gzip, os, re, sys
from collections import defaultdict

DATA, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
ddi = open(glob.glob(os.path.join(DATA, "*.xml"))[0]).read()


def labels(var):
    block = re.search(rf'<var[^>]*name="{var}".*?</var>', ddi, re.S).group(0)
    return {int(v): re.sub(r"\s+", " ", l).strip() for v, l in re.findall(r"<catValu>(\d+)</catValu>\s*<labl>(.*?)</labl>", block, re.S)}


OL, IL = labels("OCC1950"), labels("IND1950")

# OCC1950 major groups (1950 census scheme)
def ogroup(o):
    for lo, hi, g in ((0, 99, "Professional and technical"), (100, 123, "Farmers and farm managers"),
                      (200, 290, "Managers, officials and proprietors"), (300, 390, "Clerical"), (400, 490, "Sales"),
                      (500, 595, "Craft workers"), (600, 690, "Machine operatives"), (700, 720, "Private household workers"),
                      (730, 790, "Service workers"), (810, 890, "Farm labourers"), (900, 970, "Labourers")):
        if lo <= o <= hi:
            return g


def sector(i):
    if 105 <= i <= 126: return "Agriculture, forestry, fishing"
    if 206 <= i <= 499: return "Mining, construction, manufacturing"
    if 506 <= i <= 946: return "Services, trade, transport, government"


occ, ind, grp, sec = (defaultdict(float) for _ in range(4))
ind_tot = defaultdict(lambda: defaultdict(float))  # year -> measure -> weighted numerator/denominator
n = 0
with gzip.open(glob.glob(os.path.join(DATA, "*.csv.gz"))[0], "rt") as f:
    for r in csv.DictReader(f):
        n += 1
        y, w, age = int(r["YEAR"]), float(r["PERWT"]), int(r["AGE"])
        t = ind_tot[y]
        t["pop"] += w
        if r["FARM"] == "2": t["farm_pop"] += w
        if r["BPL"] and int(r["BPL"]) >= 150 and int(r["BPL"]) < 999: t["foreign"] += w
        if 14 <= age <= 17:
            t["teens"] += w
            if r["SCHOOL"] == "2": t["teens_school"] += w
        if 16 <= age <= 64 and r["SEX"] == "2" and r["MARST"] in ("1", "2"):
            t["mw"] += w
            if r["LABFORCE"] == "2": t["mw_lf"] += w
        if age < 16 or r["LABFORCE"] != "2":
            continue
        t["lf"] += w
        if r["SEX"] == "2": t["lf_women"] += w
        o = int(r["OCC1950"])
        if o < 980:  # 979 not yet classified, 980+ non-occupational or unknown
            t["occ_cl"] += w
            occ[(y, o)] += w
            g = ogroup(o)
            if g: grp[(y, g)] += w
        i = int(r["IND1950"])
        if 100 <= i <= 946:
            t["ind_cl"] += w
            ind[(y, i)] += w
            s = sector(i)
            if s: sec[(y, s)] += w
        if r["CLASSWKR"] == "1":
            t["self"] += w
        if r["CLASSWKR"] in ("1", "2"):
            t["cw_cl"] += w
print("rows", n)
years = sorted(ind_tot)


def shares(counts, key_total):
    out = defaultdict(dict)
    for (y, k), v in counts.items():
        out[y][k] = v / ind_tot[y][key_total]
    return out


O, I = shares(occ, "occ_cl"), shares(ind, "ind_cl")
G, S = shares(grp, "occ_cl"), shares(sec, "ind_cl")


def write_dist(name, D, lab):
    keys = sorted({k for y in D for k in D[y]})
    with open(os.path.join(OUT, name), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["code", "label"] + years)
        for k in keys:
            w.writerow([k, lab.get(k, "?")] + [round(D[y].get(k, 0) * 100, 4) for y in years])


write_dist("dist_occ1950.csv", O, OL)
write_dist("dist_ind1950.csv", I, IL)
with open(os.path.join(OUT, "groups.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["kind", "group"] + years)
    for kind, D in (("occupation group", G), ("sector", S)):
        for k in sorted({k for y in D for k in D[y]}):
            w.writerow([kind, k] + [round(D[y].get(k, 0) * 100, 2) for y in years])

ind_rows = [
    ("Workers in labour force (millions)", lambda t: t["lf"] / 1e6),
    ("Women as share of the labour force (%)", lambda t: 100 * t["lf_women"] / t["lf"]),
    ("Married women 16-64 in the labour force (%)", lambda t: 100 * t["mw_lf"] / t["mw"]),
    ("Population living on farms (%)", lambda t: 100 * t["farm_pop"] / t["pop"]),
    ("Workers self-employed (%)", lambda t: 100 * t["self"] / t["cw_cl"] if t["cw_cl"] else None),
    ("Teenagers 14-17 in school (%)", lambda t: 100 * t["teens_school"] / t["teens"]),
    ("Population born abroad (%)", lambda t: 100 * t["foreign"] / t["pop"]),
]
with open(os.path.join(OUT, "indicators.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["indicator"] + years)
    for name, fn in ind_rows:
        vals = []
        for y in years:
            try:
                v = fn(ind_tot[y]); vals.append("" if v is None else round(v, 2))
            except ZeroDivisionError:
                vals.append("")
        w.writerow([name] + vals)


def dis(D, a, b):
    ks = set(D[a]) | set(D[b])
    return 50 * sum(abs(D[a].get(k, 0) - D[b].get(k, 0)) for k in ks)


pairs = [(years[k], years[k + 1]) for k in range(len(years) - 1)]
pairs += [(1900, 1970), (1960, 2024), (1950, 2024), (1900, 1960), (1970, 2024)]
with open(os.path.join(OUT, "dissimilarity.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["from", "to", "years", "occupations_D", "industries_D", "occupation_groups_D", "sectors_D"])
    for a, b in pairs:
        w.writerow([a, b, b - a, round(dis(O, a, b), 1), round(dis(I, a, b), 1), round(dis(G, a, b), 1), round(dis(S, a, b), 1)])
for p in ("dissimilarity.csv", "indicators.csv", "groups.csv"):
    print(open(os.path.join(OUT, p)).read())
