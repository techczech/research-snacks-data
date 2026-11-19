---
title: "Checking the decipherment Research Snack"
date: 2026-11-19
provenance: "Published-source survey, frozen literature coding and deterministic calculation"
---

# Decipherment methods and agentic AI

This folder checks [Which scripts were deciphered, and where could AI agents help?](https://researchsnacks.semanticmachines.fyi/2026-11-19-decipherment-methods-and-agents/).

From the repository root:

```sh
uv sync --locked
uv run check.py 2026-11-19-decipherment-methods-and-agents
```

The default check needs no API key or internet source download. It rebuilds the seven expected tables from the saved coding. In particular, it reproduces **13 full bilinguals, 4 partial parallels and 3 without either; 18 usable known linguistic comparators and 2 without; 15 clear proper-name entry points, 2 partial and 3 uncertain**, across the 20 selected historical cases. These are counts of agent judgements, not a statistical test of causal necessity. See [METHOD.md](METHOD.md) before interpreting them.

The inputs comprise a 42-case CSV, cell-level evidence/uncertainty records, source metadata/access scopes and 26 computational-work records. Each corpus count retains its source date and unit; unknown is never zero. The public package contains no ancient corpus texts or third-party sign images. [DATA-SOURCES.md](DATA-SOURCES.md) records the sharing decisions and the providers' different access conditions.

To rebuild chart assets after the table check, run `uv run python snacks/2026-11-19-decipherment-methods-and-agents/code/charts-decipherment.py` from the repository root. The image renderer uses the repository's pinned dependency. The PNG, CSV and Vega-Lite files describe the same observations. A passing rerun proves computational consistency with the saved judgements; it does not validate them independently.
