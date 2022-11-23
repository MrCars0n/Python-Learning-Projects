# Carson Kramer
# Shared Digit
# 10/4/18
# Period 9

from math import *

number1 = float(input("Input your first Number: "))
number2 = float(input("Input your second Number: "))

r1 = floor((number1 * .1))
r2 = floor((number2 * .1))

if r1 == r2:
    print("Yes,", r1, "is shared!")
else:
    print("No!")
