import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from vedic_brahma_codec import decode_vedic_brahma_chunk as decode_vedic_brahma

base = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern\tools\extracted_stxt"
for fname in sorted(os.listdir(base)):
    p = os.path.join(base, fname)
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Split paragraphs
    paras = [p.strip() for p in text.split('\r') if p.strip()]
    
    vb_paras = []
    for para in paras:
        # Check if contains characteristic VedicBrahma patterns (ends with A or AA, or has typical glyphs)
        # Or decode and check devanagari ratio
        decoded = decode_vedic_brahma(para)
        deva_chars = len(re.findall(r'[\u0900-\u097f]', decoded))
        total_chars = len(decoded.replace(' ', ''))
        if total_chars > 8 and (deva_chars / total_chars) > 0.45:
            vb_paras.append((para, decoded))
            
    print(f"\n=======================================================")
    print(f"{fname}: Found {len(vb_paras)} VedicBrahma Sanskrit paragraphs")
    for orig, dec in vb_paras[:6]:
        print(f"  ORIG: {orig[:80]}")
        print(f"  DEVA: {dec[:80]}")
