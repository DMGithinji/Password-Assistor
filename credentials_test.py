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
        self.new_account_credentials = User("Facebook","DMG", "dmg@gmail.com", '!q1@w2#e3$r4%t5')


if __name__ == "__main__":
    unittest.main()