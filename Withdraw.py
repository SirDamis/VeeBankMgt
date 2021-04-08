import sqlite3

class DepositUser():
    def __init__(self, depositor_account_number, amount_to_deposit, receipent_account_number):
        self.amount_to_deposit = amount_to_deposit 
        self.depositor_account_number = depositor_account_number
        self.receipent_account_number = receipent_account_number

    def __fetch_and_deposit_user_data(self):
        """
        """
        print('Hello')

    def run_all(self):
        self.__fetch_and_deposit_user_data()
        