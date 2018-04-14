import time
from mainloop import *
from servo_calib import servo_cal

import Adafruit_PCA9685
# import gpio as GPIO

# GPIO.setmode(GPIO.BCM)
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

s1 = servo_cal(1, 550, 175)
s2 = servo_cal(2, 510, 175)
s3 = servo_cal(3, 180, 520)
s4 = servo_cal(4, 165, 555)
s5 = servo_cal(5, 500, 155)
s6 = servo_cal(6, 160, 540)
s7 = servo_cal(7, 170, 525)
s8 = servo_cal(8, 525, 170)

def wolfxy(s, st_x, en_x, step):
    for i in range(s):

        for j in range(st_x, en_x, step):

            #####################################
            ##########     leg1       ###########
            #####################################
            if j in range(31):
                a1,b1=mainloop(j, 0, 30, -40, -20, s1, s2)
                pwm.set_pwm(0, 0, int(a1))
                pwm.set_pwm(1, 0, int(b1))
                print("a1 {} and bi {}".format(a1,b1))
                print('loop1')
                #####################################
                ##########     leg2       ###########
                #####################################
                a2,b2=mainloop(j, 0, 30, 5, 40, s3, s4)
                pwm.set_pwm(2, 0, int(a2))
                pwm.set_pwm(3, 0, int(b2))
                print("a2 {} and b2 {}".format(a2, b2))
                print('loop2')
                #####################################
                ##########     leg3       ###########
                #####################################

                a3,b3=mainloop(j, 0, 30, 40, -40, s5, s6)
                pwm.set_pwm(4, 0, int(a3))
                pwm.set_pwm(5, 0, int(b3))
                print("a3 {} and b3 {}".format(a3, b3))
                print('loop3')

                #####################################
                ##########     leg4       ###########
                #####################################

                a4,b4=mainloop(j, 0, 30, -20, 5, s7, s8)
                pwm.set_pwm(6, 0, int(a4))
                pwm.set_pwm(7, 0, int(b4))
                print("a4 {} and b4 {}".format(a4, b4))
                print('loop4')

            elif j in range(31, 61):
                #####################################
                ##########     leg1       ###########
                #####################################

                a1,b1=mainloop(j, 31, 60, -20, 5, s1, s2)
                print('loop11')
                pwm.set_pwm(0, 0, int(a1))
                pwm.set_pwm(1, 0, int(b1))
                print("a1 {} and bi {}".format(a1, b1))
                #####################################
                ##########     leg2       ###########
                #####################################

                a2,b2=mainloop(j, 31, 61, 40, -40, s3, s4)
                print('loop21')
                pwm.set_pwm(2, 0, int(a2))
                pwm.set_pwm(3, 0, int(b2))
                print("a2 {} and b2 {}".format(a2, b2))
                #####################################
                ##########     leg3       ###########
                #####################################

                a3,b3=mainloop(j, 31, 61, -40, -20, s5, s6)
                print('loop31')
                pwm.set_pwm(4, 0, int(a3))
                pwm.set_pwm(5, 0, int(b3))
                print("a3 {} and b3 {}".format(a3, b3))

                #####################################
                ##########     leg4       ###########
                #####################################

                a4,b4 = mainloop(j, 31, 61, 5, 40, s7, s8)
                print('loop41')
                pwm.set_pwm(6, 0, int(a4))
                pwm.set_pwm(7, 0, int(b4))
                print("a4 {} and b4 {}".format(a4, b4))

            elif j in range(61, 91):
                #####################################
                ##########     leg1       ###########
                #####################################

                a1,b1=mainloop(j, 61, 91, 5, 40, s1, s2)
                print('loop51')
                pwm.set_pwm(0, 0, int(a1))
                pwm.set_pwm(1, 0, int(b1))
                print("a1 {} and bi {}".format(a1, b1))
                #####################################
                ##########     leg2       ###########
                #####################################

                a2,b2=mainloop(j, 61, 91, -40, -20, s3, s4)
                print('loop61')
                pwm.set_pwm(2, 0, int(a2))
                pwm.set_pwm(3, 0, int(b2))
                print("a2 {} and b2 {}".format(a2, b2))
                #####################################
                ##########     leg3       ###########
                #####################################

                a3,b3=mainloop(j, 61, 91, -20, 5, s5, s6)
                print('loop71')
                pwm.set_pwm(4, 0, int(a3))
                pwm.set_pwm(5, 0, int(b3))
                print("a3 {} and b3 {}".format(a3, b3))

                #####################################
                ##########     leg4       ###########
                #####################################

                a4,b4=mainloop(j, 61, 91, 40, -40, s7, s8)
                pwm.set_pwm(6, 0, int(a4))
                pwm.set_pwm(7, 0, int(b4))
                print('loop81')
                print("a4 {} and b4 {}".format(a4, b4))

            elif j in range(91, 121):
                #####################################
                ##########     leg1       ###########
                #####################################

                a1,b1=mainloop(j, 91, 121, 40, -40, s1, s2)
                print('loop91')
                pwm.set_pwm(0, 0, int(a1))
                pwm.set_pwm(1, 0, int(b1))
                print("a1 {} and bi {}".format(a1, b1))
                #####################################
                ##########     leg2       ###########
                #####################################

                a2,b2=mainloop(j, 91, 121, -20, 5, s3, s4)
                print('loop101')
                pwm.set_pwm(2, 0, int(a2))
                pwm.set_pwm(3, 0, int(b2))
                print("a2 {} and b2 {}".format(a2, b2))
                #####################################
                ##########     leg3       ###########
                #####################################

                a3,b3=mainloop(j, 91, 121, 5, 40, s5, s6)
                print('loop111')
                pwm.set_pwm(4, 0, int(a3))
                pwm.set_pwm(5, 0, int(b3))
                print("a3 {} and b3 {}".format(a1, b1))
                #####################################
                ##########     leg4       ###########
                #####################################

                a4,b4=mainloop(j, 91, 121, -40, -20, s7, s8)
                print('loop121')
                pwm.set_pwm(6, 0, int(a4))
                pwm.set_pwm(7, 0, int(b4))
                print("a4 {} and b4 {}".format(a4, b4))

            else:
                print("nothing works")
                break


if __name__ == "__main__":
    while (True):
        wolfxy(2, 0, 121, 1)
        time.sleep(1)
        wolfxy(2, 120, 0, -1)
        time.sleep(1)
