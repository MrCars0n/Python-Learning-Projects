# Carson Kramer
# For Loops Warm Ups
# 11/6/18
# Period 9

# Create Six separate loops which print the following sequences (left to right)
# 1) 1 2 3 4 5 6 7 8 9 10 11 
# 2) 10 9 8 7 6 5 4 3 2 1 0 
# 3) 2 4 6 8 10 12 14 16 18 20 
# 4) 0 5 10 15 20 25 30 35 40 45 50 
# 5) 77 66 55 44 33 22 11 0
# 6) A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

for a in range(1,11):
    a = a + 1
    print(a, end = " ")
    
print()

for b in range(10, -1, -1):
    print(b, end = " ")
    
print()

for c in range(2, 21, 2):
    print(c, end = " ")
    
print()

for d in range(0, 51, 5):
    print(d, end = " ")

print()

for e in range(77, -1, -11):
    print(e, end = " ")

print()

# In ASCII, "A" starts at code 65
for f in range(65, 65+26):
    print(chr(f), end = " ")

print()

# Print a word search grid

from random import *

for n in range(20):
    for n in range(20):
        letter = chr(int(random() * 26) + 65)
        print(letter, end = "")
    print()
