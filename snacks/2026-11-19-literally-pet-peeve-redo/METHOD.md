---
title: Method for checking the 2011 literally post
date: 2026-11-19
provenance: Queries and annotations made on 19 November 2026
---

# Reconstruction target

The offline check rebuilds the page's numerical tables from the saved inputs. Rebuilding is not independent replication of the linguistic interpretation. Original TIME/COCA versions and search exports were unavailable; their old values remain explicitly historical claims.

| Output in expected/ | Page number or chart checked |
|---|---|
| 1-book-frequency.csv | All annual points in book-frequency chart; three collections, 1800–2019. |
| literally-book-periods.csv | All mean annual decade rates; the page displays 1950s, 1980s, 2000s and 2010s. |
| 2-reading-distribution.csv | All six reading counts and percentages in each sixty-token sample. |
| 3-function-comparison.csv | All emphasis/figurative counts, percentages and 95% Wilson intervals. |
| literally-ambiguity-bounds.csv | Maximum figurative shares if every uncertain reading is counted as figurative. |
| literally-corpus-rates.csv | Corpus word counts, all-hit totals, sample size and hits per million words. |
| 4-book-contexts.csv | All four book-construction series and their plotted points. |
| literally-followup-counts.csv | Seven crowd matches, one height match, numbers of contexts inspected. |
| literally-second-reading-summary.csv | Thirty-six second readings, 35 retained labels, one change. |

# Retrieval and randomisation

`literally-corpora.json` records exact versions, actual word/token denominators, corpus composition and full hit counts. Query `[lc="literally"]` is case-insensitive through the lowercase corpus attribute. The complete result was awaited with `asyn=0` and `finished=1` verified. A first incomplete web response and wrong context-window parameters were rejected before annotation; neither drives these outputs. Token positions are specific to these versions. Metadata on the public BNC page describes a retagged version with a different denominator; the run used CLAWS `preloaded/bnc2`.

All 1,936 BNC1994 and 2,067 Spoken BNC2014 lines were retrieved privately. Sixty were drawn from each complete list with Python `random.Random(20110223).sample(lines, 60)`. The 52.3-billion-word web corpus had 1,837,887 complete hits; query operation `r60` selected sixty. Its server-side randomisation was not seed-controlled. The realised token positions in `literally-corpus-requests.json` define the sample that was actually annotated; a fresh random query need not return the same lines. Licensed readers can retrieve the full query and look up the stored positions, or inspect a token via their corpus interface. The API metadata reports 100 as its maximum context; the request used `kwicleftctx=-50` and `kwicrightctx=50`.

Queries and surface matches select strings. They never assign a meaning. Five of seven adjacent crowd matches and the one height match were read separately. The latter concerned an object, not human height. A wider reverse-order figuratively query timed out, which is not a zero result.

# Judgement steps and rules

One gpt-6.1-sol agent read each sampled context, using these categories set before annotation:

- **factual**: the statement is presented as actually true, including an extreme number, a conditional possibility or an event within a fictional/game world. This does not independently verify its truth. Conventional abstract vocabulary does not automatically make it a nonliteral token.
- **figurative**: the context supports a clearly nonliteral reading or hyperbole, rather than an actual event or quantity.
- **metalinguistic**: translation, lexical meaning or an instruction about how words should be interpreted.
- **dual**: wording deliberately invokes an actual circumstance and a conventional figurative reading, including motivated puns.
- **uncertain**: the context does not resolve the reading. Do not force a label where a quantity may be either asserted or exaggerated.
- **mention_or_error**: the word is being mentioned, or appears to be a typing error for another word.

The separate emphasis label asks whether the occurrence adds rhetorical force, stressing reality, extremity, immediacy, exactness or aptness. Thus emphasis can coexist with factual, metalinguistic or dual readings. The function is not recovered from a keyword rule or equated with the figurative label. `yes`, `no` and `uncertain` are available. Each row records confidence, a decision reason and the rule version.

A second manual reading used twelve positions per corpus chosen with seed 20110224. First labels were hidden from the redisplay, but the agent had already seen the text, so this is not blind independent annotation. One reading, B09, changed from figurative to uncertain because the description might concern physical ballot movement. Both labels survive in the second-reading file. No human hand-check, independent annotator or speaker-judgement experiment took place. Those are missing validation steps, not claimed passes.

# Aggregation and uncertainty

Every occurrence remains in its sixty-token denominator, including word mentions/errors. Samples are not pooled across corpora. Wilson intervals use z=1.959963984540054 and describe binomial sampling uncertainty only; repeated documents/speakers, category uncertainty and systematic annotation error are excluded. Ambiguity bounds count all `uncertain` readings as figurative at their upper bound; deliberately dual readings retain their own category.

Google Books requests use the fixed 2019 English, British and American releases, generated February 2020, for 1800–2019 with smoothing zero and case-insensitive aggregation. Use the provider's `(All)` series when supplied; otherwise use the returned exact series. Never add the component series to `(All)` again. Annual unigrams are expressed per million words; the four two-word constructions are per million bigrams. Decade rows are arithmetic means of annual normalised rates, not pooled-count decade rates. Version-specific annual corpus-size files were not obtained, so no total token-count claim is made for Google Books. Meanings are never inferred from phrase frequencies or POS tags.

# Historical claims and provenance

The entire original article, including both updates, was read. The claim inventory groups repetitions while splitting history, scope, frequency, speaker-knowledge, acceptability, confusion, search and ancillary claims. Source lines refer to the supplied Markdown copy, whose article starts after its frontmatter. All 49 Update 2 counts are retained, including the nine-row “top ten” noun list; nine other explicit counts are in a separate file. Copying them preserves an assertion; it does not reproduce the original query. Judging whether a new observation supports an original assertion is a separate interpretive step recorded in the inventory.

MD5 hashes identify the exact saved public inputs. These are provenance locators, not an authentication signature. Original source pages and restricted concordances are retained privately by the researcher and are excluded here. This folder includes no transcript, API credential, personal account metadata or timing/usage snapshot. Code is MIT; annotation and original prose are CC BY 4.0; Ngram data and derived series retain CC BY 3.0.
