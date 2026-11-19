#!/usr/bin/env python3
"""Offline arithmetic from attributed facts. Run: python code/reproduce.py OUTPUT.
Checks arithmetic and scenario definitions, not source transcription or AI model inputs.
"""
import csv,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(n):return list(csv.DictReader((ROOT/'data'/n).open()))
def write(out,n,rows):
 with (out/n).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def reproduce(out):
 out=Path(out);out.mkdir(parents=True,exist_ok=True);ai=json.loads((ROOT/'data/ai-revenue-inputs.json').read_text())
 facts={(r['company'],r['period']):float(r['cash_ppe_m'])/1000 for r in read('company-cash-inputs.csv')}
 f=lambda c,p:facts[c,p]
 companies=[]
 for c in ['Microsoft','Meta','Amazon','Alphabet','Oracle']:
  if c=='Microsoft':ytd=f(c,'FY2026')-f(c,'FY2026-H1')+f(c,'FY2027-Q1');q3=f(c,'FY2027-Q1');cal=ytd;period='Jan-Sept; FY2026 minus Jul-Dec2025 plus FY2027Q1'
  elif c=='Oracle':ytd=sum(f(c,p) for p in ['FY2026-Q3','FY2026-Q4','FY2027-Q1']);q3=f(c,'FY2027-Q1');cal=2/3*f(c,'FY2026-Q3')+f(c,'FY2026-Q4')+4/3*q3;period='Reported Dec-Aug; calendar estimate prorates Dec-Feb, carries Jun-Aug monthly pace into Sept'
  else:ytd=f(c,'CY2026-9M');q3=f(c,'CY2026-Q3');cal=ytd;period='Jan-Sept and Jul-Sept calendar cash-flow periods'
  companies.append(dict(company=c,reported_nine_month_cash_bn=round(ytd,6),calendar_estimate_nine_month_bn=round(cal,6),latest_quarter_cash_bn=q3,alignment=period))
 write(out,'company-reconciliation.csv',companies)
 gdp=read('gdp-2026-inputs.csv');g9=sum(float(r['nominal_gdp_saar_bn']) for r in gdp)/4;gq=float(gdp[-1]['nominal_gdp_saar_bn'])
 total=sum(r['reported_nine_month_cash_bn'] for r in companies);calendar=sum(r['calendar_estimate_nine_month_bn'] for r in companies);quarter=sum(r['latest_quarter_cash_bn'] for r in companies)
 scenarios=[('Nine-month cash, Oracle latest reported periods',total,g9,'Reported fiscal-quarter mapping; Oracle one month early'),('Nine-month cash, calendar estimate',calendar,g9,'Oracle uniform monthly proration and Sept carry-forward assumption'),('70% US allocation of reported cash',total*ai['us_allocation_assumption'],g9,'Scenario, not measured domestic AI capex; includes non-AI spending'),('Latest-quarter cash annualised',quarter*4,gq,'Pace, not a forecast; Oracle Jun-Aug against other firms Jul-Sept'),('EV Q3 AI cloud estimate annualised',ai['q3_2026_estimated_ai_capex_usd_bn']*4,gq,'Different estimated cohort; not measured US-only AI capex')]
 shares=[dict(measure=n,spending_bn=round(v,6),gdp_bn=round(d,6),pct_gdp=round(v/d*100,4),qualification=q) for n,v,d,q in scenarios];write(out,'ai-spending-shares.csv',shares)
 spending=[]
 spend_inputs=read('spending-inputs.csv')
 assert len({r['case'] for r in spend_inputs})==len(spend_inputs), 'duplicate spending case'
 for r in spend_inputs:
  pct=float(r['annual_spending_m'])/float(r['gdp_m'])*100
  spending.append(dict(precedent=r['precedent'],year=int(r['year']),peak_spend_pct_gdp=round(pct,4),status='Public programme' if r['case'] in ['apollo','interstate','manhattan'] else 'Historical private industry',scope=r['scope'],label=r['precedent']+' ('+str(r['year'])+')'))
 for label,pct,status,scope in [('AI: reported proxy',ai['article_2026_ytd_capex_us_gdp_pct'],'Article proxy','Global total company capex / US GDP; nine months'),('AI: 70% allocation scenario',shares[2]['pct_gdp'],'AI scenario',shares[2]['qualification']),('AI: Q3 cash pace',shares[3]['pct_gdp'],'AI scenario',shares[3]['qualification'])]:
  spending.append(dict(precedent=label,year=2026,peak_spend_pct_gdp=pct,status=status,scope=scope,label=label+' (2026)'))
 write(out,'1-spending-gdp.csv',spending)
 # Restriction: no full early-US GDP table in public outputs. Private search imports remain private.
 write(out,'historical-checks.csv',[dict(measure=r['measure'],numerator_m=float(r['numerator_m']),denominator_m=float(r['denominator_m']),result_pct=round(float(r['numerator_m'])/float(r['denominator_m'])*100,4)) for r in read('historical-sensitivity-inputs.csv')])
 revenue=[]
 for r in read('revenue-inputs.csv'):
  rev,cap=float(r['annual_revenue_m']),float(r['annual_capex_m']);stock=float(r['cumulative_financed_capital_m']) if r['cumulative_financed_capital_m'] else None
  revenue.append(dict(precedent=r['case'],year=int(r['year']),revenue_m=rev,annual_capex_m=cap,capital_m=stock or '',revenue_capital_pct=round(rev/stock*100,4) if stock else '',scope=r['scope']))
 write(out,'revenue-ratios.csv',revenue)
 growth=[]
 for case in ['UK railways','US railways','US telecom']:
  rr=[r for r in revenue if r['precedent']==case];base=rr[0]
  for r in rr:
   for series,key in [('Revenue','revenue_m'),('Capex','annual_capex_m')]:
    growth.append(dict(precedent=case,period=str(r['year']),year=r['year'],series=series,index_first_observation_100=round(r[key]/base[key]*100,3),basis='Annual observations; each series independently starts at 100'))
 for y,mult,cap in [(2025,1,ai['q3_2025_estimated_ai_capex_usd_bn']),(2026,ai['run_rate_yoy_multiple'],ai['q3_2026_estimated_ai_capex_usd_bn'])]:
  for series,index in [('Revenue',mult*100),('Capex',cap/ai['q3_2025_estimated_ai_capex_usd_bn']*100)]:
   growth.append(dict(precedent='AI: estimates',period=str(y),year=y,series=series,index_first_observation_100=round(index,3),basis='October revenue run rate; Q3 AI capex estimate; adjacent periods and changing cohort'))
 write(out,'2-revenue-and-capex.csv',growth)
 segments=[];ss=read('telecom-segments-inputs.csv');base=next(r for r in ss if r['year']=='2000')
 for r in ss:
  if int(r['year'])<2000:continue
  for n,k in [('Long-distance / toll','toll_m'),('Wireless','wireless_m'),('Local','local_m'),('Total end-user','total_m')]:
   segments.append(dict(year=int(r['year']),series=n,revenue_bn=float(r[k])/1000,index_2000_100=round(float(r[k])/float(base[k])*100,4),change_from_2000_pct=round((float(r[k])/float(base[k])-1)*100,4)))
 write(out,'telecom-segments.csv',segments)
 write(out,'3-telecom-segments.csv',segments)
 prior={(r['company'],int(r['year'])):float(r['cash_ppe_m']) for r in read('company-prior-inputs.csv')};p=lambda c,y:prior[c,y]
 yearly=[]
 for year in [2024,2025]:
  ms=p('Microsoft FY2024',2024)-p('Microsoft H1FY2024',2024)+p('Microsoft H1FY2025',2024) if year==2024 else p('Microsoft FY2025',2025)-p('Microsoft H1FY2025',2024)+p('Microsoft H1FY2026',2025)
  oc=p('Oracle TTM Nov2024',2024) if year==2024 else p('Oracle FY2025',2025)-p('Oracle H1FY2025',2025)+p('Oracle Q1FY2026',2025)+p('Oracle Q2FY2026',2025)
  yearly.append(dict(year=year,cash_capex_bn=round((sum(p(c,year) for c in ['Alphabet','Amazon','Meta'])+ms+oc)/1000,6),scope='Calendar year for four firms; Oracle Dec-Nov'))
 yearly.append(dict(year=2026,cash_capex_bn=round(total,6),scope='Jan-Sept for four firms; Oracle Dec-Aug; actual spending, not annualised'))
 write(out,'company-annual-cash.csv',yearly)
 cum=[dict(case=r['case'],cumulative_spend_m=float(r['spending_m']),reference_gdp_m=float(r['gdp_m']),reference_year=r['reference_year'],pct_one_year_gdp=round(float(r['spending_m'])/float(r['gdp_m'])*100,4),scope='Gross nominal spending; peak-share reference year; unequal boom durations') for r in read('cumulative-inputs.csv')]
 cum.append(dict(case='Five firms 2024-Sept2026',cumulative_spend_m=round(sum(r['cash_capex_bn'] for r in yearly)*1000,3),reference_gdp_m=gq*1000,reference_year='2026Q3 SAAR',pct_one_year_gdp=round(sum(r['cash_capex_bn'] for r in yearly)/gq*100,4),scope='Worldwide total company cash purchases; Oracle one month early; not domestic AI-only'))
 write(out,'cumulative-spending.csv',cum)
 capital=[dict(case='UK railways 1847',annual_revenue=8.4,capital=167.3,unit='GBP million',revenue_capital_pct=round(8.4/167.3*100,4),basis='Financed capital; gross receipts, no operating costs'),dict(case='US railways 1882',annual_revenue=770.210,capital=7016.750,unit='USD million',revenue_capital_pct=round(770.210/7016.750*100,4),basis='Poor book-finance proxy; gross traffic receipts')]
 for n,rev,stock in [('AI infrastructure / in service',ai['infrastructure_revenue_bn'],ai['capital_in_service_bn']),('AI all stack / in service',ai['october_2026_run_rate_usd_bn'],ai['capital_in_service_bn']),('AI infrastructure / including CIP',ai['infrastructure_revenue_bn'],ai['capital_including_cip_bn'])]:capital.append(dict(case=n,annual_revenue=rev,capital=stock,unit='USD billion',revenue_capital_pct=round(rev/stock*100,4),basis='EV Nov2; run rate; estimated costs and boundaries not independently audited'))
 write(out,'capital-in-service.csv',capital)
 cost=ai['depreciation_bn']+ai['operating_cost_bn']+ai['required_return_bn']
 write(out,'ai-capital-cost.csv',[dict(measure=n,value=round(v,6),unit=unit) for n,v,unit in [('Capital in service',ai['capital_in_service_bn'],'USD billion'),('Capital including CIP',ai['capital_including_cip_bn'],'USD billion'),('Construction in progress difference',ai['capital_including_cip_bn']-ai['capital_in_service_bn'],'USD billion'),('Depreciation',ai['depreciation_bn'],'USD billion/year'),('Operating costs',ai['operating_cost_bn'],'USD billion/year'),('Required return',ai['required_return_bn'],'USD billion/year'),('Annual cost hurdle',cost,'USD billion/year'),('Infrastructure cost coverage',ai['infrastructure_revenue_bn']/cost,'multiple'),('All-stack cost coverage',ai['october_2026_run_rate_usd_bn']/cost,'multiple'),('12m commitments annual cost',ai['committed_12m_annual_cost_bn'],'USD billion/year'),('24m commitments annual cost',ai['committed_24m_annual_cost_bn'],'USD billion/year'),('12m required growth',ai['required_growth_12m_pct'],'percent/year, reported model'),('24m required growth',ai['required_growth_24m_pct'],'percent/year, reported model')]])
 sens=[]
 for r in read('sensitivity-inputs.csv'):
  life,util,price,margin=[float(r[k]) for k in ['life_years','utilisation','price_multiple','cash_margin']];eq=float(r['equipment_bn']);rev=float(r['full_utilisation_revenue_bn'])*util*price;dep=eq/life;ret=eq*float(r['required_return']);surplus=rev*margin
  sens.append(dict(scenario=r['scenario'],life_years=life,utilisation_pct=util*100,price_multiple=price,cash_margin_pct=margin*100,revenue_bn=round(rev,4),cash_operating_surplus_bn=round(surplus,4),depreciation_bn=round(dep,4),required_return_bn=ret,coverage=round(surplus/(dep+ret),4)))
 write(out,'ai-sensitivity.csv',sens)
 rev=ai['anthropic_q3_2026_revenue_usd_bn'];gaap=ai['anthropic_gaap_operating_bn'];adj=ai['anthropic_adjusted_operating_bn']
 assert abs(gaap+ai['anthropic_sbc_bn']+ai['anthropic_charity_bn']-adj)<1e-9
 write(out,'anthropic-q3.csv',[dict(period='Q3 2026',revenue_bn=rev,compute_infrastructure_bn=ai['anthropic_q3_2026_compute_infrastructure_cost_usd_bn'],gaap_operating_bn=gaap,gaap_margin_pct=round(gaap/rev*100,4),adjusted_operating_bn=adj,adjusted_margin_pct=round(adj/rev*100,4),sbc_adjustment_bn=ai['anthropic_sbc_bn'],charity_adjustment_bn=ai['anthropic_charity_bn'])])
 metrics=[dict(metric='AI revenue run-rate YoY growth pct',value=(ai['run_rate_yoy_multiple']-1)*100),dict(metric='AI Q3 estimated capex YoY growth pct',value=round((ai['q3_2026_estimated_ai_capex_usd_bn']/ai['q3_2025_estimated_ai_capex_usd_bn']-1)*100,4)),dict(metric='UK receipts CAGR 1844-1847 pct',value=round(((8.4/5)**(1/3)-1)*100,4)),dict(metric='Telecom receipts CAGR 1997-2000 pct',value=round(((229149/188529)**(1/3)-1)*100,4)),dict(metric='AI October run rate USD bn',value=ai['october_2026_run_rate_usd_bn']),dict(metric='AI TTM revenue USD bn',value=ai['ttm_to_october_2026_revenue_usd_bn'])]
 write(out,'ai-metrics.csv',metrics)
 comparisons=[]
 for case,start,end in [('UK railways',1844,1847),('US railways',1880,1882),('US telecom',1997,2000)]:
  a=next(r for r in revenue if r['precedent']==case and r['year']==start);b=next(r for r in revenue if r['precedent']==case and r['year']==end)
  comparisons.append(dict(case=case,start=start,end=end,revenue_growth_pct=round((b['revenue_m']/a['revenue_m']-1)*100,4),capex_growth_pct=round((b['annual_capex_m']/a['annual_capex_m']-1)*100,4)))
 comparisons.append(dict(case='AI estimates',start=2025,end=2026,revenue_growth_pct=metrics[0]['value'],capex_growth_pct=metrics[1]['value']))
 write(out,'growth-comparison.csv',comparisons)
 write(out,'uk-gdp-sensitivity.csv',[dict(series=r['series'],spend_gdp_pct=round(float(r['annual_capex_gbp_m'])/float(r['gdp_gbp_m'])*100,4)) for r in read('uk-gdp-inputs.csv')])
 assert round(total/g9*100,1)==2.3
 assert 2.7<quarter*4/gq*100<2.9
 assert round(cost)==180 and round(ai['infrastructure_revenue_bn']/cost,2)==1.42
 print('Rebuilt',len(list(out.glob('*.csv'))),'tables; 2.3% reproduced to one decimal under disclosed reporting-period convention.')
if __name__=='__main__':reproduce(sys.argv[1])
