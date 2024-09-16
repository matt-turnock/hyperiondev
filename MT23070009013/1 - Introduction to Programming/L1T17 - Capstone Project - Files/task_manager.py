import datetime


def fetch_credentials(switch):
    # Define our empty dictionary, or list for reading in
    # all users depending on our function arg.
    # Sometimes we only to know if the user exists, others
    # we want to validate their password also
    if switch == 1:
        credentials = {}
    elif switch == 0:
        credentials = []

    # Attempt to open our file that contains user credentials
    try:
        with open('./user.txt', 'r') as f:
            for line in f:
                # Strip the \n from the end end of the line
                line = line.strip('\n')
                # We know our delimeter is `, ` so we split
                # on this, and stick this into a list
                single_cred = line.split(', ')

                if switch == 1:  # If we are returning user:password style data
                    # Using the two elements of the list we can
                    # assign the kvp to the dictionary
                    credentials[single_cred[0]] = single_cred[1]
                elif switch == 0:  # Otherwise return a list of usernames
                    credentials.append(single_cred[0])

    except FileNotFoundError as e:  # Capture my no file error
        print("Unable to locate the credential file ./user.txt, "
              "please check you are in the right directory.")
        print(e)
        # Force application exit if file not found
        print("Exiting application.")
        exit()

    # Return our dictionary or list full of names
    return credentials


def write_credentials(user, password):
    try:  # Try to open my users files for appending
        with open('./user.txt', 'a') as f:
            # Write user and password in a `user, password` format
            f.write(f"\n{user}, {password}")
            print(f"New user {user} written to credentials file.")
    except FileNotFoundError as e:  # Cant find my rile, so error
        print("Unable to locate the credential file ./user.txt, "
              "please check you are in the right directory.")
        print(e)
        # Force exit of application
        print("Exiting application.")
        exit()


def write_task(user, title, desc, start, end, complete):
    try:  # Try to open my tasks file for appending
        with open('./tasks.txt', 'a') as f:
            # Write tasks in the format -
            # user, title, description, start, end, complete
            f.write(f"\n{user}, {title}, {desc}, {start}, {end}, {complete}")
            print("New task has been saved to our file.")
    except FileNotFoundError as e:  # Otherwise error if file not found
        print("Unable to locate the tasks file ./tasks.txt, "
              "please check you are in the right directory.")
        print(e)
        # Force exit of application
        print("Exiting application.")
        exit()


def get_tasks(switch):
    try:
        with open('./tasks.txt', 'r') as f:
            # Switch so that i can just define reading this file once when reading
            # 0 is for returning the amount of tasks, and 1 is for displaying
            # tasks for the various options.
            if switch == 0:
                return len(f.readlines())
            elif switch == 1:
                for line in f:
                    # Strip the \n from the end for when there are
                    # more than 1 username and password in our user.txt
                    line = line.strip('\n')
                    # We know our delimeter is `, ` so we split on this,
                    # and stick this into a list
                    task_fields = line.split(', ')

                    # Check to see if our menu option was all, or mine
                    # when viewing tasks.
                    if menu == 'va':  # View all
                        # Assign the parts of our list into their own variables
                        # This makes reading the next function easier
                        t_title = task_fields[1]
                        t_user = task_fields[0]
                        t_assigned_date = task_fields[3]
                        t_due_date = task_fields[4]
                        t_complete = task_fields[5]
                        t_desc = task_fields[2]

                        # Call our display tasks function to print our info
                        # in a nice format
                        display_tasks(t_user,
                                      t_title,
                                      t_desc,
                                      t_assigned_date,
                                      t_due_date,
                                      t_complete)
                    elif menu == 'vm':  # View mine
                        if task_fields[0] == u_name:
                            # Assign the parts of our list into
                            # their own variables, this makes
                            # reading the next function easier
                            t_title = task_fields[1]
                            t_user = task_fields[0]
                            t_assigned_date = task_fields[3]
                            t_due_date = task_fields[4]
                            t_complete = task_fields[5]
                            t_desc = task_fields[2]

                            # Call our display tasks function to print our info
                            # in a nice format
                            display_tasks(t_user,
                                          t_title,
                                          t_desc,
                                          t_assigned_date,
                                          t_due_date,
                                          t_complete)
    except FileNotFoundError as e:
        print("Unable to locate the tasks file ./tasks.txt, "
              "please check you are in the right directory.")
        print(e)
        # Force exit of application
        print("Exiting application.")
        exit()


