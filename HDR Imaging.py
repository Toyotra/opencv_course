import cv2
import os
import matplotlib.pyplot as plt
import sys
import numpy as np

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

URL = r"https://www.dropbox.com/s/qa1hsyxt66pvj02/opencv_bootcamp_assets_NB10.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), "opencv_bootcamp_assets_NB10.zip")

# Download if asset ZIP does not exist.
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)



def readImagesAndTimes():

    filenames = ["img_0.033.jpg", "img_0.25.jpg", "img_2.5.jpg", "img_15.jpg"]

    timeList = np.array([1/30.0, 0.25, 2.5, 15.0], dtype=np.float32)

    imageList = []
    for filename in filenames:
        im = cv2.imread(filename)
        imageList.append(im)

    return imageList, timeList

images, times = readImagesAndTimes()

alignMTB = cv2.createAlignMTB()
alignMTB.process(images, images)


#WE NOW NEED TO CALCULATE THE CAMERA RESPONSE FUNCTION???

calibrateDebevec = cv2.createCalibrateDebevec()
responseDebevec = calibrateDebevec.process(images, times)

x = np.arange(256, dtype=np.uint8)
y = np.squeeze(responseDebevec)

ax = plt.figure(figsize=(30,10))
plt.title("Debevec Inverse Camera Response Function?", fontsize=24)
plt.xlabel("Measured Pixel Value", fontsize=22)
plt.ylabel("Calibrated Intensity", fontsize=22)
plt.xlim(0, 260)
plt.grid()
plt.plot(x, y[:, 0], "b", x, y[:, 1], "g", x, y[:, 2], "r")
plt.show()


#WE SHALL NOW MERGE THIS SHIT

mergeDebevic = cv2.createMergeDebevec()
hdrDebevic =  mergeDebevic.process(images, times, responseDebevec)

#we shall now map the hdr images to bit per channel images

tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
ldrDrago = tonemapDrago.process(hdrDebevic) * 3

plt.figure(figsize=(20,10)); plt.imshow(np.clip(ldrDrago, 0, 1)); plt.axis('off')
cv2.imwrite("ldr-Drago.jpg", ldrDrago *255)
print("saved ldr-Drago.jpg")
plt.show()





















