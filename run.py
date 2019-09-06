#!/usr/bin/env python3.6
from user_class import User
from cledential_class import Cledentials
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
def create_cledential(type,user_name,password):
    '''
    function to create a credential
    '''
    new_cledential=Cledential(type,user_name,password)
    return new_cledential
def save_cledentials(cledential):
    '''
    this function save the cledential
    '''
    cledential.save_cledential()
def delete_cledentials(cledential):
    '''
    this function deletes the cledential
    '''
    cledential.delete_cledential()
def find_cledential(type):
    '''
    this function deletes a cledential
    '''
    return Cledential.find_by_type(type)
def existing(type):
    '''
    this checks if an account exists
    '''
    return Cledential.cledential_exist(type)

def display_credentials():
    '''
    function returns all cledentials
    '''
    return Cledential.display_cledential()
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
    print("Use this short code: ccc- to create nea credential, dc - display credentials, fc - find credentials, ex -exit the credential list")
    short_code = input().lower()
    if short_code =='ccc':
        print("NEW CREDETIAL ACCOUNT")
        print("_"*10)
        print("Account Type........")
        a_type=input()
        
        print("User name...........")
        user_names=input()

        print("Password............")
        p_word=input()
        save_cledentials(create_cledential(a_type,user_name,p_word))
        print('\n')

        print(f"Credential for {a_type} account, User name {user_names} password {p_word}")

        print('\n')
    elif short_code == 'dc':
        if display_credentials():
            print("here is the list of your credentials")
            print('\n')
            for x in display_credentials():
                print(f"{x.type} ...{x.user_name}....{x.password}")

                print('\n')
        else:
            print("You don't seem to have any credentials yet")
            print('\n')

        elif short_code=='fc':
            print("please enter the type you want to search for")

            search_type=input() 
            if existing(search_type):
                search_cledential=find_cledential(search_type)
                print(f"{search_cledential.user_name}...{search_cledential.password}")
                print('_'* 20)

                print(f"Account type.......{search_cledential.type}")
                print(f"User name.......{search_cledential.user_name}")
                print(f"Password.......{search_cledential.password}")

            else:
                print("That credential does not exists")  
        elif short_code== 'ex':
            print("bye bye .....")
        else:
            print("please check properly the short code you are using")


if __name__ == '__main__':

    main()

