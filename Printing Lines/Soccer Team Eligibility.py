# Carson Kramer
# Soccer Name Eligibility
# 9/28/18
# Period 9

print("Let's find out if your eligible for the 9 to 12 year-old girls soccer team.")
age = float(input("Enter your age: "))
gender = input("Enter your gender (\"M\" for Male and \"F\" for Female): ")

if age <= 12 and age >= 9 and gender == "F":
    print("\nGood news! You are eligible to play for our team!")
else:
    print("\nI'm sorry, you are not eligible to play for our team.")
