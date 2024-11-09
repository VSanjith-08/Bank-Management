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
    global df_wallet
    df_wallet = pd.read_csv("Database//wallet.csv",index_col = 0)
transaction_df()

import login
upi_passwd = login.inp_passwd
u_id = login.inp_uid

def upi():

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
                    print("\n### ERROR: INCORRECT INPUT ###")
                    re_payee_upi = input(f"YOU HAVE {attempt} MORE CHANCE\n\nRE-ENTER PAYEE'S UPI ADDRESS: ")
                    payee_upi_checker(re_payee_upi)
                else:
                    print("\n### ERROR: INCORRECT INPUT ###")
                    print("YOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE MAIN MENU")
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
                    print("\n### ERROR: INCORRECT INPUT ###")
                    re_passwd_inp = input(f"YOU HAVE {attempt} MORE ATTEMPTS\n\nRE-ENTER YOUR CORRECT LOGIN PASSWORD: ")
                    if re_passwd_inp == upi_passwd:
                        stopper_passwd = False
                    else:
                        stopper_passwd = True
                else:
                    print("\n### ERROR: INCORRECT INPUT ###")
                    print("YOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE MAIN MENU")
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
                print("\n### ERROR: INSUFFICIENT BALENCE ###")
                re_amt = int(input(f"YOU HAVE {attempt} MORE ATTEMPTS\n\nRE-ENTER THE CORRECT AMOUNT: "))
                amt_check(re_amt)

            else:
                print("\n### ERROR: INCORRECT INPUT ###")
                print("YOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE TRANSACTIONS PAGE")
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
    
    if withdrawl:
        formula = f"select acc_no,ifsc from acc_details where passwd = '{upi_passwd}' and uid = '{u_id}'"
        mycursor.execute(formula)
        retrived_accno_ifsc_codes = mycursor.fetchall()
        ifsc_payer = retrived_accno_ifsc_codes[0][1]
        acc_no_payer = retrived_accno_ifsc_codes[0][0]
        acc_payer_inp = int(input("\nACCOUNT NUMBER: "))

        if acc_payer_inp == acc_no_payer:
            stopper_withdrawl = False
        else:
            stopper_withdrawl = True

        attempt = 2
        while stopper_withdrawl:
            if attempt != 0:
                print("\n### ERROR: INCORRECT ACCOUNT NUMBER ###")
                acc_payer_inp = int(input(f"YOU HAVE {attempt} MORE ATTEMPTS\n\nRE-ENTER YOUR CORRECT ACCOUNT NUMBER: "))
                if acc_payer_inp == acc_no_payer:
                    stopper_withdrawl = False

            else:
                print("\n### ERROR: INCORRECT ACCOUNT NUMBER ###")
                print("YOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE TRANSACTIONS PAGE")
                print("_"*os.get_terminal_size().columns)
                init_transfermoney()
                break
            attempt-=1

        ifsc_payer_inp = input("\nIFSC CODE: ")
        
        if ifsc_payer_inp == ifsc_payer:
            stopper_ifsc = False
        else:
            stopper_ifsc == True
        
        attempt = 2
        while stopper_ifsc:
            if attempt != 0:
                print("\n### ERROR: INCORRECT IFSC CODE ###")
                ifsc_payer_inp = input(f"YOU HAVE {attempt} MORE ATTEMPTS\n\nRE-ENTER YOUR CORRECT IFSC CODE: ")
                if ifsc_payer_inp == ifsc_payer:
                    stopper_ifsc = False

            else:
                print("\n### ERROR: INCORRECT IFSC CODE ###")
                print("YOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE TRANSACTIONS PAGE")
                print("_"*os.get_terminal_size().columns)
                init_transfermoney()
                break
            attempt-=1
        
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
                    print("\n### ERROR: INCORRECT INPUT ###")
                    re_passwd_inp = input(f"YOU HAVE {attempt} MORE ATTEMPTS\n\nRE-ENTER YOUR CORRECT LOGIN PASSWORD: ")
                    if re_passwd_inp == upi_passwd:
                        stopper_passwd = False
                    else:
                        stopper_passwd = True
                else:
                    print("\n### ERROR: INCORRECT INPUT ###")
                    print("YOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE MAIN MENU")
                    print("_"*os.get_terminal_size().columns)
                    import init_mainmenu
                    init_mainmenu.mainmenu()
                attempt-=1

        amt = int(input("\nAMOUNT OF MONEY TO BE WITHDREW: "))

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
                print("\n### ERROR: INSUFFICIENT BALENCE ###")
                re_amt = int(input(f"YOU HAVE {attempt} MORE ATTEMPTS\n\nRE-ENTER THE CORRECT AMOUNT: "))
                amt_check(re_amt)

            else:
                print("\n### ERROR: INCORRECT INPUT ###")
                print("YOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE TRANSACTIONS PAGE")
                print("_"*os.get_terminal_size().columns)
                init_transfermoney()
                break
            attempt-=1
        
        global amount_withdraw
        if re_amt != "":
            amount_withdraw = re_amt
        else:
            amount_withdraw = amt
        
        captcha()
        if captcha_pass:
            withdrawl_upi()

