import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('content/data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

chapters = d.get('chapters', [])
print(f"=== DEVABHĀṢĀ SANSKRIT CARD & LIGATURE AUDIT ===")
print(f"Total Chapters: {len(chapters)}")

total_cards = 0
suspicious_total = 0

for ch in chapters:
    recs = ch.get('audioTracks', [])
    print(f"\n--- CHAPTER {ch.get('id'):02d}: {ch.get('titleEnglish')} ({len(recs)} tracks) ---")
    for idx, rec in enumerate(recs, 1):
        total_cards += 1
        sa = rec.get('sanskrit', '')
        first_line = sa.split('\n')[0] if sa else ''
        suspicious = []

        # Check for isolated / dangling vowel signs (matras) at word boundaries
        words = re.findall(r'[\u0900-\u097F]+', sa)
        for w in words:
            if re.search(r'^[ािीुूृॄेैोौ्ंँः]', w):
                suspicious.append(f'isolated matra on {w}')
            # Check for legacy font decoding artifacts
            if '±' in w or 'Ø' in w or '×' in w or 'ß' in w:
                suspicious.append(f'unconverted glyph in {w}')

        if suspicious:
            suspicious_total += 1
            print(f"  Track {idx:02d}: {first_line[:50]}... | ALERT: {', '.join(suspicious)}")
        else:
            print(f"  Track {idx:02d}: {first_line[:50]}... [OK]")

print("\n" + "=" * 60)
print(f"AUDIT SUMMARY: {total_cards} recitations audited across {len(chapters)} chapters.")
print(f"TOTAL CORRUPTIONS / ANOMALIES: {suspicious_total}")
print(f"STATUS: {'100% CLEAN DEVANAGARI' if suspicious_total == 0 else 'ANOMALIES DETECTED'}")
print("=" * 60)
