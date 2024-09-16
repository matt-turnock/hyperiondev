# pseudo:
# request the user to input how many students are registering
# iterate over a for loop to the number of times as there are students
# within this loop, for each iteration as the user to enter the student ID number
# write each of the ID numbers to a text file called reg_form.txt
# on the same line as the student ID, include a dotted line for signing purposes

num_students = int(input("Please enter how many students are to be registered: "))
student_id = 0

# only need to open this file once, so do this first
with open('reg_form.txt', 'w') as f: # append to file
    # using enumerate again because its nice to display which student you are adding in the user input message
    for index, s in enumerate(range(num_students)):
        student_id = input(f"Please input the ID for student number {index + 1}: ")
        f.write(student_id + ".................\n")