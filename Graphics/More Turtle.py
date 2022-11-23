# Carson Kramer
# More Turtles and Ifs
# 10/1/18
# Period 9

from turtle import *
from random import *

title("Connect the dots")       # Put a title on the window
setup(500,500,0,0)              # (length, width, start X, start Y)
width(5)                        # Thickness of your pen
speed(0)                        # Speed of the turtle (0 fastest -10)

for n in range(500):
    x = int(random() * 501) - 250
    y = int(random() * 501) - 250

    goto(x,y)

    if x >= -50 and x <= 50 and y>= -50 and y<=50:
        dot(20, "red")
    else:
        dot(10, "green")
        

















    
