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
def find_accounts(name):
    '''
    This finds the account
    '''
    return User.find_by_name(name)
def check_on_acc(name):
    '''
    This function checks if an account exists using
    name
    '''
    return User.account_saved(name)
def display_accs():
    '''
    this function display accounts 
    '''
    return User.display_acc()