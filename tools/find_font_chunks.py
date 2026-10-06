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
for fname in ["chap03.dxr", "chapter5.dxr", "chapter6.dxr", "chapter7.dxr"]:
    p = os.path.join(base, fname)
    chunks = parse_chunks(p)
    # Search for chunks containing font names
    font_chunks = []
    for c in chunks:
        if b'VedicBrahma' in c[3] or b'Palatino' in c[3] or b'Arial' in c[3]:
            font_chunks.append((c[1], c[2], c[3]))
    print(f"\n=======================================================")
    print(f"{fname}: {len(font_chunks)} chunks mentioning font names")
    for tag, size, cdata in font_chunks:
        # print strings inside
        strings = re.findall(rb'[A-Za-z0-9_\-\s]{3,30}', cdata)
        str_clean = [s.decode('latin1').strip() for s in strings if any(k in s for k in [b'Vedic', b'Palatino', b'Arial', b'Times'])]
        print(f"  [{tag} size {size}]: {str_clean[:5]}")
