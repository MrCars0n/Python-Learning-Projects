# Carson Kramer
# Factoring Trinomials
# 9/14/18
# Period 9

from math import *

print("Enter the A, B, and C values of a trinomial")

a = float(input("Enter an A value: "))
b = float(input("Enter a B value: "))
c = float(input("Enter a C value: "))

xplus = (-b + sqrt(abs((b ** 2) - (4 * a * c)))) / (2 * a)
xminus = (-b - sqrt(abs((b ** 2) - (4 * a * c)))) / (2 * a)

print("X =", xplus, "or X =", xminus)
