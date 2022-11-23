# Carson Kramer
# Grades Programs Set 4, #4
# 11/19/18
# Period 9

number = int(input("Please enter a number: "))
list1 = []
numsum = 0
for factor in range(1, number + 1):
    if number % factor == 0 and factor != number:
        list1.append(factor)
#        print(factor, "+ ", end = "")
for n in range(len(list1)):
    numsum = numsum + list1[n]

if numsum == number:
    print("Perfect!")
elif numsum < number:
    print("Deficient!")
elif numsum > number:
    print("Abundant!")
