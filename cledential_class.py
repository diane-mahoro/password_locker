class Cledentials:
    """
    this class generates instances for
     user's cledentials 
    """
    cledential_list =[]
    def __init__(self,type,user_name,password):
        self.type=type
        self.user_name=user_name
        self.password=password

    def save_cledential(self):
        '''
        this method save the cledential in the list
        '''
        Cledentials.cledential_list.append(self)
    def delete_cledential(self):
        '''
        this method deleted a cledential
        '''
        Cledentials.cledential_list.remove(self)
    @classmethod
    def find_by_type(cls,account_type):
        '''
        this method takes in account type and returns
        that account that matches that type
        '''
        for i in cls.cledential_list:
            if i.type == account_type:
                return i