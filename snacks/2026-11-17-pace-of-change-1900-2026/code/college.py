"""Share of adults 25+ with four or more years of college (EDUC general code 10 or 11), 1940-2024.
Usage: python3 -I college.py CSV_GZ OUT_CSV"""
import csv, gzip, sys
from collections import defaultdict
num, den = defaultdict(float), defaultdict(float)
for r in csv.DictReader(gzip.open(sys.argv[1], "rt")):
    if int(r["AGE"]) < 25 or r["EDUC"] in ("", "0"):
        continue
    y, w = int(r["YEAR"]), float(r["PERWT"])
    if int(r["EDUC"]) == 0:
        continue
    den[y] += w
    if int(r["EDUC"]) >= 10:
        num[y] += w
with open(sys.argv[2], "w", newline="") as f:
    wr = csv.writer(f); wr.writerow(["year", "pct"])
    for y in sorted(den):
        wr.writerow([y, round(100 * num[y] / den[y], 2)])
print(open(sys.argv[2]).read())
