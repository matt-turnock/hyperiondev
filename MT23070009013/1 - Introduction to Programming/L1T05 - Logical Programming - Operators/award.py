# pseudo:
# request in three times, for swimming, cycling and running
# calculate and display the total time taken
# calculate the award based on the time given, vs the qualifying time of 100 minutes
# the awards should be as follows
# within qualifying time, provincial colours
# within 5 minutes, provincial half colours
# within 10 minutes, provincial scroll
# more than 10 minutes, no award.

# request inputs
swimming_time = int(input("Please input the time for the swimming event: "))
cycling_time = int(input("Please input the time for the cycling event: "))
running_time = int(input("Please input the time for the running event: "))

# calculate the total time and print this
total_time = swimming_time + cycling_time + running_time
print(f"The total time taken for all events combined was: {total_time} minutes.")

# if statement logic to determine the reward based on a total time of 100 minutes
if total_time < 100: # finish within 100 minutes
    print("Congratulations! You finished within the alloted time of 100 minutes. You have been awarded Provincial Colours.")
elif total_time < 105: # finish within +5 of 100 minutes
    print("Congratulations! You have finished within 5 minutes of the alloted 100 minutes. You have been awarded Provincial Half Colours.")
elif total_time < 110: # finish within +10 of 100 minutes
    print("Congratulations! You have finished within 10 minutes of the alloted 100 minutes. You have been awarded a Provincial Scroll.")
else: # otherwise... but finish over +10 of 100 minutes (So +11)
    print("You finished more than 10 minutes over the alloted 100 minutes. Better luck next time.")