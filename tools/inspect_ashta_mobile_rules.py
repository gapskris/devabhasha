import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

player_css = "Ashtavadhanam_modern/css/player.css"
if os.path.exists(player_css):
    with open(player_css, "r", encoding="utf-8") as f:
        css = f.read()
    pos = css.find("@media (max-width: 768px)")
    if pos != -1:
        print("CSS at max-width: 768px in Ashtavadhanam player.css:\n")
        print(css[pos:pos+2500])
