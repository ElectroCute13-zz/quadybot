from maps import mapyy
from pistart import l

global i, j, sx, ex, sr, se
from pistart import pwm


def mainloop(j, y, sx, ex, srange, erange, ups, ls, a, b):
    k2 = mapyy(j, sx, ex, srange, erange)
    # y2 = -(10 * sqrt(1 - ((pow(k2, 2)) / 1600)))
    # put your y2 equation here
    te3, te4 = l.move(k2, y2)
    alpha = mapyy(te3, 0, 180, ups.sp, ups.ep)
    beta = mapyy(te4 - 90, 0, 180, ls.sp, ls.ep)
    pwm.set_pwm(a, 0, alpha)
    pwm.set_pwm(b, 0, beta)
    return alpha, beta
