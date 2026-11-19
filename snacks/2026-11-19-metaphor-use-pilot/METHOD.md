---
title: Method and review corrections for the metaphor-use pilot
date: 2026-11-19
provenance: Frozen v1 instructions and A/B labels; verified Neon source critique; arithmetic-only revision
---

# What was compared

This is an unchecked pilot, not a validation of the 2005 classification. Both passes used the same configured gpt-6.1-sol model. Pass A ran in the coordinator context after reading the manuscript, planning notes and source pages and writing the codebook. Pass B ran fresh with only that codebook, six excerpts and numbered units, plus a parent message identifying the inherited configuration. B did not see A's labels or a proposed verdict; its provider-returned model ID was not independently exposed. These are asymmetric separate-context passes, not two independent readings or human raters.

The Pass A serialization script is included in `code/annotate-metaphor-pass-a.py`. Its defaults were cognitive=constitutive, elaboration=explanative, social=declarative, binding=none and scope=local. Twenty-four unit records used its default cognitive value. The serializer did not require a fresh explicit cognitive choice for each record. This may have affected the distribution; its effect cannot be separated from context and judgement here. The annotations were made by a model, not a human. The reproduction script only counts frozen records and inspects the serialization calls; it does not classify meaning.

# Sampling and units

Six documents were purposively chosen for genre, topic, access and reuse terms. No population frame or random draw was used. Select opening prose, omitting headings, salutations, images and reference numbers, until the first paragraph boundary with **at least 50 whitespace-separated tokens**. Wikipedia stops at exactly 50. Hansard contributes three short opening paragraphs; NASA's captured HTML has one combined prose paragraph. The current commission replaced the earlier education-only, human-checked plan with six genres and machine passes; these excerpts are shorter than the earlier proposed windows.

There are 404 whitespace tokens and 402 orthographic units. Only the policy excerpt differs: its two standalone ASCII hyphens count as whitespace tokens but are excluded by the word pattern, giving 70 versus 68. All other passages have identical counts under both conventions. `corpus-summary.csv` now includes both denominators. Numbers, internal hyphens and apostrophes are retained by the word pattern. These units need not equal MIP lexical units; two words of a phrase remain two correlated observations.

Current editions are not evidence of the original composition date of each paragraph. NASA's captured page says last updated 23 October 2024; Python's captured footer says 18 November 2026 at 23:07 UTC. `pilot-texts.json` corrects those dates and notices without changing text, MD5s, offsets or labels. `pilot-texts-frozen-v1.json` preserves the exact original input, including erroneous metadata. `CODEBOOK.md` is the unchanged historical v1 instruction file, including its imperfect terminology. This method records corrections rather than silently rewriting what the passes saw.

# MIP-informed identification

MIP asks whether the contextual meaning **contrasts with** a more basic contemporary meaning but can be understood through comparison with it. It begins with the entire text-discourse and makes binary metaphor decisions. The pilot instead used short excerpts, orthographic forms, an added uncertain category and an extension for overt comparisons. Its original summary under-specified the contrast criterion; the current explanation restores it without rerunning the labels. Model linguistic knowledge supplied senses; there was no systematic dictionary verification. This is an adapted, unvalidated procedure.

M means metaphor-related, U uncertain, and L **not metaphor-related**. L includes proper names and metonymy excluded by this pilot's rules and does not establish literal use. Every unit was considered in its excerpt; unlisted IDs were declared L. Marked/uncertain records include evidence and confidence. Neither pass is gold, no human checked them, and no adjudication was made.

# Departures from the 2005 scheme

