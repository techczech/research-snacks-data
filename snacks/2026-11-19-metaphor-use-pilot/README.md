---
title: Check the six-text metaphor-use pilot
date: 2026-11-19
provenance: Two frozen semantic annotation passes and six attributed opening passages
---

# Can a 2005 classification of metaphor use be applied consistently?

Checking material for [the Research Snack](https://researchsnacks.semanticmachines.fyi/2026-11-19-metaphor-use-pilot/). These are provisional machine annotations, not checked by Dominik Lukeš. Both passes used the same configured gpt-6.1-sol. A had read the manuscript and written the codebook in its coordinator context; B was fresh with the codebook, excerpts and units only. A used serialization defaults documented in METHOD.md. They are asymmetric separate-context passes, not independent raters or models.

From the repository root, run:

```sh
uv sync --locked
uv run check.py 2026-11-19-metaphor-use-pilot
```

The standard-library script makes no network requests and needs no key. It validates excerpt MD5s, regenerates word offsets, checks annotation schemas, and rebuilds eleven tables. It does not discover metaphors, infer functions, validate source facts, or establish that the annotations are linguistically correct. Unlisted unit IDs were explicitly declared not metaphor-related (L) by each annotator after full passage reading. All labelled or uncertain units have contemporary basic/contextual contrasts and evidence.

| Expected output | What it checks on the page |
|---|---|
| `corpus-summary.csv` | Six passages and their 402-unit denominator; per-pass metaphor and uncertain counts. |
| `pilot-totals.csv` | 59 and 58 metaphor-marked units, 51 common units, 66 in the union, and 64 disagreement rows. |
| `identification-confusion.csv` | All nine M/L/U combinations behind identification agreement. |
| `agreement.csv` | Exact agreement and unweighted Cohen's kappa for identification and each use dimension; per-label supplementary results. |
| `use-counts.csv` | Cognitive, nested elaboration, overlapping social/binding, and passage-scope counts, including document counts. |
| `disagreements.csv` | Every scored difference in identification or use, including the examples discussed in the snack. |
| `1-cognitive-use.csv` | Exact plotted common-unit rows (n=51) for the cognitive-use chart. |
| `2-agreement.csv` | Exact plotted rows for the agreement chart. |
| `common-cognitive-counts.csv` | Cognitive marginals on the same 51 units, separated from the full-pass counts. |
| `uncertain-annotations.csv` | Every A/B U record, including the three joint-U units excluded from functional scoring. |
| `review-audit.csv` | Uncertainty split, direction of cognitive disagreements, baseline social matches and positive-link agreements. |

[CODEBOOK.md](CODEBOOK.md) preserves the instructions frozen before annotation. [METHOD.md](METHOD.md) explains sampling, measurement and limits. [DATA-SOURCES.md](DATA-SOURCES.md) records source licences and changes. [provenance.json](provenance.json) hashes the inputs and expected outputs. The MIP baseline is from [Pragglejaz Group (2007)](https://www.lancaster.ac.uk/staff/eiaes/Pragglejaz_Group_2007.pdf); the use distinctions are from [Lukeš (2005)](https://dominiklukes.net/research/towards-a-classification-of-metaphor-use/).

Wikipedia contributors' excerpt and its numbered token representation retain [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); see the revision and contributor-history links in DATA-SOURCES.md. Python tutorial prose retains the [Python Software Foundation License Version 2](data/PSF-LICENCE.txt). Contains Parliamentary information licensed under the Open Parliament Licence v3.0. Contains public sector information licensed under the Open Government Licence v3.0. NASA prose is treated as US government material generally not protected by copyright in the United States; the media guidelines are not a blanket prose licence and no worldwide grant is asserted. NASA does not endorse this analysis. These third-party exceptions override the repository's general content licence for the corresponding source rows.

The [source notices](data/SOURCE-NOTICES.md) retain exact attribution, change summaries and non-endorsement. The original `CODEBOOK.md`, A/B labels, numbered units and `data/pilot-texts-frozen-v1.json` remain frozen. Corrected metadata in `data/pilot-texts.json` changes dates/notices only. See METHOD.md for all accepted source-review findings and the limits on the revised verdict.
