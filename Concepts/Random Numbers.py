# Carson Kramer
# Random Numbers in Python
# 9/18/18
# Period 9

# First, understand that a computer can't make truly random numbers
# It makes what are called "pseudorandom numbers"

from random import *

for n in range(20):
    num = int(random() * 6 + 1)
    print("A random number is:", num)
