# Carson Kramer
# Grade
# 10/4/18
# Period 9

name = input("Enter your name: ")
grade = float(input("Enter the Number of Programs you finished: "))

if grade == 4:
    print(name, "got a 40/40.\nThis is a 100%.")
elif grade == 3:
    print(name, "got a 38/40.\nThis is a 95%.")
elif grade == 2:
    print(name, "got a 36/40.\nThis is a 190%.")
elif grade == 1:
    print(name, "got a 32/40.\nThis is a 80%.")
elif grade == 0:
    print(name, "got a 26/40.\nThis is a 60%.")
else:
    print("This is impossible")
