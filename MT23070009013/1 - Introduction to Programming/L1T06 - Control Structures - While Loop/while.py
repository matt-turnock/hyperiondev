# pseudo:
# request user input
# keep a running total and count of how many numbers have been entered
# keep requesting the input until the user inputs -1
# calculate the average of the numbers stored excluding the -1

# set num, as our request for numbers should be inside the while loop
# but we need to have num declared in order to use it with while.
num = 0
total = 0
count = 0

# simple iteration while the num isnt equal to our exit number of -1
while num != -1:
    num = int(input("Please input a number: "))
    
    # check to see what number they entered,
    # then add it to total and increase the count
    # as long as it isnt -1
    if num != -1:
        total = total + num
        count += 1    

# calculate average of the numbers added using total and count
average = total / count
print(f"The average is: {average}")