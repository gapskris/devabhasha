import os, re

base = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_master"
with open(os.path.join(base, "indexmusic.cxt"), "rb") as f:
    data = f.read()

# Let's extract wav references
wav_matches = re.findall(rb'([a-zA-Z0-9_\-\s]+\.wav)', data, re.IGNORECASE)
print(f"Total .wav matches found in indexmusic.cxt: {len(wav_matches)}")
unique_wavs = sorted(list(set([m.decode('latin1').strip() for m in wav_matches])))
print(f"Unique wavs ({len(unique_wavs)}):")
for w in unique_wavs[:25]:
    print(f"  {w}")

# Also look for section or title strings
strings = re.findall(rb'[\x20-\x7e]{4,}', data)
clean_strings = [s.decode('latin1').strip() for s in strings if not s.endswith(b'.wav') and len(s.strip()) > 3]
print(f"\nOther strings sample ({len(clean_strings)}):")
for s in clean_strings[:30]:
    if not s.startswith("000") and not s.startswith("FFF") and not s.startswith("D:\\"):
        print(f"  {s}")
