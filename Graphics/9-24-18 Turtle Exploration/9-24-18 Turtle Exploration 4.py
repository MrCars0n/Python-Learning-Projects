# Carson Kramer
# Monday Turtle Exploration 4
# 9/24/18
# Period 9

from turtle import *
from random import *

# Okay, your turn to make something fun!
# You've checked out three programs and learned a few commands
# forward, right, left, circle, pencolors, loops, etc...

# Now, draw something!  Save it so that you can show me tomorrow.

speed(0)

for x in range(150):
    r1= random()
    b1= random()
    g1= random()
    pencolor(r1,g1,b1)
    backward(88)
    circle(66)
    forward(88)
    left(x*8)
