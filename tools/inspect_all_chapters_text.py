import os, re, json

base_extracted = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern\tools\extracted_texts"

def get_chapter_curriculum_text(dxr_name):
    txt_path = os.path.join(base_extracted, f"{dxr_name}.txt")
    if not os.path.exists(txt_path):
        return []
    with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    clean = []
    seen = set()
    for l in lines:
        s = l.strip()
        if (len(s) > 35 and not s.startswith(';') and not s.startswith('XFIR') and 
            not s.startswith('pamm') and not s.startswith('ÿ') and not s.startswith('tSAC') and
            not s.startswith('Arial') and not s.startswith('Times') and not s.startswith('Courier') and
            not s.startswith('Macromedia') and not s.startswith('===') and '=>' not in s):
            
            s_clean = re.sub(r'^[0-9A-Fa-f]{3,4},\s*', '', s)
            s_clean = re.sub(r'^0000[0-9A-Fa-f\x00\s]+,\s*', '', s_clean)
            if (len(s_clean) > 35 and s_clean not in seen and 
                not s_clean.startswith('D:\\') and not s_clean.startswith('#my') and
                not s_clean.startswith('kMoaCf') and not s_clean.startswith('System')):
                seen.add(s_clean)
                clean.append(s_clean)
    return clean

chapters = [
    "chapter1.dxr", "chapter2.dxr", "chap03.dxr", "chap04.dxr", "chapter5.dxr",
    "chapter6.dxr", "chapter7.dxr", "chap08.dxr", "chapter9.dxr", "chapter10.dxr"
]

for ch in chapters:
    texts = get_chapter_curriculum_text(ch)
    print(f"\n=== {ch}: {len(texts)} curriculum passages ===")
    for i, t in enumerate(texts[:5]):
        print(f"[{i+1}] {t[:120]}...")
