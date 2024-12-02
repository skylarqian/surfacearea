#this program takes RGB color values and a picture and creates a 
# new modified image that replaces those color values with something else

import numpy as np
import cv2
import os

#modify these values!
d = {(41, 51, 236): [0, 255, 246], (40, 51, 236): [0, 255, 246], (52, 139, 240): [191, 255, 0], (245, 64, 0): [255, 0, 234], (76, 249, 120): [255, 0, 34]} #dictionary that stores the RGB colors that appear (key) with the color it should be replaced with (value)
imagepath = "/Users/skyla/Desktop/insect3annotated.png" #path of desired image
replacementpath = "modified_image.jpg" #replacement image path

# Read the image
image = cv2.imread(imagepath)

if not os.path.exists(imagepath):
    print("Image not found!")
else:
    print("image found!")

# Get the height and width of the image
height, width, channels = image.shape

#go through each pixel
for y in range(height):
    for x in range(width):
        # Get the pixel value at (x, y)
        pixel = tuple(image[y, x])

        if pixel in d:
            image[y,x] = d[pixel]

cv2.imwrite("modified_image.jpg", image)
print("done writing!")