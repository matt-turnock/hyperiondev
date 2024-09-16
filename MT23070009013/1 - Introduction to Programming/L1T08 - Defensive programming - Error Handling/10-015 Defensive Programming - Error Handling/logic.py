# pseudo:
# brief: write a program that displays a logical error
#
# request user input in cm
# tell the user we are going to convert this into inches
# convert to mm by mistake to show a logical error in my code

cm = float(input("Please input a number in cm: "))

inches = cm * 10

print(f"Conversion of cm to inches: {inches}")