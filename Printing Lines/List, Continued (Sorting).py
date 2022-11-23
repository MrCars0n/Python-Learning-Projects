# Carson Kramer
# List, Continued (Sorting)
# 10/31/18
# Period 9

from random import *

rollList = []


for n in range(10):
    roll = int(random() * 100)
    rollList.append(roll)

print("The unsorted list is\t\t", rollList)

# Sort from least to greatest
rollList.sort()
print("The sorted list is\t\t", rollList)

# Sort from greatest to least
rollList.sort(reverse = True)
print("The sorted list in reverse is\t", rollList)

# To get the length of a list
num = 0
numList = []

while num != 20:
    num = int(random() * 20) + 1
    numList.append(num)

print(numList)
print(len(numList))     # len is the length of the list

# To get part of a list (slice)
languages = ["ada", "basic", "cobol", "python", "java"]

print(languages)
print(languages[0 : 2]) # ada and basic
print(languages[2 : 3]) # just cobal
