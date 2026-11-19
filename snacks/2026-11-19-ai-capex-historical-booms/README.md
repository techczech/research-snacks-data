---
title: AI spending and historical booms — check the calculations
date: 2026-11-19
provenance: AI capex historical-booms source captures and checked calculations
---

# Check AI spending and historical booms

The [snack page](https://researchsnacks.semanticmachines.fyi/2026-11-19-ai-capex-historical-booms/) asks whether the GDP share is unprecedented and whether revenue growth establishes likely investment returns.

From the repository root:

```sh
uv sync --locked
uv run check.py 2026-11-19-ai-capex-historical-booms
```

The offline check rebuilds 17 CSV tables and compares them with `expected/`. It makes no network or model calls and requires no API keys. `code/reproduce.py` can also run with standard-library Python: pass an output directory. To render the original chart sets, copy the expected CSVs into an entry's `data/` alongside the inputs and run `uv run python code/charts-ai-capex.py ENTRY_DIRECTORY`.

This validates the displayed arithmetic from selected transcribed source facts, not independent source transcription, a complete historical peak search, an audited AI revenue aggregate or investor profitability. No copyrighted original image, complete book, workbook, company filing, private transcript or account record is included. See [METHOD.md](METHOD.md) and [DATA-SOURCES.md](DATA-SOURCES.md).
