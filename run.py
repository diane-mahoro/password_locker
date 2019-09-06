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
def main():
    print("A WARM WELCOME TO YOU FOR CHOOSING TO USE OUR SERVICE, Trust me here we keepyour credentials very safely.")
    print("Use this short codes: cc - sing up for an account, lg - to log in your account")
    
    short_code = input().lower()
    if short_code == 'cc':
        print("User Name")
        u_name=input()
        print("enter your password")
        mypass=input()
        save_accounts(create_account(u_name,mypass))
    elif short_code == 'lg':
        print("enter your user name")
        u_name=input()
        print("enter your password")
        mypass=input()
    else:
        print("invalid input")
if __name__ == '__main__':

    main()

