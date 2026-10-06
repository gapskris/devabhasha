import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

data = json.load(open('tools/extracted_chapters_corpus/shlokas.dxr.json', encoding='utf-8'))
print(f"Total chunks in shlokas.dxr: {len(data)}")
for idx, c in enumerate(data):
    non_num_strings = [s for s in c['strings'] if len(s) > 8 and not s.startswith('-') and not s.startswith('4800') and not s.startswith('001')]
    if non_num_strings:
        print(f"\n--- Chunk {c['chunk_idx']} ({len(non_num_strings)} strings) ---")
        for s in non_num_strings[:6]:
            print(f"   {s[:90]}")
