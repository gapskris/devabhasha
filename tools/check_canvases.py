import json
import os

with open("Devabhasha_modern/content/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Total chapters:", len(data["chapters"]))
for ch in data["chapters"]:
    print(f"Chapter {ch['id']}: main canvas = {ch.get('canvas')}")
    ack_slides = [s['slideNumber'] for s in ch.get('slides', []) if 'acknowledge' in s.get('canvas', '').lower() or 'back.jpg' in s.get('canvas', '').lower()]
    if ack_slides:
        print(f"   WARNING: Chapter {ch['id']} has acknowledge canvas on slides: {ack_slides}")
