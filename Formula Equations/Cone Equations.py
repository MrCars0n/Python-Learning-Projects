# Carson Kramer
# Cone Equations
# 9/20/18
# Period 9

from math import *

# STEP 1 - INPUT (GET THE NUMBERS)
height = float(input("Enter a cone height: "))
radius = float(input("Enter a cone base radius: "))

# STEP 2 - DO THE FORMULA/CALCULATION
sa = (pi * radius) * (radius + sqrt(pow(height, 2) + pow(radius, 2)))
volume = pi * (radius ** 2) * (height / 3)

print("The surface area is", "%.2f" % sa)
print("The volume is", "%.2f" % volume)
