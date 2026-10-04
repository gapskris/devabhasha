import os, glob, re, json

base = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_master"
out_dir = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern\tools\extracted_texts"
os.makedirs(out_dir, exist_ok=True)

files = sorted(glob.glob(os.path.join(base, "*.cxt")) + glob.glob(os.path.join(base, "*.dxr")))

for fpath in files:
    fname = os.path.basename(fpath)
    with open(fpath, "rb") as f:
        data = f.read()
    
    # Extract text strings: both standard Latin and high-byte strings
    raw_matches = re.findall(rb'[\x20-\x7e\xa0-\xff]{5,}', data)
    lines = []
    for m in raw_matches:
        try:
            s = m.decode('latin1').strip()
            # Filter binary noise
            if len(s) > 4 and not re.match(r'^[0-9A-Fa-f]{8,}$', s) and not s.startswith("000"):
                lines.append(s)
        except:
            pass
            
    out_f = os.path.join(out_dir, f"{fname}.txt")
    with open(out_f, "w", encoding="utf-8") as out:
        out.write(f"=== {fname} ({len(lines)} segments) ===\n\n")
        out.write("\n".join(lines))
        
print(f"Extracted texts for {len(files)} files into {out_dir}")
