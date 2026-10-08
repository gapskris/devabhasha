import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

player_css = "Ashtavadhanam_modern/css/player.css"
main_css = "Ashtavadhanam_modern/css/main.css"

for path in [main_css, player_css]:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            css = f.read()
        print(f"\n--- Breakpoints in {path} ---")
        for m in re.finditer(r'(@media[^{]+\{)', css):
            print(m.group(1))
