---
title: Method for canals and nuclear investment comparisons
date: 2026-11-19
provenance: Linked original publications and attributed selected observations
---

# What each output checks

| Output | Page figures checked |
|---|---|
| canal-periods.csv | Expenditure totals, annual means, selected-reference GDP shares and period-average intensity. |
| canal-returns.csv and canal-turnover.csv | Selected published company/period statistics; passing checks their transcription into the presentation, not the archival reconstruction. |
| nuclear-annual.csv | US investor-owned annual construction accounting expenditure/GDP, 1979–1990. |
| nuclear-operations.csv | Selected EIA generation, generation share, capacity and capacity factor facts; NA stays missing. |
| rail-1850s.csv | Selected annual gross Fishlow investment/GDP observations. |
| cumulative.csv | Nominal spending sums divided by one explicitly named reference year's nominal GDP. |
| nuclear-economics.csv | Cancellation/default facts, Columbia revenue/expenses/historic cost, French capital totals and later audited revenue coverage; CBO cost measures. |
| comparison.csv and ai-scenarios.csv | New historical scale observations and the parent's reported AI proxy/scenarios. |
| 1–4 chart CSVs | Exactly the values plotted by the downloadable Vega-Lite specifications. |

# Definitions and judgements

Annual comparison is nominal expenditure divided by same-year nominal GDP. Canal expenditure is only available here for multi-year periods: annual mean = period total / inclusive year count, and its displayed scale divides by the named reference GDP. This does not establish any year's observed expenditure or a mania peak. The alternate period intensity divides total spending by total period GDP, and agrees at the displayed precision. The 1791–1801 interval contains eleven years.

Canals include inland waterways and are the source's quasi-net concept, not modern gross fixed investment. The spending table is a secondary transcription in Arnold/McCartney Table 1 p.218 of Ginarlis/Pollard Table 8.7 pp.213–215. The original source volume was not read in full. BoE A9 H is Great Britain at market prices. Using P after 1801 would add Ireland to the denominator.

The US nuclear window and investor-owned coverage reflect the retrieved EEI source, not all US civil nuclear spending in 1965–1990. Nuclear fuel is a separate row and excluded. Financing capitalised during construction is included in the accounting totals and cannot be allocated out by nuclear project here; this is not pure cash construction or a clean national-accounts resource measure. Public utilities are absent. A peak inside this window cannot be called the national all-time peak. The 1979 source image reads 9,855, whereas search extraction incorrectly returned 9,865.

France 1983 construction is an approximate graph reading, rounded to EUR 3.1bn, divided by four non-seasonally-adjusted Eurostat GDP quarters summed. It is not an annual peak. Its direct-cost scope excludes engineering, pre-operation and interest. The separate nominal total EUR 36,948m covers 1969–2004. It cannot be labelled Messmer 1974–1990 spending. Constant-2010-price overnight cost and interest are kept outside nominal historical GDP ratios.

Fishlow Df865 is current-dollar gross expenditure, including right-of-way and rolling stock. The Cambridge source names Fishlow Tables 53 and 54 pp.397,399. We read the documented XML transcription, not the original book. Failed projects are excluded after 1839. A private complete 1850–1860 search gave the 1854 maximum; the offline package checks that selected observation, not the complete peak search. Only isolated early-US GDP facts are published, respecting MeasuringWorth's five-consecutive-year request.

The five canal companies are selected by surviving major-company archives, not a random sample. Their means have different available company-years. Nominal share capital omits retained capital: dividend rates are not purchase-price yields or total shareholder returns. Our checking package carries attributed published statistics; it cannot redo the archival accounts.

Columbia/WPPSS 2 illustrates a completed survivor. FY2009 operating revenue is compared with mixed-year original nominal construction cost, so the ratio is a turnover illustration with no inflation adjustment. Operating income is before other income/financing; this net-billed project's revenues recover costs rather than establish a commercial investor profit. It does not represent all US reactors or cancelled projects. The primary annual report loaded through web retrieval; later PDF downloads timed out. The relevant p.42 Columbia column was read and transcribed; no quotation or local PDF capture is claimed.

French 2011–2021 accounting-cost coverage comes from the Cour des comptes 2022 synthesis p.17 and uses its revenue allocation assumptions. It is later operating evidence, not the original construction cohort's lifetime economic return.

CBO's reported mean 207% overrun differs from the ratio of its overall mean actual/projected costs (about 3.15 times). Those are different aggregation methods. Its sample excludes cancelled plants and covers construction starts after 1965 completed by 1986.

Window choices, reference GDP years, scope classification, source transcription, approximate graph reading and the interpretation of revenue versus return are explicit judgement steps. The parent comparisons retain their original definitions. AI's 1.6–2.8% scenarios are not bounds on measured domestic AI investment. Civil power is kept separate from military nuclear programmes; no military expenditure is added.

# Rebuild charts

After reproducing tables into an entry's data/ folder, run `uv run python snacks/2026-11-19-canals-nuclear-investment-booms/code/charts-canals-nuclear.py ENTRY_DIRECTORY`. PNG rendering uses inline copies of the same CSV values; the published Vega-Lite reads the CSV URLs with explicit numeric parsing. No purple/pink colours, facet container widths or automatic CSV parsing are used.
