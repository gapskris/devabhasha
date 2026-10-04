import os, glob, re

base = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_master"

def extract_strings_from_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    # Find ascii and printable sequences
    matches = re.findall(rb'[\x20-\x7e\r\n\t]{6,}', data)
    strings = [m.decode('latin1', errors='replace').strip() for m in matches if len(m.strip()) > 10]
    return strings

cxt_files = sorted(glob.glob(os.path.join(base, "*.cxt")))
print(f"Inspecting {len(cxt_files)} CXT files...")

for cxt in cxt_files:
    fname = os.path.basename(cxt)
    strs = extract_strings_from_file(cxt)
    print(f"\n--- {fname} (found {len(strs)} text blocks) ---")
    for s in strs[:8]:
        preview = s.replace('\n', ' ')[:100]
        print(f"  {preview}")
