"""Shared offline calculations. Saved judgements are inputs, never reclassified here."""
from collections import Counter, defaultdict
import csv
import json
from pathlib import Path
import runpy
import shutil
import sys


def read(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f))


def write(path, fields, rows):
    with path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)


def run(path, *args):
    previous = sys.argv
    try:
        sys.argv = [str(path), *map(str, args)]
        runpy.run_path(str(path), run_name='__main__')
    finally:
        sys.argv = previous


def pace(data, out):
    dists = defaultdict(dict)
    for r in read(data/'distribution-shares.csv'):
        dists[r['measure'], int(r['year'])][r['code']] = float(r['share'])
    years = sorted(y for m,y in dists if m=='occupations_D')
    pairs = list(zip(years, years[1:])) + [(1900, 1970), (1960, 2024), (1950, 2024), (1900, 1960), (1970, 2024)]
    rows=[]
    for a,b in pairs:
        row={'from':a,'to':b,'years':b-a}
        for measure in ['occupations_D','industries_D','occupation_groups_D','sectors_D']:
            aa,bb=dists[measure,a],dists[measure,b]
            row[measure]=round(50*sum(abs(aa.get(k,0)-bb.get(k,0)) for k in sorted(set(aa)|set(bb))),1)
        rows.append(row)
    write(out/'dissimilarity.csv',list(rows[0]),rows)
    cnt = defaultdict(dict)
    for r in read(data/'robustness-counts.csv'):
        cnt[r['scheme'], int(r['year'])][r['code']] = float(r['workers'])
    years = sorted(y for (v, y) in cnt if v == 'OCC1990')
    pairs = list(zip(years, years[1:])) + [(1900,1970),(1960,2024),(1950,2024)]
    def dis(v, a, b):
        aa, bb = cnt[v,a], cnt[v,b]
        if not aa or not bb: return float('nan')
        ta, tb = sum(aa.values()), sum(bb.values())
        return round(50*sum(abs(aa.get(k,0)/ta-bb.get(k,0)/tb) for k in set(aa)|set(bb)),1)
    rows = [{'from':a,'to':b,'years':b-a,'occ1990_D':dis('OCC1990',a,b),'occ2010_D':dis('OCC2010',a,b),
             'occ1990_categories_used_from':len(cnt['OCC1990',a]),'occ1990_categories_used_to':len(cnt['OCC1990',b])} for a,b in pairs]
    write(out/'dissimilarity_robustness.csv',list(rows[0]),rows)
    totals = {int(r.pop('year')):{k:float(v) for k,v in r.items()} for r in read(data/'indicator-counts.csv')}
    measures = [
        ('Workers in labour force (millions)', 'lf', None),
        ('Women as share of the labour force (%)','lf_women','lf'),
        ('Married women 16-64 in the labour force (%)','mw_lf','mw'),
        ('Population living on farms (%)','farm_pop','pop'),
        ('Workers self-employed (%)','self','cw_cl'),
        ('Teenagers 14-17 in school (%)','teens_school','teens'),
        ('Population born abroad (%)','foreign','pop')]
    years = sorted(totals)
    rows=[]
    for label,num,den in measures:
        row={'indicator':label}
        for y,t in sorted(totals.items()):
            row[str(y)] = round(t[num]/1e6,2) if den is None else round(100*t[num]/t[den],2) if t[den] else ''
        rows.append(row)
    write(out/'indicators.csv',['indicator']+list(map(str,years)),rows)
    rows = [{'year':r['year'],'pct':round(100*float(r['graduates'])/float(r['adults']),2)} for r in read(data/'college-counts.csv')]
    write(out/'college.csv',['year','pct'],rows)
    # Use full precision saved responses, not rounded plotted series.
    ts={}
    for line in (data/'ngram-responses.jsonl').read_text().splitlines():
        for s in json.loads(line)['response']:
            name=s['ngram'].replace(' (All)','').lower()
            if name in ts and '(All)' not in s['ngram']: continue
            ts[name]=s['timeseries']
    # The query lists are fixed in the archived output's group/title columns.
    rows=[]
    for r in read(data/'ngram_takeoff.csv'):
        s=ts.get(r['title'].lower(),[]); peak=max(s,default=0)
        rows.append({'group':r['group'],'title':r['title'],
                     'take_off_year':next((1880+i for i,v in enumerate(s) if v>=peak/10),'') if peak else '',
                     'peak_year':1880+s.index(peak) if peak else '', 'peak_per_billion':round(peak*1e9,1) if peak else 0})
    write(out/'ngram_takeoff.csv',list(rows[0]),rows)
    for name in ['dissimilarity.csv','indicators.csv','college.csv','ngram_takeoff.csv']:
        shutil.copy(out/name,data/name)


