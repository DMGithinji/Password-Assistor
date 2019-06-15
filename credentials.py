
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
