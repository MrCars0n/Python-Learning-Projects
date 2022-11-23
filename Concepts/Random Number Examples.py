# Carson Kramer
# Random Number Examples
# 9/19/18
# Period 9

from random import *

# Roll two six sided die and find the total
for n in range(10):
    die1 = int(random() * 6) + 1
    die2 = int(random() * 6) + 1
    total = die1 + die2
    print(die1, "\t", die2, "\t", total)

# Make a random number from 1000-9999 (random 4 digit number)
num = int(random() * 9000) + 1000  # (9999 - 1000) + 1

# Pick a random item from a list
names = ["Chuck", "Barbra", "Obama", "Won", "Dwight", "Isaac", "Harry"]
name = choice(names)
print(name, "is a name")
