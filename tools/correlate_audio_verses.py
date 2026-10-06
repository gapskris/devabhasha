import json
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

sys.path.insert(0, 'tools')
from vedic_brahma_codec import decode_vedic_brahma_chunk

corpus_dir = 'tools/extracted_chapters_corpus'

for ch_name in ["chapter1.dxr.json", "chapter2.dxr.json", "chap03.dxr.json", "chap04.dxr.json", "chapter5.dxr.json", "chapter6.dxr.json", "chapter7.dxr.json", "chapter10.dxr.json"]:
    path = os.path.join(corpus_dir, ch_name)
    if not os.path.exists(path): continue
    data = json.load(open(path, encoding='utf-8'))
    
    print(f"\n=======================================================")
    print(f"=== {ch_name} ({len(data)} chunks) ===")
    
    # In each chunk, look for sound references, titles, and Sanskrit verses
    for c in data:
        strings = c['strings']
        sounds = [s for s in strings if '.wav' in s or any(s.startswith(p) for p in ['chapter', 'chap', 'c2_', 'Alphabet', 'Bhagavadgita', 'Ka-varga', 'Cha-varga', 'Tta-varga', 'Ta-varga', 'Pa-varga', 'Ishatsparsha', 'ushman', 'Sandhi', 'H.'])]
        vb_verses = []
        for s in strings:
            if len(s) > 10 and (s.endswith(' A') or s.endswith(' AA') or 'AA' in s or any(k in s for k in ['izfo', 'ueks', 'czk', 'Hkw', 'nso', 'Jh', 'Lo', 'vdnZ'])):
                dec = decode_vedic_brahma_chunk(s)
                if len(re.findall(r'[\u0900-\u097f]', dec)) > 8:
                    vb_verses.append((s, dec))
                    
        if sounds or vb_verses:
            print(f" Chunk #{c['chunk_idx']} (size {c['size']}):")
            if sounds:
                print(f"   Sounds: {sounds}")
            if vb_verses:
                for orig, dec in vb_verses[:3]:
                    print(f"   Verse [ORIG]: {orig[:60]}")
                    print(f"   Verse [DEVA]: {dec[:60]}")
