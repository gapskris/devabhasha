"""
Generate PWA icons for Devabhāṣā Web Application
Creates:
- assets/icons/icon-192.png
- assets/icons/icon-512.png
- assets/icons/maskable-512.png
- assets/icons/apple-touch-icon.png (180x180)
- favicon.ico
"""

import os
from PIL import Image, ImageDraw, ImageFont

ICONS_DIR = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern\assets\icons"
os.makedirs(ICONS_DIR, exist_ok=True)

def create_emblem_icon(size, is_maskable=False):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0) if not is_maskable else (18, 12, 8, 255))
    draw = ImageDraw.Draw(img)
    
    # Outer circle
    margin = int(size * 0.08) if is_maskable else int(size * 0.04)
    r = (size - 2 * margin) // 2
    cx, cy = size // 2, size // 2
    
    # Dark sandalwood background circle
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(18, 12, 8, 255), outline=(212, 175, 55, 255), width=max(2, size // 64))
    
    # Inner gold filigree ring
    r_inner = int(r * 0.82)
    draw.ellipse([cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner], outline=(255, 215, 0, 200), width=max(1, size // 90))
    
    # Central radiant sun rays / lotus petals
    num_rays = 12
    import math
    for i in range(num_rays):
        angle = i * (2 * math.pi / num_rays)
        x1 = cx + int(r * 0.55 * math.cos(angle))
        y1 = cy + int(r * 0.55 * math.sin(angle))
        x2 = cx + int(r * 0.78 * math.cos(angle))
        y2 = cy + int(r * 0.78 * math.sin(angle))
        draw.line([x1, y1, x2, y2], fill=(212, 175, 55, 220), width=max(2, size // 80))
        
    # Center OM or Sanskrit glyph circle
    r_core = int(r * 0.40)
    draw.ellipse([cx - r_core, cy - r_core, cx + r_core, cy + r_core], fill=(36, 24, 18, 255), outline=(212, 175, 55, 255), width=max(2, size // 80))
    
    # Simple Vedic geometric motif in center
    r_dot = int(r_core * 0.35)
    draw.ellipse([cx - r_dot, cy - r_dot, cx + r_dot, cy + r_dot], fill=(255, 215, 0, 255))
    
    return img

# Generate icons
icon192 = create_emblem_icon(192)
icon192.save(os.path.join(ICONS_DIR, "icon-192.png"))

icon512 = create_emblem_icon(512)
icon512.save(os.path.join(ICONS_DIR, "icon-512.png"))

maskable512 = create_emblem_icon(512, is_maskable=True)
maskable512.save(os.path.join(ICONS_DIR, "maskable-512.png"))

apple180 = create_emblem_icon(180)
apple180.save(os.path.join(ICONS_DIR, "apple-touch-icon.png"))

# Favicon
icon32 = create_emblem_icon(32)
icon32.save(os.path.join(r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern", "favicon.ico"))

print("PWA icons generated successfully.")
