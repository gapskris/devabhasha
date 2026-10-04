import os
from PIL import Image

src_path = r"C:\Users\gkpan\.gemini\antigravity\brain\dd0693b4-ed17-4f99-aa84-c2130c23753e\devabhasha_living_manuscript_1791118552370.jpg"
root_dir = r"C:\DataScience\Vijay Ji's Music Conversion\Devabhasha_modern"
icons_dir = os.path.join(root_dir, "assets", "icons")
os.makedirs(icons_dir, exist_ok=True)

img = Image.open(src_path).convert("RGBA")

# 1. Master PNG
img.save(os.path.join(icons_dir, "master-icon.png"), "PNG", optimize=True)

# 2. 512x512 Standard PWA Icon
icon_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
icon_512.save(os.path.join(icons_dir, "icon-512.png"), "PNG", optimize=True)

# 3. 192x192 Standard PWA Icon
icon_192 = img.resize((192, 192), Image.Resampling.LANCZOS)
icon_192.save(os.path.join(icons_dir, "icon-192.png"), "PNG", optimize=True)

# 4. 180x180 Apple Touch Icon
apple_180 = img.resize((180, 180), Image.Resampling.LANCZOS)
apple_180.save(os.path.join(icons_dir, "apple-touch-icon.png"), "PNG", optimize=True)

# 5. 512x512 Maskable Icon (safe zone padded with dark background)
bg_color = (26, 17, 10, 255) # matching dark amber/sandalwood
maskable_img = Image.new("RGBA", (512, 512), bg_color)
# Scale content to 80% to fit within maskable safe area circle (diameter ~410px)
content_size = int(512 * 0.82)
scaled_content = img.resize((content_size, content_size), Image.Resampling.LANCZOS)
offset = (512 - content_size) // 2
maskable_img.paste(scaled_content, (offset, offset), scaled_content)
maskable_img.save(os.path.join(icons_dir, "maskable-512.png"), "PNG", optimize=True)

# 6. Favicon 32x32 PNG
fav_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
fav_32.save(os.path.join(icons_dir, "favicon.png"), "PNG", optimize=True)

# 7. Multi-resolution favicon.ico
ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
img.save(os.path.join(root_dir, "favicon.ico"), format="ICO", sizes=ico_sizes)

print("Successfully generated all Devabhasha icons with the opened book design!")
