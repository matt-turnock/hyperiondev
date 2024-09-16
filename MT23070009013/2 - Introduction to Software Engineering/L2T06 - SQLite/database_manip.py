# pseudo:
# create a table called python_programming with the following columns, id, name, grade
# poplate the table with the data from the brief
# select all records with a grade between 60 and 80
# change Carl Davis' grade to 65
# delete dennis fredrickson's row
# "Change the grade of all people with an id below than 55"
# Unsure what the above brief question means, because the English is broken
# So ill assume i can just change their grade arbitrarily if their id is below 55

import sqlite3


def create_table():
    '''Function to initialise the database'''
    try:
        db = sqlite3.connect('./my_db')

        cursor = db.cursor()

        cursor.execute('''create table if not exists
                       python_programming(id integer primary key, name varchar(30), grade integer)
                       ''')

        db.commit()
    except Exception as error:
        db.rollback()
        print(error)
    finally:
        db.close()


def populate_data():
    '''Function to initlise the data for the database'''
    # Just want a list of tulpes here for data
    data = [(55, 'Carl Davies', 61),
            (66, 'Dennis Fredrickson', 88),
            (77, 'Jane Richards', 78),
            (12, 'Peyton Sawyer', 45),
            (2, 'Lucas Brooke', 99)]

    try:
        db = sqlite3.connect('./my_db')

        cursor = db.cursor()

        cursor.executemany('''insert into python_programming(id, name, grade)
                           values (?, ?, ?)''', data)

        db.commit()
    except Exception as error:
        db.rollback()
        print(error)
    finally:
        db.close()


# Do the table creation and data initialisation
create_table()
populate_data()

try:
    db = sqlite3.connect('./my_db')

    cursor = db.cursor()

    cursor.execute('''select * from python_programming where grade >= 60 and grade <= 80''')

    print("Displaying all records with a grade between 60 and 80.")
    for row in cursor:  # Iterate over any records returned
        print(f"Student ID: {row[0]}, Student Name: {row[1]}, Grade: {row[2]}")

    # I decided here that commiting after each exec would be good practise as if for
    # some reason one fails, i know where im failing in my except block.
    print("Changing Carls grade to 65.")
    cursor.execute('''update python_programming set grade = 65 where id = 55''')
    db.commit()

    print("Deleting Dennis.")
    cursor.execute('''delete from python_programming where id = 66''')
    db.commit()

    print("Changing the grade of everyone with an id below 55 to 0.")
    cursor.execute('''update python_programming set grade = 0 where id < 55''')
    db.commit()

    print("Printing out final table after all changes.")
    cursor.execute('''select * from python_programming''')
    for row in cursor:
        print(row)

except Exception as error:
    db.rollback()
    print(error)
finally:
    db.close()
