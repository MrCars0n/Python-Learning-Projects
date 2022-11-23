# Carson Kramer
# More Functions - using TKinter
# 10/24/18
# Period 9

from time import *
from random import *
from tkinter import *

##################### SET UP THE WINDOW ########################

window = Tk()
window.title("Happy Haloween!")
c = Canvas(window, height = 300, width = 400)
c.pack()

##################### DRAW THE MONSTER #########################

body = c.create_oval(100, 150, 300, 250, fill = "green")
eye = c.create_oval(170, 70, 230, 130, fill = "white")
pupil = c.create_oval(190, 90, 210, 110, fill = "black")
mouth = c.create_oval(150, 220, 250, 240, fill = "red")

neck = c.create_line(200, 150, 200, 130)

hat = c.create_polygon(180, 75, 220, 75, 200, 20, fill = "blue")

speech = c.create_text(200,280, text = "BOO!")

##################### FUNCTION SECTION #########################

def mouthOpen(event):
    c.itemconfig(mouth, fill="black")

def mouthClosed(event):
    c.itemconfig(mouth, fill="red")

def blink(event):
    c.itemconfig(eye, fill = "green")
    c.itemconfig(pupil, state = HIDDEN)

def unblink(event):
    c.itemconfig(eye, fill = "white")
    c.itemconfig(pupil, state = NORMAL)

def eye_control(event):
    # Converts the event to the name of a key
    key = event.keysym

    if key == "Up":
        c.move(pupil, 0, -5)
    elif key == "Down":
        c.move(pupil, 0, 5)
    elif key == "Left":
        c.move(pupil, -5, 0)
    elif key == "Right":
        c.move(pupil, 5, 0)

def constant_blink(event):
    blink(event)
    c.update()
    sleep(.2)
    unblink(event)
    c.update()
    sleep(int(random() * 4) + 0.1)
##################### MAIN PART OF PROGRAM #####################

# Bind each function to a key/mouse button/etc...
c.bind_all("<KeyPress-o>", mouthOpen)
c.bind_all("<KeyPress-c>", mouthClosed)
c.bind_all("<Key>", eye_control)
c.bind_all("<Button-1>", blink)
c.bind_all("<Button-3>", unblink)           # 1 is left, 2 is middle, 3 is right
c.bind_all("<KeyPress-b>", constant_blink)
