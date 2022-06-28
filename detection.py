from distutils.log import error
from turtle import color
import cv2
import numpy as np

cap = cv2.VideoCapture("1") #cap = cv2.VideoCapture("1")

class coreColor:                         
   def __init__(self, up0, up1, up2, low0, low1, low2): 
     self.up0 = up0                           
     self.up1 = up1
     self.up2 = up2
     self.low0 = low0
     self.low1 = low1
     self.low2 = low2
     

def selectedColor(anyColor):
    return anyColor

if selectedColor=="black":
    color = coreColor(50, 50, 100 ,0 ,0 ,0)
elif selectedColor=="white":
    color = coreColor(0, 0, 255 ,0 ,0 ,0)
elif selectedColor=="red":
    color = coreColor(255, 255, 255, 171, 160, 60)
elif selectedColor=="green":
    color = coreColor(102, 255, 255, 25, 52, 72)
elif selectedColor=="blue":
    color = coreColor(126, 255, 255, 94, 80, 2)
elif selectedColor=="yellow":
    color = coreColor(44, 255, 255, 24, 100, 100)
else:
    error
    
upperColor=np.array[color.up0, color.up1, color.low2]
lowerColor=np.array[color.low0, color.low1, color.low2]

while True:
    success, video = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    x_axis = int(cap.get(3)/2)
    y_axis = int(cap.get(4)/2)
    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
    a = cv2.line(video, (x_axis, 0), (x_axis, height), (255, 0, 0), 1)
    a = cv2.line(video, (0, y_axis), (width, y_axis), (255, 0, 0), 1)
    a = cv2.circle(video, (x_axis, y_axis), 20, (0, 0, 255))
    font = cv2.FONT_ITALIC

    mask = cv2.inRange(img, lowerColor, upperColor)

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

                if center_x > (x_axis-20) and center_x < (x_axis+20) and center_y > (y_axis-20) and center_y < (y_axis+20):
                    a = cv2.putText(video, 'Kitlendi', (100, height-100),
                                    font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("window", video)

    if cv2.waitKey(1) == ord('q'):
        break
cap.realese()
cv2.destroyAllWindows()

def appX(aDegree:float,  aPixel:float):
    return aDegree/aPixel
    

def appY(aDegree:float,  aPixel:float):
    return aDegree/aPixel

angleX = appX*center_x
angleY = appY*center_y
