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
    stxts = [c for c in chunks if c[1] == 'STXT']
    for idx, (pos, tag, size, cdata) in enumerate(stxts):
        hdr_len, text_len, fmt_len = struct.unpack(">III", cdata[:12])
        raw_text = cdata[12:12+text_len].decode('latin1', errors='replace')
        fmt_data = cdata[12+text_len:12+text_len+fmt_len]
        print(f"=== {fname} fmt_len={fmt_len} ===")
        # In Director STXT formatting:
        # Often a count of runs (2 bytes or 4 bytes) followed by run records:
        # Each run: offset (4 bytes), fontId/style/size...
        # Let's inspect first 40 bytes of fmt_data
        print("  fmt_data hex start:", fmt_data[:48].hex())
        # Let's see how many 8-byte or 12-byte records
        num_runs = struct.unpack(">H", fmt_data[:2])[0]
        print(f"  num_runs (as uint16) = {num_runs}")
