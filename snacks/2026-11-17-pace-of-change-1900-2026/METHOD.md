---
title: "Did work change faster before 1970? — method"
date: 2026-11-18
provenance: Published Research Snacks and their archived analysis inputs
---

# Method: pace of change

The main IPUMS sample specifications, filters, category groups and formulae are preserved in `code/analyse.py`. People aged at least 16 in LABFORCE 2 supply the labour-force measures. Occupation shares use coded OCC1950 values below 980; industry shares use IND1950 100–946. These are labour-force distributions, not the employed-only population in the jobs snack.

Dissimilarity is 50 × the sum of absolute differences between two share distributions on a 0–1 scale. The same calculation uses detailed occupations, industries, eleven occupation groups and three sectors. `distribution-shares.csv` preserves full precision; rounded chart percentages can change the last reported decimal. No rounding tolerance is used to excuse a failed final-table diff.

`indicator-counts.csv` stores weighted numerators and denominators. The labels in `code/reproduce.py` specify their ratios. Education uses ages 25+ with valid nonzero EDUC, and EDUC at least 10 in the numerator. `college-counts.csv` preserves those counts. Robustness uses ages 16+ and the extract's labour-force restriction, with OCC1990 codes 3–890 and OCC2010 codes 10–9830. `robustness-counts.csv` supports the exact same D calculation.

Judgement steps are choosing endpoint proxies; choosing classification schemes; grouping occupations/sectors; assigning technological explanations; selecting historical events; and classifying newly written titles as new work or wording changes. The title extraction normalises punctuation/case, requires at least fifteen 1940 sample records and excludes any title written in the 1900 or 1910 samples. The candidate table is not proof of a new occupation. `written_titles_judgement.csv` records the original semantic labels for a selected subset.

The two lists of 25 Ngram phrases were selected before lookup. Their membership is preserved in `ngram_takeoff.csv` and `code/ngrams.py`. The optional fetch uses English, 1880–2022, case-insensitive, no smoothing. Take-off is the first year at or above 10% of the full-series maximum; a tie at the peak uses its first year. Seven scanning-noise terms are excluded from the chart explicitly in `code/charts.py`. The raw-precision response was refreshed on 18 November and reproduced all original take-off/peak rows exactly; this is a verification refresh, not evidence of the original response bytes.

Caveats include unequal time spans, classification drift, missing modern household-service codes, school-question changes and the use of printed language as an illustration rather than an employment measure. The chart excludes school values for 1950/1970 and household work from 2000. The event annotations are context, not causal estimates. Historical timing/token records are outside the rerun.
