import cv2
import numpy as np
import matplotlib.pyplot as plt
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
URL = r"https://www.dropbox.com/s/48hboi1m4crv1tl/opencv_bootcamp_assets_NB3.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB3.zip")

# Download if asset ZIP does not exist.
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)





image = cv2.imread("Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)


plt.imshow(image[:, :, ::-1])
plt.show()

imageLine = image.copy()                              #RED AND GREEN
cv2.line(imageLine, (200,300), (400,300), (0,255,255), thickness=5, lineType=cv2.LINE_AA)

plt.imshow(imageLine[:,:,::-1])
plt.show()

imageCircle = image.copy()
cv2.circle(imageCircle, (900,500), 100, (0,0,255), thickness=5, lineType=cv2.LINE_AA)

plt.imshow(imageCircle[:,:,::-1])
plt.show()


imageRect = image.copy()
cv2.rectangle(imageRect, (200,200), (400,300), (0,255,255), thickness=5, lineType=cv2.LINE_AA)
plt.imshow(imageRect[:,:,::-1])
plt.show()



imageText = image.copy()
cv2.putText(imageText, "Apollo n stuff", (200,700), cv2.FONT_HERSHEY_PLAIN, 2.3, (255,0,0), 2, cv2.LINE_AA)
plt.imshow(imageText[:,:,::-1])
plt.show()

