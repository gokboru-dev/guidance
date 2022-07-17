###################################################################
### Developer(s): umutzan2, ismailtrm                           ###
### Last Update: 4/07/2022 by ismailtrm                         ###
### Notes: edited for a new list desing.                        ###
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

class pidControl:
    def __init__(self, Ref, Sampling_Time, PID = [1, 0, 0]):
        self.set_ref(Ref)
        self.set_sampling_time(Sampling_Time)
        self.set_params(PID)
        self.clear()

    def get_ref(self):
        return self.ref
    def get_sampling_time(self):
        return self.dt
    def get_params(self):
        return self.params
    def get_sys_model(self):
        return self.sys_model
    def get_K(self, str_param):
        if str_param in self.params: 
            return self.params[str_param]
    def set_ref(self, r):
        self.ref = r
    def set_sampling_time(self, t):
        self.dt = t
    def set_params(self, arr):
        self.params = {
            'p': arr[0],
            'i': arr[1],
            'd': arr[2]
        }
    def set_sys_model(self, func):
        self.sys_model = func
    def set_K(self, str_param, value):
        if str_param in self.params:
            self.params[str_param] = value
    
    def clear(self):
        self.A = 0
        self.last_err = 0
      
    def PID(self, func, step, last_err = 0, A = 0, out = [0]):
        if step < 1: return out
        e = self.ref - out[-1]
        A += self.dt * (e + last_err) / 2
        u = self.params['p'] * e + self.params['i'] * A + self.params['d'] * (e - last_err) / self.dt
        c = func(u)
        return self.PID(func, step-1, e, A, out+[c])
    
    def one_shot(self, fb_value):
        e = self.ref - fb_value
        self.A += self.dt * (e + self.last_err) / 2
        P = self.params['p'] * e
        I = self.params['i'] * self.A
        D = self.params['d'] * (e - self.last_err) / self.dt
        u = P + I + D 
        self.last_err = e
        return self.sys_model(u)
