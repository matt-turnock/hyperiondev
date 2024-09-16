# pseudo: 
# request user to input a sentence and save this to str_manip
# calculate the string length of str_manip and print this
# find the last letter of str_manip
# using this letter replace every occurrence with the @ symbol
# print the last three letters of str_manip backwards
# get the first three and last two characters of the string, and make a new word

str_manip = input("Please provide a string for manipulation: ")

str_length = len(str_manip)
print(f"The length of your string is: {str_length}")

str_final_letter = str_manip[str_length-1:str_length-2:-1]
print(f"The final letter of the string is: {str_final_letter}")

# This is case sensitive, so 'o' does not equal 'O'
# To include this you would want to lower() this sentence first
# but this is not mentioned in the brief so has been left out
print(f"I have replaced every occurrence of the last letter with the @ symbol: {str_manip.replace(str_final_letter, '@')}")

print(f"The last three letters of the string in reverse are: {str_manip[str_length-1:str_length-4:-1]}")

first_three = str_manip[:3]
last_two = str_manip[str_length-2:]
print(f"Combining the first three letters and the last two letters of the string our new word is: {first_three + last_two}")