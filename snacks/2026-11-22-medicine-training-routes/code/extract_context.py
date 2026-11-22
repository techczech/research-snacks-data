"""Recreate context tables from public structured sources, retaining source clocks.
No degree/traineeship summation is performed. Raw workbooks stay in ignored scratch.
"""
from pathlib import Path
import json, csv, urllib.request, concurrent.futures, hashlib, io, warnings
import openpyxl
ROOT=Path(__file__).resolve().parents[3]
DEST=Path(__file__).resolve().parents[1]
CACHE=ROOT/'scratch'/'medicine-training-routes'
CACHE.mkdir(parents=True,exist_ok=True)
from datetime import datetime, timezone
ACCESSED=datetime.now(timezone.utc).date().isoformat()
def get(url):
 with urllib.request.urlopen(url,timeout=40) as r:return r.read()
def write_csv(name,rows):
 with (DEST/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def world_bank():
 out=[]
 for ind in ['SE.PRM.AGES','SE.PRM.DURS','SE.SEC.DURS','SE.COM.DURS']:
  url='https://api.worldbank.org/v2/country/USA;GBR;DEU;JPN;IND;SGP/indicator/'+ind+'?format=json&per_page=1000&date=2015:2026'
  body=get(url);(CACHE/(ind+'.json')).write_bytes(body)
  data=json.loads(body)
  for country in ['USA','GBR','DEU','JPN','IND','SGP']:
   a=sorted([x for x in data[1] if x['countryiso3code']==country and x['value'] is not None],key=lambda x:x['date'],reverse=True)
   if a:out.append(dict(country_iso3=country,indicator=ind,value=a[0]['value'],year=a[0]['date'],url=url,accessed=ACCESSED))
 write_csv('world-bank-school-indicators.csv',out)
def uis():
 # Explicit, manually checked rows. Old and new templates have different columns.
 choices=[('usa','United_States_of_America','Scope UOE',[11,12,14],False),('england','United_Kingdom','Scope UOE',[10,12,21,26],False),('bavaria','Germany','Scope UOE',[14,24,43],False),('japan','Japan','Scope UOE',[9,12,30],False),('india','India','Sheet1',[8,10,11,12],True),('singapore','Singapore','Sheet1',[12,13,15,17],True)]
 out=[]
 for route,country,sheet,rows,old in choices:
  url='https://download.uis.unesco.org/ISCED%20mapping/ISCED_2011_Mapping_'+country+'.xlsx'
  body=get(url);(CACHE/(country+'.xlsx')).write_bytes(body)
  with warnings.catch_warnings():
   warnings.simplefilter('ignore');w=openpyxl.load_workbook(io.BytesIO(body),data_only=True)
  s=w[sheet]
  for n in rows:
   out.append(dict(school_id=route,programme=s.cell(n,3 if old else 7).value,entrance_age=s.cell(n,8 if old else 11).value,duration_years=s.cell(n,9 if old else 12).value,isced=s.cell(n,18 if old else 20).value,reference_year='2020' if old else s.cell(n,3).value,sheet=sheet,row=n,age_column='H' if old else 'K',duration_column='I' if old else 'L',url=url,sha256=hashlib.sha256(body).hexdigest(),accessed=ACCESSED))
 write_csv('uis-selected-programmes.csv',out)
def eu():
 base='https://api.tech.ec.europa.eu/regprof20/prodmigration'
 allrows=json.loads(get(base+'/regprofs?id_profession=12401&maxrows=2000'))
 # Match the API's exact qualification category, not a lexical guess at profession.
 selected=[x for x in allrows['list'] if x['qualification']=='Basic medical training (Article 24 of Directive 2005/36/EC)']
 def one(x):
  url=base+'/regprof/si?id='+x['id'];body=get(url)
  (CACHE/('eu-'+x['id']+'.json')).write_bytes(body)
  data=json.loads(body);qs=[q for req in data.get('requirements',[]) for q in req.get('qualifications',[])] or [{}]
  return [dict(country=x['country'],record_id=x['id'],pathway=i+1,education_value=q.get('education_duration_value'),education_unit=q.get('education_duration_unit'),traineeship_value=q.get('traineeship_duration_value'),traineeship_unit=q.get('traineeship_duration_unit'),mandatory_traineeship=q.get('b_mandatory_traineeship'),state_exam=q.get('b_state_exam'),archived='archived' in x['country'],observation_year=None,accessed=ACCESSED,url=url) for i,q in enumerate(qs)]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:out=[row for rows in pool.map(one,selected) for row in rows]
 write_csv('eu-basic-medical-duration.csv',out)
def eu_gp():
 from bs4 import BeautifulSoup
 import re
 url='https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026SC0064'
 body=get(url);(CACHE/'eu-report.raw').write_bytes(body)
 soup=BeautifulSoup(body,'html.parser');out=[]
 for table in soup.find_all('table'):
  if 'Minimum duration of training (general' not in table.get_text(' ',strip=True):continue
  for tr in table.find_all('tr')[1:]:
   cells=[c.get_text(' ',strip=True) for c in tr.find_all(['td','th'])]
   for code,value in [cells[:2],cells[2:]]:
    if not code:continue
    numbers=[float(x) for x in re.findall(r'\d+(?:\.\d+)?',value)]
    out.append(dict(printed_code=code,duration_text=value,min_years=min(numbers),max_years=max(numbers),mapping_status='ambiguous printed code; not mapped' if code=='SL' else 'as printed',source=url,source_year=2026,accessed=ACCESSED))
 if not out:raise RuntimeError('Expected report table not found; inspect source before changing extraction')
 write_csv('eu-gp-report-table.csv',out)
if __name__=='__main__':
 import sys
 for name in sys.argv[1:] or ['world_bank','uis','eu','eu_gp']:globals()[name]()
