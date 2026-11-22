"""One-time source-provenance amendment after the NMC website migration.

Requires PyYAML; preserves all stage durations. The parent directory is fixed to
this snack so the script never modifies an unrelated research entry.
"""
from pathlib import Path
import yaml, json
p=Path(__file__).resolve().parents[1]; f=p/'routes.md'
front,body=f.read_text()[4:].split('\n---\n',1);d=yaml.safe_load(front);s=d['sources']
s['ca-exams']['passage']='Steps 1, 2CK, and 3'
s['in-degree'].update(title='Competency Based Medical Education Curriculum 2024',url='https://nmc.org.in/whats-new/download/378',source_date='12 September 2024',passage='4 ½ academic years; followed by one year of compulsory rotating medical internship',locator='PDF page 29, Phase-wise training and time distribution; page 31 phase breakdown',reading='Original 467-page PDF retrieved; duration and phase sections read, not the entire curriculum')
s['in-internship'].update(url='https://application.nmc.org.in/storage/nmc_gazette_notifications/231280.pdf',locator='PDF pages 24–26: definition 2(1)(i); regulations 3–6; Schedules I and II',reading='Original Gazette PDF retrieved; English definitions, duration, supervision and eligibility schedules read')
s['in-pg'].update(url='https://application.nmc.org.in/storage/nmc_gazette_notifications/PGMER%202023.pdf',locator='PDF page 30, Chapter II clause 2.1 and diploma exception; examinations included in duration',reading='Original Gazette PDF retrieved; qualification-duration clause and exception read')
s['in-pg'].pop('corroboration',None)
s['in-next'].update(title='Public notice on NExT — deferral',url='https://nmc.org.in/whats-new/download/589',source_date='13 July 2023; still linked by current rules index on 22 November 2026',passage='examination is deferred on the advice of the Ministry, dated 11.07.2023, till further directions',locator='PDF page 1; current rules index NExT item 1.1',reading='Original one-page notice read in full; current rules index and news titles through page 29 checked, no later commencement found. Future commencement is not predicted.')
s['in-registration-rule']=dict(publisher='Medical Council of India; hosted by National Medical Commission',title='Graduate Medical Education Regulations 1997, amendment 4 November 2019',url='https://nmc.org.in/19GraduateMedicalEducationRegulations1997Amendment04112019-2.pdf',accessed='2026-11-22',source_date='4 November 2019',passage='The State Medical Council will grant provisional registration to the candidate upon production of the provisional MBBS pass certificate.',locator='PDF page 87, clauses 12.4.3–12.4.6; supervised internship, not independent work',reading='Original Gazette PDF retrieved; relevant English clauses read. Legacy procedural provision corroborated by government hospital internship SOP; examination conditions remain cohort-specific.')
s['ca-ptl-exams']=dict(s['ca-exams'],title='Examination Requirement — Postgraduate Training License',passage='For a Postgraduate Training License (PTL), you must pass Steps 1 and 2CK of the USMLE examination.',locator='Opening paragraph, PTL examination requirements')
s['jp-act'].update(title='Medical Practitioners Act — current Japanese law',url='https://laws.e-gov.go.jp/api/1/lawdata/323AC0000000201',source_date='Current e-Gov text retrieved 22 November 2026',passage='医師国家試験に合格し、厚生労働大臣の免許を受けなければならない。',locator='Articles 2, 6 and 11; Article 11 includes the pre-clerkship common examination for domestic graduates',reading='Current official Japanese XML: relevant licensing and examination clauses independently read; English explanations are paraphrases')
s['us-conventional']['reading']='Full substantive AAMC page independently read through web reader; conventional route paragraph, not a universal admission statute'
for r in d['routes']:
 for st in r['stages']:
  if st['id']=='ca-exam12':st['sources']=['ca-ptl-exams']
  if st['id']=='in-first':st['sources']=['in-registration-rule','in-provisional'];st['note']='Provisional internship registration follows the final MBBS pass certificate. The national procedural provision is corroborated by official hospital implementation; state administration and processing vary.'
  if st['id']=='jp-exam' and 'common examination' not in st['note']:st['note']+=' Domestic graduates also need the pre-clerkship common examination under Article 11; it is embedded in medical education.'
 if r['id']=='india':
  r['notes']=r['notes'].split(' Original NMC PDFs')[0].split(' The original NMC curriculum')[0]+' The original NMC curriculum, internship regulation and deferral notice were retrieved. No later NExT commencement notice was found in the current rules index and bounded news search on 22 November 2026; rules applying to a future cohort can change.'
  r['evidence_status']='Original NMC curriculum, internship and postgraduate regulations and deferral notice read in relevant sections; legacy provisional-registration provision corroborated by government hospital practice'
 if r['id']=='japan':r['evidence_status']='Current Japanese Act licensing clauses, ministry route diagram and relevant JMSB general-practice standards read'
f.write_text('---\n'+yaml.safe_dump(d,allow_unicode=True,sort_keys=False,width=120)+'---\n'+body)
cache=p.parents[1]/'scratch/medicine-training-routes/india-retrieval.json'
rows=json.loads(cache.read_text())
for x in rows:x['accessed']='2026-11-22'
(p/'data').mkdir(exist_ok=True)
(p/'data/india-source-retrieval.json').write_text(json.dumps(rows,indent=2)+'\n')
