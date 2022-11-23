# Carson Kramer
# Smingmart
# 9/28/18
# Period 9

from math import *

print("Welcome to the grand opening of Smingmart! We are having a sale! \nWe are giving 10 percent off purchases of $10 or lower, and 20 percent off purchases of greater than $10!\n")
price = float(input("Enter the price of your purchases from Smingmart: $"))

if price >= 10:
    discount = price * 0.2
    totalNoTax = price - discount
    tax = totalNoTax * 0.06
    totalTax = totalNoTax + tax
    print("You got 20% off!")
    print("Price after discount: $", "%.2F" % totalNoTax)
    print("Sales tax: $", "%.2F" % tax)
    print("Final price: $", "%.2F" % totalTax)
elif price <= 10:
    discount = price * 0.1
    totalNoTax = price - discount
    tax = totalNoTax * 0.06
    totalTax = totalNoTax + tax
    print("You got 10% off!")
    print("Price after discount: $", "%.2F" % totalNoTax)
    print("Sales tax: $", "%.2F" % tax)
    print("Final price: $", "%.2F" % totalTax)
