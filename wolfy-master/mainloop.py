from motion import move


def translate(value, InputMin, InputMax, OutMin, OutMax):
    InSpan = InputMax - InputMin
    OutSpan = OutMax - OutMin
    valueScaled = float(value - InputMin) / float(InSpan)
    return OutMin + (valueScaled * OutSpan)


# from pistart import pwm


def mainloop(j, sx, ex, srange, erange, ups, ls):
    k2 = translate(j, sx, ex, srange, erange)
    y2 = 150
    # put your y2 equation here
    te3, te4 = move(k2, y2)
    alpha = translate(te3, 0, 180, ups.sp, ups.ep)
    beta = translate(te4 - 90, 0, 180, ls.sp, ls.ep)
    return alpha, beta