def display_tasks(t_user, t_title, t_desc, t_assigned_date, t_due_date, t_complete):
    # Format my task information and print this out to screen
    print(f'''------------------------------------------------------------------------
Task:                 {t_title}
Assigned to:          {t_user}
Date Assigned:        {t_assigned_date}
Due date:             {t_due_date}
Task Complete?        {t_complete}
Task description:
 {t_desc}\n''')


# Assign the output from our fetch_credentials function to a global dict
credentials = fetch_credentials(1)

# Variable assignment to enable input validation
u_name = ""
u_pass = ""
authenticated = False
t_user = ""
t_title = ""
t_desc = ""
t_assigned_date = ""
t_due_date = ""
t_complete = ""

# End variable declarations


# Start the authentication process
# Wasnt sure how to resolve this == False PEP8 error
# so i have left this as it is
while authenticated == False:
    # Check if the username entered
    # matches a valid key in our dict
    while u_name not in credentials.keys():
        u_name = input("Please enter a valid username: ")

    # Check that our password matches the value, of the specific username key
    while not u_pass == credentials[u_name]:
        u_pass = input(f"Please input a valid password for user {u_name}: ")
        # Set authenticated to be true to exit while loop for authentication
        authenticated = True

while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    if u_name == 'admin':
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics
e - exit
: ''').lower()
    else:
        menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r' and u_name == 'admin':
        # Declare some variables to be used for this block only
        n_name = ""
        n_pass = ""
        n_validate = ""

        # Loop and try block to validate a user has been entered
        # and that they dont try to enter a blank username
        while n_name == "":
            try:
                n_name = input("Please input the new users username: ")
            except ValueError as e:
                print("Username can not be blank.")
                print(e)

        # Loop to loop until both new password entries match
        while True:
            # Loop to check password isnt empty, this is bad security :P
            while n_pass == "":
                try:
                    n_pass = input("Please input your password: ")
                except ValueError as e:
                    print("Password can not be blank.")
                    print(e)

            # If block to check for the second password, if it matches or not
            # No need to check if empty here, because the first cant be empty
            # and this must match the first
            n_validate = input("Please confirm your password: ")
            if n_pass == n_validate:
                write_credentials(n_name, n_pass)
                break
            else:
                print("Passwords do not match, please re-enter.")

    elif menu == 'a':
        # Use fetch_credentials with 0 flag to just return
        # the user names, without passwords
        users = fetch_credentials(0)

        # Loop while our assignee for the task doesnt equal a registered user
        while t_user not in users:
            t_user = input("Please input the user assignee: ")
            if t_user not in users:
                print("Please provide an existing user")

        # Request a non blank title of the task
        while t_title == "":
            t_title = input("Please input the title for this task: ")

        # Request a non blank description of the task
        while t_desc == "":
            t_desc = input("Please input the description for this task: ")

        # Loop while our due date isnt blank, or doesnt match a date format
        while (t_due_date == "" and
                not isinstance(t_due_date, datetime.datetime)):
            try:  # Try to format the date entered to a `10 Dec 2023` format
                t_due_date = datetime.datetime.strptime(input("Please input the due date for this task: "), "%d %b %Y")
                t_due_date = t_due_date.strftime("%d %b %Y")
            except ValueError as e:
                print("Please input a valid date")
                print(e)

        # Call our write task function and pass in the variables requested
        write_task(t_user,
                   t_title,
                   t_desc,
                   datetime.datetime.now().strftime("%d %b %Y"),
                   t_due_date,
                   "No")

    elif menu == 'va':
        get_tasks(1)

    elif menu == 'vm':
        get_tasks(1)

    elif menu == 'ds':
        # Get the length of credentials to show total numbers of users
        print(f"Total number of users: {len(credentials)}")
        # Return only the number of tasks from get_tasks by providing the switch arg 0
        print(f"Total number of tasks: {get_tasks(0)}")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