def withdrawl_upi():
    df_wallet = pd.read_csv("Database//wallet.csv",index_col = 0)
    Bank_balance_transactiontable_afterwithdrawn = df_transaction.loc[df_transaction.uid == u_id].loc[:,'balance'].tail(1).values.tolist()
    Bank_balence_wallettable_afterwithdrawn = df_wallet[df_wallet.uid == u_id].loc[:,'balance'].tail(1).values.tolist()
    
    try:
        Bank_balance_transactiontable_afterwithdrawn[0]
    except:
        Bank_balance_transactiontable_afterwithdrawn=[0]
    
    try:
        Bank_balence_wallettable_afterwithdrawn[0]
    except:
        Bank_balence_wallettable_afterwithdrawn=[0]
    
    def transact_id():
        transact_no1 = df_transaction.loc[:,'transact_id'].tail(1).values
        transact_no2 = df_wallet.loc[:,'transact_id'].tail(1).values

        try:
            transact_no1.tolist()[0]
        except:
            transact_no1 = np.array([0])

        try:
            transact_no2.tolist()[0]
        except:
            transact_no2 = np.array([0])

        global transaction_id
        if transact_no1>transact_no2:
            transaction_id = transact_no1.tolist()[0]+1
        else:
            transaction_id = transact_no2.tolist()[0]+1
            
    transact_id()

    index_transaction = df_transaction.tail(1).index.values.tolist()[0]+1
    index_wallet = df_wallet.tail(1).index.values.tolist()[0]+1

    df_transaction.loc[index_transaction] = [u_id,'upi','debit',transaction_id,payer_upi,"wallet",0,amount_withdraw,Bank_balance_transactiontable_afterwithdrawn[0]-amount_withdraw,datetime.now()]
    df_wallet.loc[index_wallet] = [u_id,'upi','credit',transaction_id+1,amount_withdraw,0,Bank_balence_wallettable_afterwithdrawn[0]+amount_withdraw,datetime.now()]
    
    df_transaction.to_csv('Database//transaction.csv')
    df_wallet.to_csv('Database//wallet.csv')

    print()
    print("="*33)
    print("|::: TRANSACTION SUCCESSFULL :::|")
    print("="*33)
    print("TRANSACTION TYPE: ")
    print(f"WITHDRAWL")
    print("UPI TRANSACTION ID: ")
    print(f"{transaction_id}")
    print("AMOUNT TRANSFERRED: ")
    print(f"{amount_withdraw}")
    print(f"FROM: {payer_name} (JUST BANK ACCOUNT)")
    print(f"{payer_upi}")
    terminal_width = os.get_terminal_size().columns
    print("_"*terminal_width)
    print()


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
        transact_no1 = df_transaction.loc[:,'transact_id'].tail(1).values
        transact_no2 = df_wallet.loc[:,'transact_id'].tail(1).values

        try:
            transact_no1.tolist()[0]
        except:
            transact_no1 = np.array([0])

        try:
            transact_no2.tolist()[0]
        except:
            transact_no2 = np.array([0])

        global transaction_id
        if transact_no1>transact_no2:
            transaction_id = transact_no1.tolist()[0]+1
        else:
            transaction_id = transact_no2.tolist()[0]+1
            
    transact_id()

    index = df_transaction.tail(1).index.values.tolist()[0]+1
    df_transaction.loc[index] = [u_id,'upi','debit',transaction_id,payer_upi,Payees_upi_id,amount_deposit,0,Bank_balance_after_deposit1[0]-amount_deposit,datetime.now()]
    df_transaction.loc[index+1] = [payees_uid,'upi','credit',transaction_id+1,payer_upi,Payees_upi_id,0,amount_deposit,Bank_balance_after_deposit2[0]+amount_deposit,datetime.now()]
    
    df_transaction.to_csv('Database//transaction.csv')
    print()
    print("="*33)
    print("|::: TRANSACTION SUCCESSFULL :::|")
    print("="*33)
    print("TRANSACTION TYPE: ")
    print(f"DEPOSIT")
    print("UPI TRANSACTION ID: ")
    print(f"{transaction_id}")
    print("AMOUNT TRANSFERRED: ")
    print(f"{amount_deposit}")
    print(f"TO: {payee_name} (JUST BANK ACCOUNT)")
    print(f"{Payees_upi_id}")
    print(f"FROM: {payer_name} (JUST BANK ACCOUNT)")
    print(f"{payer_upi}")
    terminal_width = os.get_terminal_size().columns
    print("_"*terminal_width)
    print()

