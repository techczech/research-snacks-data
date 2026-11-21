# Council review: Roman Numeral Reader research pass

## 5-line summary

1. **Position:** Useful scoping pass that catches real flaws in `roman.js` (software heuristics posed as historical priors, split needed for `archaic`, unguarded chronogram hijacking), but not yet publication-ready as evidence-backed ratings or a public Research Snack bibliography.
2. **Ratings:** Several proposed zeros confuse "unfound in snippet search" with historical unlikelihood—most seriously `omittedMillennium` (`[0,0,0,0,0]`), early-medieval `runSub` (`0`), and early-modern `irregularSub`/`omittedCentury` (`0`)—while `vigesimal`, `spanishEra`, `byzantineAnnoMundi`, and `chronogram` conflate genre- or region-conditional typicality (`3`) with global priors.
3. **Spot-checks & bugs:** 6 of 8 checked claims match their cited sources (RIB 2205/2208, Hadrian aureus 121 CE, Pollard pp. 183–184, Admiralty Arch 1910, MAN 1960/47/24), but checks uncovered missed evidence on a cited page (`W = VV = 10` on Campbell), an unverified Persée string (`XLVIII` not found on page), pirated shadow-library links (`[unofficial copy host withheld]`, `[unofficial copy host withheld]`), and an undiagnosed `roman.js` bug (`Mᵒiiijᶜlvj` → `100,456`).
4. **Scope recommendation:** Implement parser fixes (`readMultiplied` scope, distinction-bar vs ×1,000 vinculum, split `earlyFifty`/`lateSix`, framed apostrophus, dot-separated scores, explicit chronogram toggle) and opt-in Spanish Era now; defer medieval letter numerals, regnal/consular years, indictions, Byzantine Anno Mundi, and hybrid prose parsing.
5. **Write-up requirement:** Strip shadow-library and unread references, verify presets against primary editions, and explicitly admit that `0–3` scores are editorial heuristics from partial-text inspection rather than corpus-derived frequencies—turning the agent review catches into part of the Research Snack's honesty.

---

## Position, reasons, uncertainty, disconfirming evidence, recommendation

- **Position:** Revise before building or publishing. Keep the research pass's structural clean-ups (demoting `separate` and `ignored` out of historical scoring, splitting `archaic`, separating distinction marks from multiplication), reject its false-zero downgrades and genre-blind `3`s, fix four concrete `roman.js` bugs, and sanitise `references.json`.
- **Reasons:**
  - `roman.js` computes reading scores via `Math.min(...features)` (`roman.js:254`). Redefining `0` as "currently unsupported" and assigning `0` whenever a rapid search missed an example turns search gaps into hard parser vetoes.
  - Only 2 of 45 entries in `references.json` (`scots`, `nps`—two short web pages) were read in full; 2 entries (`cagnat` 404, `karger` viewer shell) were never read and never cited; 1 URL in `findings.md` (`fr.scribd.com/.../Du-cange-K`) is missing from `references.json`; 2 copyrighted monographs (`chrisomalis`, `clemens`) link to pirated shadow libraries (`[unofficial copy host withheld]`, `[unofficial copy host withheld]`).
  - Several core conventions in the exact corpora cited (Visigothic *X aspada* = 40, Roman fractions/`HS`, medieval crossed-stroke halves, `M.I.D.` = 1499) are missing, while a Greek-numeral era (`byzantineAnnoMundi`) is scored `3` for a Roman-numeral tool.
- **Uncertainty:**
  - Web spot-checks here relied on grounded search summaries rather than raw PDF inspection; exact plate readings in `Cappelli 1901` (pp. 433–435), `Forcella VII` (p. 169 no. 313), and `CIL I 536` could not be verified at facsimile level in this session, and one batch of search queries hit transient HTTP 503 capacity errors before retrying.
  - Without a real corpus count (e.g. EDCS/EDR for inscriptions, ISTC/GW for incunabula), no reviewer can prove whether a cell should be `1` vs `2` across a 500-year bin; the dispute is mainly about unjustified `0`s and unconditioned `3`s.
