# tracker.py
#
# TO NOTE: The brief was extremely unclear again as to
# the exact approach you should take here.  The first
# bullet states what functions should be provided
# (listed below), but the final point tells you what the
# menu should look like, which dont match.  This is the
# case for both Capstone Project options be it the
# fitness app, or the financial app.  I will be following
# what the brief states, not what the "menu" asks for.
#
# - add new expense categories
# - update expense amounts
# - delete an entire expense category
# - track spending
# - add income
# - add income categories
# - delete an income category
# - track income
# - view expense or income categories
# - calculate and display budget, income and expenses

# TO NOTE: I decided i didnt like this menu by default and that it was
# to large, so i made a sub menu for each area of interest.

import os
import sqlite3


def run_debug():
    '''Function to print out the current values in the database.\n
    No args'''
    expenses = get_expenses()
    if not expenses:
        print("No expenses, thrifty.")
    else:
        for e in expenses:
            print(e)

    incomes = get_incomes()
    if not incomes:
        print("No income you poor *******.")
    else:
        for i in incomes:
            print(i)


def generate_db():
    '''Function that initialises the database with the following.\n
    Populates some data into the Expense category table.\n
    Populates some data into the Income category table.'''
    default_excat = [("bills", ), ("car", ), ("food", )]
    default_incat = [("salary", ), ("investment", )]
    # This is stupid that to pass in many single field rows
    # you still have to force it into tuples but hey :D

    try:
        db = sqlite3.connect(db_location)
        cursor = db.cursor()

        cursor.execute('''create table if not exists expenses
                       (id integer primary key autoincrement,
                       debit float,
                       category varchar(255))''')
        db.commit()

        cursor.execute('''create table if not exists excategories
                       (id integer primary key autoincrement,
                       category)''')
        db.commit()

        cursor.executemany('''insert into excategories
                           (category) values (?)''', default_excat)
        db.commit()

        cursor.execute('''create table if not exists income
                       (id integer primary key autoincrement,
                       credit float,
                       category varchar(255))''')
        db.commit()

        cursor.execute('''create table if not exists incategories
                       (id integer primary key autoincrement,
                       category)''')
        db.commit()

        cursor.executemany('''insert into incategories
                           (category) values (?)''', default_incat)
        db.commit()
    except ConnectionError as e:
        print(e)
    finally:
        db.close()


def sub_menu(type):
    '''This function is here to recall the same skeleton sub menu.\n
    Menu options used in:\n
        Expenses\n
        Expense Categories\n
        Income\n
        Income Categories'''
    while True:
        sub_select = input(f'''{type} Sub Menu
1. Add {type}
2. Update {type}
3. Delete {type}

4. Return to previous menu

Please make your selection: ''')
        try:
            sub_select = int(sub_select)

            if sub_select > 0 and sub_select < 5:
                return sub_select
        except ValueError as e:
            print(e)
        print("Incorrect menu selection.")


def validate_id(v_id, v_table):
    '''Function to validate the id within a table.\n
    Args:\n
        v_id: id to select\n
        v_table: table to select from
    Returns : True|False'''
    try:
        db = sqlite3.connect(db_location)
        cur = db.cursor()

        cur.execute(f'''select * from {v_table} where id ="{v_id}"''')
        if cur.fetchone() is None:
            return False
        else:
            return True
    except ConnectionError as e:
        print(e)
    finally:
        db.close()


def validate_category(v_category, v_table):
    '''Function to validate the category within a table.\n
    Args:\n
        v_category: category to select\n
        v_table: table to select from\n
    Returns : True|False'''
    try:
        db = sqlite3.connect(db_location)
        cur = db.cursor()

        cur.execute(f'''select * from {v_table} where category = "{v_category}"''')
        if cur.fetchone() is None:
            return False
        else:
            return True
    except ConnectionError as e:
        print(e)
    finally:
        db.close()


def get_categories(v_table):
    '''Function to display all categories from {v_table}\n
    Args:\n
        v_table: Name of the table within the database'''
    try:
        db = sqlite3.connect(db_location)
        cur = db.cursor()

        cur.execute(f'''select category from {v_table}''')
        categories = cur.fetchall()

        print("\nListing Expense Categories...")
        for c in categories:
            print(c[0])
    except ConnectionError as e:
        print(e)
    finally:
        db.close()


def get_expenses():
    '''Function to display all expenses.'''
    try:
        db = sqlite3.connect(db_location)
        cur = db.cursor()

        cur.execute('''select id, debit, category from expenses''')

        expenses = cur.fetchall()
        if expenses:
            for e in expenses:
                print(f"Id: {e[0]}, Debit: {e[1]}, Category: {e[2]}")
        else:
            print("No expenses to display.")
    except ConnectionError as e:
        print(e)
    finally:
        db.close()


