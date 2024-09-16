# pseudo:
# request the user to input their fullname
# validate the users input against the following criteria, with the relevant error message
# if they entered nothing - "Please enter your full name."
# less than 4 characters - "Please make sure that you have entered your name and surname."
# more than 25 characters - "Please make sure that you have only entered your full name."
# validated - "Thank you for entering your name."

# Notes on the brief, if i was asking for a full name i would normally take in both as separate
# variables.  The brief states to `Ask the user to input their full name.` which i have taken
# to be into one variable due to the wording of the brief.

full_name = input("Please enter your full name: ")

# Because we are checking its length many times, just more efficient to evaluate len() once
length = len(full_name)

print("Validating user input.")
if (length == 0):
    print("Please enter your full name.")
elif (length < 4):
    print("Please make sure that you have entered your name and surname.")
elif (length > 25):
    print("Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")