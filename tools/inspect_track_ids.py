"""
Compilation and Verification of all 149 Authentic Sanskrit Recitations
for Devabhāṣā Modern (1997 CD-ROM -> 2026 Modern Web Application)
"""

import os
import sys
import json
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Let's inspect the current track IDs in data.json
with open("content/data.json", "r", encoding="utf-8") as f:
    db = json.load(f)

current_tracks = db.get("shlokasConcordance", [])
print(f"Total current concordance entries: {len(current_tracks)}")
print("Track IDs by Chapter:")
by_ch = {}
for t in current_tracks:
    cid = t["chapterId"]
    by_ch.setdefault(cid, []).append(t["id"])

for cid, tids in sorted(by_ch.items()):
    print(f"  Chapter {cid:02d} ({len(tids)} tracks): {tids[:4]} ... {tids[-2:] if len(tids)>4 else ''}")
