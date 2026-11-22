---
title: Medicine training routes — checking package
date: 2026-11-22
status: Research Snack preview; production awaits author review
provenance: Original regulator-document coding with selected UIS, World Bank and European Commission facts
---

# What is shared

Six selected domestic medical pathways, 55 stage records and 32 source records. Registration, general medical licensing and later family/general-practice training remain distinct. This is documentary coding of requirements, not a dataset of individual doctors or measured competence.

The original authoring file is `routes.md`; its public machine-readable snapshot is `data/route-coding.json`. Root CSV files remain for compatibility with the earlier preview. `data/` holds the checked input snapshots, exact UIS workbook cells, school baseline judgements, World Bank observations, limited EU factual extract, GP report transcription and review records. Whole third-party publications and workbooks remain withheld in ignored scratch. [Source and redistribution decisions](DATA-SOURCES.md).

# Check the page's numbers

From the repository root:

```sh
uv sync
uv run check.py 2026-11-22-medicine-training-routes
```

This offline check recalculates all three `expected/` CSVs using `code/reproduce.py`: the six-row milestone table, 55-stage provenance/clock export and EU distribution. They reproduce the page's table, interactive data and plotted counts. See [method, judgement steps and limits](METHOD.md).

# Rebuild the tool and chart

The tool is self-contained HTML. With Bun installed, from this snack directory:

```sh
bun code/timeline/build.ts . medicine-timeline.html
uv run python code/chart-eu.py eu-duration.png
```

The tool builder uses checked local JSON/CSV files and bundles the browser script without a network request. `data/tool-copy.json` is the renderer input for the public wording; `code/timeline/preview.md` preserves its editable original. The chart uses the exact expected EU distribution. The site's committed bundle is copied from these sources; no service is required to run the downloaded tool.

Optional online refresh commands need the additional Python dependencies in `requirements.txt`:

```sh
python3 code/extract_context.py world_bank uis eu eu_gp
python3 code/refresh_india_sources.py
```

Fresh data may differ. Inspect changed units, dates, legal rules and category definitions before accepting new expected outputs. Extraction preserves source URLs, cell locators and hashes; failures are not bypassed. `code/amend_verified_sources.py` and `code/update_family_routes.py` are historical amendment records, not refresh commands for an already updated package.

# Verification and remaining limits

An independent source check supports all six first-registration markers conditionally; the report names source reading limits. The original NMC curriculum, internship regulation and deferral notice were retrieved after the site migration. The former blanket India unavailable-source warning is superseded. No later NExT commencement was found in the bounded dated search; this does not predict future-cohort rules. Source hashes from that retrieval are in `data/india-source-retrieval.json`.

The UI checks cover all three clocks, embedded/overlapping requirements, source selection, CSV export, no-JavaScript access and phone/intermediate/desktop layouts. A complete legal audit, typical-completion survey and causal competence comparison are outside this package.


## Shared-axis comparison revision

The tool now switches between training stages and milestone dots on the same year scale. Hover, keyboard focus or tap opens a concise stage popover; a native full-record table retains every stage and source without JavaScript. Hiding later training also hides its completion markers. Four data colours and consistent marker shapes carry meaning across both views. The surrounding EU context and the three clocks are retained.

`data/visual-annotations.json` contains explicit display labels, permission summaries, source short names and selected milestone IDs. It does not change `data/route-coding.json` or the expected tables. The checker verifies its selected first-registration, general-licence and family-training IDs against the six milestone rows and rejects unknown stage/source IDs. Short labels and permission summaries remain original interpretations of the already coded source records; the full notes and source passages stay available.
