---
title: "Only one of 270 jobs from 1950 is obsolete? — checking guide"
date: 2026-11-18
provenance: Published Research Snacks and their archived analysis inputs
---

# Only one of 270 jobs from 1950 is obsolete?

[Read the published claim and answer](https://researchsnacks.semanticmachines.fyi/2026-11-16-one-in-270-jobs/).

From the repository root:

```sh
uv sync --locked
uv run check.py 2026-11-16-one-in-270-jobs
```

`data/` holds shareable inputs, `code/` holds the reconstruction steps and `expected/` holds the final tables. The checker runs `code/reproduce.py` in a temporary output folder and compares every expected CSV. Read [METHOD.md](METHOD.md) for the decisions the code applies. Licences are listed in [DATA-SOURCES.md](../../DATA-SOURCES.md).

The claim says only one 1950 occupation became obsolete. The check distinguishes automation, other losses, reclassification and new work.

| Output | Numbers on the page |
|---|---|
| `page-summary.csv` | 268 categories, 86 zeros, 16 judged gone or nearly gone, 70 reclassification zeros; 58.9m and 140.2m employed. |
| `1-waffle-1950-occupations.csv` | Each occupation's 1950/2010 counts and assigned status. |
| `2-jobs-that-disappeared.csv` | The fifteen numeric rows of the disappearance table, worker counts and workforce shares. The photoengraver row has no separate count. |
| `3-survived-but-collapsed.csv` | The ten decline percentages and workforce shares. |
| `5-rise-and-fall.csv` | The six employment series for office and communication jobs. |
| `6-new-work.csv` | Software and systems jobs since 1970. |

The full `data/occ1990_by_year.csv` also supports the film-to-census table. The film mapping is a saved judgement described in METHOD.md; the checker does not watch the film. The literature's roughly 60% new-work estimate is a cited external finding, not something these two extracts reproduce.

For a new microdata run, register at IPUMS USA, obtain your own key and make it available to the command as `IPUMS_API_KEY`. Do not put it in a file or commit it. Keep all downloads in the ignored `private/` directory. Run these commands from the repository root:

```sh
uv run code/fetch-ipums.py snacks/2026-11-16-one-in-270-jobs/code/spec-occupations.json snacks/2026-11-16-one-in-270-jobs/private/occupations
uv run snacks/2026-11-16-one-in-270-jobs/code/analyse.py snacks/2026-11-16-one-in-270-jobs/private/occupations snacks/2026-11-16-one-in-270-jobs/actual/occupations
uv run code/fetch-ipums.py snacks/2026-11-16-one-in-270-jobs/code/spec-trends.json snacks/2026-11-16-one-in-270-jobs/private/trends
uv run snacks/2026-11-16-one-in-270-jobs/code/analyse2.py snacks/2026-11-16-one-in-270-jobs/private/trends snacks/2026-11-16-one-in-270-jobs/actual/trends
```

Diff the two generated aggregate CSVs against their namesakes in `data/`. A later IPUMS revision may differ from Version 16.0. The API script was syntax-checked; no new authenticated extract request was made for this release. Raw records, film subtitles, private transcripts and usage records are withheld.

Required IPUMS citation, copied verbatim from the original Version 16.0 codebook underlying the entry:

> Steven Ruggles, Sarah Flood, Matthew Sobek, Daniel Backman, Grace Cooper, Julia A. Rivera Drew, Stephanie Richards, Renae Rodgers, Jonathan Schroeder, and Kari C.W. Williams. IPUMS USA: Version 16.0 [dataset]. Minneapolis, MN: IPUMS, 2025. https://doi.org/10.18128/D010.V16.0
