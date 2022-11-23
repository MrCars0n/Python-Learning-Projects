# Carson Kramer
# Strings and Substrings
# 12/12/18
# Period 9

# String - any data which is alphanumeric - characters, words, sentences, symbols, and potentially numbers

# Declare a string - set it equal to a "string literal" in quotes
str1 = "Hello world!"

# Find the length of the string
print(len(str1))

# Like lists, strings begin with character 0
# So, str1[0] would pring "H"

for n in range(len(str1)):
    print(str1[n])

# Find the location of a character or substring in a string
print(str1.index("w"))      # 6 (w is in location 6)
print(str1.index("o"))      # 4 - only gives you the first match

# If you try to find the index of something not in the string it will give you a crashing error

print(str1.index("ell"))    # 1 - location of the e in Hello

# Count the number of characters/substrings in a string

print(str1.count("o"))

# Multiply a string by a number to copy that many times
print("Hello" * 5)

password = "eagles123"
print("*" * len(password))

# Concatenate - add two or more strings together (use +)
word = "exciting"
ex = "!!!!!!!!!!\t SO EXCITING"

print(word.upper() + ex.lower())

# Slicing - get part of a word
# To get multiple characters from a string use [# : #] where the first number is INCLUSIVE (includes it) and the second number is EXCLUSIVE (it doesn't)

print(word[2:6]) # citi

print(word[2:6:2]) # ct (the third 2 skips every 2 letters

print(word[::-1]) # print the word in reverse

p = "racecar"

if p == p[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
