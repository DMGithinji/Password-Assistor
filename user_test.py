import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Setup method to run before each test cases.

        '''
        self.new_user = User("Denis","Githinji","DMG", '!q1@w2#e3$r4%t5', "dmg@gmail.com")

    def test_init(self):
        '''
        Test to check if the object is initialized properly

        '''
        self.assertEqual(self.new_user.first_name,"Denis")
        self.assertEqual(self.new_user.last_name,"Githinji")
        self.assertEqual(self.new_user.preferred_username,"DMG")
        self.assertEqual(self.new_user.password,"!q1@w2#e3$r4%t5")
        self.assertEqual(self.new_user.email,"dmg@gmail.com")

    def test_save_user(self):
        '''
        Test to check if new user can be saved

        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

if __name__ == "__main__":
    unittest.main()
