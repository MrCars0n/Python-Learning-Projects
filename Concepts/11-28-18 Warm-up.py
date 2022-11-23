# Carson Kramer
# Warm-up
# 11/28/18
# Period 9

from random import *

list1 = []
count = 0

for n in range(10):
    num = int(random() * 10) + 1
    list1.append(num)
print("Original:", list1)
list1.sort()
print("Sorted:", list1)

for n in range(10):
    if list1[n-1] < 3:
        count = count + 1
print("There are", count, "numbers in the list under 3.")