def wallet():
    formula = f"select acc_no,ifsc from acc_details"
    mycursor.execute(formula)
    retrived_accno_ifsc_codes = mycursor.fetchall()

    formula2 = f"select acc_no,ifsc,cu_name from acc_details where passwd = '{upi_passwd}' and uid = '{u_id}'"
    mycursor.execute(formula2)
    retrived_accno_ifsc_codes2 = mycursor.fetchall()
    acc_no_payer = retrived_accno_ifsc_codes2[0][0]
    global payer_name
    payer_name = retrived_accno_ifsc_codes2[0][2]
    global acc_payee_inp
    acc_payee_inp = int(input("\nPAYEE'S ACCOUNT NUMBER: "))

    for i in retrived_accno_ifsc_codes:
        if i[0]==acc_payee_inp and i[0] != acc_no_payer:
            stopper_deposit = False
            break
        else:
            stopper_deposit = True

    attempt = 2
    while stopper_deposit:
        if attempt != 0:
            print("\n### ERROR: INCORRECT ACCOUNT NUMBER ###")
            acc_payee_inp = int(input(f"YOU HAVE {attempt} MORE ATTEMPTS\n\nRE-ENTER YOUR CORRECT ACCOUNT NUMBER: "))
            for i in retrived_accno_ifsc_codes:
                if i[0]==acc_payee_inp and i[0] != acc_no_payer:
                    stopper_deposit = False
                    break
                else:
                    stopper_deposit = True

        else:
            print("\n### ERROR: INCORRECT ACCOUNT NUMBER ###")
            print("YOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE TRANSACTIONS PAGE")
            print("_"*os.get_terminal_size().columns)
            init_transfermoney()
            break
        attempt-=1

    for i in retrived_accno_ifsc_codes:
        if i[0] == acc_payee_inp:
            ifsc_payee = i[1]
    
    ifsc_payee_inp = input("\nPAYEE'S IFSC CODE: ")
    
    if ifsc_payee_inp == ifsc_payee:
        stopper_ifsc = False
    else:
        stopper_ifsc = True
    
    attempt = 2
    while stopper_ifsc:
        if attempt != 0:
            print("\n### ERROR: INCORRECT IFSC CODE ###")
            ifsc_payee_inp = input(f"YOU HAVE {attempt} MORE ATTEMPTS\n\nRE-ENTER THE CORRECT IFSC CODE: ")
            if ifsc_payee_inp == ifsc_payee:
                stopper_ifsc = False
            else:
                stopper_ifsc == True

        else:
            print("\n### ERROR: INCORRECT IFSC CODE ###")
            print("YOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE TRANSACTIONS PAGE")
            print("_"*os.get_terminal_size().columns)
            init_transfermoney()
            break
        attempt-=1
    
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
                print("\n### ERROR: INCORRECT INPUT ###")
                re_passwd_inp = input(f"YOU HAVE {attempt} MORE ATTEMPTS\n\nRE-ENTER YOUR CORRECT LOGIN PASSWORD: ")
                if re_passwd_inp == upi_passwd:
                    stopper_passwd = False
                else:
                    stopper_passwd = True
            else:
                print("\n### ERROR: INCORRECT INPUT ###")
                print("YOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE MAIN MENU")
                print("_"*os.get_terminal_size().columns)
                import init_mainmenu
                init_mainmenu.mainmenu()
            attempt-=1

    amt = int(input("\nAMOUNT OF MONEY TO BE TRANSFERRED: "))

    df_wallet = pd.read_csv("Database//wallet.csv",index_col = 0)

    Wallet_balance = df_wallet.loc[df_wallet.uid == u_id].loc[:,'balance'].tail(1).values.tolist()
    try:
        Wallet_balance[0]
    except:
        Wallet_balance = [0]

    def amt_check(amt):
        global stopper_amt
        if amt <= Wallet_balance[0]:
            stopper_amt = False
        else:
            stopper_amt = True
    amt_check(amt)

    attempt = 2
    re_amt = ""
    while stopper_amt:
        if attempt != 0:
            print("\n### ERROR: INSUFFICIENT BALENCE ###")
            re_amt = int(input(f"YOU HAVE {attempt} MORE ATTEMPTS\n\nRE-ENTER THE CORRECT AMOUNT: "))
            amt_check(re_amt)

        else:
            print("\n### ERROR: INCORRECT INPUT ###")
            print("YOU'RE INPUTS ARE OVER, WE'RE DIRECTING YOU TO THE TRANSACTIONS PAGE")
            print("_"*os.get_terminal_size().columns)
            init_transfermoney()
            break
        attempt-=1
    
    global amount_transferred
    if re_amt != "":
        amount_transferred = re_amt
    else:
        amount_transferred = amt
    
    captcha()
    if captcha_pass:
        deposit_wallet()


