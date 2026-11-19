---
title: Checking revolution speed and a 2011 claim
date: 2026-11-19
provenance: NAVCO 1.3 and explicitly transcribed historical boundaries
---

# Check revolution speed

This folder checks the calculations behind [the Research Snack](https://researchsnacks.semanticmachines.fyi/2026-11-19-revolution-speed-2011-redo/). From the repository root run:

```sh
uv sync --locked
uv run check.py 2026-11-19-revolution-speed-2011-redo
```

The offline check regenerates eleven CSV tables in a temporary folder and compares their exact bytes with `expected/`. No account, key or network request is needed. It checks 23 versus 17 elapsed days and the six-day gap; sixteen selected clocks; alternative endpoints; era medians and exclusions; NAVCO success denominators, onset cohorts and boundary examples; and transcribed survey facts. It does not independently validate the transcriptions or historical judgements.

Read [METHOD.md](METHOD.md) for the rule behind each table and [DATA-SOURCES.md](DATA-SOURCES.md) for terms and the provider's exact citation. `data/cases.csv` and `data/boundaries.csv` retain judgement reasons. The SHA-256 inventory in [manifest.json](manifest.json) identifies the shipped inputs, scripts and expected outputs.

For chart exports, first run `uv run python snacks/2026-11-19-revolution-speed-2011-redo/code/reproduce.py snacks/2026-11-19-revolution-speed-2011-redo/expected`, then `uv run python snacks/2026-11-19-revolution-speed-2011-redo/code/charts.py`. The latter writes matching CSV, PNG and Vega-Lite assets. These use the same plotted records, numeric units and source cutoff as the page.
