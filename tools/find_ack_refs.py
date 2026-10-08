import os

for root, dirs, files in os.walk("Devabhasha_modern"):
    if any(p in root for p in [".git", "node_modules"]):
        continue
    for f in files:
        if f.endswith((".js", ".html", ".css", ".json")):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                text = file.read()
                if "back.jpg" in text or "acknowledge" in text:
                    for line_no, line in enumerate(text.splitlines(), 1):
                        if "back.jpg" in line or "acknowledge" in line:
                            # Only print if not in credits section
                            print(f"{path}:{line_no}: {line.strip()[:100]}")
