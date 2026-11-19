#!/usr/bin/env python3
"""Offline arithmetic for canals, civil nuclear and 1850s railways.
Run: python code/reproduce.py OUTPUT. Checks selected-source arithmetic, not
source transcription, an exhaustive peak search or lifetime investor returns.
"""
import csv, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(n):return list(csv.DictReader((ROOT/'data'/n).open()))
def write(out,n,rows):
 with (out/n).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def reproduce(out):
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 canals=[]
 for r in read('canal-period-inputs.csv'):
  n=int(r['end'])-int(r['start'])+1;total=float(r['investment_gbp_m']);g=float(r['reference_gdp_gbp_m'])
  canals.append(dict(period=r['start']+'-'+r['end'],years=n,investment_gbp_m=total,annual_mean_gbp_m=round(total/n,6),gdp_reference_year=r['reference_year'],gdp_gbp_m=round(g,6),annual_mean_over_reference_gdp_pct=round(total/n/g*100,4),cumulative_over_reference_gdp_pct=round(total/g*100,4),period_spend_over_period_gdp_pct=round(total/n/float(r['mean_gdp_gbp_m'])*100,4)))
 write(out,'canal-periods.csv',canals)
 cr=[]
 for r in read('canal-company-inputs.csv'):
  cr.append(dict(company=r['company'],mean_roe_pct=float(r['mean_roe_pct']),mean_dividend_on_share_capital_pct=float(r['mean_dividend_on_share_capital_pct'])))
 write(out,'canal-returns.csv',cr)
 ct=[{k:(float(v) if k.endswith('_pct') else v) for k,v in r.items() if k!='source'} for r in read('canal-turnover-inputs.csv')];write(out,'canal-turnover.csv',ct)
 nu=[]
 for r in read('us-nuclear-investment-inputs.csv'):
  v=float(r['construction_usd_m']);g=float(r['nominal_gdp_usd_m']);nu.append(dict(year=int(r['year']),construction_usd_m=v,nominal_gdp_usd_m=g,share_gdp_pct=round(v/g*100,4)))
 assert [r['year'] for r in nu]==list(range(1979,1991))
 write(out,'nuclear-annual.csv',nu)
 op=[]
 for r in read('us-nuclear-operation-inputs.csv'):
  if int(r['year']) in [1965,1970,1980,1990,2000,2010]:
   op.append(dict(year=int(r['year']),generation_twh=float(r['generation_twh']),share_generation_pct=float(r['share_generation_pct']),summer_capacity_gw=float(r['summer_capacity_gw']),capacity_factor_pct=r['capacity_factor_pct']))
 write(out,'nuclear-operations.csv',op)
 ra=[]
 for r in read('us-rail-1850s-inputs.csv'):
  v,g=float(r['gross_investment_usd_m']),float(r['gdp_usd_m']);ra.append(dict(year=int(r['year']),gross_investment_usd_m=v,gdp_usd_m=g,share_gdp_pct=round(v/g*100,4)))
 write(out,'rail-1850s.csv',ra)
 cum=[]
 rail_spending={int(r['year']):float(r['gross_investment_usd_m']) for r in read('us-rail-annual-investment-inputs.csv')}
 france_gdp=sum(float(r['nominal_gdp_eur_m']) for r in read('france-gdp-quarter-inputs.csv'))
 for r in read('cumulative-inputs.csv'):
  spending=sum(rail_spending[y] for y in range(1851,1861)) if r['case']=='US railways 1851-1860' else float(r['spending_m'])
  assert abs(spending-float(r['spending_m']))<1e-6
  if r['case'].startswith('France'):assert abs(france_gdp-float(r['gdp_m']))<1e-6
  cum.append(dict(case=r['case'],window=r['start']+'-'+r['end'],spending_m=float(r['spending_m']),gdp_reference_year=int(r['gdp_reference_year']),reference_gdp_m=float(r['gdp_m']),unit=r['unit'],share_one_year_gdp_pct=round(float(r['spending_m'])/float(r['gdp_m'])*100,4),scope=r['scope']))
 c=canals[-1];cum.append(dict(case='GB canals and waterways',window=c['period'],spending_m=c['investment_gbp_m'],gdp_reference_year=int(c['gdp_reference_year']),reference_gdp_m=c['gdp_gbp_m'],unit='GBP million',share_one_year_gdp_pct=c['cumulative_over_reference_gdp_pct'],scope='Quasi-net; secondary citation; period differs from requested 1790-1797'))
 g=next(r['nominal_gdp_usd_m'] for r in nu if r['year']==1983);s=sum(r['construction_usd_m'] for r in nu)
 cum.append(dict(case='US IOU nuclear construction',window='1979-1990',spending_m=s,gdp_reference_year=1983,reference_gdp_m=g,unit='USD million',share_one_year_gdp_pct=round(s/g*100,4),scope='IOUs only; includes capitalised financing; not all US civil nuclear 1965-1990'))
 write(out,'cumulative.csv',cum)
 facts={r['metric']:float(r['value']) for r in read('nuclear-outcome-inputs.csv')}
 f=lambda k:facts[k]
 economics=[]
 def calc(n,v,u):economics.append(dict(metric=n,value=round(v,6),unit=u))
 for r in read('nuclear-outcome-inputs.csv'):calc(r['metric'],float(r['value']),r['unit'])
 revenue=f('Columbia FY2009 operating revenue');expense=f('Columbia FY2009 operating expense');net=revenue-expense
 assert abs(net-f('Columbia FY2009 net operating revenue'))<1e-6
 calc('Columbia revenue over original nominal construction cost',revenue/f('Columbia final construction estimate 1984')*100,'percent; nominal turnover against mixed-year historic cost, not real return')
 calc('Columbia operating margin before other income and financing',net/revenue*100,'percent; cost recovery billing, not investor profit')
 calc('Columbia final over initial nominal construction estimate',f('Columbia final construction estimate 1984')/f('Columbia initial construction estimate 1971'),'multiple; includes inflation and changed scope')
 calc('France 1983 direct construction over GDP',f('France 1983 direct construction graph reading')/f('France 1983 GDP')*100,'percent; approximate graph reading, not annual peak')
 calc('France overnight plus estimated capitalised interest',f('France fleet overnight cost')+f('France fleet capitalised interest'),'2010 EUR million; approximate')
 calc('Ratio of CBO mean actual to projected costs',f('US completed-plant actual overnight cost')/f('US completed-plant projected overnight cost'),'multiple; differs from mean percentage overrun')
 write(out,'nuclear-economics.csv',economics)
 comp=[]
 for r in read('parent-comparison-inputs.csv'):
  comp.append(dict(case=r['precedent'],period=r['year'],spend_gdp_pct=round(float(r['annual_spending_m'])/float(r['gdp_m'])*100,4),basis='Historical annual reconstruction',qualification=r['scope']))
 for r in ra:
  if r['year']==1854:comp.append(dict(case='US railways, antebellum',period='1854',spend_gdp_pct=r['share_gdp_pct'],basis='Historical annual reconstruction',qualification='Fishlow gross current-dollar expenditure; excludes failed projects; Cambridge transcription'))
 peak=max(nu,key=lambda r:r['share_gdp_pct'])
 comp.append(dict(case='US nuclear, investor-owned utilities',period=str(peak['year']),spend_gdp_pct=peak['share_gdp_pct'],basis='Partial nuclear coverage',qualification='Peak only within 1979-1990 IOU accounting construction expenditure; includes financing'))
 comp.append(dict(case='France nuclear, direct construction',period='1983',spend_gdp_pct=round(f('France 1983 direct construction graph reading')/f('France 1983 GDP')*100,4),basis='Approximate single observation',qualification='Graph reading; no peak claim; excludes engineering/pre-operation/interest'))
 comp.append(dict(case='GB canals and waterways, annual mean',period='1791-1801',spend_gdp_pct=c['annual_mean_over_reference_gdp_pct'],basis='Period mean, not annual peak',qualification='Annual mean divided by 1796 GDP; quasi-net waterways; secondary citation'))
 ai=json.loads((ROOT/'data/parent-ai-inputs.json').read_text())
 comp.append(dict(case='Five technology firms, reported proxy',period='2026 YTD',spend_gdp_pct=ai['article_2026_ytd_capex_us_gdp_pct'],basis='Global company proxy',qualification='Global company all-asset cash spending / US GDP; not domestic AI-only investment'))
 write(out,'comparison.csv',comp)
 write(out,'ai-scenarios.csv',read('parent-ai-scenario-inputs.csv'))
 chart1=[dict(r,label=r['case']+' ('+r['period']+')') for r in comp];write(out,'1-spending-comparison.csv',chart1)
 chart2=[]
 for r in cr:
  for label,k in [('Return on equity','mean_roe_pct'),('Dividend / nominal share capital','mean_dividend_on_share_capital_pct')]:chart2.append(dict(company=r['company'],measure=label,percent=r[k]))
 write(out,'2-canal-dividends-returns.csv',chart2)
 write(out,'3-nuclear-construction.csv',nu)
 chart4=[]
 for r in op:
  for label,k,u in [('Electricity generated','generation_twh','TWh'),('Capacity factor','capacity_factor_pct','%')]:
   if r[k]!='NA':chart4.append(dict(year=r['year'],measure=label,value=float(r[k]),unit=u))
 write(out,'4-nuclear-output-use.csv',chart4)
 print('Rebuilt 14 tables; source interpretation remains a human judgement.')
if __name__=='__main__':reproduce(sys.argv[1])
