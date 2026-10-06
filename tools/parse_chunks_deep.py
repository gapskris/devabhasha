import struct, os, re, sys
from collections import Counter

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def parse_chunks(path):
    if not os.path.exists(path): return []
    with open(path, "rb") as f:
        data = f.read()
    magic = data[:4]
    endian = '<' if magic == b'XFIR' else '>'
    pos = 12
    chunks = []
    while pos < len(data) - 8:
        tag_bytes = data[pos:pos+4]
        if magic == b'XFIR':
            tag = tag_bytes[::-1].decode('latin1', errors='replace')
        else:
            tag = tag_bytes.decode('latin1', errors='replace')
        size = struct.unpack(f"{endian}I", data[pos+4:pos+8])[0]
        chunks.append((pos, tag, size, data[pos+8:pos+8+size]))
        pos += 8 + size + (size % 2)
    return chunks

base = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_master"
for fname in ["shlokas.dxr", "chapter5.dxr", "chapter6.dxr", "chapter7.dxr", "chap03.dxr"]:
    p = os.path.join(base, fname)
    chunks = parse_chunks(p)
    counts = Counter(c[1] for c in chunks)
    print(f"=== {fname}: {len(chunks)} chunks ===")
    print(f"  Chunk types: {dict(counts)}")
    for pos, tag, size, cdata in chunks:
        if tag in ['XMED', 'STXT', 'text', 'VWSC', 'CAS*']:
            # look for strings inside
            s_matches = re.findall(rb'[\x20-\x7e\xa0-\xff]{12,}', cdata)
            clean = [m.decode('latin1', errors='ignore') for m in s_matches if not m.startswith(b'000') and not m.startswith(b'FFF')]
            if clean:
                print(f"  [{tag} size {size}]: {clean[:3]}")
