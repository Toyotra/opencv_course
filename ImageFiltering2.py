import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

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

URL = r"https://www.dropbox.com/s/zuwnn6rqe0f4zgh/opencv_bootcamp_assets_NB8.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB8.zip")

# Download if asset ZIP does not exist.
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)



# Read reference image
refFilename = "form.jpg"
print("Reading reference image:", refFilename)
im1 = cv2.imread(refFilename, cv2.IMREAD_COLOR)
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)

# Read image to be aligned
imFilename = "scanned-form.jpg"
print("Reading image to align:", imFilename)
im2 = cv2.imread(imFilename, cv2.IMREAD_COLOR)
im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(20,20))
plt.subplot(121); plt.axis('off'); plt.imshow(im1); plt.title('Original')
plt.subplot(122); plt.axis('off'); plt.imshow(im2); plt.title('Scanned')
plt.show()


im1_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
im2_gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)


#THIS GETS THE KEY POINTS IN THE 2 IMAGES USING THE ORB CREATE METHOD IN OPENCV
MAX_NUM_FEATURES = 500
orb = cv2.ORB_create(MAX_NUM_FEATURES)
keypoints1, descriptors1 = orb.detectAndCompute(im1_gray, None)
keypoints2, descriptors2 = orb.detectAndCompute(im2_gray, None)

im1_display = cv2.drawKeypoints(im1_gray, keypoints1, outImage=np.array([]), color=(255,0,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
im2_display = cv2.drawKeypoints(im2_gray, keypoints2, outImage=np.array([]), color=(255,0,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.figure(figsize=(20,10))
plt.subplot(121); plt.axis('off'); plt.imshow(im1_display); plt.title('Original')
plt.subplot(122); plt.axis('off'); plt.imshow(im2_display); plt.title('Scanned')
plt.show()


#WE WILL NOW MATCH THE KEYPOINTS
matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)

matches = list(matcher.match(descriptors1, descriptors2, None))

matches.sort(key=lambda x: x.distance, reverse=False) #wtf is reverse?

numGoodMatches = int(len(matches)*0.1)
matches = matches[:numGoodMatches]

#drawing good matches

im_matches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None, flags=2)
plt.figure(figsize=(20,10))
plt.imshow(im_matches);plt.axis("off");plt.title("Original Form")
plt.show()



#WE SHALL NOW FIND HOMOGRAPHY
points1 =  np.zeros((len(matches),2), dtype=np.float32)
points2 =  np.zeros((len(matches),2), dtype=np.float32)

for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt
h, mask = cv2.findHomography(points2, points1, cv2.RANSAC)

height, width, channels = im1.shape
im2_reg = cv2.warpPerspective(im2, h, (width, height))

plt.figure(figsize=(20,10))
plt.subplot(121);plt.imshow(im1); plt.axis('off'); plt.title('Original')
plt.subplot(122); plt.imshow(im2_reg); plt.axis('off'); plt.title('Scanned')
plt.show()

