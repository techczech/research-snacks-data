"""Rebuild this snack from its shareable inputs; called by check.py."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'code'))
from reproduce import reproduce
if __name__=='__main__':
    reproduce(Path(__file__).resolve().parents[1],sys.argv[1])
