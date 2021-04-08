import sqlite3

def validate_input(depositor_account_number, depositor_account_password):
    """
    Validate depositor account number and password.
    Return True if account number and password entered are found in SQLite database, else False
    """
    try:
        conn = sqlite3.connect('database/customers.db')
        cursor = conn.cursor()
        conn.commit()
        #Select data from database
        cursor.execute("SELECT COUNT(*) FROM all_customers_database WHERE account_number=? AND account_number=?", (depositor_account_number, depositor_account_password))
        data = cursor.fetchone()
        print(data)
        if data == 0:
            return False
        else:
            print("The account number and password is correct.")
            return True
    except sqlite3.Error as err:
        print(err)
        print("Error fetching database")
    finally:
        if conn:
            conn.close()

def validate_receipent_account_number(receipent_account_number):
    """
    Validate receipent account number.
    Return True if account number is found in SQLite database, else False
    """
    try:
        conn = sqlite3.connect('database/customers.db')
        cursor = conn.cursor()
        conn.commit()
        #Select data from database
        cursor.execute("SELECT COUNT(*) FROM all_customers_database WHERE account_number=? AND account_number=?", (depositor_account_number, depositor_account_password))
        data = cursor.fetchone()
        print(data)
        if data == 0:
            print("The account number entered is not in database.")
            return False
        else:
            print("The account number entered is in database.")
            return True
    except sqlite3.Error as err:
        print(err)
        print("Error fetching database")
    finally:
        if conn:
            conn.close()

def failed_authentication_prompt():
    print("Either the account number or password is not correct.")
    print("Login again and input the right details.\n Quitting program....")


def sucessful_authentication_prompt():
    print("Login successful.")
    