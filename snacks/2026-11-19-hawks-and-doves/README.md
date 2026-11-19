---
title: "Do political hawks kill political doves? Checking the counts"
date: 2026-11-19
provenance: Primary-source retrieval and saved agent judgements on 19 November 2026
---

# Check the hawks and doves snack

Page: [Do political hawks kill political doves?](https://researchsnacks.semanticmachines.fyi/2026-11-19-hawks-and-doves/).

From the repository root, run `uv sync --locked` and `uv run check.py 2026-11-19-hawks-and-doves`.

The default check has no network or key requirement. It recounts 492 saved annotations into six expected tables. It checks the page's 160/50/2 newspaper sample figures, its 111/107/15 Hansard and 221/197/19 newspaper paired-search figures, source/decade breakdowns, monetary-policy split and Ngram decade averages. It does not independently validate the linguistic annotations, recover withheld newspaper text, or prove that killing metaphors are absent from public discourse.

Read [METHOD.md](METHOD.md) for the counting rules and [DATA-SOURCES.md](DATA-SOURCES.md) for redistribution decisions. `annotations.csv` includes rejected and uncertain cases, token/contribution locators, dates, source links, confidence, model and human-validation status. `queries.json` preserves the exact successful corpus requests. The frozen sample's token positions define the sample for subsequent checks; asking the server for a new random sample can return different positions.

Run `uv run python snacks/2026-11-19-hawks-and-doves/code/charts.py` to rebuild PNG/CSV/Vega-Lite charts from the expected tables. The checked counts are the deliverable; images are not part of the arithmetic diff.
