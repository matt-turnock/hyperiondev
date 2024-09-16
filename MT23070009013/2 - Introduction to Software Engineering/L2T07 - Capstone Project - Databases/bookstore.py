import sqlite3
import os


def initialise_db(db):
    '''Function to check for the existance of the DB, if it doesnt exist, create and populate.\n
       Args: database_file_location'''

    # Populate a list of tuples with book data.
    book_data = [(3001, "A Tale of Two Cities", "Charles Dickens", 30),
                 (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
                 (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
                 (3004, "The Lord of the Rings", "J.R.R Tolkien", 37),
                 (3005, "Alice in Wonderland", "Lewis Carroll", 12)]

    # Attempt to connect to the DB.
    try:
        db = sqlite3.connect(db)

        cursor = db.cursor()

        # Create our table.
        cursor.execute('''create table if not exists book(id integer primary key, title varchar(100), author varchar(50), qty integer)''')
        db.commit()

        # Input our data from our list of tulpes.
        cursor.executemany('''insert into book(id, title, author, qty) values (?, ?, ?, ?)''', book_data)
        db.commit()
    except ConnectionError as error:
        print(error)
    finally:
        db.close()


def obtain_books(db):
    '''Function to return a list of tulpes, containing all book data from the database.\n
       Args: database_file_location\n
       Returns a list of tulpes containing book data.'''

    # Define empty list for book data.
    books = []

    # Attempt to connect to the DB.
    try:
        db = sqlite3.connect(db)

        cursor = db.cursor()

        # Select all data from the database called book.
        cursor.execute('''select * from book''')

        # For every row returned in the cursor object
        # append the tulpe of data into an element of
        # the list books.
        for row in cursor:
            books.append(row)

        return books
    except ConnectionError as error:
        print(error)
    finally:
        db.close()


def enter_book(db):
    '''Function to enter book data into the database, existing or new.\n
       Args: database_file_location'''

    # Define empty title variable so that we can loop
    # until the user enters something other tan an empty
    # book title.
    title = ""

    # Loop while title is empty
    while title == "":
        title = input("Please input your book title: ")

        # Error message for empty book titles.
        if title == "":
            print("Book title cannot be empty.")

    # Check to see if any ' exists, as this breaks our sql later
    # If it exists we need to basically double quote here, so
    # ' becomes ''.
    if "'" in title:
        title.replace("'", "''")

    # Returns True or False to check if the book exists
    # in the databast already.
    exists = check_for_book(db, title)

    # Attempt to connect to the DB.
    try:
        db = sqlite3.connect(db)

        cursor = db.cursor()

        # Essentially, if True.
        if exists:
            # Update the quantity of an existing book by +1.
            cursor.execute(f'''update book set qty = qty + 1 where title = "{title}"''')
            db.commit()
        else:
            # I want to continue the numbering system from the brief data
            # so i obtain the max id, so that i can increment it.
            cursor.execute('''select max(id) from book''')
            next_id = cursor.fetchone()
            next_id = next_id[0] + 1

            # Empty author variable to ensure that we dont have an empty
            # user input later.
            author = ""

            # Iterate over the input until this isnt empty.
            while author == "":
                author = input("Please input the book author: ")
                if author == "":
                    print("Author cannot be empty.")

            # Ask for an enter a quantity for this book.
            qty = ""
            while True:
                try:
                    qty = int(input("Please input the quantity of books: "))
                    if isinstance(qty, int):
                        break
                except Exception as error:
                    print(error)
                    print(f"Invalid entry: {qty}. Must be an integer value.")

            # Input our new book into the database.
            cursor.execute(f'''insert into book(id, title, author, qty) values ("{next_id}", "{title}", "{author}", {qty})''')
            db.commit()
    except ConnectionError as error:
        print(error)
    finally:
        db.close()


def check_for_book(db, book):
    '''Function to check the existance of a book in the database.\n
       Args: database_file_location\n
       Returns bool (True|False)'''

    # Attempt to connect to the DB.
    try:
        db = sqlite3.connect(db)

        cursor = db.cursor()

        # Select the count value of any title that matches our users
        # new title.
        cursor.execute(f'''select count(*) from book where title = "{book}"''')

        # I just want the only result, as count will only return one so
        # no need to loop over the cursor as if there are more than one
        # row available.
        count = cursor.fetchone()

        # Because it returns a tulpe we just check the first element
        # to see if the value is a 1, it shouldnt be anything else
        # as duplicate books should not exist.
        if count[0] > 0 and count[0] <= 1:
            # Returns True
            return True
        else:
            # Returns False
            return False
    except ConnectionError as error:
        print(error)
    finally:
        db.close()


def update_book(db):
    '''Function to update the quantity of books.
       Args: database_file_location'''

    # Obtain our book data in a list of tulpes.
    books = obtain_books(db)
    valid_ids = []
    # Print these books so that we know how to reference
    # the book to be updated.
    print("Printing book list.\n")
    for book in books:
        valid_ids.append(book[0])
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Author: {book[2]}")
        print(f"Quantity: {book[3]}\n")

    # Obtain the ID of the book to update.
    while True:
        try:
            id_to_update = int(input("Please input the ID of the book to update in the system: "))
            if isinstance(id_to_update, int):
                break
        except Exception as error:
            print(error)

        print("ID must be an integer value")

    if id_to_update in valid_ids:
        # Give the user a new menu to select what they want to update
        while True:
            choice = ""
            try:
                choice = int(input('''Please select what you would like to update:\n
1. Title
2. Author
3. Quantity\n
Choice: '''))
            except ValueError as error:
                print(error)
                print("Please input a valid integer.")

            query = ""
            if choice == 1:  # Update the title
                title = ""
                while title == "":
                    title = input("Please input your book title: ")

                    # Error message for empty book titles.
                    if title == "":
                        print("Book title cannot be empty.")

                if "'" in title:
                    title.replace("'", "''")

                # Define our query
                query = f'''update book set title = "{title}" where id = {id_to_update}'''
                break
            elif choice == 2:  # Update the author
                author = ""
                while author == "":
                    author = input("Please input the book author: ")

                    if author == "":
                        print("Author cannot be empty.")

                # Define our query
                query = f'''update book set author = "{author}" where id = {id_to_update}'''
                break
            elif choice == 3:  # Update the quantity
                qty = ""
                while True:
                    try:
                        qty = int(input("Please input the quantity of books: "))
                        if isinstance(qty, int):
                            break
                    except Exception as error:
                        print(error)
                        print(f"Invalid entry: {qty}. Must be an integer value.")

                # Define our query
                query = f'''update book set qty = "{qty}" where id = {id_to_update}'''
                break

        # Attempt to connect to the DB.
        try:
            db = sqlite3.connect(db)

            cursor = db.cursor()

            # Update my book quantity by -1.
            cursor.execute(query)
            db.commit()
        except ConnectionError as error:
            print(error)
        finally:    
            db.close()
    else:
        print("Please provide a valid book ID to update. This ID does not exist.")


def delete_book(db):
    '''Function to delete a book from the database\n
       Args: database_file_location'''

    # Obtain our list of books.
    books = obtain_books(db)
    valid_ids = []
    # Print the books out in a nice format so that we can get the
    # id of the book to be deleted.
    print("Printing book list.\n")
    for book in books:
        valid_ids.append(book[0])
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Author: {book[2]}")
        print(f"Quantity: {book[3]}\n")

    while True:
        # Request the id to be deleted from the user.
        try:
            id_to_delete = int(input("Please input the ID of the book to delete from the system: "))
            if isinstance(id_to_delete, int):
                break
        except Exception as error:
            print(error)

        print("ID must be an integer value")

    if id_to_delete in valid_ids:
        # Attempt to connect to the DB.
        try:
            db = sqlite3.connect(db)

            cursor = db.cursor()

            # Do my sql delete on the id entered by the user.
            cursor.execute(f'''delete from book where id = {id_to_delete}''')
            db.commit()
        except ConnectionError as error:
            print(error)
        finally:
            db.close()
    else:
        print("Please provide a valid book ID to delete. This ID does not exist.")


def search_book(db):
    '''Function to search for books in the database\n
       Args: database_file_location'''

    # Obtain our search term from the user.
    term = input("Please input your search term: ")

    # Attempt to connect to the DB.
    try:
        db = sqlite3.connect(db)

        cursor = db.cursor()

        # Search our title and author fields for our term.
        cursor.execute(f'''select * from book where title LIKE "%{term}%" or author LIKE "%{term}%"''')

        # Print out our results.
        for index, row in enumerate(cursor):
            print(f"Search result {index + 1}: ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Quantity: {row[3]}")
    except ConnectionError as error:
        print(error)
    finally:
        db.close()


# START MAIN

# Define our database location, relative to our program.
db_file = './ebookstore'
# Set True for additional info, False for off.
DEBUG = False

# We check for existance of the database here.
if os.path.isfile(db_file):
    if DEBUG:
        print("DEBUG: Database exists, skipping initialisation.")
else:
    if DEBUG:
        print("DEBUG: No database found, initialising...")

    # DB Doesnt exist so we are calling initialise_db
    # to create it and popuplate it.
    initialise_db(db_file)
    if DEBUG:
        print("DEBUG: Initialisation complete.")

# Infinite loop for our menu, until we select 0 to exit()
while True:
    # Debug code here to show the contents of our table
    # as we are testing our functionality.  Would turn this
    # off on a production app probably.
    if DEBUG:
        # Call obtain_books to get a list of everything in
        # the database, returns a list of tulpes.
        books = obtain_books(db_file)

        # Print out the books and their details in a human
        # readable view.
        print("DEBUG: Printing book list.\n")
        for book in books:
            print(f"DEBUG: ID: {book[0]}")
            print(f"DEBUG: Title: {book[1]}")
            print(f"DEBUG: Author: {book[2]}")
            print(f"DEBUG: Quantity: {book[3]}\n")

    # Display our menu with options.
    menu = input('''Select one of the following options:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
: ''')

    # Section for switching on menu option entered.
    if menu == "1":
        enter_book(db_file)
    elif menu == "2":
        update_book(db_file)
    elif menu == "3":
        delete_book(db_file)
    elif menu == "4":
        search_book(db_file)
    elif menu == "0":
        exit()
    else:
        print("Incorrect menu option.")
