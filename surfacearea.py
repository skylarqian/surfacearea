#this is program takes a picture and returns colors that appear often and computes the area of that color
import numpy as np
import cv2
import os

#modify these values!
vertboxnum = 23 #height of picture in grids
horboxnum = 13 #width of picture in grids
imagepath = "/Users/skyla/Desktop/insect7.png" #path of desired image
threshold = 5000 #change higher if >4 colors, change lower if <4 colors

# Read the image
image = cv2.imread(imagepath)

if not os.path.exists(imagepath):
    print("Image not found!")
else:
    print("image found!")

# Get the height and width of the image
height, width, channels = image.shape

print("height: ", height)
print("width: ", width)
print("channels: ", channels)



#create a dictionary
d = {}
# Iterate through each pixel
for y in range(height):
    for x in range(width):
        if x > width*4/13 or y > height*7/23:
            # Get the pixel value at (x, y)
            pixel = tuple(image[y, x])

            if pixel in d:
                d[pixel] = d[pixel] + 1
            else:
                d[pixel] = 1
            # # Do something with the pixel value
            # if np.all(pixel == orange):
            #     orangepixels += 1 
            #     image[y, x] = replacement

for key in d:
    value = d[key]
    if (value > threshold):
        print("RGB value: ", key)
        print("pixel number: ", value)
        ratio = value/width/height
        print("ratio to all: ", ratio)
        heightinch = vertboxnum/5
        widthinch = horboxnum/5
        print("surface area: ", ratio*heightinch*widthinch)
        print("\n")
print("done writing!")



# print("number of orange pixels: ", orangepixels)
# ratio = orangepixels/width/height
# print("ratio of orange to all pixels: ", ratio)
# heightinch = 19*1/5
# widthinch = 11/5
# print("body surface area in inches: ", ratio*heightinch*widthinch)
# cv2.imwrite("modified_image.jpg", image)
# print("done writing!")