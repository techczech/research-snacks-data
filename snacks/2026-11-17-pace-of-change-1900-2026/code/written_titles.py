"""Job titles as written on the census forms (OCCSTR), 1900-1940 1% samples, people in the labour force.
Finds titles common in 1940 (at least MIN sample people) that nobody in the 1900 and 1910 samples wrote.
Usage: python3 -I written_titles.py OCCSTR_CSV_GZ OUT_DIR [MIN]"""
import csv, gzip, os, re, sys
from collections import Counter, defaultdict

SRC, OUT = sys.argv[1], sys.argv[2]
MIN = int(sys.argv[3]) if len(sys.argv) > 3 else 15
cnt = defaultdict(Counter)
wt = defaultdict(Counter)
tot = Counter()
for r in csv.DictReader(gzip.open(SRC, "rt", encoding="latin-1")):
    t = re.sub(r"[^A-Z0-9 ]", " ", r["OCCSTR"].upper())
    t = re.sub(r"\s+", " ", t).strip()
    if not t:
        continue
    y = int(r["YEAR"]); w = float(r["PERWT"])
    cnt[y][t] += 1; wt[y][t] += w; tot[y] += w
early = set(cnt[1900]) | set(cnt[1910])
new = [(t, cnt[1940][t], wt[1940][t]) for t in cnt[1940] if cnt[1940][t] >= MIN and t not in early]
new.sort(key=lambda x: -x[1])
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "written_titles_new_by_1940.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["title_as_written_1940", "sample_people_1940", "weighted_workers_1940", "in_1920_sample", "in_1930_sample"])
    for t, c, ww in new:
        w.writerow([t, c, round(ww), cnt[1920][t], cnt[1930][t]])
share = sum(ww for _, _, ww in new) / tot[1940]
print(f"titles in 1940 with >= {MIN} people and absent in 1900+1910: {len(new)}; share of 1940 workers with a written title: {share*100:.1f}%")
print("distinct titles per year:", {y: len(cnt[y]) for y in sorted(cnt)})
for t, c, ww in new[:80]:
    print(t.ljust(40), c, cnt[1920][t], cnt[1930][t])
