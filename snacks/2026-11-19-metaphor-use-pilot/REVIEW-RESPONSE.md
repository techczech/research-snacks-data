---
title: Source-review response for the metaphor-use pilot
date: 2026-11-19
provenance: Completed coordinator-requested source critique; all findings checked against frozen records and archived primary sources
requested_model: gemini-4-neon
returned_model: Gemini 4 Neon (High)
provider: antigravity
status: all-eleven-material-findings-applied
---

# What this review establishes

The coordinator started this replacement review at full access after cancelling an earlier approval-blocked attempt. The requested model was gemini-4-neon through T3 provider antigravity. The completed review frontmatter reports actual model Gemini 4 Neon (High). Usage was not supplied. It audited claims and arithmetic, not a third annotation pass, human checking or gold labels. Its timing/token and live-site scope was limited; final build and deployment checks are separate.

All eleven material findings were accepted after inspecting the underlying evidence. No A/B label, excerpt string or unit offset was changed. Updated dates/notices are separated from the exact frozen original metadata. Additional CSVs only recount those same records.

| Finding | Verification | Applied correction |
|---|---|---|
| 1. Independence and defaults | Both JSON records name the same configured model; provenance distinguishes A's manuscript/codebook context from fresh B. The serializer has constitutive/explanative/declarative/none/local defaults; 24 units use its cognitive default. | Removed independent-reading claims from current narration/chart. Exposed asymmetric preparation and serializer, with no causal claim about the defaults' effect. |
| 2. Positive verdict | Identification κ 0.8113; cognitive κ 0.0964; figurative κ 0.1282; binding κ −0.0238. | Revised verdict: identification reproduced within this run; these use judgements did not. No narrator claim that the dimensions hold up. |
| 3. Changed categories | Original paper and frozen v1 differ on cataphoric/exophoric evidence, conceptual/declarative, exegetic, conventionality, explanative subtypes and prevaricative scepticism. | Added explicit paper/pilot comparison and qualification that this is not a direct test of the entire 2005 scheme. |
| 4. Uncertainty | Use counts filter M only; U totals 7/13; 14 identification differences involve U and 8 are M/L; joint U=P018/S068/E054. | Added passage U counts, confusion matrix, U table and excluded joint-U differences. Zero uncertain use rows are identified as M-only schema counts. |
| 5. Chart2 and elaboration | All use comparisons n=51; binding matches35 none/none, zero positive matches. Elaboration is a 1:1 recoding here. | Added n and visible κ labels/caption to Chart2, including figurative appeal; stated elaboration is not a separate result. |
| 6. Representative examples | Cognitive disagreement direction 20 constitutive→attributive versus 5 reverse; two-unit examples and hallucination binding differences confirmed. | Added field/conventional-word example, direction counts, unit IDs/multiplicity, omitted binding and explicit M/U identification contrasts. |
| 7. Chart1 denominators | Common-unit margins A 34/17, B 19/32; full sets A 40/19, B 19/39 on 59/58 units. | Chart1 now plots common 51-unit counts; page retains both full and common margins. |
| 8. MIP and L | Original MIP requires contrast and comparison, whole discourse and binary decisions; L does not imply literal use. | Restored criterion, disclosed excerpt/orthographic/U/direct-comparison adaptations, replaced current L=literal wording. Historical codebook remains unchanged and labelled as such. |
| 9. Stopping/counting | Sampling code uses >=50; Wikipedia exactly 50; two standalone policy hyphens explain 404 whitespace tokens versus 402 units. | Corrected stopping prose and added both counts to corpus-summary.csv and the page. |
| 10. Dates/licences | Archived Python footer 18 November 2026 at 23:07 UTC; NASA 23 October 2024; exact PSF/OGL notices; OPL now successfully captured; source transformations inspected. | Corrected metadata while retaining frozen v1; exact notices and proper PSF licence title; changes/credits, NASA scope/non-endorsement, archived/cited OPL, source notices in both repos. |
| 11. Concentration/baseline | Exegetic/performance labels each one passage; passage scope two. Social matches include 30 declarative-only and 6 Wikipedia exegetic sets. | Added document counts, baseline decomposition and per-label social κ including undefined constant declarative. |

No complete material finding was rejected. One source qualification matters: the review described conventionality as context-independent; the manuscript itself makes recoverability dependent on individual knowledge and use. The revision preserves that distinction rather than applying blanket context-independence to both parts.

The minor editorial items were also addressed: broadened the use-count heading, changed the serializer description to agent-judged, encoded parentheses in Wikipedia links, and retained final relative-link/rendering verification as a release gate. No new metaphor annotations or post-hoc adjudication were performed.
