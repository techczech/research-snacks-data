"""Render the exact plotted CSVs as Vega-Lite and PNG; requires vl-convert-python."""
from pathlib import Path
import csv,json,sys,shutil
import vl_convert as vlc
P=Path(__file__).resolve().parents[1]
C=P/'charts';C.mkdir(exist_ok=True)
BASE={'$schema':'https://vega.github.io/schema/vega-lite/v5.json','background':'#ffffff','width':580,'config':{'view':{'stroke':None},'axis':{'labelFontSize':12,'titleFontSize':13,'gridColor':'#e6e5df'},'legend':{'orient':'bottom','labelFontSize':12,'labelLimit':330},'title':{'anchor':'start','fontSize':18,'subtitleFontSize':12,'subtitleColor':'#555555'}}}
def save(name,spec):
 shutil.copy2(P/'expected'/f'{name}.csv',C/f'{name}.csv')
 spec={**BASE,**spec,'data':{'url':f'charts/{name}.csv'}}
 (C/f'{name}.vl.json').write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
 rr=list(csv.DictReader((C/f'{name}.csv').open()))
 # Parse numeric fields explicitly for the PNG; browser CSV inference uses same fields.
 for r in rr:
  for k in ['elapsed_days','onset_year','decade','campaigns','successes','ongoing','resolved','success_pct']:
   if k in r:r[k]=float(r[k])
 pngspec={**spec,'width':580,'data':{'values':rr}}
 (C/f'{name}.png').write_bytes(vlc.vegalite_to_png(pngspec,scale=2))
 print(name,'PNG + CSV + Vega-Lite')
save('1-selected-clocks',{
 'title':{'text':'Selected protest-to-departure clocks','subtitle':['Sixteen chosen episodes, 1848–2024; final protest episode, not whole campaign.','Libya uses loss of the capital; mixed mechanisms are tested separately.']},
 'height':470,'mark':{'type':'point','filled':True,'size':100},
 'params':[{'name':'era_pick','select':{'type':'point','fields':['era']},'bind':'legend'}],
 'encoding':{
 'y':{'field':'case','type':'nominal','sort':['France 1848','Russia 1917','Iran 1978–79','Philippines 1986','East Germany 1989','Czechoslovakia 1989','Romania 1989','Serbia 2000','Georgia 2003','Tunisia 2010–11','Egypt 2011','Libya 2011','Yemen 2011–12','Sudan 2018–19','Sri Lanka 2022','Bangladesh 2024'],'title':None,'axis':{'labelLimit':210}},
 'x':{'field':'elapsed_days','type':'quantitative','scale':{'type':'log','domain':[1,500]},'axis':{'values':[1,3,10,30,100,300],'format':'d'},'title':'Elapsed days (logarithmic scale)'},
 'color':{'field':'era','type':'nominal','scale':{'domain':['Before 1990','1990–2009','2010–2024'],'range':['#626b75','#d47629','#167e86']},'legend':{'title':None}},
 'opacity':{'condition':{'param':'era_pick','value':1},'value':0.2},
 'tooltip':[{'field':'case'},{'field':'start','title':'Start'},{'field':'end','title':'End'},{'field':'elapsed_days','title':'Elapsed days'},{'field':'mechanism'}]}})
save('2-success-denominators',{
 'title':{'text':'NAVCO success depends on the denominator','subtitle':['Primarily nonviolent maximalist campaigns grouped by peak decade.','Preliminary NAVCO 1.3; outcomes observed through 31 December 2019.']},
 'height':310,'mark':{'type':'bar','cornerRadiusEnd':2},
 'params':[{'name':'denom_pick','select':{'type':'point','fields':['denominator']},'bind':'legend'}],
 'encoding':{
 'x':{'field':'decade','type':'ordinal','title':'Peak decade','axis':{'labelAngle':0}},
 'xOffset':{'field':'denominator'},
 'y':{'field':'success_pct','type':'quantitative','scale':{'domain':[0,100]},'title':'Full success (%)'},
 'color':{'field':'denominator','type':'nominal','scale':{'domain':['All campaigns, status at 2019','Exclude ongoing campaigns'],'range':['#167e86','#d47629']},'legend':{'title':None,'columns':1}},
 'opacity':{'condition':{'param':'denom_pick','value':1},'value':0.2},
 'tooltip':[{'field':'decade'},{'field':'denominator'},{'field':'success_pct','format':'.1f'},{'field':'campaigns'},{'field':'successes'},{'field':'ongoing'},{'field':'resolved'}]}})
