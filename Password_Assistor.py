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

 print("The login details you entered do not march, please try again by entering shortcode 'lg' or exit by entering shortcode 'ex'")
'''

if __name__ == '__main__':
    main()