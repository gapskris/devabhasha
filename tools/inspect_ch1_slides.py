import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("Devabhasha_modern/content/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

ch1 = data["chapters"][0]
for s in ch1["slides"]:
    print(f"Slide {s['slideNumber']}: canvas={s.get('canvas')}, trackIndex={s.get('trackIndex')}, trackIndices={s.get('trackIndices')}")
