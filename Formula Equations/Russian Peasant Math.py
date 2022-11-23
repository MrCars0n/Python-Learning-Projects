# Carson Kramer
# Russian Peasant Math
# 10/29/18
# Period 9

from math import *

left = int(input("Enter your first multiplication number: "))
right = int(input("Enter your second multiplication number: "))

leftOrigin = left
rightOrigin = right

total = 0

# We must go to "zero", nto one, because we need to use the final step, which is when the left is one

while left != 0:
    print(left, "\t", right)

    if left % 2 == 1:
        total = total + right

    left = int(left / 2)
    right = right * 2
print(leftOrigin, "+", rightOrigin, "=", total)
