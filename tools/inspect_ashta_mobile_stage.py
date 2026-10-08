import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

for path in ["Ashtavadhanam_modern/css/main.css", "Ashtavadhanam_modern/css/player.css"]:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            css = f.read()
        for m in re.finditer(r'@media\s*\([^)]*max-width[^)]*\)\s*\{([^@]+)\}', css):
            block = m.group(0)
            if any(k in block for k in ['dialogue', 'stage', 'canvas', 'art-left', 'art-right']):
                print(f"\n--- Match in {path} ---")
                print(block[:1800])
