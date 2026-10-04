import os
import re
import zlib
import sys

sys.stdout.reconfigure(encoding='utf-8')

master_swf_dir = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_master\swf"

def extract_strings_from_swf(swf_path):
    with open(swf_path, 'rb') as f:
        header = f.read(8)
        if len(header) < 8:
            return []
        magic = header[:3]
        if magic == b'CWS':
            compressed = f.read()
            try:
                data = header[:8] + zlib.decompress(compressed)
            except Exception:
                data = header + compressed
        else:
            f.seek(0)
            data = f.read()

    # Extract printable ASCII and Latin-1 strings
    raw_strings = re.findall(rb'[\x20-\x7e\xa0-\xff]{4,}', data)
    clean = []
    seen = set()
    for r in raw_strings:
        try:
            s = r.decode('latin1', errors='ignore').strip()
            if len(s) >= 4 and s not in seen and not s.startswith('Arial') and not s.startswith('Times'):
                seen.add(s)
                clean.append(s)
        except:
            pass
    return clean

def scan_all_swfs():
    for root, dirs, files in os.walk(master_swf_dir):
        for file in sorted(files):
            if file.endswith('.swf'):
                p = os.path.join(root, file)
                rel_path = os.path.relpath(p, master_swf_dir)
                strings = extract_strings_from_swf(p)
                meaningful = [s for s in strings if len(s) > 15]
                if meaningful:
                    print(f"\n=======================================================")
                    print(f"SWF: {rel_path} ({len(meaningful)} strings)")
                    print(f"=======================================================")
                    for m in meaningful[:15]:
                        print(f"   {m[:90]}")

scan_all_swfs()
