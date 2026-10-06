import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

for fname in ["chapter5_stxt_0.txt", "chapter6_stxt_0.txt", "chapter7_stxt_0.txt", "chap03_stxt_0.txt"]:
    path = f"tools/extracted_stxt/{fname}"
    with open(path, "r", encoding="latin1") as f:
        content = f.read()
    # Split on CR/LF
    paras = [p.strip() for p in content.replace('\r', '\n').split('\n') if len(p.strip()) > 0]
    print(f"\n=======================================================")
    print(f"{fname}: {len(paras)} paragraphs, total {len(content)} chars")
    print(f"Sample paragraphs:")
    for i, p in enumerate(paras[:15]):
        print(f"  [{i+1}] {p[:90]}")
