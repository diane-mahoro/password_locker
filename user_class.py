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