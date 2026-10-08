import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

player_css = "Ashtavadhanam_modern/css/player.css"
if os.path.exists(player_css):
    with open(player_css, "r", encoding="utf-8") as f:
        css = f.read()
    print("Found Ashtavadhanam player.css, size:", len(css))
    for rule in re.finditer(r'(\.[a-zA-Z0-9_-]*(?:stage|canvas|dialogue|card|art)[a-zA-Z0-9_-]*\s*\{[^}]+\})', css):
        print(rule.group(1))
        print("---")
