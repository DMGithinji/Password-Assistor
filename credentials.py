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

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''
        Credentials.accounts_credentials.remove(self)

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

        self.assertEqual(Contact.display_contact(),Contact.contact_list)

    @classmethod
    def password_generator(cls, password_length = 8):
        '''
        Method for generating random passwords with lower-case, upper-case, digits and special characters

        '''
        password_chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password_chars) for i in range (password_length))