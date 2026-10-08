import os
import re
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

ashta_path = "Ashtavadhanam_modern/index.html"
if os.path.exists(ashta_path):
    with open(ashta_path, "r", encoding="utf-8") as f:
        content = f.read()
    print("Found Ashtavadhanam index.html, size:", len(content))
    # Find main layout elements
    for m in re.finditer(r'<main[^>]*>.*?</main>', content, re.DOTALL):
        print("MAIN TAG (first 2000 chars):\n", m.group(0)[:2000])

ashta_css = "Ashtavadhanam_modern/css/main.css"
if os.path.exists(ashta_css):
    with open(ashta_css, "r", encoding="utf-8") as f:
        css = f.read()
    print("\nCSS matches for stage, canvas, card:")
    for rule in re.finditer(r'(\.[a-zA-Z0-9_-]*(?:stage|canvas|card|dialogue|art|container)[a-zA-Z0-9_-]*\s*\{[^}]+\})', css):
        print(rule.group(1)[:300])
        print("---")
