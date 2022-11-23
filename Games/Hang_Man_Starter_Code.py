# Name: Carson Kramer
# Date: 12/10/18
# Period: 9
# Hangman

from random import *

# HANGMANPICS is a constant variable thus all-CAPS

HANGMANPICS=["""

   +---+
   |   |
       |
       |
       |
       |
 =========""", """

   +---+
   |   |
   0   |
       |
       |
       |
 =========""", """

   +---+
   |   |
   0   |
   |   |
       |
       |
 =========""", """

   +---+
   |   |
   0   |
  /|   |
       |
       |
 =========""", """

   +---+
   |   |
   0   |
  /|\  |
       |
       |
 =========""", """

   +---+
   |   |
   0   |
  /|\  |
  /    |
       |
 =========""", """

   +---+
   |   |
   0   |
  /|\  |
  / \  |
       |
 ========="""]

words="""
python basic fortran cobol logo java hypertext
simula perl program input print variables text labels
code syntax random array lists algorithm boolean strings
fractal languages computer internet browser mouse keyboard
mainframe programmer electronic digital
""".split()

#######################################################################################

# Choose a random word from out list of possible words
def getRandomWord(wordList):
    return choice(wordList)

#######################################################################################

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):

    # Print the proper picture based on how many letters you've missed
    print(HANGMANPICS[len(missedLetters)])
    print()

    # Print the list of missed letters so far
    print("Missed letters: ", end = " ")
    for letter in missedLetters:
        print(letter, end = " ")
    print()

    blanks = "_" * len(secretWord)

    # Replace any nlanks with letters from the correct letter list
    for x in range(len(secretWord)):
        if secretWord[x] in correctLetters:
            blanks = blanks[:x] + secretWord[x] + blanks[x+1:]

    # Show the secret word with spaces between each letter
    for letter in blanks:
        print(letter, end = " ")
    print()
    print()
    
#######################################################################################
# Returns the letter the player entered.
# This makes sure the person only entered a single letter.

def getGuess(alreadyGuessed):
    while True:
        print("Guess a letter: ")
        guess = input()
        guess = guess.lower()
        
        if len(guess) != 1:
            print("Please enter only one letter!")
        elif guess in alreadyGuessed:
            print("Please enter a letter you haven't chosen yet!")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter only letters!")
        else:
            return guess
    
#######################################################################################
# This checks to see if the player wants to play again

def playAgain():
    print("Do you want to play again? (yes or no?)")
    return input().lower().startswith("y")
    
#######################################################################################

##########################
#MAIN PART OF THE PROGRAM
##########################

print("Welcome to Hangman!")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameIsOver = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Did you win? (AKA you got every letter in the word)
        foundAllLetters = True
        for x in range(len(secretWord)):
            if secretWord[x] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters == True:
            print("You win!")
            gameIsOver = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print("You lose!")
            print("The word was " + secretWord)
            gameIsOver = True

    if gameIsOver == True:
        if playAgain() == True:
            missedLetters = ""
            correctLetters = ""
            secretWord = getRandomWord(words)
            gameIsOver = False
        else:
            print("Thank you for playing!")
            break
