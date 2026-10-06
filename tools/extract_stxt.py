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
        if magic == b'XFIR':
            tag = tag_bytes[::-1].decode('latin1', errors='replace')
        else:
            tag = tag_bytes.decode('latin1', errors='replace')
        size = struct.unpack(f"{endian}I", data[pos+4:pos+8])[0]
        chunks.append((pos, tag, size, data[pos+8:pos+8+size]))
        pos += 8 + size + (size % 2)
    return chunks

base = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_master"
for fname in sorted(os.listdir(base)):
    if not fname.endswith('.dxr'): continue
    p = os.path.join(base, fname)
    chunks = parse_chunks(p)
    stxts = [c for c in chunks if c[1] == 'STXT']
    if not stxts: continue
    print(f"\n=======================================================")
    print(f"{fname}: {len(stxts)} STXT chunks")
    for i, (pos, tag, size, cdata) in enumerate(stxts):
        # Director STXT: usually header (12 bytes) or length prefix
        # Let's inspect first 30 bytes
        # In Director 5/6/7, STXT data often has a 4-byte or 8-byte header followed by text
        print(f"  STXT #{i} (size {size}, offset {pos}): header hex = {cdata[:16].hex()}")
        # Let's find length of string
        # Often cdata starts with textLength (4 bytes, big endian or little endian)
        text_len = struct.unpack(">I", cdata[:4])[0]
        text_len_le = struct.unpack("<I", cdata[:4])[0]
        print(f"    text_len BE: {text_len}, LE: {text_len_le}")
        # Let's extract ascii text from cdata
        text_data = cdata[4:4+text_len] if text_len < size else cdata[12:]
        # print first 150 chars
        sample = text_data[:150].decode('latin1', errors='replace').replace('\r', ' ').replace('\n', ' ')
        print(f"    Sample: {sample}")
