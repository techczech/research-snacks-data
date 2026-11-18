"""When did job titles enter written English? Google Books Ngram (English corpus, 1880-2022).
For each title: the take-off year, when its frequency first reaches 10% of its 1880-2022 peak, and the peak year.
Two lists, fixed before looking at the data: titles tied to technologies that arrived 1880-1960 and titles
tied to technologies that arrived 1950-2025. Usage: python3 -I ngrams.py OUT_DIR"""
import csv, json, os, sys, time, urllib.parse, urllib.request

OUT = sys.argv[1]
Y0, Y1 = 1880, 2022
LISTS = {
    "Technologies of 1880-1960": [
        "telephone operator", "switchboard operator", "lineman", "electrician", "chauffeur", "auto mechanic",
        "filling station attendant", "aviator", "airline pilot", "stewardess", "air traffic controller",
        "radio announcer", "radio operator", "disc jockey", "movie projectionist", "cameraman", "film editor",
        "sound engineer", "recording engineer", "x-ray technician", "typist", "keypunch operator",
        "comptometer operator", "television announcer", "television producer"],
    "Technologies of 1950-2025": [
        "computer programmer", "systems analyst", "computer operator", "data processing manager",
        "software engineer", "software developer", "database administrator", "network administrator",
        "web designer", "web developer", "webmaster", "help desk technician", "data scientist", "data analyst",
        "UX designer", "product manager", "social media manager", "content creator", "app developer",
        "cybersecurity analyst", "machine learning engineer", "cloud architect", "drone pilot",
        "sonographer", "prompt engineer"],
}


def fetch(terms):
    q = urllib.parse.urlencode({"content": ",".join(terms), "year_start": Y0, "year_end": Y1, "corpus": "en", "smoothing": 0, "case_insensitive": "true"})
    req = urllib.request.Request("https://books.google.com/ngrams/json?" + q, headers={"User-Agent": "research-snacks/1.0"})
    response = json.load(urllib.request.urlopen(req))
    os.makedirs(OUT, exist_ok=True)
    snapshots = os.path.join(OUT, "ngram-responses.jsonl")
    with open(snapshots, "a") as f:
        f.write(json.dumps({"query": dict(urllib.parse.parse_qsl(q)), "response": response}) + "\n")
    return response


rows, series = [], []
for group, terms in LISTS.items():
    for k in range(0, len(terms), 8):
        batch = terms[k:k + 8]
        got = {}
        for s in fetch(batch):
            name = s["ngram"].replace(" (All)", "").lower()
            if name in got and "(All)" not in s["ngram"]:
                continue
            got[name] = s["timeseries"]
        for t in batch:
            ts = got.get(t.lower())
            if not ts or max(ts) == 0:
                rows.append({"group": group, "title": t, "take_off_year": "", "peak_year": "", "peak_per_billion": 0}); continue
            pk = max(ts)
            take = next(Y0 + i for i, v in enumerate(ts) if v >= 0.1 * pk)
            rows.append({"group": group, "title": t, "take_off_year": take, "peak_year": Y0 + ts.index(pk), "peak_per_billion": round(pk * 1e9, 1)})
            series += [{"title": t, "group": group, "year": Y0 + i, "per_billion": round(v * 1e9, 2)} for i, v in enumerate(ts)]
        time.sleep(1.5)
os.makedirs(OUT, exist_ok=True)
for name, data in (("ngram_takeoff.csv", rows), ("ngram_series.csv", series)):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(data[0])); w.writeheader(); w.writerows(data)
for r in sorted(rows, key=lambda r: (r["group"], r["take_off_year"] or 9999)):
    print(r["group"][:16], r["title"].ljust(28), r["take_off_year"], r["peak_year"], r["peak_per_billion"])
