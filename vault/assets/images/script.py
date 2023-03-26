import os

for filename in os.listdir():
    if filename.endswith(".png"):
        print(
            f'<img src="/assets/images/{filename}" alt="{filename}" width="256px" height="256px">\n'
        )
