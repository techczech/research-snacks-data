---
title: "Can a cake be sickly? — method"
date: 2026-11-18
provenance: Published Research Snacks and their archived analysis inputs
---

# Method: sickly

The original study queried exact word forms, not only adjective tags. The BNC version was `preloaded/bnc2_tt31`, written OANC `preloaded/oanc_text`, and spoken OANC `preloaded/oanc_speech`. The query is `[word="(?i)sickly"]`. The original word totals and hit counts are in `corpus-totals.csv`; rates divide exact-form hits by words and multiply by one million. These are not national prevalence estimates.

Judgement steps are deciding whether a referent is food/drink or another inanimate thing; assigning attributive, explicit verbal-complement or elliptical/supplementary construction; distinguishing a sole adjective from coordination; and interpreting flavour, visual or metaphorical readings. Degree expressions do not count as additional adjectives. Explicit complements include object predication. Elliptical cases cannot be counted as complete predicative clauses. The 15 cases were selected after reading wider contexts, not sampled randomly. `food-annotations.csv` preserves their original decisions without text.

`example-locators.csv` preserves construction/reading labels and token anchors for the 39 curated examples, including diagnostic exclusions. The supplementary corpus names match the original study. Rebuilding this count does not recreate the searchable text table on the website. The two cake rows use a passage anchor shared by the retrieved context; neither is a verified token position for the later predicate.

The window query settings are in `queries.json`: five tokens either side, lemma collocates, candidate frequency at least five, pair count at least two, maximum 100, ordered by logDice. No additional sentence boundary was configured. The BNC self-collocate was excluded in the original displayed array. T-score = (pair − node×candidate/tokens)/sqrt(pair); MI = log2(pair×tokens/(node×candidate)); logDice = 14 + log2(2×pair/(node+candidate)). Token totals differ from word totals used for rates. Five-decimal provider scores are checked within 0.00002 before final tables are diffed.

No clear food evaluation was found among the thirteen American hits. All twelve written OANC hits were automatically tagged as adverbs, including clear adjectives. This is why the automatic sketch is not reliable evidence for a dialect difference. Auditing those syntax judgements requires your own authorised source access; this release does not perform new corpus calls.
