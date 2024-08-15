# This is the Transaction module
import pandas as pd
import numpy as np
import os
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sanjith",
    database = "Bank_Management"
)

mycursor = mydb.cursor()

import login
upi_passwd = login.inp_passwd
u_id = login.inp_uid

def upi():
    
    formula1 = f"select upi_id from acc_details where uid = '{u_id}' and passwd = '{upi_passwd}'"
    mycursor.execute(formula1)
    retrived_upi_id = mycursor.fetchall()
    upi_id = retrived_upi_id[0][0]

    # This is upi deposit
    if withdrawl == False:
        print("Hello world")


# Init for this module
def init_transfermoney():
        print("\n"+"\033[1;20;96m=\033[0m"*29)
        print("\033[1;20;96m|::: TRANSFER MONEY PAGE :::|\033[0m")
        print("\033[1;20;96m=\033[0m"*29)
        print("""
CHOOSE YOUR MODE OF TRANSACTION
1 - DEPOSIT           
2 - WITHDRAWL
3 - MAIN MENU
""")
        # Function to repeat the input if the user gives a wrong input
        def inp_mod():
            # Global variable for choosing the mode of transaction
            global inp_mode
            inp_mode = int(input(">>> "))
        inp_mod()
        if inp_mode in [1,2,3]:
            if inp_mode == 1:
                # Making a bool to make sure deposit and withdraw do not coincide
                global withdrawl
                withdrawl = False
                print("""
DIGITAL DEPOSIT OPTIONS
1 - UPI
2 - NET BANKING
3 - WALLET
""")
                # Function to repeat the input if the user gives a wrong input
                def inp_dep_opti():
                    # Global variable for making the option viewalbe in the next row
                    global inp_dep_opt
                    inp_dep_opt = int(input(">>> "))
                inp_dep_opti()
                if inp_dep_opt in [1,2,3]:
                    if inp_dep_opt == 1:
                        upi()
                else:
                    print("\033[1;20;31m\nERROR: WRONG INPUT!\nTRYAGAIN!\033[0m\n")
                    inp_dep_opti()
            elif inp_mode == 2:
                withdrawl = True
                print("\033[1;20;31m\nNOTE: YOUR WITHDRAWED MONEY WILL BE CREDITED TO YOUR WALLET\033[0m")
                print("""
DIGITAL WITHDRAWL OPTIONS
1 - UPI
2 - NET BANKING
3 - WALLET
""")
                # Function to repeat the input if the user gives a wrong input
                def inp_wit_opti():
                    # Global variable for making the option viewalbe in the next row
                    global inp_wit_opt
                    inp_wit_opt = int(input(">>> "))
                inp_wit_opti()
                if inp_wit_opt in [1,2,3]:
                    if inp_wit_opt == 1:
                        # Making a bool to make sure deposit and withdraw do not coincide
                        withdrawl = True
                        upi()
                else:
                    print("\033[1;20;31m\nERROR: WRONG INPUT!\nTRYAGAIN!\033[0m\n")
                    inp_wit_opti()
            elif inp_mode == 3:
                print("_"*os.get_terminal_size().columns)
                import init_mainmenu
                init_mainmenu.mainmenu()
        else:
            print("\033[1;20;31m\nERROR: WRONG INPUT!\nTRYAGAIN!\033[0m\n") 
            inp_mod()