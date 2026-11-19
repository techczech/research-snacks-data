---
title: Revolution speed methods and judgement steps
date: 2026-11-19
provenance: Exploratory analysis fixed before the era medians were calculated
---

# Method

## Reconstruction target

Rebuild the numerical claims on the linked snack from saved input facts and the official preliminary NAVCO 1.3 campaign list. This is an exploratory descriptive comparison. The source search and initial NAVCO counts preceded the written protocol; it was not preregistered.

## Judgement steps

1. **Select the comparison roster.** Sixteen well-known exit episodes from the periods named in the brief; a convenience sample, not every revolution or a random sample. France represents one 1848 episode. The three measured 1989 episodes are accompanied by decisions for Poland, Hungary and Bulgaria. Ukraine's Orange Revolution remains an electoral-outcome boundary. Other colour revolutions were not comprehensively surveyed.
2. **Select the onset.** Use the cited chronology's named beginning of the final sustained mobilisation episode. Local events that spread are eligible. No common crowd-size threshold is imposed retrospectively. This clock omits earlier organising and opposition. The final episode can differ substantially from NAVCO's campaign boundary.
3. **Select the endpoint.** Resignation, abdication or loss of power of the named incumbent. Libya uses loss of the capital as an explicit proxy; Iran uses the Shah's departure; East Germany uses removal as party leader; Czechoslovakia uses Husák's presidential resignation to preserve the original claim. Their meanings differ. Sri Lanka uses the legal effective date in Parliament's record; Bangladesh uses de facto flight, without adjudicating a contested resignation document. Yemen uses successor inauguration, with agreement and handover as alternatives.
4. **Classify exclusions.** Exclude France, Russia, Romania, Libya and Yemen in one armed/war/mutiny sensitivity; additionally exclude Philippines and Sudan for military split/coup. These are authorial classifications, not a completed Powell–Thyne match. Egypt and East Germany still have military/elite mechanisms. No exclusion makes the cases causally comparable.
5. **Choose technology periods.** Before 1990, 1990–2009, 2010–24; also pool the last two for a two-era comparison. They are calendar proxies, not observed adoption or internet penetration.
6. **Respect provider fields.** NAVCO `NONVIOL=1`; no row deduplication, because some IDs are reused for different campaign entries. `EYEAR` is peak year, not leader exit. `SUCCESS=1` means full achievement within one year of peak activity, attributable directly to the campaign. `ONGOING=1` means unfinished as of 31 December 2019 and is also coded failure by the provider. Never relabel an unfinished case a known eventual failure.
7. **Choose denominators and cohorts.** Report success divided by all campaigns and by resolved campaigns. Both are selected at a common administrative cutoff with unequal observation periods; neither is an equal-follow-up or survival estimate. Repeat by onset decade, restrict to regime change, and separate onset cohorts 2010–14 and 2015–19. Independence/secession goals remain in the main maximalist calculation.

## Tables and page claims

| Expected output | Page numbers or statements checked |
|---|---|
| original-comparison.csv | Czech 23/24 and Egyptian 17/18 days; six-day difference asserted independently in code. |
| 1-selected-clocks.csv | All sixteen date intervals and plotted records; 2–394 days. |
| alternative-clocks.csv | Fourteen alternative endpoints/onsets; includes Czech 7, 12 and 42 days. |
| era-sensitivity.csv | Main medians 7 versus 35; exclusions 33.5 versus 28; further exclusions 44 versus 24; three-era n and medians. |
| leave-one-out.csv | Sensitivity to omitting each individual selected case; retained for inspection, not a population inference. |
| rank-diagnostic.csv | Descriptive year/duration rank correlation; not a causal result or population significance test. |
| navco-all-denominators.csv | Peak/onset decades and all-goals/regime-change comparisons. |
| 2-success-denominators.csv | 1970s–2010s chart; 2010s 34/101=33.7% and 34/73=46.6%; 1990s 36/55=65.5%. |
| navco-exposure-sensitivity.csv | 2010–14 onset cohort: 18/45=40.0%, six ongoing; resolved 18/39=46.2%. |
| navco-boundary-examples.csv | Provider's 2007 Egyptian campaign onset; 1989 Velvet Revolution; limited East German and Orange outcomes. |
| egypt-survey-facts.csv | 1,050 valid surveys and the four published first-information percentages; passthrough facts, not respondent-data reanalysis. |

## Calculation and verification limits

Gregorian date subtraction; Russia's 23 February/2 March Old Style correspond to 8/15 March New Style. Inclusive days add one to both intervals. Medians use all selected intervals with the documented exclusions. The Spearman diagnostic ranks ties by their average rank. No causal regression, population p-value, internet-penetration join, Archigos merge or Mass Mobilization Project event analysis is claimed. Archigos 4.1 coverage stops in 2015. NAVCO's preliminary file has 622 campaigns and 320 nonviolent campaigns, differing from the 628/325 totals in the cited 2020 article.

Rebuilding saved source facts cannot validate an onset choice. Complete raw sources and private timing records are not shipped. Provider links and locators support a separate source audit. Survey observations come from a convenience/snowball sample whose representativeness is unknown. Success rates describe this dataset's 2019 status, not current outcomes.
