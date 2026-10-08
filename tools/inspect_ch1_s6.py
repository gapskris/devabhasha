import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("Devabhasha_modern/content/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

ch1_s6 = data["chapters"][0]["slides"][5]
print("Chapter 1 Slide 6:\n", json.dumps(ch1_s6, ensure_ascii=False, indent=2))
