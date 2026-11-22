"""Recalculate the snack's milestone table, provenance export and EU distribution.

Inputs are original human-coded route records, selected school baselines and the
limited EU database snapshot. This checks arithmetic, joins and provenance; it
cannot decide the meaning or validity of a regulation.
"""
from pathlib import Path
import csv, json, sys
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'
def read(name):
    with (DATA/name).open(newline='') as f:return list(csv.DictReader(f))
def write(name,fields,rows):
    with (out/name).open('w',newline='') as f:
        w=csv.writer(f,lineterminator='\n');w.writerow(fields);w.writerows(rows)
def number(n):return format(n,'.12g')
if __name__=='__main__':
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
    model=json.loads((DATA/'route-coding.json').read_text())
    schools={r['school_id']:r for r in read('school-baselines.csv')}
    visual=json.loads((DATA/'visual-annotations.json').read_text())
    rows=[];milestones=[];seen=set()
    fields=['jurisdiction','stage_id','stage','kind','start_months_after_school','end_months_after_school','duration_basis','start_years_after_age18','end_years_after_age18','start_years_after_primary_entry','end_years_after_primary_entry','source_ids','source_passages','source_dates','source_urls','accessed_dates','reading_depth','note']
    for route in model['routes']:
        school=schools[route['school_id']];age=int(school['school_leaving_age']);years=int(school['school_years'])
        for s in route['stages']:
            assert s['id'] not in seen;sources=[model['sources'][k]for k in s['sources']];seen.add(s['id'])
            assert 0<=s['start']<=s['end'] and all(x['passage'] and x['accessed'] and x['source_date'] for x in sources)
            rows.append([route['label'],s['id'],s['label'],s['kind'],s['start'],s['end'],s['duration_basis'],number(age-18+s['start']/12),number(age-18+s['end']/12),number(years+s['start']/12),number(years+s['end']/12),' | '.join(s['sources']),*[' | '.join(str(x[k])for x in sources)for k in ['passage','source_date','url','accessed','reading']],s['note']])
        first=next(s for s in route['stages']if s['kind']=='first_registration')
        full=next(s for s in route['stages']if s['kind']=='full_registration')
        family_id={'california':'ca-family-ready','england':'en-gp-ready','bavaria':'de-gp-ready','japan':'jp-gp-ready','india':'in-family-ready','singapore':'sg-family-ready'}[route['id']]
        family=next(s for s in route['stages']if s['id']==family_id)
        assert visual['milestones'][route['id']]==[first['id'],full['id'],family['id']]
        milestones.append([route['label'],first['start'],full['start'],family['start'],family['label'],age,years,first['id'],full['id'],family['id']])
    write('stages.csv',fields,rows)
    write('milestones.csv',['jurisdiction','first_registration_month','general_licence_month','family_training_month','family_endpoint','modelled_medical_entry_age','school_years','first_stage_id','general_stage_id','family_stage_id'],milestones)
    eu=read('eu-basic-medical-duration.csv')
    current=[r for r in eu if r['education_unit']=='year' and r['archived']=='False']
    write('eu-duration-distribution.csv',['education_years','jurisdictions'],[[n,sum(float(r['education_value'])==n for r in current)]for n in [5,6,7]])
    assert len(eu)==32 and len(current)==26
    assert len(seen)==55 and len(schools)==6
    assert set(visual['stages'])<=seen
    assert set(visual['sources'])==set(model['sources'])
    print('Rebuilt 55 stages, six matched milestone rows and EU distribution (26 of 32 records).')
