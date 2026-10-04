import struct, os, re, json

def parse_chunks(path):
    if not os.path.exists(path): return []
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

def extract_clean_texts_from_chunks(chunks):
    results = []
    for i, (pos, tag, size, cdata) in enumerate(chunks):
        if tag in ['XMED', 'STXT', 'snd ']:
            # find text
            matches = re.findall(rb'[\x20-\x7e\xa0-\xff]{10,}', cdata)
            for m in matches:
                try:
                    s = m.decode('latin1').strip()
                    if (len(s) > 15 and not s.startswith('000') and not s.startswith('FFF')
                        and not s.startswith('D:\\') and not s.startswith('Arial')):
                        results.append(s)
                except:
                    pass
    return results

base = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_master"
for ch in ["chapter1.dxr", "chapter1.cxt", "chapter2.dxr", "chapter10.dxr", "acknowledge.cxt"]:
    p = os.path.join(base, ch)
    chunks = parse_chunks(p)
    txts = extract_clean_texts_from_chunks(chunks)
    print(f"{ch}: {len(chunks)} chunks, {len(txts)} clean text strings")
    for t in txts[:3]:
        print(f"   {t[:80]}")
