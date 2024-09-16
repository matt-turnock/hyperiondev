# pseudo:
# create a list called menu which contains food items
# create a dictionary called stock which contains the values for each item in our menu list
# create another dictionary called price which contains the prices for items on the menu
# calculate the total_stock worth of the cafe
# print out this calculation

# I want to make this a bit more, random and fluid to show how you can populate dicts and lists
# using import random to set the stock values

import random

total = 0

# This is where we set what items we have, and their prices
price_dict = {'apple': 0.20, 'banana': 0.50, 'toastie': 2.99, 'muffin': 2.50}

# Initialise dict, then generate its stock values based off of what keys are inside price_dict
# aware that i didnt need to do this but thought it would be fun.
# Using 0,9 here, as something could technically be out of stock but still on the menu
stock_dict = {}
for i in price_dict.keys():
    stock_dict[i] = random.randint(0,9)

# Simply just populate my menu with my price dict keys, as if one changes so should the other regardless of stock values
menu_list = price_dict.keys()

# A simple value * value from two dicts based on the key matching
for i in menu_list:
    total += stock_dict[i] * price_dict[i]

# For the sake of my random stock values, print them out so you can do the math :P
print(f"Our stock consists of: {stock_dict}")
print(f"Out prices are as follows: {price_dict}")

print(f"Total stock value: £{total}")