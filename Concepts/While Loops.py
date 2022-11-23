# Carson Kramer
# While Loops
# 10/26/18
# Period 9

# Indefinite Loop Examples

from random import *

# Roll a six-sided die until you get a 1
d= 0
count = 0

while d != 1:
    d = int(random() * 6) + 1
    count = count + 1
    print(d)
    
print("It took", count, "rolls")

# Enter a password until it is correct
password = ""

while password != "password":
    password = input("Please enter your password: ")
    if password != "password":
        print("Wrong Passoword, Try Again.")
print("Correct Password! Welcome, Carson!")

# Collatz Conjecture
# Take any positive number
#  - if it is even, divide it by 2
#  - if it is odd, multiply it by 3 and add 1

# WE BELIEVE* that every number eventually gets to 1

num = int(input("Enter a number: "))

while num > 1:
    if num % 2 == 0:
        num = num / 2
    else:
        num = num + 1
    print(num)
