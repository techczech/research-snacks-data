---
title: Medicine route comparison — method and reproduction
date: 2026-11-22
status: preview
provenance: Original comparative coding and arithmetic, checked against cited primary documents
---

# What is compared

Six selected domestic, continuous, full-time routes: California's conventional four-year college plus four-year MD route; England's standard five-year medical course; Bavaria's standard medical course; Japan; India; and Singapore's NTU five-year course. These are selected pathways, not country averages or an exhaustive list of legal minima. Bavaria supplies one explicit continental jurisdiction and a current state-specific GP training rule.

# Judgement steps

1. Read each regulator's qualification and licensing conditions; code academic, clinical, examination and registration stages in integer months. `routes.md` is the editable source; `data/route-coding.json` is its machine-readable snapshot used by the portable checker.
2. Distinguish the first registration allowing any medical work, the general licence/full registration and a named family-practice training or qualification endpoint. Shared marker categories do not imply equal legal rights. Dates are conditional eligibility positions, not observed issue dates. Successful examinations and applications are assumed; administrative delay is unestimated.
3. Keep overlapping requirements embedded: Germany's practical year is in its 6.25-year standard course; England's licensing assessment is in its degree; California's first residency year counts towards its three-year family-medicine residency. Japan's facility-manager experience lane can overlap later training and is not added to it.
4. Match later bars to family/general practice: ABFM residency, English GP specialty training, Bavarian Allgemeinmedizin, Japanese 総合診療, optional Indian MD Family Medicine and Singapore family-medicine residency. Qualification, accreditation and practice permissions retain local conditions. Training completion is not automatically credential award.
5. Select theoretical school structures from the UIS workbook cells and World Bank observations. The selected Bavaria G9 and Singapore junior-college additions require explicit national interpretation. Primary-entry and age-18 clocks are shifts of the same training route, never new duration sums. Structures from different reference years are not an observed cohort.
6. Retain the EU snapshot's missing units, missing durations and archived UK. Count only 26 non-archived year-valued education records. Never sum education and traineeship fields without knowing overlap. The 27-entry European GP table is a report transcription, separate from the structured database.

# What the outputs check

`uv run check.py 2026-11-22-medicine-training-routes` recalculates three expected CSVs using only Python's standard library. `milestones.csv` checks every number in the six-row page table; `eu-duration-distribution.csv` checks the three plotted EU counts; `stages.csv` checks every stage, school-clock transformation and joined provenance field. These are deterministic checks on authored inputs. The separate independent source review tests the first-registration interpretation against original rules; no test proves clinical competence.

# Updating the sources

The optional online retrieval scripts use additional dependencies in `requirements.txt` and save complete source bodies in ignored `scratch/`. `refresh_india_sources.py` downloads six migrated NMC originals and records hashes. Do not redistribute those third-party bodies. `extract_context.py` refreshes UIS/WDI/EU extracts; inspect changes to definitions and units before accepting any new expected table. `update_family_routes.py` and `amend_verified_sources.py` record historical amendments and are not part of the ordinary reproduction check.

# Scope limits

No estimates of typical completion, repeats, competitive admission gaps, part-time training, service obligations or processing times are supplied. No competence outcomes or causal effect of duration is estimated. India's NExT deferral is verified from the original notice and still linked by the current rules index; no later commencement was found in the bounded notice search. This does not predict rules for future cohorts. Full texts were retrieved where possible; source reading-depth fields name partial reading and access limits.