def get_incomes():
    '''Function to display all incomes.'''
    try:
        db = sqlite3.connect(db_location)
        cur = db.cursor()

        cur.execute('''select id, credit, category from income''')

        incomes = cur.fetchall()
        if incomes:
            for i in incomes:
                print(f"Id: {i[0]}, Credit: {i[1]}, Category: {i[2]}")
        else:
            print("No incomes to display.")
    except ConnectionError as e:
        print(e)
    finally:
        db.close()


def generate_budget():
    '''Function that displays budget information.'''
    print("Generating and displaying budget.")
    expenses = totals("expenses")
    incomes = totals("income")

    print("Your Expenses.")
    get_expenses()
    print(f"Total: {expenses}")

    print("\nYour Incomes.")
    get_incomes()
    print(f"Total: {incomes}")

    print(f"\nYour budget is (income - expenses) {incomes - expenses}")


def totals(v_table):
    '''Function that calculates total values\n
    Args:\n
        v_table: Name of the table to get values from
    Returns: list|0'''
    try:
        db = sqlite3.connect(db_location)
        cur = db.cursor()
        if v_table == "expenses":
            cur.execute(f'''select debit from expenses''')
        elif v_table == "income":
            cur.execute(f'''select credit from income''')

        results = cur.fetchall()

        result = 0
        for r in results:
            result += r[0]

        if result:
            return result
        else:
            return 0
    except ConnectionError as e:
        print(e)
    finally:
        db.close()


cwd = os.getcwd()
db_name = "tracker.db"
db_location = f"{cwd}\\{db_name}"
DEBUG = False

if DEBUG:
    run_debug()

