import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

def download_and_unzip(url, save_path):
    print(f"Downloading and extracting assets....", end="")

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

URL = r"https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), "opencv_bootcamp_assets_NB1.zip")

# Download if asset ZIP does not exist.
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)

cb_img = cv2.imread("checkerboard_18x18.png", 0)

print(f"The shape is {cb_img.shape}")

print(f"The datatype is {cb_img.dtype}")

print(cb_img)

plt.imshow(cb_img, cmap = "gray")
plt.show()
c_fuzzy = cv2.imread("checkerboard_fuzzy_18x18.jpg", 0)

print(c_fuzzy)

plt.imshow(c_fuzzy, cmap = "gray")
plt.show()


coca_cola_img = cv2.imread("coca-cola-logo.png", 1)

coca_cola_reversed = coca_cola_img[:,:,::-1]
plt.imshow(coca_cola_reversed)
plt.show()





img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
b,g,r = cv2.split(img_NZ_bgr)


plt.figure(figsize=(20,5))
plt.subplot(141);plt.imshow(r,cmap = "gray");plt.title("Red Channel")
plt.subplot(142);plt.imshow(g,cmap = "gray");plt.title("Green Channel")
plt.subplot(143);plt.imshow(b,cmap = "gray");plt.title("Blue Channel")

imgMerged = cv2.merge([r,g,b])

plt.subplot(144);plt.imshow(imgMerged,cmap = "gray");plt.title("Merged Output")
plt.show()


#WE CAN DO THIS A VERY EZ WAY USING cv2.cvtColor

NZ_colorize = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB);plt.title("cvtColor")
plt.imshow(NZ_colorize)
plt.show()

#WE WILL NOW DO IT VIA HSV
NZ_HSV = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(img_NZ_bgr)

plt.subplot(141);plt.imshow(h,cmap = "gray");plt.title("Hue")
plt.subplot(142);plt.imshow(s,cmap = "gray");plt.title("Saturation")
plt.subplot(143);plt.imshow(v,cmap = "gray");plt.title("Value")

plt.subplot(144);plt.imshow(NZ_colorize);plt.title("HSV Original")
plt.show()


cv2.imwrite("NZLake Hue.png", h)





cv2.namedWindow("w1")
cv2.imshow("w1", s)
cv2.waitKey(8000)
cv2.destroyWindow("w1")


cv2.namedWindow("w4")

Alive=True
while Alive:
    cv2.imshow("w4", img_NZ_bgr)
    keypress = cv2.waitKey(1)
    if keypress == ord('q'):
        Alive=False
cv2.destroyWindow("w4")

cv2.destroyAllWindows()
