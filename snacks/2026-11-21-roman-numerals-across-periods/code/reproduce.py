"""Run the reader tests and export the observed preset results and totals."""
import csv
import json
from collections import Counter
from pathlib import Path
import subprocess
import sys

CODE = Path(__file__).resolve().parent
SNACK = CODE.parent
PERIODS = {
    "classical": "Classical",
    "early-medieval": "Early medieval",
    "late-medieval": "Late medieval",
    "early-modern": "Early modern",
    "modern": "Modern",
}


def write_table(destination, header, rows):
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def main(output):
    run = subprocess.run(
        ["node", str(CODE / "test.mjs"), "--json"],
        cwd=CODE, check=True, text=True, stdout=subprocess.PIPE,
    )
    results = json.loads(run.stdout.splitlines()[-1])
    presets = results["presetResults"]
    write_table(
        output / "preset-results.csv",
        ["input", "period", "expected", "reader_outputs", "result"],
        ((row["input"], PERIODS[row["period"]], " / ".join(map(str, row["expected"])),
          " / ".join(map(str, row["values"])), "Matched" if row["match"] else "Mismatch")
         for row in presets),
    )
    counts = Counter((row["period"], row["match"]) for row in presets)
    write_table(
        output / "preset-coverage.csv", ["period", "result", "presets"],
        ((label, result, counts[period, match]) for period, label in PERIODS.items()
         for match, result in ((True, "Matched"), (False, "Mismatch"))),
    )
    refs = json.loads((SNACK / "data/references.json").read_text())
    examples = json.loads((SNACK / "data/examples.json").read_text())
    write_table(output / "summary.csv", ["measure", "count"], [
        ("Attested presets", len(presets)),
        ("Attested presets matched", sum(row["match"] for row in presets)),
        ("Attested presets with a source availability note", sum("source_status" in row for row in examples)),
        ("Constructed presets", results["constructed"]),
        ("Regression and data checks passed", results["total"] - results["fail"]),
        ("Cleaned reference records", len(refs)),
        ("Cleaned references read in full", sum(ref["read_full_text"] for ref in refs)),
    ])


if __name__ == "__main__":
    main(Path(sys.argv[1]))
