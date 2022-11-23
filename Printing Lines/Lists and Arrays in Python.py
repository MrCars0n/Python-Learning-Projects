# Carson Kramer
# Lists and Arrays in Python
# 10/30/18
# Period 9

# A list is a collection of items with an order
# In Python, the square brackets [] indicate a list
# Items in lists are separated by commas

# One variable = one item

villain = "Magneto"

# A list can hold multiple items
# (The backslash lets you continue a list on the next line)
xmen = ["Cyclops", "Wolverine", "Beast", "Storm",\
        "Iceman", "Colossus"]

# To print the entire list...
print(xmen)

# To print one item from the list
print(xmen[0])

# To replace an item in the list, treat it like a variable
xmen[4] = "Jean Grey"

# To add an item to the end of the list, use append()
xmen.append("Deadpool")

# To insert an item into the list at a certain position
xmen.insert(1, "Professor X")

# To remove something by the position
print(xmen)
del xmen[0]
print(xmen)

# To remove something by name
xmen.remove("Beast")
print(xmen)
