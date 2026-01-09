import sys
import os
from PIL import Image

# grab the first and second arguments
src_dir = sys.argv[1]
dest_dir = sys.argv[2]

# check if second folder exits, if not create it
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# loop through images folder and then convert images to PNG
for filename in os.listdir(src_dir):
    src_path = os.path.join(src_dir, filename)

    try:
        # finally save them to new folder
        img = Image.open(src_path)
        name, ext = os.path.splitext(filename)
        dest_path = os.path.join(dest_dir, name + ".png")

        img.save(dest_path, "PNG")

    except Exception as e:
        print(f"Skipping {filename}: {e}")

