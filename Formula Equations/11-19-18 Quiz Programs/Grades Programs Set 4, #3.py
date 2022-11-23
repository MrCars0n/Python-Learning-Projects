# Carson Kramer
# Grades Programs Set 4, #3
# 11/19/18
# Period 9

from random import *
randomName = int(random() * 4)
list1 = []
list1.append(input("Enter name 1: "))
list1.append(input("Enter name 2: "))
list1.append(input("Enter name 3: "))
list1.append(input("Enter name 4: "))
num1 = 3
print("Original:", list1)
for n in range(len(list1)):
    list1.append(list1[num1])
    list1.remove(list1[num1])
    num1 = num1 - 1
print("Reversed:", list1)
print(list1[randomName], "is my favorite of them all!")

