class servo_cal:
    print("servos were calibrated")
    servo_count = 0

    def __init__(self, num, startp, endp):
        self.number = num
        self.sp = startp
        self.ep = endp
        servo_cal.servo_count += 1
