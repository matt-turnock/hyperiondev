# pseudo:
# create a function that returns the largest numbers in a list of integers takes as arg

# I will admit i wanted to know what i could include in my return statement on line 10.
# Turns out i can return based off of a conditional statement which is REALLY nice.

def largest_number(my_list, list_len):
    # My base clause, in that if my list element to check is 0, return that element
    if list_len == 0:
        return my_list[list_len]
    else: #Otherwise, we return what ever element we are on if the current element value is greater than the next element to the left.
        return my_list[list_len] if my_list[list_len] > largest_number(my_list, list_len - 1) else largest_number(my_list, list_len - 1)
    
# Define my list
og_list = [1, 2, 3, 70, 100, 5, 0]

# Print and begin recursion passing in my list, and the value for the highest element in said list
print(largest_number(og_list, len(og_list) - 1))