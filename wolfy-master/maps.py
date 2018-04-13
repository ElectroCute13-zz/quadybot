def mapyy(v, x1, x2, y1, y2):
    length1 = x2 - x1
    length2 = y2 - y1
    d = length2 / length1
    n = v - x1 + 1
    t = y1 + (n - 1) * d
    return t
