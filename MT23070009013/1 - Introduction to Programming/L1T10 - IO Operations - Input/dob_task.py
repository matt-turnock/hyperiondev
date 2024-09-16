# pseudo:
# read the data from the file provided (DOB.txt)
# print out the information under two sections, name, and birthdate

names = []
dobs = []
sort = []

# Make sure when running this we are running this from the same directory as dob_task.py
# else it gets ran in what ever diretory you are in and wont find the DOB.txt file.
with open('DOB.txt', 'r') as f:
    for index, line in enumerate(f):
        # Strip tailing \n to conform with brief output
        line = line.strip('\n')
        # Temporarily store each lines elements
        sort = line.split(" ")
        # Append the firstname and surname into a single element of names
        names.append(sort[0] + " " + sort[1])
        # Append the entire date of birth into a single element of dobs
        dobs.append(sort[2] + " " + sort[3] + " " + sort[4])
        
# iterate over names, printing each fullname
print("Name")
for name in names:
    print(name)
    
# iterate over dobs, printing each dob
print("\nBirthdate")
for date in dobs:
    print(date)