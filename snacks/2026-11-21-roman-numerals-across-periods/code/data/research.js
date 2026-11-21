// Generated from the research and teaching data. Run node build-data.mjs.
globalThis.RomanResearch = {
  "conventions": {
    "standard": {
      "label": "Standard form",
      "note": "Subtraction only in the six usual pairs (IV, IX, XL, XC, CD, CM); no letter more than three times in a row.",
      "ratings": [
        2,
        2,
        2,
        3,
        3
      ],
      "justification": "The forms now standard already occur in Roman and medieval material, but stricter modern canonical order is typical chiefly in modern usage.",
      "citations": [
        "egbert",
        "rib2205",
        "cappelli",
        "pollard",
        "chrisomalis",
        "nps",
        "bossert"
      ]
    },
    "additive4": {
      "label": "Additive fours and nines",
      "note": "IIII for 4, VIIII for 9, XXXX for 40, CCCC for 400. Common on Roman inscriptions and in medieval manuscripts; survives on clock faces.",
      "ratings": [
        3,
        3,
        3,
        2,
        1
      ],
      "justification": "Additive fours and nines are ordinary in the examined Roman and medieval records and survive in early modern accounts and modern clocks and monuments.",
      "citations": [
        "egbert",
        "mattingly",
        "kajanto",
        "pollard",
        "nrs",
        "barnes",
        "royalparks"
      ],
      "where": "Roman inscriptions and medieval documents. Later examples include clock dials and monuments."
    },
    "irregularSub": {
      "label": "Irregular subtraction",
      "note": "A smaller letter subtracted from a larger one outside the six usual pairs: IC = 99, IL = 49, XM = 990.",
      "ratings": [
        1,
        1,
        1,
        1,
        0
      ],
      "justification": "Classical exceptions have narrow scope, and late-fifteenth-century IC is attested in print and stone; a wider period rating for IL or XM lacks equivalent evidence.",
      "citations": [
        "egbert",
        "pollard",
        "forcella"
      ],
      "where": "Check the exact pair. The late medieval evidence includes IC in Italian print and Roman epitaphs."
    },
    "runSub": {
      "label": "Repeated subtraction",
      "note": "Several identical letters subtracted together: IIX = 8, XIIX = 18, XXC = 80.",
      "ratings": [
        2,
        1,
        2,
        1,
        0
      ],
      "justification": "Flavian IIX and XIIX, Republican XXC, and incunable iic/iiic belong to identifiable traditions, with scarce evidence in the intervening centuries.",
      "citations": [
        "egbert",
        "dessau253",
        "pollard",
        "cajori"
      ]
    },
    "oddOrder": {
      "label": "Letters out of the usual order",
      "note": "The letters break the usual descending order; read mechanically, each letter is added unless the next one is larger.",
      "ratings": [
        1,
        1,
        1,
        null,
        0
      ],
      "justification": "Individually documented exceptions such as classical XXCIII and reported eighth-century LXL support a low prior for named forms, conditional on structure and context.",
      "citations": [
        "egbert",
        "cappelli",
        "cappelli1901",
        "cajori"
      ]
    },
    "additiveSum": {
      "label": "Every letter added",
      "note": "This reading adds all the letters. Compare it with readings that use subtraction or multipliers.",
      "ratings": [
        null,
        null,
        1,
        null,
        0
      ],
      "justification": "Certain lower-before-higher medieval ordinals are additive in Latin word order, but the general method of ignoring order is only a fallback.",
      "citations": [
        "cappelli1901",
        "cappellien",
        "cajori"
      ]
    },
    "multiplicative": {
      "label": "Superscript multiplier",
      "note": "A superscript ᵐ or ᶜ multiplies the number before it: iiᵐ = 2000, vᶜ = 500.",
      "ratings": [
        0,
        null,
        3,
        2,
        0
      ],
      "justification": "Raised C and M are frequent in some late medieval accounts and attested in sixteenth-century commercial arithmetic and Scottish records.",
      "citations": [
        "cappellien",
        "cappelli1901",
        "cajori",
        "nrs",
        "chrisomalis"
      ],
      "where": "Late medieval accounts and date formulae, early modern commercial arithmetic and Scottish accounts."
    },
    "multiplicativePlain": {
      "label": "Multiplier written on the line",
      "note": "M or C read as a multiplier although written on the line: IIM = 2000, VC = 500.",
      "ratings": [
        1,
        null,
        2,
        2,
        0
      ],
      "justification": "Baseline multiplication is reported sporadically for classical thousands and attested in later medieval and early modern evidence, sometimes with a separating dot or an abbreviated unit word.",
      "citations": [
        "cajori",
        "chrisomalis",
        "scots"
      ]
    },
    "vigesimal": {
      "label": "Counting in scores",
      "note": "ˣˣ multiplies by twenty: iiijˣˣ = 4 × 20 = 80 (French quatre-vingts); also found in English accounts.",
      "ratings": [
        0,
        null,
        3,
        2,
        0
      ],
      "justification": "Score notation is reported as frequent in late-medieval print and characterises some French and British records, with continued use in early modern hands.",
      "citations": [
        "cappelli",
        "pollard",
        "cajori",
        "chastel",
        "nrs",
        "chrisomalis"
      ],
      "where": "Especially French and British accounts and some French-language print."
    },
    "separate": {
      "label": "Two numbers run together",
      "note": "An internal j prompts a split into two candidate numbers. Check the spacing and layout of the source.",
      "ratings": [
        null,
        null,
        null,
        null,
        null
      ],
      "justification": "This is a transcription aid. The cited sources document final j, while its use here to propose a split is heuristic.",
      "citations": [
        "nrs",
        "pollard",
        "cappelli1901",
        "cajori"
      ],
      "referenceOnly": true
    },
    "vinculum": {
      "label": "Bar over a letter",
      "note": "A bar (vinculum) multiplies by 1000: V̅ = 5000.",
      "ratings": [
        2,
        2,
        1,
        1,
        1
      ],
      "justification": "Roman multiplication by 1,000 is documented. Compare the distinction-mark reading when the stroke only identifies a number.",
      "citations": [
        "egbert",
        "cappelli",
        "cappellien",
        "chrisomalis",
        "cajori"
      ]
    },
    "frame": {
      "label": "Framed numeral",
      "note": "Bars on three sides multiply by 100,000: |X̅| = 1,000,000.",
      "ratings": [
        1,
        null,
        null,
        null,
        null
      ],
      "justification": "Roman three-sided frames multiply by 100,000 in rare high-value inscriptions, with no independently dated examples of continued ordinary use in the other bins.",
      "citations": [
        "egbert",
        "chrisomalis",
        "cappellien"
      ],
      "where": "Rare Roman inscriptions recording very large numbers, including monetary amounts."
    },
    "apostrophus": {
      "label": "Apostrophus",
      "note": "Thousands written with I and reversed C: CIↃ = 1000, IↃ = 500, CCIↃↃ = 10,000. Roman, and revived by early modern printers.",
      "ratings": [
        2,
        1,
        1,
        2,
        1
      ],
      "justification": "Ancient inscriptional signs, Priscian's account around 500 and Renaissance imprints establish use and transmission; the evidence does not establish general popularity.",
      "citations": [
        "egbert",
        "rib2205",
        "cappelli",
        "cajori",
        "dorn",
        "chrisomalis"
      ]
    },
    "ignored": {
      "label": "Unrecognised signs left out",
      "note": "This reading uses the recognised signs. Inspect the omitted text, signs and units before using the value.",
      "ratings": [
        null,
        null,
        null,
        null,
        null
      ],
      "justification": "This is a software fallback. The cited sources illustrate signs that require their own interpretation.",
      "citations": [
        "nrs",
        "cappellien",
        "pollard"
      ],
      "referenceOnly": true
    },
    "minim": {
      "label": "Possible misreading of minims",
      "note": "In handwriting i, n, u and m are built from identical short strokes (minims); n may be a misread ii, m a misread iii.",
      "ratings": [
        0,
        1,
        2,
        2,
        0
      ],
      "justification": "Similar strokes motivate alternative transcriptions in late medieval and early modern hands, with judgement required for the individual token.",
      "citations": [
        "tna",
        "harvard",
        "nrs",
        "scots"
      ],
      "where": "Late medieval and early modern manuscript hands, including Secretary and Scottish examples."
    },
    "ad": {
      "label": "Year of the Christian era",
      "note": "Read as written in AD/CE. Local calendars could start the year at Christmas, the Annunciation or Easter.",
      "ratings": [
        0,
        2,
        3,
        3,
        3
      ],
      "justification": "The Christian era spreads in the early Middle Ages and becomes ordinary for years in later Western sources, with local differences in year start.",
      "citations": [
        "kajanto",
        "cheney",
        "tock",
        "pollard",
        "nps"
      ]
    },
    "omittedMillennium": {
      "label": "Thousand left out",
      "note": "Try adding a thousand to a shortened year. Check the neighbouring text for a written word for “thousand”.",
      "ratings": [
        0,
        0,
        2,
        1,
        0
      ],
      "justification": "The build provisionally allows shortened late medieval and early modern dates. The León fragment is unverified and printed examples sometimes spell out the thousand.",
      "citations": [
        "leon",
        "pollard"
      ]
    },
    "omittedCentury": {
      "label": "Hundreds left out",
      "note": "Dates written without thousands and hundreds, the century understood: lxxv for 1475 or 1575.",
      "ratings": [
        0,
        null,
        2,
        1,
        1
      ],
      "justification": "Late fifteenth-century printed examples include XCij for 1492. Comparable shortened forms can be considered when the source establishes the century.",
      "citations": [
        "pollard"
      ]
    },
    "auc": {
      "label": "Years from the founding of Rome (AUC)",
      "note": "This converter uses the Varronian epoch, in which AUC 1 corresponds to 753 BCE.",
      "ratings": [
        1,
        1,
        null,
        1,
        1
      ],
      "justification": "The Hadrianic city date is secure and Renaissance humanists and modern scholarship use AUC retrospectively; require the era and epoch to be supplied.",
      "citations": [
        "mattingly",
        "egbert",
        "thompson",
        "diplomatics"
      ]
    },
    "chronogram": {
      "label": "Chronogram",
      "note": "Add selected numeral letters in a phrase. Some traditions count W as VV (10).",
      "ratings": [
        null,
        null,
        1,
        3,
        1
      ],
      "justification": "The ratings apply within the genre of deliberate letter-dates. Capitals, colour or size may select the counted letters.",
      "citations": [
        "campbell",
        "chrisomalis"
      ],
      "where": "Especially early modern European maps, medals and inscriptions containing letter-dates."
    },
    "medievalLetters": {
      "label": "Alphabetic numeral signs",
      "note": "Local lists assign different values to letters. Consult the letter gloss and the source tradition.",
      "ratings": [
        null,
        null,
        null,
        null,
        null
      ],
      "justification": "Glossaries and specialised local traditions give differing values. A selected source profile is necessary.",
      "citations": [
        "cappelli1901",
        "ducangeAC",
        "ducangeOZ",
        "cajori",
        "chrisomalis",
        "keyser"
      ],
      "where": "Palaeographical glossaries and specialised Iberian traditions.",
      "referenceOnly": true
    },
    "indiction": {
      "label": "Indiction",
      "note": "Cycle of 15 numbered years. The converter uses the January reckoning, with 1 CE in indiction 4. Other styles change the count at other times of year.",
      "ratings": [
        0,
        3,
        2,
        1,
        0
      ],
      "justification": "A 15-year cycle used by medieval chanceries and some later notaries narrows a dated interval when the year-start style is known.",
      "citations": [
        "cheney",
        "kajanto",
        "stgall",
        "lorusso",
        "diplomatics"
      ],
      "where": "Medieval chanceries and some later notaries, with local start dates."
    },
    "spanishEra": {
      "label": "Spanish era",
      "note": "Era year 1 corresponds to 38 BCE. Check the document’s era label and transcription, including any crossed X.",
      "ratings": [
        null,
        3,
        2,
        0,
        0
      ],
      "justification": "Iberian inscriptions and documents use an era counted from 38 BCE with regional end dates.",
      "citations": [
        "santiago",
        "menor",
        "cheney"
      ],
      "where": "Iberian inscriptions and charters. Abolition dates varied by jurisdiction."
    },
    "finalJ": {
      "label": "Final j",
      "note": "The last i in a group may descend below the line and look like j.",
      "ratings": [
        0,
        1,
        3,
        3,
        0
      ],
      "justification": "A long or descended last i is written j in many later Western hands and in fifteenth-century print.",
      "citations": [
        "cajori",
        "pollard",
        "nrs",
        "tna",
        "cappelli1901"
      ]
    },
    "ordinalMarks": {
      "label": "Raised ordinal endings",
      "note": "Raised letters such as ᵒ can indicate a grammatical ending and leave the value unchanged.",
      "ratings": [
        0,
        1,
        3,
        2,
        0
      ],
      "justification": "Raised ordinal endings such as o in date formulae may carry grammar while leaving the numeral value unchanged.",
      "citations": [
        "cappelli1901",
        "pollard",
        "tock"
      ]
    },
    "distinctionMarks": {
      "label": "Distinction marks",
      "note": "Dots and bars can identify a numeral within text. An overbar used this way leaves its value unchanged.",
      "ratings": [
        2,
        2,
        3,
        2,
        null
      ],
      "justification": "Dots and strokes can distinguish numerals or currency from letters; they are evidence to retain even when they do not modify the value.",
      "citations": [
        "egbert",
        "rib2208",
        "cappelli",
        "cajori",
        "clemens"
      ]
    },
    "clockIIII": {
      "label": "Four strokes on clock dials",
      "note": "IIII is a customary way to mark the fourth hour on a Roman-numeral dial.",
      "ratings": [
        null,
        null,
        2,
        2,
        3
      ],
      "justification": "Four strokes are the usual form on modern Roman-numeral dials in the cited synthesis, with older clock examples and surviving alternatives.",
      "citations": [
        "chrisomalis",
        "barnes",
        "bn"
      ],
      "where": "Roman-numeral clock dials."
    },
    "hybridNumerals": {
      "label": "Mixed notation",
      "note": "Words, Arabic digits and unit signs can supply part of a value. Interpret those elements from their context.",
      "ratings": [
        null,
        null,
        1,
        1,
        null
      ],
      "justification": "Some late medieval and early modern examples mix number words, Arabic digits or special units with Roman numeral signs.",
      "citations": [
        "cappelli1901",
        "chrisomalis",
        "pollard",
        "scots"
      ]
    },
    "earlyFifty": {
      "label": "Early fifty",
      "note": "The arrow-shaped sign ↆ has the value 50.",
      "ratings": [
        2,
        0,
        0,
        0,
        0
      ],
      "justification": "The early arrow-like forms of fifty are distinct from the late six and from L.",
      "citations": [
        "egbert",
        "unicode"
      ]
    },
    "lateSix": {
      "label": "Late six",
      "note": "The C-like sign ↅ has the value 6.",
      "ratings": [
        2,
        2,
        1,
        null,
        null
      ],
      "justification": "A late-form six appears from the imperial period and in late-antique and early medieval hands; specialised sources disagree on origins and the end of related forms.",
      "citations": [
        "unicode",
        "cappelli1901",
        "chrisomalis"
      ]
    }
  },
  "sources": [
    {
      "id": "egbert",
      "author": "James C. Egbert Jr",
      "year": 1896,
      "title": "Introduction to the Study of Latin Inscriptions",
      "publisher_or_journal": "American Book Company",
      "url": "https://upload.wikimedia.org/wikipedia/commons/4/47/Introduction_to_the_study_of_Latin_inscriptions_%28IA_cu31924075494371%29.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Numerals pp. 72–77; pp. 129–130, 181–182 for Flavian titulature and editions"
    },
    {
      "id": "dessau253",
      "author": "Hermann Dessau",
      "year": 1892,
      "title": "Inscriptiones Latinae Selectae, vol. 1",
      "publisher_or_journal": "Weidmann; EDCS scan",
      "url": "https://db.edcs.eu/epigr/dessau/de-a0069.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "p. 69, no. 253 (CIL III 6993)"
    },
    {
      "id": "rib2205",
      "author": "R. G. Collingwood and R. P. Wright",
      "year": 1965,
      "title": "RIB 2205. Distance Slab of the Sixth Legion",
      "publisher_or_journal": "Roman Inscriptions of Britain Online",
      "url": "https://romaninscriptionsofbritain.org/inscriptions/2205",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Date, Diplomatic l. 6, Translation"
    },
    {
      "id": "rib2208",
      "author": "R. G. Collingwood and R. P. Wright",
      "year": 1965,
      "title": "RIB 2208. Distance Slab of the Twentieth Legion",
      "publisher_or_journal": "Roman Inscriptions of Britain Online",
      "url": "https://romaninscriptionsofbritain.org/inscriptions/2208",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Date, Diplomatic l. 7, Translation and commentary"
    },
    {
      "id": "mattingly",
      "author": "Harold Mattingly",
      "year": 1936,
      "title": "Coins of the Roman Empire in the British Museum, vol. 3: Nerva to Hadrian",
      "publisher_or_journal": "British Museum",
      "url": "https://ignca.gov.in/Asi_data/17029.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "p. cxxvi and n. 2 (Hadrian aureus)"
    },
    {
      "id": "unicode",
      "author": "David J. Perry",
      "year": 2006,
      "title": "Proposal for Additional Ancient Roman Characters (L2/06-269)",
      "publisher_or_journal": "Unicode Consortium document archive",
      "url": "https://www.unicode.org/wg2/docs/n3218.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "§2, pp. 5–6; figs. 13–16 and 20"
    },
    {
      "id": "keyser",
      "author": "Paul Keyser",
      "year": 1988,
      "title": "The Origin of the Latin Numerals 1 to 1000",
      "publisher_or_journal": "American Journal of Archaeology 92(4), 529–546",
      "url": "https://www.academia.edu/7554252/_The_Origin_of_the_Latin_Numerals_1_to_1000_American_Journal_of_Archaeology_92_1988_529_546",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Extracts pp. 541–543, including n. 83; publisher abstract via DOI 10.2307/505248"
    },
    {
      "id": "cappelli",
      "author": "Adriano Cappelli",
      "year": 1990,
      "title": "Dizionario di abbreviature latine ed italiane (6th ed.)",
      "publisher_or_journal": "Hoepli; University of Warwick scan",
      "url": "https://warwick.ac.uk/fac/arts/ren/languages/manuscripttoprint/latin/manuali_hoepli_adriano_cappelli-lexicon_abbreviaturarum._dizionario_di_abbreviature_latine_ed_italiane-ulrico_hoepli_1999.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Introduction, Numerazione romana ed arabica, pp. LII–LV; scanned edition carries 1990 copyright"
    },
    {
      "id": "cappelli1901",
      "author": "Adriano Cappelli",
      "year": 1901,
      "title": "Lexicon abbreviaturarum (German ed.)",
      "publisher_or_journal": "J. J. Weber; Internet Archive OCR of the scan",
      "url": "https://archive.org/stream/lexiconabbreviat00capp/lexiconabbreviat00capp_djvu.txt",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Römische Zahlschrift pp. 429–437, alphabetised plates and glosses; OCR distorts glyphs"
    },
    {
      "id": "cappellien",
      "author": "Adriano Cappelli; trans. David Heimann and Richard Kay",
      "year": 1982,
      "title": "The Elements of Abbreviation in Medieval Latin Paleography",
      "publisher_or_journal": "University of Kansas Libraries",
      "url": "https://bms-du-chatillonnais.e-monsite.com/medias/files/latin-abreviations-medievales-pour-la-paleographie.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "§§7.1–7.81, pp. 43–46; check number of reversed Cs against Italian original"
    },
    {
      "id": "cajori",
      "author": "Florian Cajori",
      "year": 1928,
      "title": "A History of Mathematical Notations, vol. 1, Romans",
      "publisher_or_journal": "Open Court; digitised transcription of the historical text",
      "url": "https://en.wikisource.org/wiki/A_History_Of_Mathematical_Notations/Volume_1/Romans",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "§§47–56, pp. 31–35; this section opened, wider book unreviewed"
    },
    {
      "id": "chrisomalis",
      "author": "Stephen Chrisomalis",
      "year": 2010,
      "title": "Numerical Notation: A Comparative History",
      "publisher_or_journal": "Cambridge University Press",
      "url": "https://www.cambridge.org/core/books/numerical-notation/4C3107573159D539D04DD7307423FA36",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "pp. 110–115, 118–129; tables 4.11, 4.13; fig. 4.2; Bischoff and Gordon cited indirectly"
    },
    {
      "id": "pollard",
      "author": "Alfred W. Pollard",
      "year": 1905,
      "title": "An Essay on Colophons: With Specimens and Translations",
      "publisher_or_journal": "Caxton Club; Project Gutenberg transcription",
      "url": "https://www.gutenberg.org/files/56628/56628-h/56628-h.htm",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "pp. 11–12, 78–79, 102–104, 182–185"
    },
    {
      "id": "kajanto",
      "author": "Iiro Kajanto",
      "year": 1977,
      "title": "Dating in the Latin Inscriptions of Medieval and Renaissance Rome",
      "publisher_or_journal": "Arctos 11",
      "url": "https://journal.fi/arctos/article/download/88205/47344",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "pp. 45–49, including nn. 17–21 and corpus examples"
    },
    {
      "id": "cheney",
      "author": "C. R. Cheney; revised Michael Jones",
      "year": 2000,
      "title": "A Handbook of Dates for Students of British History",
      "publisher_or_journal": "Cambridge University Press",
      "url": "https://assets.cambridge.org/97805217/70958/sample/9780521770958wsc00.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "The year pp. 1–5, Christian era, Spanish era, indiction and regnal years"
    },
    {
      "id": "tock",
      "author": "Olivier Guyotjeannin and Benoît-Michel Tock",
      "year": 1999,
      "title": "« Mos presentis patrie » : les styles de changement du millésime dans les actes français (XIe–XVIe siècle)",
      "publisher_or_journal": "Bibliothèque de l’École des chartes 157(1)",
      "url": "https://www.persee.fr/doc/bec_0373-6237_1999_num_157_1_450961?pageId=T1_52",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "pp. 43–62 (selected passages and nn. 13–17, 54–55); Annexe I"
    },
    {
      "id": "nrs",
      "author": "National Records of Scotland",
      "year": 2022,
      "title": "Scottish Handwriting 1500–1700: A self-help pack",
      "publisher_or_journal": "National Records of Scotland; Scottish Records Association mirror",
      "url": "https://scottishrecordsassociation.org/documents/NRS-Scottish_handwriting_self-help_kit-web.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "pp. 7–8, documents 3–4, 8 and their transcripts"
    },
    {
      "id": "scots",
      "author": "National Records of Scotland",
      "year": "n.d.",
      "title": "Is it a date?",
      "publisher_or_journal": "Scotland's People",
      "url": "https://api.scotlandspeople.gov.uk/scottish-handwriting/coaching/problem-solver/problem-words/dates",
      "accessed": "2026-11-21",
      "read_full_text": true,
      "pages": "Jaj dates; illustrated 1663 transcription"
    },
    {
      "id": "chastel",
      "author": "Centre André-Chastel",
      "year": "n.d.",
      "title": "Du bon usage des archives de l’Ancien Régime",
      "publisher_or_journal": "Sorbonne Université",
      "url": "https://www.centrechastel.sorbonne-universite.fr/ressources/du-bon-usage-des-archives-de-lancien-regime",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Quelques conseils pour la transcription des textes d'archives, numeral table"
    },
    {
      "id": "tna",
      "author": "The National Archives",
      "year": "n.d.",
      "title": "Latin Palaeography Activities and Documents",
      "publisher_or_journal": "The National Archives",
      "url": "https://cdn.nationalarchives.gov.uk/documents/latin-palaeography-activities-and-documents.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Selected document alphabets, entries I/i, N/n, U/u, V/v; numeral examples in transcriptions"
    },
    {
      "id": "harvard",
      "author": "Harvard Geoffrey Chaucer Website editors",
      "year": "n.d.",
      "title": "How to Read Medieval Handwriting (Paleography)",
      "publisher_or_journal": "Harvard Geoffrey Chaucer Website",
      "url": "https://chaucer.fas.harvard.edu/how-read-medieval-handwriting-paleography",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Search extract, Minims section and context-dependent examples"
    },
    {
      "id": "santiago",
      "author": "Javier de Santiago Fernández",
      "year": 2020,
      "title": "Dos inscripciones tardoantiguas donadas al Museo Arqueológico Nacional (Madrid)",
      "publisher_or_journal": "Gerión 38(2), 623–638",
      "url": "https://revistas.ucm.es/index.php/GERI/article/download/71951/4564456554709/4564456599554",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "pp. 625–626, 632–634, fig. 2 (MAN 1960/47/24)"
    },
    {
      "id": "menor",
      "author": "Elisabeth Menor Natal",
      "year": 2020,
      "title": "Epitafio de Diego González",
      "publisher_or_journal": "Boletín del Archivo Epigráfico Hispano 5",
      "url": "https://www.ucm.es/archivoepigraficohispania/file/bae5f03-menor-ac?ver=",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "pp. 80–83, inscription, edition and dual date commentary"
    },
    {
      "id": "lorusso",
      "author": "Vito Lorusso",
      "year": 2017,
      "title": "Locating Greek Manuscripts through Paratexts",
      "publisher_or_journal": "De Gruyter",
      "url": "https://www.degruyterbrill.com/document/doi/10.1515/9783110479010-008/pdf?licenseType=free",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "pp. 226–227, three collated manuscript examples and conversion rule"
    },
    {
      "id": "stgall",
      "author": "Dianne Tillotson; facsimile after Franz Steffens",
      "year": "n.d.",
      "title": "A Florilegium of Dates",
      "publisher_or_journal": "Medieval Writing",
      "url": "https://losthistory.net/medievalwriting/whyread/florilegium.htm",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "St Gall charter, Stiftsarchiv Urkunden IV, 485"
    },
    {
      "id": "ducangeAC",
      "author": "Charles du Fresne, sieur du Cange",
      "year": 1710,
      "title": "Glossarium ad scriptores mediae et infimae latinitatis, A–C",
      "publisher_or_journal": "Johann Adam Jung; CAMENA",
      "url": "https://mateo.uni-mannheim.de/camenaref/ducange/bd1/DuCange_glossarium_a-c.html",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "s.v. A and B; 1710 edition title-page transcribed at top"
    },
    {
      "id": "ducangeOZ",
      "author": "Charles du Fresne, sieur du Cange",
      "year": 1710,
      "title": "Glossarium ad scriptores mediae et infimae latinitatis, O–Z",
      "publisher_or_journal": "Johann Adam Jung; CAMENA",
      "url": "https://mateo.uni-mannheim.de/camenaref/ducange/bd4/DuCange_glossarium_o-z.html",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "s.v. Z; selected headword text"
    },
    {
      "id": "dorn",
      "author": "Gerhard Dorn",
      "year": 1594,
      "title": "Clavis totius philosophiae chymisticae",
      "publisher_or_journal": "Christoph Rab, Herborn; Bibliographia Paracelsica, BP.Dorn.1594-01",
      "url": "https://www.theatrum-paracelsicum.com/Bibliographia_Paracelsica/BP.Dorn.1594-01",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "A1r, diplomatic imprint transcription and copy links"
    },
    {
      "id": "campbell",
      "author": "Tony Campbell and contributors",
      "year": 2018,
      "title": "Chronograms: a round-up of present knowledge",
      "publisher_or_journal": "Map History",
      "url": "https://www.maphistory.info/chronograms.html",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Introduction; What is a chronogram?; Census (1600, 1603, 1605, 1608, 1704); inscription at page end"
    },
    {
      "id": "barnes",
      "author": "Barnes Foundation",
      "year": 2019,
      "title": "Research Notes: Tall Case Clock",
      "publisher_or_journal": "Barnes Foundation",
      "url": "https://www.barnesfoundation.org/research-notes-clock",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Dial detail and object 2001.25.86"
    },
    {
      "id": "nps",
      "author": "National Park Service",
      "year": 2021,
      "title": "Statue Front",
      "publisher_or_journal": "US National Park Service",
      "url": "https://www.nps.gov/places/000/statue-front.htm",
      "accessed": "2026-11-21",
      "read_full_text": true,
      "pages": "Tablet inscription and monument date"
    },
    {
      "id": "bossert",
      "author": "Dave Bossert",
      "year": "n.d.",
      "title": "Alice’s Little Parade Struts with Restoration and New Music Score",
      "publisher_or_journal": "Author's restoration account",
      "url": "https://davidbossert.com/assets/article-alice-s-litte-parade-article.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "p. 1 reproduced copyright frame and first release information"
    },
    {
      "id": "leon",
      "author": "Author and editorial status unverified",
      "year": "n.d.",
      "title": "Lápidas medievales del Museo de León (España)",
      "publisher_or_journal": "Academia.edu upload",
      "url": "https://www.academia.edu/170401993/L%C3%A1pidas_medievales_del_Museo_de_Le%C3%B3n_Espa%C3%B1a_",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Search extract only, fragment cccc liij; opening returned cache miss"
    },
    {
      "id": "poitiers",
      "author": "Robert Favreau and Jean Michaud",
      "year": 1974,
      "title": "Corpus des inscriptions de la France médiévale 1.1: Ville de Poitiers",
      "publisher_or_journal": "CNRS; Persée",
      "url": "https://www.persee.fr/doc/cifm_0000-0000_1974_cat_1_1?pageId=T2_16",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "No. 82, Epitaphe de Madalfredus; reported dates 802 or 808"
    },
    {
      "id": "prinz",
      "author": "Joseph Prinz",
      "year": 1972,
      "title": "Der karolingische Kalender der Handschrift Ambros. M 12 sup⁸",
      "publisher_or_journal": "Vandenhoeck & Ruprecht, Festschrift für Hermann Heimpel III; MGH library scan",
      "url": "https://www.mgh-bibliothek.de/dokumente/a/a089822.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "p. 294, October entries and n. 23"
    },
    {
      "id": "forcella",
      "author": "Vincenzo Forcella",
      "year": 1876,
      "title": "Iscrizioni delle chiese e d’altri edificii di Roma, vol. VII",
      "publisher_or_journal": "Tipografia delle Scienze Matematiche e Fisiche; Warburg Institute scan",
      "url": "https://resources.warburg.sas.ac.uk/pdf/hnh5600b2797976v7.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Nos. 239 (1464), 313 (1499, p. 169, from Vatican cod. 7919), 350 (1515, p. 172)"
    },
    {
      "id": "royalparks",
      "author": "The Royal Parks",
      "year": "n.d.",
      "title": "Monuments in St James’s Park",
      "publisher_or_journal": "The Royal Parks",
      "url": "https://www.royalparks.org.uk/visit/parks/st-jamess-park/monuments",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Admiralty Arch inscription and 1912 completion"
    },
    {
      "id": "diocles",
      "author": "Pablo Ozcáriz Gil",
      "year": 2021,
      "title": "Natione Hispanus. Sobre la identificación de los hispanos en el Imperio romano",
      "publisher_or_journal": "Araucaria 23(47), 21–45",
      "url": "https://agora.edu.es/descarga/articulo/8065051.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "p. 36, Diocles entry and n. 16; CIL VI 10048 / EDR102150"
    },
    {
      "id": "lexRubria",
      "author": "Yves Lassard, ed.",
      "year": 2013,
      "title": "Lex de Gallia Cisalpina (CIL I² 592)",
      "publisher_or_journal": "The Roman Law Library editorial transcription",
      "url": "https://www.academia.edu/4970696/Lex_de_Gallia_Cisalpina_CIL_I_2_592_",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Chapter XXI; indexed text expands the thousand mark as (milia)"
    },
    {
      "id": "thompson",
      "author": "Edward Maunde Thompson",
      "year": 1906,
      "title": "Handbook of Greek and Latin Palaeography, Additions and Corrections",
      "publisher_or_journal": "Katapi transcription",
      "url": "https://katapi.org.uk/G&LPalaeography/AddsCorrs.html",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Additions to Chapter IX, indictions, years, regnal dating and year starts"
    },
    {
      "id": "clemens",
      "author": "Raymond Clemens and Timothy Graham",
      "year": 2007,
      "title": "Introduction to Manuscript Studies",
      "publisher_or_journal": "Cornell University Press",
      "url": "https://discover.library.unt.edu/catalog/b3451328",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Chapter 6, p. 91, passage on Roman and Arabic numbers, OCR has glyph errors"
    },
    {
      "id": "bn",
      "author": "Biblioteca Nacional (Brazil)",
      "year": 2020,
      "title": "Anais da Biblioteca Nacional, vol. 140",
      "publisher_or_journal": "Fundação Biblioteca Nacional",
      "url": "https://www.gov.br/bn/pt-br/central-de-conteudos/producao/publicacoes/colecoes/anais-biblioteca-nacional/copy_of_anais-da-biblioteca-nacional-vol-140/anais-da-biblioteca-nacional-vol-140/an140_digital-9094.pdf",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Date of imprint, p. 31; table and Wells clock example"
    },
    {
      "id": "diplomatics",
      "author": "Federico Gallo",
      "year": 2024,
      "title": "Diplomatics: The Science of Reading Medieval Documents. A Handbook",
      "publisher_or_journal": "Milano University Press",
      "url": "https://www.academia.edu/123756218/Diplomatics_The_Science_of_Reading_Medieval_Documents_A_Handbook_Milano_2024",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Chapter XII, pp. 85–87; AUC, regnal, Spanish era, Anno Mundi and indictions"
    },
    {
      "id": "lastparis-title",
      "author": "Metro-Goldwyn-Mayer",
      "year": 1954,
      "title": "The Last Time I Saw Paris, copyright title card",
      "publisher_or_journal": "Title-card reproduction, CopyrightData.com",
      "url": "https://www.copyrightdata.com/chart/ch02.html",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "Errors or Absence of Year"
    },
    {
      "id": "lastparis-afi",
      "author": "American Film Institute",
      "year": "n.d.",
      "title": "The Last Time I Saw Paris (1954), AFI Catalog of Feature Films",
      "publisher_or_journal": "American Film Institute",
      "url": "https://catalog.afi.com/Film/51256-THE-LAST-TIME-I-SAW-PARIS?cxt=filmography",
      "accessed": "2026-11-21",
      "read_full_text": false,
      "pages": "History and copyright details"
    }
  ],
  "letters": {
    "A": [
      {
        "source": "cappelli1901",
        "value": "500; marked form 5,000"
      },
      {
        "source": "ducangeAC",
        "value": "500"
      }
    ],
    "B": [
      {
        "source": "cappelli1901",
        "value": "300; marked form 3,000"
      },
      {
        "source": "ducangeAC",
        "value": "300"
      },
      {
        "source": "chrisomalis",
        "value": "Portuguese navigational b = 5"
      }
    ],
    "E": [
      {
        "source": "cappelli1901",
        "value": "250"
      }
    ],
    "F": [
      {
        "source": "cappelli1901",
        "value": "40"
      }
    ],
    "G": [
      {
        "source": "cappelli1901",
        "value": "400"
      }
    ],
    "H": [
      {
        "source": "cappelli1901",
        "value": "200"
      }
    ],
    "K": [
      {
        "source": "cappelli1901",
        "value": "151; marked form 151,000"
      }
    ],
    "N": [
      {
        "source": "cappelli1901",
        "value": "90"
      },
      {
        "source": "chrisomalis",
        "value": "Iberian astronomical N = 9"
      }
    ],
    "O": [
      {
        "source": "cappelli1901",
        "value": "11"
      },
      {
        "source": "chrisomalis",
        "value": "Iberian astronomical o = 8"
      }
    ],
    "P": [
      {
        "source": "cappelli1901",
        "value": "400"
      }
    ],
    "Q": [
      {
        "source": "cappelli1901",
        "value": "500"
      },
      {
        "source": "chrisomalis",
        "value": "Iberian astronomical Q = 5 and q = 4"
      }
    ],
    "R": [
      {
        "source": "cappelli1901",
        "value": "80"
      },
      {
        "source": "chrisomalis",
        "value": "Portuguese navigational R = 40"
      }
    ],
    "S": [
      {
        "source": "cappelli1901",
        "value": "70"
      },
      {
        "source": "chrisomalis",
        "value": "Iberian astronomical S = 7 and s = 6"
      }
    ],
    "T": [
      {
        "source": "cappelli1901",
        "value": "160 or 1,000"
      },
      {
        "source": "chrisomalis",
        "value": "Iberian astronomical t = 3"
      }
    ],
    "Y": [
      {
        "source": "cappelli1901",
        "value": "150; marked form 150,000"
      }
    ],
    "Z": [
      {
        "source": "cappelli1901",
        "value": "2,000"
      },
      {
        "source": "ducangeOZ",
        "value": "2,000"
      }
    ]
  },
  "glossary": [
    {
      "id": "additive",
      "term": "Additive notation",
      "aliases": [
        "additive",
        "every letter added"
      ],
      "definition": "Add the values of the signs. IIII is 1 + 1 + 1 + 1."
    },
    {
      "id": "subtractive",
      "term": "Subtractive notation",
      "aliases": [
        "subtraction",
        "subtractive",
        "subtractive pairs"
      ],
      "definition": "Take a smaller value away from a larger one. In IV, I before V gives 5 − 1 = 4."
    },
    {
      "id": "vinculum",
      "term": "Vinculum",
      "aliases": [
        "vinculum",
        "thousands bar",
        "bar over a letter"
      ],
      "definition": "A bar above a numeral. In the thousands convention, X̅ stands for 10,000. A similar bar can mark a numeral without changing its value."
    },
    {
      "id": "apostrophus",
      "term": "Apostrophus",
      "aliases": [],
      "definition": "Large-number signs built from I, C and a reversed C. CIↃ means 1,000 and IↃ means 500."
    },
    {
      "id": "minim",
      "term": "Minim",
      "aliases": [
        "minim misreading",
        "minims"
      ],
      "definition": "A short upright stroke in handwriting. Two strokes could look like either ii or n, depending on the hand."
    },
    {
      "id": "scores",
      "term": "Scores (vigesimal)",
      "aliases": [
        "scores",
        "score notation",
        "vigesimal",
        "counting in twenties"
      ],
      "definition": "A score is twenty. Four scores are eighty. A small superscript xx can mark multiplication by twenty."
    },
    {
      "id": "chronogram",
      "term": "Chronogram",
      "aliases": [
        "chronograms"
      ],
      "definition": "A phrase whose selected numeral letters add up to a number, often a year. Capitals can mark which letters to count."
    },
    {
      "id": "indiction",
      "term": "Indiction",
      "aliases": [
        "indictions",
        "indiction cycle"
      ],
      "definition": "A year number from 1 to 15 in a repeating dating cycle. The same number recurs every fifteen years."
    },
    {
      "id": "auc",
      "term": "AUC",
      "aliases": [
        "founding of Rome"
      ],
      "definition": "Ab urbe condita, “from the founding of the city”. This reckoning counts from Rome’s traditional foundation in 753 BCE."
    },
    {
      "id": "spanish-era",
      "term": "Spanish era",
      "aliases": [],
      "definition": "A year count used in parts of medieval Iberia. Its year 1 corresponds to 38 BCE."
    },
    {
      "id": "distinction-bar",
      "term": "Distinction bar",
      "aliases": [
        "distinction bars",
        "distinction marks",
        "bar as a distinction mark"
      ],
      "definition": "A line over a numeral that marks it off from nearby writing without multiplying it."
    },
    {
      "id": "superscript",
      "term": "Superscript multiplier",
      "aliases": [
        "superscript multipliers",
        "superscripts"
      ],
      "definition": "A small raised sign that multiplies the numeral before it. In iiᶜ, the raised c gives 2 × 100."
    },
    {
      "id": "final-j",
      "term": "Final j",
      "aliases": [],
      "definition": "A j used for i at the end of a numeral. In viij, j adds one, just as in viii."
    }
  ],
  "presets": [
    {
      "kind": "attested",
      "input": "CCCXXC",
      "period_id": "classical",
      "values": [
        380
      ],
      "convention_ids": [
        "runSub",
        "irregularSub"
      ],
      "date": "157 BCE",
      "source": "CIL I 536, as cited on p. 74 n. 2",
      "why": "Two tens subtracted from the final hundred in a larger number.",
      "url": "https://upload.wikimedia.org/wikipedia/commons/4/47/Introduction_to_the_study_of_Latin_inscriptions_%28IA_cu31924075494371%29.pdf"
    },
    {
      "kind": "attested",
      "input": "IIII",
      "period_id": "classical",
      "values": [
        4
      ],
      "convention_ids": [
        "additive4"
      ],
      "date": "late Republic, probably mid-1st century BCE",
      "source": "CIL I² 592, Lex de Gallia Cisalpina",
      "why": "The four in the municipal office IIIIvir uses four strokes.",
      "url": "https://www.academia.edu/4970696/Lex_de_Gallia_Cisalpina_CIL_I_2_592_"
    },
    {
      "kind": "attested",
      "input": "|(I)|",
      "period_id": "classical",
      "values": [
        100000000
      ],
      "convention_ids": [
        "frame",
        "apostrophus"
      ],
      "date": "36 CE",
      "source": "Ostia inscription, reported by Chrisomalis p. 114 citing Menninger p. 245",
      "why": "Frame applied to a thousand sign. Full-width side strokes represent the source's printed transcription; the original has not been inspected.",
      "url": "https://www.cambridge.org/core/books/numerical-notation/4C3107573159D539D04DD7307423FA36",
      "source_status": "Source unavailable to the council reviewer. Link opens the publisher record"
    },
    {
      "kind": "attested",
      "input": "IIX",
      "period_id": "classical",
      "values": [
        8
      ],
      "convention_ids": [
        "runSub"
      ],
      "date": "71 CE",
      "source": "CIL VI 931, Vespasian's road restoration, no. 22",
      "why": "The eighth imperial acclamation appears in a copy of an official inscription.",
      "url": "https://upload.wikimedia.org/wikipedia/commons/4/47/Introduction_to_the_study_of_Latin_inscriptions_%28IA_cu31924075494371%29.pdf"
    },
    {
      "kind": "attested",
      "input": "XIIX",
      "period_id": "classical",
      "values": [
        18
      ],
      "convention_ids": [
        "runSub"
      ],
      "date": "77–78 CE",
      "source": "ILS 253 / CIL III 6993, near Prusa",
      "why": "The eighteenth imperial acclamation, written with a subtractive run at the end.",
      "url": "https://db.edcs.eu/epigr/dessau/de-a0069.pdf"
    },
    {
      "kind": "attested",
      "input": "VIIII",
      "period_id": "classical",
      "values": [
        9
      ],
      "convention_ids": [
        "additive4"
      ],
      "date": "77–78 CE",
      "source": "ILS 253 / CIL III 6993, near Prusa",
      "why": "The same inscription used additive nine in Vespasian's tribunician count and designation for consul.",
      "url": "https://db.edcs.eu/epigr/dessau/de-a0069.pdf"
    },
    {
      "kind": "attested",
      "input": "DCCCLXXIIII",
      "period_id": "classical",
      "values": [
        121
      ],
      "convention_ids": [
        "additive4",
        "auc"
      ],
      "date": "121 CE",
      "source": "Hadrian aureus, RIC II.3 353",
      "why": "The coin counts 874 years in Rome's foundation era. The expected civil year is 121 CE.",
      "url": "https://ignca.gov.in/Asi_data/17029.pdf",
      "options": {
        "date": "auc"
      }
    },
    {
      "kind": "attested",
      "input": "ↀↀↀↀ C XLI",
      "period_id": "classical",
      "values": [
        4141
      ],
      "convention_ids": [
        "apostrophus"
      ],
      "date": "142–180 CE",
      "source": "RIB 2205, Antonine Wall, diplomatic line 6",
      "why": "Four thousand signs and subtractive XL occur in a single distance.",
      "url": "https://romaninscriptionsofbritain.org/inscriptions/2205"
    },
    {
      "kind": "attested",
      "input": "IIII CĐXI",
      "period_id": "classical",
      "values": [
        4411
      ],
      "convention_ids": [
        "additive4",
        "distinctionMarks"
      ],
      "date": "142–161 CE",
      "source": "RIB 2208, Antonine Wall, diplomatic line 7",
      "why": "The initial four means thousands and struck Đ participates in a subtractive 411. The modern value comes from the edition. The date shown expands the edition’s abbreviated or mistyped “a.d. 142-61”.",
      "url": "https://romaninscriptionsofbritain.org/inscriptions/2208"
    },
    {
      "kind": "attested",
      "input": "XXXXII",
      "period_id": "classical",
      "values": [
        42
      ],
      "convention_ids": [
        "additive4"
      ],
      "date": "146–150 CE",
      "source": "CIL VI 10048 / ILS 5287, Diocles's age",
      "why": "Four tens on the charioteer's career inscription.",
      "url": "https://agora.edu.es/descarga/articulo/8065051.pdf"
    },
    {
      "kind": "attested",
      "input": "XXIII",
      "period_id": "classical",
      "values": [
        23
      ],
      "convention_ids": [
        "standard"
      ],
      "date": "146–150 CE",
      "source": "CIL VI 10048 / ILS 5287, Diocles's age",
      "why": "Days of age supplement the 42 years on the same inscription.",
      "url": "https://agora.edu.es/descarga/articulo/8065051.pdf"
    },
    {
      "kind": "attested",
      "input": "ↅ",
      "period_id": "early-medieval",
      "values": [
        6
      ],
      "convention_ids": [
        "lateSix"
      ],
      "date": "8th century CE",
      "source": "Cappelli’s eighth-century figures, reproduced in Perry fig. 16",
      "why": "Unicode shorthand for the C-like six among Cappelli's eighth-century glyph specimens.",
      "url": "https://www.unicode.org/wg2/docs/n3218.pdf"
    },
    {
      "kind": "attested",
      "input": "VI",
      "period_id": "early-medieval",
      "values": [
        6
      ],
      "convention_ids": [
        "standard"
      ],
      "date": "345 CE",
      "source": "ILCV 4422 / CIL X 6420, Tarracina epitaph",
      "why": "An early date by day of the month. The year was supplied by naming consuls.",
      "url": "https://journal.fi/arctos/article/download/88205/47344",
      "source_status": "Source unavailable to the council reviewer"
    },
    {
      "kind": "attested",
      "input": "XVIII",
      "period_id": "early-medieval",
      "values": [
        18
      ],
      "convention_ids": [
        "standard"
      ],
      "date": "517 CE",
      "source": "ILCV 1147A, Nola epitaph",
      "why": "The numeral gives 18 January in the burial record.",
      "url": "https://journal.fi/arctos/article/download/88205/47344",
      "source_status": "Source unavailable to the council reviewer"
    },
    {
      "kind": "attested",
      "input": "DCLXXXIII",
      "period_id": "early-medieval",
      "values": [
        645
      ],
      "convention_ids": [
        "standard",
        "spanishEra"
      ],
      "date": "23 August 645 CE",
      "source": "Museo Arqueológico Nacional 1960/47/24, l. 6",
      "why": "The era numeral is 683. The edition converts it to 645 CE.",
      "url": "https://revistas.ucm.es/index.php/GERI/article/download/71951/4564456554709/4564456599554",
      "options": {
        "date": "spanishEra"
      }
    },
    {
      "kind": "attested",
      "input": "dcccLxxvi",
      "period_id": "early-medieval",
      "values": [
        876
      ],
      "convention_ids": [
        "standard",
        "ad"
      ],
      "date": "876 CE (event recorded)",
      "source": "Milan calendar, October 8 entry, p. 294",
      "why": "Mixed-case Christian year dates the battle at Andernach. The same calendar’s 5 October entry gives 876 for an event Prinz dates to 877. The exact glyphs of the 8 October entry need checking against the plate.",
      "url": "https://www.mgh-bibliothek.de/dokumente/a/a089822.pdf",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "dccccxxxiii",
      "period_id": "early-medieval",
      "values": [
        933
      ],
      "convention_ids": [
        "additive4",
        "ad"
      ],
      "date": "13 August 933 CE",
      "source": "St Gall, Stiftsarchiv Urkunden IV, 485",
      "why": "Christian era year appears next to an indiction and a conflicting regnal count.",
      "url": "https://losthistory.net/medievalwriting/whyread/florilegium.htm",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "vi",
      "period_id": "early-medieval",
      "values": [
        933
      ],
      "convention_ids": [
        "standard",
        "indiction"
      ],
      "date": "13 August 933 CE",
      "source": "St Gall, Stiftsarchiv Urkunden IV, 485",
      "why": "Indiction six is written beside the year 933. The converter lists 933 alongside the other years with the same indiction.",
      "url": "https://losthistory.net/medievalwriting/whyread/florilegium.htm",
      "options": {
        "date": "indiction"
      }
    },
    {
      "kind": "attested",
      "input": "DCCCCLXIII",
      "period_id": "early-medieval",
      "values": [
        963
      ],
      "convention_ids": [
        "additive4",
        "ad"
      ],
      "date": "963 CE",
      "source": "Rome, Silvagni Monum. XVI.3, apud Kajanto p. 45",
      "why": "An early Christian-era numeral in the corpus of Roman epitaphs.",
      "url": "https://journal.fi/arctos/article/download/88205/47344",
      "source_status": "Source unavailable to the council reviewer",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "DCCCCLXXVII",
      "period_id": "early-medieval",
      "values": [
        977
      ],
      "convention_ids": [
        "additive4",
        "ad"
      ],
      "date": "977 CE",
      "source": "Rome, Silvagni Monum. XVI.4, apud Kajanto p. 45",
      "why": "Christian-era date with four hundreds.",
      "url": "https://journal.fi/arctos/article/download/88205/47344",
      "source_status": "Source unavailable to the council reviewer",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "DCCCCLXXXI",
      "period_id": "early-medieval",
      "values": [
        981
      ],
      "convention_ids": [
        "additive4",
        "ad"
      ],
      "date": "981 CE",
      "source": "Rome, Silvagni Monum. XVII.1, apud Kajanto p. 45",
      "why": "Christian-era date with four additive hundreds.",
      "url": "https://journal.fi/arctos/article/download/88205/47344",
      "source_status": "Source unavailable to the council reviewer",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "IX.XX.XVI",
      "period_id": "late-medieval",
      "values": [
        196
      ],
      "convention_ids": [
        "vigesimal"
      ],
      "date": "1231 CE",
      "source": "Numerical Notation table 4.13, citing Smith 1926 p. 6",
      "why": "Nine scores plus sixteen gives 196. The document dates to 1231 CE.",
      "url": "https://www.cambridge.org/core/books/numerical-notation/4C3107573159D539D04DD7307423FA36",
      "source_status": "Source unavailable to the council reviewer. Link opens the publisher record"
    },
    {
      "kind": "attested",
      "input": "IIIIˣˣ et huit",
      "period_id": "late-medieval",
      "values": [
        88
      ],
      "convention_ids": [
        "vigesimal",
        "hybridNumerals"
      ],
      "date": "1388 CE",
      "source": "Numerical Notation table 4.13, citing Guitel 1975 p. 225",
      "why": "Mixed-script numeral phrase, four scores plus French eight. Raised xx represented with Unicode superscripts here.",
      "url": "https://www.cambridge.org/core/books/numerical-notation/4C3107573159D539D04DD7307423FA36",
      "source_status": "Source unavailable to the council reviewer. Link opens the publisher record"
    },
    {
      "kind": "attested",
      "input": "MCCCCXII",
      "period_id": "late-medieval",
      "values": [
        1412
      ],
      "convention_ids": [
        "additive4",
        "ad"
      ],
      "date": "January 1412 CE",
      "source": "S. Maria sopra Minerva, Forcella I no. 1579, apud Kajanto p. 46",
      "why": "The epitaph gives both a Christian-era year and indiction.",
      "url": "https://journal.fi/arctos/article/download/88205/47344",
      "source_status": "Source unavailable to the council reviewer",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "Mᵒiiijᶜlvj",
      "period_id": "late-medieval",
      "values": [
        1456
      ],
      "convention_ids": [
        "multiplicative",
        "ordinalMarks",
        "finalJ",
        "ad"
      ],
      "date": "1456 CE (year glossed by Cappelli)",
      "source": "Römische Zahlschrift p. 434, M plate",
      "why": "Ordinal o, raised hundred and terminal j. Input renders the edition's parenthesised reading with Unicode superscripts.",
      "url": "https://archive.org/stream/lexiconabbreviat00capp/lexiconabbreviat00capp_djvu.txt",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "M . CCCC . LXIIII",
      "period_id": "late-medieval",
      "values": [
        1464
      ],
      "convention_ids": [
        "additive4",
        "ad"
      ],
      "date": "20 September 1464 CE",
      "source": "Forcella VII no. 239, Camane family tomb",
      "why": "Dots and additive hundreds and units in a Rome epitaph.",
      "url": "https://resources.warburg.sas.ac.uk/pdf/hnh5600b2797976v7.pdf",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "lxxixº",
      "period_id": "late-medieval",
      "values": [
        79
      ],
      "convention_ids": [
        "ordinalMarks",
        "standard"
      ],
      "date": "16 August 1479 CE",
      "source": "Lerida Breviary colophon, p. 102",
      "why": "The numeric tail is 79. Printed words supply the other 1400.",
      "url": "https://www.gutenberg.org/files/56628/56628-h/56628-h.htm",
      "source_status": "Source unavailable to the council reviewer"
    },
    {
      "kind": "attested",
      "input": "M.cccc.xc.",
      "period_id": "late-medieval",
      "values": [
        1490
      ],
      "convention_ids": [
        "additive4",
        "ad"
      ],
      "date": "7 September 1490 CE",
      "source": "Hermann Lichtenstein's Aquinas Opuscula colophon, p. 184",
      "why": "The following vii belongs to a day clause. Concatenation would make a plausible but wrong year.",
      "url": "https://www.gutenberg.org/files/56628/56628-h/56628-h.htm",
      "source_status": "Source unavailable to the council reviewer",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "XCij",
      "period_id": "late-medieval",
      "values": [
        1492
      ],
      "convention_ids": [
        "omittedCentury",
        "finalJ"
      ],
      "date": "10 March 1492 CE",
      "source": "Hans Schauer's Augsburg Beichtbuchlein colophon, p. 183",
      "why": "The written numeral is 92. Context supplies the century.",
      "url": "https://www.gutenberg.org/files/56628/56628-h/56628-h.htm",
      "source_status": "Source unavailable to the council reviewer",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "M.cccc.lxxxxiii.",
      "period_id": "late-medieval",
      "values": [
        1493
      ],
      "convention_ids": [
        "additive4",
        "ad"
      ],
      "date": "1493 CE",
      "source": "Gasparo Visconti, Rithmi, Milan, p. 104",
      "why": "The colophon writes both 400 and 90 additively.",
      "url": "https://www.gutenberg.org/files/56628/56628-h/56628-h.htm",
      "source_status": "Source unavailable to the council reviewer",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "MCCCCIC",
      "period_id": "late-medieval",
      "values": [
        1499
      ],
      "convention_ids": [
        "irregularSub",
        "additive4",
        "ad"
      ],
      "date": "1499 CE (death date)",
      "source": "Forcella VII no. 313, Thomas Knyght epitaph, Rome",
      "why": "IC is 99 following four written hundreds. The edition transmits it from a Vatican manuscript.",
      "url": "https://resources.warburg.sas.ac.uk/pdf/hnh5600b2797976v7.pdf",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "IIᶜ",
      "period_id": "early-modern",
      "values": [
        200
      ],
      "convention_ids": [
        "multiplicative"
      ],
      "date": "1514 CE",
      "source": "Jakob Köbel, Rechenbiechlin, Augsburg, quoted in Cajori §55 p. 34",
      "why": "The numerator in a fraction, with C in superscript.",
      "url": "https://en.wikisource.org/wiki/A_History_Of_Mathematical_Notations/Volume_1/Romans"
    },
    {
      "kind": "attested",
      "input": "IIIIᶜ.LX",
      "period_id": "early-modern",
      "values": [
        460
      ],
      "convention_ids": [
        "multiplicative",
        "additive4"
      ],
      "date": "1514 CE",
      "source": "Jakob Köbel, Rechenbiechlin, Augsburg, quoted in Cajori §55 p. 34",
      "why": "The denominator of the same fraction adds LX after four hundreds.",
      "url": "https://en.wikisource.org/wiki/A_History_Of_Mathematical_Notations/Volume_1/Romans"
    },
    {
      "kind": "attested",
      "input": "XVCXIV",
      "period_id": "early-modern",
      "values": [
        1514
      ],
      "convention_ids": [
        "multiplicativePlain",
        "ad"
      ],
      "date": "1514 CE (as listed)",
      "source": "Numerical Notation table 4.13, citing Smith 1926 p. 7",
      "why": "Baseline XV multiplies C, followed by XIV.",
      "url": "https://www.cambridge.org/core/books/numerical-notation/4C3107573159D539D04DD7307423FA36",
      "source_status": "Source unavailable to the council reviewer. Link opens the publisher record",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "vij·c.",
      "period_id": "early-modern",
      "values": [
        700
      ],
      "convention_ids": [
        "multiplicativePlain",
        "finalJ"
      ],
      "date": "1534 CE",
      "source": "Sebastian Franck, Weltbuch, fol. ccxx, quoted in Cajori §55 n. 18",
      "why": "The source joins a punctuated seven hundreds with XL in words for 740 German miles.",
      "url": "https://en.wikisource.org/wiki/A_History_Of_Mathematical_Notations/Volume_1/Romans"
    },
    {
      "kind": "attested",
      "input": "ijᶜ xxij",
      "period_id": "early-modern",
      "values": [
        222
      ],
      "convention_ids": [
        "multiplicative",
        "finalJ"
      ],
      "date": "May 1580 CE",
      "source": "Estate of James VI's Household, National Records of Scotland, doc. 3 l. 14",
      "why": "A payment amount in pounds, with a raised hundred and final j.",
      "url": "https://scottishrecordsassociation.org/documents/NRS-Scottish_handwriting_self-help_kit-web.pdf"
    },
    {
      "kind": "attested",
      "input": "iiiiᶜ xliiij",
      "period_id": "early-modern",
      "values": [
        444
      ],
      "convention_ids": [
        "multiplicative",
        "additive4",
        "finalJ"
      ],
      "date": "May 1580 CE",
      "source": "Estate of James VI's Household, National Records of Scotland, doc. 3 l. 16",
      "why": "Four hundreds and forty-four pounds in a livery payment total.",
      "url": "https://scottishrecordsassociation.org/documents/NRS-Scottish_handwriting_self-help_kit-web.pdf"
    },
    {
      "kind": "attested",
      "input": "CIↃ IↃ XCIV",
      "period_id": "early-modern",
      "values": [
        1594
      ],
      "convention_ids": [
        "apostrophus",
        "ad"
      ],
      "date": "1594 CE",
      "source": "Dorn, Clavis totius philosophiae chymisticae, A1r, Herborn",
      "why": "The title-page revived apostrophus for 1000 and 500 alongside ordinary subtraction for 94.",
      "url": "https://www.theatrum-paracelsicum.com/Bibliographia_Paracelsica/BP.Dorn.1594-01",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "MIserICorDIae",
      "period_id": "early-modern",
      "values": [
        1603
      ],
      "convention_ids": [
        "chronogram"
      ],
      "date": "1603 CE",
      "source": "Angliae et Hiberniae nova descriptio, cartographic chronogram census",
      "why": "Highlighted capitals in the selected word date the original map issue.",
      "url": "https://www.maphistory.info/chronograms.html",
      "options": {
        "mode": "chronogram"
      }
    },
    {
      "kind": "attested",
      "input": "MIserICorDIae et patIentIae",
      "period_id": "early-modern",
      "values": [
        1605
      ],
      "convention_ids": [
        "chronogram"
      ],
      "date": "1605 CE",
      "source": "Quadus and Caymox, distance triangle, Nuremberg, census entry 1605",
      "why": "Selected capital letters across two words sum to 1605.",
      "url": "https://www.maphistory.info/chronograms.html",
      "options": {
        "mode": "chronogram"
      }
    },
    {
      "kind": "attested",
      "input": "Lxxxxj",
      "period_id": "early-modern",
      "values": [
        91
      ],
      "convention_ids": [
        "additive4",
        "finalJ"
      ],
      "date": "1609 CE",
      "source": "John Tod inventory, National Records of Scotland, doc. 4 l. 40",
      "why": "Total of pounds uses four tens and final j.",
      "url": "https://scottishrecordsassociation.org/documents/NRS-Scottish_handwriting_self-help_kit-web.pdf"
    },
    {
      "kind": "attested",
      "input": "vj C&",
      "period_id": "early-modern",
      "values": [
        600
      ],
      "convention_ids": [
        "multiplicativePlain",
        "finalJ",
        "hybridNumerals"
      ],
      "date": "1663 CE",
      "source": "National Records of Scotland, illustrated Jaj date",
      "why": "The numeric component vj with abbreviated hundreds is 600. The suspension mark is rendered as in the archive transcript.",
      "url": "https://api.scotlandspeople.gov.uk/scottish-handwriting/coaching/problem-solver/problem-words/dates"
    },
    {
      "kind": "attested",
      "input": "IV",
      "period_id": "modern",
      "values": [
        4
      ],
      "convention_ids": [
        "standard"
      ],
      "date": "1886 CE (tablet installed)",
      "source": "Statue of Liberty tablet, day of month",
      "why": "The same monument uses subtractive IV and commemorates July 1776.",
      "url": "https://www.nps.gov/places/000/statue-front.htm"
    },
    {
      "kind": "attested",
      "input": "MDCCLXXVI",
      "period_id": "modern",
      "values": [
        1776
      ],
      "convention_ids": [
        "standard",
        "ad"
      ],
      "date": "1886 CE (tablet installed)",
      "source": "Statue of Liberty tablet, year",
      "why": "The date referred to predates the inscription by 110 years.",
      "url": "https://www.nps.gov/places/000/statue-front.htm",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "IIII",
      "period_id": "modern",
      "values": [
        4
      ],
      "convention_ids": [
        "additive4",
        "clockIIII"
      ],
      "date": "c. 1890–1910 CE",
      "source": "Barnes Foundation tall-case clock, 2001.25.86",
      "why": "Four strokes mark four hours on the chapter ring.",
      "url": "https://www.barnesfoundation.org/research-notes-clock"
    },
    {
      "kind": "attested",
      "input": "MDCCCCX",
      "period_id": "modern",
      "values": [
        1910
      ],
      "convention_ids": [
        "additive4",
        "ad"
      ],
      "date": "1910 date, arch completed 1912",
      "source": "Admiralty Arch, London, frieze",
      "why": "A modern public inscription chooses DCCCC for 900.",
      "url": "https://www.royalparks.org.uk/visit/parks/st-jamess-park/monuments",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "MCMXXV",
      "period_id": "modern",
      "values": [
        1925
      ],
      "convention_ids": [
        "standard",
        "ad"
      ],
      "date": "1925 copyright, 1926 release",
      "source": "Alice’s Little Parade, Winkler title card reproduced by restorer Dave Bossert, p. 1",
      "why": "The copyright date on the frame differs from the first release year.",
      "url": "https://davidbossert.com/assets/article-alice-s-litte-parade-article.pdf",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "attested",
      "input": "MCMXLIV",
      "period_id": "modern",
      "values": [
        1944
      ],
      "convention_ids": [
        "standard",
        "ad"
      ],
      "date": "1954 film",
      "source": "MGM, The Last Time I Saw Paris, title card",
      "why": "The 1954 film’s notice reads MCMXLIV (1944). MCMLIV would give 1954.",
      "url": "https://www.copyrightdata.com/chart/ch02.html",
      "source_status": "Title-card reproduction. The AFI Catalog also records the 1944 date in the copyright notice.",
      "topic": "A film date misprint",
      "start": 8
    },
    {
      "kind": "constructed",
      "input": "MCMLXXXIV",
      "period_id": "modern",
      "values": [
        1984
      ],
      "convention_ids": [
        "standard",
        "ad"
      ],
      "why": "A modern subtractive year, with CM and IV.",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "constructed",
      "input": "Ⅻ",
      "period_id": "modern",
      "values": [
        12
      ],
      "convention_ids": [
        "standard"
      ],
      "why": "One Unicode character expands to XII."
    },
    {
      "kind": "constructed",
      "input": "VIIII",
      "period_id": "classical",
      "values": [
        9
      ],
      "convention_ids": [
        "additive4"
      ],
      "why": "Five plus four ones, where a modern writer might choose IX."
    },
    {
      "kind": "constructed",
      "input": "XIIX",
      "period_id": "classical",
      "values": [
        18,
        20,
        22
      ],
      "convention_ids": [
        "runSub",
        "oddOrder",
        "additiveSum"
      ],
      "why": "Two ones subtracted from the last X give 18. Pairwise subtraction and a simple sum give other values."
    },
    {
      "kind": "constructed",
      "input": "IIC",
      "topic": "A medieval puzzle",
      "start": 7,
      "period_id": "late-medieval",
      "values": [
        98,
        100,
        102,
        200
      ],
      "convention_ids": [
        "runSub",
        "multiplicativePlain",
        "oddOrder",
        "additiveSum"
      ],
      "why": "Two before C can be subtracted together, read in a pair, added, or treated as a multiplier."
    },
    {
      "kind": "constructed",
      "input": "IL",
      "period_id": "late-medieval",
      "values": [
        49,
        51
      ],
      "convention_ids": [
        "irregularSub",
        "additiveSum"
      ],
      "why": "A subtractive pair outside the modern six alongside a simple sum."
    },
    {
      "kind": "constructed",
      "input": "IXX",
      "period_id": "early-medieval",
      "values": [
        19,
        21
      ],
      "convention_ids": [
        "oddOrder",
        "additiveSum"
      ],
      "why": "A pairwise reading gives 19 even though the written order is unusual."
    },
    {
      "kind": "constructed",
      "input": "IIM",
      "period_id": "late-medieval",
      "values": [
        998,
        1000,
        1002,
        2000
      ],
      "convention_ids": [
        "multiplicativePlain",
        "runSub"
      ],
      "why": "A baseline thousand multiplier competes with subtraction."
    },
    {
      "kind": "constructed",
      "input": "iiᵐ vᶜ xxiiij",
      "period_id": "late-medieval",
      "values": [
        2524
      ],
      "convention_ids": [
        "multiplicative",
        "finalJ"
      ],
      "why": "Thousands and hundreds have separate raised multipliers, followed by a remainder."
    },
    {
      "kind": "constructed",
      "input": "Mᵒijᶜxxx",
      "period_id": "late-medieval",
      "values": [
        1230
      ],
      "convention_ids": [
        "ordinalMarks",
        "multiplicative"
      ],
      "why": "The raised o is grammatical. The raised c multiplies only ij."
    },
    {
      "kind": "constructed",
      "input": "vˣˣ ix",
      "period_id": "late-medieval",
      "values": [
        109
      ],
      "convention_ids": [
        "vigesimal"
      ],
      "why": "Five scores and nine."
    },
    {
      "kind": "constructed",
      "input": ".iiij.xx.",
      "period_id": "late-medieval",
      "values": [
        24,
        80
      ],
      "convention_ids": [
        "vigesimal",
        "distinctionMarks",
        "finalJ"
      ],
      "why": "Dots can divide four scores or simply separate groups of signs."
    },
    {
      "kind": "constructed",
      "input": ".iij.xx.vi.",
      "period_id": "late-medieval",
      "values": [
        66
      ],
      "convention_ids": [
        "vigesimal",
        "distinctionMarks"
      ],
      "why": "Three scores plus a remainder of six."
    },
    {
      "kind": "constructed",
      "input": "iij viij",
      "period_id": "late-medieval",
      "values": [
        "3 and 8"
      ],
      "convention_ids": [
        "separate",
        "finalJ"
      ],
      "why": "An internal final j prompts a candidate split into two amounts."
    },
    {
      "kind": "constructed",
      "input": "X̅V",
      "period_id": "classical",
      "values": [
        10005,
        15
      ],
      "convention_ids": [
        "vinculum",
        "distinctionMarks"
      ],
      "why": "An overbar can multiply X by 1,000 or mark part of an ordinary numeral."
    },
    {
      "kind": "constructed",
      "input": "X̅I̅V̅",
      "period_id": "classical",
      "values": [
        14000,
        14
      ],
      "convention_ids": [
        "vinculum",
        "distinctionMarks"
      ],
      "why": "The same stroke can cover several signs."
    },
    {
      "kind": "constructed",
      "input": "|X̅|",
      "period_id": "classical",
      "values": [
        1000000
      ],
      "convention_ids": [
        "frame"
      ],
      "why": "A three-sided enclosure changes the scale to ×100,000."
    },
    {
      "kind": "constructed",
      "input": "|ↀ|",
      "period_id": "classical",
      "values": [
        100000000
      ],
      "convention_ids": [
        "frame",
        "apostrophus"
      ],
      "why": "The enclosure applies to the entire thousand sign."
    },
    {
      "kind": "constructed",
      "input": "CCIↃↃ IↃ",
      "period_id": "early-modern",
      "values": [
        10500
      ],
      "convention_ids": [
        "apostrophus"
      ],
      "why": "Two pairs of arcs mark 10,000, and a half form adds 500."
    },
    {
      "kind": "constructed",
      "input": "ↆXV",
      "period_id": "classical",
      "values": [
        65
      ],
      "convention_ids": [
        "earlyFifty"
      ],
      "why": "The arrow-like 50 combines with a familiar XV."
    },
    {
      "kind": "constructed",
      "input": "ↅII",
      "period_id": "early-medieval",
      "values": [
        8
      ],
      "convention_ids": [
        "lateSix"
      ],
      "why": "The C-like 6 combines additively with two ones."
    },
    {
      "kind": "constructed",
      "input": "xin",
      "period_id": "late-medieval",
      "values": [
        11,
        13
      ],
      "convention_ids": [
        "minim",
        "ignored"
      ],
      "why": "A transcribed n could be two i strokes. It could also be a letter left out of the numeral."
    },
    {
      "kind": "constructed",
      "input": "xiu",
      "period_id": "late-medieval",
      "values": [
        14,
        16,
        13
      ],
      "convention_ids": [
        "minim",
        "standard"
      ],
      "why": "Consider whether the final shape is a u for v or a pair of ii strokes."
    },
    {
      "kind": "constructed",
      "input": "cccclxxv",
      "period_id": "late-medieval",
      "values": [
        475,
        1475
      ],
      "convention_ids": [
        "omittedMillennium",
        "ad"
      ],
      "why": "A written 475 could be the end of a date for which the thousand was understood.",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "constructed",
      "input": "lxxv",
      "period_id": "early-modern",
      "values": [
        75,
        1575,
        1675,
        1775
      ],
      "convention_ids": [
        "omittedCentury",
        "ad"
      ],
      "why": "A short year needs other evidence to place it in a particular century.",
      "options": {
        "date": "ad"
      }
    },
    {
      "kind": "constructed",
      "input": "I",
      "period_id": "classical",
      "values": [
        "753 BCE"
      ],
      "convention_ids": [
        "auc"
      ],
      "why": "The first year in the Varronian AUC reckoning.",
      "options": {
        "date": "auc"
      }
    },
    {
      "kind": "constructed",
      "input": "DCCLIII",
      "period_id": "classical",
      "values": [
        "1 BCE"
      ],
      "convention_ids": [
        "auc"
      ],
      "why": "AUC 753 is the last BCE year in this reckoning.",
      "options": {
        "date": "auc"
      }
    },
    {
      "kind": "constructed",
      "input": "DCCLIV",
      "period_id": "classical",
      "values": [
        "1 CE"
      ],
      "convention_ids": [
        "auc"
      ],
      "why": "AUC 754 follows 1 BCE. There is no civil year zero.",
      "options": {
        "date": "auc"
      }
    },
    {
      "kind": "constructed",
      "input": "XXXVIII",
      "period_id": "early-medieval",
      "values": [
        "1 BCE"
      ],
      "convention_ids": [
        "spanishEra"
      ],
      "why": "The last year on the BCE side of the Spanish-era epoch.",
      "options": {
        "date": "spanishEra"
      }
    },
    {
      "kind": "constructed",
      "input": "XXXIX",
      "period_id": "early-medieval",
      "values": [
        "1 CE"
      ],
      "convention_ids": [
        "spanishEra"
      ],
      "why": "The first year on the CE side of the Spanish-era epoch.",
      "options": {
        "date": "spanishEra"
      }
    },
    {
      "kind": "constructed",
      "input": "XV",
      "period_id": "late-medieval",
      "values": [
        "1002 CE, 1017 CE, …"
      ],
      "convention_ids": [
        "indiction"
      ],
      "why": "Fifteen marks the end of a cycle. The same number recurs every fifteen years.",
      "options": {
        "date": "indiction"
      }
    },
    {
      "kind": "constructed",
      "input": "DaWn In CIVIC LIght",
      "period_id": "early-modern",
      "values": [
        "759 without W",
        "769 with W"
      ],
      "convention_ids": [
        "chronogram"
      ],
      "why": "Compare the capital-only sums with and without counting W as VV.",
      "options": {
        "mode": "chronogram"
      }
    },
    {
      "kind": "constructed",
      "input": "Q",
      "period_id": "late-medieval",
      "values": [
        "500, 5 or 4 in the gloss"
      ],
      "convention_ids": [
        "medievalLetters"
      ],
      "why": "Cappelli’s Q and the Iberian forms Q and q have different reference values."
    },
    {
      "kind": "constructed",
      "input": "S",
      "period_id": "late-medieval",
      "values": [
        "70, 7 or 6 in the gloss"
      ],
      "convention_ids": [
        "medievalLetters"
      ],
      "why": "Capital and lowercase assignments differ across the cited lists."
    },
    {
      "kind": "constructed",
      "input": "IIII",
      "period_id": "modern",
      "values": [
        4
      ],
      "convention_ids": [
        "additive4",
        "clockIIII"
      ],
      "why": "Choose a clock-dial context to compare IIII with IV."
    },
    {
      "kind": "constructed",
      "input": "C4",
      "period_id": "late-medieval",
      "values": [
        "104 with mixed notation"
      ],
      "convention_ids": [
        "hybridNumerals",
        "ignored"
      ],
      "why": "An Arabic digit can contribute to an amount. The reader warns that it only used the Roman sign."
    },
    {
      "kind": "constructed",
      "input": "Paid .xx. for cloth and XII for thread.",
      "period_id": "late-medieval",
      "values": [
        ".xx. and XII"
      ],
      "convention_ids": [
        "distinctionMarks",
        "standard"
      ],
      "why": "Find both numeral tokens and open each reading separately.",
      "options": {
        "mode": "passage"
      }
    },
    {
      "kind": "constructed",
      "input": "2026",
      "period_id": "modern",
      "values": [
        2026
      ],
      "convention_ids": [
        "standard"
      ],
      "why": "Enter digits to write a year as MMXXVI.",
      "topic": "Convert a number",
      "start": 1
    },
    {
      "kind": "constructed",
      "input": "Chapter xiv",
      "period_id": "modern",
      "values": [
        14
      ],
      "convention_ids": [
        "standard"
      ],
      "why": "Lower-case xiv marks the fourteenth chapter.",
      "topic": "Chapter heading",
      "start": 2
    },
    {
      "kind": "constructed",
      "input": "Henry VIII",
      "period_id": "modern",
      "values": [
        8
      ],
      "convention_ids": [
        "standard"
      ],
      "why": "Read the name as Henry the Eighth.",
      "topic": "A monarch’s name",
      "start": 3
    },
    {
      "kind": "constructed",
      "input": "IIII",
      "period_id": "modern",
      "values": [
        4
      ],
      "convention_ids": [
        "clockIIII",
        "additive4"
      ],
      "why": "Some dials use four I signs instead of IV.",
      "topic": "Clock face",
      "start": 4
    },
    {
      "kind": "constructed",
      "input": "MCMXCIX",
      "period_id": "modern",
      "values": [
        1999
      ],
      "convention_ids": [
        "standard",
        "ad"
      ],
      "why": "A sample copyright date that uses three subtractive pairs.",
      "topic": "Film credits",
      "start": 5
    },
    {
      "kind": "constructed",
      "input": "MDCCCXCII",
      "period_id": "modern",
      "values": [
        1892
      ],
      "convention_ids": [
        "standard",
        "ad"
      ],
      "why": "A sample building date. XC contributes 90.",
      "topic": "Foundation stone",
      "start": 6
    },
    {
      "kind": "constructed",
      "input": "Pope John Paul II",
      "period_id": "modern",
      "values": [
        2
      ],
      "convention_ids": [
        "standard"
      ],
      "why": "The numeral reads as “the Second” after the name.",
      "topic": "A pope’s name"
    },
    {
      "kind": "constructed",
      "input": "Elizabeth II",
      "period_id": "modern",
      "values": [
        2
      ],
      "convention_ids": [
        "standard"
      ],
      "why": "The numeral reads as “the Second” after the name.",
      "topic": "A monarch’s name"
    },
    {
      "kind": "constructed",
      "input": "Super Bowl LIX",
      "period_id": "modern",
      "values": [
        59
      ],
      "convention_ids": [
        "standard"
      ],
      "why": "LIX labels the 59th Super Bowl.",
      "topic": "Sporting event"
    },
    {
      "kind": "constructed",
      "input": "Page xii",
      "period_id": "modern",
      "values": [
        12
      ],
      "convention_ids": [
        "standard"
      ],
      "why": "Roman numerals can number the pages before the main text.",
      "topic": "Book front matter"
    },
    {
      "kind": "constructed",
      "input": "Outline iii",
      "period_id": "modern",
      "values": [
        3
      ],
      "convention_ids": [
        "standard"
      ],
      "why": "An outline can count i, ii, iii, then iv.",
      "topic": "Outline numbering"
    },
    {
      "kind": "constructed",
      "input": "Rocky II",
      "period_id": "modern",
      "values": [
        2
      ],
      "convention_ids": [
        "standard"
      ],
      "why": "The numeral gives the film’s position in the series.",
      "topic": "Film sequel"
    }
  ]
};
