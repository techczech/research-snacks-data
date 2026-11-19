---
title: "Checking the revised decipherment Research Snack"
date: 2026-11-19
provenance: "Frozen literature coding revised after independent source critique; deterministic recomputation"
---

# Decipherment methods and agentic AI

This folder checks [Which scripts were deciphered, and where could AI agents help?](https://researchsnacks.semanticmachines.fyi/2026-11-19-decipherment-methods-and-agents/).

From the repository root:

```sh
uv sync --locked
uv run check.py 2026-11-19-decipherment-methods-and-agents
```

The seven expected tables reproduce **9 full readable parallels, 8 partial keys/parallels and 3 without either; 18 usable known linguistic comparators and 2 without**, across twenty selected historical recovery stages. Proper-name entry codes are 14 yes, 2 partial, 1 no and 3 uncertain. These are author judgements with explicit stage choices, not a statistical test of causal necessity. Read [METHOD.md](METHOD.md) and the [item-by-item review response](data/REVIEW-RESPONSE.md).

The case file has 44 rows: twenty historical recoveries and 24 open/partial/readable-with-gaps/comparator cases. The 37 computational-work rows distinguish actual task and publication status. There are 105 source records and 783 evidence mappings. Every historical headline cell and every ordinal priority score has an individual rationale; other mappings are explicitly not individually annotated.

Priorities are ranked within two task cohorts: undeciphered/partly mapped systems and already readable systems with remaining language/character gaps. Vinča is unranked. The alternative doubles linguistic weight. Comparator matrix and rubric scores are checked for agreement. Missing counts remain unknown; dated editions are not a current global census.

The package contains our codings, summaries and code, with no ancient corpus text, source images or full papers. [DATA-SOURCES.md](DATA-SOURCES.md) states access and redistribution decisions. Run `uv run python snacks/2026-11-19-decipherment-methods-and-agents/code/charts-decipherment.py` to rebuild the PNG/CSV/Vega-Lite triples with the pinned renderer. A passing rerun establishes consistency with these saved decisions, not specialist validation of them.
