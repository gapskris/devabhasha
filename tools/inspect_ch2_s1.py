import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("Devabhasha_modern/content/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

ch2 = data["chapters"][1]
print("Chapter 2 canvas:", ch2.get("canvas"))
print("Chapter 2 slide 1:", json.dumps(ch2["slides"][0], ensure_ascii=False, indent=2))
