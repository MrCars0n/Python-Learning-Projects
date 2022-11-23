# Carson Kramer
# Tutles (If and Randoms)
# 9/27/18
# Period 9

from turtle import *
from random import *

speed(0)
width(5)

while True:
    r1 = random()
    b1 = random()
    g1 = random()
    d = int(random() * 4) + 1
    pencolor(r1,b1,g1)
    if d==1:
        setheading(0)
    elif d==2:
        setheading(90)
    elif d==3:
        setheading(180)
    elif d==4:
        setheading(270)

    forward(5)