def deposit_wallet():
    formula = f"select cu_name from acc_details where acc_no = '{acc_payee_inp}'"
    mycursor.execute(formula)
    tuple_of_name = mycursor.fetchall()[0]
    payee_name = tuple_of_name[0]

    df_wallet = pd.read_csv("Database//wallet.csv",index_col = 0)
    Bank_balance_transactiontable_afterdeposit = df_transaction.loc[df_transaction.uid == u_id].loc[:,'balance'].tail(1).values.tolist()
    Bank_balence_wallettable_afterwithdrawn = df_wallet[df_wallet.uid == u_id].loc[:,'balance'].tail(1).values.tolist()
    
    try:
        Bank_balance_transactiontable_afterdeposit[0]
    except:
        Bank_balance_transactiontable_afterdeposit=[0]

    try:
        Bank_balence_wallettable_afterwithdrawn[0]
    except:
        Bank_balence_wallettable_afterwithdrawn=[0]
    
    def transact_id():
        transact_no1 = df_transaction.loc[:,'transact_id'].tail(1).values
        transact_no2 = df_wallet.loc[:,'transact_id'].tail(1).values

        try:
            transact_no1.tolist()[0]
        except:
            transact_no1 = np.array([0])

        try:
            transact_no2.tolist()[0]
        except:
            transact_no2 = np.array([0])

        global transaction_id
        if transact_no1>transact_no2:
            transaction_id = transact_no1.tolist()[0]+1
        else:
            transaction_id = transact_no2.tolist()[0]+1

    transact_id()

    index_transaction = df_transaction.tail(1).index.values.tolist()[0]+1
    index_wallet = df_wallet.tail(1).index.values.tolist()[0]+1

    df_transaction.loc[index_transaction] = [u_id,'wallet','credit',transaction_id,"wallet",acc_payee_inp,amount_transferred,0,Bank_balance_transactiontable_afterdeposit[0]+amount_transferred,datetime.now()]
    df_wallet.loc[index_wallet] = [u_id,'wallet','debit',transaction_id+1,0,amount_transferred,Bank_balence_wallettable_afterwithdrawn[0]-amount_transferred,datetime.now()]

    df_transaction.to_csv('Database//transaction.csv')
    df_wallet.to_csv('Database//wallet.csv')

    print()
    print("="*33)
    print("|::: TRANSACTION SUCCESSFULL :::|")
    print("="*33)
    print("TRANSACTION TYPE: ")
    print(f"DEPOSIT")
    print("TRANSACTION ID: ")
    print(f"{transaction_id}")
    print("AMOUNT TRANSFERRED: ")
    print(f"{amount_transferred}")
    print(f"TO: {payee_name} (JUST BANK ACCOUNT)")
    print(f"{acc_payee_inp}")
    print(f"FROM: {payer_name} (JUST BANK ACCOUNT)")
    print(f"WALLET")
    terminal_width = os.get_terminal_size().columns
    print("_"*terminal_width)
    print()

