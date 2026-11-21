---
title: Version 2 preset check
date: 2026-11-21
---

# Version 2 preset check

The tool matched 45 of 47 reported examples from sources. A match means that the documented numerical value, converted year, chronogram sum or indiction year appears among the results with the preset’s settings. This check measures coverage of the documented readings. Source availability and rank are recorded separately.

The Madalfredus example XLVIII was removed before this check because the transcription could not be confirmed on the cited page.

## Mismatches

| Preset | Expected | Reader output | Source context |
| --- | --- | --- | --- |
| IIII CĐXI | 4411 | 113, 107, 411, 115 | The struck Đ and the implied unit of thousands in the inscription require a source-specific interpretation. |
| IIIIˣˣ et huit | 88 | 83, 86 | The remaining eight is written out in French. The reader does not add words as numbers. |

Run node test.mjs for each result or add --write-preset-check to regenerate this file.
