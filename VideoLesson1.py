import cv2
import sys
import matplotlib.pyplot as plt
import os

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

URL = r"https://www.dropbox.com/s/p8h7ckeo2dn1jtz/opencv_bootcamp_assets_NB6.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB6.zip")

# Download if asset ZIP does not exist.
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)


source = 'race_car.mp4'  # source = 0 for webcam
cap = cv2.VideoCapture(source)

if not cap.isOpened():
    print("Could not open video.")

ret, frame = cap.read()

plt.imshow(frame); plt.show()




#VideoWriter in OpenCV, cv2.VideoWriter(filename, fourcc (this is the codec), fpx, frameSize)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out_avi = cv2.VideoWriter('race_car_out.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, (frame_width, frame_height))

out_mp4 = cv2.VideoWriter('race_car_out.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 10, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:

        out_avi.write(frame)
        out_mp4.write(frame)
    else:
        break
cap.release()
out_avi.release()
out_mp4.release()