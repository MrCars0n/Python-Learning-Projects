# Carson Kramer
# Functions in Python
# 10/22/18
# Period 9
# (See also - October 22nd Notes)

from math import *
from random import *
from turtle import *

speed(0)

# Put your functions at the top if the code so that they're all together and easy to find

def f(x):
    return x ** 2 + 1

def pyth(a,b):
    return sqrt(a**2 + b**2)

def rollDie():
    return int(random() * 6) + 1

# You can't name functions with duplicate names
def roll(n):
    return int(random() * n) + 1

def triangle():
    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)

def triangleSize(n):
    forward(n)
    right(120)
    forward(n)
    right(120)
    forward(n)

for n in range(1,100):
    triangleSize(n)

sides = int(input("Enter the number of sides of your dice: "))
if sides >= 1:
    print("You rolled a", roll(sides), "on your", sides, "sided die.")
print(f(4))
print(pyth(5,12))
print(rollDie())
