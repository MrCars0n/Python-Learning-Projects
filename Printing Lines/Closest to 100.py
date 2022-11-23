# Carson Kramer
# Closest to 100
# 10/11/18
# Period 9

from math import *
from random import *

print("There are two players in this game. Each player will roll 2 dice.\nThe numbers rolled will be multiplied and then added to the total. \nThe player can roll as many times as they want to try and be the closest, or be exactly on 100.\nIf you go over 100 however, you automatically loose. Roll Wisley!")

player1name = input("Enter the name of player 1: ")
player1score = 0
player2name = input("Enter the name of player 2: ")
player2score = 0
player1choice = "Y"
player2choice = "Y"
player1turn = "true"
player2turn = "false"


while player1name == player2name:
    player2name = input("Player 1 cannot have the same name as Player 2.\nPlease enter a new Player 2 name:")
        
print("It's", player1name, "'s turn!")

while player1turn == "true":

    if player1score <= 100:
        player1choice = input("Would you like to roll the dice? (Y or N): ")
        if player1choice == "Y":
            player1roll = (int(random() * 6) + 1) * (int(random() * 6) + 1)
            player1score = player1score + player1roll
            print("Your current count is", player1score)
        elif player1choice != "Y":
            print("It's", player2name, "'s turn!")
            player2turn = "true"
            player1turn = "false"
    else:
        print("It's", player2name, "'s turn!")
        player2turn = "true"
        player1turn = "false"
        
while player2turn == "true":

    if player2score <= 100:
        player2choice = input("Would you like to roll the dice? (Y or N): ")
        if player2choice == "Y":
            player2roll = (int(random() * 6) + 1) * (int(random() * 6) + 1)
            player2score = player2score + player2roll
            print("Your current count is", player2score)
        elif player2choice != "Y":
            player2turn = "false"
    else:
        player2turn = "false"
        
if player2turn == "false" and player1turn == "false":
    print("The Game is over")
    if (player2score > player1score or player1score > 100) and player2score <= 100:
        print(player2name, "won with a score of", player2score, "!")
    elif (player1score > player2score or player2score > 100) and player1score <= 100:
        print(player1name, "won with a score of", player1score, "!")
    elif player2score == player1score:
        print("It is a tie!")
    elif player2score > 100 and player1score > 100:
        print("Both", player1name, "and", player2name, "lost.")
    else:
        print("The Winner is Undetermind")
