
class User:
    '''
    Class that generates new instance of the user, with their login informations to the application
    
    '''
    user_list = []

    def __init__ (self, first_name, last_name, password, email):
        '''
        __init__ method that helps to define properties for our objects

        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    def save_user(self):
        '''
        Method to save user to the application

        '''
        User.user_list.append(self)





