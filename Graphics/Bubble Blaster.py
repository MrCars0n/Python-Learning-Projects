# Bubble Blaster
# Period 9
# 11-12-2018
# Carson Kramer

from tkinter import *
from random import *
from time import *
from math import *

# Any varialbe which we may watn to change later, we use these constant-type variables
# - writing them in all caps to make them easy to find
HEIGHT = 500
WIDTH = 800

# Create the game window (500 x 800 pixels)
window = Tk()
window.title("Bubble Blaster")
window.resizable(0,0)
c = Canvas(window, width = WIDTH, height = HEIGHT, bg = "darkblue")
c.pack()
# Draw the player's ship
ship_id = c.create_polygon(5,5,5,25,30,15,fill="yellow")
ship_id2 = c.create_oval(0,0,30,30,outline="darkblue")

# Define the "size" of our ship
SHIP_R = 15

# Define the screen's midpoint
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2

# Start the ship in the center to begin the game
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)

# Function to move our ship using the arrow keys
# We call this an "event handler" - it "handles" what happens when we press a key

# this is the ship's speed (20 pixels with each key)
SHIP_SPD = 20

def move_ship(event):
    if event.keysym == "Up":
        c.move(ship_id, 0, -SHIP_SPD)
        c.move(ship_id2, 0, -SHIP_SPD)
        
    elif event.keysym == "Down":
        c.move(ship_id, 0, SHIP_SPD)
        c.move(ship_id2, 0, SHIP_SPD)
        
    elif event.keysym == "Left":
        c.move(ship_id, -SHIP_SPD, 0)
        c.move(ship_id2, -SHIP_SPD, 0)
        
    elif event.keysym == "Right":
        c.move(ship_id, SHIP_SPD, 0)
        c.move(ship_id2, SHIP_SPD, 0)

# We now have to bind the keys to the move ship function
c.bind_all("<Key>", move_ship)

#######################################################################
############################# The Bubbles #############################
#######################################################################

bub_id = list()
bub_r = list()
bub_speed = list()

MIN_BUB_R = 10
MAX_BUB_R = 30

MAX_BUB_SPEED = 10

GAP = 100

def create_bubbles():
    # Creates ONE bubble
    x = WIDTH + GAP
    y = int(random() * HEIGHT)
    
    r = int(random() * (MAX_BUB_R - MIN_BUB_R + 1) + MIN_BUB_R)

    id1 = c.create_oval(x-r,y-r,x+r,y+r, outline="white")
    speed = int(random() * MAX_BUB_SPEED) + 1

    # Now, add your one bubble to the list of all the bubbles!
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(speed)

def move_bubbles():
    for n in range(len(bub_id)):
        c.move(bub_id[n], -bub_speed[n], 0)

def get_coords(id_num):
    pos = c.coords(id_num)
    
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2

    return x, y

def del_bubbles(n):
    c.delete(bub_id[n])
    del bub_id[n]
    del bub_r[n]
    del bub_speed[n]

def clean_up_bubs():
    for n in range(len(bub_id)-1, -1, -1):
        x, y = get_coords(bub_id[n])

        if x < -GAP:
            del_bubbles(n)

def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)

    return sqrt((x2-x1)**2 + (y2-y1)**2)

def collision():
    points = 0

    for bub in range(len(bub_id)-1, -1, -1):
        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points = points + bub_r[bub] + bub_speed[bub]
            del_bubbles(bub)

    return points

##########################################################################
############################# TIME AND SCORE #############################
##########################################################################

c.create_text(50, 30, text = "TIME", fill = "white")
c.create_text(150, 30, text = "SCORE", fill = "white")

time_text = c.create_text(50, 50, fill = "white")
score_text = c.create_text(150, 50, fill = "white")

def show_score(score):
    c.itemconfig(score_text, text = str(score))

def show_time(time_left):
    c.itemconfig(time_text, text = str(time_left))

##########################################################################
############################# MAIN GAME LOOP #############################
##########################################################################

BUB_CHANCE = 10

TIME_LIMIT = 30

# Every 100 points, add 30 seconds
BONUS_SCORE = 1000

score = 0
bonus = 0

end = time() + TIME_LIMIT

while time() < end:
    if int(random() * BUB_CHANCE) == 0:
        create_bubbles()
    move_bubbles()
    clean_up_bubs()

    score = score + collision()

    if int(score/BONUS_SCORE) > bonus:
       bonus = bonus + 1
       end = end + TIME_LIMIT

    show_score(score)
    show_time(int(end-time()))

    window.update()
    sleep(.01)
