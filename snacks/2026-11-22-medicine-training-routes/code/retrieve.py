"""Retrieve public sources to ignored scratch; retain hashes, never credentials."""
from pathlib import Path
import urllib.request, http.cookiejar, hashlib, json, concurrent.futures, io
from datetime import datetime, timezone
from bs4 import BeautifulSoup
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[3]
CACHE=ROOT/'scratch'/'medicine-training-routes'
CACHE.mkdir(parents=True,exist_ok=True)
def get(item):
 key,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'ResearchSnacks source verification (public documents)'})
  opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
  with opener.open(req,timeout=45) as r: body=r.read(); final=r.url
  (CACHE/(key+'.raw')).write_bytes(body)
  if body.startswith(b'%PDF'): txt='\n'.join(p.extract_text() or '' for p in PdfReader(io.BytesIO(body)).pages)
  elif body[:2]==b'PK': txt='Workbook: inspect with openpyxl'
  else: txt=BeautifulSoup(body,'html.parser').get_text(' ',strip=True)
  (CACHE/(key+'.txt')).write_text(txt)
  return {'id':key,'url':url,'retrieved_url':final,'accessed':datetime.now(timezone.utc).isoformat(),'sha256':hashlib.sha256(body).hexdigest(),'bytes':len(body)}
 except Exception as e:return {'id':key,'url':url,'error':str(e)}
if __name__=='__main__':
 import sys
 sources=json.loads(Path(sys.argv[1]).read_text())
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: results=list(pool.map(get,sources.items()))
 (CACHE/'retrieval-manifest.json').write_text(json.dumps(results,indent=2))
 for row in results:print(row['id'],row.get('bytes',row.get('error')))
