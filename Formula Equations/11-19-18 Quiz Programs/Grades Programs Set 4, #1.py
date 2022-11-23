# Carson Kramer
# Grades Programs Set 4, #1
# 11/19/18
# Period 9

num1 = int(input("Enter your first number: "))
num2 = int(input("enter your second number: "))

numadd = num1
list1 = []

for n in range(num2 - num1 + 1):
    list1.append(numadd)
    numadd = numadd + 1

print(list1, "\t", sum(list1))
