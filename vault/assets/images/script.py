import os
from PIL import Image

for filename in os.listdir():
    if filename.endswith(".png") and not filename.endswith("-resized.png"):
        image = Image.open(filename)
        image = image.resize((128, 128))
        new_filename = f"{filename[:-4]}-resized.png"
        image.save(new_filename)
        print(
            f'<a href="/assets/images/{filename}"><img src="/assets/images/{new_filename}" alt="{filename}" width="256px" height="256px" /></a>\n'
        )
