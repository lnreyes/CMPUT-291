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
        CONNECT_INFO = "{0}/{1}@gwynne.cs.ualberta.ca:1521/CRS".format(ORACLE_USER, ORACLE_PSWD)
        PARTY_SIZE = 1

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

    valid = False
    while not valid:
        
        # Get car info
        while True:
            serial_no = input('Please enter the serial number of the vehicle: ').strip()
            if serial_no == 'q':
                exit()
            else:
                # Look up serial number if it's already registered
                try:
                    curs.execute("""SELECT serial_no FROM vehicle WHERE serial_no = int('{0}')""".format(serial_no))
                    result = curs.fetchall()
                except cx_Oracle.DatabaseError as exception:
                    error = exception.args
                    print(sys.stderr, "Oracle code: ", error.code)
                    print(sys.stderr, "Oracle message: ", error.message)
                    return
                        
                if result:
                    print('Vehicle has already been registered.')
                else:
                    # Register vehicle
                    try:
                        maker = input('Please enter the maker of the vehicle: ').strip()
                        model = input('Please enter the model of the vehicle: ').strip()
                        year = input('Please enter the year of the vehicle: ').strip()
                        color = input('Please enter the serial number of the vehicle: ').strip()
                        type_id = input('Please enter the serial number of the vehicle: ').strip()
                        
                        #UNSURE ABOUT TYPE_ID BEING CONVERTED TO AN INT // do we even need type_id?
                        curs.execute("""INSERT INTO vehicle VALUES
                                        (int('{0}'), '{1}', '{2}', '{3}', '{4}', int('{5}'))"""
                                        .format(serial_no, maker, model, year, color, type_id)
                        con.commit()
                    except cx_Oracle.DatabaseError as exception:
                        error = exception.args
                        print(sys.stderr, "Oracle code: ", error.code)
                        print(sys.stderr, "Oracle message: ", error.message)
                        return
        
        # Get person info
        while True:
            sin = input('Please enter the sin number of the person: ').strip()
            if sin == 'q':
                exit()
            else:
                # Look up serial number if it's already registered
                try:
                    curs.execute("""SELECT serial_no FROM vehicle WHERE serial_no = '{0}'""".format(serial_no))
                    result = curs.fetchall()
                except cx_Oracle.DatabaseError as exception:
                    error = exception.args
                    print(sys.stderr, "Oracle code: ", error.code)
                    print(sys.stderr, "Oracle message: ", error.message)
                    return
                                     
                if result:
                    print('Person has already been registered.')
                else:
                    # Register person
                    try:
                        name = input('Please enter the name of the person: ').strip()
                        height = input('Please enter the height of the person: ').strip()
                        weight = input('Please enter the weight of the person: ').strip()
                        eyecolor = input('Please enter the eye colour of the person: ').strip()
                        haircolor = input('Please enter the hair colour of the person: ').strip()
                        addr = input('Please enter the address of the person: ').strip()
                        gender = input('Please enter the gender of the person: ').strip().lower()
                        birthday = input('Please enter the birthday of the person: ').strip()
                        
                        #TO_DATE WORKS OR NAH
                        curs.execute("""INSERT INTO people VALUES
                            (int('{0}'), '{1}', float('{2}'), float('{3}'), '{4}', '{5}', '{6}', '{7}', to_date('{8}', YYYY-MM-DD)"""
                            .format(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
                        con.commit()
                    except cx_Oracle.DatabaseError as exception:
                        error = exception.args
                        print(sys.stderr, "Oracle code: ", error.code)
                        print(sys.stderr, "Oracle message: ", error.message)
                        return
        
        # Get owner info
        while True:
            # Register owner
            try:
                sin = input('Please enter the sin number of the person: ').strip()
                curs.execute("""SELECT name FROM people WHERE sin = '{0}'""".format(sin))
                result = curs.fetchall()
                
                                     #
                primary_owner = input('Is %s the primary owner of this vehicle? (y/n) ' %result).lower()
                curs.execute("""INSERT INTO vehicle VALUES
                    (int('{0}'), '{1}', '{2}')"""
                    .format(sin, serial_no, primary_owner)
                con.commit()
            except cx_Oracle.DatabaseError as exception:
                error = exception.args
                print(sys.stderr, "Oracle code: ", error.code)
                print(sys.stderr, "Oracle message: ", error.message)
                return
                                
    valid = True

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


