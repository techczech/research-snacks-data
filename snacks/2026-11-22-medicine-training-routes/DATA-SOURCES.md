---
title: Medical routes preview — sources and sharing decisions
date: 2026-11-22
status: author-preview
provenance: Provider pages, public legal texts, structured API responses and original comparative coding
---

# What is shared

Original route coding, a short source-passage register, selected theoretical school-programme facts and a small factual EU duration extract are shared. Full regulator PDFs, scraped HTML, whole workbooks, complete database records and third-party publication copies remain in ignored scratch and are not redistributed. Source wording is not relicensed under this repository's code licence.

| Source | Access and licence boundary | Shared material |
|---|---|---|
| UNESCO UIS ISCED mapping workbooks | Public XLSX links on the [UIS mapping page](https://www.uis.unesco.org/en/methods-and-tools/isced/mapping-and-diagrams). Individual workbook-specific reuse terms not established; the browser's terms cannot automatically license every old workbook. | Selected factual programme ages, durations, ISCED codes, source cell locators and file hashes; no workbook copies. |
| World Bank WDI education structure indicators, sourced from UIS | Public [API](https://api.worldbank.org/v2/); World Bank dataset default [CC BY 4.0 terms](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets) subject to source-specific exceptions. | Twenty-four observations with year and query URL. These are theoretical structures, not realised schooling. |
| EU Regulated Professions Database | Public frontend and JSON service. [Commission legal notice](https://commission.europa.eu/legal-notice_en): EU-owned content normally CC BY 4.0; specific database/member-state and bulk-extraction scope not verified. | Thirty-two selected basic-medical-training factual duration records, including missing values and an archived-UK flag. No complete records, activities or personal data. This limited snapshot is not a relabelled open bulk database. |
| Commission SWD(2026)64 | Public [EUR-Lex document](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026SC0064); Commission legal notice applies to EU-owned report content. | Selected GP-duration table facts, preserving the printed ambiguous code SL and Luxembourg range. Table credits the EC survey and WONCA Europe/UEMO. |
| WHO NHWA | Public indicator PDF; usable medical-duration observations not retrieved. [Portal](https://apps.who.int/nhwaportal/). Exact raw-data licence unresolved; data.who.int terms are platform-specific. | No NHWA observations in the medicine dataset. Source audit only. |
| Regulators, public laws and credential bodies | Public documents; differing copyright regimes. No general permission to redistribute entire documents is assumed. | Original factual coding, citations, dates, precise locations and short excerpts, with reading-depth limits. Each source has at most 25 quoted whitespace-delimited words in the route register. Japanese excerpts are also short in actual character length. |

# Source access limitations

GMC pages/PDF sections were read through the web reader after direct requests were blocked. Several NMC links returned errors; attempts to obtain Gazette and ministry copies also hit certificate failures, which were not bypassed. India therefore remains visibly provisional: relevant indexed regulator passages and government-provider/court corroboration were read, but full originals and the current NExT implementation status require confirmation before publication. An inaccessible document is not described as fully read. The older Japanese English legal translation is paired with a 2025 ministry diagram and current 2026 facility-manager guidance; it is not passed off as a current consolidated translation.

# Provenance and clocks

`routes.md` is the canonical editable human coding. `uis-selected-programmes.csv` preserves actual workbook cells and observation years. `school-baselines.csv` is an original selection and harmonisation layer, including England's primary definition, Bavaria's current G9 and Singapore's ISCED4 junior college. World Bank compulsory duration is retained for context only; it never sets the university-entry date. `eu-basic-medical-duration.csv` is an access-date snapshot with unknown source observation dates. Degree and traineeship fields are never summed automatically. `eu-gp-report-table.csv` is a transcription of a report table, not a ready-made individual-level dataset.
