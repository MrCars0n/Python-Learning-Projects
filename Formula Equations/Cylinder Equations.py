# Carson Kramer
# Cylinder Equations
# 9/13/18
# Period 9

# Enter the radius and height of a cylinder
# Print the surface area and volume of the cylinder

from math import *

# STEP 1 - INPUT (GET THE NUMBERS)
height = float(input("Enter a cylinder height: "))
radius = float(input("Enter a cylinder base radius: "))

# STEP 2 - DO THE FORMULA/CALCULATION
sa = (2 * pi * radius * height) + (2 * pi * (radius ** 2))
volume = pi * (radius ** 2) * height

print("The surface area is", "%.2f" % sa)
print("The volume is", "%.2f" % volume)
