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
if __name__ == '__main__':
    unittest.main()