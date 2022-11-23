# Carson Kramer
# If Statements - Continued
# 9/26/18
# Period 9

from random import *

num = int(random() * 100) + 1

print("Your number is", num)

# Is your number even or odd?
# "MOD" is short for modulus, which is a fancy term for remainder
# The % symbol is used for remainder

# "If the variable num can be divided by 2 without a remainder"
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# Is the number divisible by 2, 5, or 10?   (only print one of them)
if num % 10 == 0:
    print(num, "is divisible by 10")
elif num % 5 == 0:
    print(num, "is divisible by 5")
elif num % 2 == 0:
    print(num, "is divisible by 2")
else:
    print(num, "is not divisible by 2, 5, or 10")

# Roll two six sided dice
die1 = int(random() * 6) + 1
die2 = int(random() * 6) + 1

print("Your dice rolled", die1, "and", die2)

# Did you roll double sixes?
if die1 == 6 and die2 == 6:
    print("You rolled double sixes!")

# Did you roll a four?
if die1 == 4 or die2 == 4:
    print("You rolled a four!")


# If-Statements also work with Strings
username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == "Carson" and password == "password":
    print("Validated - please continue!")
else:
    print("INVAlID CREDENTIALS")

# This style works in Python, but not most languages

grade = int(input("Please enter your number grade to convert: "))

if 93 <= grade <= 100:
    print("You earned an A!")
