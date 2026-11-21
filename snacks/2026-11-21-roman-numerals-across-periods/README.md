---
title: Roman numerals across periods
date: 2026-11-21
provenance: Roman Numeral Reader v3, commit b15675de12c18fcd8c1092417a0671854d84f786
---

# Roman numerals across periods

Data and code for the [Research Snack](https://researchsnacks.semanticmachines.fyi/2026-11-21-roman-numerals-across-periods/). Open [the reader](code/index.html) from a local clone. It works offline.

Install Node.js and uv, then run these commands from the repository root.

```sh
uv sync --locked
uv run check.py 2026-11-21-roman-numerals-across-periods
```

The check rebuilds [the per-preset results](expected/preset-results.csv), [coverage by period](expected/preset-coverage.csv) and [the reported counts](expected/summary.csv). The unit of comparison is a preset. Several presets share a source. A match means that the reported value occurs among the reader's results for that preset. See [the two mismatches](data/preset-check.md), [method](METHOD.md) and [source and reuse decisions](DATA-SOURCES.md).
