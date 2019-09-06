class User:
    """
    This class generates instances for users to 
    create their logoin user name and password
    """
    user_account=[]
    def __init__(self,userName,password):
        self.userName = userName
        self.password = password

    def save_account(self):
        '''
        this method is for saving a user's acount
        '''
        User.user_account.append(self)
    def delete_acc(self):
        '''
        this method deletes an account
        '''
        User.user_account.remove(self)
    @classmethod
    def find_by_name(cls,name):
        '''
        this method takes in the username and returns
        the account with the same name
        '''
        for i in cls.user_account:
            if i.userName == name:
                return i
    @classmethod
    def account_saved(cls,name):
        '''
        this method checks wether the account is there
        using name
        '''
        for i in cls.user_account:
            if i.userName == name:
                return True
        return False
    @classmethod
    def display_acc(cls):
        '''
        This method is for displaying accounts
        '''
        return cls.user_account