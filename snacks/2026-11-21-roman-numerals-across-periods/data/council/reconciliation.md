---
title: Council reconciliation and build decisions
date: 2026-11-21
by: Claude Opus 5.5 (coordinator)
inputs: findings.md (GPT-6.2 Sol), council/claude-haiku-5-5.md, council/gemini-4-neon.md
---

## Where both reviewers agree
- The research is a sound base for examples and glosses; the 0–3 ratings are editorial judgement from partial reading (2 of 45 references read in full), not corpus frequencies. The tool and write-up must say so.
- Split `archaic` into early fifty (ↆ) and late six (ↅ); drop unsupported labels (e.g. "Merovingian").
- Implement opt-in date converters (AUC, Spanish era); defer regnal years and Byzantine Anno Mundi.
- Defer medieval letter numerals as a scoring rule.

## Where they differ, and the decision
- Zeros. Sol's pass set some cells to 0 where it found no example (omittedMillennium all 0; early-medieval runSub; early-modern irregularSub/omittedCentury). Gemini: absence of evidence in a quick search is not unlikelihood. Decision: separate "no evidence found" from "unlikely". A cell with no evidence found is shown as such (grey, hatched) and does not veto a reading; only positive evidence of rarity or anachronism gives 0. Use Gemini's suggested cells where Sol's were zeros from absence (omittedMillennium [0,0,2,1,0]).
- Genre/region-conditional conventions (vigesimal, Spanish era, chronogram). Decision: rate them for their home genre and show a "where" note (e.g. French and English accounts; Iberian charters) rather than a global "typical".
- Indiction: Haiku says implement now (explicit selector), Gemini says defer. Decision: implement as an explicit converter that lists candidate years within the chosen period (an indiction number alone is ambiguous every 15 years) — cheap and honest.
- Medieval letter numerals: both say defer as a scoring rule; Dominik approved the addition. Decision: show them as an opt-in reference gloss (each letter, its values in the sources consulted, where lists disagree), not as an automatic reading.
- Passage reading: deferred by both. Dominik approved. Decision: implement a simple "find numerals in a passage" mode (dot-delimited .xx. and standalone numeral words), each linked to the full analysis; no automatic chronogram hijack — chronogram becomes an explicit toggle.

## Parser fixes (all agreed or found by a reviewer)
- `readMultiplied` must apply a multiplier only to the run of smaller numerals just before it: Mᵒiiijᶜlvj must give 1456, not 100,456.
- Overbar: add a "distinction bar" reading (×1, bar marks a numeral) alongside ×1000.
- Framed apostrophus |(I)|; dot-separated scores (.iiij.xx.); W = VV = 10 in chronograms (on the cited page).
- Minimum aggregation: keep min, but a "no evidence found" cell does not lower the score below "rare".

## References
- Remove shadow-library links ([unofficial copy host withheld], [unofficial copy host withheld]); cite the publisher or library record instead and mark not read in full.
- Remove references never read and never cited (cagnat 404, karger shell); add the missing Du Cange URL or drop the claim.
- Fix examples: IX.XX.XVI is 196 in a document dated 1231 (not 1231); verify XLVIII on the Persée page or drop it; examples resting on unreachable sources are labelled so.
