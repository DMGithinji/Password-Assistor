import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the Credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    '''
    def setUp(self):
        '''
        Setup method to run before each test cases.

        '''
        self.new_account_credentials = Credentials("Facebook","DMG", "dmg@gmail.com", '!q1@w2#e3$r4%t5')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.

        '''
        Credentials.accounts_credentials = []

    def test_save_credentials(self):
        '''
        Test to determine if account credentials can be saved

        '''
        self.new_account_credentials.save_credentials()
        self.assertEqual(len(Credentials.accounts_credentials),1)

    def test_multiple_saved_credentials(self):
        '''
        Test to determine if user can add credentials for multiple accounts

        '''
        self.new_account_credentials.save_credentials()
        self.test_credentials = Credentials("Twitter","Username2", "username2@gmail.com", '12345')
        self.test_credentials.save_credentials()
        self.assertEqual(len(Credentials.accounts_credentials),2)

if __name__ == "__main__":
    unittest.main()