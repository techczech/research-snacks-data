---
title: Roman Numeral Reader preset check method
date: 2026-11-21
provenance: Roman Numeral Reader research and v3 engine
---

# Method

The unit of comparison is a selected, transcribed example with a period and, where appropriate, a mode or date reckoning. The target is an ordinary numeral value, a converted year, a chronogram sum or a year in the chosen indiction range. Any candidate matching the target counts. In a preset with multiple targets, every target must occur.

The research judgement steps were finding and choosing sources, reading and normalising glyphs, deciding which date belongs to the writing and which to the event, choosing the documented reading and period, tagging conventions and assigning ordinal rankings. Region and genre qualify some ratings. The two reviewers checked selected judgements independently and the coordinator reconciled their findings. [The reconciliation](data/council/reconciliation.md) records the engineering decisions, including how missing evidence ranks.

- [First-version ratings](data/first-version-ratings.json) recover the initial engine vectors. [Research ratings](data/ratings.json) are the first evidence pass and [conventions](data/conventions.json) are the v2 tables still used in v3. In each vector the order runs from Classical through late antiquity and the early Middle Ages, high and late Middle Ages, early modern, then modern.
- [Per-preset results](expected/preset-results.csv) records the expected values, actual reader outputs and match decision. Its two mismatches reproduce the article's exceptions. [Coverage by period](expected/preset-coverage.csv) is the source for the chart and the period counts.
- [Summary counts](expected/summary.csv) reproduces 46/48 matches, 49 constructed examples, 15 source-status notes, 44 regression and data checks and 2 full readings out of 45 current records. Fourteen notes concern sources Haiku could not reach. The other records where the film title card can be checked. [Provenance](provenance.json) records the initial count of 45 references and source checksums.

[The test runner](code/test.mjs) runs the v3 regression checks and preset comparison. This packaging adds a JSON output flag and adjusts the paths in the test runner and [data generator](code/build-data.mjs) to use the checking repository's layout. The browser files and outcome logic are from v3. The checker calls Node and compares the regenerated CSV files byte for byte at the line level. It does not access external sources.

The result estimates coverage of these selected examples. It cannot establish ranking accuracy, independent historical accuracy or prevalence. The named periods are broad, the sources are uneven and some are only reported through handbooks or limited views. The council reviews are fallible and predate v2.
