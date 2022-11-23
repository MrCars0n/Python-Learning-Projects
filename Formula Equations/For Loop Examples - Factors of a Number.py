# Carson Kramer
# For Loop Examples - Factors of a Number
# 11/5/18
# Period 9

number = int(input("Please enter a number: "))

for factor in range(1, number + 1):
    if number % factor == 0:
        print(factor)

# How to find a prime number
count = 0

for factor in range(1, number + 1):
    if number % factor == 0:
        count = count + 1

if count == 2:
    print(number, "is a prime number!")
else:
    print(number, "is not a prime number!")

# Now, we can take that code and repeat all of it using another loop!
# Find all of the primes from 1 to 1,000,000

for number in range(1, 1000001):
    count = 0

    for factor in range(1, number + 1):
        if number % factor == 0:
            count = count + 1

    if count == 2:
        print(number)
