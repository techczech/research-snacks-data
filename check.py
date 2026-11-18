"""Rebuild final tables in a temporary directory and compare every expected CSV."""
import argparse
import difflib
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('id',nargs='?',default='all',help='Full snack id, or all (default)')
a=p.parse_args()
ids=sorted(x.name for x in (ROOT/'snacks').iterdir() if x.is_dir())
if a.id!='all':
    if a.id not in ids: p.error('Unknown snack id')
    ids=[a.id]
failures=[]
for id in ids:
    snack=ROOT/'snacks'/id
    expected=sorted((snack/'expected').glob('*.csv'))
    if not expected: raise SystemExit(f'{id}: no expected tables')
    with tempfile.TemporaryDirectory(prefix='research-snack-') as tmp:
        result=subprocess.run([sys.executable,str(snack/'code/reproduce.py'),tmp],cwd=ROOT)
        if result.returncode:
            failures.append(id); continue
        for f in expected:
            actual=Path(tmp)/f.name
            before=f.read_text().splitlines(keepends=True)
            after=actual.read_text().splitlines(keepends=True) if actual.exists() else []
            if before!=after:
                failures.append(id+':'+f.name)
                sys.stdout.writelines(difflib.unified_diff(before,after,fromfile='expected/'+f.name,tofile='actual/'+f.name))
        if not any(f.startswith(id) for f in failures): print(f'PASS {id}: {len(expected)} tables')
if failures: raise SystemExit('FAIL '+', '.join(failures))
print(f'PASS: {len(ids)} snacks; all expected tables match.')
