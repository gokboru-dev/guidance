###################################################################
### Developer(s): umutzan2, ismailtrm                           ###
### Last Update: 4/07/2022 by ismailtrm                         ###
### Notes: upper red and lower red, configured with using cam.  ###
###                                                             ###
###################################################################

import cv2
import numpy as np

def guidance(theColor, video, xDegree, yDegree, xPixel, yPixel):

    xD = 500.5
    yD = 500.5

    colors = {
        "black": {"theUpper": [50, 50, 100],
                  "theLower": [0, 0, 0]},

        "white": {"theUpper": [0, 0, 255],
                  "theLower": [0, 0, 0]},

        "red": {"theUpper": [255, 255, 255],
                "theLower": [171, 160, 60]},

        "green": {"theUpper": [102, 255, 255],
                  "theLower": [25, 52, 72]},

        "blue": {"theUpper": [126, 255, 255],
                 "theLower": [94, 80, 2]},

        "yellow": {"theUpper": [44, 255, 255],
                   "theLower": [24, 100, 100]},
    }
    theUpper = np.array(colors[theColor]["theUpper"])
    theLower = np.array(colors[theColor]["theLower"])
    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img, theLower, theUpper)

    mask_contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv2.contourArea(mask_contour) > 500:
                x, y, w, h = cv2.boundingRect(mask_contour)
                cv2.rectangle(video, (x, y), (x + w, y + h),
                              (0, 255, 255), 1)

                center_x = int((w/2)+x)
                center_y = int((h/2)+y)
                cv2.circle(video, (center_x, center_y), 2, (255, 0, 255), -1)

                Cx = (xDegree/xPixel)
                Cy = (yDegree/yPixel)
                xD = (center_x-(xPixel/2))*Cx
                yD = (center_y-(yPixel/2))*Cy
    return xD, yD
