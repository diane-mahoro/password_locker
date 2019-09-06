#!/usr/bin/env python3.6
from user_class import User
def create_account(userName,password):
    '''
    This function creates a new account for a user
    '''
    new_user=User(userName,password)
    return new_user