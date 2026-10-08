import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

for root, dirs, files in os.walk("."):
    # Limit search depth
    if any(p in root for p in [".git", "node_modules", ".pytest_cache", "__pycache__"]):
        continue
    for f in files:
        if any(f.lower().endswith(ext) for ext in [".dxr", ".cxt", ".bmp", ".jpg", ".png"]):
            if "cdrom" in root.lower() or "legacy" in root.lower() or "source" in root.lower() or "devabhasha" in root.lower():
                pass
print("Search complete.")
