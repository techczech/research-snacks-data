---
title: Metaphor-use pilot codebook v1
date: 2026-11-19
status: frozen-before-annotation
provenance: Dominik's commissioned pilot; Lukeš 2005 author manuscript; Pragglejaz Group 2007 pp. 3-4
---

# Question and design

Does separating cognitive, social and textual USE help interpret modern metaphorical wording? Do independent readings of the same instructions agree? This is a convenience sample and a codebook test, not a prevalence estimate or validation of the 2005 theory. The current user brief authorises six genres and machine annotation with no human validation; this supersedes the earlier education-only, human-checked plan. All annotations remain provisional and unchecked by Dominik.

Six named documents were chosen purposively for genre/access, not randomly from a population. Select opening prose, excluding headings, salutations, figures, objectives and footnote numbers; stop at the first paragraph boundary after 50 whitespace words. Hansard has three short opening paragraphs. NASA HTML combines what are separate browser line blocks into one paragraph; retain that paragraph. PDF textbook candidate was rejected for changed restrictive terms before annotation; use Python tutorial instead. Source topics were known before sampling; selection is not blind to topic or prior familiarity.

# Identification

MIP baseline: read the whole selected passage; consider every numbered unit; state contextual meaning, a more basic CURRENT meaning and whether comparison permits the contextual reading. Do not infer from keywords or etymology alone. Model linguistic knowledge supplies candidate senses; there is NO systematic dictionary verification, so call this MIP-informed, not a certified MIP/MIPVU annotation. Add overt direct comparisons/analogies as a declared extension. Proper names and metonymy alone are literal for this task; do not interpret a brand name as metaphor without local reactivation. Units are mechanically frozen orthographic word forms (apostrophes/hyphens retained), not full MIP lexical-unit segmentation. Mark constituents of a multiword metaphor separately and give shared evidence; no phrase-level reliability claim.

Annotate all 402 units: M=metaphor-related (includes direct comparison), L=not metaphor-related, U=uncertain. Supply records for every M or U; all omitted unit IDs must be explicitly declared L after reading EVERY unit. Record a short basic/contextual contrast and confidence (high/medium/low). No minimum or maximum number of metaphors; retain negative cases.

# Use classification for every M or U

- cognitive: constitutive / attributive / mixed / uncertain. Constitutive: the source supplies relations or inferences used to organise the passage's account. Attributive: selected properties or associations with no developed source structure. Mixed: both with identifiable evidence. Sparse conventional wording may still be constitutive, but a possible historical mapping alone is insufficient. Use uncertain if the local context cannot distinguish.
- elaboration: explanative / generative / uncertain / na. Explanative for routine sense-making or explanation using available mappings; generative only where a reconceptualisation visibly produces a new proposal or inference. Attributive normally na. The 2005 distinction is nested especially under constitutive, not a competing metaphor species.
- social: one or more of declarative, figurative, innovative, exegetic, performative, uncertain, separated by | and sorted. Declarative shares an account; figurative adds expressive appeal; innovative proposes a new view; exegetic interprets another's formulation; performative enacts an explicit position/commitment in context (a will-clause alone is not enough). Overlap allowed. Never infer prevaricative intent from disagreement or inaccurate analogy: use independent evidence, otherwise not assessed. Report zero observed evidence as no evidence, not proof no deception.
- binding: any of none, anaphoric, cataphoric, exophoric, uncertain, sorted with |. Anaphoric needs a named earlier textual anchor; cataphoric needs a later identifiable development within the selected passage (not just possible future reference); exophoric needs an identifiable outside discourse/allusion, not familiarity alone. None=no specific binding tie observed in this passage. The broader 2005 sense of cataphora remains a codebook question.
- scope: local / passage / uncertain. Passage means organises this entire selected passage; NEVER equate with global organisation of the full document. Full-document global scope is not assessed.
- salience and recoverability: not assessed for all records. An agent's ease of recognising a metaphor cannot measure a reader's experience.

# Calibration (old evidence, not evaluation)

The Fourth R: often attributive, associating the added subject with basic skills. Pedocratic oath: source roles generate proposed ethical obligations, supporting constitutive/generative and innovative. Baker's education-consumer formulation: a commitment can be performative while using familiar metaphors. Marriage vocabulary can recur across a passage without a full constitutive transfer. Functions overlap: do not force a single social label.

# Independence and outputs

Pass A: coordinator model in its current context, records data/pass-a.json. Pass B: separate fresh-context model run, reads only this codebook, data/pilot-texts.json and data/pilot-units.csv, records data/pass-b.json. B must not inspect A, any results or proposed verdict. The same model family is permissible; context independence is weaker than different-model/human independence and must be disclosed. Outputs are frozen before comparison; no adjudicated gold labels. Code counts fixed labels only. Agreement: identification over all fixed units (three categories, plus binary sensitivity excluding U if present); use dimensions on common M units only; exact social/binding SET agreement plus per-label binary kappa. Kappa is descriptive for these two readings; constant margins make it undefined. No invented agreement or threshold for validity.
