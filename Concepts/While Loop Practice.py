# Carson Kramer
# While Loop Practice
# 10/29/18
# Period 9

# Rolling 2 six-sided dice, add the totals, keep going until you roll a total of 7

from random import *

total = 0
count = 0
n = 0

while total != 7:
    die1 = int(random() * 6) + 1
    die2 = int(random() * 6) + 1
    count = count + 1
    total = die1 + die2
    print(die1, "+", die2, "=", total)
if count == 1:
    print("It took you", count, "roll to get to a sum of 7.")
else:
    print("It took you", count, "rolls to get to a sum of 7.")

# Make a spiral using Turtle, but keep within a certain boundary

from turtle import *
from math import *
speed(0)

while xcor() > -200 and xcor() < 200 and ycor() > -200 and ycor() < 200:
    r = random()
    b = random()
    g = random()
    forward(n)
    right(n ** pi)
    pencolor(r,b,g)
    n = n + int(random() * 10) + 1
