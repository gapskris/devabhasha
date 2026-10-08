import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("Devabhasha_modern/content/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for ch in data["chapters"]:
    print(f"\nChapter {ch['id']} ({ch['titleEnglish']}):")
    for s in ch.get("slides", []):
        diag = s.get("diagram")
        vis = s.get("visual")
        if diag or vis:
            print(f"   Slide {s['slideNumber']}: diagram={diag or vis}, title={s.get('diagramTitle')}")
