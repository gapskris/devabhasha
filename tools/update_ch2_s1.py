import json

path = "Devabhasha_modern/content/data.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# In Chapter 2 Slide 1: remove redundant alpha.jpg diagram
ch2 = data["chapters"][1]
s1 = ch2["slides"][0]
if "diagram" in s1:
    del s1["diagram"]
if "diagramTitle" in s1:
    del s1["diagramTitle"]

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated Chapter 2 Slide 1 in content/data.json.")
