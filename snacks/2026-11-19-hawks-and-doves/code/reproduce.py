"""Recount saved semantic annotations; this does not independently validate them."""
import csv,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=Path(sys.argv[1]);OUT.mkdir(parents=True,exist_ok=True)
def read(name):return list(csv.DictReader((ROOT/'data'/name).open()))
def write(name,rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
r=read('annotations.csv')
assert len(r)==492 and len({x['id'] for x in r})==492
assert all(x['human_validated']=='0' for x in r)
for prefix,n in [('H',111),('S',160),('P',221)]:assert sum(x['id'].startswith(prefix) for x in r)==n
for x in r:
 assert int(x['elaboration'])<=int(x['political'])
 assert int(x['hawk_chases_dove'])<=int(x['elaboration'])
 assert len(x['context_sha256'])==64
sources=sorted({x['source'] for x in r})
def aggregate(rr,source,decade=None):
 p=sum(int(x['political']) for x in rr);e=sum(int(x['elaboration']) for x in rr)
 d={'source':source}
 if decade is not None:d['decade']=decade
 d.update(retrieved_units=len(rr),political_units=p,elaborated_units=e,chasing_doves=sum(int(x['hawk_chases_dove']) for x in rr),killing_or_eating_doves=sum(int(x['hawk_kills_or_eats_dove']) for x in rr),elaboration_share_percent=f'{100*e/p:.1f}' if p else '')
 return d
write('source-totals.csv',[aggregate([x for x in r if x['source']==s],s) for s in sources])
write('source-decades.csv',[aggregate([x for x in r if x['source']==s and x['decade']==d],s,d) for s in sources for d in sorted({x['decade'] for x in r if x['source']==s})])
s=[x for x in r if x['id'].startswith('S')]
write('news-sample.csv',[{'decade':d,'category':c,'count':sum(1 for x in s if x['decade']==d and ('Other sense' if x['political']=='0' else 'Bird elaboration' if x['elaboration']=='1' else 'Conventional policy use')==c),'all_lexical_hits_in_decade':sum(x['decade']==d for x in s),'political_hits_in_decade':sum(int(x['political']) for x in s if x['decade']==d)} for d in sorted({x['decade'] for x in s}) for c in ['Other sense','Conventional policy use','Bird elaboration']])
write('news-domains.csv',[{'domain':d,'policy_tokens':sum(x['domain']==d for x in s if x['political']=='1'),'elaborated_tokens':sum(int(x['elaboration']) for x in s if x['domain']==d),'policy_sample_denominator':sum(int(x['political']) for x in s)} for d in ['monetary','fiscal_or_price','other_policy']])
ng=read('ngram-series.csv');write('ngram-decades.csv',[{'decade':str(d)+'s','phrase':p,'mean_frequency_per_billion_ngrams':f"{sum(float(x['frequency_per_billion_ngrams']) for x in ng if x['phrase']==p and d<=int(x['year'])<d+10)/10:.6f}",'political_sense_denominator':'unavailable'} for d in range(1900,2020,10) for p in sorted({x['phrase'] for x in ng})])
print('Recounted 492 saved judgements; no API calls or new semantic decisions.')

status=read('ngram-query-status.csv')
assert len(status)==7
observed={x['phrase'] for x in ng}
assert all((x['status']=='series_returned')==(x['phrase'] in observed) for x in status)
write('ngram-query-summary.csv',[{'queries':len(status),'series_returned':len(observed),'no_series_returned':len(status)-len(observed),'political_sense_denominator':'unavailable'}])
negative=__import__('json').loads((ROOT/'data/predation-query.json').read_text())
assert negative['finished']==1 and negative['concsize']==0 and negative['Lines']==[]
