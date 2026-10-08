import os
import sys

# Scan Devabhasha_master cxt files for embedded member names and types
cxt_files = [f for f in os.listdir("Devabhasha_master") if f.endswith(".cxt")]
print("CXT files in Devabhasha_master:", cxt_files)

def inspect_cxt(filename):
    path = os.path.join("Devabhasha_master", filename)
    with open(path, "rb") as f:
        data = f.read()
    # Find chunk tags like 'CAS*', 'MCst', 'VWSC', 'CASt'
    print(f"\n--- {filename} ({len(data)} bytes) ---")
    # Search for strings
    import re
    # printable strings of length >= 4
    strings = [s.decode('latin1', errors='ignore') for s in re.findall(b'[\x20-\x7e]{4,}', data)]
    # Filter for image names or interesting labels
    interesting = [s for s in strings if any(ext in s.lower() for ext in ['.jpg', '.bmp', '.pct', 'back', 'canvas', 'page', 'chap', 'frame'])]
    print("Interesting strings:", interesting[:20])

for cxt in ["chap03.cxt", "chap04.cxt", "chap08.cxt", "chapter9.cxt", "chapter10.cxt"]:
    if os.path.exists(os.path.join("Devabhasha_master", cxt)):
        inspect_cxt(cxt)
