---
title: "Did work change faster before 1970? — checking guide"
date: 2026-11-18
provenance: Published Research Snacks and their archived analysis inputs
---

# Did work change faster before 1970?

[Read the published claim and answer](https://researchsnacks.semanticmachines.fyi/2026-11-17-pace-of-change-1900-2026/).

From the repository root:

```sh
uv sync --locked
uv run check.py 2026-11-17-pace-of-change-1900-2026
```

`data/` holds shareable inputs, `code/` holds the reconstruction steps and `expected/` holds the final tables. The checker runs `code/reproduce.py` in a temporary output folder and compares every expected CSV. Read [METHOD.md](METHOD.md) for the decisions the code applies. Licences are listed in [DATA-SOURCES.md](../../DATA-SOURCES.md).

The claim compares 1900–1969 with 1957–2026. Census data cannot supply those exact endpoints: the published comparison uses 1900–1970, 1950–2024 and 1960–2024.

| Output | Numbers on the page |
|---|---|
| `dissimilarity.csv` | 56.0%, 43.4% and 39.0% occupational change, other classifications and each neighbouring-census comparison. |
| `dissimilarity_robustness.csv` | OCC1990/OCC2010 comparisons, including 57.4%, 62.9%, 52.2% and 53.6%. |
| `indicators.csv`, `college.csv` | Social measures and college shares, including 4.91%, 10.81% and 37.7%. |
| `1-change-per-decade.csv` through `5-new-job-titles.csv` | Exact chart tables, group shares, social measures and plotted job-title take-off years. |
| `ngram_takeoff.csv` | All fifty preselected titles, including exclusions and missing results. |

The written-title judgement and candidate tables are included in `data/`. They allow an audit of which 1940 titles were labelled new jobs rather than new wording. These are saved research decisions, not independently reclassified by the checker.

For a new microdata run, provide your own `IPUMS_API_KEY` at runtime. Request each of the four JSON specifications under `code/` using `uv run code/fetch-ipums.py SPEC OUTPUT_DIRECTORY`. Use a separate ignored `private/` directory per specification so codebook/data globs cannot mix extracts. The matching aggregation commands are:

```sh
uv run snacks/2026-11-17-pace-of-change-1900-2026/code/aggregate-inputs.py main snacks/2026-11-17-pace-of-change-1900-2026/private/main snacks/2026-11-17-pace-of-change-1900-2026/actual/main
uv run snacks/2026-11-17-pace-of-change-1900-2026/code/aggregate-inputs.py robustness YOUR_ROBUSTNESS.csv.gz snacks/2026-11-17-pace-of-change-1900-2026/actual/robustness
uv run snacks/2026-11-17-pace-of-change-1900-2026/code/aggregate-inputs.py college YOUR_EDUCATION.csv.gz snacks/2026-11-17-pace-of-change-1900-2026/actual/college
uv run snacks/2026-11-17-pace-of-change-1900-2026/code/aggregate-inputs.py titles YOUR_TITLES.csv.gz snacks/2026-11-17-pace-of-change-1900-2026/actual/titles
```

Replace each `YOUR_*.csv.gz` with the relative path returned by IPUMS. Diff the generated aggregate files against `data/`. The original main, robustness and education aggregations were rerun locally for this release; only aggregates are shipped. The authenticated request itself was not repeated. Written-title extraction is supplied for your own data; the recorded judgement file still needs human review.

`uv run snacks/2026-11-17-pace-of-change-1900-2026/code/ngrams.py snacks/2026-11-17-pace-of-change-1900-2026/actual/ngrams` performs an optional network refresh. It saves full-precision responses; the published rounded chart series alone can move a threshold. Raw census records, codebooks, private session records and account information are withheld.

Required IPUMS citation, copied verbatim from the original Version 16.0 codebook underlying the entry:

> Steven Ruggles, Sarah Flood, Matthew Sobek, Daniel Backman, Grace Cooper, Julia A. Rivera Drew, Stephanie Richards, Renae Rodgers, Jonathan Schroeder, and Kari C.W. Williams. IPUMS USA: Version 16.0 [dataset]. Minneapolis, MN: IPUMS, 2025. https://doi.org/10.18128/D010.V16.0
