import numpy as np
import cv2
import os


imagepath = "/Users/skyla/Desktop/insect7.png"
d = {(41, 51, 235): [[0, 255, 246],0], (52, 140, 240): [[191, 255, 0],0], (244, 64, 0): [[255, 0, 234],0], (76, 249, 120): [[255, 0, 34],0]} #dictionary that stores the RGB colors that appear (key) with the color it should be replaced with (value)
vertboxnum = 23 #height of picture in grids
horboxnum = 13 #width of picture in grids

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
        if x > width*4/13 or y > height*7/23:
            # Get the pixel value at (x, y)
            pixel = tuple(image[y, x])

            for ke in d.keys():
                if (abs(ke[0]- pixel[0]) < 10) and (abs(ke[1]- pixel[1]) < 10) and (abs(ke[2]- pixel[2]) < 10):
                    image[y,x] = d[ke][0]
                    d[ke][1] = d[ke][1]+1
            # if pixel in d:
            #     image[y,x] = d[pixel]

cv2.imwrite("modifiedimagewtolerance.jpg", image)

for key in d:
    value = d[key][1]
    print("RGB value: ", key)
    print("pixel number: ", value)
    ratio = value/width/height
    print("ratio to all: ", ratio)
    heightinch = vertboxnum/5
    widthinch = horboxnum/5
    print("surface area: ", ratio*heightinch*widthinch)
    print("\n")


print("done writing!")