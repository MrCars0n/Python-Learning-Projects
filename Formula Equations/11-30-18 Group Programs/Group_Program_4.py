# Group Program 4
# Enter five unique numbers (between 1 and 10) into a list (you type, not random)
# Find the “Nice Teacher Average”
# i.e. the average when you drop the lowest score

scoreList = []

for n in range(5):
    num = int(input("Enter your score: "))
    scoreList.append(num)

print(scoreList)
average = (sum(scoreList) - min(scoreList)) / 4
print(average)