def sickly(data, out):
    food=read(data/'food-annotations.csv')
    counts=Counter((r['construction'],r['coordination']) for r in food)
    labels={'attributive':'Attributive','explicit verbal complement':'Explicit verbal complement','elliptical/supplementary':'Ellipsis or supplement'}
    rows=[{'construction':label,'coordination':'Sole adjective' if coord=='sole' else 'Coordinated','cases':counts[key,coord]}
          for key,label in labels.items() for coord in ['sole','coordinated']]
    write(out/'1-sickly-food-constructions.csv',list(rows[0]),rows)
    rows=[{**r,'per_million':round(int(r['hits'])/int(r['words'])*1e6,3)} for r in read(data/'corpus-totals.csv')]
    write(out/'corpus-rates.csv',list(rows[0]),rows)
    examples=read(data/'example-locators.csv')
    rows=[{'corpus':c,'curated_examples':n} for c,n in sorted(Counter(r['corpus'] for r in examples).items())]
    write(out/'example-counts.csv',list(rows[0]),rows)
    # Check association formulae against provider counts and published scores.
    import math
    rows=[]
    for corpus,total,node in [('bnc',112181015,218),('oanc',12739019,12)]:
        meta=json.loads((data/'collocation-denominators.json').read_text())[corpus]
        total,node=meta['tokens'],meta['node_hits']
        for word,pair,candidate,t,mi,dice in json.loads((data/f'collocations-{corpus}.json').read_text()):
            expected= node*candidate/total
            actual=[(pair-expected)/math.sqrt(pair),math.log2(pair/expected),14+math.log2(2*pair/(node+candidate))]
            for a,b in zip(actual,[t,mi,dice]):
                if abs(a-b)>0.00002: raise ValueError(f'{corpus}: score differs for {word}')
            rows.append({'corpus':corpus,'collocate':word,'pair_count':pair,'candidate_count':candidate,
                         't_score':round(actual[0],5),'mi':round(actual[1],5),'logdice':round(actual[2],5)})
    write(out/'association-scores.csv',list(rows[0]),rows)


def reproduce(snack, output):
    snack=Path(snack); output=Path(output); output.mkdir(parents=True,exist_ok=True)
    data=output/'data'; shutil.copytree(snack/'data',data)
    charts=output/'charts'; charts.mkdir()
    if snack.name.endswith('one-in-270-jobs'):
        run(snack/'code/interactive.py',output)
        rows=read(data/'occ1950_1950_vs_2010.csv')
        trends=read(data/'occ1990_by_year.csv')
        gone={761,365,360,325,542,520,960,631,785,304,752,751,645,501,525,571}
        values=[('1950 categories',len(rows)),('Zero in 2010',sum(int(r['emp2010'])==0 for r in rows)),
                ('Judged gone or nearly gone',len(gone)),
                ('Reclassification zeros',sum(int(r['emp2010'])==0 and int(r['occ1950']) not in gone for r in rows)),
                ('Employed 1950',sum(int(r['1950']) for r in trends)),('Employed 2010',sum(int(r['2010']) for r in trends))]
        write(output/'page-summary.csv',['measure','value'],[{'measure':k,'value':v} for k,v in values])
    elif snack.name.endswith('pace-of-change-1900-2026'):
        pace(data,output)
        run(snack/'code/charts.py',output)
    elif snack.name.endswith('can-a-cake-be-sickly'):
        sickly(data,output)
    elif snack.name.endswith('ai-wealth-control-2035'):
        run(snack/'code/analyse.py','--entry',output)
    else:
        raise ValueError('Unknown snack')
    for f in charts.glob('*.csv'): shutil.copy(f,output/f.name)
