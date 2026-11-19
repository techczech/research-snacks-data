#!/usr/bin/env python3
"""Offline arithmetic checks for AI capex and historical booms.
Run: python3 code/reproduce.py OUTPUT_DIRECTORY
Inputs are selected transcribed facts. This does not independently validate the
transcriptions, prove a complete historical peak search, or audit Exponential View.
"""
import csv
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]

def read(name):
    with (ROOT/'data'/name).open(newline='') as f:return list(csv.DictReader(f))

def write(out,name,rows):
    with (out/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def reproduce(out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    spending=[]
    for r in read('spending-inputs.csv'):
        n,d=float(r['annual_spending_m']),float(r['gdp_m'])
        assert n>0 and d>n
        spending.append({'precedent':r['precedent'],'year':int(r['year']),'peak_spend_pct_gdp':round(n/d*100,4),'status':'Reconstructed historical share','scope':r['scope']})
    # This value is the article's reported proxy, not a reconstructed domestic AI series.
    ai=json.loads((ROOT/'data/ai-revenue-inputs.json').read_text())
    spending.append({'precedent':'Five tech firms, 2026 YTD','year':2026,'peak_spend_pct_gdp':ai['article_2026_ytd_capex_us_gdp_pct'],'status':'Reported global-company proxy','scope':'Global total company capex / US GDP; YTD, not a complete year or domestic AI total'})
    write(out,'1-spending-gdp.csv',spending)
    revenue=[]
    for r in read('revenue-inputs.csv'):
        rev,cap=float(r['annual_revenue_m']),float(r['annual_capex_m'])
        stock=float(r['cumulative_financed_capital_m']) if r['cumulative_financed_capital_m'] else None
        revenue.append({'precedent':r['case'],'year':int(r['year']),'years_since_boom_start':int(r['year'])-int(r['boom_start']),'revenue_m':rev,'annual_capex_m':cap,'revenue_to_annual_capex':round(rev/cap,4),'revenue_to_cumulative_capital_pct':round(rev/stock*100,4) if stock else '', 'scope':r['scope']})
    write(out,'revenue-ratios.csv',revenue)
    # Growth chart: the same series on both sides; no interpolated historical paths.
    growth=[]
    for case in ['UK railways','US telecom']:
        rr=[r for r in revenue if r['precedent']==case];base=rr[0]
        for r in rr:
            for metric,field in [('Gross revenue' if case=='UK railways' else 'End-user revenue','revenue_m'),('Annual capex','annual_capex_m')]:
                growth.append({'precedent':case,'year':r['year'],'years_from_first_observation':r['year']-base['year'],'series':metric,'index_first_observation_100':round(r[field]/base[field]*100,3),'first_observation_year':base['year']})
    write(out,'2-revenue-and-capex.csv',growth)
    # Exponential View's AI-specific Q3 estimate annualised, not its depreciation/cost hurdle.
    annual_ai_capex=ai['q3_2026_estimated_ai_capex_usd_bn']*4
    annual_broad_capex=ai['article_q3_2026_five_company_capex_usd_bn']*4
    diagnostics=[]
    for measure,key in [('October revenue run rate','october_2026_run_rate_usd_bn'),('Trailing twelve-month revenue','ttm_to_october_2026_revenue_usd_bn')]:
        for denom,label in [(annual_ai_capex,'Estimated AI cloud capex, Q3 x 4'),(annual_broad_capex,'All capex of five firms, Q3 x 4')]:
            diagnostics.append({'revenue_measure':measure,'revenue_usd_bn':ai[key],'capex_measure':label,'annualised_capex_usd_bn':denom,'ratio':round(ai[key]/denom,4),'limitation':'Different periods and coverage; diagnostic only, not a matched return or margin'})
    write(out,'ai-diagnostics.csv',diagnostics)
    metrics=[{'metric':'October implied monthly revenue, USD bn','value':round(ai['october_2026_run_rate_usd_bn']/12,6)},
             {'metric':'Run rate divided by TTM revenue','value':round(ai['october_2026_run_rate_usd_bn']/ai['ttm_to_october_2026_revenue_usd_bn'],6)},
             {'metric':'Run-rate revenue growth YoY, percent','value':round((ai['run_rate_yoy_multiple']-1)*100,4)},
             {'metric':'Estimated AI Q3 capex growth YoY, percent','value':round((ai['q3_2026_estimated_ai_capex_usd_bn']/ai['q3_2025_estimated_ai_capex_usd_bn']-1)*100,4)},
             {'metric':'Anthropic Q3 revenue / compute and infrastructure cost','value':round(ai['anthropic_q3_2026_revenue_usd_bn']/ai['anthropic_q3_2026_compute_infrastructure_cost_usd_bn'],6)}]
    write(out,'ai-metrics.csv',metrics)
    # A rough third elapsed year, retaining both mature-base and cohort mismatches.
    stages=[r for r in revenue if r['years_since_boom_start']==3]
    stage=[{'precedent':r['precedent'],'year':r['year'],'chosen_start':r['year']-3,'elapsed_years':3,'revenue_to_annual_capex':r['revenue_to_annual_capex'],'qualification':r['scope']} for r in stages]
    for d in diagnostics[:]:
        if d['annualised_capex_usd_bn']==annual_ai_capex:
            stage.append({'precedent':'AI: '+d['revenue_measure'],'year':2026,'chosen_start':2023,'elapsed_years':3,'revenue_to_annual_capex':d['ratio'],'qualification':d['limitation']})
    write(out,'stage-three-comparison.csv',stage)
    sensitivity=[{'series':r['series'],'spend_gdp_pct':round(float(r['annual_capex_gbp_m'])/float(r['gdp_gbp_m'])*100,4)} for r in read('uk-gdp-inputs.csv')]
    write(out,'uk-gdp-sensitivity.csv',sensitivity)
    assert 6<float(spending[0]['peak_spend_pct_gdp'])<7
    assert ai['october_2026_run_rate_usd_bn']>ai['ttm_to_october_2026_revenue_usd_bn']
    # Independent source sanity checks: annual cash is not a financed stock;
    # NASA's entire agency budget is not Apollo's programme budget.
    assert next(r for r in revenue if r['precedent']=='UK railways' and r['year']==1847)['revenue_to_annual_capex']==0.1913
    assert next(r for r in spending if r['precedent']=='Apollo including overhead')['peak_spend_pct_gdp']<0.5
    print(f'Rebuilt 7 tables from transcribed inputs in {out.name}')

if __name__=='__main__':reproduce(sys.argv[1])
