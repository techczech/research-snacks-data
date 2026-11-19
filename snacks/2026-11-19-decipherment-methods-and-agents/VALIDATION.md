---
title: "Decipherment survey validation record"
date: 2026-11-19
provenance: "Observed worker checks; independent source review is outside this record"
---

# Reproduction

At 14:47 UK on 19 November 2026, a fresh clone from the public remote at commit `e9c2d912aa9fe4741b4be69e2955905ece2f5e90` passed:

```text
uv sync --locked
uv run check.py 2026-11-19-decipherment-methods-and-agents
PASS 2026-11-19-decipherment-methods-and-agents: 7 tables
PASS: 1 snacks; all expected tables match.
```

The complete clone's Git history (20 commits, about 3.28 MB inspected by Gitleaks) passed its redacted secret scan. The publication folder passed a separate redacted scan. A complete current-tree private-path/address scan found no matches. Two historical patch hits were manually inspected: both quoted the literal path-detection pattern in an earlier validation note, not a private machine path. No source corpus text, sign images, full scholarly publications, local paths or session records are in this checking package.

# Site and scientific limits

The website's build/type/content checks and nine tests passed, as did its full headless release suite. All four new Vega-Lite figures drew marks at desktop and phone widths, and the PNG fallback survived simulated chart-CDN failure. The historical/precondition/ranking tables and citation block were inspected in headless captures. The final page's clean-main production deployment is recorded by the publication coordinator; its live URL is in README.md.

The coding audit corrected Brahmi/Kharosthi coin keys and early Carian name pairs from full to partial, consistently with the explicit bilingual definition. Final selected-sample counts are **10 full, 7 partial, 3 absent**. Known linguistic comparators are **18 yes, 2 no**. Correcting those cells changed the counts/matrix/timeline metadata, not the open-case ranking.

These checks establish the calculations and presentation of saved literature coding. They do not independently establish the accuracy of every historical classification, completeness of corpus counts, validity of a published decipherment claim or usefulness of a future agent loop. Missing source numbers, abstract-only access, contested cases, un-audited third-party corpus rights and absence of specialist review remain explicit in METHOD.md, DATA-SOURCES.md and the source/cell tables. No new model benchmark or decipherment experiment was run.

This entry was not yet included in the existing Zenodo release when this record was written. Cite the checked Git commit for its fixed computational inputs; a later release may archive it.