- **Disconfirming evidence (where the research pass is stronger than initial scepticism suggests):**
  - The research pass is genuinely disciplined on several subtle points: flagging that `separate` and `ignored` are software fallbacks rather than historical rules; catching that `read_full_text` is almost everywhere `false`; warning against blind minim substitution; distinguishing date-written from date-referred (Statue of Liberty 1886/1776, *Alice's Little Parade* 1925/1926); and verifying Thomas Knyght (Winchester Cathedral sacrist, d. Rome 1499—confirmed independently).
  - Its scepticism toward `roman.js`'s over-generous `omittedMillennium = 3` and `omittedCentury` multi-century spraying is directionally right; it simply overcorrected to `0`.
- **Recommendation:** Execute a targeted half-day revision: (1) recalibrate the disputed rating cells below, (2) fix the four `roman.js` parser bugs and clean up UI modes, (3) replace shadow-library/broken URLs and verify the 48 presets (especially `XLVIII` and `|(I)|`), and (4) frame the Research Snack explicitly around *editorial priors + verifiable caveats + what agent review caught*.

---

## 1. Review of proposed ratings

### Structural flaw across the table
`findings.md` redefines `0` as "unlikely as a software prior or currently unsupported" ("Zeros are not evidence of absence"), while simultaneously rating region- or genre-specific conventions as `3` ("typical within the documented genre or tradition"). Because `roman.js` has no region/genre selector and uses `Math.min` across features, this creates two opposite distortions:
- **False vetoes (`0`):** genuine historical practices get zeroed out because a 10-minute search did not retrieve a dated specimen in that bin.
- **Unconditioned `3`s:** narrow regional/genre practices (`vigesimal`, `spanishEra`, `byzantineAnnoMundi`, `chronogram`) receive the same weight as universal conventions (`ad`, `additive4`).

### Specific ratings that are wrong or unsupported

- **`omittedMillennium` — proposed `[0, 0, 0, 0, 0]` (was `[0, 1, 3, 2, 0]`) → Wrong; suggest `[0, 0, 2, 1, 0]`.**
  - Zeroing out High & Late Medieval because one Academia.edu León fragment returned a cache miss and two Pollard colophons spell out *millesimo* is an error of absence-of-evidence. Omitting the leading `M` in fifteenth-century dates (`CCCCLXXV` = 1475, `CCCCLXXXV` = 1485) is well documented in Italian Quattrocento inscriptions/paintings, late-medieval charters, and incunabula (e.g. Giry, *Manuel de diplomatique*; TNA guidance). The original `3` for 1000–1500 was too high; `2` (attested, chiefly 15th c.) and `1` (rare, early 16th c.) is accurate, gated as an explicit shorthand rather than default.
- **`omittedCentury` — proposed `[0, 0, 1, 0, 0]` (was `[0, 1, 2, 2, 1]`) → Too low for Early Modern; suggest `[0, 0, 2, 1, 1]` (or `[0, 0, 1, 1, 0]` for formal dates).**
  - Dropping 1500–1800 to `0` rests solely on having looked only at Pollard's 1492 Augsburg colophon (`XCij`). Two-digit year shorthand persisted in 16th–18th-century accounts, marginalia, and informal notes. The real bug is `roman.js` spraying every century in a 500-year window at equal rank—fix the UX, do not pretend the habit ended on 31 December 1499.
- **`runSub` — proposed `[2, 0, 2, 1, 0]` (was `[1, 2, 2, 1, 0]`) → Early-medieval `0` is unsupported; suggest `[2, 1, 2, 1, 0]`.**
  - The justification itself says "scarce evidence in the intervening centuries"—which is `1` (rare), not `0`. A sudden `2 → 0 → 2` trough between 300 and 1000 CE reflects not searching late-antique corpora (EDCS/ILCV) for `IIX`/`XIIX`/`XXC`. Also, `runSub` conflates classical *duode-* subtractions (`IIX`, `XIIX`, `XXC`) with late-incunable `iic`/`iiic`/`iiiic` (98–96).
- **`irregularSub` — proposed `[1, 0, 2, 0, 0]` (was `[1, 1, 1, 1, 0]`) → Bin-boundary artefact and over-generalised category; suggest `[1, 1, 1, 1, 0]` generic, or split attested `IC`/`ID` (`[1, 0, 2, 1, 0]`) from unattested `IL`/`XM` (`[0, 0, 1, 0, 0]`).**
  - Setting Late Medieval to `2` and Early Modern to `0` when the prime specimens are from the 1490s (Knyght 1499, Pollard's 1490s colophons) splits a continuous c. 1480–1520 printing/epigraphic practice across an arbitrary 1500 boundary. Meanwhile, `roman.js` treats `IL`, `XM`, `LD`, and `IC` identically, so a blanket `2` over-promotes unattested pairs.
- **`additive4` — proposed `[3, 3, 3, 2, 2]` (was `[3, 3, 3, 2, 1]`) → Modern `2` is overstated; suggest `[3, 3, 3, 2, 1]`.**
  - Raising Modern to `2` on the strength of one clock face (already broken out into `clockIIII = 3`) and one monument (Admiralty Arch, 1910) overweights additive fours/nines in general modern usage. Keep Modern `additive4` at `1`, with `clockIIII` carrying dials.
- **`standard` — proposed `[2, 2, 2, 2, 3]` (was `[2, 2, 2, 3, 3]`) → Early Modern `2` is slightly understated; suggest `[2, 2, 2, 3, 3]` (or clarify definition).**
  - Downgrading 1500–1800 from `3` to `2` cites Köbel (1514) and a 1499 epitaph (wrong period). Standard subtractive/mixed numerals (`IV`, `IX`, `XL`, `XC`, `MDCCLXXVI`, even Dorn's 1594 `XCIV`) were routine across early-modern print and inscriptions.
- **`archaic` — proposed `[2, 2, 1, 0, 0]` → Internally contradicted; must be split.**
  - `ratings.json` itself adds `earlyFifty` (`[2, 0, 0, 0, 0]`) and `lateSix` (`[2, 2, 1, 0, 0]`). Keeping the merged `archaic` vector falsely rates early-Roman `ↆ` as `2` in 300–1000 and `1` in 1000–1500.
- **`vinculum` — proposed `[2, 1, 2, 1, 0]` (was `[3, 2, 1, 1, 1]`) → Conflates ×1,000 with distinction bar; suggest `[2, 2, 1, 1, 1]` for ×1,000 alongside explicit `×1` distinction-bar reading.**
  - Raising High & Late Medieval ×1,000 vinculum to `2` while `roman.js` never emits a `×1` distinction-bar reading will misread routine medieval supralineate numerals (`X̅` = 10) as thousands (`10,000`). Modern `0` is also slightly harsh given standard textbook notation (`V̅ = 5,000`; `1` is fairer).
- **`auc` — proposed `[1, 0, 0, 1, 1]` (was `[1, 1, 0, 1, 0]`) → Early Medieval `0` vs Modern `1` is inverted; suggest `[1, 1, 0, 1, 1]`.**
  - Late-antique and early-medieval historians/chronicles (Eutropius, Orosius, Jerome, Bede quoting Roman sources) still cited AUC occasionally—at least as often as modern writers do.
- **`vigesimal` (`[0, 0, 3, 2, 0]`), `spanishEra` (`[0, 3, 3, 0, 0]`), `byzantineAnnoMundi` (`[0, 2, 3, 2, 0]`), `chronogram` (`[0, 0, 1, 3, 1]`) → Unconditioned `3`s are misleading.**
  - `vigesimal` is `3` only in French/British accounts (`2` pan-European); `spanishEra` was abolished across Iberia between 1180 (Catalonia) and 1422 (Portugal), so it is not `3` across all of 1000–1500 even in Iberia, and `0` outside it; `chronogram` is `2` overall in 1500–1800 (`3` only *given* chronogram mode); **`byzantineAnnoMundi` is a Greek-numeral system** and should not be rated `[0, 2, 3, 2, 0]` in a Roman-numeral tool (`[0, 1, 1, 0, 0]` at most for Latin-script Roman numerals in Norman/Venetian/Crusader borderlands).
- **Ratings rightly supported:** `ad` (`[0, 2, 3, 3, 3]`), `separate` and `ignored` removed from historical priors, `minim` raised in Early Modern (`[0, 1, 2, 2, 0]` for Secretary/Scottish hands), `frame` lowered in Classical (`[1, 0, 0, 0, 0]`), `multiplicative` (`[0, 0, 3, 2, 0]` for medieval accounts—though `2` globally is safer), `multiplicativePlain` (`[1, 0, 2, 2, 0]`).

---

## 2. Spot-checks against cited sources

*Method note:* Spot-checks used grounded web search against the cited domains and reference works (no raw PDF download tool was available; one parallel batch returned transient HTTP 503 `MODEL_CAPACITY_EXHAUSTED` errors and was retried in smaller batches).

1. **RIB 2208 (`IIII CĐXI` = 4411, `examples.json:118–131`) — Confirmed transcription, flawed tagging & parser failure.**
   - RIB Online confirms diplomatic `FEC. P ‣ P ‣ IIII CĐXI ‣` and expanded edition `fec(it) p(er) p(edum) IIII (milia) CĐXI` = 4,411 feet (Antonine Wall, Old Kilpatrick, 142–161 CE, Hunterian Museum).
   - *Catch:* Sol tagged `additive4` and `distinctionMarks`, omitting how `IIII` denotes 4,000 (*milia*) and treating struck `Đ` (medial-barred `D` = 500, used subtractively in `CĐ` = 400) as a generic distinction mark. `roman.js` fails completely (`113, 107, 115, 411`).
2. **RIB 2205 (`ↀↀↀↀ C XLI` = 4141, `examples.json:104–116`) — Confirmed.**
   - RIB Online confirms diplomatic `OPVS ‣ VALLI P ‣ ↀↀↀↀ C ‣ XLI ‣` (Antonine Wall, 142–180 CE). (Minor: four `ↀ` signs in a row also exemplifies additive fours, though untagged.)
3. **Hadrian aureus `DCCCLXXIIII` (RIC II.3 353, 121 CE, `examples.json:89–102`) — Confirmed.**
   - Numismatic catalogues (CNG, Numista, BMCRE 333 / RIC II 144 / RIC II.3 353) confirm reverse `ANN DCCCLXXIIII NAT VRB P CIR CON`, celebrating Rome's 874th birthday on 21 April AD 121 (Varronian 753 BCE epoch). Notably exceptional—one of very few Roman coins explicitly dated by AUC.
4. **Ostia inscription of 36 CE (`|(I)|` = 100,000,000, `examples.json:32–45`) — Context confirmed; primary glyph unverified; pirated citation URL.**
   - The underlying monument is the **Fasti Ostienses** (AD 36 entry), recording Tiberius's fire-relief donation of 100,000,000 sesterces (*sestertium milies*) after the Circus Maximus fire (`ad quod Ti. Caesar ((sestertium milies)) public(e) [d(edit)...]`).
   - *Catches:* (a) `|(I)|` comes via Chrisomalis ← Menninger without inspecting CIL XIV / Fasti Ostienses; (b) the ×100,000 frame here is specifically sesterce accounting (*centena milia sestertium*), not an abstract integer; (c) the Chrisomalis URL in `references.json`/`findings.md`/`examples.json` points to a pirated shadow library (`[unofficial copy host withheld]`).
5. **Pollard, *An Essay on Colophons* (1905), pp. 183–184 (`XCij`, `iic`–`iiiic`, `M.cccc.xc.`, `findings.md:73, 179`) — Confirmed, with notable omission.**
   - Project Gutenberg #56628 confirms Pollard's discussion of `in dem XCij. iar` (1492 *Beichtbüchlein*, omitting `Mcccc.`), `ic` (99), `iic` (98), `iiic` (97), `iiiic` (96), `iiiixx` (80), and Lichtenstein's 1490 Aquinas colophon.
   - *Catch:* The same chapter in Pollard documents `vc` (95) and **`M.I.D.` (1499)** (Brescian Politian, subtracting `I` from `D`), neither of which is captured in `findings.md`.
6. **Tony Campbell, *Chronograms* (`maphistory.info/chronograms.html`, `findings.md:195, 256`) — 1603 example confirmed; `W = 10` claim contradicted by the cited page itself.**
   - Confirmed `Absoluta opus hoc est anno MIserICorDIae...` = 1603 on the British Library map copy.
   - *Catch:* `findings.md` claims "A general W=10 rule ... require examples of their own" and lists it under Open Question #5, yet Campbell's *very same page* already documents `W = VV = 10` (e.g. Dutch map chronogram `tWIntICh`)! Caused by partial-page reading (`read_full_text: false`).
7. **Forcella Vol. VII no. 313, Thomas Knyght (`MCCCCIC` = 1499, `examples.json:460–474`) — Partially confirmed; raw PDF text unretrieved.**
   - Independent Winchester Cathedral biographical records confirm Thomas Knyght (sacrist, 1498) died in Rome in 1499, and Warburg's Forcella Vol. VII PDF contains 1499 inscriptions with `MCCCCIC` (e.g. *Honorius Tornabonus ... obiit IIII Non. Jun. MCCCCIC*). Grounded search could not pull the verbatim text of entry no. 313 on p. 169 (first attempt hit 503; retry did not surface the raw text), so the exact Knyght–`MCCCCIC` pairing remains unverified independently here, and Forcella himself depended on a later Vatican manuscript copy (`Vat. lat. 7919`).
8. **Additional checks — Admiralty Arch (`MDCCCCX`, 1910), MAN 1960/47/24 (`DCLXXXIII` = 645 CE), Chrisomalis Table 4.13 (`IX.XX.XVI`, `IIIIxx et huit`, `XVCXIV`), and CIFM 1.1 no. 82 (Madalfredus, `XLVIII`):**
   - Admiralty Arch (`ANNO DECIMO EDWARDI SEPTIMI REGIS VICTORIÆ REGINÆ CIVES GRATISSIMI MDCCCCX`, 1910/1912), MAN 1960/47/24 (Santiago Fernández, *Gerión* 38/2, 2020, `era DCLXXXIII` = 645 CE), and Chrisomalis Table 4.13's three entries (French 1231, Parisian 1388, Bohemian 1514) are all confirmed.
   - *Catch on Madalfredus (`XLVIII`):* While the Poitiers epitaph of Madalfredus (c. 802/808) is real, `search-log.md:273` explicitly records `Find "XLVIII" — No matching text found for "XLVIII"` on the Persée page! Putting `"input": "XLVIII"` into `examples.json` without noting that the string failed verification in the opened source is a provenance lapse.

---

## 3. Missing conventions, pitfalls, parser bugs and sources

### Missing historical conventions & pitfalls
- **Visigothic *X aspada* (`X'` = 40):** Notorious in Visigothic and medieval Iberian inscriptions/charters (7th–12th c.)—the exact corpus that uses the Spanish Era. Reading it as `10` creates a 30-year dating error.
- **Iberian *calderón* (`U` / `⊍` = thousands separator, e.g. `I U D` = 1,500) & Portuguese *cifrão* (`$`):** Directly collides with `roman.js:93`, which unconditionally converts `U → V` (5).
- **Roman duodecimal fractions (`S` = semis = ½, uncial dots/strokes for twelfths, `Ƨ` = 1/24) and medieval crossed-stroke halves (`iiij̶` = 3½, `x̶` = 9½, *dimidium*):** Far more frequent in real manuscripts and accounts than `K = 151`.
- **Roman `HS` / `IIS` (sestertius = 2½ asses):** Crucial context for Classical framed numerals and vincula; its medial bar is a currency/cancellation stroke, not a ×1,000 multiplier.
- **Late-incunable `MID`/`MIID`/`MIIID`/`MIIIID` (1499–1496) & `VC` (95), plus multiplicative-vs-subtractive collisions:** `IIC` (98 vs 200), `IIM` (1998 vs 2,000), `VC` (95 vs 500) are genuine historical ambiguities that merit explicit dual output.
- **Chronogram rules:** `W = VV = 10` (Dutch/German/English), strict (every numeral letter counts) vs impure (highlighted letters only), and early-16th-c. omission of `D`.
- **Calendar/diplomatic traps:** Julian–Gregorian transition (1582 Catholic Europe, 1700 Protestant Germany, 1752 Britain/colonies) + dual dating (`1603/4`); Roman inclusive backward counting from **Kalends, Nones, and Ides** (`a.d. VI Kal. Mai.` = 26 April, not 6 May—relevant to `examples.json`'s `VI` and `XVIII` day numerals!); Era of Diocletian / Martyrs (284 CE).

### Undiagnosed `roman.js` bugs exposed by the research pass
1. **Critical `readMultiplied` bug (`roman.js:223–244`):** `seg` accumulates *all* tokens before a superscript multiplier, including larger ones (`M` before `^c`, `C` before `^xx`). Result: `Mᵒiiijᶜlvj` (1456) parses as `(1000 + 4) × 100 + 56 = 100,456`! Every standard late-medieval date of the form `M iiijᶜ ...` or `M iiijˣˣ ...` is broken.
2. **Overbar (`vinculum`) tunnel vision (`roman.js:77, 136`):** Only parses bars as ×1,000 (never as ×1 distinction marks), and `_XV` only bars `X` (no multi-character bar span).
3. **`frame` silently dropped on apostrophus (`roman.js:123–131`):** `seq()` ignores `frame`, turning `|(I)|` into `1,000` instead of `100,000,000`.
4. **Chronogram hijacking (`roman.js:299`):** Any letter outside `IJVUXLCDM` forces chronogram mode, breaking `IIIIˣˣ et huit`, `era DCLXXXIII`, `anno MCCCCLXXV`, and currency strings (`li. s. d.`).
5. **Non-canonical `standard` test (`roman.js:168–192`):** Local pair checks instead of comparing against `toRoman(value)` for 1–3999.

### Missing authoritative sources
- **Arthur Giry, *Manuel de diplomatique* (1894)** (standard chronology & millésime omission reference; searched but never cited).
- **Bernhard Bischoff, *Latin Palaeography*** (1990) & **Arthur E. Gordon, *Illustrated Introduction to Latin Epigraphy*** (1983) / ***Supralineate Abbreviations in Latin Inscriptions*** (1948) (cited only second-hand).
- **Karl Menninger, *Number Words and Number Symbols*** (1969) (cited only second-hand via Chrisomalis).
- **René Cagnat, *Cours d'épigraphie latine*** (4th ed., 1914) (404 in `references.json`; freely available on Gallica / Internet Archive).
- **James Hilton, *Chronograms*** (3 vols., 1882–1895) (standard chronogram reference; searched but never cited).
- **H. Grotefend, *Taschenbuch der Zeitrechnung*** (Central European chronology counterpart to Cheney).
- **A. Millares Carlo, *Tratado de paleografía española*** (Visigothic *X aspada* and *calderón*).
- **Primary digital corpora** for actual frequency/attestation checks: **EDCS** (Clauss-Slaby), **EDR**, **OCRE**, **ISTC** / **GW**—rather than leaning primarily on 1890s textbooks.

---

## 4. Candidate additions: implement now vs wait

### Implement now (high value, low complexity, directly improves core reading)
1. **Fix `readMultiplied` scope** so a multiplier (`^c`, `^xx`, baseline `C`) only consumes preceding tokens strictly smaller than the multiplier (fixes `Mᵒiiijᶜlvj` → `1456`, `M iiijˣˣ` → `1080`).
2. **Dual overbar handling (`distinctionMarks` ×1 vs `vinculum` ×1,000) + group-span syntax** (e.g. `_(XV)` or consecutive combining macrons).
3. **Split `archaic` into `earlyFifty` (`ↆ`: `[2,0,0,0,0]`) and `lateSix` (`ↅ`: `[2,2,1,0,0]`)**, and fix `frame` over apostrophus (`|(I)|` / `|ↀ|`, glossed as Roman ×100,000, commonly sesterces).
4. **Dot/space-separated baseline vigesimal** (`IX.XX.XVI` → `196`) and explicit dual display for subtractive-vs-multiplicative collisions (`IIC` = 98 / 200, `IIM` = 1998 / 2000).
5. **Remove `separate` and `ignored` from period-plausibility scoring** (render them as parser heuristics/warnings), and surface `finalJ` and `ordinalMarks` as clean informational hints.
6. **Make chronogram an explicit opt-in mode** (instead of auto-hijacking on any non-numeral letter), with `W = VV = 10` documented via Campbell (`maphistory.info/chronograms.html`) as a Dutch/German toggle.
7. **Opt-in Spanish Era (`-38`)** in Year mode (3 lines of code, paired with an explicit *X aspada* = 40 caveat), plus a concise **year-start style caveat** (25 March / Christmas / Easter before 1752) and a **`clockIIII` dial note** for modern `IIII`.
8. **Restored, opt-in `omittedMillennium` (`[0,0,2,1,0]`) & constrained `omittedCentury`** (requiring user context/century rather than spraying five centuries at equal plausibility).

### Wait / defer (high complexity, high false-positive risk, or out of scope)
1. **Medieval alphabetic letter numerals (`A=500`, `K=151`, Iberian/Portuguese systems):** Conflicting tables, rare in real documents, and guaranteed to turn ordinary Latin/vernacular words into spurious numbers. Only ever an isolated opt-in glossary lookup, never in the main parser.
2. **Regnal, pontifical, episcopal, and consular years:** Requires curated, jurisdiction-specific ruler/consul databases, accession rules, and joint-reign tables—a full diplomatic chronology engine, not a numeral reader. Return the ordinal and state what external inputs are needed.
3. **Indiction cycles:** Needs a user-supplied date window plus 5+ regional start styles; defer or keep as a separate helper note.
4. **Byzantine Anno Mundi (`-5508` / `-5509`):** Primary manuscripts use **Greek alphabetic numerals**, not Roman numerals. Out of scope for a Roman numeral reader until core Latin/Roman forms are complete.
5. **Full Christian year-start & Julian/Gregorian conversion:** Needs month, day, place, and jurisdiction; a clear caveat covers 95% of user risk without false precision.
6. **Multilingual hybrid prose parsing (`IIIIˣˣ et huit`, Scots `Jaj`, `li. s. d.`):** Fragile NLP scope creep; better handled by guiding users to paste numeral tokens or cleanly flagging non-numeral words.
7. **Duodecimal fractions (`S`, uncials) & crossed-stroke halves:** Worth scheduling for v2 (ahead of Byzantine Anno Mundi or medieval letter numerals), but requires a non-integer display model.

---

## 5. What a sceptical palaeographer or epigrapher would object to—and what the write-up must admit

### Seven objections a sceptical specialist will raise
1. **Snippet mining dressed as a bibliography:** Only 2 of 45 references (two short web pages) were read in full; two listed references were never opened (`cagnat` 404, `karger` viewer shell); one cited URL (`scribd`) was omitted from `references.json`; and one preset (`XLVIII` for Madalfredus) failed text-match on the opened Persée page.
2. **Pirated shadow-library links in a public publication:** Linking a Cambridge University Press book (`chrisomalis`, 2010) to `[unofficial copy host withheld]` and a Cornell University Press book (`clemens`, 2007) to `[unofficial copy host withheld]` is an immediate reputational and copyright red flag.
3. **Pseudo-quantification without a corpus denominator:** Assigning `0–3` scores across 500-year pan-European bins from 48 hand-picked examples cannot establish historical frequency; medium (stone, charter, ledger, incunable, clock) and region (Iberia, France, Scotland, Rome) dominate century.
4. **Secondary/OCR reliance over primary editions and images:** Quoting Menninger via Chrisomalis for the Fasti Ostienses (`|(I)|`), trusting 19th-c. print of a Renaissance transcript (`Forcella` / `Vat. lat. 7919`) for `MCCCCIC`, and reading `Cappelli 1901` via noisy DjVu OCR—when palaeography depends on seeing the actual hand or stone.
5. **De-contextualised numerals:** Real dates and amounts sit inside diagnostic formulae (`anno Domini`, `era`, `HS`, `a.d. VI Kal.`, `li. s. d.`). Isolating the numeral creates artificial ambiguity and misses contextual cues (like whether an overbar marks a numeral or multiplies by 1,000).
6. **Flattening graphic forms into Unicode and conflating parser heuristics with conventions:** Encoding variable handwritten/carved glyphs as `ↅ`, `Đ`, `ˣˣ` hides transcription judgement; scoring `minim`, `ignored`, and `separate` alongside `additive4` confuses software guesses with scribal practices.
7. **Sampling skew and awkward gaps:** Heavy Anglophone/Roman/French weighting, missing Visigothic *X aspada* (40) despite Spanish Era coverage, missing Roman fractions, and importing Greek-numeral Byzantine Anno Mundi.

### What the Research Snack write-up MUST explicitly admit
1. **Priors are editorial heuristics, not corpus statistics:** State plainly that the `0–3` table summarises targeted handbook/example reading as a UX ranking aid, not measured historical prevalence, and that medium, region, and genre often outweigh period.
2. **How the AI research actually worked—including its failure modes:** Disclose the partial-text retrieval (2/45 read in full, paywalls, OCR noise) and **show what independent council review caught** (false zeros from search gaps, `W = 10` missed on a cited page, `XLVIII` unverified, the `Mᵒiiijᶜlvj → 100,456` parser bug, and shadow-library links stripped before release). That transparency is the strongest possible proof of the Snack's thesis about evidence-grounded AI engineering.
3. **Transcription happens before the tool:** Make clear that the reader evaluates already-transcribed strings; visual palaeographic judgements (distinction bar vs vinculum, minim counts, *X aspada*, damaged stone) remain with the human reader.
4. **Clean bibliographic hygiene before launch:** Replace all shadow-library links with standard bibliographic citations/DOIs/official open-access repositories (e.g. KU ScholarWorks for Cappelli English, Milano UP for Gallo, Gallica/Archive.org for Cagnat), remove unread dead entries, and verify every enabled UI preset against a primary edition or image.
5. **Explicit scope boundaries:** State up front that full medieval chronology (regnal years, indictions, Easter/Lady Day year-starts, Julian/Gregorian shifts, Roman Kalends/Nones/Ides) requires external diplomatic context beyond a numeral parser.
