import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

base_extracted = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern\tools\extracted_texts"

# Let's inspect chapter5, chapter6, chapter7, chap03
for fname in ["chap03.dxr.txt", "chap04.dxr.txt", "chapter5.dxr.txt", "chapter6.dxr.txt", "chapter7.dxr.txt", "chapter10.dxr.txt"]:
    path = os.path.join(base_extracted, fname)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='latin1', errors='ignore') as f:
        content = f.read()
    
    # Find chunks with VedicBrahma2 font
    vb_indices = [m.start() for m in re.finditer(r'VedicBrahma2', content)]
    print(f"=== {fname}: {len(vb_indices)} VedicBrahma2 references ===")
    
    # Also find text blocks near them
    for idx in vb_indices[:5]:
        snippet = content[max(0, idx-200):min(len(content), idx+500)]
        # Filter printable
        lines = [line.strip() for line in snippet.split('\n') if len(line.strip()) > 3]
        print(f"  --- Near offset {idx} ---")
        for l in lines[:8]:
            print(f"    {l[:80]}")
