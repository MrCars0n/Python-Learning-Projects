# Carson Kramer
# Triangle Type
# 10/3/18
# Period 9

a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))

if a<=0 or b<=0 or c<=0:
    print("Not a Triangle")
elif a==b and b==c:
    print("Equalateral")
elif a==b or b==c or a==c:
    print("Isosceles")
else:
    print("Scalene")
