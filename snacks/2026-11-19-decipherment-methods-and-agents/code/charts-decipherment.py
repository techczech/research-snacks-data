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
 spec={'$schema':'https://vega.github.io/schema/vega-lite/v5.json','background':'#fffdf8','width':480,'config':{'font':'Arial','axis':{'labelFontSize':16,'titleFontSize':16,'gridColor':'#e2dfd5'},'title':{'fontSize':18,'anchor':'start','subtitleFontSize':16,'subtitleColor':'#4c5556'},'view':{'stroke':None},'legend':{'orient':'bottom','labelFontSize':16,'titleFontSize':16,'labelLimit':650}},'data':{'url':'charts/'+stem+'.csv'},**spec}
 colorfield=spec.get('encoding',{}).get('color',{}).get('field')
 if colorfield in ['state','task_group']:
  spec['params']=[{'name':'state_pick','select':{'type':'point','fields':[colorfield]},'bind':'legend'}]
  spec['encoding']['opacity']={'condition':{'param':'state_pick','value':1},'value':0.2}
 (C/(stem+'.vl.json')).write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n')
 png=copy.deepcopy(spec);png['width']=480;png['data']={'values':rows}
 (C/(stem+'.png')).write_bytes(vlc.vegalite_to_png(png,scale=2))
rows=read('1-timeline.csv')
for r in rows:r['year']=int(r['year'])
save('1-decipherment-timeline',rows,{'title':{'text':'Decipherment happened in stages','subtitle':'Selected milestones in 20 recoveries; a plotted date is not a date of complete understanding'},'height':550,'mark':{'type':'point','filled':True,'size':85,'color':'#23656c'},'encoding':{'x':{'field':'year','type':'quantitative','scale':{'domain':[1740,2005]},'axis':{'format':'d','title':'Year of selected milestone','tickCount':8}},'y':{'field':'case','type':'nominal','sort':[r['case'] for r in rows],'axis':{'title':None,'labelLimit':240}},'tooltip':[{'field':'case'},{'field':'year','type':'quantitative','format':'d'},{'field':'milestone'},{'field':'people'}]}})
rows=[]
for r in read('2-preconditions-counts.csv'):
 for state in ['yes','partial','no','uncertain']:rows.append({'condition':r['condition'],'state':state,'count':int(r[state]),'denominator':int(r['total'])})
colors={'domain':['yes','partial','no','uncertain'],'range':['#23656c','#c79b36','#e3dfd4','#859398']}
save('2-shared-preconditions',rows,{'title':{'text':'What the decipherers had to work with','subtitle':'Provisional coding by one compiler; selected dependent stages'},'height':340,'mark':{'type':'bar','height':26},'encoding':{'x':{'field':'count','type':'quantitative','stack':'zero','axis':{'title':'Cases','tickMinStep':1}},'y':{'field':'condition','type':'nominal','sort':None,'axis':{'title':None,'labelLimit':260}},'color':{'field':'state','type':'nominal','scale':colors,'title':'Evidence code'},'order':{'field':'state','sort':'ascending'},'tooltip':[{'field':'condition'},{'field':'state'},{'field':'count','type':'quantitative'},{'field':'denominator','type':'quantitative'}]}})
rows=[r for r in read('3-preconditions-matrix.csv') if r['group']=='open']
# Authored column labels; no semantic inference from source text.
short={'Readable parallel or key':'Parallel/key','Language or close relative documented at stage':'Documented','Language proposed for inscriptions before breakthrough':'Proposed','Usable known linguistic comparator at stage':'Comparator','Broad script type before mapping':'Script type','Proper names as entry point':'Names'}
for r in rows:r['heading']=short[r['condition']]
save('3-open-preconditions',rows,{'title':{'text':'Different gaps remain','subtitle':'Present resources in open/partial and comparison cases'},'height':900,'mark':{'type':'rect','stroke':'#fffdf8','strokeWidth':2},'encoding':{'x':{'field':'heading','type':'ordinal','sort':list(short.values()),'axis':{'title':None,'labelAngle':-35,'labelFontSize':16}},'y':{'field':'case','type':'ordinal','sort':None,'axis':{'title':None,'labelLimit':220}},'color':{'field':'state','type':'nominal','scale':colors,'title':'Evidence code'},'tooltip':[{'field':'case'},{'field':'condition'},{'field':'state'},{'field':'source_ids'}]}})
rows=[r for r in read('8-task-groups.csv') if r['group_id']!='excluded']
groups=['Structure without language','Partly read, with a language to test against','Audit of a published proposal','Script readable, language not understood','Language known, individual signs unread','Limited by evidence']
rows=sorted(rows,key=lambda r:(groups.index(r['task_group']),r['case']))
# A categorical matrix replaces the score bars; neither axis is a numerical priority.
save('4-agent-priorities',rows,{'title':{'text':'Different tasks need different checks','subtitle':'Unordered within each group; no estimate of decipherment prospects'},'height':1000,'mark':{'type':'point','filled':True,'size':130},'encoding':{'x':{'field':'task_group','type':'nominal','sort':groups,'axis':None},'y':{'field':'case','type':'nominal','sort':[r['case'] for r in rows],'axis':{'title':None,'labelLimit':250}},'color':{'field':'task_group','type':'nominal','scale':{'domain':groups,'range':['#23656c','#b47a1c','#3b78a0','#738c36','#a34c32','#68777b']},'title':'Kind of task','legend':{'columns':1,'labelLimit':650}},'tooltip':[{'field':'case'},{'field':'task_group'},{'field':'checkable_result'},{'field':'obstacle'}]}})
print('Rendered four charts; every PNG has its exact plotted CSV and Vega-Lite spec.')
