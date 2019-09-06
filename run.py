#!/usr/bin/env python3.6
from user_class import User
def create_account(userName,password):
    '''
    This function creates a new account for a user
    '''
    new_user=User(userName,password)
    return new_user
def save_accounts(acc):
    '''
    This function save the created account
    '''
    acc.save_account()
def delete_accounts(acc):
    '''
    this function deletes the account of a user
    '''
    acc.delete_acc()
