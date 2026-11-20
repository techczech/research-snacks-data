"""Submit an IPUMS USA extract (1950 1% + 2010 ACS; OCC1950, OCC, EMPSTAT), wait, download.
Key comes from env IPUMS_API_KEY (injected by bws_manager run). Usage: python3 -I extract.py OUTDIR
"""
import json, os, sys, time, urllib.request

KEY = os.environ["IPUMS_API_KEY"]
OUT = sys.argv[1]
BASE = "https://api.ipums.org/extracts"
Q = "?collection=usa&version=2"


def call(url, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers={"Authorization": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


spec = {
    "description": "Short-lived occupations 1950-2019 (OCC1990)",
    "dataStructure": {"rectangular": {"on": "P"}},
    "dataFormat": "csv",
    "samples": {s: {} for s in ["us1950a", "us1960a", "us1970a", "us1980b", "us1990b", "us2000b", "us2010a", "us2019a"]},
    "variables": {"OCC1990": {}, "OCC": {}, "EMPSTAT": {"caseSelections": {"general": ["1"]}}},
}
ext = call(BASE + Q, spec)
n = ext["number"]
print("submitted", n, flush=True)
while True:
    ext = call(f"{BASE}/{n}{Q}")
    st = ext["status"]
    print("status", st, flush=True)
    if st == "completed":
        break
    if st in ("failed", "canceled"):
        sys.exit(json.dumps(ext)[:2000])
    time.sleep(30)

for kind in ("data", "ddiCodebook"):
    link = ext["downloadLinks"].get(kind)
    if not link:
        continue
    url = link["url"]
    dest = os.path.join(OUT, os.path.basename(url))
    req = urllib.request.Request(url, headers={"Authorization": KEY})
    with urllib.request.urlopen(req) as r, open(dest, "wb") as f:
        while chunk := r.read(1 << 20):
            f.write(chunk)
    print("saved", dest, os.path.getsize(dest), flush=True)
