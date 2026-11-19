"""Summarise this Codex JSONL without exporting private records.
Usage: python3 session_usage_codex.py SESSION_JSONL
Input tokens already include cached_input_tokens. Do not double count.
"""
from pathlib import Path
import sys,json,datetime
rows=[]
with Path(sys.argv[1]).open() as f:
 for line in f:
  try:r=json.loads(line)
  except ValueError:continue
  rows.append(r)
usage=[r for r in rows if r.get('type')=='event_msg' and r.get('payload',{}).get('type')=='token_count' and r.get('payload',{}).get('info')]
assert usage
last=usage[-1];u=last['payload']['info']['total_token_usage']
# Count unique sampling records, not tool invocations or assistant message fragments.
calls=len({(r['timestamp'],r.get('ordinal')) for r in usage})
start=rows[0]['timestamp'];end=last['timestamp']
a=datetime.datetime.fromisoformat(start.replace('Z','+00:00'));b=datetime.datetime.fromisoformat(end.replace('Z','+00:00'))
print(json.dumps({'start_utc':start,'snapshot_utc':end,'elapsed_minutes':round((b-a).total_seconds()/60,1),'sampling_usage_records':calls,'input_tokens':u['input_tokens'],'cached_input_tokens_subset':u.get('cached_input_tokens'),'output_tokens':u['output_tokens'],'reasoning_output_tokens_subset':u.get('reasoning_output_tokens'),'scope':'This research session through snapshot; input includes cached context; no transcript exported'},indent=2))
