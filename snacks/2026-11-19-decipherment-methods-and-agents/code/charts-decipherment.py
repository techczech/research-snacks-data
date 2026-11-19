"""Create exact plotted CSVs, Vega-Lite specs and PNG fallbacks from rebuilt tables.
Run from snack folder with: uv run --project <checking-repository> python code/charts-decipherment.py
The calculation-only checker does not require the optional image renderer.
"""
from pathlib import Path
import csv,json,copy
import vl_convert as vlc
R=Path(__file__).resolve().parents[1]
P=R/'expected' if (R/'expected').exists() else R/'data'
C=R/'charts';C.mkdir(exist_ok=True)
def read(name):return list(csv.DictReader((P/name).open()))
def save(stem,rows,spec):
 with (C/(stem+'.csv')).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator="\n");w.writeheader();w.writerows(rows)
 spec={'$schema':'https://vega.github.io/schema/vega-lite/v5.json','background':'#fffdf8','width':'container','config':{'font':'Arial','axis':{'labelFontSize':12,'titleFontSize':13,'gridColor':'#e2dfd5'},'title':{'fontSize':18,'anchor':'start','subtitleFontSize':12,'subtitleColor':'#4c5556'},'view':{'stroke':None},'legend':{'orient':'bottom','labelFontSize':12}},'data':{'url':'charts/'+stem+'.csv'},**spec}
 (C/(stem+'.vl.json')).write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
 png=copy.deepcopy(spec);png['width']=720;png['data']={'values':rows}
 (C/(stem+'.png')).write_bytes(vlc.vegalite_to_png(png,scale=2))
rows=read('1-timeline.csv')
for r in rows:r['year']=int(r['year'])
save('1-decipherment-timeline',rows,{'title':{'text':'Decipherment happened in stages','subtitle':'Selected milestones in 20 recoveries; a plotted date is not a date of complete understanding'},'height':550,'mark':{'type':'point','filled':True,'size':85,'color':'#23656c'},'encoding':{'x':{'field':'year','type':'quantitative','scale':{'domain':[1740,2005]},'axis':{'format':'d','title':'Year of selected milestone','tickCount':8}},'y':{'field':'case','type':'nominal','sort':[r['case'] for r in rows],'axis':{'title':None,'labelLimit':240}},'tooltip':[{'field':'case'},{'field':'year','type':'quantitative','format':'d'},{'field':'milestone'},{'field':'people'}]}})
rows=[]
for r in read('2-preconditions-counts.csv'):
 for state in ['yes','partial','no','uncertain']:rows.append({'condition':r['condition'],'state':state,'count':int(r[state]),'denominator':int(r['total'])})
colors={'domain':['yes','partial','no','uncertain'],'range':['#23656c','#c79b36','#e3dfd4','#859398']}
save('2-shared-preconditions',rows,{'title':{'text':'Different routes supplied different constraints','subtitle':'20 selected historical recoveries; judgement codes, not a representative statistical sample'},'height':240,'mark':{'type':'bar','height':26},'encoding':{'x':{'field':'count','type':'quantitative','stack':'zero','axis':{'title':'Cases','tickMinStep':1}},'y':{'field':'condition','type':'nominal','sort':None,'axis':{'title':None,'labelLimit':260}},'color':{'field':'state','type':'nominal','scale':colors,'title':'Evidence code'},'order':{'field':'state','sort':'ascending'},'tooltip':[{'field':'condition'},{'field':'state'},{'field':'count','type':'quantitative'},{'field':'denominator','type':'quantitative'}]}})
rows=[r for r in read('3-preconditions-matrix.csv') if r['group']=='open']
# Short display headings retain an exact meaning in the CSV and tooltip.
short={'Bilingual / partial parallel':'Parallel','Target identified at outset':'Known target','Usable known linguistic comparator':'Comparator','Broad script type before mapping':'Script type','Proper names as entry point':'Names'}
for r in rows:r['heading']=short[r['condition']]
save('3-open-preconditions',rows,{'title':{'text':'The remaining gaps differ by case','subtitle':'Present evidence for 22 open or partial cases; full cell evidence and dated corpus notes in the CSVs'},'height':660,'mark':{'type':'rect','stroke':'#fffdf8','strokeWidth':2},'encoding':{'x':{'field':'heading','type':'ordinal','sort':list(short.values()),'axis':{'title':None,'labelAngle':0,'labelFontSize':11}},'y':{'field':'case','type':'ordinal','sort':None,'axis':{'title':None,'labelLimit':235}},'color':{'field':'state','type':'nominal','scale':colors,'title':'Evidence code'},'tooltip':[{'field':'case'},{'field':'condition'},{'field':'state'},{'field':'source_ids'}]}})
rows=read('4-agent-ranking.csv')
for r in rows:
 for key in ['total','corpus','digital','language','anchors','tests','verification','language_double_total']:r[key]=int(r[key])
save('4-agent-priorities',rows,{'title':{'text':'Agent priorities for checkable gains','subtitle':'Ordinal literature-based judgement, /18; Vinča comparator shown but excluded from the rank'},'height':630,'mark':{'type':'bar','color':'#23656c','height':17},'encoding':{'x':{'field':'total','type':'quantitative','scale':{'domain':[0,18]},'axis':{'title':'Six criteria, each scored 0–3','tickMinStep':1}},'y':{'field':'case','type':'nominal','sort':[r['case'] for r in rows],'axis':{'title':None,'labelLimit':235}},'tooltip':[{'field':'case'},{'field':'rank'},{'field':'total','type':'quantitative'},{'field':'language_double_rank'},{'field':'status'},{'field':'agent_loop'}]}})
print('Rendered four charts; every PNG has its exact plotted CSV and Vega-Lite spec.')
