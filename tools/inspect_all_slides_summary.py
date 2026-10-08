import json, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('content/data.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for c in d['chapters']:
    cid = c['id']
    ctitle = c.get('titleEnglish')
    slides = c.get('slides', [])
    print(f"\n=== CHAPTER {cid}: {ctitle} ({len(slides)} slides) ===")
    for s in slides:
        snum = s.get('slideNumber')
        stitle = s.get('title')
        stitle_sa = s.get('titleSanskrit')
        tids = s.get('trackIndices', [])
        p_len = len(s.get('proseText') or '')
        p_sa = s.get('proseTextSanskrit') or ''
        has_robot = 'अध्यायस्य' in p_sa and 'विशिष्टा विषय-चर्चा' in p_sa
        print(f"  Slide {snum:2d}: tracks={tids} | robot={has_robot} | p_sa='{p_sa[:40]}' | '{stitle}' / '{stitle_sa}'")
