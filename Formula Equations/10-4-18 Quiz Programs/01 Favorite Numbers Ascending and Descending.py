# Carson Kramer
# Favorite Numbers Ascending & Descending
# 10/4/18
# Period 9

from math import *

first = float(input("Enter your first favorite number: "))
second = float(input("Enter your second favorite number: "))
third = float(input("Enter your third favorite number: "))

if first < second and second < third:
    print("Ascending!")
elif first > second and second > third:
    print("Descending!")
else:
    print("Neither!")
