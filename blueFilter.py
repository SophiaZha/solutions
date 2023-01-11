from tkinter import Image

IMAGE_URL = "https://codehs.com/uploads/c709d869e62686611c1ac849367b3245"
IMAGE_WIDTH = 280
IMAGE_HEIGHT = 200

RED = 0
GREEN = 1
BLUE = 2
def remove_green_and_blue(pixel):
    new_green = 0
    new_blue = 0
    return (pixel[RED], new_green, new_blue)

image = Image(IMAGE_URL)
image.set_position(70, 70)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)









"""
In this exercise, you’ll get some more practice writing image filters!

YOUR JOB:
Write a function called remove_blue that takes an image as a parameter and sets the blue value of every pixel in the image to be 0.
his will remove all blue from the image, giving it a night vision tone.

EXAMPLE:

BEFORE:


AFTER:


BONUS CHALLENGE:
Try writing extra filters like remove_red that sets all red values to 0,
and remove_green which sets all green values to 0.

What happens if you only cut the blue values in half instead of setting them
to 0? What happens if you remove both red and blue, or both red and green? See what kinds of cool filters you can come up with!

See if you can produce this image:


Or this image:



"""