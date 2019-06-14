
class User:
    '''
    Class that generates new instance of the user, with their login informations to the application
    
    '''

    def __init__ (self, first_name, last_name, preferred_username, password, email):
        '''
        __init__ method that helps to define properties for our objects

        '''
        self.first_name = first_name
        self.last_name = last_name
        self.preferred_username = preferred_username
        self.password = password
        self.email = email


