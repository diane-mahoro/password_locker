import unittest
from user_class import User
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
    def test_save_user_account(self):
        '''
        This test case test wether the user account of
        a user is saved
        '''
        self.new_user.save_account()
        self.assertEqual(len(User.user_account),1)
    def tearDown(self):
        User.user_account=[]

    def test_multiple_account(self):
        '''
        this test case tocheck if we can save multiple 
        accounts
        '''
        self.new_user.save_account()
        another_account=User("shema yvan","yvan-buravan")
        another_account.save_account()
        self.assertEqual(len(User.user_account),2)
    def test_delete_account(self):
        '''
        this test case check wether a user can delete the 
        account
        '''
        self.new_user.save_account()
        another_account=User("shema yvan","yvan-buravan")
        another_account.save_account()
        self.new_user.delete_acc()
        self.assertEqual(len(User.user_account),1)
if __name__ == '__main__':
    unittest.main()