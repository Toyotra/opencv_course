import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

from zipfile import ZipFile
from urllib.request import urlretrieve

from sqlalchemy.sql.operators import truediv

PREVIEW = 0
BLUR = 1
FEATURES = 2
CANNY = 3

feature_params = dict(maxCorners=500, qualityLevel=0.2, minDistance=15, blockSize=9)

s=0

if len(sys.argv)>1:
    s=sys.argv[1]

image_filter = PREVIEW
alive = True

win_name = "Camera Filters"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
result = None

source = cv2.VideoCapture(s)

while alive:
    has_frame, frame = source.read()
    if not has_frame:
        break

    if image_filter == PREVIEW:
        result = frame
    elif image_filter == CANNY:
        result = cv2.Canny(frame, 130,140)
    elif image_filter == BLUR:
        result = cv2.blur(frame,(5,5),0)
    elif image_filter == FEATURES:
        result = frame
        frame_gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners = cv2.goodFeaturesToTrack(frame_gray, **feature_params)

        if corners is not None:
            for x, y in np.float32(corners).reshape(-1,2):
                cv2.circle(result, (int(x),int(y)), 10, (0,255,0), 2)

    cv2.imshow(win_name, result)

    key = cv2.waitKey(1)

    if key==ord('q') or key == ord('Q') or key==27:
        alive=False
    elif key==ord('C') or key==ord('c'):
        image_filter= CANNY
    elif key==ord('B') or key==ord('b'):
        image_filter= BLUR
    elif key==ord('F') or key==ord('f'):
        image_filter= FEATURES
    elif key==ord('P') or key==ord('p'):
        image_filter= PREVIEW

source.release()
cv2.destroyAllWindows()