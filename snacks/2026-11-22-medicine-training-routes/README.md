---
title: Medical training routes — six-place preview data package
date: 2026-11-22
status: Author preview; not a published Research Snack
provenance: Original regulator-document coding with selected UIS, World Bank and European Commission facts
---

# What this package contains

`routes.md` owns the six selected pathways, 50 stage records, 26 source passages, exact source locations and reading-depth limits. `stages.csv` and `sources.json` are generated from it by the preview builder. Each exported stage expands source passages, source/access dates, URLs and reading limits. These records are documentary coding, not practitioner-level observations.

`uis-selected-programmes.csv` contains 21 selected workbook rows with source cell locators, school reference years and workbook SHA-256 hashes. `school-baselines.csv` records six harmonisation choices, including Bavaria's G9 and Singapore's junior college. `world-bank-school-indicators.csv` has 24 latest non-missing observations found within 2015–2026; all are 2025 at this check. These are theoretical structures. The historical UIS structures and current professional rules are not one cohort's longitudinal experience.

`eu-basic-medical-duration.csv` contains a dated factual snapshot of 32 exact-category basic-medical-training records. Missing dates and values remain missing. Education and traineeship fields are never summed. `eu-gp-report-table.csv` transcribes a distinct 27-entry report table; the ambiguous printed SL code is not silently corrected. These sources must not be joined as if they measured a common total.

`source-fingerprints.json` retains hashes only for actual locally retrieved source documents. A null hash means the original was not obtained through that route; the source register describes web-reader, indexed-excerpt and corroborating access. Full publications/workbooks and API documents are withheld in ignored scratch. See [source terms and limits](DATA-SOURCES.md).

# Reproduction

Use Python 3.11 and the versions in `requirements.txt` for source extraction. From this package directory:

```sh
python3 code/extract_context.py world_bank uis eu eu_gp
```

This refreshes public structured data, writes source access dates for the actual run, and retains source inputs under the repository's ignored `scratch/medicine-training-routes`. Fresh downloads may differ from this snapshot. The published CSVs and hashes identify the checked snapshot. The report-table selector is exact and fails if the expected table disappears; it does not guess its way to another table. The numeric parsing operates only on manually identified duration cells. EU qualification filtering uses an exact provider category; it is not a keyword classifier.

The separate `code/retrieve.py` accepts a JSON mapping of source IDs to public URLs, storing whole documents and extraction text only in ignored scratch. Retrieval failures and TLS errors are retained rather than bypassed. The companion Research Snacks preview folder holds these URL manifests and its build script.

To recreate `stages.csv`, `sources.json` and the preview, run the documented `build.ts` command in the companion [Research Snacks preview source](https://github.com/techczech/research-snacks/tree/main/research/2026-11-22-professional-qualification-duration/medicine-preview). It uses the existing Research Snacks bun dependencies; no runtime network calls are needed by the packaged HTML.

# Validation boundary

The preview's targeted headless checks passed for the three clocks, legal-milestone distinction, embedded and overlapping requirements, source display, CSV export, offline operation and no-JavaScript record access. Original NMC documents and current NExT implementation require further confirmation before publication; this limitation is visible in the preview. No independent full source audit, competence analysis or author acceptance is asserted.
