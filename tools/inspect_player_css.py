import re

with open("Devabhasha_modern/css/player.css", "r", encoding="utf-8") as f:
    css = f.read()

# Find rules for .canvas-stage-wrapper, .dialogues-wrapper, .stage-diagram-container
for m in re.finditer(r'(\.(?:canvas-stage-wrapper|dialogues-wrapper|stage-diagram-container)[^{]*\{[^}]+\})', css):
    print(m.group(1))
    print("---")
