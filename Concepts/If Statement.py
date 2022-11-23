# Carson Kramer
# If Statement
# 9/25/18
# Period 9

# Computer picks a random number from -10 to 10
# It says whether the number is positive, negative, or zero
from random import *

# Range is 21 = (10 - (-10)) + 1
# Lowest number is -10
# number = int(random() * 21) - 10
while True:
    number = float(input("Enter a number: "))


if number > 0:
    print("%.0F" % number, "is positive!")

if number < 0:
    print("%.0F" % number, "is negative!")

if number == 0:
    print("%.0F" % number, "is zero!")

