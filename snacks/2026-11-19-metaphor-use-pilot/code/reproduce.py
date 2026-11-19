"""Recount frozen model judgements; never classify language algorithmically.
Run: python code/reproduce.py OUTPUT_DIR. Standard-library only; no network.
"""
import csv,json,sys
from collections import Counter
from pathlib import Path
R=Path(__file__).resolve().parents[1]
O=Path(sys.argv[1]);O.mkdir(parents=True,exist_ok=True)
texts=json.loads((R/'data/pilot-texts.json').read_text())
units=list(csv.DictReader((R/'data/pilot-units.csv').open()))
uid={u['unit_id']:u for u in units}
labels={}
allowed={'identification':{'M','L','U'},'cognitive':{'constitutive','attributive','mixed','uncertain'},'elaboration':{'explanative','generative','uncertain','na'},'social':{'declarative','figurative','innovative','exegetic','prevaricative','performative','uncertain'},'binding':{'none','anaphoric','cataphoric','exophoric','uncertain'},'scope':{'local','passage','uncertain'}}
for p in ['a','b']:
 raw=json.loads((R/f'data/pass-{p}.json').read_text())
 assert raw['read_all_units'] and raw['all_unlisted_units']=='L'
 assert len({r['unit_id'] for r in raw['records']})==len(raw['records'])
 labels[p]={u['unit_id']:{'identification':'L'} for u in units}
 for r in raw['records']:
  assert r['unit_id'] in uid
  assert r['confidence'] in {'high','medium','low'}
  assert r['basic_meaning'] and r['contextual_meaning'] and r['evidence']
  for f,a in allowed.items():
   assert set(r[f].split('|'))<=a,(p,r['unit_id'],f,r[f])
   if f in {'social','binding'}:r[f]='|'.join(sorted(r[f].split('|')))
  labels[p][r['unit_id']]=r
# Recreate deterministic unit segmentation independently from archived excerpt text.
import re,hashlib
for t in texts:
 assert hashlib.md5(t['text'].encode()).hexdigest()==t['md5']
 regenerated=[(m.start(),m.end(),m.group()) for m in re.finditer(r"[A-Za-z0-9]+(?:[’'\-][A-Za-z0-9]+)*",t['text'])]
 saved=[(int(u['start']),int(u['end']),u['word']) for u in units if u['text_id']==t['id']]
 assert regenerated==saved,t['id']
