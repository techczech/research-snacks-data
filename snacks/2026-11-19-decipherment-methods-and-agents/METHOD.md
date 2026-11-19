---
title: "Method: decipherment resources, identity questions and task groups"
date: 2026-11-19
register: FOR AGENTS
provenance: "Council reconciliation and dated authored cell amendments; arithmetic only in reproduce.py"
---

# Scope

Literature survey, not a decipherment experiment. Twenty selected historical language recoveries remain fixed. Script-only recoveries (especially Meroitic and Iberian) are outside that sample: the comparator pattern is partly definitional. The page’s exclusion table names other useful sampling tests. Historical rows share evidence and scholarly chains. `9-historical-lineages.csv` groups them into eleven interpretive clusters, including Luwian with the cuneiform key chain through seals and Hittitology. These are not eleven demonstrated independent trials.

The historical full/partial/no parallel counts remain 9/8/3; known usable comparator coding remains 18/20. Both are one compiler’s provisional annotations. The first review moved three cells; “about half had a full bilingual” is as precise as this coding supports. Counts do not establish population frequency, necessity or causal prediction.

# Authored decisions

Frozen CSVs are semantic authority. `decipherment-authored-decisions-council.csv` records before/after values, rationale, source IDs, date, compiler and stage for changed judgements. Code applies no language classifier and infers no historical facts. `reproduce.py` checks identifiers and evidence consistency, counts states, adds numerical scores only when audited, and copies authored task/lineage records into expected tables. A successful run cannot validate the judgements.

Every historical evidence code and every existing numerical score has an individual rationale in `decipherment-cell-evidence.csv`. Other rows remain explicitly marked row-level mappings. New Issyk-Kushan and khipu scores are `not audited`: there is no point estimate or imputed total. Public outputs contain our annotations and arithmetic, no corpus text or paper copies.

# One stage per historical row

`selected_stage` applies to every coded column. `used_later_in_recovery` separates later confirmation from the evidence available then. Milestone years are not completion dates. Luwian uses the 1930s sign-mapping phase; 1935 is an explicitly labelled decade midpoint for plotting. Hittite was the usable known Anatolian comparator then; Karatepe and the 1973 revision are later evidence. Old Persian uses 1802 and preliminary Iranian/Avestan comparison; Rask/Burnouf/Lassen refinements are later evidence. Tangut retains 1909 as the dictionary expansion stage while recognising earlier identification and readings.

Norris: 1853 remains the recovery stage following Cathcart. Iranica and the JRAS volume record date the memoir to 1855; Cambridge catalogue metadata displays 1854. The page distinguishes the bibliographic date without claiming the sources agree on first circulation/publication.

# Evidence codes

Yes / partial / no / uncertain remain distinct. No historical partial code is silently counted as yes.

- `bilingual`: a substantial independently readable translated parallel or lexical resource at the stage = yes. Restricted sign keys, name pairs, coin names or contextual commemorative parallels = partial. No readable parallel/key = no. Unread trilingual versions do not qualify. Old Persian remains no, although de Sacy’s royal formula plus Herodotus can be called a virtual bilingual; contest stated. Hittite partial is retained because the inspected histories do not establish an extended translated Hittite key available to Hrozný’s 1915 argument; the existence of Boğazköy lexical lists alone does not date their discovery/use.
- `language_documented`: was the language, or a close relative, documented to scholarship at the selected stage? Yes = documented usable language/close relative; partial = incomplete or disputed closeness/knowledge; no = neither documented. This is not an assignment to these inscriptions. Greek was documented before Linear B was assigned to it. Tangut is partial because earlier limited readings and broad Tibeto-Burman affiliation did not supply independently documented close target knowledge.
- `language_proposed`: had that language already been proposed or shown for these inscriptions before the breakthrough? Yes = explicit identification already advanced; partial = family/continuity/region clue, tentative or disputed assignment; no = no correct prior assignment established in the inspected account. This last value is not proof that no earlier scholar ever suggested it. Every historical case has its own rationale.
- `related_language_known`: usable known linguistic comparator at the selected stage, broader than the first question’s close documented relative. Tangut’s Chinese/Tibetan comparison is broad and mediated by glosses, not proof of a close relative; it is retained provisionally. A translation language is not itself a genetic relative (Sumerian/Elamite remain no).
- `script_type_known`: broad model before sound mapping; partial for a type inferred during preliminary work.
- `proper_names`: entry at the selected stage, not every later name reading. Maya’s 1952 common-noun entry remains no despite earlier calendars and later dynastic names.

