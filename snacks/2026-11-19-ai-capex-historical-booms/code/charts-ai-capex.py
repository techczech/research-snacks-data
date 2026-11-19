#!/usr/bin/env python3
"""Make original PNG/CSV/Vega-Lite charts from the checked derived tables.
Run with uv run in the checking repo (vl-convert-python is already locked there):
python3 charts-ai-capex.py ENTRY_DIRECTORY
"""
import csv,json,shutil,sys
from pathlib import Path
import vl_convert as vlc
P=Path(sys.argv[1]);C=P/'charts';C.mkdir(exist_ok=True)
BASE={'$schema':'https://vega.github.io/schema/vega-lite/v5.json','width':'container','config':{'font':'Arial, sans-serif','view':{'stroke':None},'axis':{'labelColor':'#343d46','titleColor':'#343d46','gridColor':'#dedfdc','labelFontSize':12,'titleFontSize':13},'legend':{'orient':'top','title':None,'labelFontSize':12,'labelLimit':500},'title':{'anchor':'start','fontSize':20,'subtitleFontSize':12,'subtitleColor':'#4b5563'},'background':'#fbfaf7'}}
def emit(name,source,spec):
 shutil.copy2(P/'data'/source,C/(name+'.csv'))
 if name=='1-spending-gdp':
  plotted=list(csv.DictReader((P/'data'/source).open()))
  spec['encoding']['y']['sort']=[r['precedent'] for r in sorted(plotted,key=lambda r:float(r['peak_spend_pct_gdp']),reverse=True)]
 spec={**BASE,**spec,'data':{'url':f'charts/{name}.csv','format':{'type':'csv','parse':'auto'}}}
 (C/(name+'.vl.json')).write_text(json.dumps(spec,indent=2,ensure_ascii=False)+'\n')
 png=json.loads(json.dumps(spec));png['width']=650
 
 if 'facet' in png:
  png.pop('width',None);png['spec']['width']=650
 rows=list(csv.DictReader((C/(name+'.csv')).open()))
 for row in rows:
  for key in ['year','peak_spend_pct_gdp','years_from_first_observation','index_first_observation_100','first_observation_year']:
   if key in row: row[key]=float(row[key])
 png['data']={'values':rows}
 (C/(name+'.png')).write_bytes(vlc.vegalite_to_png(png,scale=2))

emit('1-spending-gdp','1-spending-gdp.csv',{
 'title':{'text':'Railway booms were larger shares of GDP','subtitle':['Annual nominal spending / same-country, same-year nominal GDP (%)','AI is the article’s global-company YTD proxy; historical scopes differ.']},
 'height':{'step':36},
 'encoding':{'y':{'field':'precedent','type':'nominal','sort':{'field':'peak_spend_pct_gdp','order':'descending'},'title':None,'axis':{'labelLimit':235}},'x':{'field':'peak_spend_pct_gdp','type':'quantitative','title':'Annual spending as a share of GDP (%)','scale':{'domain':[0,7]}},'tooltip':[{'field':'precedent','title':'Comparison'},{'field':'year','title':'Year'},{'field':'peak_spend_pct_gdp','title':'Share of GDP (%)','format':'.2f'},{'field':'scope','title':'Coverage'},{'field':'status','title':'Evidence'}]},
 'layer':[{'mark':{'type':'bar','cornerRadiusEnd':2},'params':[{'name':'pick','select':{'type':'point','fields':['status']},'bind':'legend'}],'encoding':{'color':{'field':'status','type':'nominal','scale':{'domain':['Reconstructed historical share','Reported global-company proxy'],'range':['#126782','#ce7515']},'legend':{'direction':'vertical'}},'opacity':{'condition':{'param':'pick','value':1},'value':0.2}}},{'mark':{'type':'text','align':'left','dx':5,'fontSize':12,'color':'#253341'},'encoding':{'text':{'field':'peak_spend_pct_gdp','format':'.2f'}}}]})

emit('2-revenue-and-capex','2-revenue-and-capex.csv',{
 'title':{'text':'Revenue growth can coexist with overbuilding','subtitle':['Both series start at 100; UK 1844, US telecom 1997.','Telecom: end-user receipts / broader provider spending; imperfect cohort match.']},
 'facet':{'row':{'field':'precedent','type':'nominal','header':{'labelFontSize':15,'labelFontWeight':'bold','labelAngle':0,'labelAlign':'left','title':None},'sort':['UK railways','US telecom']}},
 'spec':{'width':'container','height':170,'mark':{'type':'line','point':{'filled':True,'size':45}},'params':[{'name':'seriespick','select':{'type':'point','fields':['series']},'bind':'legend'}],
 'encoding':{'x':{'field':'years_from_first_observation','type':'quantitative','title':'Years after the first displayed observation','axis':{'tickMinStep':1}},'y':{'field':'index_first_observation_100','type':'quantitative','title':'Index (first year = 100)','scale':{'zero':True}},'color':{'field':'series','type':'nominal','scale':{'domain':['Annual capex','Gross revenue','End-user revenue'],'range':['#b86412','#126782','#126782']}},'strokeDash':{'condition':{'test':"datum.series === 'Annual capex'",'value':[1,0]},'value':[7,2]},'opacity':{'condition':{'param':'seriespick','value':1},'value':0.2},'tooltip':[{'field':'precedent'},{'field':'year'},{'field':'series'},{'field':'index_first_observation_100','title':'Index','format':'.1f'}]}},
 'resolve':{'scale':{'y':'independent'}}})
