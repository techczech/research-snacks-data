---
title: "Can AI control more wealth by 2035? — checking guide"
date: 2026-11-18
provenance: Published Research Snacks and their archived analysis inputs
---

# Can AI control more wealth by 2035?

[Read the published claim and answer](https://researchsnacks.semanticmachines.fyi/2026-11-17-ai-wealth-control-2035/).

From the repository root:

```sh
uv sync --locked
uv run check.py 2026-11-17-ai-wealth-control-2035
```

`data/` holds shareable inputs, `code/` holds the reconstruction steps and `expected/` holds the final tables. The checker runs `code/reproduce.py` in a temporary output folder and compares every expected CSV. Read [METHOD.md](METHOD.md) for the decisions the code applies. Licences are listed in [DATA-SOURCES.md](../../DATA-SOURCES.md).

The claim predicts that AI could control more wealth by 2035 than humans controlled at baseline. The check tests whether historical comparisons support that inference; it does not estimate a probability for 2035.

| Output | Numbers on the page |
|---|---|
| `1-observed-transitions.csv` | Electric-motor power 5–82%; internet users 40–68%; index-fund assets 19–51%; electronic spot-FX turnover approximately 55–70%, each with its own denominator. |
| `2-payments-denominators.csv` | Payment count shares 74.25/19.24/6.51% and value shares 7.84/69.25/22.91%. |

The default run recalculates elapsed years, validates the percentage ranges, reconciles payment totals and tests the strict wealth comparison at equality and either side. It rebuilds charts too; only the CSV tables are diffed because image rendering can differ across platforms.

Every input row includes its primary-source URL and page/table locator. Source values were transcribed and checked in the original research. The checking repo makes that transcription inspectable; it does not independently re-extract the PDFs. Fetch the sources at those URLs to inspect the transcription. See DATA-SOURCES.md for the distinct ICI, ITU and BIS terms before reusing these rows.

Private model scenarios, assumptions from broader exploratory models, personal usage/account snapshots, session logs, full PDFs and cached web pages are withheld. They are not required by this published snack's calculation. Historical timing and token figures are outside the rerun.

## Additional research files

- [`data/source-manifest.json`](data/source-manifest.json) — Primary-source URLs, retrieval statuses and checksums; source provenance without source documents.

These additions do not change `check.py` or its expected-output set. Extraction and optional chart-rendering scripts are separate from the default numerical check.
