# Carson Kramer
# Guess the Number
# 9/25/18
# Period 9

# Computer pick a random number from 1 to 100
# We will guess, the computer will respond higher or lower, or win

from random import *

number = int(random() * 100) + 1
print("I am thinking of a number from 1 to 100...")

for x in range(10):
    guess = int(input("Please enter your guess: "))

    if guess > number:
        print("Your guess was too high")
    if guess < number:
        print("Your guess was too low")
    if guess == number:
        print("You got it right!")
        exit()
