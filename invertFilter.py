from tkinter import Image

import timer

IMAGE_URL = "https://codehs.com/uploads/c709d869e62686611c1ac849367b3245"
IMAGE_WIDTH = 280
IMAGE_HEIGHT = 200

RED = 0
GREEN = 1
BLUE = 2

image = Image(IMAGE_URL)
image.set_position(70, 70)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)

def invert_pixel(pixel):
    r = 255 - pixel[0]
    g = 255 - pixel[1]
    b = 255 - pixel[2]
    return(r, g, b)

def change_picture():
    for x in range(image.ge_width()):
        for y in range(image.get_height()):
            pixel = image.get_pixel(x, y)
            new_color - invert_pixes(pixel)
            image.set_red(x, y, new_colors[0])
            image.set_green(x, y, new_colors[1])
            image.set_blue(x, y, new_colors[2])


print("Invering Image..")
timer.set_timeout(change_picture, 1000)


"""
# Get pixel data: return a list of [r, g, b] colors
# with values between 0 and 255
pixel = img.get_pixel(x,y)

# Set new pixel values
img.set_red(x, y, new_value)
img.set_green(x, y, new_value)
img.set_blue(x, y, new_value)
"""