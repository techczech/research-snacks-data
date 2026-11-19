---
title: Method and limits of the metaphor-use pilot
date: 2026-11-19
provenance: Frozen v1 codebook, input hashes and independent A/B annotation records
---

# Sampling and reconstruction target

Six texts were purposively chosen to cover a parliamentary speech, government policy, encyclopaedia, news report, science explainer and programming tutorial. No collection frame or random document draw was used. The current commission changed the earlier education-only plan to multiple genres and allowed machine passes. Opening passages ended at the first body-paragraph boundary after at least 50 whitespace words, excluding headings, salutations, figures and reference numbers. The resulting windows contain 50–87 orthographic units. They are shorter than the earlier proposed 250–400-word windows; the purpose is a small cross-genre codebook test.

Stable units retain apostrophes and hyphens and split punctuation. Numbers are units. They do not necessarily equal MIP lexical units; multiword expressions are represented by several units. Every unit has an ID, text ID and character offsets into `pilot-texts.json`. Full-document global coherence cannot be measured from these excerpts. “Passage” is deliberately used in place of “global”.

# Identification and use judgements

The MIP-informed baseline compares meaning in context with a more basic current meaning, checking whether comparison supports the contextual reading. Overt analogies are included as a stated extension. The models supplied linguistic senses; no systematic dictionary audit was performed. This is not a validated implementation of MIP or MIPVU. The code never classifies words by keywords.

A was frozen before B's result was read. B ran in a fresh context and saw only the frozen codebook, six texts and numbered units; no A labels or proposed verdict. Both were configured gpt-6.1-sol. Independent contexts reduce label leakage but do not provide independent model families or independent human judgement. Neither pass is gold. Both originals are retained without adjudication.

Each marked/uncertain unit records identification, cognitive use, nested elaboration, social functions, textual binding, passage scope, confidence and evidence. Other units were explicitly declared L after every unit was read. Cognitive labels allow constitutive, attributive, mixed and uncertain. Social/binding labels may overlap. Reader salience/recoverability and deceptive intent are not measured. Codebook v1 contains the calibration examples and operational rules.

# Arithmetic and denominators

Identification agreement uses all 402 units and three nominal categories M/L/U. A supplementary binary result excludes every unit that either pass calls U; this is a sensitivity analysis, not a replacement for the three-category headline. Use agreement includes only the 51 units both passes call M. Use counts use each pass's own M set (59 and 58), so their denominators differ from the agreement subset. Uncertain identifications remain in the raw files and identification table, not in the M-only use counts.

For N paired labels, observed agreement is the fraction equal; chance agreement is the sum, over categories, of the two marginal proportions' products. Unweighted Cohen's kappa is (observed − chance)/(1 − chance). Social and binding exact-set kappa treats each sorted label set as a nominal category; per-label binary kappas are also provided. Constant margins make kappa undefined, even when raw agreement is perfect. There is no reliability threshold, confidence interval or population inference. Word units from one multiword expression are correlated; repeated words and six passages are not independent participants.

Elaboration agreement repeats cognitive agreement because every constitutive decision in this sample was also explanative; these are not independent confirmations. No generative/innovative labels were assigned, and no prevaricative intent was assessed. Empty categories cannot establish their usefulness or absence in other writing. Both passes agreed on local/passage scope, but that does not establish full-document global validity.

# Scaling decisions

Revise the constitutive/attributive manual to require stated source-to-target inferences and a specified evidence span; include counterexamples where a comparison merely attributes a property. Add a separate use/mention/direct-analogy field. Require explicit anchors for backward/forward binding and distinguish ordinary lexical repetition from metaphor-dependent links. Preserve overlapping social labels and assess commitment at a clause/passage level before projecting labels onto words. Test the revised instructions with independent human annotators on held-out passages, after calibration. Longer whole-document context and a defined sampling frame are needed for a full study. A reader task is required for salience/recoverability.

# What a passing check establishes

The saved annotations, counts, confusion matrix, agreement statistics and plotted rows can be reconstructed byte-for-byte. A successful run does not establish a correct metaphor inventory, the truth of a source passage, a validated taxonomy, human agreement or an approved change to the 2005 paper. Source permissions and attribution are recorded separately.
