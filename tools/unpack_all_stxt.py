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
out_dir = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern\tools\extracted_stxt"
os.makedirs(out_dir, exist_ok=True)

for fname in sorted(os.listdir(base)):
    if not fname.endswith('.dxr'): continue
    p = os.path.join(base, fname)
    chunks = parse_chunks(p)
    stxts = [c for c in chunks if c[1] == 'STXT']
    for idx, (pos, tag, size, cdata) in enumerate(stxts):
        if len(cdata) < 12: continue
        hdr_len, text_len, fmt_len = struct.unpack(">III", cdata[:12])
        raw_text = cdata[12:12+text_len]
        text_str = raw_text.decode('latin1', errors='replace')
        
        stem = fname.replace('.dxr', '')
        out_path = os.path.join(out_dir, f"{stem}_stxt_{idx}.txt")
        with open(out_path, "w", encoding="utf-8") as out:
            out.write(text_str)
            
        print(f"Extracted {stem} STXT: text_len={text_len}, saved {len(text_str)} chars to {out_path}")
        # Print sample
        lines = [l.strip() for l in text_str.split('\r') if l.strip()]
        for l in lines[:4]:
            print(f"    {l[:100]}")
