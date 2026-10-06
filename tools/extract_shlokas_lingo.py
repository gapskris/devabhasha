import os, re, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

p = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern\tools\extracted_texts\shlokas.dxr.txt"
with open(p, "r", encoding="latin1") as f:
    text = f.read()

# Search for play, sound, puppetSound, go to, or .wav
scripts = re.findall(r'(?:on\s+mouseUp.*?end|on\s+mouseDown.*?end|play.*?sound.*?\n|puppetSound.*?\n)', text, re.DOTALL | re.IGNORECASE)
print(f"Found {len(scripts)} script matches in shlokas.dxr.txt")
for s in scripts[:20]:
    print("---------------------------------------------")
    print(s[:250])
