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

GMC pages/PDF sections were read through the web reader after direct requests were blocked. On 22 November the migrated NMC gazette and notices indexes yielded the original 2024 curriculum, 2021 internship regulation, 2023 postgraduate regulation and NExT deferral notice. They were retrieved as PDFs and the relevant sections read. The undergraduate curriculum specifies 4½ academic years followed by internship; CRMI regulation 5 specifies at least twelve months. The legacy 2019 national provisional-registration provision is corroborated by current government-hospital implementation. India no longer has a blanket unavailable-originals label. No later NExT commencement was found in the current rules index and news titles through page 29; future cohort rules remain unpredicted. Current Japanese e-Gov licensing provisions replace reliance on the older English translation for the licence milestone.

# Provenance and clocks

`routes.md` is the canonical editable human coding. `uis-selected-programmes.csv` preserves actual workbook cells and observation years. `school-baselines.csv` is an original selection and harmonisation layer, including England's primary definition, Bavaria's current G9 and Singapore's ISCED4 junior college. World Bank compulsory duration is retained for context only; it never sets the university-entry date. `eu-basic-medical-duration.csv` is an access-date snapshot with unknown source observation dates. Degree and traineeship fields are never summed automatically. `eu-gp-report-table.csv` is a transcription of a report table, not a ready-made individual-level dataset.

## Family-practice endpoint amendment

New short factual citations use the Japanese Medical Specialty Board's general-practice standards PDF linked through its public Box share and its public qualification explanation; FPAB's family-medicine residency and accreditation pages; MOHH's publicly linked July 2027 entry guide; and NMC's scanned permission letter for MD Family Medicine at CMC Vellore. Whole documents and the checking image remain in ignored scratch and are not distributed. Only brief passages, source dates, original coding and hashes are shared. The public NMC letter confirms a regulator-authorised named course; it is not a national census of current course places. The later original-document retrieval supersedes the former India access limitation. The replaced internal-medicine coding remains available in repository history.
