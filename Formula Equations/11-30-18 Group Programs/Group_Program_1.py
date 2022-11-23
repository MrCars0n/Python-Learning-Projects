# Program 1
# Create a list of twenty random numbers from 1 to 100.
# Count the number of perfect squares in your list.

from random import *
from math import *

numList = []
count = 0

for n in range(20):
    num = int(random()*100) + 1
    numList.append(num)
    if sqrt(num) == int(sqrt(num)):
        count = count + 1

print(numList)
print(count)

