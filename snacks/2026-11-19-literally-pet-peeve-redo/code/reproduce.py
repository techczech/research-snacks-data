"""Rebuild page tables and plotted CSVs from saved inputs, without network or an API key.
Usage: python code/reproduce.py OUTPUT_DIRECTORY
This recounts recorded judgements; it does not validate their meanings.
"""
import csv,json,math,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'data';D=D/'public' if (D/'public').is_dir() else D
LABELS={'bnc':'BNC1994','spoken2014':'Spoken BNC2014','ententen':'enTenTen21'}
READINGS=['factual','figurative','metalinguistic','dual','uncertain','mention_or_error']
def readcsv(name):return list(csv.DictReader((D/name).open()))
def wilson(k,n):
 z=1.959963984540054;p=k/n;den=1+z*z/n;mid=(p+z*z/(2*n))/den;half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
 return round((mid-half)*100,3),round((mid+half)*100,3)
def generate():
 a=readcsv('literally-annotations.csv');assert len(a)==180 and len({x['sample_id'] for x in a})==180
 result={};rd=[];fc=[];bounds=[]
 for corpus,label in LABELS.items():
  x=[r for r in a if r['corpus']==corpus];assert len(x)==60
  for reading in READINGS:
   n=sum(r['reading']==reading for r in x);rd.append(dict(corpus=label,reading=reading,count=n,sample_size=60,percent=round(n/60*100,3)))
  for measure,field,target in [('Emphatic function','emphasis','yes'),('Clearly figurative reading','reading','figurative')]:
   k=sum(r[field]==target for r in x);lo,hi=wilson(k,60)
   fc.append(dict(corpus=label,measure=measure,count=k,sample_size=60,percent=round(k/60*100,3),lower=lo,upper=hi))
  k=sum(r['reading']=='figurative' for r in x);u=sum(r['reading']=='uncertain' for r in x)
  bounds.append(dict(corpus=label,clearly_figurative=k,uncertain=u,minimum_percent=round(k/60*100,3),maximum_if_all_uncertain_figurative=round((k+u)/60*100,3)))
 result['2-reading-distribution.csv']=rd;result['3-function-comparison.csv']=fc;result['literally-ambiguity-bounds.csv']=bounds
 meta=json.loads((D/'literally-corpora.json').read_text())
 result['literally-corpus-rates.csv']=[dict(corpus=x['label'],period=x['period'],words=x['words'],hits=x['hits'],per_million_words=round(x['hits']/x['words']*1e6,3),sample_size=60) for x in meta]
 annual=[];periods=[];contexts=[]
 for label in ['English','British English','American English']:
  raw=json.loads((D/(label.lower().replace(' ','-')+'-ngram.json')).read_text());series={x['ngram']:x['timeseries'] for x in raw}
  def get(term):
   values=series.get(term+' (All)',series.get(term));assert values is not None and len(values)==220;return values
  values=get('literally')
  for i,v in enumerate(values):annual.append(dict(corpus=label,year=1800+i,per_million_words=round(v*1e6,6)))
  for start,end in [(1800,1809),(1920,1929),(1950,1959),(1980,1989),(2000,2009),(2010,2019)]:
   periods.append(dict(corpus=label,period=f'{start}–{end}',mean_annual_per_million_words=round(sum(values[start-1800:end-1799])/(end-start+1)*1e6,6)))
  if label=='English':
   for term in ['literally died','literally true','literally thousands','literally _ADJ_']:
    for i,v in enumerate(get(term)):contexts.append(dict(construction=term,year=1800+i,per_million_bigrams=round(v*1e6,8)))
 result['1-book-frequency.csv']=annual;result['literally-book-periods.csv']=periods;result['4-book-contexts.csv']=contexts
 follow=json.loads((D/'literally-followup-queries.json').read_text())
 result['literally-followup-counts.csv']=[dict(query=x['query_id'],surface_hits=x['hits'],contexts_inspected=len(x['inspected_positions'])) for x in follow]
 checks=readcsv('literally-second-reading.csv');assert len(checks)==36
 result['literally-second-reading-summary.csv']=[dict(contexts=36,reading_agreements=sum(x['first_reading']==x['second_reading'] for x in checks),reading_changes=sum(x['first_reading']!=x['second_reading'] for x in checks),independent='no',human_validated='no')]
 return result
if __name__=='__main__':
 out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
 for name,rows in generate().items():
  with (out/name).open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
  print(name,len(rows))
