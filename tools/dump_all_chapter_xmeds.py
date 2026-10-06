import struct, os, re, sys, json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tools'))
from vedic_brahma_codec import decode_vedic_brahma_chunk

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
out_dir = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern\tools\extracted_chapters_corpus"
os.makedirs(out_dir, exist_ok=True)

for fname in sorted(os.listdir(base)):
    if not fname.endswith('.dxr'): continue
    p = os.path.join(base, fname)
    chunks = parse_chunks(p)
    xmeds = [c for c in chunks if c[1] == 'XMED']
    
    chapter_corpus = []
    for idx, (pos, tag, size, cdata) in enumerate(xmeds):
        # find string sequences
        strings = re.findall(rb'[\x20-\x7e\xa0-\xff]{4,}', cdata)
        clean = []
        for s in strings:
            try:
                dec = s.decode('latin1').strip()
                if not dec.startswith('000') and not dec.startswith('FFF') and not dec.startswith('D:\\'):
                    clean.append(dec)
            except:
                pass
        if clean:
            chapter_corpus.append({
                "chunk_idx": idx,
                "size": size,
                "strings": clean
            })
            
    out_file = os.path.join(out_dir, f"{fname}.json")
    with open(out_file, "w", encoding="utf-8") as out:
        json.dump(chapter_corpus, out, ensure_ascii=False, indent=2)
    print(f"{fname}: saved {len(chapter_corpus)} text chunks to {out_file}")
