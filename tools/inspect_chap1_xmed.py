import struct, os, re

def parse_chunks(path):
    with open(path, "rb") as f:
        data = f.read()
    magic = data[:4]
    endian = '<' if magic == b'XFIR' else '>'
    pos = 12
    chunks = []
    while pos < len(data) - 8:
        tag = data[pos:pos+4][::-1].decode('latin1', errors='replace')
        size = struct.unpack(f"{endian}I", data[pos+4:pos+8])[0]
        chunks.append((pos, tag, size, data[pos+8:pos+8+size]))
        pos += 8 + size + (size % 2)
    return chunks

base = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_master"
chunks = parse_chunks(os.path.join(base, "chapter1.dxr"))

for idx, (pos, tag, size, cdata) in enumerate(chunks):
    if tag == 'XMED':
        # look for text
        matches = re.findall(rb'[\x20-\x7e\xa0-\xff]{20,}', cdata)
        texts = [m.decode('latin1', errors='replace').strip() for m in matches if len(m.strip()) > 30]
        if texts:
            print(f"Chunk {idx} (XMED, size {size}): {len(texts)} text strings")
            for t in texts:
                if not t.startswith('Palatino') and not t.startswith('Mac:Courier'):
                    print(f"  -> {t[:120]}")
