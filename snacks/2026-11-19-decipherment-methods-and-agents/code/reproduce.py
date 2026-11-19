"""Recalculate frozen literature judgements; does not certify them. Standard library only.
Usage: python code/reproduce.py OUTPUT_DIRECTORY
"""
import csv
from collections import Counter
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
CONDITIONS={
 'bilingual':'Readable parallel or key',
 'language_documented':'Language or close relative documented at stage',
 'language_proposed':'Language proposed for inscriptions before breakthrough',
 'related_language_known':'Usable known linguistic comparator at stage',
 'script_type_known':'Broad script type before mapping',
 'proper_names':'Proper names as entry point',
}
SCORES=['corpus','digital','language','anchors','tests','verification']
def read(path):
 with path.open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
def write(out,name,rows):
 assert rows,name
 with (out/name).open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def main(out):
 out.mkdir(parents=True,exist_ok=True)
 cases=read(ROOT/'data/decipherment-cases.csv'); evidence=read(ROOT/'data/decipherment-cell-evidence.csv')
 sources=read(ROOT/'data/decipherment-sources.csv'); sourceids={s['source_id'] for s in sources}
 assert len(sourceids)==len(sources),'Duplicate source IDs'
 byid={c['case_id']:c for c in cases};assert len(byid)==len(cases),'Duplicate case IDs'
 for e in evidence:
  assert e['case_id'] in byid
  assert e['value']==byid[e['case_id']][e['field']],('Evidence/cell mismatch',e['case_id'],e['field'])
  assert set(e['source_ids'].split(';'))<=sourceids
 for c in cases:
  assert set(c['source_ids'].split(';'))<=sourceids
  for field in CONDITIONS:
   assert c[field] in {'yes','partial','no','uncertain'},(c['case_id'],field,c[field])
   matches=[e for e in evidence if e['case_id']==c['case_id'] and e['field']==field]
   assert matches,('Missing evidence',c['case_id'],field)
   if c['group']=='historical':assert any(e['annotation_level']=='individual rationale' for e in matches)
  if c['group']=='open':
   strength=c['score_language']
   if strength!='not audited':assert c['related_language_known']==('no' if int(strength)==0 else 'yes' if int(strength)==3 else 'partial'),c['case_id']
   for s in SCORES:
    assert c['score_'+s]=='not audited' or 0<=int(c['score_'+s])<=3
    assert any(e['case_id']==c['case_id'] and e['field']=='score_'+s and e['annotation_level']=='individual rationale' for e in evidence)
 hist=[c for c in cases if c['group']=='historical'];opened=[c for c in cases if c['group']=='open']
 assert len(hist)==20,'Locked historical sample changed'
 counts=[]
 for field,label in CONDITIONS.items():
  n=Counter(c[field] for c in hist);counts.append(dict(condition=label,yes=n['yes'],partial=n['partial'],no=n['no'],uncertain=n['uncertain'],total=len(hist)))
 write(out,'2-preconditions-counts.csv',counts)
 write(out,'1-timeline.csv',[dict(case=c['case'],year=int(c['year']),milestone=c['year_label'],people=c['who'],bilingual=c['bilingual'],selected_stage=c['selected_stage'],used_later=c['used_later_in_recovery'],source_ids=c['source_ids']) for c in sorted(hist,key=lambda x:(int(x['year']),x['case_id']))])
 write(out,'3-preconditions-matrix.csv',[dict(case=c['case'],group=c['group'],condition=label,state=c[f],selected_stage=c['selected_stage'],source_ids=c['source_ids']) for c in cases for f,label in CONDITIONS.items() if c['group']=='historical' or f not in {'language_documented','language_proposed'}])
 def total(c,double=False):
  values=[c['score_'+f] for f in SCORES]
  return 'not audited' if 'not audited' in values else sum(map(int,values))+(int(c['score_language']) if double else 0)
 write(out,'4-agent-ranking.csv',[dict(case=c['case'],task_group=c['priority_group'],**{s:c['score_'+s] for s in SCORES},total=total(c),language_double_total=total(c,True),language_condition=c['language_condition'],status=c['status'],source_ids=c['source_ids']) for c in sorted(opened,key=lambda c:(c['priority_group'],c['case_id']))])
 corpusfields=['case','status','corpus_inscriptions','sign_tokens','distinct_signs','longest_text','corpus_snapshot','dataset','dataset_licence','candidate_languages','bilingual','blocker','source_ids']
 write(out,'5-corpus-availability.csv',[{f:c[f] for f in corpusfields} for c in opened])
 tests=[('Every success needed a full readable parallel',lambda c:c['bilingual']!='yes'),('Every success had a documented language or close relative at the stage',lambda c:c['language_documented']=='no'),('Every success had a usable known linguistic comparator',lambda c:c['related_language_known']=='no'),('No success lacked both a parallel/key and a known linguistic comparator',lambda c:c['bilingual']=='no' and c['related_language_known']=='no')]
 claims=[]
 for claim,test in tests:
  counter=[c['case'] for c in hist if test(c)];claims.append(dict(claim=claim,counterexamples_in_selected_sample=len(counter),cases='; '.join(counter),scope='20 selected dependent language recoveries; provisional coding; no universal proof'))
 write(out,'6-claim-tests.csv',claims)
 tasks=read(ROOT/'data/decipherment-task-groups.csv')
 for t in tasks:assert t['case_id'] in byid and set(t['source_ids'].split(';'))<=sourceids
 write(out,'8-task-groups.csv',tasks)
 write(out,'9-historical-lineages.csv',[dict(case=c['case'],lineage=c['lineage'],selected_stage=c['selected_stage'],source_ids=c['source_ids']) for c in hist])
 write(out,'7-survey-size.csv',[dict(group='historical recoveries',rows=len(hist)),dict(group='interpretive lineage clusters',rows=len({c['lineage'] for c in hist})),dict(group='open/partial/comparison cases',rows=len(opened)),dict(group='task records including residual Maya/Tangut',rows=len(tasks)),dict(group='computational works',rows=len(read(ROOT/'data/decipherment-computational-work.csv'))),dict(group='source records',rows=len(sources)),dict(group='cell evidence records',rows=len(evidence))])
 print('Rebuilt nine tables from authored cells; arithmetic verified, historical judgements not independently validated.')
if __name__=='__main__':main(Path(sys.argv[1]))
