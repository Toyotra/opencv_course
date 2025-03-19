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


img_NZ_rgb = cv2.imread("New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)[:,:,::-1]
plt.imshow(img_NZ_rgb)
plt.show()