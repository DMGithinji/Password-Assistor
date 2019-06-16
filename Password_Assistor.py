#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

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

while True:
    print("WELCOME TO YOUR PA - PASSWORD ASSISTOR ")
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
                break

            else:
                print("Oops, the passwords do not seem to march, please try again")



if __name__ == '__main__':
    main()