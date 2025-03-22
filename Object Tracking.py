# Import modules

# import urllib

import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from matplotlib.animation import FuncAnimation
from base64 import b64encode

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

URL = r"https://www.dropbox.com/s/ld535c8e0vueq6x/opencv_bootcamp_assets_NB11.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB11.zip")

# Download if asset ZIP does not exist
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)


video_input_file_name = "race_car.mp4"

def drawRectangle(currentFrame, bbox):
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0]+ bbox[2]), int(bbox[1] + bbox[3]))
    cv2.rectangle(currentFrame, p1, p2, (255, 0, 0), 2)


def displayRectangle(currentFrame, bbox):
    plt.figure(figsize=(20,10))
    frameCopy = currentFrame.copy()[:,:,::-1]
    drawRectangle(frameCopy, bbox)
    plt.imshow(frameCopy)
    plt.axis('off')

def drawText(currentFrame, txt, location, color=(50,170,50)):
    cv2.putText(currentFrame, txt, location, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)



