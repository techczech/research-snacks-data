"""Render the exact EU distribution as a PNG from the checked counts."""
import csv, json, sys
from pathlib import Path
import vl_convert as vlc
p=Path(__file__).resolve().parents[1]
spec=json.loads((p/'data/eu-chart.vl.json').read_text())
with (p/'expected/eu-duration-distribution.csv').open() as f:rows=list(csv.DictReader(f))
spec['data']={'values':rows};spec['width']=680
Path(sys.argv[1]).write_bytes(vlc.vegalite_to_png(spec,scale=2))
