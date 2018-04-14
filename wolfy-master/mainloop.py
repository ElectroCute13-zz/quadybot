from maps import translate
from pistart import l

global i, j, sx, ex, sr, se


# from pistart import pwm


def mainloop(j, sx, ex, srange, erange, ups, ls, a, b):
    k2 = translate(j, sx, ex, srange, erange)
    y2 = 150
    # put your y2 equation here
    te3, te4 = l.move(k2, y2)
    alpha = translate(te3, 0, 180, ups.sp, ups.ep)
    beta = translate(te4 - 90, 0, 180, ls.sp, ls.ep)
    # pwm.set_pwm(a, 0, int(alpha))
    #pwm.set_pwm(b, 0, int(beta))
    return alpha, beta
