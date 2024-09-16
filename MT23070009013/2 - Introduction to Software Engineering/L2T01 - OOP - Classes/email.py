# Define Email class with class variable has been read, then
# include some object level variable in the constructor
class Email():
    # Define class level variable for each new email created
    has_been_read = False

    # Constructor for Email object class
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Mark_as_read function inside class object to change the
    # class level varaible read from False to True
    def mark_as_read(self):
        self.has_been_read = True


# Assume classes should be defined before functions so define this
# function to populate our email list with some data
def populate_inbox():
    # Just creating 3 random emails with arbitrary data at this point
    # the brief is designed to show use of the Class, not what data
    # i can create on the fly.
    for num in range(0, 3):
        inbox.append(Email(f"matt{num}@gmail.com",
                           f"To do list item {num}",
                           f"We need to do things for task {num}"))


# Function to list my emails, as viewing unread and reading
# both requires the user to be able to view these.
# Pass in true or false flag to switch if its to show all
# or to only show unread
def list_emails(display_read):
    print("\n")  # Print newline for formatting purposes.
    for num, email in enumerate(inbox):
        if display_read is True:  # If we want to display read emails
            print(f"{num} {email.subject_line}")
        elif email.has_been_read is False:  # Otherwise display only unread
            print(f"{num} {email.subject_line}")


# Function to read emails regardless of status
# but marks unread emails as read
def read_email(index):
    # Just want to store this as a variable to make it nicer to reference later
    current_email = inbox[index]
    # Print nicely for the user, otherwise they may stop using our awesome system
    print(f'''\nReading Email {index}\n
          Sender:       {current_email.email_address}
          Subject:      {current_email.subject_line}
          Message body: {current_email.email_content}
          ''')
    # The next line isnt really required but, its good to check values.
    # Could assume its unread, but setting it to read if its already read
    # wont error, but again i feel like its good to check.
    if current_email.has_been_read is False:
        current_email.mark_as_read()
        print(f"Marking email {index} as read.")


# Define empty inbox as a list
inbox = []

# Populate our empty inbox using the define function
populate_inbox()

# Iterate our menu until we select option 3, invalid options
# are met with our final else print block
while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    if user_choice == 1:
        # Call our function with true, so that it display ALL emails regardless
        # of if they are read or unread.
        list_emails(True)
        email_choice = int(input('''\nPlease select which email you would like to read from the list:'''))
        # Check to see if our choice was a valid choice
        if email_choice <= len(inbox)-1:
            # Call our read_email function with our desired email index
            read_email(email_choice)
        else:
            # Tell them it wasnt a valid choice
            print(f"Email {email_choice} doesnt exist, there are only {len(inbox)} emails.")

    elif user_choice == 2:
        # List emails with false flag, to only show unread emails
        list_emails(False)

    elif user_choice == 3:
        # Cleanly exit out program
        exit()

    else:
        # Tell the user they didnt input a valid menu option
        print("Oops - incorrect input.")
