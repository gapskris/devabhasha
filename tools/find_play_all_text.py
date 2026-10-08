import re

for js_file in ["Devabhasha_modern/js/app.js", "Devabhasha_modern/js/player.js"]:
    with open(js_file, "r", encoding="utf-8") as f:
        text = f.read()
    for m in re.finditer(r'play-all-text', text):
        line_no = text[:m.start()].count('\n') + 1
        print(f"{js_file}:{line_no}: {text[max(0, m.start()-40):min(len(text), m.end()+60)]}")
