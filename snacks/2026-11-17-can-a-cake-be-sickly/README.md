---
title: "Can a cake be sickly? — checking guide"
date: 2026-11-18
provenance: Published Research Snacks and their archived analysis inputs
---

# Can a cake be sickly?

[Read the published claim and answer](https://researchsnacks.semanticmachines.fyi/2026-11-17-can-a-cake-be-sickly/).

From the repository root:

```sh
uv sync --locked
uv run check.py 2026-11-17-can-a-cake-be-sickly
```

`data/` holds shareable inputs, `code/` holds the reconstruction steps and `expected/` holds the final tables. The checker runs `code/reproduce.py` in a temporary output folder and compares every expected CSV. Read [METHOD.md](METHOD.md) for the decisions the code applies. Licences are listed in [DATA-SOURCES.md](../../DATA-SOURCES.md).

The question asks whether *sickly* can describe inanimate things as the only adjective, and whether the evidence establishes a British–American difference.

| Output | Numbers on the page |
|---|---|
| `1-sickly-food-constructions.csv` | The 2/3, 3/2 and 4/1 construction counts: 9 sole-adjective cases and 6 coordinated cases, 15 selected cases in total. |
| `corpus-rates.csv` | 218, 12 and 1 exact-form hits; rates 2.268, 1.086 and 0.312 per million words. |
| `example-counts.csv` | Counts of the 39 curated examples by corpus. |
| `association-scores.csv` | T-score, MI and logDice recomputed from the archived counts and token denominators; these support the association discussion. |

No corpus query is made by the default check. To audit the classifications, open the corpus versions in `data/queries.json` through your own Sketch Engine access. Run the case-insensitive exact-form query `[word="(?i)sickly"]`; use `food-annotations.csv` document IDs and token positions to read the fifteen selected BNC contexts. `example-locators.csv` locates all 39 examples. For spoken OANC use the corpus version identified in METHOD.md. The historical web rows need their corresponding corpus versions and passage anchors; both enTenTen13 cake rows deliberately retain the same passage anchor.

The BNC licence restricts text extracts. OANC allows redistribution, but all contexts are omitted consistently here to keep personal names out of the checking package. Permissions for supplementary web text were not established. No concordance lines, source web titles, complete original report, session transcript or usage snapshot is included. Saved classifications are evidence to audit, not a newly validated gold standard.

## Additional research files

- [`data/source-manifest-sickly.json`](data/source-manifest-sickly.json) — Checksums and sizes identifying study artifacts; records provenance without reproducing withheld text.
- [`data/word-sketch.json`](data/word-sketch.json) — Only word-level collocate/count/score triples: 156 aggregate rows, no example sentences or source passages.
- [`code/build-sickly-figures.py`](code/build-sickly-figures.py) — Figure renderer; adapt to existing shareable stand-off annotations and locators instead of withheld contexts.

These additions do not change `check.py` or its expected-output set. Extraction and optional chart-rendering scripts are separate from the default numerical check.

The figure renderer uses the shareable `food-annotations.csv` and `example-locators.csv`. It writes to the ignored `actual/charts/` folder. The display contains 39 stand-off records with no corpus passages. The source manifest identifies earlier archived artifacts by checksum; it does not imply those withheld or working-note artifacts are distributed. `word-sketch.json` contains only aggregate collocate statistics.
