"""Render PNG + exact plotted CSV + portable Vega-Lite spec."""
import csv,json,shutil
from pathlib import Path
import vl_convert as vlc
R=Path(__file__).resolve().parents[1];C=R/'charts';C.mkdir(exist_ok=True)
def rows(file):return list(csv.DictReader(((R/'expected' if (R/'expected').exists() else R/'data')/file).open()))
def save(name,data,spec):
 with (C/(name+'.csv')).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
 spec={'$schema':'https://vega.github.io/schema/vega-lite/v5.json','background':'white','data':{'url':'charts/'+name+'.csv'},**spec,'config':{'font':'Arial','axis':{'labelFontSize':12,'titleFontSize':13},'legend':{'labelFontSize':12,'titleFontSize':13},'view':{'stroke':None}}}
 (C/(name+'.vl.json')).write_text(json.dumps(spec,indent=2)+'\n')
 static={**spec,'data':{'values':data}}
 (C/(name+'.png')).write_bytes(vlc.vegalite_to_png(static,scale=2))
 tooltip=[{'field':k,'type':'quantitative' if k in ['count','all_lexical_hits_in_decade','political_hits_in_decade'] else 'nominal'} for k in data[0]]
 print(name,len(data))
save('1-news-sample',rows('news-sample.csv'),{'width':600,'height':280,'title':{'text':'Most sampled policy uses are conventional labels','subtitle':['Random sample of 160 hawk/dove forms in SiBol; 50 policy tokens','Two tokens add bird behaviour. Counts concern the saved sample.'],'anchor':'start'},'mark':{'type':'bar'},'params':[{'name':'pick','select':{'type':'point','fields':['category']},'bind':'legend'}],'encoding':{'x':{'field':'decade','type':'ordinal','title':'Publication decade (uneven corpus coverage)','axis':{'labelAngle':0}},'y':{'field':'count','type':'quantitative','title':'Sampled lexical tokens'},'color':{'field':'category','type':'nominal','title':None,'scale':{'domain':['Other sense','Conventional policy use','Bird elaboration'],'range':['#bdc6cb','#246b8e','#d48b20']},'legend':{'orient':'bottom','direction':'vertical'}},'opacity':{'condition':{'param':'pick','value':1},'value':0.18},'tooltip':[{'field':'category'},{'field':'count','type':'quantitative'},{'field':'political_hits_in_decade','type':'quantitative'},{'field':'all_lexical_hits_in_decade','type':'quantitative'}]}})
r=[x for x in rows('source-decades.csv') if x['source']!='SiBol random lexical sample' and int(x['political_units'])>0]
for x in r:x['collection']='Hansard contributions' if x['source'].startswith('Hansard') else 'SiBol close-pair matches'
save('2-paired-searches',r,{'title':{'text':'Bird elaboration occurs in paired mentions','subtitle':['Each bar uses all annotated policy units in its source and decade.','Different retrieval units: these are not comparable population rates.'],'anchor':'start'},'facet':{'column':{'field':'collection','type':'nominal','title':None}},'spec':{'width':285,'height':260,'mark':{'type':'bar','color':'#246b8e'},'encoding':{'x':{'field':'decade','type':'ordinal','title':'Publication decade','axis':{'labelAngle':-45}},'y':{'field':'elaboration_share_percent','type':'quantitative','title':'Elaborated policy units (%)','scale':{'domain':[0,30]}},'tooltip':[{'field':'source'},{'field':'decade'},{'field':'elaborated_units','type':'quantitative'},{'field':'political_units','type':'quantitative'},{'field':'elaboration_share_percent','type':'quantitative'}]}},'resolve':{'scale':{'x':'independent'}}})
