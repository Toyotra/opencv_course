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