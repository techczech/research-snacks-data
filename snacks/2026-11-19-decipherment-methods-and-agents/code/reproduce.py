"""Recalculate a literature-coded survey. Does not certify the underlying historical judgements.
Usage: python code/reproduce.py OUTPUT_DIRECTORY
Uses only the Python standard library and the committed data/ files. No network calls.
"""
import csv
from collections import Counter
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
CONDITIONS={
 'bilingual':'Bilingual / partial parallel',
 'language_known':'Prior target identity / continuity',
 'related_language_known':'Usable known linguistic comparator',
 'script_type_known':'Broad script type before mapping',
 'proper_names':'Proper names as entry point',
}
SCORES=['corpus','digital','language','anchors','tests','verification']

def read(path):
 with path.open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
def write(out,name,rows):
 assert rows,name
 with (out/name).open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator="\n");w.writeheader();w.writerows(rows)

def main(out):
 out.mkdir(parents=True,exist_ok=True)
 cases=read(ROOT/'data/decipherment-cases.csv')
 evidence=read(ROOT/'data/decipherment-cell-evidence.csv')
 sources=read(ROOT/'data/decipherment-sources.csv')
 sourceids={s['source_id'] for s in sources}
 assert len(sourceids)==len(sources),'Duplicate source IDs'
 assert len({c['case_id'] for c in cases})==len(cases),'Duplicate case IDs'
 byid={c['case_id']:c for c in cases}
 for e in evidence:
  assert e['case_id'] in byid
  assert e['value']==byid[e['case_id']][e['field']],('Evidence/cell mismatch',e['case_id'],e['field'])
  assert set(e['source_ids'].split(';'))<=sourceids
 for c in cases:
  assert set(c['source_ids'].split(';'))<=sourceids
  for field in CONDITIONS:
   assert c[field] in {'yes','partial','no','uncertain'},(c['case_id'],field,c[field])
   assert any(e['case_id']==c['case_id'] and e['field']==field for e in evidence)
   if c['group']=='historical':
    assert any(e['case_id']==c['case_id'] and e['field']==field and e['annotation_level']=='individual rationale' for e in evidence),'Headline cell lacks individual rationale'
  if c['group']=='open':
   strength=int(c['score_language'])
   assert c['related_language_known']==('no' if strength==0 else 'yes' if strength==3 else 'partial'),('Comparator matrix/rubric contradiction',c['case_id'])
   for criterion in SCORES:
    assert any(e['case_id']==c['case_id'] and e['field']=='score_'+criterion and e['annotation_level']=='individual rationale' for e in evidence),'Score lacks individual rationale'
 hist=[c for c in cases if c['group']=='historical']
 opened=[c for c in cases if c['group']=='open']
 counts=[]
 for field,label in CONDITIONS.items():
  n=Counter(c[field] for c in hist)
  counts.append(dict(condition=label,yes=n['yes'],partial=n['partial'],no=n['no'],uncertain=n['uncertain'],total=len(hist)))
 write(out,'2-preconditions-counts.csv',counts)
 timeline=[dict(case=c['case'],year=int(c['year']),milestone=c['year_label'],people=c['who'],bilingual=c['bilingual'],source_ids=c['source_ids']) for c in sorted(hist,key=lambda x:(int(x['year']),x['case_id']))]
 write(out,'1-timeline.csv',timeline)
 matrix=[]
 for c in cases:
  for f,label in CONDITIONS.items():matrix.append(dict(case=c['case'],group=c['group'],condition=label,state=c[f],source_ids=c['source_ids']))
 write(out,'3-preconditions-matrix.csv',matrix)
 rankable=[c for c in opened if c['case_id']!='vinca']
 def score(c,double=False):
  vals=[int(c['score_'+f]) for f in SCORES]
  assert all(0<=x<=3 for x in vals),(c['case'],vals)
  return sum(vals)+(vals[2] if double else 0)
 def order(c,double=False):return (-score(c,double),-int(c['score_digital']),-int(c['score_verification']),c['case_id'])
 # Rank within task cohorts. A known Chinese/Jurchen/Etruscan character/word gap
 # is not placed ahead of an unknown-script problem merely because it has keys.
 cohorts=['undeciphered_or_partial','readable_with_gaps']
 base=[];rbase={};ralt={}
 for cohort in cohorts:
  selected=[c for c in rankable if c['priority_group']==cohort]
  ordered=sorted(selected,key=order);alternative=sorted(selected,key=lambda c:order(c,True))
  base+=ordered
  rbase.update({c['case_id']:i+1 for i,c in enumerate(ordered)})
  ralt.update({c['case_id']:i+1 for i,c in enumerate(alternative)})
 ranking=[]
 for c in base+[c for c in opened if c['case_id']=='vinca']:
  ranking.append(dict(rank=rbase.get(c['case_id'],'excluded'),case=c['case'],priority_group=c['priority_group'],**{s:int(c['score_'+s]) for s in SCORES},total=score(c),language_double_total=score(c,True),language_double_rank=ralt.get(c['case_id'],'excluded'),status=c['status'],agent_loop=c['agent_loop'],method_cannot_supply=c['method_cannot_supply'],source_ids=c['source_ids']))
 write(out,'4-agent-ranking.csv',ranking)
 corpusfields=['case','status','corpus_inscriptions','sign_tokens','distinct_signs','longest_text','corpus_snapshot','dataset','dataset_licence','candidate_languages','bilingual','blocker','source_ids']
 write(out,'5-corpus-availability.csv',[{f:c[f] for f in corpusfields} for c in opened])
 # Logical counterexamples, not a search over all writing systems in history.
 claims=[]
 tests=[
 ('Every success needed a full bilingual',lambda c:c['bilingual']!='yes'),
 ('Every target language was independently known before recovery',lambda c:c['language_known']=='no'),
 ('Every success had a known linguistic relative/comparator',lambda c:c['related_language_known']=='no'),
 ('No success lacked both a parallel and a known linguistic comparator',lambda c:c['bilingual']=='no' and c['related_language_known']=='no')]
 for claim,test in tests:
  counter=[c['case'] for c in hist if test(c)]
  claims.append(dict(claim=claim,counterexamples_in_selected_sample=len(counter),cases='; '.join(counter),scope=str(len(hist))+' selected recoveries; partial and uncertain codes need separate reading; no universal proof'))
 write(out,'6-claim-tests.csv',claims)
 write(out,'7-survey-size.csv',[dict(group='historical recoveries',rows=len(hist)),dict(group='open/partial/comparator cases',rows=len(opened)),dict(group='ranked open/partial cases',rows=len(rankable)),dict(group='computational works',rows=len(read(ROOT/'data/decipherment-computational-work.csv'))),dict(group='source records',rows=len(sources)),dict(group='cell evidence records',rows=len(evidence))])
 print('Rebuilt seven tables from explicit literature coding; historical validity is outside this calculation check.')
if __name__=='__main__':main(Path(sys.argv[1]))
