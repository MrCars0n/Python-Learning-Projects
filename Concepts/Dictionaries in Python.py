# Carson Kramer
# Dictionaries in Python
# 11/28/18
# Period 9

# Dictionaries are list lists, except instead of single value entreis each entry is a KEY paired with a VALUE.
# In a real-world dictionary, when you look up a word, you find the information about that word (definition, part of speech, etc.)


favoriteFoodList = {
    "Rachel" : "Waffles",
    "Arber" : "Pizza",
    "Sidharth" : "Chicken",
    "Logan" : "Tacos",
    "Bendeguz" : "Carbonara",
    "Eli" : "Tacos"
}

# Loop through the dictionary and print the items

for name in favoriteFoodList.keys():
    print(name + "loves to eat " + favoriteFoodList[name])

# We can not search in reverse though because more than one person may have the same favorite food

#for food in favoriteFoodList.values():
#    print(food + " is loved by " + favoriteFoodList[food])

# "Does anyone like pizza?"
if "Pizza" in favoriteFoodList.values():
    print("I see somebody likes pizza!")
else:
    print("I can't believe nobody likes pizza!")
