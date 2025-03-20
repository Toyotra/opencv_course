import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


cb_img =  cv2.imread("checkerboard_18x18.png")
plot = plt.imshow(cb_img, cmap="gray")

#print(plot)
print(cb_img[0,0]) #1st row, 1st column
print(cb_img[0,6]) #7th column, 1st row
print(cb_img[6,0]) #7th row, 1st column
plt.show()
cb_copy = cb_img.copy()

cb_copy[2,2] = 200
cb_copy[3,2] = 200
cb_copy[2,3] = 200
cb_copy[3,3] = 200
plt.imshow(cb_copy, cmap="gray")
plt.show()


img_NZ_rgb = cv2.imread("New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)[:, :, ::-1]
plt.imshow(img_NZ_rgb)
plt.show()


#FOR CROPPING, WE CAN SPECIFY THE SPECIFIC ROWS AND COLUMNS

NZ_CROPPED = img_NZ_rgb[200:400, 300:600]
plt.imshow(NZ_CROPPED)
plt.show()

#image resizing
CROPPED_2X = cv2.resize(NZ_CROPPED,None,fx=2,fy=2)
plt.imshow(CROPPED_2X)
plt.show()
print(img_NZ_rgb.shape)
y,x,n = img_NZ_rgb.shape #IT IS FLIPPED

new_resized_img = cv2.resize(NZ_CROPPED, dsize=(x,y), interpolation = cv2.INTER_AREA)
plt.imshow(new_resized_img)
plt.show()

#flipping images
img_NZ_rgb_flipped_horz = cv2.flip(img_NZ_rgb, 1) #horizontal
img_NZ_rgb_flipped_vert = cv2.flip(img_NZ_rgb, 0) #vertical
img_NZ_rgb_flipped_both = cv2.flip(img_NZ_rgb, -1) #both
