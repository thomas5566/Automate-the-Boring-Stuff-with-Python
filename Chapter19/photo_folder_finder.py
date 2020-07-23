#!python3

import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('D:\\'):
    photos = 0
    not_photos = 0

    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not(filename.lower().endswith('jpg') or filename.lower().endswith('.png')):
            not_photos += 1
            continue

        try:
            # Open image file using Pillow.
            im = Image.open(os.path.join(foldername, filename))
        except OSError:
            continue

        width, height = im.size

        # Check if width & height are larger than 500.
        if width > 500 and height > 500:
            # Image is large enough to be considered a photo.
            photos += 1
        else:
            # Image is too small to be a photo.
            not_photos += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if photos > not_photos:
        print(os.path.abspath(foldername))
