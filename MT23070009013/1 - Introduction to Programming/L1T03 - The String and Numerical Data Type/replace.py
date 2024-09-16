# pseudo:
# define string variable with the contents The!quick!brown!fox!jumps!over!the!lazy!dog
# remove all ! from the string above using the replace() function and replace with a space
# print the string without !
# remove all ! and uppercase the string using the upper function()
# print the string without ! and uppercase all parts of the string
# print the sentence backwards using slicing

my_string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

print(my_string.replace('!', ' '))
print(my_string.replace('!', ' ').upper())
print(my_string[::-1])