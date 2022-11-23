# Group Program 3
# Create a list of ten random numbers either 1 or 2.
#  Find and count the longest streak of consecutive numbers.
#  1, 1, 2, 1, 2, 2, 2, 1, 2, 2 would print 3

from random import *

numList = []
currentStreak = 1
longestStreak = 1

for n in range(10):
    num = int(random() * 2) + 1
    numList.append(num)

for n in range(1,10):
    if numList[n-1] == numList[n]:
        currentStreak = currentStreak + 1

        if currentStreak > longestStreak:
            longestStreak = currentStreak

    else:
        currentStreak = 1

print(numList)
print(longestStreak)

    
