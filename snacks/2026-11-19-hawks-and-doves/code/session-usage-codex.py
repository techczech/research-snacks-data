"""Export only timestamps and cumulative token totals from a Codex transcript.
Usage: python session-usage-codex.py SESSION.jsonl OUTPUT.json
The site's session-usage.py reads Claude transcripts; this adapter handles Codex events.
"""
import json,sys
from pathlib import Path
first=last=None;last_usage=None;seen=set()
for line in Path(sys.argv[1]).open():
 d=json.loads(line)
 first=first or d.get('timestamp');last=d.get('timestamp') or last
 p=d.get('payload',{})
 if d.get('type')=='event_msg' and p.get('type')=='token_count':
  info=p.get('info') or {};u=info.get('total_token_usage')
  if u:
   seen.add(tuple(sorted(u.items())));last_usage=u
if not last_usage:raise SystemExit('No recorded Codex usage')
out={'model':'gpt-6.1-sol','start_utc':first,'snapshot_utc':last,'distinct_usage_events':len(seen),'input_tokens':last_usage['input_tokens'],'cached_input_tokens':last_usage.get('cached_input_tokens'),'output_tokens':last_usage['output_tokens'],'reasoning_output_tokens':last_usage.get('reasoning_output_tokens'),'coverage':'This research and drafting session through the snapshot. Later validation and publication excluded.'}
Path(sys.argv[2]).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
