"""Aggregate your own IPUMS extract; never publish the private input directory.
Usage: uv run snacks/2026-11-17-pace-of-change-1900-2026/code/aggregate-inputs.py MODE INPUT OUTPUT
MODE: main (directory), robustness (csv.gz), college (csv.gz), titles (csv.gz).
The original scripts run first. Extra sufficient statistics support offline recalculation.
"""
import csv, runpy, sys
from pathlib import Path
mode, source, output = sys.argv[1:]
out = Path(output); out.mkdir(parents=True, exist_ok=True)
code = Path(__file__).parent
script = {"main": "analyse.py", "robustness": "robustness.py", "college": "college.py", "titles": "written_titles.py"}[mode]
sys.argv = [script, source, str(out / "college.csv" if mode == "college" else out)]
ns = runpy.run_path(str(code / script), run_name="__main__")
def write(name, fields, rows):
    with (out / name).open("w", newline="") as f:
        w = csv.writer(f); w.writerow(fields); w.writerows(rows)
if mode == "main":
    totals = ns["ind_tot"]
    fields = sorted({k for values in totals.values() for k in values})
    write("indicator-counts.csv", ["year"] + fields,
          [[y] + [totals[y].get(k, 0) for k in fields] for y in sorted(totals)])
if mode == "main":
    write("distribution-shares.csv", ["measure", "year", "code", "share"],
          [[measure, y, k, value] for measure, name in [("occupations_D", "O"), ("industries_D", "I"), ("occupation_groups_D", "G"), ("sectors_D", "S")]
           for y, counts in sorted(ns[name].items()) for k, value in sorted(counts.items())])
if mode == "robustness":
    write("robustness-counts.csv", ["scheme", "year", "code", "workers"],
          [[v, y, c, n] for v, counts in ns["cnt"].items() for (y, c), n in sorted(counts.items())])
if mode == "college":
    write("college-counts.csv", ["year", "graduates", "adults"],
          [[y, ns["num"][y], ns["den"][y]] for y in sorted(ns["den"])])
