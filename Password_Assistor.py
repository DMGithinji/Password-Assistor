#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

#########################################################################################################################################
#User functions
#########################################################################################################################################

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

#########################################################################################################################################
#Credentials functions
#########################################################################################################################################

def create_account(account,username,email, password):
    '''
    Function to create a new user

    '''
    new_account = Credentials(account, username, email, password)
    return new_account

def save_credentials(credentials):
    '''
    Function to save account credentials

    '''
    credentials.save_credentials()

def delete_by_account(account):
    '''
    Function to  delete saved credentials from the credentials_list

    '''
    Credentials.delete_by_account(account)

def display_accounts():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_accounts()

def account_exists(account_name):
    '''
    Function that determines whether an account exists or not

    Output: Boolean
    '''
    return Credentials.account_exists(account_name)

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

############################################################################################################################################
#Begin main program
############################################################################################################################################
def main():

    print("WELCOME TO YOUR P.A. - PASSWORD ASSISTOR ")

    while True:
        breakToken = True
        print("Use these short codes to navigate through this section of the app:\nca - create a new user account\nex -exit the contact list ")
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
                if breakToken:
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
                        #Account Credentials Section
                        ##########################################################################################################################

                        while True:
                            print("Use these short codes to navigate through this section of the app:\nsa - Save Account Credentials\nna - New Account Credentials\nda - Display Accounts that have been registered on the app\ndc - Display Credentials for a specific account that has been registered on the app\ndel - Delete an account that has been registered on the app\nex -Exit the Credentials Section")
                            print("Input shortcode: ")

                            short_code = input().lower()
                            if short_code == 'sa':
                                print("Save an Existing Account")
                                print("-"*10)

                                print ("Account name ....")
                                account = input()

                                print("Account username ...")
                                username = input()

                                print("Email used for account...")
                                account_email = input()

                                print("Account Password ...")
                                account_password = input()

                                save_credentials(create_account(account, username, account_email, account_password))
                                print ('\n')
                                print(f"Ok {first_name}, your account credentials for {account} have been successfully been saved")
                                print ('\n')

                            elif short_code == 'na':
                                print("Create and Save New Account Credentials")
                                print("-"*10)

                                print ("Account name ....")
                                account = input()

                                print("Account username ...")
                                username = input()

                                print("Email used for account...")
                                account_email = input()                    
                                
                                ##########################################################################################################################

                                print("Would you like to suggest us to generate a secure password for you or would you like to use one of your own?")
                                print("Enter 'gen' - for us to generate one for you\nEnter 'mine' - if you wish to input your own")
                                decision = input().lower()

                                if decision == 'mine':
                                    print("Enter your desired password for this account...")
                                    account_password = input()
                                    save_credentials(create_account(account, username, account_email, account_password))
                                    print ('\n')
                                    print(f"Ok {first_name}, your account credentials for {account} have been successfully been saved")
                                    print ('\n')

                                elif decision == 'gen':
                                    print("Enter your desired password length...")
                                    password_length = int(input())
                                    account_password =  password_generator(password_length)
                                    print(f"Your generated password is: {account_password}")
                                    save_credentials(create_account(account, username, account_email, account_password))
                                    print ('\n')
                                    print(f"Ok {first_name}, your account credentials for {account} have been successfully been saved")
                                    print ('\n')

                                else:
                                    print("Oops, that short code does not seem to march any of the prescribed shortcodes, please try again")

                            elif short_code == 'da':
                                if display_accounts():
                                    print("The following are the accounts have your login credentials saved:")
                                    print(display_accounts())
                                else:
                                    print("You don't seem to have anything saved yet.")

                            elif short_code == 'dc':
                                print("Enter the name of the account you wish to see the credentials of")
                                account_name = input()
                                if account_exists(account_name):
                                    print(find_by_account(account_name))
                                else:
                                    print("The account name you entered is currently not registered in the app")

                            elif short_code == 'del':
                                print("Enter the name of the account you wish to delete")
                                account_name = input()
                                if account_exists(account_name):
                                    delete_by_account(account_name)
                                    print(f"{account_name} has been successfully deleted")
                                else:
                                    print("The account name you entered is currently not registered in the app")

                            elif short_code == 'ex':
                                breakToken = False
                                break

                            else:
                                print("Oops, the passwords do not seem to march, please try again")  

                    else:
                        print("Oops, the passwords do not seem to march, please try again")                
                    
                else:
                    break
                        ##########################################################################################################################
                        #End of Account Credentials section
                        ##########################################################################################################################

                    

        elif short_code == 'ex':
            print("Good Day .......")
            break

        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()