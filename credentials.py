import random
import string

class Credentials:
    '''
    Class that generates new instance of the account credentials, with the account details to the application

    '''
    accounts_credentials = []

    def __init__ (self, account, username, email, password):
        '''
        __init__ method that helps to define properties for our objects

        '''
        self.account = account
        self.username = username
        self.email = email
        self.password = password
    
    def save_credentials(self):
        '''
        Method to save new account credentials input by user

        '''
        Credentials.accounts_credentials.append(self)

    @classmethod
    def display_accounts(cls):
        '''
        test to see if the display is shown

        '''
        displayed_accounts = ''
        i = 1
        for accounts_credential in cls.accounts_credentials:
            displayed_accounts += '{} - {}\n' .format(i, accounts_credential.account)
            i=i+1
        return displayed_accounts

        self.assertEqual(Credentials.display_contact(),Credentials.contact_list)

    @classmethod
    def find_by_account(cls, account_name):
        '''
        Method to display an account's credentials on entering account name
        Args:
            account_name: Name of the account which you seek display its credentials
        '''
        for account_details in cls.accounts_credentials:
            if account_details.account == account_name:
                return "Account name: " + account_details.account + "\nUsername: " + account_details.username + "\nEmail used: " + account_details.email + "\nPAssword: " + account_details.password

    @classmethod
    def delete_by_account(cls, account_name):
        '''
        Method to display an account's credentials on entering account name
        Args:
            account_name: Name of the account which you seek display its credentials
        '''
        i=-1
        for account_details in cls.accounts_credentials:
            i=i+1
            if account_details.account == account_name:
                cls.accounts_credentials.pop(i)
                    

    @classmethod
    def password_generator(cls, password_length = 8):
        '''
        Method for generating random passwords with lower-case, upper-case, digits and special characters
        Args:
            password_length: The number of characters in the password to be generated
        '''
        password_chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password_chars) for i in range (password_length))

