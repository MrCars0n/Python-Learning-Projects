# Program 4 - Nice Teacher Average

grades = []
lowest = 200
lowestSlot = 200
total = 0
for n in range(5):
    grades.append(int(input("Enter number " + str(n + 1) + ": ")))

for a in range(5):
    if grades[a] < lowest:
        lowest = grades[a]
        lowestSlot = a
        print(lowest)

print(grades)

grades.remove(grades[lowestSlot])

print(grades)

for b in range(4):
    total = total + grades[b]

average = total / 4

print("Average: " + str(average))
