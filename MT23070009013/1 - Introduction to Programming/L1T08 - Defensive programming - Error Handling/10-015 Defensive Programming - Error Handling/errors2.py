# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# FIX-Runtime: Lion needs to be in quotes as it is a string, not an integer
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# FIX-Syntax: incomplete f string
# FIX-Logical: teeth and type are in the wrong positions for the statement
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

# FIX-Syntax: missing parentheses for print statement
print(full_spec)

