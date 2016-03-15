#Mini-Project 1

import cx_Oracle
import sys
import getpass
import random
import datetime

def main():

    setup_oracle_connection()
    
    #Get user to pick an option
    print("--------------------------------------------")
    print("Enter '1' to register a vehicle")
    print("Enter '2' to make an auto transaction")
    print("Enter '3' for register a license")
    print("Enter '4' to record a violation ticket")
    print("Enter '5' to search")
    print("Enter 'q' to exit program")
    print("--------------------------------------------")
    option = input('Please pick an option: ')
    if 'q' in option.lower():
        exit()
    else:
        try:
            option = int(choice)
        except ValueError as ve:
            pass

    if option == 1:
        #TO DO
        register_vehicle()
    elif option == 2:
        #TO DO
        transaction()
    elif option == 3:
        #TO DO
        register_license()
    elif option == 4:
        #TO DO
        record_violation()
    elif option == 5:
        #TO DO
        search()

    return


def setup_oracle_connection():
    #TO DO

def register_vehicle():
    #TO DO

def transaction():
    #TO DO

def register_license():
    #TO DO

def record_violation():
    #TO DO

def search():
    #TO DO

if __name__ == "__main__":
    main()


