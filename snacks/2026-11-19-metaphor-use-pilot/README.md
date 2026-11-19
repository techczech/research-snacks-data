---
title: Check the six-text metaphor-use pilot
date: 2026-11-19
provenance: Two frozen semantic annotation passes and six attributed opening passages
---

# Can a 2005 classification of metaphor use be applied consistently?

Checking material for [the Research Snack](https://researchsnacks.semanticmachines.fyi/2026-11-19-metaphor-use-pilot/). These are provisional machine annotations, not checked by Dominik Lukeš. Two fresh contexts of configured gpt-6.1-sol read every one of the 402 fixed word units without sharing labels. A and B are separate readings of one model family, not different model families or human annotators.

From the repository root, run:

```sh
uv sync --locked
uv run check.py 2026-11-19-metaphor-use-pilot
```

The standard-library script makes no network requests and needs no key. It validates excerpt MD5s, regenerates word offsets, checks annotation schemas, and rebuilds eight tables. It does not discover metaphors, infer functions, validate source facts, or establish that the annotations are linguistically correct. Unlisted unit IDs were explicitly declared literal by each annotator after full passage reading. All labelled or uncertain units have contemporary basic/contextual contrasts and evidence.

| Expected output | What it checks on the page |
|---|---|
| `corpus-summary.csv` | Six passages and their 402-unit denominator; per-pass metaphor and uncertain counts. |
| `pilot-totals.csv` | 59 and 58 metaphor-marked units, 51 common units, 66 in the union, and 64 disagreement rows. |
| `identification-confusion.csv` | All nine M/L/U combinations behind identification agreement. |
| `agreement.csv` | Exact agreement and unweighted Cohen's kappa for identification and each use dimension; per-label supplementary results. |
| `use-counts.csv` | Cognitive, nested elaboration, overlapping social/binding, and passage-scope counts, including document counts. |
| `disagreements.csv` | Every scored difference in identification or use, including the examples discussed in the snack. |
| `1-cognitive-use.csv` | Exact plotted rows for the cognitive-use chart. |
| `2-agreement.csv` | Exact plotted rows for the agreement chart. |

[CODEBOOK.md](CODEBOOK.md) preserves the instructions frozen before annotation. [METHOD.md](METHOD.md) explains sampling, measurement and limits. [DATA-SOURCES.md](DATA-SOURCES.md) records source licences and changes. [provenance.json](provenance.json) hashes the inputs and expected outputs. The MIP baseline is from [Pragglejaz Group (2007)](https://www.lancaster.ac.uk/staff/eiaes/Pragglejaz_Group_2007.pdf); the use distinctions are from [Lukeš (2005)](https://dominiklukes.net/research/towards-a-classification-of-metaphor-use/).

Wikipedia contributors' excerpt and its numbered token representation retain [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); see the revision and contributor-history links in DATA-SOURCES.md. Python tutorial prose retains the [PSF Licence v2](data/PSF-LICENCE.txt). Contains Parliamentary information licensed under the Open Parliament Licence v3.0. Contains public sector information licensed under the Open Government Licence v3.0. NASA prose is shared under its educational/informational reuse permission. These third-party exceptions override the repository's general content licence for the corresponding source rows.
