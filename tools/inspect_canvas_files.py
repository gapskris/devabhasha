import os
from PIL import Image

canvases = [
    "assets/images/chap03/chap3canvas.jpg",
    "assets/images/chapter4/chap4canvas.jpg",
    "assets/images/chapter8/chap8canvas.jpg",
    "assets/images/chapter9/chap9canvas.jpg",
    "assets/images/chapter10/chap10canvas.jpg",
    "assets/images/canvas_parchment.jpg"
]

base_dir = "Devabhasha_modern"
for c in canvases:
    p = os.path.join(base_dir, c)
    if os.path.exists(p):
        im = Image.open(p)
        print(f"{c}: {im.size}, mode={im.mode}")
    else:
        print(f"MISSING: {c}")
