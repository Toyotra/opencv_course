import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

from zipfile import ZipFile
from urllib.request import urlretrieve


def download_and_unzip(url, save_path):
    print(f"Downloading and extracting assests....", end="")

    # Downloading zip file using urllib package.
    urlretrieve(url, save_path)

    try:
        # Extracting zip file using the zipfile package.
        with ZipFile(save_path) as z:
            # Extract ZIP file contents in the same directory.
            z.extractall(os.path.split(save_path)[0])

        print("Done")

    except Exception as e:
        print("\nInvalid file.", e)


URL = r"https://www.dropbox.com/s/0oe92zziik5mwhf/opencv_bootcamp_assets_NB4.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB4.zip")

# Download if asset ZIP does not exist.
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)

NZ_coast = cv2.imread("New_Zealand_Coast.jpg", cv2.IMREAD_COLOR)[:,:,::-1]
plt.imshow(NZ_coast)
plt.show()



#THIS IS FOR BRIGHTNESS
matrix = np.ones(NZ_coast.shape, dtype="uint8")*100
NZ_darker = cv2.subtract(NZ_coast, matrix)
NZ_brighter = cv2.add(NZ_coast, matrix)

plt.figure(figsize=(18,5))

plt.subplot(131); plt.imshow(NZ_darker); plt.title("Darker")
plt.subplot(132); plt.imshow(NZ_coast); plt.title("Original")
plt.subplot(133); plt.imshow(NZ_brighter); plt.title("Brighter")
plt.show()


#THIS IS FOR CONTRAST

matrix1 = np.ones(NZ_coast.shape) * .3
matrix2 = np.ones(NZ_coast.shape) * 3

lower_contrast_img = np.uint8(cv2.multiply(np.float64(NZ_coast), matrix1))
higher_contrast_img =np.uint8(np.clip(cv2.multiply(np.float64(NZ_coast), matrix2), 0, 255)) #clip is needed so that when values get over 255, they don't roll back to 0+n

plt.figure(figsize=(18,5))

plt.subplot(131); plt.imshow(lower_contrast_img); plt.title("Lower Contrast")
plt.subplot(132); plt.imshow(NZ_coast); plt.title("Original")
plt.subplot(133); plt.imshow(higher_contrast_img); plt.title("Higher Contrast")
plt.show()




#THIS IS FOR THRESHOLDING
img_read =  cv2.imread("building-windows.jpg", cv2.IMREAD_GRAYSCALE)
retval, img_thresh = cv2.threshold(img_read, 130, 255, cv2.THRESH_BINARY)

plt.figure(figsize=(18,5))

plt.subplot(121); plt.imshow(img_thresh, cmap = "gray"); plt.title("Threshold")
plt.subplot(122); plt.imshow(img_read, cmap = "gray"); plt.title("Unchanged Image")
plt.show()




img_read = cv2.imread("Piano_Sheet_Music.png", cv2.IMREAD_GRAYSCALE)

retval, img_thresh_1 = cv2.threshold(img_read, 50,255, cv2.THRESH_BINARY)
retval, img_thresh_2 = cv2.threshold(img_read, 130,255, cv2.THRESH_BINARY)

adaptive_thresh = cv2.adaptiveThreshold(img_read, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

plt.figure(figsize=(18,5))
plt.subplot(141); plt.imshow(img_read, cmap = "gray"); plt.title("Original")
plt.subplot(142); plt.imshow(img_thresh_1, cmap = "gray"); plt.title("Threshold 1")
plt.subplot(143); plt.imshow(img_thresh_2, cmap = "gray"); plt.title("Threshold 2")
plt.subplot(144); plt.imshow(adaptive_thresh, cmap = "gray"); plt.title("Adaptive Threshold")
plt.show()



img_rec = cv2.imread("rectangle.jpg", cv2.IMREAD_GRAYSCALE)
img_cir = cv2.imread("circle.jpg", cv2.IMREAD_GRAYSCALE)

plt.figure(figsize = (20,5))

plt.subplot(121);plt.imshow(img_rec, cmap = "gray")
plt.subplot(122);plt.imshow(img_cir, cmap = "gray")
plt.show()

#BITWISE AND OPERATORS
plt.figure(figsize = (5,7))
result1 = cv2.bitwise_and(img_rec, img_cir, mask=None)
plt.subplot(311);plt.imshow(result1, cmap = "gray");plt.title("AND")
result2 = cv2.bitwise_or(img_rec, img_cir, mask=None)
plt.subplot(312);plt.imshow(result2, cmap = "gray");plt.title("OR")
result3 = cv2.bitwise_xor(img_rec, img_cir, mask=None)
plt.subplot(313);plt.imshow(result3, cmap = "gray");plt.title("XOR")
plt.show()

cola = cv2.imread("coca-cola-logo.png")[:,:,::-1]
plt.imshow(cola)
w,h,c = cola.shape
plt.show()

img_background_RGB = cv2.imread("checkerboard_color.png")[:,:,::-1]

dim = (w, h)
img_background_RGB = cv2.resize(img_background_RGB, dim, interpolation = cv2.INTER_AREA)

plt.imshow(img_background_RGB)
plt.show()


#NOW WE MAP IT

cola_gray = cv2.cvtColor(cola, cv2.COLOR_BGR2GRAY)

retval, img_mask = cv2.threshold(cola_gray, 100, 255, cv2.THRESH_BINARY)
plt.imshow(img_mask, cmap = "gray"); plt.show()

#INVERSION OF MASK

img_mask_inv = cv2.bitwise_not(img_mask)
plt.imshow(img_mask_inv, cmap = "gray"); plt.show()

img_background = cv2.bitwise_and(img_background_RGB, img_background_RGB, mask=img_mask)
plt.imshow(img_background);plt.show()

img_foreground = cv2.bitwise_and(cola, cola, mask=img_mask_inv)
plt.imshow(img_foreground); plt.show()

full_img = cv2.bitwise_or(img_background, img_foreground)

plt.imshow(full_img); plt.show()


