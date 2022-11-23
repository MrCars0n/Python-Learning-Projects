from math import *
from fractions import *
while True:
    x=0
    y = input("X: ")

    if float(y) % 1 != 0:
        num,den = map(float, y.split('/'))
        x = num/den
    else:
        x=float(y)

    solution = (4 * (x ** 5)) - (52*(x**3)) + (48*(x**2))
    print(Fraction(solution).limit_denominator())
