# Carson Kramer
# Dice Roll Simulator
# 9/27/18
# Period 9


from random import *

# Variables start at 0 only if you tell them to!
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
sevens = 0
eights = 0
nines = 0
tens = 0
elevens = 0
twelves = 0

# Roll the two 6 sided die 1,000,000
for n in range(1000000):
    d1 = int(random() * 6) + 1
    d2 = int(random() * 6) + 1
    total = d1 + d2

    if total==2:
        twos = twos + 1
    elif total==3:
        threes = threes + 1
    elif total==4:
        fours = fours + 1
    elif total==5:
        fives = fives + 1
    elif total==6:
        sixes = sixes + 1
    elif total==7:
        sevens = sevens + 1
    elif total==8:
        eights = eights + 1
    elif total==9:
        nines = nines + 1
    elif total==10:
        tens = tens + 1
    elif total==11:
        elevens = elevens + 1
    elif total==12:
        twelves = twelves + 1

print("The number of two-dice rolls totalling two out of 1,000,000 roles were", twos, ".")
print("The number of two-dice rolls totalling three out of 1,000,000 roles were", threes, ".")
print("The number of two-dice rolls totalling four out of 1,000,000 roles were", fours, ".")
print("The number of two-dice rolls totalling five out of 1,000,000 roles were", fives, ".")
print("The number of two-dice rolls totalling six out of 1,000,000 roles were", sixes, ".")
print("The number of two-dice rolls totalling seven out of 1,000,000 roles were", sevens, ".")
print("The number of two-dice rolls totalling eight out of 1,000,000 roles were", eights, ".")
print("The number of two-dice rolls totalling nine out of 1,000,000 roles were", nines, ".")
print("The number of two-dice rolls totalling ten out of 1,000,000 roles were", tens, ".")
print("The number of two-dice rolls totalling eleven out of 1,000,000 roles were", elevens, ".")
print("The number of two-dice rolls totalling twelve out of 1,000,000 roles were", twelves, ".")
