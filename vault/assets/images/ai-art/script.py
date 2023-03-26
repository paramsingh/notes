import os
from PIL import Image

for filename in os.listdir():
    new_filename = f"{filename[:-4]}-resized.png"
    if new_filename in os.listdir():
        continue
    if filename.endswith(".png") and not filename.endswith("-resized.png"):
        image = Image.open(filename)
        image = image.resize((128, 128))
        image.save(new_filename)
        print(
            f'<a href="/assets/images/ai-art/{filename}"><img src="/assets/images/ai-art/{new_filename}" alt="{filename}" width="128px" height="128px" /></a>\n'
        )
