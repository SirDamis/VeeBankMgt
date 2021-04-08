import sqlite3
import secrets
import string
import random
import os

class CreateUser():
    def __init__(self, first_name, second_name, gender, account_type):
        """
        Create 9 digits account number that starts with 531. 
        The account number is then saved into the database.
        """
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.account_type = account_type
        self.account_number = '531'+ ''.join(random.choices(string.digits, k=6)) #todo: Generate new number if it exissts in database
        self.account_password = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(10))
        self.account_balance = 0.0

    def __display_details(self):
        print(f'Account successfully created.\n\tAccount Name: {self.second_name} {self.first_name}.\n\tAccount Number: {self.account_number}.\n\tAccount Password: {self.account_password}\n\tAccount Balance: {self.account_balance}')
        
    def __upload_data(self):
        """
        Upload customer data to database (SQLite database)
        """
        data_path = "database"
        os.makedirs(data_path, exist_ok=True)
        try:
            conn = sqlite3.connect('database/customers.db')
            query = '''CREATE TABLE IF NOT EXISTS all_customers_database (
                         first_name TEXT, second_name TEXT,
                         gender TEXT, account_type TEXT, account_number INTEGER PRIMARY KEY UNIQUE NOT NULL,
                         account_password VARCHAR, account_balance REAL );'''
            #Create table
            cursor = conn.cursor()
            print("Connection sucessful")
            cursor.execute(query)
            conn.commit()
            print("Table created")
            #Insert a row to a database
            insert_query ='''INSERT INTO all_customers_database
                         (first_name, second_name, gender, account_type, account_number, account_password, account_balance)
                         VALUES  
                         (?, ?, ?, ?, ?, ?, ?);'''
            conn.execute(insert_query, (self.first_name, self.second_name, self.gender, self.account_type, self.account_number, self.account_password, self.account_balance))
            print("Your details saved successfully.")
        except sqlite3.Error as err:
            # print("Error while creating a sqlite table ", err)
            print("Error creating database")
        finally:
            if conn:
                conn.close()
                # print("Sqlite connection closed.")

    def run_all(self):
        self.__upload_data()
        self.__display_details()
        