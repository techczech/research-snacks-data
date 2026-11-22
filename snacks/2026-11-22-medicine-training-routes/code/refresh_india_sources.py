"""Fetch the NMC originals from the migrated public site; archive only hashes.

Run with the source-retrieval Python requirements. Whole third-party documents
remain in ignored scratch. This script does not reinterpret their content.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, urllib.request
ROOT = Path(__file__).resolve().parents[3]
CACHE = ROOT / 'scratch/medicine-training-routes'
OUT = Path(__file__).resolve().parents[1] / 'data/india-source-retrieval.json'
URLS = {
    'in-cbme2024': 'https://nmc.org.in/whats-new/download/378',
    'in-gmer2019': 'https://nmc.org.in/19GraduateMedicalEducationRegulations1997Amendment04112019-2.pdf',
    'in-gmer2023': 'https://application.nmc.org.in/storage/nmc_gazette_notifications/246254.pdf',
    'in-crmi2021': 'https://application.nmc.org.in/storage/nmc_gazette_notifications/231280.pdf',
    'in-pg2023': 'https://application.nmc.org.in/storage/nmc_gazette_notifications/PGMER%202023.pdf',
    'in-next2023': 'https://nmc.org.in/whats-new/download/589',
}
if __name__ == '__main__':
    from pypdf import PdfReader
    CACHE.mkdir(parents=True, exist_ok=True)
    OUT.parent.mkdir(exist_ok=True)
    rows = []
    for key, url in URLS.items():
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=45) as response:
            body = response.read()
            final = response.url
        if not body.startswith(b'%PDF'): raise ValueError(f'{key}: not a PDF')
        path = CACHE / (key + '.raw')
        path.write_bytes(body)
        (CACHE / (key + '.txt')).write_text('\n'.join(p.extract_text() or '' for p in PdfReader(path).pages))
        rows.append(dict(id=key, url=url, retrieved_url=final,
                         accessed=datetime.now(timezone.utc).isoformat(),
                         sha256=hashlib.sha256(body).hexdigest(), bytes=len(body)))
    OUT.write_text(json.dumps(rows, indent=2) + '\n')
    print(f'Verified {len(rows)} original NMC PDFs; source bodies kept in ignored scratch.')
