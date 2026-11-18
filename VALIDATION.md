---
title: Research Snacks rerun and privacy verification
date: 2026-11-18
provenance: Release verification recorded in this repository
---

# Verification

The default target is reconstruction of final numerical tables from shareable inputs. It does not validate every judgement, recreate historical runtime/token records or repeat every external retrieval.

The original census aggregation for the pace comparison was rerun against the existing Version 16.0 extracts: 25,130,118 records in the main extract, plus the robustness and education extracts. Their tables match the published values. This release adds numeric sufficient statistics so the offline run can recalculate the figures without redistributing microdata. The original jobs aggregates are unchanged. All extract definitions and Python scripts were syntax-checked; no new authenticated IPUMS request was made.

On 18 November 2026, fresh full-precision Google Books responses reproduced all fifty original summary rows exactly. The saved rounded series was insufficient for one threshold and is not the input used by the checker. Corpus construction labels and historical source transcriptions remain saved judgements, with source/query locators for an independent audit.

The release gate requires a fresh clone, `uv sync --locked`, all four `uv run check.py` pipelines, a deliberately changed expected-table failure, all Python sources parsing, Gitleaks over the complete publication tree and Git history, and the structural privacy scan in `code/privacy-scan.py`. Results are recorded below after the gate runs.

Only the mandated public IPUMS bibliographic citation retains source authors' names. No personal or account records are included. The scan covers repository content and historical blobs; standard Git identity metadata is separate and uses no personal email address.

## Release results, 18 November 2026

A fresh local clone of commit `f0d7453` passed `uv sync --locked` and `uv run check.py` under Python 3.13.11 with vl-convert-python 1.9.0.post1. All 22 expected CSV tables matched: jobs 6, pace 10, sickly 4 and wealth 2. The temporary clone was removed when the run ended.

Changing the expected occupation count from 268 to 269 made the checker fail with the expected table diff. All 19 Python files parsed, including the shared IPUMS request script and original aggregation scripts. Gitleaks found no secrets in the complete 1.26 MB publication tree or its initial Git commit. The privacy-pattern scan passed across 91 tracked files and all 83 historical blobs. Human reading checked the source selection, corpus redactions and licence boundaries. Final scans were repeated after this record was committed.

These results cover an offline aggregate rerun. Credentialled IPUMS recreation and independent reannotation of corpus examples remain steps for a checker with their own authorised access. A successful calculation preserves the published result; it does not establish that every source transcription or semantic judgement is right.
