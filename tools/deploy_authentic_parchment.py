import os
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

base_dir = "Devabhasha_modern"
# 1. Base parchment: Take the warm golden parchment from Devabhasha_master/jpeg/chapter 5/chap5page02.jpg
src_img_path = "Devabhasha_master/jpeg/chapter 5/chap5page02.jpg"
if os.path.exists(src_img_path):
    src = Image.open(src_img_path).convert("RGB")
    # The right half (x: 450 to 800) is pure, smooth golden glowing parchment!
    # Let's sample a tile from (480, 50, 780, 550) and create a rich 800x600 smooth parchment
    crop = src.crop((480, 40, 780, 560))
    # Resize and mirror to fill 800x600
    parchment = Image.new("RGB", (800, 600))
    # Paste smooth gradient
    p_resized = crop.resize((800, 600), Image.Resampling.LANCZOS)
    
    # Overlay subtle texture from anib.jpg
    anib_path = "Devabhasha_master/jpeg/chap2/anib.jpg"
    if os.path.exists(anib_path):
        anib = Image.open(anib_path).convert("L").resize((800, 600))
        anib_arr = np.array(anib, dtype=float)
        # Normalize anib grain
        grain = (anib_arr - anib_arr.mean()) / 255.0 * 18.0
        p_arr = np.array(p_resized, dtype=float)
        p_arr = np.clip(p_arr + grain[:, :, np.newaxis], 0, 255).astype(np.uint8)
        parchment = Image.fromarray(p_arr)
    else:
        parchment = p_resized

    # Draw authentic subtle antique gold border / double fillet
    draw = ImageDraw.Draw(parchment)
    # Outer gold rule
    draw.rectangle([10, 10, 789, 589], outline=(184, 134, 11), width=2)
    # Inner subtle rule
    draw.rectangle([14, 14, 785, 585], outline=(218, 165, 32), width=1)

    out_path = os.path.join(base_dir, "assets", "images", "canvas_parchment.jpg")
    parchment.save(out_path, quality=96)
    print(f"Created authentic clean parchment canvas: {out_path} ({parchment.size})")

    # Now deploy this clean authentic parchment canvas for all SWF chapters (3, 4, 8, 9, 10):
    for ch_id in [3, 4, 8, 9, 10]:
        dir_name = f"chapter{ch_id}"
        if ch_id == 3: dir_name = "chap03"
        dest_dir = os.path.join(base_dir, "assets", "images", dir_name)
        os.makedirs(dest_dir, exist_ok=True)
        dest_file = os.path.join(dest_dir, f"chap{ch_id}canvas.jpg")
        parchment.save(dest_file, quality=96)
        print(f"Deployed clean authentic canvas to: {dest_file}")

print("All chapter canvases updated successfully!")
