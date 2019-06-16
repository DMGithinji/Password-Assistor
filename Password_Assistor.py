#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

#######################################################################
def create_user(first_name,last_name,email, password):
    '''
    Function to create a new user

    '''
    new_user = User(first_name, last_name, email, password)
    return new_user

def save_user(user):
    '''
    Function to save user

    '''
    user.save_user()

def password_correct(password):
    '''
    Function to confirm if password is correct

    '''
    return Credentials.password_correct(password)

def name_exists(first_name, last_name):
    '''
    Function to confirm if user already exists in app

    '''
    return Credentials.name_exists(first_name, last_name)

#######################################################################

def create_account(account,username,email, password):
    '''
    Function to create a new user

    '''
    new_account = Credentials(first_name, last_name, email, password)
    return new_account

def save_credentials(credentials):
    '''
    Function to save account credentials

    '''
    credentials.save_credentials()

def delete_credentials(credentials):
    '''
    Function to  delete saved credentials from the credentials_list

    '''
    credentials.delete_credentials()

def display_accounts():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_accounts()

def find_by_account(account_name):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credentials.find_by_account(account_name)

def password_generator(password_length):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credentials.password_generator(password_length)

#######################################################################

def main():

    print("WELCOME TO YOUR P.A. - PASSWORD ASSISTOR ")

    while True:
        print("Use these short codes to navigate through this section of the app:\nca - create a new user account\nlg - login to existing account\nex -exit the contact list ")
        print("Input shortcode: ")

        short_code = input().lower()

        if short_code == 'ca':
            print("New User Account")
            print("-"*10)

            print ("First name ....")
            first_name = input()

            print("Last name ...")
            last_name = input()

            print("Email ...")
            email = input()

            while True:
                print("Password ...")
                password1 = input()

                print("Confirm password ...")
                password2 = input()

                if password1 == password2:
                    password = password1
                    save_user(create_user(first_name, last_name, email, password))
                    print ('\n')
                    print(f"{first_name} {last_name}, your Password Assistor (PA) account has been successfully been created")
                    print ('\n')
                    ##########################################################################################################################

                    ##########################################################################################################################


                else:
                    print("Oops, the passwords do not seem to march, please try again")

        elif short_code == 'ex':
            print("Bye .......")
            break

        else:
            print("I really didn't get that. Please use the short codes")
    '''
        elif short_code == 'lg':

            print("Please enter your Password Assistor (PA) account details to login")
            print("-"*10)

            print ("Email ....")
            email = input()

            print("Password ...")
            password = input()

            if login_checker(email, password):
                print(f"Welcome {first_name}, you have successfully logged in")

            else:
                print("The login details you entered do not march, please try again by entering shortcode 'lg' or exit by entering shortcode 'ex'")
    '''

if __name__ == '__main__':
    main()