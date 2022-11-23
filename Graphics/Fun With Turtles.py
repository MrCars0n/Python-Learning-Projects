# Carson Kramer
# 8-28-18
# Period 9
# Fun with Turtles

from turtle import *
from random import *

r1= random()
b1= random()
g1= random()

shape("turtle")
speed(0)
pensize(20)
bgcolor(r1,g1,b1)

while True:
    x = int(random() * 1920) - 960
    y = int(random() * 1080) - 540
    r2= random()
    b2= random()
    g2= random()
    pencolor(r2,g2,b2)

    penup()
    goto(x,y)
    pendown()
    forward(1)
