import os
from PIL import Image

jpeg_dir = "Devabhasha_master/jpeg"
for root, dirs, files in os.walk(jpeg_dir):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.bmp', '.png')):
            p = os.path.join(root, f)
            try:
                im = Image.open(p)
                print(f"{p}: {im.size}, {im.mode}")
            except Exception as e:
                print(f"{p}: error {e}")
