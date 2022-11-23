# Carson Kramer
# Monday Turtle Exploration 2
# 9/24/18
# Period 9

# We also need random here, for the "choice" command to pick a random color
from turtle import *
from random import *

# Again, if you get impatient, take the # off the line below
# speed(0)

# Oooo, a list of colors!? I wonder what other colors you could use...
colors = ["red", "purple", "blue", "green", "orange"]

for x in range(150):
    pencolor(choice(colors))
    width(x/10 + 1)
    forward(x)
    left(59)

# 1) What ARE some other colors you can pick from?
#       antiquewhite, cadetblue, carrot, etc.
# 2) What the heck does width(x/10 + 1) do?
#       It sets the width of the brush
# 3) What happens when you change the left() number?
#       It changes the angle of the pen
