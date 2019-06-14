import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

def setUp():
    '''
    Setup method to run before each test cases.

    '''
    self.new_contact = Contact("Denis","Githinji","DMG", '!q1@w2#e3$r4%t5', "dmg@gmail.com")

if __name__ == "__main__":
    unittest.main()
