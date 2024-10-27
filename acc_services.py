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

df_wallet = pd.read_csv("Database//wallet.csv",index_col = 0)
df_transaction = pd.read_csv("Database//transaction.csv",index_col = 0)

def bank_bal():
    import login
    Bank_balance_transactiontable_afterdeposit = df_transaction.loc[df_transaction.uid == login.inp_uid].loc[:,'balance'].tail(1).values.tolist()
    Bank_balence_wallettable_afterwithdrawn = df_wallet[df_wallet.uid == login.inp_uid].loc[:,'balance'].tail(1).values.tolist()
    
    if sum(Bank_balance_transactiontable_afterdeposit) == 0:
        Bank_balance_transactiontable_afterdeposit = ["0"]
    if sum(Bank_balence_wallettable_afterwithdrawn) == 0:
        Bank_balence_wallettable_afterwithdrawn = ["0"]
    
    print()
    print("="*31)
    print("|::: ACCOUNT BALENCE CHECK :::|")
    print("="*31)
    print("ACCOUNT BALENCE")
    print(f"₹ {Bank_balance_transactiontable_afterdeposit[0]}")
    print("WALLET BALENCE")

    print(f"₹ {Bank_balence_wallettable_afterwithdrawn[0]}")
    terminal_width = os.get_terminal_size().columns
    print("_"*terminal_width)
    print()

def mini_statement():
    import login
    print()
    print("="*24)
    print("|::: MINI STATEMENT :::|")
    print("="*24)
    print()
    statement = df_transaction.loc[df_transaction.uid == login.inp_uid].loc[:,['mode','transact_type','transact_id','from','to','credit','debit','balance',"timestamp"]]
    print(statement.tail(10))
    print()
    Bank_balance_transactiontable_afterdeposit = df_transaction.loc[df_transaction.uid == login.inp_uid].loc[:,'balance'].tail(1).values.tolist()
    print("ACCOUNT BALENCE")
    print(f"₹ {Bank_balance_transactiontable_afterdeposit[0]}")
    terminal_width = os.get_terminal_size().columns
    print("_"*terminal_width)
    print()

def acc_statement():
    import login
    print()
    print("="*27)
    print("|::: ACCOUNT STATEMENT :::|")
    print("="*27)
    print()    
    statement = df_transaction.loc[df_transaction.uid == login.inp_uid].loc[:,['mode','transact_type','transact_id','from','to','credit','debit','balance',"timestamp"]]
    print(statement)
    print()
    Bank_balance_transactiontable_afterdeposit = df_transaction.loc[df_transaction.uid == login.inp_uid].loc[:,'balance'].tail(1).values.tolist()
    print("ACCOUNT BALENCE")
    print(f"₹ {Bank_balance_transactiontable_afterdeposit[0]}")
    terminal_width = os.get_terminal_size().columns
    print("_"*terminal_width)
    print()

def acc_details():
    import login
    formula = f"select * from acc_details where uid = '{login.inp_uid}'"
    mycursor.execute(formula)
    myresult = mycursor.fetchall()
    details = list(myresult[0][0:9])
    print()
    print("="*25)
    print("|::: ACCOUNT DETAILS :::|")
    print("="*25)
    print()
    acc_details = pd.DataFrame(details,index=["NAME","UPI ID",'ACCOUNT NUMBER','IFSC CODE','DATE OF OPENING',"UID",'STATE','DOB','GENDER'],columns=['<=>> A JUSTBANK ACCOUNT <<=>'])
    print(acc_details)
    terminal_width = os.get_terminal_size().columns
    print("_"*terminal_width)
    print()
import login
formula = f"select passwd from acc_details where uid = '{login.inp_uid}'"
mycursor.execute(formula)
myresult = mycursor.fetchall()


def reset_passwd():
    print()
    global n_passwd
    n_passwd = input("NEW PASSWORD: ")
    caps,small,digit,space,spc = False,False,False,False,False
    for i in n_passwd:
        if i.isupper():
            caps = True
        if i.islower():
            small = True
        if i.isspace():
            space = True
        if i.isdigit():
            digit = True
        if [i.isdigit(),i.isalpha(),i.isspace()] == [False,False,False]:
            spc = True
    if n_passwd == myresult[0][0]:
        print("ERROR: YOUR NEW PASSWORD IS AS YOUR OLD PASSWORD")
        reset_passwd()
    elif [caps,small,digit,space,spc] != [True,True,True,False,True]:
        
        print("\nERROR: WRONG INPUT!")
        print("YOUR PASSWORD SHOULD HAVE ATLEAST ONE CAPITAL,SMALL,DIGIT,SPACE AND SPECIAL-CHARACTER.\n")
        reset_passwd()
    else:
        repeat()
    formula1 = f"update acc_details set passwd = '{n_passwd}' where uid = '{login.inp_uid}'"
    mycursor.execute(formula1)
    mydb.commit()

def repeat():
    global c_passwd
    c_passwd = input("REPEAT PASSWORD: ")
    while n_passwd != c_passwd:
        print("\nERROR: PASSWORDS DOES NOT MATCH\n")
        reset_passwd()
        break

def init_accser():
    print("\n"+"="*31)
    print("|::: ACCOUNT SERVICES PAGE :::|")
    print("="*31)
    print("""
CHOOSE THE TYPE OF ACCOUNT SERVICE
          
1 - BANK AND WALLET BALENCE      
          
2 - MINI STATEMENT
          
3 - ACCOUNT STATEMENT
          
4 - MY ACCOUNT DETAILS
          
5 - RESET LOGIN PIN

6 - MAIN MENU
""")
    # Function to repeat the input if the user gives a wrong input
    inp_mode = int(input(">>> "))
    def imp_mod():
        global inp_mode
        inp_mode = int(input(">>> "))

    if inp_mode in [1,2,3,4,5,6]:
        if inp_mode == 1:
            bank_bal()
        if inp_mode == 2:
            mini_statement()
        if inp_mode == 3:
            acc_statement()
        if inp_mode == 4:
            acc_details()
        if inp_mode == 5:
            reset_passwd()
            terminal_width = os.get_terminal_size().columns
            print("_"*terminal_width)
            print()
        if inp_mode == 6:
            import init_mainmenu
            terminal_width = os.get_terminal_size().columns
            print("_"*terminal_width)
            print()
            init_mainmenu.mainmenu()
    else:
        imp_mod()