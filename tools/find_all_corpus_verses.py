import json
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

sys.path.insert(0, 'tools')
from vedic_brahma_codec import decode_vedic_brahma_chunk

corpus_dir = 'tools/extracted_chapters_corpus'

for fname in sorted(os.listdir(corpus_dir)):
    if not fname.endswith('.json'): continue
    data = json.load(open(os.path.join(corpus_dir, fname), encoding='utf-8'))
    
    found_verses = []
    for chunk in data:
        for s in chunk['strings']:
            # A VedicBrahma string typically contains specific characters or ends with A / AA
            # or matches typical Sanskrit words
            if len(s) > 10 and (s.endswith(' A') or s.endswith(' AA') or 'AA' in s or 'A A' in s or any(k in s for k in ['izfo', 'ueks', 'czk', 'Hkw', 'nso', 'Jh', 'Lo'])):
                try:
                    deva = decode_vedic_brahma_chunk(s)
                    deva_chars = len(re.findall(r'[\u0900-\u097f]', deva))
                    if deva_chars > 8:
                        found_verses.append((s, deva))
                except Exception as e:
                    pass
    if found_verses:
        print(f"\n=======================================================")
        print(f"{fname}: {len(found_verses)} potential VedicBrahma verses")
        for orig, deva in found_verses[:5]:
            print(f"  ORIG: {orig[:70]}")
            print(f"  DEVA: {deva[:70]}")
