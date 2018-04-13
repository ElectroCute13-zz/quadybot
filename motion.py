from math import *


class leg:
    def __init__(self, ul, ll):
        self.ul = ul
        self.ll = ll

    def move(self, x1, y1):
        a = self.ul
        b = self.ll
        c = sqrt(pow(x1, 2) + pow(y1, 2))
        betaf = degrees(acos((pow(a, 2) + pow(b, 2) - pow(c, 2)) / (2 * a * b)))
        alpha1 = degrees(acos((pow(a, 2) + pow(c, 2) - pow(b, 2)) / (2 * a * c)))
        alphaf = 90 + alpha1
        return alphaf, betaf
