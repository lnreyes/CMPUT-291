#Mini-Project 1

import cx_Oracle
import sys
import getpass
import random
import datetime

def main():

    setup_oracle_connection()
    
    while True:
        #Get user to pick an option
        print("--------------------------------------------")
        print("Enter '1' to register a vehicle")
        print("Enter '2' to make an auto transaction")
        print("Enter '3' for register a license")
        print("Enter '4' to record a violation ticket")
        print("Enter '5' to search")
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
        else:
            print("--------------------------------------------")
            print("Enter '1' to register a vehicle")
            print("Enter '2' to make an auto transaction")
            print("Enter '3' for register a license")
            print("Enter '4' to record a violation ticket")
            print("Enter '5' to search")
            print("--------------------------------------------")
            print('Invalid option! Please pick again.')

    return


def setup_oracle_connection():
    global ORACLE_USER
    global ORACLE_PSWD
    global CONNECT_INFO

    while True:
        # Get account info
        ORACLE_USER = input('Please enter Oracle username: ')
        ORACLE_PSWD = getpass.getpass('Please enter Oracle password: ')
        CONNECT_INFO = '{0}/{1}@gwynne.cs.ualberta.ca:1521/CRS'.format(ORACLE_USER, ORACLE_PSWD)
        PART_SIZE = 1

        # Connect to database
        try:
            con = cx_Oracle.connect(CONNECT_INFO)
            curs = con.cursor()
        except cx_Oracle.DatabaseError as exception:
            error = exception.args
            print(sys.stderr, "Oracle code: ", error.code)
            print(sys.stderr, "Oracle message: ", error.message)
            return
                
    try:
        curs.close()
        con.close()
    except cx_Oracle.DatabaseError as exception:
        error = exception.args
        print(sys.stderr, "Oracle code: ", error.code)
        print(sys.stderr, "Oracle message: ", error.message)
        return

    return

def register_vehicle():
    # Connect to database
    try:
        con = cx_Oracle.connect(CONNECT_INFO)
        curs = con.cursor()
    except cx_Oracle.DatabaseError as exception:
        error = exception.args
        print(sys.stderr, "Oracle code: ", error.code)
        print(sys.stderr, "Oracle message: ", error.message)
        return
    #-----------------
    valid = False
    while not valid:
        # Get serial_no of car from user
        while True:
            serial_no = input('Please enter the serial number of the vehicle: ').strip()
            if serial_no == 'q':
                exit()
            elif int(serial_no):
                # Look up serial number if it's already registered
                try:
                    curs.execute("SELECT serial_no FROM vehicle WHERE serial_no = '{0}'".format(serial_no))
                    result.curs.fetchall()
                
                    

    
    #-----------------
    try:
        curs.close()
        con.close()
    except cx_Oracle.DatabaseError as exception:
        error = exception.args
        print(sys.stderr, "Oracle code: ", error.code)
        print(sys.stderr, "Oracle message: ", error.message)
        return

    #return something

def transaction():
    #TO DO
    # Connect to database
    try:
        con = cx_Oracle.connect(CONNECT_INFO)
        curs = con.cursor()
    except cx_Oracle.DatabaseError as exception:
        error = exception.args
        print(sys.stderr, "Oracle code: ", error.code)
        print(sys.stderr, "Oracle message: ", error.message)
        return
    #-----------------
    #TO DO
    #-----------------
    try:
        curs.close()
        con.close()
    except cx_Oracle.DatabaseError as exception:
        error = exception.args
        print(sys.stderr, "Oracle code: ", error.code)
        print(sys.stderr, "Oracle message: ", error.message)
        return

    #return something

def register_license():
    #TO DO
    # Connect to database
    try:
        con = cx_Oracle.connect(CONNECT_INFO)
        curs = con.cursor()
    except cx_Oracle.DatabaseError as exception:
        error = exception.args
        print(sys.stderr, "Oracle code: ", error.code)
        print(sys.stderr, "Oracle message: ", error.message)
        return
    #-----------------
    #TO DO
    #-----------------
    try:
        curs.close()
        con.close()
    except cx_Oracle.DatabaseError as exception:
        error = exception.args
        print(sys.stderr, "Oracle code: ", error.code)
        print(sys.stderr, "Oracle message: ", error.message)
        return

    #return something

def record_violation():
    #TO DO
    # Connect to database
    try:
        con = cx_Oracle.connect(CONNECT_INFO)
        curs = con.cursor()
    except cx_Oracle.DatabaseError as exception:
        error = exception.args
        print(sys.stderr, "Oracle code: ", error.code)
        print(sys.stderr, "Oracle message: ", error.message)
        return
    #-----------------
    #TO DO
    #-----------------
    try:
        curs.close()
        con.close()
    except cx_Oracle.DatabaseError as exception:
        error = exception.args
        print(sys.stderr, "Oracle code: ", error.code)
        print(sys.stderr, "Oracle message: ", error.message)
        return

    #return something

def search():
    # Connect to database
    try:
        con = cx_Oracle.connect(CONNECT_INFO)
        curs = con.cursor()
    except cx_Oracle.DatabaseError as exception:
        error = exception.args
        print(sys.stderr, "Oracle code: ", error.code)
        print(sys.stderr, "Oracle message: ", error.message)
        return
    #-----------------
    #TO DO
    #-----------------
    try:
        curs.close()
        con.close()
    except cx_Oracle.DatabaseError as exception:
        error = exception.args
        print(sys.stderr, "Oracle code: ", error.code)
        print(sys.stderr, "Oracle message: ", error.message)
        return

    #return something

if __name__ == "__main__":
    main()


