---
title: "Research Snacks: data, code and methods"
date: 2026-11-18
provenance: Published Research Snacks and their archived analysis inputs
---

# Check a Research Snack

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24370344.svg)](https://doi.org/10.5281/zenodo.24370344)

This repository holds the shareable inputs, code, methods and expected tables behind [Research Snacks](https://researchsnacks.semanticmachines.fyi). The [website repository](https://github.com/techczech/research-snacks) builds the site. This repository checks the calculations.

Install [Git](https://git-scm.com/) and [uv](https://docs.astral.sh/uv/), then run these three commands:

```sh
git clone https://github.com/techczech/research-snacks-data.git
cd research-snacks-data && uv sync --locked
uv run check.py
```

The checker rebuilds all snacks in temporary folders and diffs every final CSV against `expected/`. A difference gives a non-zero exit and a readable diff. The folders are removed on success and failure. To check one snack, pass its full folder name: `uv run check.py 2026-11-16-one-in-270-jobs`.

| Snack | What the default check rebuilds |
|---|---|
| [One in 270 jobs](snacks/2026-11-16-one-in-270-jobs/) | Headline totals, classifications, decline tables and employment trends from IPUMS aggregates. |
| [Pace of change](snacks/2026-11-17-pace-of-change-1900-2026/) | Dissimilarity, robustness, social indicators, college shares and Ngram take-off years. |
| [Can a cake be sickly?](snacks/2026-11-17-can-a-cake-be-sickly/) | Construction counts, corpus rates, association scores and counts of curated examples. |
| [AI wealth control by 2035](snacks/2026-11-17-ai-wealth-control-2035/) | Historical comparison and payment tables, plus the stock-comparison boundary checks. |
| [AI spending and historical booms](snacks/2026-11-19-ai-capex-historical-booms/) | Spending as a share of GDP, cumulative boom spending, revenue against capital in service, and the growth paths behind the charts. |
| [Canals and nuclear power as investment booms](snacks/2026-11-19-canals-nuclear-investment-booms/) | Canal and civil nuclear spending as a share of GDP, canal receipts and returns, nuclear utilisation and cancellations. |
| [Hawks and doves](snacks/2026-11-19-hawks-and-doves/) | Counts of elaborations of the political hawk and dove metaphor by source and decade, from saved annotations. |
| [Literally](snacks/2026-11-19-literally-pet-peeve-redo/) | Claim audit counts, Ngram series and the reading and function counts from annotated contexts. |
| [Metaphor use pilot](snacks/2026-11-19-metaphor-use-pilot/) | Agreement tables between two annotation passes over six texts, from frozen annotation records. |
| [Revolution speed](snacks/2026-11-19-revolution-speed-2011-redo/) | Date arithmetic for sixteen episodes, era sensitivities, NAVCO success rates and survey facts. |
| [Decipherment methods and agents](snacks/2026-11-19-decipherment-methods-and-agents/) | Precondition counts for 20 historical recoveries, 22-case open/partial matrix, corpus evidence, ordinal agent ranking and sensitivity from frozen cited judgements. |

The default run needs no API key and makes no source-data requests. IPUMS microdata cannot be included. Each census snack explains how to request it with your own free account and `IPUMS_API_KEY`, then rerun the original aggregation. Corpus text is withheld; query options, positions and saved annotations let a licensed reader inspect the evidence. Recounting saved annotations does not validate their linguistic judgements. Rebuilding a chart does not independently verify a transcribed source value or a forecast.

Code is MIT. Our text, annotations and derived tables are CC BY 4.0, subject to the third-party exceptions in [LICENCE.md](LICENCE.md). In particular, Ngram data retains CC BY 3.0 and ITU data retains its non-commercial, share-alike terms. See [DATA-SOURCES.md](DATA-SOURCES.md) before reusing any data.

To cite this checking material: Dominik Lukeš (2026), *Research Snacks: data, code and methods*, this repository, the snack folder and the commit hash you checked. Cite the linked snack page and the original data providers as well. Each census folder includes the required IPUMS citation. There is no DOI yet.

[VALIDATION.md](VALIDATION.md) records the verification and its limits. [provenance.json](provenance.json) identifies the public source version and hashes of the shipped inputs and expected tables.

## Cite

Lukeš, Dominik (2026). *Research Snacks: data, code and methods*. Zenodo. [https://doi.org/10.5281/zenodo.24370344](https://doi.org/10.5281/zenodo.24370344)

That DOI always points to the latest archived release. Each release also has its own DOI, listed on the Zenodo record; cite that one when you need a fixed version.
