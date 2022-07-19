from pymavlink import mavutil
import time



master = mavutil.mavlink_connection(  # aracin baglantisi
    '/dev/serial0',
    baud=57600)



def set_rc_channel_pwm(id, pwm=1500):

    if id < 1:
        print("Channel does not exist.")
        return

    if id < 9:  # ardusubla iletisim
        rc_channel_values = [65535 for _ in range(8)]
        rc_channel_values[id - 1] = pwm
        master.mav.rc_channels_override_send(
            master.target_system,
            master.target_component,
            *rc_channel_values)

x=1500
while x < 2000:
    x+=50
    print(x)
    time.sleep(5)