Present-evidence rows use dated sources as inspected on 19 November. The two before-breakthrough identity questions are not applied to open/comparison rows: raw fields stay uncertain and the present-resource matrix omits these two columns. No target identity is inferred mechanically from a candidate-language string. The historical two-question counts include only the twenty selected stages. Other present-resource codes retain their dated, provisional scopes.

# Unordered task groups

`decipherment-task-groups.csv` is authored classification with a checkable result and obstacle per case. Structure without language; partly read with a language to test; audit of a published proposal; script readable/language not understood; language known/individual signs unread; evidence-limited. The case order within a group has no priority meaning. Vinča is a separate non-writing comparison. Residual Maya and Tangut signs have task records without duplicating their historical case rows.

Eteocypriot belongs with Etruscan/Iberian/Meroitic. Khitan’s Langjun bilingual is named; direct Shimunek text was blocked, so the article’s title/bibliography establishes the named bilingual without certifying literal completeness. Khitan large has a source-confirmed manuscript; the author corrects its English pressmark to Nova H 176. Khipu is a structural/documentary comparison, not an assumed phonetic script. Issyk-Kushan is a developing partial reading with revised Bactrian identification, not a settled 2023 unknown-language result.

# Downloaded tractability scores

The legacy filename `4-agent-ranking.csv` is retained for existing links. It now contains six ordinal scores and two totals, alphabetically within task group, without rank numbers. Scores describe how easy it is to run checks today, not expected scientific return or decipherment probability.

| Criterion | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| C corpus | Unique object / unusable fragment | Small or sparse collection | Many short records / several substantial texts | Large varied collection |
| D digital | No usable digital evidence located | Images/editions/application access; preparation needed | Machine-readable material with coverage/rights limits | Searchable reusable core with stated academic reuse terms |
| L comparator | None securely usable | Speculative/fragmentary candidate | Supported family/target hypothesis | Close known comparator or supported family with usable living comparators |
| A anchors | None accepted | Context/internal repeated forms | Names/dates/short parallels or partial sign classes | Extended dictionary/bilingual or independently interpretable structural constraints |
| T tests | No defined check | Few weak checks | Several checks constrained by sparsity/noise/access | Multiple feasible corpus-scale checks |
| V checking | No comparable evidence | Weak/insufficient independent passages | Predictions on withheld documents/sites/forms | External labels/dictionary entries independent of hypothesis formation |

`not audited` is separate from every number, including zero. Zapotec C is not audited, not small. Voynich C0 follows the unique-object wording, despite many tokens. Rongorongo L2 is conditional on Rapa Nui speech encoding; `language_condition` records it. Proto-Elamite A3 is numerical/structural, not linguistic. Oracle-bone V1 concerns genuinely unread characters; benchmarks on already-read ones do not label them. Linear A/Proto-Sinaitic/Zapotec V1 reflects weak independent passage validation.

L and the present comparator matrix retain the consistency convention: 0=no, 1–2=partial, 3=yes. The convention does not make the ordinal intervals equal. Base total is the sum of six scores; sensitivity adds L a second time. A missing score leaves both totals not audited. No ranks, probabilities, necessity claim or statistical calibration follows. Existing computational pipelines and corpus-access barriers must be checked before a new experiment.

# Corpus and access boundaries

Keep objects, inscriptions, fragments, words, sign tokens and sign types separate. Linear A about 1,400/7,400 rounds the older computational selection; its alternate document convention remains unverified. Indus M77/EBUDS, Met/Wallace Etruscan and Rilly Meroitic descriptions retain their dates. ICIT/Fuls 2022, ET²/Meiser 2014 and Urcid 2001 are named, but proposed replacement totals remain unverified from primary editions. No absent count is zero.

Source access is stated in the source register and council response. An abstract, bibliography, indexed extract or publisher excerpt is not a full-paper/book reading. Reports of scholarly interviews establish attributed positions only. No ancient-script agent benchmark was run. A fair test needs specialist, fixed pipeline and agent with the same tools, an untouched final test, contamination and adaptive-search controls, and correct results, false discoveries, expert time and cost.

# Outputs

Nine expected tables: selected-stage timeline; six evidence-code distributions; complete matrix; downloadable scores/sensitivity; corpus/access descriptions; sample-only logical counterexamples; inventory counts; authored task groups; historical lineage groups. Four charts each carry an exact plotted CSV, PNG and Vega-Lite spec. Legacy precondition/ranking filenames preserve public URLs, not the old interpretation. All chart text uses at least 16px and categorical colours avoid purple/pink; legend selections are bound to evidence/task categories.
