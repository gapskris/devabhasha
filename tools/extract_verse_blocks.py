import sys, os, re, json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

sys.path.insert(0, 'tools')
from vedic_brahma_codec import decode_vedic_brahma_chunk

def extract_chapter_verses_and_context(stxt_filename):
    path = os.path.join("tools", "extracted_stxt", stxt_filename)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="latin1") as f:
        content = f.read()
    
    # Split lines regardless of newline convention
    paras = [p.strip() for p in content.splitlines() if p.strip()]
    
    entries = []
    for i, p in enumerate(paras):
        # Check if line looks like VedicBrahma verse (ends in A or AA, or has typical indicators)
        if len(p) > 10 and (p.endswith(' A') or p.endswith(' AA') or 'AA' in p or ' A ' in p):
            prev_ctx = paras[max(0, i-2):i]
            next_ctx = paras[i+1:min(len(paras), i+3)]
            entries.append({
                "idx": i,
                "raw": p,
                "prev": prev_ctx,
                "next": next_ctx
            })
    return entries

for fname in ["chap03_stxt_0.txt", "chap04_stxt_0.txt", "chapter5_stxt_0.txt", "chapter6_stxt_0.txt", "chapter7_stxt_0.txt", "chapter10_stxt_0.txt"]:
    entries = extract_chapter_verses_and_context(fname)
    print(f"\n=======================================================")
    print(f"{fname}: Found {len(entries)} candidate verse blocks")
    for e in entries[:4]:
        print(f"  Line {e['idx']}: {e['raw'][:60]}")
        print(f"    Context after: {e['next'][0][:70] if e['next'] else 'None'}")
