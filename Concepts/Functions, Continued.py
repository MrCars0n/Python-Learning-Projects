# Carson Kramer
# Functions, continued
# 10/23/18
# Period 9
# WELCOME TO THE DRAGON'S REALM!

from random import *
from time import *
import emoji

def displayIntro():
    print("You are in a land full of dragons! In front of you, \nyou see two caves. In one cave, the dragon is friendly\nand will share its treasure with you. The other dragon\nis greedy and hungry and eats you on sight.\n")

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        cave = input("Which cave will you go into, 1 or 2? ")

    return cave

def checkCave(chosenCave):
    print("\nYou approach the cave...")
    sleep(1)
    print("It is dark and spooky...")
    sleep(1)
    print("a dragon leaps out in fround of you, and...")
    sleep(2)

    friendlyCave = int(random() * 2) + 1
    if chosenCave == str(friendlyCave):
        print("gives you its treasure.")
    else:
        print("eats you whole in one bite!")
######################### END FUCNTIONS, BEGIN MAIN PROGRAM #########################

playAgain = "yes"

while playAgain == "yes" or playAgain == "y" or playAgain == "Y" or playAgain == "Yes":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    playAgain = input("\nDo you want to play again? ")
