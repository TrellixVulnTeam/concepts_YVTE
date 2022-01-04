"""
Reference:
https://www.geeksforgeeks.org/create-transparent-png-image-with-python-pillow/
"""
import os
from PIL import Image


def make_transparent(filename, color=(0, 0, 0)):
    img = Image.open(filename)
    rgba = img.convert("RGBA")
    data = rgba.getdata()

    item_0, item_1, item_2 = color

    new_data = []
    for item in data:
        if item[0] == item_0 and item[1] == item_1 and item[2] == item_2:
            new_data.append((255, 255, 255, 0))

        else:
            new_data.append(item)
    rgba.putdata(new_data)

    out_fn = os.path.basename(filename)
    rgba.save(f"../../outputs/trans_{item_0}_{item_1}_{item_2}_{out_fn}", "PNG")


def main():
    filename = "../../data/gfg.png"
    black = (0, 0, 0)
    make_transparent(filename, color=black)

    yellow = (255, 255, 0)
    make_transparent(filename, color=yellow)


if __name__ == '__main__':
    main()
