# Carson Kramer
# 100m Dash
# 10/2/18
# Period 9

from math import *

firstName = input("Input the 1st Runner's Name: ")
firstTime = float(input("Input the 1st Runner's 100m Dash time: "))

secondName = input("\nInput the 2nd Runner's Name: ")
secondTime = float(input("Input the 2nd Runner's 100m Dash time: "))

thirdName = input("\nInput the 3rd Runner's Name: ")
thirdTime = float(input("Input the 3rd Runner's 100m Dash time: "))
print()
if firstTime > secondTime and firstTime > thirdTime:
    print(firstName, "won the race with a time of", firstTime, "seconds.")
    if secondTime > thirdTime:
        print(secondName, "got second with a time of", secondTime, "seconds.")
        print(thirdName, "came in third with a time of", thirdTime, "seconds.")
    if thirdTime > secondTime:
        print(thirdName, "got second with a time of", thirdTime, "seconds.")
        print(secondName, "came in third with a time of", secondTime, "seconds.")
        
elif secondTime > firstTime and secondTime > thirdTime:
    print(secondName, "won the race with a time of", secondTime, "seconds.")
    if firstTime > thirdTime:
        print(firstName, "got second with a time of", firstTime, "seconds.")
        print(thirdName, "came in third with a time of", thirdTime, "seconds.")
    if thirdTime > firstTime:
        print(thirdName, "got second with a time of", thirdTime, "seconds.")
        print(firstName, "came in third with a time of", firstTime, "seconds.")
        
elif thirdTime > secondTime and thirdTime > firstTime:
    print(thirdName, "won the race with a time of", thirdTime, "seconds.")
    if firstTime > secondTime:
        print(firstName, "got second with a time of", firstTime, "seconds.")
        print(secondName, "came in third with a time of", secondTime, "seconds.")
    if secondTime > firstTime:
        print(secondName, "got second with a time of", secondTime, "seconds.")
        print(firstName, "came in third with a time of", firstTime, "seconds.")
