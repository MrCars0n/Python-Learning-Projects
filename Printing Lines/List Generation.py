# Carson Kramer
# List Generation
# 11/6/18
# Period 9

# Generate a list of 24 random values (0-100)
# Find the total, average, etc...

from random import *

# Start with an empty list of grades
grades = []

for n in range(24):
    grades.append(int(random() * 101))

print(grades)

print("The total of the values is", sum(grades))
print("The average of the values is", round(sum(grades) / len(grades), 2), "%")

# Find the largest and smallest numbers in the list
print("The smallest value is", min(grades))
print("The largest value is", max(grades))
