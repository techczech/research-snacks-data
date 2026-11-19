---
title: AI spending and historical booms — revised method
date: 2026-11-19
provenance: Coordinator-selected Astra and Fable reviews; attributed public source facts
---

# Method

This revision distinguishes three questions: reproducing the article's 2.3%; measuring domestic AI capex; and testing twentieth-century US precedents. The first rounds correctly under the disclosed reporting-period convention. The second is not identified by company totals. The third has a close case in 1910, not a demonstrated maximum across the century.

## Outputs and page figures

| Output | What it checks |
|---|---|
| company-reconciliation.csv | Five named companies, cash PPE, reporting/calendar alignment; 560.350bn reported and 563.638bn calendar-estimated nine-month cash. Company/period/source/statement locators in company-cash-inputs.csv. |
| ai-spending-shares.csv | 2.2994%, 2.3129%, conditional 70% allocation 1.6096%, latest-quarter pace 2.7927%, EV estimated AI cloud pace 2.1327%. GDP2026 Q1-Q3: BEA A191RC via FRED, 29 October 2026 vintage. |
| 1-spending-gdp.csv | Main historical table/chart; 1910 rail740/33746=2.1929%; 1924 private electricity791.6/87786=0.9017%; other peaks unchanged. Numerator and denominator links in spending-inputs.csv. |
| historical-checks.csv | Railway land exclusions; 1949 electricity0.7618%; NASA FY1964 obligations0.7352%, separately from Apollo programme0.4795%. Input source table/cell locators included. |
| company-annual-cash.csv | 2024,2025 and first nine reported months2026 actual company purchases; Microsoft's calendar-year bridge; Oracle's Dec-Nov years and Dec-Aug nine months. Prior inputs carry individual filing locators. |
| cumulative-spending.csv | Sum of nominal gross spending / one stated reference year's GDP: UK23.3048%, US18.9911% and12.0568%, broad global firms3.6685%. Not summed annual shares; unequal durations and price changes retained. |
| revenue-ratios.csv | Historical gross revenue / financed-capital stock. Revenue and capex have separate source/locator fields. No third-year ranking or AI TTM/current-quarter ratio remains. |
| 2-revenue-and-capex.csv, growth-comparison.csv | Actual-year growth paths. UK1844 onward, US1880 onward, telecom1997 onward; independently indexed revenue/capex. AI October run-rate growth4.2x versus Q3 estimated capex176/79; adjacent timing, changing cohort, not a matched return. Common logarithmic chart scale. |
| telecom-segments.csv, 3-telecom-segments.csv | FCC Table1.1 end-user toll,wireless,local,total,2000-2003. Toll -32.7959%, wireless49.9446%, total0.6817% (CSV authoritative). No segment capex matched to these receipts. |
| capital-in-service.csv | Historical gross receipts/financed capital; EV November2 infrastructure255/563=45.2931%; all-stack345/563=61.2789%; infrastructure255/915 including CIP=27.8689%. No net-return interpretation. |
| ai-capital-cost.csv | Reported capital563,including CIP915; annual80depreciation+16OpEx+84return=180; infrastructure coverage1.416667,all-stack1.916667; commitments475/703 annual costs and source-reported growth conditions22/36%. |
| ai-sensitivity.csv | Hypothetical100bn equipment,60bn revenue at full use/base price. Straight-line depreciation,15% return on original capital. Cash operating surplus=revenue*utilisation*price*cash margin; coverage=surplus/(equipment/life+required return). Margin is before depreciation. One variable changes per row; no fleet estimate, buildings,land,tax or separate finance costs. |
| anthropic-q3.csv | Fact sheet printed pp.13-15:16.956bn sales,9.863compute,-.567GAAP result,2.463adjusted;1.070SBC+1.960noncash charity reconcile. Margins-3.3439%/14.5258%. Single-company illustration. |
| ai-metrics.csv, uk-gdp-sensitivity.csv | Published revenue/run-rate endpoints and growth; UK1847 market-price6.4752% versus older factor-cost7.2682%. |

## Periods and accounting

For nine-month nominal GDP, add Q1,Q2,Q3 seasonally adjusted annual rates and divide by four. The Q3 pace instead divides four times quarterly cash by Q3 annual-rate GDP. Do not divide nine months' cash by one annual-rate observation.

Microsoft January-September2026 cash = FY2026 115948 - six months ended December2025 49270 + quarter ended September2026 39367 (USD million). Calendar2024/2025 use the analogous annual-minus-prior-half-plus-current-half bridge.

Oracle's quarters end February,May,August,November. The available Dec-Aug flow is18635+16493+28499. The calendar estimate takes2/3 ofDec-Feb,allMar-May/allJun-Aug,and aSeptember atJun-Aug's monthly pace. September is not disclosed; this is an explicitly assumed alignment, not exact calendar observation. Earlier annual totals keep Oracle's reportedDec-Nov windows, disclosed rather than disguised as calendar years. Oracle2025 rolling total =FY2025 21215 -H1FY2025 6273 +Q1FY2026 8502 +Q2FY2026 12033.

All firms use cash PPE purchases. Exclude new finance-lease assets and financing principal; do not mix Microsoft's lease-inclusive headline or Meta's purchases-plus-principal with this series. Amazon is gross before sales/incentives; Oracle is before customer-financing offsets. Cash does not equal national-account fixed investment; all firms include non-AI and overseas activity.

## Historical peak reconstruction and rights

Peak selection windows: UK1844-1850; US1870-1889,1880-1889,1900-1914; electricity1900-1950; telecom1996-2013; ApolloFY1960-1973; federal interstatesFY1956-1976; Manhattan1942-1946. Peak means share, not greatest currency total. The1910rail sample and electricity extension were added after reviews identified them; they are exploratory additions. Ulmer C-10 pp.272-273 includes land; D-1 pp.320-321 excludes land and public utilities.1871is extrapolated from1873sample; excluding land gives5.4187% rather than5.5348%.

The public offline check validates selected facts and arithmetic, not full peak selection. To repeat the private search: obtain MeasuringWorth nominal GDP1900-1928 through itsNOMINALGDP query; transcribe UlmerC-10 columns1/3 for1900-1914 and D-1 column3 for1900-1928; join laterBEA calendar GDP; divide cash byGDP and select the maximum within the stated window.1924wins the electricity1900-1950search. Keep the full GDP extract private: the provider asks permission above five consecutive observations. Selected public GDP facts are non-consecutive. UKBoE A9 P165 gives1847historical-UKGDP,includingIreland.

BEA detailed investment was redownloaded from the actual linked detailnonres_inv1.xlsx workbook and validated as OOXML. Earlier spreadsheet-named responses were HTML. This repair is not a completed standardTable2.7 or all-public/private full-century comparison.

Investor outcomes are sourced narrative, not numeric return estimates: Odlyzko railway share chart/analysis; Commercial and Financial Chronicle1894 retrospective and receiverships; Couper/Hejkal/Wolman telecom bankruptcies. Fable's memory-only receivership share,Poor1871receipts and shale totals are excluded. Canal,nuclear and1850srail named-source leads remain unresolved. The cost model's internal company estimates and eliminations remain unaudited.
