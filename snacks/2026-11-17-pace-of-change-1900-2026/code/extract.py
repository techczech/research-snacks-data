"""Submit an IPUMS USA extract described by a JSON spec file, wait, download data and codebook.
Key comes from env IPUMS_API_KEY (injected by bws_manager run). Usage: python3 -I extract.py SPEC.json OUTDIR"""
import json, os, sys, time, urllib.request

KEY = os.environ["IPUMS_API_KEY"]
SPEC, OUT = sys.argv[1], sys.argv[2]
BASE, Q = "https://api.ipums.org/extracts", "?collection=usa&version=2"


def call(url, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers={"Authorization": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)


ext = call(BASE + Q, json.load(open(SPEC)))
n = ext["number"]
print("submitted", n, flush=True)
while True:
    ext = call(f"{BASE}/{n}{Q}")
    print("status", ext["status"], flush=True)
    if ext["status"] == "completed":
        break
    if ext["status"] in ("failed", "canceled"):
        sys.exit(json.dumps(ext)[:2000])
    time.sleep(30)
for kind in ("data", "ddiCodebook"):
    url = ext["downloadLinks"][kind]["url"]
    dest = os.path.join(OUT, os.path.basename(url))
    with urllib.request.urlopen(urllib.request.Request(url, headers={"Authorization": KEY})) as r, open(dest, "wb") as f:
        while chunk := r.read(1 << 20):
            f.write(chunk)
    print("saved", dest, os.path.getsize(dest), flush=True)
