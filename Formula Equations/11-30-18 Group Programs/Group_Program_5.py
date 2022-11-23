# Group Program 5
# Enter a number.  Make a list of the prime factorization of the number.
# For example:  12 would make a list [2, 2, 3]	18 would make a list [2, 3, 3]

factorList = []

num = int(input("Enter a number: "))
factor = 2

while factor <= num:
    if num % factor == 0:
        factorList.append(factor)
        num = num / factor
        factor = 2
    else:
        factor = factor + 1

print(factorList)

    
