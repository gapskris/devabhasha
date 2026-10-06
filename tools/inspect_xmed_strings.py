import struct, os, re, sys

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
        tag = tag_bytes[::-1].decode('latin1', errors='replace') if magic == b'XFIR' else tag_bytes.decode('latin1', errors='replace')
        size = struct.unpack(f"{endian}I", data[pos+4:pos+8])[0]
        chunks.append((pos, tag, size, data[pos+8:pos+8+size]))
        pos += 8 + size + (size % 2)
    return chunks

base = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_master"
for fname in ["chap03.dxr", "chapter6.dxr", "chapter7.dxr"]:
    p = os.path.join(base, fname)
    chunks = parse_chunks(p)
    xmeds = [c for c in chunks if c[1] == 'XMED' and b'VedicBrahma2' in c[3]]
    print(f"\n=======================================================")
    print(f"{fname}: {len(xmeds)} XMED chunks with VedicBrahma2")
    for idx, (pos, tag, size, cdata) in enumerate(xmeds[:6]):
        # Extract ASCII strings
        strings = re.findall(rb'[\x20-\x7e\xa0-\xff]{6,}', cdata)
        clean = []
        for s in strings:
            try:
                dec = s.decode('latin1').strip()
                if not dec.startswith('000') and not dec.startswith('FFF') and not dec.startswith('D:\\') and dec not in ['Arial', 'VedicBrahma2', 'VedicBrahma2 Bold', 'Times New Roman']:
                    clean.append(dec)
            except:
                pass
        print(f"--- Chunk #{idx} (size {size}) ---")
        for c in clean[:6]:
            print(f"    {c[:100]}")
