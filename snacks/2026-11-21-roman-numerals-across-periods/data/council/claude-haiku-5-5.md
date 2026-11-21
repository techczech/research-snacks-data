# Council review: Roman Numeral Reader research pass

Reviewer: Claude Haiku 5.5 (claude-haiku-5-5). Date: 2026-11-21. Packet: `research/council/packet.md`. Read-only except this file.

## Position in five lines

The research pass is a sound base for examples, glosses and deterministic converters, but its 0–3 ratings are not yet evidence-based enough to publish as period priors.
The sources I could reach mostly confirm the examples I checked; 14 of the 48 examples rest on three sources I could not reach (Kajanto, Chrisomalis, Pollard).
Nine cells rated 3 have at most one example in their period, and four of those have none, so the 3s are overclaimed.
Two errors need fixing before any write-up: IX.XX.XVI is a quantity of 196 dated 1231, not a 1231 reading, and the "Merovingian" label for the late six is not in the cited source.
Implement now: apostrophus glosses, explicit-selector converters (AUC, Spanish era, indiction) and a split of ↆ from ↅ; wait on alphabetic numerals, regnal years, Byzantine Anno Mundi, chronogram variants and passage reading.

## 1. Are the ratings supported?

I checked each proposed vector against the examples in `examples.json` (count of examples carrying that feature in the same period) and against the justification text in `ratings.json`. I also read `roman.js`. `scoresFor` takes the **minimum** of a reading's feature weights, so any 0 removes that reading in that period. The findings say "zeros are not evidence of absence", yet the engine treats 0 as elimination. That mismatch matters for the zeros proposed for `ignored`, `separate` and `omittedMillennium`.

Ratings I think are wrong or overstated:

| Feature | Period | Proposed | Examples in period | Problem | Suggested |
|---|---|---:|---:|---|---:|
| `multiplicative` | High & late medieval | 3 | 1 | "Frequent" rests on Cappelli's description and one 1456 plate, with no count. | 2 |
| `finalJ` | High & late medieval | 3 | 2 | Generalises from Scottish records and Augsburg print to the whole band. | 2 |
| `finalJ` | Early modern | 3 | 5 | Attested, but "typical" needs a counted corpus the findings say they lack. | 2, or 3 for a Scottish/English profile only |
| `vigesimal` | High & late medieval | 3 | 2 | Both examples are cited through Chrisomalis (unreachable); one is mis-dated in the text. | 2 |
| `ordinalMarks` | High & late medieval | 3 | 2 | A grammatical marker, not a numeral value. One colophon plus Cappelli. | 2, or move to display flags |
| `distinctionMarks` | High & late medieval | 3 | 0 | Generic punctuation, not a reading convention. No example. | 1, or drop from the ratings |
| `regnalYear` | Early medieval / High & late | 3 / 3 | 1 / 0 | The input carries no ruler, so no default prior can apply. Madalfredus is unresolved (802 or 808). | 0 by default; ruler-gated |
| `spanishEra` | Early medieval / High & late | 3 / 3 | 1 / 0 | Typical in Iberia only. Mixes a regional prior with a general one. | 1 by default; 3 when region is set |
| `byzantineAnnoMundi` | High & late (also 2 in early med.) | 3 | 0 | The originals use Greek numerals; out of scope for a Roman-letter reader. | 0; exclude |
| `indiction` | Early medieval | 3 | 1 | One charter (St Gall, 933). | 2 |
| `clockIIII` | High & late / early modern | 2 / 2 | 0 / 0 | The only dated dial in the set is 1890–1910. The `bn` citation (Anais da Biblioteca Nacional, vol. 140) is not shown to concern clocks. | 0–1 late medieval; 1 early modern pending a source |
| `multiplicativePlain` | High & late medieval | 2 | 0 | No medieval example in the set. | 1 until one is found |
| `minim` | High & late / early modern | 2 | 0 | No example at all. | Keep only once examples exist |
| `vinculum` | Classical / High & late | 2 / 2 | 0 | A core engine feature with no example. | Keep; add examples |
| `archaic` | Classical | 2 | 0 | The combined vector is a copy of `lateSix`; the findings' own text says ↆ and ↅ need separate priors. | Split (see section 4) |

