import json

path = "Devabhasha_modern/content/data.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

for ch in data["chapters"]:
    ch_id = ch["id"]
    if ch_id in [3, 4, 8, 9, 10]:
        dir_name = f"chapter{ch_id}"
        if ch_id == 3: dir_name = "chap03"
        correct_canvas = f"assets/images/{dir_name}/chap{ch_id}canvas.jpg"
        ch["canvas"] = correct_canvas
        for s in ch.get("slides", []):
            s["canvas"] = correct_canvas

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated content/data.json canvas mappings.")
