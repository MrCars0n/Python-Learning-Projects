# Carson Kramer
# Math Commands (and how to use decimals!)
# 9/13/18
# Period 9

# Remember, integers 0which use int) are whole numers +/-
# To use decimals, we have to use float
# (The technical name for decimals is "floating point numbers")

# "from math import *" used for complex math, not basic math
from math import *


num = float(input("Please enter a number: "))

print("The absolute value is ", abs(num))
print("The ceiling is ", ceil(num))
print("The floor is ", floor(num))
print("The square root is ", sqrt(num))

print(factorial(15))
print(gcd(24,30))
print("Pi = ", pi)
print("e = ", e)

# Find the circumference of a circle
radius = int(input("Type in the radius of a circle: "))
circum = 2 * pi * radius
print("The circumference is ", "%.2f" % circum)
