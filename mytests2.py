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
if __name__ == '__main__':
    unittest.main()