"""Print a Codex session's measured model usage and timestamp span. No transcript text is printed.
Usage: python session-usage-codex.py SESSION_JSONL
The companion website's session-usage.py reads Claude-format transcripts; Codex has different fields.
Input includes cached tokens as a subset. Do not add cache tokens to input a second time.
"""
import json,sys
from datetime import datetime
from pathlib import Path
rows=[];first=None;last=None;seen=set();model='unknown'
for line in Path(sys.argv[1]).open():
 d=json.loads(line);ts=d.get('timestamp');first=first or ts;last=ts or last
 p=d.get('payload',{})
 if d.get('type')=='turn_context':model=p.get('model',model)
 if d.get('type')=='token_usage_record' and p.get('response_id') not in seen:
  seen.add(p.get('response_id'));rows.append(p['usage'])
read=sum(r.get('input_tokens',0) for r in rows);cache=sum(r.get('cached_input_tokens',0) for r in rows)
written=sum(r.get('output_tokens',0) for r in rows);reasoning=sum(r.get('reasoning_output_tokens',0) for r in rows)
print(f'{model} | Research, coding, analysis, writing and verification | {len(rows)} | {read:,} | {written:,}')
print(f'Snapshot {first} to {last}; cached input subset {cache:,}; reasoning output subset {reasoning:,}.')
print('Input counts include repeated cached history. Output includes reported reasoning tokens. This is usage, not a charge.')
