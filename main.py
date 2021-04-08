""""
Vee Banking Management Platform is a command line interface application that allows users to:
- create an account
- view account history
- deposit fund to an account
- withdraw fund from an account
User data is stored into SQLite database
"""

# import necessary modules
from CreateAccount import CreateUser
from Deposit import DepositUser
from Withdraw import *
from AccountHistory import *
from UserAuthenticate import *
print("\tWelcome to Vee Banking Management Platform")

try:
    response = int(input("Enter:\n\t1. To create an account.\n\t2. View account history. \n\t3. Deposit fund to account. \n\t4. Withdraw fund from account.\n"))
    if response == 1:
        """
        - Save user data to database. 
        - User data ccannot be empty string.
        """
        print("*"*10," Create Account ", "*"*10)
        first_name = input("Enter first name: ").capitalize()
        second_name = input("Enter last name: ").capitalize()
        gender = input("Enter gender (Male / Female): ").lower()
        account_type = input("Enter account type(Saving / Current): ").lower()
        CreateUser(first_name, second_name, gender, account_type).run_all()

    elif response == 2:
        """
        - User data is allowed for editing.
        - Only account name and account password can be edited.
        """
        print("*"*10," Edit Account Details ", "*"*10)
        print("To withdraw, you have to login with your account number and account password.")
        personal_account_number = int(input("Enter your account number: "))
        personal_account_password = input("Enter your account password: ")
        details_input = validate_input(personal_account_number, personal_account_password)
        print('\n')
        if details_input == True:
            sucessful_authentication_prompt()
            amount_to_deposit = float(input("Enter the amount you want to withdraw: "))
            DepositUser(personal_account_number, amount_to_deposit).run_all()
        else:
            failed_authentication_prompt()
        

    elif response == 3:
        print("*"*10," Withdraw From Account ", "*"*10)
        """
        - User data is validated by a parallel database check.
        - Withdrawal is made from the user account.
        - The amount is deducted from the user account.
        - Successful withdrawal prompt is displayed.
        """
        print("To withdraw, you have to login with your account number and account password.")
        personal_account_number = int(input("Enter your account number: "))
        personal_account_password = input("Enter your account password: ")
        details_input = validate_input(personal_account_number, personal_account_password)
        print('\n')
        if details_input == True:
            amount_to_deposit = float(input("Enter the amount you want to withdraw: "))
            DepositUser(personal_account_number, amount_to_deposit).run_all()
            print("Try again later. Quitting program....")
        else:
            failed_authentication_prompt()

    elif response == 4:
        print("*"*10," Deposit into Account ", "*"*10)
        """
        - User data is validated by a parallel database check
        - Deposit is made from the user account to the receipent account
        - The amount is deducted from the user account
        - The amount is credited into the receipt account.
        """
        print("To deposit, you have to login with your account number and account password.")
        personal_account_number = int(input("Enter your account number: "))
        personal_account_password = input("Enter your account password: ")
        details_input = validate_input(personal_account_number, personal_account_password)
        print('\n')
        if details_input == 'correct':
            receipent_account_number = input("Enter account number you want to deposit into: ")
            found = validate_receipent_account_number(receipent_account_number)
            if found == True:
                amount_to_deposit = float(input("Enter the amount you want to deposit"))
                DepositUser(personal_account_number, amount_to_deposit, receipent_account_number).run_all()
            else:
                # If account number not found, quit the program.
                print("Account number not found. Enter a registered account number.")
                print("Try again later. Quitting program....")
        else:
            print("Either the account number or password is not correct.")
            print("Try again later. Quitting program....")
    else:
       print('Invalid input. Try again.')
except ValueError:
    print('Invalid input. Try again.')