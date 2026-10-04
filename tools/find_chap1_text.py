import os, re

txt_path = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern\tools\extracted_texts\chapter1.dxr.txt"
with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
meaningful = []
for line in lines:
    l = line.strip()
    if len(l) > 25 and not l.startswith('XFIR') and not l.startswith('pamm') and not l.startswith('ÿ') and not l.startswith('tSAC'):
        if any(w in l.lower() for w in ['sanskrit', 'language', 'india', 'jones', 'muller', 'william', 'schlegel', 'culture', 'sacred', 'ancient', 'literature']):
            meaningful.append(l)

print(f"Found {len(meaningful)} matching lines:")
for m in meaningful[:40]:
    print(f"  {m[:100]}")
