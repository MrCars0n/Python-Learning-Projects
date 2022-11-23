# Carson Kramer
# Leap Year
# 10/2/18
# Period 9

while True:
    year = float(input("Input a Year: "))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Your year is a Leap Year!")
    else:
        print("Your year is not a Leap Year!")
