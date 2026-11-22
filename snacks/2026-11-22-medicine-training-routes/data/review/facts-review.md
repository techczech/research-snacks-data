---
title: Second-family factual review of the medicine training snack draft
date: '2026-11-22'
register: FOR AGENTS
reviewer: Claude Sonnet 5.5 (second-family source validation; not the route author and not the first-registration checker)
status: supported-with-minor-corrections
subject: data/review/draft-reviewed.md (frozen draft), packet.md
inputs_read: route-coding.json, expected/milestones.csv, expected/stages.csv, expected/eu-duration-distribution.csv, data/eu-basic-medical-duration.csv, data/eu-gp-report-table.csv, data/school-baselines.csv, data/uis-selected-programmes.csv, data/world-bank-school-indicators.csv, data/review/source-spot-check.md, archived originals in the ignored scratch folder, and a few live public pages re-fetched on 22 November 2026
scope: factual claims in the draft against the records and primary sources; not a legal audit; no competence comparison
---

# Verdict

**Supported, with six minor corrections and four reading limits.** No error changes the headline range, any milestone month, any count or the no-causal-claim stance. Nothing here needs a model month changed. Items 1 to 3 are the ones worth fixing before release; items 4 to 6 are wording precision.

This is source validation of the draft's statements. It is not a legal audit of six regulatory systems, and it does not test the author's hypothesis.

# Calculation checks (all pass)

| Claim | Check | Result |
|---|---|---|
| Headline "5½ to 9 years" | General-licence months in `expected/milestones.csv`: 108, 72, 75, 72, 66, 72 | Min 66 = 5.5 (India), max 108 = 9 (California). The range is for the general-licence column only; first registration spans 4.5 to 8. The draft wording matches the former. |
| Six-row table | Months ÷ 12 for first, general and family columns against the table | All 18 cells match (8/9/11; 5/6/10; 6.25/6.25/11.25; 6/6/11; 4.5/5.5/8.5; 5/6/9). Additive chains hold: England 60+12+12+36=120; Bavaria 75+60=135; Japan 72+24+36=132; India 54+12+36=102; Singapore 60+12+36=108; California 96+12+24=132. |
| India 4½+1 | 54 + 12 = 66 months | Holds. |
| EU counts | Recounted `eu-basic-medical-duration.csv` | 32 records; 1 archived (UK); 4 empty (Liechtenstein, Greece, France, Portugal); 1 `OTHER` unit (Poland); 26 non-archived records with a year value, split 5 years = 3, 6 years = 21, 7 years = 2. Matches draft, alt text, table and `eu-duration-distribution.csv`. |
| EU GP report table | Recounted `eu-gp-report-table.csv` and compared with the table text in the archived Commission report | 27 entries, range 3 to 6 years, Luxembourg "3 or 4 years", printed code `SL`. Matches. All 27 EU member codes appear once if `SL` stands in for Slovakia, so retaining `SL` unmapped is the careful choice. |
| Package counts | 55 stages, 6 school baselines, 21 UIS rows, 24 World Bank rows, 32 EU records, 27 GP entries | All match the files. |
| School clocks | `school_years` and `entry_age` in `school-baselines.csv`, and age-18 and primary-entry columns in `expected/stages.csv` | Leaving age 18 in five cases and 19 for Bavaria (4+6+3 = 13 years from age 6). England 13 years from age 5. Age-18 clock shows Bavaria's degree starting at year 1 (`de-degree` 1 to 7.25), which supports the draft's "additional school year" sentence. World Bank primary entry ages and 2025 dates match; 21 UIS rows are 2020 or 2020/21 for all six school routes. Singapore's junior college is UIS code 444 (post-secondary non-tertiary), matching "after secondary education". |
| Germany overlap | Live registry record for Germany re-fetched; `law` text `Approbationsordnung §1(2)` and `Bundesärzteordnung §3(1)` in the archive | Registry record: education 6 years, mandatory traineeship 12 months, method "Studium der Medizin". Law: 6-year, 5,500-hour course whose last year is a 48-week practical year; standard course 6 years 3 months including the third examination; Approbation on application once the examination is passed. No separate post-course traineeship precedes Approbation, so adding 6 years + 12 months would double count. |

