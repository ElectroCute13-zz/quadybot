from math import *

from servo_calib import servo_cal


def translate(value, InputMin, InputMax, OutMin, OutMax):
    leftSpan = InputMax - InputMin
    rightSpan = OutMax - OutMin
    valueScaled = float(value - InputMin) / float(leftSpan)
    return OutMin + (valueScaled * rightSpan)


a = 75
b = 100


def move(x1, y1):
    c = sqrt(pow(x1, 2) + pow(y1, 2))
    betaf = degrees(acos((pow(a, 2) + pow(b, 2) - pow(c, 2)) / (2 * a * b)))
    alpha1 = degrees(acos((pow(a, 2) + pow(c, 2) - pow(b, 2)) / (2 * a * c)))
    alphaf = 90 + alpha1
    return alphaf, betaf


# import Adafruit_PCA9685
# import gpio as GPIO

# GPIO.setmode(GPIO.BCM)
# pwm = Adafruit_PCA9685.PCA9685()
# pwm.set_pwm_freq(50)

s1 = servo_cal(1, 550, 175)
s2 = servo_cal(2, 510, 175)
s3 = servo_cal(3, 180, 520)
s4 = servo_cal(4, 165, 555)
s5 = servo_cal(5, 500, 155)
s6 = servo_cal(6, 160, 540)
s7 = servo_cal(7, 170, 525)
s8 = servo_cal(8, 525, 170)

if __name__ == "__main__":

    for i in range(3):
        for j in range(150):
            if j in range(31):
                k2 = translate(j, 0, 30, -40, -24)
                y2 = 150
                # put your y2 equation here
                te3, te4 = move(k2, y2)
                alpha = translate(te3, 0, 180, s1.sp, s1.ep)
                beta = translate(te4 - 90, 0, 180, s2.sp, s2.ep)
                print("{} and {} ".format(alpha, beta))
            elif j in range(31, 61):
                k2 = translate(j, 31, 61, -23, -9)
                y2 = 150
                # put your y2 equation here
                te3, te4 = move(k2, y2)
                alpha = translate(te3, 0, 180, s1.sp, s1.ep)
                beta = translate(te4 - 90, 0, 180, s2.sp, s2.ep)
                print("{} and {} ".format(alpha, beta))
            elif j in range(61, 91):
                k2 = translate(j, 61, 91, -8, 8)
                y2 = 150
                # put your y2 equation here
                te3, te4 = move(k2, y2)
                alpha = translate(te3, 0, 180, s1.sp, s1.ep)
                beta = translate(te4 - 90, 0, 180, s2.sp, s2.ep)
                print("{} and {} ".format(alpha, beta))

            elif j in range(91, 121):
                k2 = translate(j, 91, 121, 9, 25)
                y2 = 150
                # put your y2 equation here
                te3, te4 = move(k2, y2)
                alpha = translate(te3, 0, 180, s1.sp, s1.ep)
                beta = translate(te4 - 90, 0, 180, s2.sp, s2.ep)
                print("{} and {} ".format(alpha, beta))

            elif j in range(121, 150):
                k2 = translate(j, 91, 121, 26, 40)
                y2 = 130
                # put your y2 equation here
                te3, te4 = move(k2, y2)
                alpha = translate(te3, 0, 180, s1.sp, s1.ep)
                beta = translate(te4 - 90, 0, 180, s2.sp, s2.ep)
                print("{} and {} ".format(alpha, beta))
        print("once")
