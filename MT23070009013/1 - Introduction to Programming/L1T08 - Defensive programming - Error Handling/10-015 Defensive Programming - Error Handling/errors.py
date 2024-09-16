# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# FIX-Syntax: Missing parentheses for print statement
print("Welcome to the error program")

# FIX-Syntax: Removed indentation from lines 6 -> 15
print("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
# FIX-Runtime: made the age_Str, a string of numbers instead of having letters also
age_Str = "24"
age = int(age_Str)

# FIX-Runtime: you cannot add a number to a string in print, so i have used f string to have this displayed as a string
print(f"I'm {age} years old.")

# Variables declaring additional years and printing the total years of age
years_from_now = 3
total_years = age + years_from_now

# FIX-Runtime: you cannot add a number to a string in print, so i have used f string to have this displayed as a string
print(f"The total number of years: {total_years}")

# Variable to calculate the total amount of months from the total amount of years and printing the result
# FIX-Runtime: Changed total to be total_years as it was a mispelling
# FIX-Logical: Reworked the calculation as it hasnt taken into account for the +6 months that are required.
total_months = (total_years * 12) + 6

# FIX-Runtime: you cannot add a number to a string in print, so i have used f string to have this displayed as a string
print(f"In 3 years and 6 months, I'll be {total_months} months old")

#HINT, 330 months is the correct answer