| Component | 2005 account | Pilot operationalisation or omission |
|---|---|---|
| Cognitive use | Constitutive–attributive continuum; uses can coexist or change. | Discrete labels, with mixed/uncertain available; no M unit received either. |
| Cataphoric | Opens a mental space for possible later reference, potentially over a whole book. | Required realised later development inside the excerpt. |
| Exophoric | Ties to surrounding discourse and its associations. | Required an identifiable external discourse/allusion; familiarity alone excluded. |
| Conceptual/declarative | Default sharing of conceptual background, potentially superseded by other functions. | Declarative was always on for every M unit in both passes. |
| Exegetic | A new reading of somebody else's position, discussed with deliberate/generative uses. | Assigned to the Wikipedia terminology/synonym explanation, largely attributive. |
| Conventionality | Salience and recoverability are discussed separately; recoverability depends on individuals and use. | Both unmeasured; agent recognition is not a reader measure. |
| Explanative subtypes | Structural, ontological, orientational. | Not coded. |
| Prevaricative | The paper itself doubts its separability and warns about imputed intent. | No deceptive-intent assessment without external evidence; zero assignments prove no absence. |
| Textual scope | Local versus global organisation. | Only local versus passage-wide; whole-document scope unavailable. |

These differences prevent treating low agreement as a direct test or refutation of the complete 2005 scheme.

# Counts, uncertainty and agreement

Identification uses all 402 units with M/L/U. Use agreement is restricted to the 51 units both mark M. Full-pass use counts use different M sets: 59 in A and 58 in B. Chart 1 now plots the same 51 units for both passes; its counts are A=34 constitutive/17 attributive and B=19/32. The full-set counts remain in `use-counts.csv`.

`use-counts.csv` excludes all U identifications. Its uncertain-label rows are zero only within each M set, not evidence that the pilot lacked uncertainty. A's 7 and B's 13 U records remain in the raw JSON and `uncertain-annotations.csv`. Fourteen identification disagreements involve U and eight are direct M/L differences. Three joint-U units (P018, S068, E054) are excluded from functional scoring, despite social disagreement on all three and binding disagreement on S068. `disagreements.csv` contains 64 scored unit rows: 22 identification differences plus 42 functional differences among common M units; it is not every possible difference among U annotations.

Unweighted Cohen's kappa=(observed agreement−chance agreement)/(1−chance agreement), with chance computed from marginal category frequencies. Social/binding exact-set kappa treats each sorted label set as a nominal category; per-label kappas are also supplied. Constant labels give undefined kappa. The supplementary M/L calculation drops any U; it is a sensitivity analysis, not a replacement headline. There is no human-reliability claim, population inference, significance threshold or confidence interval; words within phrases/passages are clustered.

Elaboration is exactly a recoding of cognitive use in this sample (constitutive→explanative, attributive→na); its identical agreement is not an additional result. Twenty of 25 cognitive disagreements are A=constitutive/B=attributive, mostly grammatical or conventional wording; five go the other way. Figurative appeal has κ 0.1282: only one of nine units tagged by either pass was tagged by both. All 35 binding agreements are none/none; no positive link was agreed. Social exact-set agreement includes 30 declarative-only baseline matches and six declarative+exegetic matches in one Wikipedia passage. Exegetic and performative each occur in one passage; passage-wide scope in two. Perfect local/passage agreement does not test global organisation.

# Review and next study

The coordinator requested gemini-4-neon through antigravity; the completed review reports actual model **Gemini 4 Neon (High)**. The earlier approval-blocked attempt was cancelled and provides no completed review. The source critic checked counts and claims; it did not supply a third annotation pass or human validation. All eleven material findings were accepted after checking the frozen records. Conventionality is described with the manuscript's reader/use qualification rather than as wholly context-independent.

A full study first needs explicit source-to-target inference evidence for constitutive use, contrasting examples, symmetric training/exposure and no silent serialization defaults. Reconcile original versus narrowed categories before testing them. Separate identification from use/mention, clause-level commitment and textual links; retain uncertain cases in the reporting plan. Calibrate on old examples, freeze a revised manual, then use independent human annotators on held-out, sufficiently contextualised passages from a defined sample. Reader tasks are needed for salience/recoverability. No such validation has occurred here.

# What rerunning proves

The eleven expected tables reproduce saved counts, marginals, uncertainty, agreement and plotted rows. Rebuilding them verifies arithmetic and file consistency only, not the accuracy of the annotations, source facts, licences worldwide, or the theory.
