"""Scan tracked content and every historical blob without printing matched text.
Names, source licences and scientific interpretation still require reading.
"""
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])
patterns={
    'home path':re.compile(rb'/(?:Users|home)/|~/(?:gitrepos|Documents)/'),
    'private estate path':re.compile(rb'_(?:COORDINATION|CONTEXT|LEARNINGLOG|MACHINECONFIG|SKILLS|BACKLOG|DTC)\b'),
    'address':re.compile(rb'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'),
    'machine address':re.compile(rb'\b[A-Za-z0-9-]+\.(?:local|ts\.net)\b'),
    'credential':re.compile(rb'(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)'),
}
fail=[];count=0
for path in git('ls-files','-z').decode().split('\0'):
    if not path:continue
    data=(ROOT/path).read_bytes(); count+=1
    for label,pat in patterns.items():
        if pat.search(data):fail.append((path,label))
try:
    objects=git('rev-list','--objects','--all').decode().splitlines()
except subprocess.CalledProcessError:
    objects=[]
blobs=0
for row in objects:
    oid=row.split(' ',1)[0]
    if git('cat-file','-t',oid).strip()!=b'blob':continue
    blobs+=1;data=git('cat-file','blob',oid)
    for label,pat in patterns.items():
        if pat.search(data):fail.append(('historical blob '+oid,label))
if fail:
    for path,label in fail:print(f'FAIL {path}: {label}')
    raise SystemExit(1)
print(f'PASS privacy patterns: {count} tracked files; {blobs} historical blobs. No matched content printed.')
