# pseudo:
# request a string from a user
# iterate over the length of the string and for each element of said string
# make even elements uppercase
# make odd elements lowercase
# forcing an output of the original string to print "HeLlO WoRlD" (As an example)
#
# starting with the same string provided, make each even WORD lowercase
# make each odd WORD uppercase
# display i AM learning TO code (example)

originalString = input("Please input a string of any length: ")
newOString = ""
splitString = []
newLString = []

# Make use of the enumerate() function to track the element that i 
# am at so that i can check its position in the string

# I am also forming the parameters of my for iterations based on the length of the string

for index, l in enumerate(originalString[0:len(originalString)]):
    if index % 2 == 0: # Even, 0, 2, 4, etc
        newOString += l.upper()
    else: # Otherwise, Odd, 1, 3, 5, etc
        newOString += l.lower()
        
print(f"CaMeLcAsE letters new string: {newOString}")

# Split my original string by " " - we havent covered lists, but the string.split() function
# automatically puts this into a list so i feel like its ok to use them here.
#
# The split delimeter is whitespace, so i can leave this blank, or define it.

splitString = originalString.split(" ")

for index, w in enumerate(splitString[0:len(splitString)]):
    if index % 2 == 0:
        newLString.append(w.lower())
    else:
        newLString.append(w.upper())
        
# I would have liked to have done it as i did it above
# without using append, and join.  As it doesnt allow me to
# nicely display it without then concating two strings below.
# But the brief said join and split are your friends here
# so i felt obliged to use them at least once.
print("CaMeLcAsE words new string: " + " ".join(newLString))