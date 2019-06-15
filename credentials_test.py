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
        self.test_credentials = Credentials("Twitter","Username2","username2@gmail.com",'12345')
        self.test_credentials.save_credentials()
        self.assertEqual(len(Credentials.accounts_credentials),2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credentials from our credentials list

        '''
        self.new_account_credentials.save_credentials()
        self.test_credentials = Credentials("Twitter","Username2","username2@gmail.com",'12345')
        self.test_credentials.save_credentials()
        self.new_account_credentials.delete_credentials()
        self.assertEqual(len(Credentials.accounts_credentials),1)

    def test_credentials_display_all_accounts(self):
        '''
        Test to see if all accounts can display

        '''
        self.new_account_credentials.save_credentials()
        self.test_credentials = Credentials("Twitter","Username2","username2@gmail.com",'12345')
        self.test_credentials.save_credentials()
        self.assertEqual(Credentials.display_accounts(), '1 - Facebook\n2 - Twitter\n')

    def test_display_account_credentials(self):
        '''
        Test to see if an account credentials can be displayed

        '''
        self.new_account_credentials.save_credentials()
        self.test_credentials = Credentials("Twitter","Username2","username2@gmail.com",'12345')
        self.test_credentials.save_credentials()
        account_details = Credentials.find_by_account("Twitter")
        self.assertEqual(account_details, Credentials.test_credentials)

    def test_password_update(self):
        '''
        Test to determine if password generator can generate random passwords

        '''
        self.new_account_credentials.save_credentials()
        generated_password = Credentials.password_generator(10)
        self.assertEqual(len(generated_password), 10)


if __name__ == "__main__":
    unittest.main()