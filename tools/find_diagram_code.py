import re

with open("Devabhasha_modern/js/app.js", "r", encoding="utf-8") as f:
    text = f.read()

for m in re.finditer(r'(folio-narrative|stage-diagram-container|diagram-frame)', text):
    line_no = text[:m.start()].count('\n') + 1
    print(f"Line {line_no}: {text[max(0, m.start()-40):min(len(text), m.end()+60)]}")
