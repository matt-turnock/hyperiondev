# pseudo:
# define a function that takes in a list of ints, and a single int as args
# add the sum of the list ints, up to the index value of the single int

# [1, 2, 3, 4, 5]
# index = 3

# adding_up(3) = 4 + adding_up(2)
# adding_up(2) = 3 + adding_up(1)
# adding_up(1) = 2 + adding_up(0)
# adding_up(0) = 1
# adding_up(0) = 1
# adding_up(1) = 2 + 1 = 3
# adding_up(2) = 3 + 3 = 6
# adding_up(3) = 4 + 6 = 10

def adding_up(my_list, int_index):
    # Check if my base clause has been his and if so, return the last value in my list.
    if int_index == 0:
        return my_list[int_index]
    else: # Otherwise i want to add the current element of my list to the next in line in my list.
        return my_list[int_index] + adding_up(my_list, int_index - 1)
   
# Print out the outcome from my recursive function
print(adding_up([7, 4, 12, 9, 0], 3))