import os, re

base = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_master"
with open(os.path.join(base, "shlokas.cxt"), "rb") as f:
    data = f.read()

# Search for printable string sequences of length >= 6
strings = re.findall(rb'[\x20-\x7e\xa0-\xff]{6,}', data)
clean = []
for s in strings:
    try:
        dec = s.decode('latin1').strip()
        if len(dec) > 8 and not dec.startswith('000') and not dec.startswith('FFF') and not dec.startswith('D:\\'):
            clean.append(dec)
    except:
        pass

print(f"Found {len(clean)} text fragments in shlokas.cxt.")
print("Sample extracted verses and titles:")
for c in clean[:35]:
    print(f"  [{len(c)}] {c[:90]}")
