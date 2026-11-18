---
title: "Only one of 270 jobs from 1950 is obsolete? — method"
date: 2026-11-18
provenance: Published Research Snacks and their archived analysis inputs
---

# Method: occupations

1. Request the 1950 and 2010 samples in `spec-occupations.json`. `analyse.py` selects EMPSTAT 1 for employed counts, weights people by PERWT and sums by OCC1950. It retains codes below 970 and records the leading 2010 codes feeding each old category. Unemployed records are tracked separately in the original aggregation; they are not employed counts.
2. The first judgement is the explicit `GONE` list in `code/interactive.py`: 16 categories judged gone or nearly gone, including elevator operators. This is an agent judgement, not a classification by a labour historian. The remaining zero categories are treated as reclassification artefacts. A zero alone does not demonstrate obsolescence.
3. The `CAUSE` mapping assigns technology or falling demand. The `SHRINK` mapping selects ten surviving categories with large declines. Those selections are judgement inputs; code applies them and computes change as 100 × (later − earlier) / earlier.
4. Request the employed-person samples in `spec-trends.json`. `analyse2.py` sums PERWT by OCC1990 and year. Workforce shares use all employed people in that extract, not only plotted occupations.
5. The `RISE` and `NEW` lists select trends and omit years with no comparable category. They omit computer operators in 2019 and stenographers after 1990. Missing categories are not observed zeros.
6. The film mapping groups keypunch and paper-tape jobs with data-entry keyers; console and computer operators with computer operators; tabulators with statistical clerks; programmers with software developers. Other mappings follow the labelled occupations in the aggregate. This semantic mapping requires reviewing the film; it is not a mechanical title match.

One-percent samples make small categories noisy. The 1950 scheme hides new work and changes meaning across classifications. The wider literature uses a different title-level method. Runtime, human-time and token summaries on the page are historical records and are not regenerated here.