while True:
    input_id = ""
    input_value = ""
    input_category = ""

    if not os.path.isfile(db_location):
        print("Database does not exist, generating tables...")
        generate_db()

    menu_select = (input('''\nExpense Tracker App Menu Selection

1. -> Expenses
2. -> Expense Categories
3. Track Expenses
4. -> Income
5. -> Income Categories
6. Track Income
7. View Expense/Income Categories
8. Display Budget
9. Exit

Selection:
'''))
    try:
        menu_select = int(menu_select)
        if menu_select == 1:
            sub = sub_menu("Expenses")
            try:
                db = sqlite3.connect(db_location)
                cur = db.cursor()

                get_expenses()

                if sub == 1:
                    get_categories("excategories")
                    input_category = input("Please input the category you wish to add this Expense to: ")
                    if validate_category(input_category, "excategories"):
                        try:
                            input_value = int(input(f"Please input the value for your {input_category} Expense: "))

                            print("Adding Expense...")
                            cur.execute(f'''insert into expenses (debit, category) values ("{input_value}", "{input_category}")''')
                            db.commit()
                        except ValueError as e:
                            print(e)
                            print("Please input a valid amount for the Expense.")
                    else:
                        print("Category doesnt exist, please add this via the menu.")
                elif sub == 2:
                    while validate_id(input_id, "expenses") is False:
                        try:
                            input_id = int(input("Please input the id of the expense you wish to update: "))
                        except ValueError as e:
                            print(e)

                    get_categories("excategories")
                    input_category = input("Please input an updated category for this Expense: ")
                    if validate_category(input_category, "excategories"):
                        try:
                            input_value = int(input("Please input an updated Debit value for this Expense: "))

                            print(f"Updating expense {input_id}...")
                            cur.execute(f'''update expenses set debit = "{input_value}", category = "{input_category}" where id = "{input_id}"''')
                            db.commit()
                        except ValueError as e:
                            print(e)
                            print("Please input a valid amount for the Expense.")
                    else:
                        print("Invalid category.")
                elif sub == 3:
                    while validate_id(input_id, "expenses") is False:
                        try:
                            input_id = int(input("Please input the id of the Expense you wish to delete: "))
                        except ValueError as e:
                            print(e)

                    print(f"Deleting Expense {input_id}...")
                    cur.execute(f'''delete from expenses where id = "{input_id}"''')
                    db.commit()
                else:
                    pass
            except ConnectionError as e:
                print(e)
            finally:
                db.close()
        elif menu_select == 2:
            sub = sub_menu("Expense Categories")
            try:
                db = sqlite3.connect(db_location)
                cur = db.cursor()

                get_categories("excategories")

                if sub == 1:
                    input_category = input("Please input the new category: ")
                    if validate_category(input_category, "excategories"):
                        print("This category already exists.")
                    else:
                        print("Adding expense category...")
                        cur.execute(f'''insert into excategories (category) values ("{input_category}")''')
                        db.commit()
                elif sub == 2:
                    input_category = input("Please input the category to be updated: ")
                    if validate_category(input_category, "excategories"):
                        updated_category = input("Please input what you wish this category to be updated to: ")
                        if validate_category(updated_category, "excategories"):
                            print("Category already exists.")
                        else:
                            print(f"Updating expense category {input_category}...")
                            cur.execute(f'''update excategories set category = "{updated_category}" where category = "{input_category}"''')
                            db.commit()                            
                    else:
                        print("Invalid category.")
                elif sub == 3:
                    while validate_category(input_category, "excategories") is False:
                        input_category = input("Please input the category you wish to delete: ")

                    print(f"Deleting expense category {input_category}...")
                    cur.execute(f'''delete from excategories where category = "{input_category}"''')
                    db.commit()
                else:
                    pass
            except ConnectionError as e:
                print(e)
            finally:
                db.close()
        elif menu_select == 3:
            get_expenses()
        elif menu_select == 4:
            sub = sub_menu("Income")
            try:
                db = sqlite3.connect(db_location)
                cur = db.cursor()

                get_incomes()

                if sub == 1:
                    get_categories("incategories")
                    input_category = input("Please input the category you wish to add this income to: ")
                    if validate_category(input_category, "incategories"):
                        try:
                            input_value = int(input(f"Please input the value for your {input_category} Income: "))
                            print("Adding Income...")
                            cur.execute(f'''insert into income (credit, category) values ("{input_value}", "{input_category}")''')
                            db.commit()
                        except ValueError as e:
                            print(e)
                            print("Must be a numerical value.")
                    else:
                        print("Category doesnt exist, please add this via the menu.")
                elif sub == 2:
                    while validate_id(input_id, "income") is False:
                        try:
                            input_id = int(input("Please input the id of the Income you wish to update: "))
                        except ValueError as e:
                            print(e)

                    get_categories("incategories")
                    input_category = input("Please input an updated category for this Income: ")
                    if validate_category(input_category, "incategories"):
                        try:
                            input_value = int(input("Please input an updated Credit value for this Income: "))
                            print(f"Updating Income {input_id}...")
                            cur.execute(f'''update income set credit = "{input_value}", category = "{input_category}" where id = "{input_id}"''')
                            db.commit()
                        except ValueError as e:
                            print(e)
                            print("Must me a numerical value.")
                    else:
                        print("Invalid category.")
                elif sub == 3:
                    while validate_id(input_id, "income") is False:
                        try:
                            input_id = int(input("Please input the id of the Income you wish to delete: "))
                        except ValueError as e:
                            print(e)

                    print(f"Deleting Income {input_id}...")
                    cur.execute(f'''delete from income where id = "{input_id}"''')
                    db.commit()
                else:
                    pass
            except ConnectionError as e:
                print(e)
            finally:
                db.close()
        elif menu_select == 5:
            sub = sub_menu("Income Categories")

            try:
                db = sqlite3.connect(db_location)
                cur = db.cursor()

                get_categories("incategories")

                if sub == 1:
                    input_category = input("Please input the new category: ")

                    if validate_category(input_category, "incategories"):
                        print("This category already exists.")
                    else:
                        print("Adding Income category...")
                        cur.execute(f'''insert into incategories (category) values ("{input_category}")''')
                        db.commit()
                elif sub == 2:
                    input_category = input("Please input the category to be updated: ")
                    if validate_category(input_category, "incategories"):
                        updated_category = input("Please input what you wish this category to be updated to: ")
                        if validate_category(updated_category, "incategories"):
                            print("Category already exists.")
                        else:
                            print(f"Updating Income category {input_category}...")
                            cur.execute(f'''update incategories set category = "{updated_category}" where category = "{input_category}"''')
                            db.commit()
                    else:
                        print("Invalid category.")
                elif sub == 3:
                    while validate_category(input_category, "incategories") is False:
                        input_category = input("Please input the category you wish to delete: ")

                    print(f"Deleting Income category {input_category}...")
                    cur.execute(f'''delete from incategories where category = "{input_category}"''')
                    db.commit()
                else:
                    pass
            except ConnectionError as e:
                print(e)
            finally:
                db.close()
        elif menu_select == 6:
            get_incomes()
        elif menu_select == 7:
            get_categories("excategories")
            get_categories("incategories")
        elif menu_select == 8:
            generate_budget()
        elif menu_select == 9:
            exit()
        else:
            print(f"Incorrect menu selection made: {menu_select}!")
    except ValueError as e:
        print(f"Error {e}: You didnt provide a valid data type for this menu selection.")

    # I did this because when i was testing singular areas of the code
    # i was getting fed up with selecing 9 to exit my application :rofl:
    if DEBUG:
        exit()
