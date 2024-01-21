from math import sqrt, isnan, isinf


def solve(a, b, c, e=10**(-5)):
    if isnan(a) or isnan(b) or isnan(c):
        raise ValueError('Not a number')
    if isinf(a) or isinf(b) or isinf(c):
        raise ValueError('Infinity')
    if abs(a) < e:
        raise ValueError('a cannot be 0')
    D = b*2 - 4*a*c
    if D < 0:
        return ()
    elif abs(D) > e:
        x = (-b + sqrt(D)) / (2*a)
        y = (-b - sqrt(D)) / (2*a)
        return x, y
    elif abs(D) < e:
        x = -b / (2*a)
        return x, x