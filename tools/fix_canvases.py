import os
import shutil
from PIL import Image
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASHTA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "Ashtavadhanam_modern"))

# 1. Create clean parchment canvas from back.jpg
back_path = os.path.join(BASE_DIR, "assets", "images", "acknowledge", "back.jpg")
if os.path.exists(back_path):
    im = Image.open(back_path).convert('RGB')
    arr = np.array(im)
    
    # In back.jpg, the text "ACKNOWLEDGEMENTS" is at y: 26 to 82, x: 230 to 570
    # The parchment texture is smooth and gradient-like in that upper region.
    # We can patch this banner region using texture from y: 88 to 144 (or blending rows above/below)
    # Let's inspect rows around y=10..24 and y=85..100
    top_patch = arr[10:25, 200:600]
    # Sample parchment texture from a clean region
    # Rows 180 to 240 have clean parchment
    patch_source = arr[180:240, 180:620]
    
    # Let's do a smooth gradient blend across the banner region:
    # y from 26 to 84:
    h, w, c = arr.shape
    clean_arr = arr.copy()
    
    # We interpolate between row 22 and row 86 for each column x between 180 and 620
    row_top = clean_arr[22, 180:620, :].astype(float)
    row_bot = clean_arr[86, 180:620, :].astype(float)
    
    num_rows = 86 - 22
    for r_idx, y in enumerate(range(23, 86)):
        alpha = r_idx / float(num_rows)
        # linear blend plus slight subtle noise from the clean region to preserve parchment grain
        grain = (patch_source[r_idx % len(patch_source), :, :].astype(float) - patch_source.mean()) * 0.25
        clean_arr[y, 180:620, :] = np.clip((1 - alpha) * row_top + alpha * row_bot + grain, 0, 255).astype(np.uint8)
        
    clean_parchment = Image.fromarray(clean_arr)
    parchment_out = os.path.join(BASE_DIR, "assets", "images", "canvas_parchment.jpg")
    clean_parchment.save(parchment_out, quality=95)
    print(f"Created clean parchment canvas: {parchment_out}")

# 2. Deploy chapter-specific master canvases from Ashtavadhanam illuminated 800x600 canvases
# Ashtavadhanam and Devabhasha share the same 1997 CD-ROM master series from Sri Aurobindo Society
canvas_mapping = {
    3: "eightfold 03.jpg",
    4: "eightfold 04.jpg",
    8: "eightfold 08.jpg",
    9: "eightfold 09.jpg",
    10: "eightfold 10.jpg"
}

for ch_id, eightfold_file in canvas_mapping.items():
    src_canvas = os.path.join(ASHTA_DIR, "assets", "images", eightfold_file)
    target_dir = os.path.join(BASE_DIR, "assets", "images", f"chapter{ch_id}")
    if ch_id == 3:
        target_dir = os.path.join(BASE_DIR, "assets", "images", "chap03")
    os.makedirs(target_dir, exist_ok=True)
    target_canvas = os.path.join(target_dir, f"chap{ch_id}canvas.jpg")
    
    if os.path.exists(src_canvas):
        shutil.copy2(src_canvas, target_canvas)
        print(f"Deployed authentic 800x600 master canvas for Chapter {ch_id}: {target_canvas}")
    else:
        # Fallback to the clean parchment
        shutil.copy2(parchment_out, target_canvas)
        print(f"Deployed clean parchment for Chapter {ch_id}: {target_canvas}")

print("Canvas deployment completed successfully!")
