# Carson Kramer
# Heron's Formula
# 9/21/18
# Period 9

from math import *

a = float(input("Enter a side of a triangle: "))
b = float(input("Enter another side of a triangle: "))
c = float(input("Enter another side of a triangle: "))

perimiter = a + b + c
s = perimiter / 2
area = sqrt(s * (s - a) * (s - b) * (s - c))

print("The area is", area)
