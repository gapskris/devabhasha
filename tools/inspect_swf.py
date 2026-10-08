import os
import sys

for root, dirs, files in os.walk("Devabhasha_master/swf"):
    print(root, len(files), files[:10])
