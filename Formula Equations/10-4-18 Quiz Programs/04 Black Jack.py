# Carson Kramer
# Black Jack
# 10/4/18
# Period 9

from random import *
from math import *

n1 = int(random() * 11) + 2
n2 = int(random() * 11) + 2
n3 = int(random() * 11) + 2

s1 = n1 + n2 + n3

if s1 == 21:
    print(n1, n2, n3,", The sum is", s1, "\tBLACKJACK!")
elif s1 > 21:
    print(n1, n2, n3, ", The sum is", s1, "\tBUSTED!")
else:
    print(n1, n2, n3, ", The sum is", s1)