The following look well supported and I would keep them: `additive4` (5, 4, 5 and 3 examples across four periods), `standard`, `ad` (0 classical, 2+ thereafter), `auc` (Hadrian's coin is the only classical instance; 1 is defensible), and `earlyFifty` and `lateSix` for classical and late-antique use. Perry's Unicode proposal dates the late six to Roman imperial times and later.

Scale problem. The findings define 3 as "typical within the documented genre or tradition", but the numbers are then combined as if they were general priors. Regional conventions (Spanish era, Scottish final j, French scores, Chronogram in central Europe) therefore score as high as a general convention. Either gate regional features on a selected tradition or report them under separate scales.

Engine problem. `yearReadings` adds a BCE `auc` candidate for every numeral below 753. The findings' own test output shows this (DCLXXXIII → −70). Gate AUC behind an explicit era selection.

## 2. Spot-checks against sources

I fetched cited pages on 21 November 2026. Results:

| Claim or example | Source checked | Result |
|---|---|---|
| `ↀↀↀↀ C XLI` = 4141; 142–180 CE; distance slab | RIB 2205 (romaninscriptionsofbritain.org) | **Confirmed.** Diplomatic line reads "ↀ ↀ ↀ ↀ C XLI"; the translation gives 4,141 feet (*p(edum)*). |
| `IIII CĐXI` = 4411; 142–161 CE | RIB 2208 | **Confirmed** for the text ("p(edum) IIII (milia) CĐXI"). The record's date line reads "a.d. 142-61", almost certainly a typo for 142–161. The findings silently correct it; say so. |
| `July IV, MDCCLXXVI` on the Statue of Liberty | NPS "Statue Front" | **Confirmed.** Day 4 and year 1776; the tablet is dated July 4, 1776. |
| Köbel 1514: `II C / IIII C .LX` = 200 / 460; Pliny `LXXXIII.M` = 83,000 (c. AD 77); Frank `vij·c.` = 700 (1534, fol. ccxx) | Cajori, *History of Mathematical Notations* §§50, 55 (Wikisource) | **Confirmed.** The Frank attribution is in a footnote (Weltbuch, 1534, fol. ccxx). Karpinski's XXCIII for 83 (c. 130 BC) is Cajori's second-hand report. |
| `IIX` = 8 (71 CE, CIL VI 931); `XIIX` (Prusa, CIL III Suppl. 6993); `CCCXXC` = 380 | Egbert, *Introduction to the Study of Latin Inscriptions* (Wikimedia PDF) | **Mostly confirmed.** CIL VI 931 shows "tr. pot. III, imp. IIX". The Prusa text shows "imp. XIIX". `CCCXXC = 380` is confirmed; I did not find the 157 BCE date for CIL I 536 in the passage. Note also that the XIIX in CIL II 2107 is Augustan, not Flavian. |
| Late six (ↅ) as 6, 8th century | Perry, Unicode L2/06-269 (n3218), fig. 16 | **Partly confirmed.** The 8th-century date and the Cappelli source (pp. 418–419) are right. The label "Merovingian" is **not** in Perry and I did not find it in the Cappelli text. Perry also says the late six is "common from the second century CE onwards" and gives 6I = 7, 6II = 8, 6III = 9. Neither point is in the findings. |
| Andernach battle, 8 October 876, in the Ambrosiana calendar | Prinz (1972), MGH copy of Ambros. M 12 sup. | **Confirmed**, with two caveats. The OCR is garbled ("dcccl.xxui"), so check the plate for the exact spelling. Prinz also argues that the 5 October entry, recording Charles the Bald's death in 877, wrongly carries 876. That scribal year error is in the same calendar and belongs in the example's note. |
| Letter-value table (A 500, K 151, etc.) attributed to Cappelli pp. 430–436 | Cappelli OCR (archive.org); Cajori's Tartaglia 1556 table | **Unresolved.** Most values match Tartaglia's table as Cajori reproduces it, which the findings do not cite. Tartaglia gives K = 51; the findings' Cappelli column gives K = 151. I did not locate the letter-value table in the Cappelli OCR within the time I spent. |
| Chrisomalis examples: `IX.XX.XVI` (1231), `IIIIˣˣ et huit` (1388), `XVCXIV` (1514), `|(I)|` (Ostia, 36 CE) | [unofficial copy host withheld] PDF | **Not verified.** The link returns 404. |
| Kajanto examples: 963, 977, 981, 1412, 345, 517 | journal.fi PDF | **Not verified.** The PDF returns a bot-check page; the landing page has no abstract. |
| Pollard examples: `XCij` (1492), `lxxixº` (1479), `M.cccc.xc.` (1490), `M.cccc.lxxxxiii.` (1493) | Gutenberg | **Not verified.** Gutenberg returned 503 ("temporarily down for maintenance") on every attempt. |

Internal error (not a retrieval issue). `IX.XX.XVI` is worth 196 by the reader's own rule (9 × 20 + 16). The findings say "Chrisomalis prints IX.XX.XVI (1231)" and that the rule "misses the 1231 example". The 1231 is the document date, not the numeral's value. The example should carry 196 as the quantity and 1231 as the date, and the findings should not present a reading of 1231 as the target.

Other example semantics. The `values` field mixes three things: a date (`XCij` → 1492), a sum inside a dated line (`lxxixº` → 79, `Lxxxxj` → 91, `IX.XX.XVI` → 196) and a converted era (`DCLXXXIII` → 645). The "42 of 48" pass rate measures only that the value appears somewhere in the output. It is not a correctness check.

Coverage. 14 of 48 examples depend on the three unreachable sources (6 Kajanto, 4 Pollard, 4 Chrisomalis). Several engine features have no example at all (`vinculum`, `minim`, `oddOrder`, `additiveSum`).

## 3. Missing conventions, pitfalls and sources

Conventions:
- **Calendar reform and year starts.** The findings mention year-start styles but not the Julian–Gregorian change (1582 in Catholic states; 1752 in Britain) or the Scottish move to 1 January in 1600. Records such as the 1609 Tod inventory or the 1663 Jaj date need the year-start style before "1609" means anything.
- **Overbar as distinction, not only multiplier.** Cappelli's §8 (OCR) says a horizontal line over numerals in inscriptions often separates figures from abbreviation signs (his example is COS XI III), and that the same stroke can be a mere abbreviation mark (XP = Christus). The findings have this point in part; make it the default reading for `vinculum`.
- **Units and money words.** Many examples are sums in pounds, florins or miles. Unit words (li, s, d, libra, florins) are the main source of spurious readings and should be a named rule, not an "ignored" catch-all.
- **Scribal errors within one source.** Prinz's calendar case shows a single scribe can err on the year. Date evidence needs a warning for this.

Sources to add:
- Grotefend, *Taschenbuch der Zeitrechnung des deutschen Mittelalters und der Neuzeit*, for year starts, indictions and regnal conversions. Absent from the list and the standard reference.
- Richards, *Mapping Time* (OUP, 1998), or Reingold and Dershowitz, *Calendrical Calculations*, for Julian–Gregorian conversion checks.
- Tartaglia (1556), as reproduced in Cajori §55, for the alphabetic-numeral table.
- Primary epigraphic databases (EDCS, EDR, EDH) for any inscription entered as an example, so each example points to the stone and not only to a handbook.

## 4. Candidate additions: now or later

**Implement now**
- **Apostrophus signs** (ↀ, ↁ, ↂ, IↃ, CIↃ) with a visible gloss. RIB 2205, Egbert and Cajori support this.
- **Explicit-selector converters.** AUC (already coded; the arithmetic checks out, AUC 874 = 121 CE). Spanish era (683 → 645 CE, and 1280 → 1242 CE, both arithmetically right). Indiction, with a named year-start style (933 → indiction 6, which matches (933 + 3) mod 15).
- **Split ↆ and ↅ** as separate features with separate vectors. Add Perry's 6I, 6II, 6III forms to the late six.
- **Final j as an alternative transcription** (ij, iij), not a value change.

**Wait**
- **Regnal years.** Need a named ruler, a dataset and a start rule. Madalfredus is unresolved.
- **Alphabetic numerals.** The three sources (Cappelli, Du Cange, Tartaglia) disagree on K and possibly others. Single letters in ordinary words would produce false readings. If built at all, opt-in per named tradition.
- **Byzantine Anno Mundi.** The originals use Greek numerals; leave out of a Roman-letter reader.
- **Chronogram variants** (W = 10, all capitals in mixed copy). The findings already say these need their own examples.
- **Consulship, tribunician power, passage reading and mixed notation.** Need datasets or a document model.
- **Omitted millennium.** One unverified León case; keep at 0.

## 5. What a sceptical palaeographer or epigrapher would object to

1. **The unit is wrong.** Practice varies by region, genre and decade. A 0–3 prior per century band averages traditions into a number no scribe worked with.
2. **"Typical" is not counted.** The findings say frequencies need counted corpora (open question 2) and then assign 3 in several cells. The examples are selected to show each convention, so the 42/48 pass rate is circular.
3. **Secondary and old handbooks.** Egbert (1896), Pollard (1905), Cajori (1928), Cappelli (1901 OCR) and Kajanto (1977), reached through Wikisource, Gutenberg and academia uploads, not through editions or plates. Two of 45 references were read in full. A palaeographer will ask for the edition and the plate.
4. **Transcription is not the object.** Many inputs are editorial transcriptions with Unicode substitutes (superscripts, ↀ, Đ, Ↄ). The reader returning 4411 from "IIII CĐXI" is a fact about the edition, not the stone.
5. **Writing date and event date are conflated.** The 1776 tablet on an 1886 monument; the 876 battle recorded in a calendar whose neighbouring entry has the wrong year; the 1456 year glossed by Cappelli. The tool treats them as one thing.
6. **Numerals are not dating systems.** AUC, Spanish era, indiction and regnal years are dating systems. Putting them in the same ranking as numeral grammar is a category error.
7. **Script and hand are how dating is done.** Period priors by century are not how palaeographers date a manuscript. "Period" should not look like date evidence.

**What the write-up must admit**
- The ratings are one model's editorial judgements (GPT-6.2 Sol), not counted frequencies. No palaeographer has reviewed them. Reviews here are by AI models.
- Only 2 of 45 references were read in full. Three sources were unreachable on the day, and 14 examples depend on them.
- The examples are a hand-picked set, not a sample. Zero is not absence.
- Known errors in the current set: the IX.XX.XVI date/value mix, the RIB 2208 date typo, the unsupported "Merovingian" label, and the Prinz scribal year error.
- The engine's minimum-aggregation makes a 0 eliminate a reading; the findings' zeros do not mean what the engine does with them.
- The reader computes possible readings. It does not date documents.
- Some ratings concern features that are not implemented, and the test checks presence of a value, not ranking or convention.

## 6. Uncertainty and disconfirming evidence

- I did not read Kajanto, Chrisomalis or Pollard. Claims resting on them are unverified, not wrong.
- I did not check the Hadrian aureus (Mattingly), the Diocles inscription, the León case, Forcella, Dorn, Dessau or the Barnes clock beyond the list above.
- I could not confirm the CIL I 536 date of 157 BCE from the passage, nor the Cappelli letter table's location.
- My downgrades are to the period-wide prior. Some 3s are defensible within a tradition: raised c and m in some late medieval and early modern accounts, score notation in French records, final j in Scottish and English hands. The findings' definition of 3 allows those. The problem is the label, not the existence of the convention.
- Disconfirming for my overall view: the examples and glosses held up better than the ratings. That is a reason to publish the examples and retract the scores, not to drop the project.

## 7. Recommendation

1. Do not publish the ratings as evidence scores yet. Reduce unsupported 3s to 2 (or lower) using the table in section 1, and remove the combined `archaic` vector.
2. Fix the example semantics: separate document date, numeral value and reader output. Correct IX.XX.XVI, the RIB 2208 date note, the "Merovingian" label and the Prinz scribal error.
3. Check the three unreachable sources (Kajanto, Chrisomalis, Pollard) before the examples that rely on them are shown as "attested".
4. Change the engine so a 0 does not silently remove a displayed reading; use warnings or a floor. Gate AUC and regional features behind an explicit selection.
5. Add the missing sources (Grotefend; Richards or Reingold and Dershowitz; Tartaglia via Cajori; primary databases) and state the Julian–Gregorian and year-start issues in the write-up.
6. Build the "implement now" list in section 4. Hold the "wait" list.
7. For the Research Snack, use the admissions in section 5 as the write-up's limitations section.
