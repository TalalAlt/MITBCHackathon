# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random
import uuid

from PIL import Image, ImageDraw, ImageOps

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

def make_circular(im):

    im2 = Image.new('RGB', im.size)
    mask = Image.new("L", im.size)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0,0) + im.size, fill=255)
    out = Image.composite(im, im2, mask)


    return out

image = Image.new('RGB', (128, 128))
width, height = image.size

rectangle_width = random.randint(1,20)
rectangle_height = random.randint(1,20)

number_of_squares = random.randint(6000, 10000)

draw_image = ImageDraw.Draw(image)
for i in range(number_of_squares):
    rectangle_x = random.randint(0, width)
    rectangle_y = random.randint(0, height)

    rectangle_shape = [
        (rectangle_x, rectangle_y),
        (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
    draw_image.rectangle(
        rectangle_shape,
        fill=(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )
circular_Image = make_circular(image)
circular_Image.save(f'./output/{run_id}.png')

