
class User:
    '''
    Class that generates new instance of the user, with their login informations to the application
    
    '''
    user_list = []

    def __init__ (self, first_name, last_name, email, password):
        '''
        __init__ method that helps to define properties for our objects

        '''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save_user(self):
        '''
        Method to save user to the application

        '''
        User.user_list.append(self)

    @classmethod
    def password_correct(cls, password):
        ''' 
        Method to confirm whether password entered is correct

        '''
        for user in cls.user_list:
            return user.password == password

    @classmethod
    def name_exists(cls, first_name, last_name):
        ''' 
        Method to confirm whether password entered is correct

        '''
        for user in cls.user_list:
            return not(user.first_name == first_name and user.last_name == last_name)