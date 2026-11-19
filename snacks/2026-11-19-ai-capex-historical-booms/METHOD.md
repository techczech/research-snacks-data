---
title: AI spending and historical booms — method
date: 2026-11-19
provenance: AI capex historical-booms source captures and checked calculations
---

# Method

Annual nominal spending divided by same-country, same-year nominal GDP is the target scale comparison. Programme obligations/outlays, private capex, land and geographical coverage are stated in the inputs and on the page. A fiscal series uses OMB fiscal GDP; a calendar series uses BEA GDPA. UK GDP is the historical UK including Ireland at market prices. The older factor-cost GDP is a separate sensitivity.

## What each output checks

| Output | Page figures and source locators |
|---|---|
| `1-spending-gdp.csv` | Main table/chart: 6.48%, 5.53%, 3.78%, 1.15%, 0.83%, 0.48%, 0.44%, 0.42%; the 2.3% AI row is an explicitly reported proxy. Odlyzko Tables 1–2 pp.32–34; BoE A9 P165; Ulmer C-10 p.272 and D-1 pp.320–321; MeasuringWorth selected years; USTelecom chart 1 p.2; Planetary Society original-dollar Apollo worksheet; FHWA FA-203; Hewlett/Anderson p.724; BEA GDPA and OMB 10.1. |
| `revenue-ratios.csv` | Annual receipts/annual capex and separately annual receipts/accumulated financed capital. UK: Odlyzko pp.32,34. US: Poor through Statistical Abstract 1888 Table98 p.184, plus Ulmer C-10. Telecom: FCC Table1.1 p.1-13, USTelecom chart1 p.2. |
| `2-revenue-and-capex.csv` | Chart indices: UK 1844=100; US telecom 1997=100. Both revenue and capital spending, all seven annual observations in each case. |
| `ai-diagnostics.csv` | 345/704, 188/704, 345/920, 188/920; capex denominators are Q3 estimates multiplied by four. These periods/cohorts are not matched. |
| `ai-metrics.csv` | 345/12=28.75; run rate/TTM=1.835; revenue growth 320%; AI Q3 capex growth 122.78%; Anthropic 17/9.9=1.717 (revenue/compute-and-infrastructure expense, not capex or profit). |
| `stage-three-comparison.csv` | Third elapsed year after judgement-selected starts: UK1844→1847, US1879→1882, telecom1996→1999, AI2023→2026. Existing mature businesses remain included; AI is only a diagnostic. |
| `uk-gdp-sensitivity.csv` | 43.9 / 677.973×100 =6.475%; 43.9/604×100 =7.268%. Market-price historical UK versus older factor-cost GDP. |

## Judgements and exclusions

Boom windows: UK1844–1850; US1870–1889 and subwindow1880–1889; telecom1996–2013; private electricity1929–1950; ApolloFY1960–1973; federal interstatesFY1956–1976; Manhattan1942–1946. Peak means the greatest share of GDP in that window, not greatest nominal spending. Public inputs retain selected peak candidates. Full annual-source searching was performed in the analysis, and is not independently validated by this offline check. In particular, MeasuringWorth asks permission for publishing more than five consecutive GDP observations; the public inputs contain only the isolated early-US GDP facts used in the displayed calculations. A reader can retrieve the linked complete series for a new peak search.

Ulmer's annual railway estimates before 1912 depend on reconstruction and interpolation; they are not precise contemporary accounts. Its including-land cash series is used, not moving averages or the all-regulated-industries total. Poor's financed cost is a book-liability proxy; explicit divisions can differ from Poor's own differently based published percentage. Its traffic reporting covers returning lines; the capex/revenue cohorts do not align exactly.

Telecom's revenue excludes carrier-to-carrier pass-through, but omits some revenue covered by the broader capex population. Fibre-only receipts/capex were not established. The US 1850s railway national peak, British1790s canal annual national share and stage-matched receipts, and civil nuclear programme revenue/capex remain missing, not zero.

AI inputs are Exponential View's published estimates and the article's broad-company proxy. The Oct26 capex estimate preceded some Q3 earnings. Company disclosures support substantial sales but do not reconstruct the deduplicated aggregate. Its in-service depreciation/operating-cost/required-return model has a different denominator from current cash capex. Do not sum lab sales and the same money paid to hosting providers. No model of eventual profits or bubble probability is fitted.