######################
# Init for this module
def init_transfermoney():
        print("\n"+"="*29)
        print("|::: TRANSFER MONEY PAGE :::|")
        print("="*29)
        print("""
CHOOSE YOUR MODE OF TRANSACTION
1 - SEND MONEY           
2 - WITHDRAW MONEY
3 - MAIN MENU
""")
        
        inp_mode = int(input(">>> "))
        while inp_mode not in [1,2,3]:
            print("\nERROR: WRONG INPUT!\nTRYAGAIN!") 
            inp_mode = int(input(">>> "))

        if inp_mode == 1:
            # Making a bool to make sure deposit and withdraw do not coincide
            global withdrawl
            withdrawl = False
            print("""
DIGITAL DEPOSIT OPTIONS
1 - UPI
2 - WALLET
3 - MAIN MENU
""")
            inp_dep_opt = int(input(">>> "))
            while inp_dep_opt not in [1,2,3]:
                print("\nERROR: WRONG INPUT!\nTRYAGAIN!")
                inp_dep_opt = int(input(">>> "))

            if inp_dep_opt == 1:
                upi()
            if inp_dep_opt == 2:
                wallet()
            if inp_dep_opt == 3:
                print("_"*os.get_terminal_size().columns)
                import init_mainmenu
                init_mainmenu.mainmenu()

        elif inp_mode == 2:
            withdrawl = True
            print("\nNOTE: YOUR WITHDRAWED MONEY WILL BE CREDITED TO YOUR WALLET")
            print()
            print("""
DIGITAL WITHDRAWL OPTIONS
1 - UPI
2 - MAIN MENU
""")

            inp_wit_opt = int(input(">>> "))
            while inp_wit_opt not in [1,2]:
                print("\nERROR: WRONG INPUT!\nTRYAGAIN!")
                inp_wit_opt = int(input(">>> "))

            if inp_wit_opt == 1:
                # Making a bool to make sure deposit and withdraw do not coincide
                withdrawl = True
                upi()
            if inp_wit_opt == 2:
                print("_"*os.get_terminal_size().columns)
                import init_mainmenu
                init_mainmenu.mainmenu()

        elif inp_mode == 3:
            print("_"*os.get_terminal_size().columns)
            import init_mainmenu
            init_mainmenu.mainmenu()