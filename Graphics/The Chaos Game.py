# Carson Kramer
# 9-7-18
# Period 9
# The Chaos Game

from tkinter import *
from random import *

window = Tk()
window.title("The Chaos Game")

c = Canvas(window, width = 1920, height = 1080, bg = 'black')
c.pack()

x1 = 960
y1 = 0

x2 = 0
y2 = 1080

x3 = 1920
y3 = 1080

x = randint(0, 1920)
y = randint(0, 1080)

while True:
    n = randint(1,3)

    if n==1:
        x = (x + x1) / 2
        y = (y + y1) / 2
    if n==2:
        x = (x + x2) / 2
        y = (y + y2) / 2
    if n==3:
        x = (x + x3) / 2
        y = (y + y3) / 2

    c.create_line(x,y,x+1,y+1,fill="yellow")
    window.update()
