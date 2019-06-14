import unittest
from user import User

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

def test_init(self):
    '''
    Test to check if if the object is initialized properly

    '''
    self.assertEqual(self.user.first_name,"Denis")
    self.assertEqual(self.user.last_name,"Githinji")
    self.assertEqual(self.user.preferred_username,"DMG")
    self.assertEqual(self.user.password,"!q1@w2#e3$r4%t5")
    self.assertEqual(self.user.email,"dmg@gmail.com")

if __name__ == "__main__":
    unittest.main()
