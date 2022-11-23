# Program 2 - Contains 0

number = int(input("Enter a number: "))
zero = "false"

while zero != "true":
    if int(number) == 0:
        print("NO")
        break
    elif int(number) % 10 == 0:
        print("YES")
        break
    else:
        number = number * .1