def write(name,rows,fields=None):
 with (O/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def stats(pairs):
 n=len(pairs);agree=sum(a==b for a,b in pairs)
 if not n:return n,agree,'',''
 ac=Counter(a for a,b in pairs);bc=Counter(b for a,b in pairs)
 pe=sum(ac[k]*bc[k] for k in ac|bc)/n**2
 return n,agree,f'{100*agree/n:.2f}',f'{((agree/n-pe)/(1-pe)):.4f}' if pe<1 else 'undefined'
rows=[]
for t in texts:
 ids=[u['unit_id'] for u in units if u['text_id']==t['id']]
 rows.append(dict(text_id=t['id'],genre=t['genre'],whitespace_tokens=len(t['text'].split()),units=len(ids),a_metaphor=sum(labels['a'][i]['identification']=='M' for i in ids),b_metaphor=sum(labels['b'][i]['identification']=='M' for i in ids),a_uncertain=sum(labels['a'][i]['identification']=='U' for i in ids),b_uncertain=sum(labels['b'][i]['identification']=='U' for i in ids),both_metaphor=sum(labels['a'][i]['identification']==labels['b'][i]['identification']=='M' for i in ids),identification_disagreements=sum(labels['a'][i]['identification']!=labels['b'][i]['identification'] for i in ids)))
write('corpus-summary.csv',rows)
common=[i for i in uid if labels['a'][i]['identification']==labels['b'][i]['identification']=='M']
metrics=[]
def metric(name,ids,field,tag=None):
 pairs=[]
 for i in ids:
  a,b=labels['a'][i][field],labels['b'][i][field]
  if tag is not None:a,b=str(tag in a.split('|')),str(tag in b.split('|'))
  pairs.append((a,b))
 n,agree,pct,k=stats(pairs)
 metrics.append(dict(dimension=name,n=n,agree=agree,disagree=n-agree,agreement_percent=pct,kappa=k))
metric('Identification (M/L/U)',list(uid),'identification')
metric('Identification (M/L; excludes any U)',[i for i in uid if 'U' not in (labels['a'][i]['identification'],labels['b'][i]['identification'])],'identification')
for field in ['cognitive','elaboration','social','binding','scope']:metric(field,common,field)
for field in ['social','binding']:
 for tag in sorted(allowed[field]):metric(field+': '+tag,common,field,tag)
write('agreement.csv',metrics)
conf=Counter((labels['a'][i]['identification'],labels['b'][i]['identification']) for i in uid)
write('identification-confusion.csv',[dict(pass_a=a,pass_b=b,units=conf[(a,b)]) for a in ['L','M','U'] for b in ['L','M','U']])
counts=[]
for field in ['cognitive','elaboration','social','binding','scope']:
 for tag in sorted(allowed[field]):
  for p in ['a','b']:
   matched=[i for i in uid if labels[p][i]['identification']=='M' and tag in labels[p][i][field].split('|')]
   docs={uid[i]['text_id'] for i in matched}
   counts.append(dict(dimension=field,category=tag,pass_id=p.upper(),units=len(matched),documents=len(docs)))
write('use-counts.csv',counts)
disagreements=[]
for i,u in uid.items():
 a,b=labels['a'][i],labels['b'][i]
 fields=['identification'] if a['identification']!=b['identification'] else []
 if a['identification']==b['identification']=='M':fields += [f for f in ['cognitive','elaboration','social','binding','scope'] if a[f]!=b[f]]
 if not fields:continue
 disagreements.append(dict(unit_id=i,text_id=u['text_id'],word=u['word'],dimensions='|'.join(fields),a_identification=a['identification'],b_identification=b['identification'],a_cognitive=a.get('cognitive','na'),b_cognitive=b.get('cognitive','na'),a_social=a.get('social','na'),b_social=b.get('social','na'),a_binding=a.get('binding','na'),b_binding=b.get('binding','na'),a_scope=a.get('scope','na'),b_scope=b.get('scope','na'),a_evidence=a.get('evidence','Not marked after full reading'),b_evidence=b.get('evidence','Not marked after full reading')))
write('disagreements.csv',disagreements,['unit_id','text_id','word','dimensions','a_identification','b_identification','a_cognitive','b_cognitive','a_social','b_social','a_binding','b_binding','a_scope','b_scope','a_evidence','b_evidence'])
# Chart data exactly equals the plotted rows. Exclude unused categories only on the bar chart.
common_counts=[]
for category in sorted(allowed['cognitive']):
 for p in ['a','b']:
  matched=[i for i in common if labels[p][i]['cognitive']==category]
  common_counts.append(dict(dimension='cognitive',category=category,pass_id=p.upper(),units=len(matched),documents=len({uid[i]['text_id'] for i in matched}),n=len(common)))
write('common-cognitive-counts.csv',common_counts)
write('1-cognitive-use.csv',common_counts)
chart2=[]
for r in metrics:
 if r['dimension'] not in ['cognitive','social: figurative','social','binding','scope']:continue
 names={'cognitive':'Cognitive use','social: figurative':'Figurative appeal','social':'Social label sets','binding':'Textual binding','scope':'Scope in excerpt'}
 chart2.append(dict(r,display=names[r['dimension']],label=f"{r['agreement_percent']}% · κ {r['kappa']}"))
write('2-agreement.csv',chart2)
write('pilot-totals.csv',[dict(units=len(uid),a_metaphor=sum(labels['a'][i]['identification']=='M' for i in uid),b_metaphor=sum(labels['b'][i]['identification']=='M' for i in uid),common_metaphor=len(common),union_metaphor=sum('M' in (labels['a'][i]['identification'],labels['b'][i]['identification']) for i in uid),disagreement_rows=len(disagreements))])
uncertain=[]
for p in ['a','b']:
 for i in uid:
  r=labels[p][i]
  if r['identification']=='U':uncertain.append(dict(pass_id=p.upper(),unit_id=i,word=uid[i]['word'],cognitive=r['cognitive'],elaboration=r['elaboration'],social=r['social'],binding=r['binding'],scope=r['scope']))
write('uncertain-annotations.csv',uncertain)
joint_u=[i for i in uid if labels['a'][i]['identification']==labels['b'][i]['identification']=='U']
import ast
calls=[]
for c in ast.walk(ast.parse((R/'code/annotate-metaphor-pass-a.py').read_text())):
 if isinstance(c,ast.Call) and isinstance(c.func,ast.Name) and c.func.id=='add' and len(c.args)<4 and not any(k.arg=='cognitive' for k in c.keywords):calls+=ast.literal_eval(c.args[0]).split()
audit={
 'whitespace_tokens':sum(len(t['text'].split()) for t in texts),
 'identification_disagreements_involving_U':sum(labels['a'][i]['identification']!=labels['b'][i]['identification'] and 'U' in (labels['a'][i]['identification'],labels['b'][i]['identification']) for i in uid),
 'identification_direct_M_L_disagreements':sum({labels['a'][i]['identification'],labels['b'][i]['identification']}=={'M','L'} for i in uid),
 'joint_U_units':len(joint_u),
 'joint_U_social_disagreements':sum(labels['a'][i]['social']!=labels['b'][i]['social'] for i in joint_u),
 'joint_U_binding_disagreements':sum(labels['a'][i]['binding']!=labels['b'][i]['binding'] for i in joint_u),
 'cognitive_A_constitutive_B_attributive':sum(labels['a'][i]['cognitive']=='constitutive' and labels['b'][i]['cognitive']=='attributive' for i in common),
 'cognitive_A_attributive_B_constitutive':sum(labels['a'][i]['cognitive']=='attributive' and labels['b'][i]['cognitive']=='constitutive' for i in common),
 'binding_none_none_agreements':sum(labels['a'][i]['binding']==labels['b'][i]['binding']=='none' for i in common),
 'binding_positive_link_agreements':sum(labels['a'][i]['binding']==labels['b'][i]['binding']!='none' for i in common),
 'social_both_declarative_only':sum(labels['a'][i]['social']==labels['b'][i]['social']=='declarative' for i in common),
 'social_both_declarative_exegetic':sum(labels['a'][i]['social']==labels['b'][i]['social']=='declarative|exegetic' for i in common),
 'figurative_marked_by_either':sum('figurative' in labels['a'][i]['social'].split('|') or 'figurative' in labels['b'][i]['social'].split('|') for i in common),
 'figurative_marked_by_both':sum('figurative' in labels['a'][i]['social'].split('|') and 'figurative' in labels['b'][i]['social'].split('|') for i in common),
 'pass_A_cognitive_default_units':len(calls)}
write('review-audit.csv',[dict(metric=k,units=v) for k,v in audit.items()])
print('Rebuilt 11 tables from two frozen annotation records; common M:',len(common))
