---
title: "Hawks and doves: method and annotation rules"
date: 2026-11-19
provenance: Successful API requests, source contexts and model annotations
---

# What was counted

The source period is the source's publication date, not the archive ingestion date. A decade is its calendar decade. These are three distinct retrieval sets, never pooled:

| Retrieval set | Unit | Retrieved | Policy sense | Bird elaboration |
|---|---|---:|---:|---:|
| SiBol random lexical sample | Token | 160 | 50 | 2 |
| SiBol close-pair search | Pair match | 221 | 197 | 19 |
| Hansard paired-term search | Spoken contribution | 111 | 107 | 15 |

The denominator is **all annotated policy-sense units in that retrieval set and decade**. The random set includes one-sided uses. The two pair searches omit one-sided uses, and cannot estimate the proportion of all political hawk/dove uses in their whole source. No full-population political denominator was established for any source. Pair matches overlap; repeated mentions and reproduced headlines are not independent articles. Zero is an observed count within saved contexts, not a statement about an entire archive.

## Retrieval

[SiBol](https://www.sketchengine.eu/sibol-corpus/) is a selected-year newspaper collection, not continuous 1993–2021 coverage. The actual successful requests are in `data/queries.json`; `asyn=0`, returned `finished=1`. Lexical query: `[lc="hawks?|doves?|hawkish|dovish"]`, followed by the server's `r160` random sample. The underlying lexical query reported 11,766 hits. The sample is saved by corpus token position. No seed was exposed or chosen. The broad all-hit download failed; an attempted 10,000-line tool retrieval was incomplete and not retained or used as a sampling frame.

Pair query: `[lc="hawks?"] []{0,20} [lc="doves?"] | [lc="doves?"] []{0,20} [lc="hawks?"]`. It has up to 20 intervening tokens and may cross sentences. An additional explicit predation query (saved without corpus text as `data/predation-query.json`) required a hawk term, one of kill/eat/hunt/devour/prey/swoop/tear/pluck, and a dove term, or the reverse, with at most fifteen intervening tokens on either side of the verb. It returned a completed zero. A positive control using the same lemma attribute returned matches. This narrow pattern is not a test of every possible word order, verb or distance.

Wider annotation requests used `kwicleftctx=-80` and `kwicrightctx=80`, plus newspaper/date/year references. Full-context hashes detect source changes; no newspaper text is shipped.

[Hansard's API](https://hansard-api.parliament.uk/swagger/ui/index) was queried at `/search/contributions/Spoken.json`, with `queryParameters.searchTerm=hawks doves`, start `1800-01-01`, end `2026-11-19`, `queryParameters.skip=0/100`, `queryParameters.take=100`. The two pages contain 100 and 11 distinct contribution IDs, matching the API's total of 111. Bare `skip` and `skipContributions` were ignored; duplicate pages were rejected. Bare-word multi-term retrieval is not a lexical census or a guarantee of perfect search recall. Three nineteenth-century animal allegories and one uncertain literal nesting joke are excluded from the policy denominator.

[Govinfo](https://api.govinfo.gov/docs/) was accessed with its public DEMO_KEY. POST `/search` with query `collection:CRECB AND hawks AND doves`, `pageSize=100`, `offsetMark=*`, sorts `score DESC` returned a candidate count of 6,771 archive granules and 100 result records. This metadata count is not a political denominator. A 1999 text and a 1966 bound-Record PDF were read; the latter reprints a newspaper elaboration. Selected web-indexed historic Record passages were candidate leads, not an exhaustive concordance. No US frequency estimate is made.

[Google Books Ngram](https://books.google.com/ngrams) used `en-2019`, case-insensitive, smoothing 0, 1900–2019. Seven queried phrases are in `ngram-query-status.csv`. Two returned series, five did not. A missing series is not replaced by zeros. Frequencies include literal and metaphorical senses and are normalised ngram frequencies, not political counts. Decade values are simple means of the ten returned yearly frequencies, not reconstructed token totals.

GDELT DOC requests failed (first transport failure, then HTTP 429). The Quora short link returned HTTP 403, and indexed exact-title/short-link searches recovered no answers. The Federal Reserve and ECB examples were selected primary documents; no source-wide denominator is claimed. The claim that most other metaphors are dissected was **not tested**: no matched comparison-metaphor sample or denominator was assembled.

## Judgement rules

An agent read local contexts and made each judgement; Python only records and counts the decisions. The annotator was gpt-6.1-sol. No independent human or second model validated these annotations.

1. **Policy sense:** a label for a person's, faction's or policy's relative militancy, conciliation, monetary tightening/easing or fiscal strictness. Metalinguistic discussion of these labels and political views in reviewed fiction can qualify. Exclude literal animals, peace emblems without a policy actor, names, brands, aircraft, sports teams, and generic non-political temperament or corporate management.
2. **Bird elaboration:** a further recognisable bird property or scene: cooing, feathers, talons, flight, fluttering, captivity, aviaries, or deliberately adding other bird species to the political taxonomy. Plain “becoming a hawk”, aggression, battles, victory, opposition, head/soul contrasts and generic human displacement do not suffice.
3. **Chase/displacement:** hawks explicitly act against doves in a reactivated bird scene. P095 qualifies because a White House claim is explicitly paralleled with real birds of prey at Wimbledon. It does **not** say kill or eat.
4. **Killing/eating:** a hawk kills, eats, devours, tears up or explicitly hunts a political dove. Nearby violence against another target, literal predation, biological game theory and the author's own proposed example do not qualify. No unambiguous qualifying case occurred in the annotated sets.
5. **Uncertainty:** record it, exclude uncertain elaborations from positive counts, retain locators. Seven P rows have ambiguous puns and are not counted as elaboration; H035 nesting is uncertain between literal observation and political joke; H101's elephant image is a mixed zoological scene, excluded from bird-specific elaboration. Confidence is a model judgement, not validation.

Examples: H106 cooing/squawking, H053 feathers/talons and S066 circling are elaboration. P095 is chase, not killing. P040 is doves grounding hawks, not hawks eating doves. S048 is a descending peace emblem, excluded from the policy-actor sense. P063 is literal birds. P110–111 concern corporate management, excluded. H078's angry doves/peaceful hawks is conventional stance contrast, not an extra bird property.

Invalidation: changes to the saved context, counting definition or policy-sense rule require reannotation of affected rows. The checking script cannot determine whether those judgements are right.
