"""
In this exercise we’ll get some practice modifying pixels with the Image class.

YOUR JOB:
Write a darken_filter and change_picture function that modifies the pixels in the left half of the image to be darker.

You can darken a pixel by subtracting the same value from each of the red, green, and blue values of the pixel.

for every pixel in the left half of the image
    set pixel red to be (red - DARKENING_FACTOR)
    set pixel green to be (green - DARKENING_FACTOR)
    set pixel blue to be (blue - DARKENING_FACTOR)
Of course, we cannot have negative values for red, green, or blue, so make sure to limit the pixel values to not go below 0.

EXAMPLE:

BEFORE:


AFTER:


HINT:
This exercise is very similar to the previous example Brighten Filter. The main difference is,
instead of adding the same value to each pixel, we are subtracting the same value from each pixel. We are also only applying this on half the picture.

Looking at the Brighten Filter example and really understanding that code is a good starting place for writing the Darken Filter.


"""