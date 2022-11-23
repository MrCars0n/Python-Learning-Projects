# Carson Kramer
# Warm-up
# 11/29/18
# Period 9

from random import *

numList1 = []
numList2 = []

count = 0

for n in range(5):
    numList1.append(int(random() * 10) + 1)
    numList2.append(int(random() * 10) + 1)
    
print(numList1)
print(numList2)

for n in range(5):
    if numList1[n-1] in numList2:
        count = count + 1

print(count)
