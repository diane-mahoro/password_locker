import unittest
from cledential_class import Cledentials

class TestCledentials(unittest.TestCase):

    '''
    This is a test class for cledentials class behaviors
    '''
    def setUp(self):
        '''
        This method run before each test cases
        '''
        self.new_cledential=Cledentials("Facebook","Mubiligi Diane","di123456789")
    def test_init(self):
        self.assertEqual(self.new_cledential.type,"Facebook")
        self.assertEqual(self.new_cledential.user_name,"Mubiligi Diane")
        self.assertEqual(self.new_cledential.password,"di123456789")
    
    def test_save_cledential(self):
        '''
        this case checks if the cledential is added
        to to the list
        '''
        self.new_cledential.save_cledential()
        self.assertEqual(len(Cledentials.cledential_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Cledentials.cledential_list=[]

    def test_multiple_cledentials(self):
        '''
        this case checks if more cledentials can be 
        saved
        '''
        self.new_cledential.save_cledential()
        another_cledential=Cledentials("istagram","mubiligi diane","d123456789")
        another_cledential.save_cledential()
        self.assertEqual(len(Cledentials.cledential_list),2)

    def test_delete_cledential(self):
        '''
        this case checks if a cledential can be deleted
        '''
        self.new_cledential.save_cledential()
        another_cledential=Cledentials("istagram","mubiligi diane","d123456789")
        another_cledential.save_cledential()
        another_cledential.delete_cledential()
        self.assertEqual(len(Cledentials.cledential_list),1)

    def test_find_cledentials(self):
        '''
        this case checks if you can find your cledentials
        '''
        self.new_cledential.save_cledential()
        another_cledential=Cledentials("instagram","mubiligi diane","d123456789")
        another_cledential.save_cledential()
        find_cledential=Cledentials.find_by_type("instagram")
        self.assertEqual(find_cledential.password,another_cledential.password)
if __name__ == '__main__':
    unittest.main()