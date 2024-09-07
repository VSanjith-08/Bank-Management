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

def transaction_df():
    global df_transaction
    df_transaction = pd.read_csv("Database//transaction.csv",index_col = 0)
transaction_df()

import login
upi_passwd = login.inp_passwd
u_id = login.inp_uid

def upi():
    '''
    # Initials
    global upi_passwd,u_id
    upi_passwd = 'sanjith'
    u_id = 'sanjith'
    #withdrawl = init_transfermoney.withdrawl
    withdrawl = False'''
###################################################


    formula1 = f"select upi_id,cu_name from acc_details where uid = '{u_id}' and passwd = '{upi_passwd}'"
    mycursor.execute(formula1)
    retrived_upi_id = mycursor.fetchall()
    global payer_name
    payer_name = retrived_upi_id[0][1]
    global payer_upi
    payer_upi = retrived_upi_id[0][0]
    
    formula2 = "select upi_id from acc_details"
    mycursor.execute(formula2)
    retrived_payee_upi = mycursor.fetchall()

    # This is upi deposit
    if withdrawl == False:
        payee_upi = input("\nPAYEE'S UPI ADDRESS: ")
        # Checking the repeation of the payee's upi
        def payee_upi_checker(payee_upi):
            global stopper_upi
            for i in retrived_payee_upi:
                if payee_upi in i  and payee_upi != payer_upi:
                    stopper_upi = False
                    break
                else:
                    stopper_upi = True

        payee_upi_checker(payee_upi)

        if True:
            # Making only two attempts for the user to write the payee's upi id
            attempt = 2
            re_payee_upi = ""
            while stopper_upi:
                if attempt != 0:
                    print("\033[1;20;31m\n### ERROR: INCORRECT INPUT ###\033[0m")
                    re_payee_upi = input(f"YOU HAVE {attempt} MORE CHANCE\n\nRE-ENTER PAYEE'S UPI ADDRESS: ")
                    payee_upi_checker(re_payee_upi)
                else:
                    print("\033[1;20;31m\n### ERROR: INCORRECT INPUT ###\033[0m")
                    print("\033[1;20;31mYOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE MAIN MENU\033[0m")
                    print("_"*os.get_terminal_size().columns)
                    import init_mainmenu
                    init_mainmenu.mainmenu()
                attempt-=1
        # Assigning a permanant variable for the payee's upi id
        global Payees_upi_id
        if re_payee_upi != "":
            Payees_upi_id = re_payee_upi
        else:
            Payees_upi_id = payee_upi

        passwd_inp = input("\nLOGIN PASSWORD: ")
        stopper_passwd = True

        # Checking the passwd
        if passwd_inp == upi_passwd:
            stopper_passwd = False
        else:
            stopper_passwd = True

        if True:
            # Making only two attempts for the user to write the payee's upi id
            attempt = 2
            while stopper_passwd:
                if attempt != 0:
                    print("\033[1;20;31m\n### ERROR: INCORRECT INPUT ###\033[0m")
                    re_passwd_inp = input(f"YOU HAVE {attempt} MORE ATTEMPTS\n\nRE-ENTER YOUR CORRECT LOGIN PASSWORD: ")
                    if re_passwd_inp == upi_passwd:
                        stopper_passwd = False
                    else:
                        stopper_passwd = True
                else:
                    print("\033[1;20;31m\n### ERROR: INCORRECT INPUT ###\033[0m")
                    print("\033[1;20;31mYOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE MAIN MENU\033[0m")
                    print("_"*os.get_terminal_size().columns)
                    import init_mainmenu
                    init_mainmenu.mainmenu()
                attempt-=1

        # Amount of money to be transferred
        amt = int(input("\nAMOUNT OF MONEY TO BE TRANSFERRED: "))

        Bank_balance = df_transaction.loc[df_transaction.uid == u_id].loc[:,'balance'].tail(1).values.tolist()
        try:
            Bank_balance[0]
        except:
            Bank_balance = [0]

        def amt_check(amt):
            global stopper_amt
            if amt <= Bank_balance[0]:
                stopper_amt = False
            else:
                stopper_amt = True
        amt_check(amt)

        attempt = 2
        re_amt = ""
        while stopper_amt:
            if attempt != 0:
                print("\033[1;20;31m\n### ERROR: INSUFFICIENT BALENCE ###\033[0m")
                re_amt = int(input(f"YOU HAVE {attempt} MORE ATTEMPTS\n\nRE-ENTER THE CORRECT AMOUNT: "))
                amt_check(re_amt)

            else:
                print("\033[1;20;31m\n### ERROR: INCORRECT INPUT ###\033[0m")
                print("\033[1;20;31mYOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE TRANSACTIONS PAGE\033[0m")
                print("_"*os.get_terminal_size().columns)
                init_transfermoney()
                break
            attempt-=1
        
        global amount_deposit
        if re_amt != "":
            amount_deposit = re_amt
        else:
            amount_deposit = amt
        
        captcha()
        if captcha_pass:
            deposit_upi()
