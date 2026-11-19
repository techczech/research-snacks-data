#!/usr/bin/env python3
"""Recompute selected-date arithmetic and NAVCO denominators, offline.
Python standard library only. Usage: python3 code/reproduce.py OUTPUT_DIRECTORY
This checks calculations, not historical date judgements or causal identification.
"""
from pathlib import Path
import csv,sys,statistics,math
from datetime import date
P=Path(__file__).resolve().parents[1]
def read(name,delimiter=','):
 with (P/'data'/name).open(newline='') as f:return list(csv.DictReader(f,delimiter=delimiter))
def write(out,name,rows):
 assert rows
 with (out/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def n(r,k):return int(float(r[k]))
def elapsed(r):return (date.fromisoformat(r['end'])-date.fromisoformat(r['start'])).days
def ranks(x):
 return [1+sum(v<z for v in x)+(sum(v==z for v in x)-1)/2 for z in x]
def corr(x,y):
 a,b=statistics.mean(x),statistics.mean(y)
 return sum((u-a)*(v-b) for u,v in zip(x,y))/math.sqrt(sum((u-a)**2 for u in x)*sum((v-b)**2 for v in y))
def era(y):return 'Before 1990' if y<1990 else '1990–2009' if y<2010 else '2010–2024'
def reproduce(out):
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 cases=read('cases.csv');assert len(cases)==16
 plotted=[]
 for r in cases:
  d=elapsed(r);assert d>=0
  y=int(r['start'][:4]);plotted.append({'case':r['case'],'onset_year':y,'era':era(y),'start':r['start'],'end':r['end'],'elapsed_days':d,'inclusive_days':d+1,'mechanism':r['mechanism'],'source_url':r['source_url']})
 write(out,'1-selected-clocks.csv',plotted)
 pair=[r for r in plotted if r['case'] in ['Czechoslovakia 1989','Egypt 2011']]
 assert [r['elapsed_days'] for r in pair]==[23,17]
 assert pair[0]['elapsed_days']-pair[1]['elapsed_days']==6
 write(out,'original-comparison.csv',pair)
 write(out,'alternative-clocks.csv',[{**r,'elapsed_days':elapsed(r),'inclusive_days':elapsed(r)+1} for r in read('alternative-dates.csv')])
 groups=[('All selected exits',lambda r:True),('Exclude armed revolt/war/mutiny',lambda r:r['exclude_armed']=='0'),('Also exclude military split/coup',lambda r:r['exclude_armed']=='0' and r['exclude_military_split']=='0')]
 summaries=[]
 for label,fn in groups:
  for a,b,e in [(0,1989,'Before 1990'),(1990,2009,'1990–2009'),(2010,2024,'2010–2024'),(1990,2024,'1990–2024')]:
   q=[elapsed(r) for r in cases if a<=int(r['start'][:4])<=b and fn(r)]
   summaries.append({'selection':label,'era':e,'n':len(q),'median_days':statistics.median(q),'min_days':min(q),'max_days':max(q)})
 write(out,'era-sensitivity.csv',summaries)
 # Exploratory sensitivity to individual selected cases; no population p-values.
 loo=[]
 for drop in [None]+[r['case'] for r in cases]:
  rr=[r for r in cases if r['case']!=drop];early=[elapsed(r) for r in rr if int(r['start'][:4])<1990];late=[elapsed(r) for r in rr if int(r['start'][:4])>=1990]
  loo.append({'omitted_case':drop or 'None','early_n':len(early),'late_n':len(late),'late_minus_early_median_days':statistics.median(late)-statistics.median(early)})
 write(out,'leave-one-out.csv',loo)
 write(out,'rank-diagnostic.csv',[{'selected_cases':len(cases),'spearman_year_days':round(corr(ranks([int(r['start'][:4]) for r in cases]),ranks([elapsed(r) for r in cases])),6),'scope':'Descriptive association among selected exits; no causal or population inference'}])
 raw=read('navco-1.3.tab','\t');assert len(raw)==622
 nv=[r for r in raw if n(r,'NONVIOL')==1];assert len(nv)==320
 success=[]
 for basis,field in [('Peak decade','EYEAR'),('Onset decade','BYEAR')]:
  for scope in ['All maximalist goals','Regime change only']:
   for dec in range(1900,2020,10):
    q=[r for r in nv if dec<=n(r,field)<dec+10 and (scope=='All maximalist goals' or n(r,'REGCHANGE')==1)]
    if not q:continue
    ongoing=sum(n(r,'ONGOING') for r in q);win=sum(n(r,'SUCCESS') for r in q);resolved=len(q)-ongoing
    assert not any(n(r,'ONGOING') and n(r,'SUCCESS') for r in q)
    success.append({'basis':basis,'scope':scope,'decade':dec,'campaigns':len(q),'successes':win,'ongoing':ongoing,'resolved':resolved,'success_asof_2019_pct':round(100*win/len(q),3),'success_resolved_only_pct':round(100*win/resolved,3) if resolved else ''})
 write(out,'navco-all-denominators.csv',success)
 chart=[]
 for r in success:
  if r['basis']=='Peak decade' and r['scope']=='All maximalist goals' and r['decade']>=1970:
   for col,label in [('success_asof_2019_pct','All campaigns, status at 2019'),('success_resolved_only_pct','Exclude ongoing campaigns')]:
    chart.append({**{k:r[k] for k in ['decade','campaigns','successes','ongoing','resolved']},'denominator':label,'success_pct':r[col]})
 write(out,'2-success-denominators.csv',chart)
 exposure=[]
 for a,b in [(1990,1999),(2000,2009),(2010,2014),(2015,2019)]:
  for scope in ['All maximalist goals','Regime change only']:
   q=[r for r in nv if a<=n(r,'BYEAR')<=b and (scope=='All maximalist goals' or n(r,'REGCHANGE')==1)]
   win=sum(n(r,'SUCCESS') for r in q);ongoing=sum(n(r,'ONGOING') for r in q);resolved=len(q)-ongoing
   exposure.append({'onset_cohort':f'{a}–{b}','scope':scope,'n':len(q),'successes':win,'ongoing':ongoing,'success_asof_2019_pct':round(100*win/len(q),3),'success_resolved_only_pct':round(100*win/resolved,3)})
 write(out,'navco-exposure-sensitivity.csv',exposure)
 # Exact provider rows: campaign boundaries disagree with the final-episode clocks.
 audit=[r for r in nv if (r['LOCATION']=='Egypt' and r['CAMPAIGN']=='Anti-Mubarak movement') or (r['LOCATION']=='Czechoslovakia' and r['CAMPAIGN']=='Velvet Revolution') or (r['LOCATION']=='East Germany' and n(r,'BYEAR')==1989) or (r['LOCATION']=='Ukraine' and r['CAMPAIGN']=='Orange Revolution')]
 assert len(audit)==4
 write(out,'navco-boundary-examples.csv',audit)
 write(out,'egypt-survey-facts.csv',read('egypt-survey-inputs.csv'))
 print('Rebuilt 11 CSV tables: date arithmetic, era sensitivities, NAVCO and survey facts')
if __name__=='__main__':reproduce(sys.argv[1])