# Material findings and minimal corrections

## 1. Japan: the licence precedes a legal training duty on clinical practice (precision)

The draft says Japan "grants its medical licence before the separate two years of initial clinical training". That is correct, but it omits why the gap matters. Current Medical Practitioners Act Article 16-2 says a physician who intends to engage in clinical practice must receive at least two years of designated clinical training (`診療に従事しようとする医師は、二年以上…臨床研修を受けなければならない`). Article 6 makes the licence effective on register entry after passing the national examination. The Article 11 pre-clerkship common examination for domestic graduates is also as coded.

- Effect on numbers: none. If "general licence" were defined as clinical-practice-ready, Japan would be 8 years, still inside the 5.5 to 9 range.
- Minimal correction: in the paragraph beginning "Japan grants its medical licence", add that Article 16-2 requires the two years of anyone intending to practise clinically, so the six-year marker is not a date from which a graduate can practise clinically.
- Source locator: Medical Practitioners Act (current Japanese text, official XML), Articles 6, 11, 16-2. The archived English text in the scratch folder is the older 2007 translation, not the current law; the coded passages come from the Japanese text, which I re-fetched and read.

## 2. EU database label: "EU" and "jurisdictions" (wording)

The 32 records are the 27 EU member states plus Iceland, Liechtenstein, Norway, Switzerland and archived UK data. Three of the 26 counted records are not EU states (Iceland 7, Norway 6, Switzerland 6). The chart alt text and section heading say "EU basic-medical-training snapshot".

- Minimal correction: say "EU, EEA and Swiss records" (or "regulated-professions-database jurisdictions") in the chart caption and heading. For information, the 23 EU-member-state records alone split 3 / 19 / 1 for 5 / 6 / 7 years.
- The draft prose already says "jurisdictions", which is accurate; only the "EU" label is loose.

## 3. India NExT bounded check: state the span and the 2024 consultation (completeness)

The deferral notice (13 July 2023) is verbatim as quoted and sits as item 1.1 under the NExT Regulations in the current rules index. Two points about the supporting search:

- The local archive holds 25 news-listing pages covering 23 October 2023 to 22 November 2026. The route coding says titles "through page 29" were checked. Pages 26 to 29 (roughly July to October 2023) are not in the archive, so that span cannot be re-verified from the package. Nothing in the draft depends on it.
- News page 23 lists three NExT items after the deferral: a stakeholder consultation on the NExT Regulations 2023 (24 January 2024), a corrigendum (25 January 2024) and an extension (8 February 2024). None is a commencement notice, so "no later commencement notice" holds. A reader could still take the deferral as the end of the matter.
- Minimal correction: change "subsequent news titles" to name the span (October 2023 to November 2026) and add that a January to February 2024 consultation on NExT regulations appears but no commencement. The draft's refusal to predict future cohorts is correct.

## 4. EU GP table: "minimum" is dropped and the clock is inferred (wording)

The archived report table is headed "Minimum duration of training (general medical practice / family medicine)" and captioned as from an EC survey with WONCA Europe and UEMO. The draft calls it "postgraduate GP or family-medicine training" and says "its clock begins after basic medical education". The second statement is reasonable but is not printed in the table extract.

- Minimal correction: write "minimum duration of GP or family-medicine training, as printed" and "(presumably after basic medical education)", or drop the clock clause. Germany's 5 years agrees with Bavaria's 60 months in the route coding, which supports the reading.

## 5. India family-medicine endpoint: duration source (wording)

The cited regulator letter for Christian Medical College Vellore is about increasing MD Family Medicine seats for 2023 to 2024 ("Increase of seats of MD - Family Medicine course"). It proves NMC approval at that institution, not the three-year duration. The three years comes from the Post-Graduate Medical Education Regulations 2023, clause 2.1 table (broad-speciality "3 Years/ 2 years*", including M.D. (Family Medicine) in the broad-speciality annexure list). The coded note already says this; the public reference note should not suggest the letter gives the duration.

