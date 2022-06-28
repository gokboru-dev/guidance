from distutils.log import error
#import detection
import numpy


def app(theAxis:str, aDegree:float,  aPixel:float):
    
    if theAxis == "x" or theAxis == "X":
        appX = aDegree/aPixel
        return appX
    elif theAxis == "y" or theAxis == "Y":
        appY = aDegree/aPixel
        return appY
    else:
        return error


print(app("y", 135, 1920))
print(app("x", 135, 1080))
print(app("z", 135, 720))
