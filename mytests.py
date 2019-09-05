import unittest
from user_class import user
class Testuser(unittest.TestCase):
    '''
    This is a test class that defines tests of class behaviours
    '''
    def setUp(self):
        '''
        this method runs before each test cases
        '''
        self.new_user=User("diane-mahoro","diane-mahoro")

    def test_init(self):
        '''
        test_init is a test case to check whether an
        object is initialized properly
        '''
        self.assertEqual(self.new_user.userName,"diane-mahoro")
        self.assertEqual(self.new_user.password,"diane-mahoro")
if __name__ == '__main__':
    unittest.main()