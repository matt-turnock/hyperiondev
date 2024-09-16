# pseudo:
# using an if-else, and only 1 for(brief doesnt say explicitly for) loop generate the following star pattern
#
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
#

# going to just use slicing here to manipulate the output of a string variable
stars = "*****"

# this is just so i can slice backwards
count = 0

# interate 9 times, 1 -> 9
for x in range(1, 10):
    # if our iteration is less than or equal to 5 we want to slice incrementally as we iterate x up
    if x <= 5:
        count += 1
        print(f"{stars[0:count]}")
    # if our iteration is greater than 5 we want to slice decrementally as we iterate x up
    elif x > 5:
        count -= 1
        print(f"{stars[0:count]}")