## 6. Time claim: 20 min 26 s is not verifiable (limit, not an error)

The repository history is consistent with "first packaged preview ready by 13:32" (commit at 13:31:24 on 22 November, 33 min 47 s after 12:57:37). The separate "initial scoping 20 minutes 26 seconds" figure has no record in the files I read. Four source retrievals in the retrieval manifest are stamped 13:35, after the preview commit; that is consistent with re-archiving but means the preview's source set was not frozen at 13:32. The draft says these are elapsed intervals, not active time, which is the right framing.

# Interpretations spot-checked against primary sources

These are the six general-licence and family-training readings. "Read" means I read the passage in an archived original or a page I fetched on the day.

| Jurisdiction | Reading | Result |
|---|---|---|
| California | P&S licence needs 12 credited months for a US or Canadian graduate; PTL and P&S must be held within 180 days of residency start; initial renewal needs 36 months or continued enrolment; ABFM needs 36 months | Confirmed. The 180-day rule is on the P&S landing page (re-fetched), not on the PTL page; the archived P&S application page applies a 180-day clock only to those with prior credit elsewhere. The draft cites the landing page, so it is correct. AAMC conventional route: the local archive of the AAMC page is a bot-challenge page; I re-fetched it and got no usable text, so that quotation is unverified here and rests on the first-registration check. |
| England | Provisional registration with licence for F1; full registration after F1; GP training usually 3 years | GP duration confirmed in the archived NHS England page ("usually 3 years"). Full registration after F1: the GMC page returned 403 for me; a search of GMC pages gave consistent snippets (full registration on receipt of the F1 certificate of experience). Treated as supported, not independently read in full. |
| Bavaria | Course 6 years 3 months including exam; Approbation on application; GP training 60 months | Confirmed in archived Approbationsordnung §1, Bundesärzteordnung §3 and the Bavarian training regulation (60-month Allgemeinmedizin clause, with 24 months in outpatient general practice). |
| Japan | Licence at 6 years; initial training 2 years; GP specialty at least 3 years with required rotations | Confirmed (see finding 1; archived programme standards p. 27 completion requirements, and the public board page "少なくとも3年間"). |
| India | 4½ academic years then 1 year CRMI; internship at least 12 months; permanent registration barred before internship; provisional registration on pass certificate; degree award after internship; MD 3 years | Confirmed: CBME 2024 text, CRMI 2021 regs 4 and 5 and definition 2(1)(i), GMER 2019 clauses 12.4.3 to 12.4.4, GMER 2023 reg. 23 (graduation not complete until internship), PGMER 2023 clause 2.1. See findings 3 and 5. |
| Singapore | Five-year NTU degree; provisional registration for PGY1; full registration after PGY1 certificate; family-medicine residency 3 years; FPAB accreditation needs further experience | Confirmed in archived NTU, SMC and FPAB pages. The residency entry guide (re-fetched): applicants must be PGY2 "at the minimum" by the July of R1; this fits entry straight after PGY1 as an earliest route, and the model correctly presents it as a minimum, not a typical path. |

# No causal inference

The draft's verdict, "Limits of this check" and "What the years establish" sections consistently say the comparison maps requirements and does not show that shorter routes produce equal competence or that longer routes are needed. I found no sentence that implies a causal or minimum-for-competence claim. The title "How long before a doctor can practise?" is slightly stronger than the content (a licence is not always permission to practise, see finding 1) but the page says so itself.

# Reading limits

- Not a legal audit. Regulations were read for the six selected full-time domestic routes only; alternative entry, graduate-entry, overseas-graduate and transition rules were not tested.
- Milestone markers are conditional eligibility, not observed issue dates; no individual or cohort records were checked.
- Bavaria's selected "current G9" route was accepted as the author's modelling choice; I did not check which school-leaving cohorts it applies to.
- Pages I could not read in the original: GMC (403), AAMC (bot challenge), and the MOH Holdings guide only through text extraction. English quotations are under 25 words each and paraphrases are the reviewer's.
- No whole third-party publications are reproduced here. All findings use relative record locators; no private paths, hostnames or account details are included.
