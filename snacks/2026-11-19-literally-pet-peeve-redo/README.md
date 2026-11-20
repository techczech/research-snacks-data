---
title: Checking the 2011 literally post
date: 2026-11-19
provenance: New primary-corpus queries and the complete original 2011 post
---

# Check the literally snack

This folder supports [Literally: how close was I in 2011?](https://researchsnacks.semanticmachines.fyi/2026-11-19-literally-pet-peeve-redo/). It preserves 56 groups of empirical claims from the original post, 49 reported Update 2 collocation numbers, nine other reported counts, new complete corpus counts, 180 contextual annotations, a 36-context second reading and fixed-version Google Books responses.

From the repository root:

```sh
uv sync --locked
uv run check.py 2026-11-19-literally-pet-peeve-redo
```

The run rebuilds nine expected CSV tables without network access or an API key. It checks the page's numbers and exact chart data. It does not independently verify the annotations, historical Google estimates, 2011 TIME/COCA counts or judgements about acceptability and confusion. See [METHOD.md](METHOD.md) and [DATA-SOURCES.md](DATA-SOURCES.md).

The key distinction is **reading versus function**: a factually true statement may still be emphatic. “Clearly figurative” is a narrower category than the original author's “intensifier”. The categories, uncertainty, same-agent correction and token positions remain inspectable. No restricted corpus passages, raw conversations, personal account records, authentication material or whole copyrighted source pages are shipped.

## Additional research files

- [`code/make-charts.py`](code/make-charts.py) — Renders the literally snack from already checked expected CSV tables.

These additions do not change `check.py` or its expected-output set. Extraction and optional chart-rendering scripts are separate from the default numerical check.
