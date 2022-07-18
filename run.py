###################################################################
### Developer(s): umutzan2, ismailtrm                           ###
### Last Update: 4/07/2022 by umutzan2                          ###
### Notes: running code was writen.                             ###
###                                                             ###
###################################################################

from turtle import delay
from pymavlink import mavutil
import cv2
from theScript import guidance

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)

master = mavutil.mavlink_connection( # aracin baglantisi
            '/dev/serial0',
            baud=57600)

#master = "mavutil.mavlink_connection('udpin:192.168.2.2:14550')" #eğer bilgisayardan konttrol edilecekse
def set_rc_channel_pwm(id, pwm=1500):

    if id < 1:
        print("Channel does not exist.")
        return


    if id < 9: # ardusubla iletisim
        rc_channel_values = [65535 for _ in range(8)]
        rc_channel_values[id - 1] = pwm
        master.mav.rc_channels_override_send(
            master.target_system,
            master.target_component,
            *rc_channel_values)

def colorTricking():
    while True:
        success, video = cap.read() #calling for a cam.
        width = int(cap.get(3))     #screen has created.
        height = int(cap.get(4))
    
        xD, yD = guidance("red", video, 135, 135, width, height)  #function from theScript is configureted.



        def theLoop(x:int):
            if x==500.5:
                set_rc_channel_pwm(6, 1400)
            elif x==0:
                set_rc_channel_pwm(5, 1650)
            elif x>0 and x<200:
                while x>5:
                    print(x)
                    set_rc_channel_pwm(6, 1550)
                set_rc_channel_pwm(6, 1500)
                theLoop()
            elif x<0:
                while x<-5:
                    print(x)
                    set_rc_channel_pwm(6, 1450)
                set_rc_channel_pwm(6, 1500)
                theLoop()
        theLoop(xD)
        

    
        break
    cap.release()
    cv2.destroyAllWindows()
colorTricking()


