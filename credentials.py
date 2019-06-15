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
    def password_generator(cls, password_length = 8):
        '''
        Method for generating random passwords with lower-case, upper-case, digits and special characters

        '''
        password_chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password_chars) for i in range (password_length))