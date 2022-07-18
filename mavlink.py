from pymavlink import mavutil

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


def dMovment(pwm):
    set_rc_channel_pwm(5, pwm) # ileri git    
def lrMovment(pwm):
    set_rc_channel_pwm(6, pwm)
def fly(pwm):
    set_rc_channel_pwm(3, pwm)
def rotation(pwm):
    set_rc_channel_pwm(4, pwm)