def captcha():
    print()
    import string
    import random
    lst = [1,2,3,4,5,6,7,8,9]+list(string.ascii_lowercase)+list(string.ascii_uppercase)
    random_sequence = random.choices(lst,k = 5)
    c1,c2,c3,c4,c5 = f'\033[3;44;93m{random_sequence[0]}\033[0m',f'\033[1;44;93m{random_sequence[1]}\033[0m',f'\033[4;44;93m{random_sequence[2]}\033[0m',f"\033[1;44;33m{random_sequence[3]}\033[0m",f'\033[9;44;93m{random_sequence[4]}\033[0m'
    set_str = {c1,c2,c3,c4,c5}
    str_captcha = ""
    lst_re = []
    for i in set_str:
        str_captcha += i
        lst_re +=[i]
    str = ""
    
    for i in lst_re:
        k = 0
        for j in list(i):
            if k == 10:
                str += j
                break
            k+=1

    print('\033[3;44;93m \033[0m'*7,"\n"+'\033[3;44;93m \033[0m'+str_captcha+'\033[3;44;93m \033[0m'+"\n"+'\033[3;44;93m \033[0m'*7)
    print("\nWHAT CODE IS IN THE ABOVE IMAGE?")
    inp = input(">>> ")
    global stopper_captcha
    stopper_captcha = True
    if str == inp:
        global captcha_pass
        captcha_pass = True
        stopper_captcha = False
    else:
        attempt = 2
        re_amt = ""
        while stopper_captcha:
            if attempt != 0:
                print("\033[1;20;31m\n### ERROR: INCORRECT INPUT ###\033[0m")
                inp = input(f"YOU HAVE {attempt} MORE ATTEMPTS\n\nRE-ENTER THE CORRECT CODE: ")
                if str == inp:
                    captcha_pass = True
                    stopper_captcha = False

            else:
                print("\033[1;20;31m\n### ERROR: INCORRECT INPUT ###\033[0m")
                print("\033[1;20;31mYOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE TRANSACTIONS PAGE\033[0m")
                print("_"*os.get_terminal_size().columns)
                init_transfermoney()
                break
            attempt-=1

def deposit_upi():
    formula = f"select uid,cu_name from acc_details where upi_id = '{Payees_upi_id}'"
    mycursor.execute(formula)
    tuple_of_name_uid = mycursor.fetchall()[0]
    payees_uid = tuple_of_name_uid[0]
    payee_name = tuple_of_name_uid[1]

    Bank_balance_after_deposit1 = df_transaction.loc[df_transaction.uid == u_id].loc[:,'balance'].tail(1).values.tolist()
    Bank_balance_after_deposit2 = df_transaction.loc[df_transaction.uid == payees_uid].loc[:,'balance'].tail(1).values.tolist()
    
    try:
        Bank_balance_after_deposit1[0]
    except:
        Bank_balance_after_deposit1=[0]

    try:
        Bank_balance_after_deposit2[0]
    except:
        Bank_balance_after_deposit2=[0]

    def transact_id():
        transact_no = df_transaction.loc[:,'transact_id'].tail(1).values
        global transaction_id
        transaction_id = transact_no.tolist()[0]+1
    transact_id()

    index = df_transaction.tail(1).index.values.tolist()[0]+1
    df_transaction.loc[index] = [u_id,'upi','debit',transaction_id,payer_upi,Payees_upi_id,amount_deposit,0,Bank_balance_after_deposit1[0]-amount_deposit]
    df_transaction.loc[index+1] = [payees_uid,'upi','credit',transaction_id,payer_upi,Payees_upi_id,0,amount_deposit,Bank_balance_after_deposit2[0]+amount_deposit]
    df_transaction.to_csv('Database//transaction.csv')
    print()
    print("\033[1;49;93m=\033[0m"*33)
    print("\033[1;49;93m|::: TRANSACTION SUCCESSFULL :::|\033[0m")
    print("\033[1;49;93m=\033[0m"*33)
    print("\033[1;20;96mUPI TRANSACTION ID: \033[0m")
    print(f"\033[1;20;34m{transaction_id}\033[0m")
    print("\033[1;20;96mAMOUNT TRANSFERRED: \033[0m")
    print(f"\033[1;20;34m{amount_deposit}\033[0m")
    print(f"\033[1;20;96mTO: {payee_name} (JUST BANK ACCOUNT)\033[0m")
    print(f"\033[1;20;34m{Payees_upi_id}\033[0m")
    print(f"\033[1;20;96mFROM: {payer_name} (JUST BANK ACCOUNT)\033[0m")
    print(f"\033[1;20;34m{payer_upi}\033[0m")
    terminal_width = os.get_terminal_size().columns
    print("_"*terminal_width)
    print()

######################
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