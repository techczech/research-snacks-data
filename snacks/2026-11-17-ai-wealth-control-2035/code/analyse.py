# /// script
# requires-python = ">=3.10"
# dependencies = ["vl-convert-python==1.9.0.post1"]
# ///
"""Rebuild charts from source-checked extracts; no forecast parameters are fitted.
Run: uv run code/analyse.py --entry DIRECTORY
"""
from pathlib import Path
import argparse, csv, json, copy
import vl_convert as vlc
ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--entry', type=Path, required=True)
args = parser.parse_args()
entry = args.entry.resolve()
SOURCE = ROOT/'outputs' if (ROOT/'outputs'/'historical-observations.csv').exists() else ROOT/'data'
for part in ('data','charts','code'):
 (entry/part).mkdir(parents=True,exist_ok=True)
PALETTE=['#216d68','#b36b21','#426b97','#6b6c65']
BASE={"$schema":"https://vega.github.io/schema/vega-lite/v5.json","width":"container","height":310,"autosize":{"type":"fit-x","contains":"padding"},"background":"#faf9f6","config":{"font":"Arial, sans-serif","view":{"stroke":None},"axis":{"labelColor":"#44443e","titleColor":"#44443e","gridColor":"#e3e1d9","labelFontSize":12,"titleFontSize":13},"legend":{"orient":"bottom","columns":1,"labelFontSize":12,"labelLimit":420,"title":None},"title":{"anchor":"start","fontSize":18,"subtitleFontSize":12,"subtitleColor":"#55554f","offset":16}}}
def chart(name, rows, spec):
 with (entry/'charts'/f'{name}.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
 out={**copy.deepcopy(BASE),**spec,'data':{'url':f'charts/{name}.csv'}}
 (entry/'charts'/f'{name}.vl.json').write_text(json.dumps(out,indent=2)+'\n')
 image_spec=copy.deepcopy(out)
 image_spec['width']=780
 image_spec['data']={'values':rows}
 (entry/'charts'/f'{name}.png').write_bytes(vlc.vegalite_to_png(image_spec,scale=2))
observations=list(csv.DictReader((SOURCE/'historical-observations.csv').open()))
for r in observations:
 r['year']=int(r['year']);r['share_pct']=float(r['share_pct'])
 first=min(x['year'] if isinstance(x['year'],int) else int(x['year']) for x in observations if x['series']==r['series'])
 r['years_from_first_observation']=r['year']-first
 assert 0<=r['share_pct']<=100
series=list(dict.fromkeys(r['series'] for r in observations))
chart('1-observed-transitions', observations, {
 'title':{'text':'Observed changes','subtitle':['Different denominators:','power, people, assets, turnover.','Clock starts at first point shown.']},
 'params':[{'name':'pick','select':{'type':'point','fields':['series']},'bind':'legend'}],
 'mark':{'type':'line','point':{'filled':True,'size':65},'strokeWidth':2.5},
 'encoding':{
  'x':{'field':'years_from_first_observation','type':'quantitative','title':'Years since first point','scale':{'domain':[0,30]},'axis':{'tickMinStep':1}},
  'y':{'field':'share_pct','type':'quantitative','title':'Reported percentage','scale':{'domain':[0,100]}},
  'color':{'field':'series','type':'nominal','scale':{'domain':series,'range':PALETTE}},
  'opacity':{'condition':{'param':'pick','value':1},'value':0.15},
  'tooltip':[{'field':'series','title':'Measure'},{'field':'year','title':'Year','format':'d'},{'field':'share_pct','title':'Reported percentage','format':'.0f'},{'field':'denominator','title':'Denominator'},{'field':'source_url','title':'Primary source'}]}})
payments=list(csv.DictReader((SOURCE/'payment-shares.csv').open()))
for r in payments:r['share_pct']=float(r['share_pct']);r['year']=int(r['year'])
for measure in ['Number','Value']:
 assert abs(sum(r['share_pct'] for r in payments if r['measure']==measure)-100)<0.015
chart('2-payments-denominators',payments,{
 'title':{'text':'Payment count and value','subtitle':['US core noncash payments, 2020.','Federal Reserve Payments Study.']},
 'params':[{'name':'pick','select':{'type':'point','fields':['measure']},'bind':'legend'}],
 'mark':{'type':'bar','cornerRadiusEnd':3},
 'encoding':{'x':{'field':'instrument','type':'nominal','title':None,'sort':['Card','ACH','Cheque'],'axis':{'labelAngle':0}},
 'y':{'field':'share_pct','type':'quantitative','title':'Share of payments (%)','scale':{'domain':[0,100]}},
 'xOffset':{'field':'measure','sort':['Number','Value']},
 'color':{'field':'measure','type':'nominal','scale':{'domain':['Number','Value'],'range':PALETTE[:2]}},
 'opacity':{'condition':{'param':'pick','value':1},'value':0.15},
 'tooltip':[{'field':'instrument','title':'Instrument'},{'field':'measure','title':'Denominator'},{'field':'share_pct','title':'Share (%)','format':'.2f'},{'field':'year','title':'Year','format':'d'}]}})
# Equal denominators and exclusive attribution are requirements, not observations.
def crosses(ai_share_future, total_future_real, human_controlled_baseline_real):
 assert 0<=ai_share_future<=1 and total_future_real>=0
 return ai_share_future*total_future_real>human_controlled_baseline_real
# Boundary checks: equality is not 'more'; nominal turnover is never an input.
assert not crosses(0.5,2,1)
assert crosses(0.6,2,1)
assert not crosses(1,1,1)
print('Rebuilt two PNG/CSV/Vega-Lite chart sets; payment totals reconcile; stock comparison boundaries checked.')
