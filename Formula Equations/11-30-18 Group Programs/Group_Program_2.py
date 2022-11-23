# Group Program 2
# Enter a number.
# The computer will print YES or NO if it contains a zero anywhere in the number.
# (4096 would say YES.  4731 would say NO.)

num = int(input("Enter a number: "))

while num > 0:
    digit = num % 10
    if digit == 0:
        print("YES!")
        exit()
    else:
        num = int(num / 10)

print("NO!")
    
