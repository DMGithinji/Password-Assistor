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
        self.new_user = User("Denis","Githinji", '!q1@w2#e3$r4%t5', "dmg@gmail.com")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []


    def test_init(self):
        '''
        Test to check if the object is initialized properly

        '''
        self.assertEqual(self.new_user.first_name,"Denis")
        self.assertEqual(self.new_user.last_name,"Githinji")
        self.assertEqual(self.new_user.password,"!q1@w2#e3$r4%t5")
        self.assertEqual(self.new_user.email,"dmg@gmail.com")

    def test_save_user(self):
        '''
        Test to check if new user can be saved

        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        '''
        Test to check if multiple users can be saved

        '''
        self.new_user.save_user()
        test_user = User("Test", "User", "12345", "testuser@gmail.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

if __name__ == "__main__":
    unittest.main()
