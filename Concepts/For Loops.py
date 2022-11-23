# Carson Kramer
# For Loops
# 11/1/18
# Period 9

# Used for definite sized loops
# (We know both the starting and ending values)

# range(#) - loop goes from 0 to (#-1)  (range(10) is 0 to 9)
for n in range(10):
    print(n, end = " ")

print()

y = 1
for n in range(y):
    y = y + 1
    print(n)

print()

for n in range(1,10):
    print(n, end = " ")

print()

# The reason range is "weird" is due to lists and length
names = ["Carson", "Logan", "Keely", "Essam"]

# len(names) is 4, but we want 0 to 3 - always off by one
for n in range(len(names)):
    print(names[n])

# range(#, #, #) - the third number is the "step"
for n in range(0, 101, 2):
    print(n, end = " ")

for n in range(10, 1, -1):
    print(n, end = " ")
